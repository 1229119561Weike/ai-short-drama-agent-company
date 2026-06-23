---
title: Empire of Dust YouTube Shorts 管线在生产部门侧的固定资源、参数与规则
confidence: H
tag: knowledge
description: Empire of Dust 生产管线的固定画布、脚本路径、输出参数、后期工具和跨部门资源参考。
created: 2026-04-23
source: seeded from empire-of-dust-youtube-pipeline skill onboarding; canvas URL token refreshed 2026-04-28 after Ep07 fix; subtitle visual baseline corrected after Ep09 v4 on 2026-04-29
---

# Empire of Dust 生产管线参考

## 固定资源

- 生产画布 conv_id：`51e5ed99-7c7d-4bc9-be3f-d9b44a6a80b1`
- 生产画布最新可用 URL（含 token，CEO 在 Ep07 修复期发的版本）：
  `https://flowith.io/conv/51e5ed99-7c7d-4bc9-be3f-d9b44a6a80b1?U2FsdGVkX1/fXZvbnckVi2gQ/3aZZuixjFahPTJsy99T3MONd6Czn77P7avS9uMnI7z3aUvOelOUrtQ3SiT96w==`
- 注意：CEO 派单原文与 `empire-of-dust-youtube-pipeline` skill 文档里仍写着 4/23 的旧 token（`...HqeKGcQ==`）。token 会偶尔轮换；下单前以本卡或最新 CEO 消息为准，不要直接 copy SKILL.md 里那条。
- 剧本总表：`/Users/flowith-mac-mini-001-user/Documents/Playground/docs/empire-of-dust-retention-20ep-dense-master.md`
- 分集剧本：`/Users/flowith-mac-mini-001-user/Documents/Playground/docs/empire-of-dust-retention-20ep-dense/episode-*.md`
- Prompts 输出根：`/Users/flowith-mac-mini-001-user/Downloads/Empire of Dust `
- 拆分脚本：`<workspace>/skills/empire-of-dust-youtube-pipeline/scripts/split_empire_of_dust_prompts.py`

## 固定参数

- 模型：`Seedance 2.0`
- 每 beat：`480p` / `9:16` / `15s`
- 最终成片：`1080x1920` / `mp4` / 约 1 分钟 / 含字幕（仅念白片段）
- 字幕样式：先用实际音频 word timestamps 拆短句；视觉验收不能只看参数，必须抽真实帧/像素落点。1080x1920 Shorts 默认底部单行小字幕，bbox 约落在画面高度 0.86-0.91，底边距约 160-220px，长句宽度通常不超过 55%-60%，不遮脸、不压主体、不贴边；优先使用 `drawtext`/等效精确定位。
- `内容分发部门` id：`b3e2d81f`
- `数据分析与内容策略部门` id：`d9a6c417`

## 工具依赖

- `canvas-cowork` skill（本机 `~/.codex/skills/canvas-cowork`，如缺失用 `npx skills add flowith-ai/canvas-cowork`）
- `ffmpeg`（后期拼接 / 缩放 / 字幕烧录）
  - 本机已安装：`/Users/flowith-mac-mini-001-user/.local/bin/ffmpeg` (v7.1.1)
  - 该路径不在默认 PATH 中，必要时用绝对路径调用
- macOS AVFoundation/VideoToolbox 可作为本机缺少 `ffmpeg`/`ffprobe` 时的拼接转码 fallback，但完成后仍要验证最终 MP4 的分辨率、时长、fps、文件大小和哈希，再进入发布。
- `faster-whisper`（对白校时）
  - 安装方式：`pip3 install --user faster-whisper`
  - 调用：`python3 -c "from faster_whisper import WhisperModel; ..."`

如上述基础设施缺失或版本异常，先安装再进入后期阶段。

参见 [[canvas-active-binding-can-drift]]：在 `submit` 前必须显式校验/重绑 active canvas，否则 beat 可能被丢进别的画布。



<!-- backlinks:auto -->
## Backlinks

- [[canvas-active-binding-can-drift]]
- [[production-waits-for-explicit-dispatch]]
- [[seedance-quota-error-can-mask-partial-success]]
- [[stop-production-when-prereq-is-missing]]
- [[subtitles-must-follow-generated-audio]]
<!-- /backlinks:auto -->
