---
title: Minimalist knowledge videos should derive subtitles from generated sentence audio boundaries
confidence: H
tag: self
created: 2026-06-16
source: 2026-06-16 maintenance: 世界十大顶级思维 production attempt used local TTS sentence boundaries, script text SRT, and bundled Python ffmpeg when system ffmpeg was absent
---

Decision: For minimalist-illustration knowledge videos, generate narration sentence-by-sentence and use the resulting audio boundaries as the SRT timing source, while keeping the approved script text as subtitle text.

Why: This preserves exact wording for Chinese and English versions, avoids Whisper/STT substitution errors on scripted educational copy, and still keeps subtitles synchronized with the actual generated audio. If system `ffmpeg` is missing from `PATH`, use the bundled encoder exposed by Python packages such as `imageio-ffmpeg` or `moviepy` rather than treating that alone as a production blocker.

Rejected: Directly transcribing finished narration with Whisper as the sole subtitle source loses approved wording and can introduce Chinese mistranscriptions. Copying script timestamps without generating per-sentence audio boundaries risks drift. Declaring missing system `ffmpeg` as blocked is too early when an embedded encoder is available.

Reverse if: The narration comes from externally generated audio without reliable sentence boundaries, the voice engine changes timing after concatenation, or the bundled encoder cannot produce the required 1080x1920 MP4; then fall back to [[local-audio-pipeline-on-apple-silicon]] STT alignment and the QA gates in [[media-qa-evidence-required]].
