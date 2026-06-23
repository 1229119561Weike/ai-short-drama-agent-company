---
title: Local TTS and transcription via kokoro-onnx and faster-whisper run efficiently on Apple Silicon
confidence: H
tag: knowledge
created: 2026-06-16
source: 2026-06-16 session: successful compilation and setup of local offline audio synthesis and transcription using kokoro-onnx and faster-whisper inside tts_env on Apple Silicon macOS
---

Using local offline text-to-speech (TTS) and speech-to-text (STT) tools dramatically improves pipeline reliability and speed, avoiding API rate limits, latency, and cloud costs.

### Speech Synthesis (TTS) via Kokoro-ONNX
- **Library**: `kokoro-onnx` combined with `soundfile` and `edge-tts`.
- **Model and Voice Files**:
  - Model: Use the fp16 version for faster inference and smaller footprint: `https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0-fp16.onnx`
  - Voices: Download `https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin`
- **Inference**: Loads instantly and runs locally with negligible CPU/GPU overhead on Apple Silicon (M1/M2/M3).

### Speech Transcription (STT) via Faster-Whisper
- **Library**: `faster-whisper` (utilizing CTranslate2 backend).
- **Benefits**: Local execution is highly optimized on macOS. Provides exact word timestamps and segments, which are critical for matching the subtitle alignment constraints in [[subtitles-must-follow-generated-audio]].
- **Usage**: Always leverage word-level timestamps to segment audio into single-line short subtitles to avoid long blocks of text in 1080x1920 portrait formats.

### Environment & Dependency Management
- To ensure clean and fast isolation, compile and manage these packages using `uv` inside a dedicated virtual environment (e.g., `tts_env`).
- For installation and execution rules, read [[uv-environment-management-guidelines]].
