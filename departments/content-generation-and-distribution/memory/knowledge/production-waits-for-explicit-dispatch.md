---
title: 内容生产部门只在收到明确 production dispatch 后启动 Empire of Dust 后续集数生产
confidence: H
tag: self
created: 2026-04-25
source: 2026-04-25 repeated idle checks and session excerpt repeatedly confirmed no autonomous production start without formal CEO dispatch
---
在 Empire of Dust S01 的后续生产里，本部门的默认工作边界是等待上游明确下发 `s01-episode-NN-production` 指令，再启动该集生产。即使已知 Ep07–Ep20 归内容生产部门执行，只要缺少正式 dispatch，就不主动补跑、跳过、顺延或自发开工；此时应保持最小核查并继续等待 [[empire-of-dust-pipeline]] 的正式触发。

收到新的 Agent Wire episode dispatch 时，要先用最小字段回执确认接收；如果当前线程已经在处理另一集或刚发生中断，优先确认最新有效唤醒并一次只推进一集，避免同时生产两集或让回执被误判成终态交付。



<!-- backlinks:auto -->
## Backlinks

- [[aivideopro-ugc-routes-to-ugc-forge]]
- [[harness-actionable-work-can-be-false-positive]]
<!-- /backlinks:auto -->
