#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


def workspace_root() -> Path:
    return Path(os.environ.get("NEO_WORKSPACE_ROOT", Path(__file__).resolve().parents[3]))


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True)


def require_ffmpeg() -> None:
    missing = [name for name in ("ffmpeg", "ffprobe") if shutil.which(name) is None]
    if missing:
        raise SystemExit(
            "Missing required command(s): " + ", ".join(missing) + ". Install ffmpeg and rerun."
        )


def ffprobe_duration(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
    ).strip()
    return float(out)


def srt_time(seconds: float) -> str:
    if seconds < 0:
        seconds = 0
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, milli = divmod(rem, 1000)
    return f"{h:02}:{m:02}:{s:02},{milli:03}"


def parse_srt_time(value: str) -> float:
    match = re.fullmatch(r"(\d\d):(\d\d):(\d\d),(\d\d\d)", value.strip())
    if not match:
        raise ValueError(f"Invalid SRT timestamp: {value}")
    hours, minutes, seconds, millis = (int(part) for part in match.groups())
    return hours * 3600 + minutes * 60 + seconds + millis / 1000


def parse_srt_entries(path: Path) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    blocks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8").strip())
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 3 or " --> " not in lines[1]:
            continue
        start, end = lines[1].split(" --> ", 1)
        entries.append({"start": parse_srt_time(start), "end": parse_srt_time(end), "text": " ".join(lines[2:])})
    return entries


def escape_subtitle_path(path: Path) -> str:
    value = str(path.resolve())
    return value.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\\'")


@dataclass
class Beat:
    index: int
    video: Path
    srt: Path
    json_path: Path
    subtitled: Path


def discover_beats(episode_dir: Path) -> list[Path]:
    exact = [episode_dir / f"beat{idx}.mp4" for idx in range(1, 5)]
    if all(path.exists() for path in exact):
        return exact

    candidates: list[Path] = []
    for pattern in ("beat*.mp4", "Beat*.mp4", "*beat*.mp4", "*Beat*.mp4"):
        candidates.extend(episode_dir.glob(pattern))
    excluded = ("sub", "final", "concat", "subtitle", "seedance", "regen")
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in sorted(candidates):
        low = path.name.lower()
        if any(word in low for word in excluded):
            continue
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(path)
    return unique[:4]


def subtitle_entries_from_words(seg: object) -> list[dict[str, object]]:
    words = [word for word in getattr(seg, "words", None) or [] if getattr(word, "word", "").strip()]
    if not words:
        text = getattr(seg, "text", "").strip()
        if not text:
            return []
        return [{"start": getattr(seg, "start"), "end": getattr(seg, "end"), "text": text}]

    entries: list[dict[str, object]] = []
    current_words: list[object] = []
    max_chars = 34
    max_duration = 2.6
    sentence_end = re.compile(r"[.!?]$|[.!?][\"']$")

    def flush() -> None:
        if not current_words:
            return
        text = " ".join(getattr(word, "word").strip() for word in current_words).strip()
        text = re.sub(r"\s+([,.!?;:])", r"\1", text)
        end = getattr(current_words[-1], "end")
        if len(text) <= 18 and end - getattr(current_words[0], "start") > 2.6:
            end = getattr(current_words[0], "start") + 2.6
        entries.append(
            {
                "start": getattr(current_words[0], "start"),
                "end": end,
                "text": text,
            }
        )
        current_words.clear()

    for word in words:
        word_text = getattr(word, "word").strip()
        current_words.append(word)
        text = " ".join(getattr(item, "word").strip() for item in current_words).strip()
        text = re.sub(r"\s+([,.!?;:])", r"\1", text)
        duration = getattr(current_words[-1], "end") - getattr(current_words[0], "start")
        if sentence_end.search(word_text) or len(text) >= max_chars or duration >= max_duration:
            flush()
    flush()
    return entries


def transcribe_to_srt(video: Path, srt: Path, json_path: Path, model_size: str, language: str | None) -> None:
    try:
        from faster_whisper import WhisperModel
    except Exception as exc:
        raise SystemExit(
            "Python package faster-whisper is required. Run setup_subtitle_env.sh or install requirements-subtitles.txt."
        ) from exc

    model = WhisperModel(model_size, device="auto", compute_type="auto")
    kwargs: dict[str, object] = {"vad_filter": True, "word_timestamps": True}
    if language:
        kwargs["language"] = language
    segments, info = model.transcribe(str(video), **kwargs)
    payload: dict[str, object] = {"language": getattr(info, "language", None), "segments": []}
    lines: list[str] = []
    subtitle_index = 1
    for seg_id, seg in enumerate(segments, 1):
        text = seg.text.strip()
        words_payload = [
            {"start": word.start, "end": word.end, "word": word.word.strip()}
            for word in (getattr(seg, "words", None) or [])
            if word.word.strip()
        ]
        entries = subtitle_entries_from_words(seg)
        payload["segments"].append(
            {
                "id": seg_id,
                "start": seg.start,
                "end": seg.end,
                "text": text,
                "words": words_payload,
                "subtitles": entries,
            }
        )
        for entry in entries:
            entry_text = str(entry["text"]).strip()
            if entry_text:
                lines.extend(
                    [
                        str(subtitle_index),
                        f"{srt_time(float(entry['start']))} --> {srt_time(float(entry['end']))}",
                        entry_text,
                        "",
                    ]
                )
                subtitle_index += 1
    json_path.parent.mkdir(parents=True, exist_ok=True)
    srt.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    srt.write_text("\n".join(lines), encoding="utf-8")


