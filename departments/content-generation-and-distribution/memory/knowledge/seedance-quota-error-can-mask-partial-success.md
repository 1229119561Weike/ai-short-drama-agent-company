---
title: Seedance 批量任务或单 beat 失败时，部分任务可能仍成功，需先复查任务 ID 再重试
confidence: H
tag: knowledge
description: Seedance 批量提交或单 beat 回传失败时，不能直接整集重跑；应保留任务 ID/失败响应，逐条复查，只用原 prompt 重试真失败 beat。
created: 2026-05-08
source: 2026-05-08 Ep15 生产：四个 beat 并发提交后网关返回 401 令牌额度已用尽，但复查发现 Beat1/2/4 已成功取回，只有 Beat3 需重试；2026-05-15 Ep10 Beat3 failed/no-output 后保留失败响应并从 submitted_prompt.md 原样重跑
---

# 现象

Empire of Dust 生产侧并发提交四个 Seedance beat 任务时，网关可能在任一 beat 上返回 `401 令牌额度已用尽`。这个错误会让整批提交看起来全部失败，但实际情况可能是部分任务已成功创建并能够取回视频，只有其中一两个真正失败。

单个 beat 的后续轮询也可能返回 failed、空 `response.json` 或无输出产物。此时仍不代表整集素材不可用；应先把失败响应、stderr、exit code、command log 和原 `submitted_prompt.md` 保留下来，再只对这个 beat 做原 prompt 重跑。

# 后果

2026-05-08 Ep15 初次提交返回四个任务 ID（`cgt-20260508115041-qzzft` / `-psvd7` / `-drs7p` / `-drjmg`）并伴随 401 额度错误。若直接判定全部失败并重新提交四个 beat，会在额度恢复后对已经成功的 Beat1/2/4 重复下单，既浪费额度又可能产出不一致的素材。实际复查发现 Beat1/2/4 已经完成，只有 Beat3 (`cgt-20260508115041-drs7p`) 失败，只需用原 prompt 重试这一条。

2026-05-15 Ep10 Beat3 原任务确认为 failed 且没有输出；可靠做法是先把 `response_attempt1_failed.json` 等诊断副本落盘，再从既有 `submitted_prompt.md` 原样重跑 Beat3，并让最终拼接等待该 beat 成功。

# 操作规则

遇到 Seedance 批量提交出现 401/额度错误，或单 beat 轮询失败/无输出时：

1. **先保留全部任务 ID 与失败证据**，不要立刻假设全部失败，也不要覆盖空响应或错误日志。
2. **逐条复查**每个任务状态；已有产物的 beat 直接取回归位，不重新下单。
3. **仅对真失败的 beat** 用原 prompt 重试一次；重试时不要改写 prompt，以保持 Beat 之间的连续性（参见 [[empire-of-dust-pipeline]] 的固定参数要求）。
4. **重试成功后**再进入拼接、字幕、QA 环节，保证四个 beat 都在同一次生成基调上。

# 对应反例

不要做的事：
- 看到批量提交返回错误就触发“整集重跑”，在额度恢复后重复下单。
- 把部分成功视为不可信而丢弃已成功的 beat，造成风格/镜头在重新生成版本里漂移。
- 用新写法重编失败 beat 的 prompt，导致唯一重试片段与其余三段叙事或视觉风格漂移。



<!-- backlinks:auto -->
## Backlinks

- [[generation-timeout-without-taskid-requires-output-check]]
<!-- /backlinks:auto -->
