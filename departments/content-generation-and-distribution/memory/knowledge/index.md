# Department Knowledge Index

## knowledge
- [[empire-of-dust-pipeline]] — Empire of Dust 生产管线的固定画布、脚本路径、输出参数、后期工具和跨部门资源参考。 [H]
- [[harness-actionable-work-can-be-false-positive]] — 当 department snapshot 显示 `Actionable work items: 1` 或 `Inbox pending: 1`，但 `mail/inbox/new`、`mail/inbox/cur`、`missions.json` 都为空时，应优先怀疑是 harness 统计误报，而不是生产漏单。已核实的模式包括把当前打开的 canonical chat 会话，或已经 `status: "closed"` 的历史 runtime task 记录算进队列。遇到这种情况时，应先核对真实 maildir 和 mission store，再决定是否需要继续等待 [[production-waits-for-explicit-dispatch]]。 [H]
- [[local-audio-pipeline-on-apple-silicon]] — Using local offline text-to-speech (TTS) and speech-to-text (STT) tools dramatically improves pipeline reliability and speed, avoiding API rate limits, latency, and cloud costs. [H]
- [[seedance-quota-error-can-mask-partial-success]] — Seedance 批量提交或单 beat 回传失败时，不能直接整集重跑；应保留任务 ID/失败响应，逐条复查，只用原 prompt 重试真失败 beat。 [H]
- [[short-form-drama-factory-method]] — Use a four-layer factory model for short-form drama planning: market/hook selection, episode architecture, production consistency, and distribution learning. The practical next proof should usually be a small finished pilot or scene that tests hook retention and visual consistency before expanding into a full season package. [H]
- [[subtitles-must-follow-generated-audio]] — Empire of Dust 短视频的字幕不能直接从剧本对白拷贝生成；必须先依据每个 Beat 的实际成片音频做转写与校时，再烧录进分镜和最终成片。若脚本与生成音频存在改写、停顿漂移或开口延后，直接套用剧本文本会导致字幕内容 and 时间轴同时出错。这个约束补充了 [[empire-of-dust-pipeline]] 中的固定流程要求。 [H]
- [[verify-final-asset-before-subtitle-or-publish]] — Empire of Dust 或同类短剧进入返工、补字幕或发布前校验时，不能凭“看起来对”“相邻节点命名接近”或关键词搜索结果来猜目标素材。必须先确认用户指定的精确 asset，再核对该 asset 的父子关系、分辨率、时长与是否真是最终导出版本；只有在目标文件身份被锁定后，后续转写、对时、烧录和完成宣称才可信。这个约束补强了 [[subtitles-must-follow-generated-audio]]：字幕不仅要跟实际音频走，还要先确认用来转写的就是最终要交付的那个音频/视频资产。 [H]

## self
- [[admin-bulk-upload-manifest-first]] — Read before any multi-episode admin-console upload; build a manifest of local final MP4 paths, locked metadata, and per-site field rules before touching the upload page. [H]
- [[aivideopro-ugc-routes-to-ugc-forge]] — When AIVideoPro UGC promo or creative-package work appears, treat it as UGC Forge Department ownership rather than Content Generation & Distribution unless the dispatch explicitly asks for short-drama production, assembly, publishing, or analytics handoff. If such work is misrouted here, close or cancel the local task with the cancellation/routing proof and reply on the thread instead of continuing production work. [H]
- [[canvas-active-binding-can-drift]] — canvas-cowork 提交前必须用完整生产画布 URL 重绑并确认 activeConvId，避免浏览器前台标签导致投递漂移。 [H]
- [[handling-deferred-tools-and-planning-timeouts]] — When operating inside complex workflows, planning loops, and multi-agent setups, automated tool usage can fail due to missing schemas or permission barriers. [H]
- [[media-qa-evidence-required]] — 每集生产完成应交付 final 路径、媒体规格、beat 顺序、字幕产物、生成/返工日志和抽帧 QA 文档，便于协调和分发结算。 [H]
- [[production-waits-for-explicit-dispatch]] — 在 Empire of Dust S01 的后续生产里，本部门的默认工作边界是等待上游明确下发 `s01-episode-NN-production` 指令，再启动该集生产。即使已知 Ep07–Ep20 归内容生产部门执行，只要缺少正式 dispatch，就不主动补跑、跳过、顺延或自发开工；此时应保持最小核查并继续等待 [[empire-of-dust-pipeline]] 的正式触发。 [H]
- [[public-platform-final-action-requires-confirmation]] — Read before clicking any final Publish/Post button on YouTube, TikTok, or another public distribution platform; stage the upload, report the exact state, and wait for explicit confirmation. [H]
- [[stop-production-when-prereq-is-missing]] — 前置能力缺失会让 Empire of Dust 生产失真时，应停止生产、回写阻塞，并等待基础功能补齐。 [H]
- [[tiktok-publish-evidence-gates-release-records]] — Read before settling TikTok distribution; require post URL, post ID, public/Everyone status, caption used, asset path, and local release CSV update after explicit posting confirmation. [H]
- [[uv-environment-management-guidelines]] — When managing dependencies and python virtual environments using `uv` on macOS, standard pip patterns and virtual environment assumptions can break. Follow these guidelines to avoid installer and shell execution failures. [H]
- [[youtube-publish-evidence-gates-analytics]] — Empire of Dust 发布完成必须有 Shorts URL、video ID、Public 状态、标题、播放列表确认；发现标题、metadata 或 playlist 错误时，必须先锁定正确 metadata 与阻塞证据，不能把公开状态当成完全结算。 [H]
- [[generation-timeout-without-taskid-requires-output-check]] — Read before retrying media generation after a creation timeout; verify task IDs and output directories first, then retry only confirmed-missing beats at smaller scope. [M]

---
Updated: 2026-06-16T12:00:00Z
