---
title: Empire of Dust 成片字幕必须以实际生成音频为准，而不能直接套用剧本文本
confidence: H
tag: knowledge
created: 2026-04-23
source: 2026-04-23 Ep06 字幕返工，Beat1 因手写脚本字幕与实际生成音频不一致而出错；2026-04-29/30 Ep09 返工确认底部小字幕像素落点验收标准；2026-05-06 Ep13 确认 ASS MarginV 可误导，必须做真实画面差分 QA
---
Empire of Dust 短视频的字幕不能直接从剧本对白拷贝生成；必须先依据每个 Beat 的实际成片音频做转写与校时，再烧录进分镜和最终成片。若脚本与生成音频存在改写、停顿漂移或开口延后，直接套用剧本文本会导致字幕内容和时间轴同时出错。这个约束补充了 [[empire-of-dust-pipeline]] 中的固定流程要求。

2026-04-29 Ep09 再次暴露两个字幕质量坑：第一，Whisper 会把多句短对白合并成一整条，不能把这种整段字幕直接烧录；必须用 word timestamps 拆成短句，并按实际音频轻量纠字。第二，字幕视觉样式也必须 QA：1080x1920 Shorts 默认使用底部居中的较小字幕（约 `FontSize=30`、白字黑描边、`Alignment=2`、`MarginV≈130`），目标是完整展示文本、位置靠底但不贴边、尽量不压主体。烧录后至少抽首句/中段/末句三帧检查字号、底部安全区和整体观感，不能只凭 ASS 参数或导出规格宣称字幕合格。

2026-04-30 Ep09 字幕返工最终覆盖经验：不能把字幕 QA 等同于 ASS/ffmpeg 参数。错误版本暴露了三类坑：直接烧录 Whisper 合并 segment 会变成长句块；只调 `FontSize` 会让字幕占画面；只看 ASS `MarginV` 会误判位置，参数像在底部但真实画面可能偏中。合格标准改为：逐词时间轴拆短句，优先单行；用可控 `drawtext`/等效方式把字幕放到底部安全区；导出后抽帧与无字幕底图做像素差分，确认 bbox 在画面高度约 0.86-0.91、底边距约 160-220px、长句宽度通常不超过 55%-60%、不遮脸不压主体。没有真实抽帧/像素落点验收，不得说字幕完成。

2026-05-06 Ep13 最终 QA 再次确认：即使 ASS `subtitles` 滤镜参数看似正确，实际字幕也可能落到画面中上部；必须以导出后真实帧为准。可靠返工路径是用 SRT/转写结果生成分段 `drawtext`，用 `textfile` 避免英文撇号等转义失败，再以抽帧差分确认字幕 bbox 实际在底部安全区。Ep13 合格样本的字幕 bbox 落在画面高度约 0.897-0.907、底边距约 179-182px；只有这类画面级证据完成后，final 才能放行给分发。



<!-- backlinks:auto -->
## Backlinks

- [[local-audio-pipeline-on-apple-silicon]]
- [[media-qa-evidence-required]]
- [[verify-final-asset-before-subtitle-or-publish]]
<!-- /backlinks:auto -->
