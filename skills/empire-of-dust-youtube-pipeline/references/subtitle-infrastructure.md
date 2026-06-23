# Portable Subtitle Infrastructure

This workspace includes reusable subtitle tooling for Empire of Dust episodes.

## Included files

- `skills/empire-of-dust-youtube-pipeline/scripts/auto_subtitle_episode.py`
  - discovers four beat videos in an episode folder
  - transcribes actual generated audio with `faster-whisper`
  - writes `subs_auto/beatN.srt` and `whisper_auto/beatN.json`
  - burns visible bottom subtitles with `ffmpeg`
  - concatenates the four subtitled beats into one final MP4
- `skills/empire-of-dust-youtube-pipeline/requirements-subtitles.txt`
- `skills/empire-of-dust-youtube-pipeline/scripts/setup_subtitle_env.sh`

## Restore after exporting workplace

From the workspace root:

```bash
export NEO_WORKSPACE_ROOT="$PWD"
bash skills/empire-of-dust-youtube-pipeline/scripts/setup_subtitle_env.sh
```

Install `ffmpeg` separately if the target machine does not already have it. On macOS:

```bash
brew install ffmpeg
```

## Run for an episode

```bash
python3 skills/empire-of-dust-youtube-pipeline/scripts/auto_subtitle_episode.py \
  --episode-dir "$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 10" \
  --output "$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 10/Empire of Dust Episode 10 final.mp4"
```

The script uses actual generated audio. Do not replace transcript text with script text unless you have listened and confirmed the audio matches.
