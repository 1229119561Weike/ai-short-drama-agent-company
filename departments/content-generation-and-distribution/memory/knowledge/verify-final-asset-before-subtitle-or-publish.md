---
title: Empire of Dust 返工时必须先锁定最终使用的精确 asset 与媒体规格，再做字幕或宣称完成
confidence: H
tag: knowledge
created: 2026-04-27
source: 2026-04-27 Ep07 返工多次误把相邻节点或错误版本当成目标素材，导致字幕与口播和成片均错配；2026-05-14 Arena Ep01 用户明确拒绝 rough final 后，发布候选必须撤回并按 beat 重做；2026-05-20 The Last Wall Burns 用户要求停止字幕并直接发布无字幕版，发布候选必须锁定 non-subtitled final.mp4
---
Empire of Dust 或同类短剧进入返工、补字幕或发布前校验时，不能凭“看起来对”“相邻节点命名接近”或关键词搜索结果来猜目标素材。必须先确认用户指定的精确 asset，再核对该 asset 的父子关系、分辨率、时长与是否真是最终导出版本；只有在目标文件身份被锁定后，后续转写、对时、烧录和完成宣称才可信。这个约束补强了 [[subtitles-must-follow-generated-audio]]：字幕不仅要跟实际音频走，还要先确认用来转写的就是最终要交付的那个音频/视频资产。

如果用户或 QA 明确拒绝某个 rough final、要求重做 Beat，必须立即停止把该 rough final 当成发布候选。后续状态只能围绕新一轮逐 Beat 产物、提交日志和最终重导出的 asset 回答，不能沿用旧 final 的规格或发布准备作为“已完成”证据。

如果用户明确改交付版本，例如取消字幕版并要求直接发布无字幕版，必须在上传前按精确文件名/路径重新锁定发布候选。应排除所有被拒绝的变体（例如文件名包含 `subtitled` 的版本），并在状态更新中点名选中的 `final.mp4`，让上传路径可审计。



<!-- backlinks:auto -->
## Backlinks

- [[media-qa-evidence-required]]
<!-- /backlinks:auto -->
