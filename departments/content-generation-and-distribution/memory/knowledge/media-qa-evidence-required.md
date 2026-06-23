---
title: Empire of Dust 完成交付必须附带可审计的媒体 QA 证据，而不只是一条 final 路径
confidence: H
tag: self
description: 每集生产完成应交付 final 路径、媒体规格、beat 顺序、字幕产物、生成/返工日志和抽帧 QA 文档，便于协调和分发结算。
created: 2026-05-07
source: 2026-05-07 Ep14 production handoff required ffprobe, Whisper/SRT, concat order, keyframe, and subtitle-render evidence before distribution settlement; 2026-05-14 Arena Ep01 rework required preserving per-submission logs before accepting a new final; 2026-05-18 EP18 showed final video alone is not enough when packaging/QA/handoff remain incomplete
---

Empire of Dust 每集生产侧宣称完成时，必须同时给出可结算证据：final MP4 的绝对路径、`ffprobe`/AVFoundation 规格（至少分辨率、时长、音频存在）、四个 beat 的顺序清单、每段生成/返工任务日志、每段转写/SRT 或字幕烧录产物、以及能证明字幕可见的抽帧或 QA 文档。仅说明“final 已生成”、媒体参数通过或只贴路径不足以让协调/分发方安全接手；如果包装文件、per-beat QA 或 handoff 缺失，应按生产交付未完成回报，即使 final MP4 已核验。

Ep14 的可靠交付形态是先生成 `Episode NN Production QA Handoff.md`，把 [[subtitles-must-follow-generated-audio]] 和 [[verify-final-asset-before-subtitle-or-publish]] 的检查结果集中成一页：素材身份、拼接顺序、字幕来源、渲染位置、关键帧抽查和 caveats 都写清楚，再把该文档连同 final 路径回传给协调线程。这样后续出现 urgent status gate 时，可以复用同一套证据回答，而不会因为口头状态更新缺少附件而反复追问。

返工型任务还要保存每次 Seedance/媒体请求的 prompt、参考图/first-frame/text-only 路线、返回任务 ID、错误原文和降级原因。Arena Ep01 的重做证明：如果只保留成功下载的 mp4，而不保留失败的多参考图或模型错误日志，用户要求逐条追溯“为什么降级/为什么重做”时无法结算。



<!-- backlinks:auto -->
## Backlinks

- [[youtube-publish-evidence-gates-analytics]]
<!-- /backlinks:auto -->