def escape_drawtext_value(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace(":", "\\:").replace("'", r"\'").replace("%", r"\%")


def escape_drawtext_path(path: Path) -> str:
    return escape_drawtext_value(path.resolve())


def drawtext_filter(entry: dict[str, object], text_file: Path, font_size: int, bottom_margin: int) -> str:
    start = float(entry["start"])
    end = float(entry["end"])
    y_expr = f"h-text_h-{bottom_margin}"
    return (
        "drawtext="
        f"textfile='{escape_drawtext_path(text_file)}':"
        "fontcolor=white:"
        f"fontsize={font_size}:"
        "borderw=2:bordercolor=black:"
        "x=(w-text_w)/2:"
        f"y={y_expr}:"
        f"enable='between(t,{start:.3f},{end:.3f})'"
    )


def burn_subtitles(video: Path, srt: Path, output: Path, font_size: int, bottom_margin: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    text_dir = output.parent / "subs_auto" / "drawtext"
    text_dir.mkdir(parents=True, exist_ok=True)
    filters = [
        "scale=1080:1920:force_original_aspect_ratio=decrease",
        "pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
    ]
    for index, entry in enumerate(parse_srt_entries(srt), 1):
        text_file = text_dir / f"{output.stem}-{index}.txt"
        text_file.write_text(str(entry["text"]), encoding="utf-8")
        filters.append(drawtext_filter(entry, text_file, font_size, bottom_margin))
    run(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(video),
            "-vf",
            ",".join(filters),
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            str(output),
        ]
    )


def concat_videos(videos: list[Path], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    concat_file = output.parent / "concat_subtitled.txt"
    concat_file.write_text("".join(f"file '{path.resolve()}'\n" for path in videos), encoding="utf-8")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file), "-c", "copy", str(output)])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Transcribe beat videos, burn subtitles, and export an Empire of Dust episode final."
    )
    parser.add_argument("--episode-dir", type=Path, required=True, help="Episode folder under workspace Files.")
    parser.add_argument("--output", type=Path, help="Final mp4 path. Defaults to '<episode>/final_subtitled.mp4'.")
    parser.add_argument("--model", default="small", help="faster-whisper model size, e.g. tiny/base/small/medium.")
    parser.add_argument("--language", default="en", help="Speech language; use empty string for auto-detect.")
    parser.add_argument("--font-size", type=int, default=15, help="ASS subtitle font size for 1080x1920 output.")
    parser.add_argument("--bottom-margin", type=int, default=180, help="Vertical bottom margin for 1080x1920 Shorts safe area.")
    parser.add_argument("--skip-transcribe", action="store_true", help="Use existing SRT files if present.")
    args = parser.parse_args()

    require_ffmpeg()
    episode_dir = args.episode_dir.resolve()
    videos = discover_beats(episode_dir)
    if len(videos) != 4:
        raise SystemExit(f"Expected 4 beat videos in {episode_dir}, found {len(videos)}: {[path.name for path in videos]}")

    beats: list[Beat] = []
    for idx, video in enumerate(videos, 1):
        beats.append(
            Beat(
                index=idx,
                video=video,
                srt=episode_dir / "subs_auto" / f"beat{idx}.srt",
                json_path=episode_dir / "whisper_auto" / f"beat{idx}.json",
                subtitled=episode_dir / f"beat{idx}_subtitled.mp4",
            )
        )

    language = args.language or None
    for beat in beats:
        if not args.skip_transcribe or not beat.srt.exists():
            transcribe_to_srt(beat.video, beat.srt, beat.json_path, args.model, language)
        if beat.srt.read_text(encoding="utf-8").strip():
            burn_subtitles(beat.video, beat.srt, beat.subtitled, args.font_size, args.bottom_margin)
        else:
            beat.subtitled = beat.video

    output = args.output or (episode_dir / "final_subtitled.mp4")
    concat_videos([beat.subtitled for beat in beats], output)
    duration = ffprobe_duration(output)
    print(json.dumps({"output": str(output), "duration": duration, "beats": [str(beat.video) for beat in beats]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
