#!/usr/bin/env bash
set -euo pipefail

python3 -m pip install -r "$(dirname "$0")/../requirements-subtitles.txt"

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg is required. Install it with Homebrew on macOS: brew install ffmpeg" >&2
  exit 1
fi

python3 - <<'PY'
import faster_whisper
print('Subtitle Python dependency OK: faster_whisper')
PY
