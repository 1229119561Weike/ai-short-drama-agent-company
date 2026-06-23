---
title: YouTube 发布只有拿到公开视频证据后才能结算并移交 analytics
confidence: H
tag: self
description: Empire of Dust 发布完成必须有 Shorts URL、video ID、Public 状态、标题、播放列表确认；发现标题、metadata 或 playlist 错误时，必须先锁定正确 metadata 与阻塞证据，不能把公开状态当成完全结算。
created: 2026-05-10
source: 2026-05-10 Ep17 production completed before browser returned YouTube URL/video ID, so gate stayed failed until published evidence arrived; confirmed again by Ep19 on 2026-05-12 and Ep20 finale on 2026-05-13, where URL/video ID/Public/title/playlist evidence arrived only after browser completion; deepened on 2026-05-15 when EP2 was public but title correction was blocked by YouTube identity verification; extended on 2026-05-19 to cover internal admin-console uploads after YouTube integration could not access local MP4 files; extended on 2026-05-21 after direct YouTube integration upload skipped the distribution CSV handoff artifact; deepened on 2026-05-26 when THE LAST WALL BURNS Ep3 was published but the expected playlist was unavailable in YouTube Studio
---

Empire of Dust 的分发 gate 不能把“上传流程已启动”“已点击 Publish”、[[public-platform-final-action-requires-confirmation]] 后的确认，或浏览器处于 ready 状态当作发布完成。只有拿到可复核的发布证据后，才能把该集标为 published 并移交 analytics：Shorts URL、video ID、Public/Published 状态、最终标题，以及目标播放列表已选中或不可用的明确证据。

最终标题和公开 metadata 是发布证据的一部分，而不只是包装记录。若视频已 public 但标题、description 或 tags 与本地锁定版本不一致，结算口径应拆成“公开视频存在，但 metadata 修正未完成”；同时保存正确的本地 metadata lock、当前公开视频状态、需要修正的字段和阻塞截图/原因，例如 YouTube “Verify it’s you”。

如果 production final 与 [[media-qa-evidence-required]] 已齐，但 YouTube URL、video ID 或播放列表确认缺失，结算口径应写成“生产完成，发布未结算”。这样能避免把未完成的上传误传给策略部门，也能在浏览器稍后返回结果时追加证据完成 handoff。

当 YouTube integration 因本地文件访问失败而无法上传时，可以切换到内部视频中台，但仍要先完成 [[admin-bulk-upload-manifest-first]]，并在中台上传完成后回收同等发布证据再结算。

即使用 YouTube integration 直接上传本地视频，也不能跳过 `publishing/` 下的 distribution CSV。CSV 是分发指导和发布 handoff artifact，应在上传前锁定 20 集规划、标题、description、tags、发布时间/状态、播放列表和已发布 URL；若用户临时要求先发布无字幕版，也要在发布后立即补齐并标明对应集数的实际 URL/video ID。

发布证据拿到后，应主动关闭 `neo-browser`/browser monitor，避免发布完成后的空闲保活被误解为还在继续操作账号。



<!-- backlinks:auto -->
## Backlinks

- [[admin-bulk-upload-manifest-first]]
<!-- /backlinks:auto -->
