#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path
import os


def workspace_root() -> Path:
    return Path(os.environ.get("NEO_WORKSPACE_ROOT", Path(__file__).resolve().parents[3]))


PIPELINE_FILES_ROOT = workspace_root() / "storage/files/empire-of-dust-youtube-pipeline"
MASTER_PATH = PIPELINE_FILES_ROOT / "scripts/empire-of-dust-retention-20ep-dense-master.md"
EPISODE_DIR = PIPELINE_FILES_ROOT / "scripts/empire-of-dust-retention-20ep-dense"
OUTPUT_ROOT = PIPELINE_FILES_ROOT / "production/Empire of Dust"


def load_global_suffix(master_text: str) -> str:
    marker = "## Episode 1"
    if marker not in master_text:
        raise ValueError(f"Could not find {marker!r} in master file.")
    prefix = master_text.split(marker, 1)[0].rstrip()
    if prefix.startswith("# Empire of Dust\n\n"):
        prefix = prefix[len("# Empire of Dust\n\n") :]
    return prefix + "\n"


def split_beats(episode_text: str) -> list[str]:
    matches = list(re.finditer(r"^### Beat \d+\n", episode_text, flags=re.MULTILINE))
    if len(matches) != 4:
        raise ValueError(f"Expected 4 beats, found {len(matches)}")

    beats: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(episode_text)
        chunk = episode_text[start:end].strip()
        beats.append(chunk)
    return beats


def extract_episode_number(path: Path) -> str:
    match = re.search(r"episode-(\d{2})\.md$", path.name)
    if not match:
        raise ValueError(f"Could not parse episode number from {path.name}")
    return match.group(1)


def write_prompt_file(path: Path, beat_text: str, global_suffix: str) -> None:
    content = beat_text.rstrip() + "\n\n" + global_suffix
    path.write_text(content, encoding="utf-8")


def main() -> None:
    master_text = MASTER_PATH.read_text(encoding="utf-8")
    global_suffix = load_global_suffix(master_text)

    episode_paths = sorted(EPISODE_DIR.glob("episode-*.md"))
    if not episode_paths:
        raise ValueError(f"No episode files found in {EPISODE_DIR}")

    created = 0
    skipped = 0
    overwritten = 0

    for episode_path in episode_paths:
        episode_no = extract_episode_number(episode_path)
        episode_text = episode_path.read_text(encoding="utf-8")
        beats = split_beats(episode_text)

        episode_dir = OUTPUT_ROOT / f"Empire of Dust｜episode {episode_no}"
        episode_dir.mkdir(parents=True, exist_ok=True)

        for idx, beat_text in enumerate(beats, start=1):
            output_path = episode_dir / f"Beat{idx} Seedance 2.0 Prompts.md"
            if output_path.exists() and episode_no == "06":
                skipped += 1
                continue
            if output_path.exists():
                overwritten += 1
            write_prompt_file(output_path, beat_text, global_suffix)
            created += 1

    print(f"Created {created} prompt files.")
    print(f"Skipped {skipped} existing prompt files.")
    print(f"Overwrote {overwritten} prompt files.")


if __name__ == "__main__":
    main()
