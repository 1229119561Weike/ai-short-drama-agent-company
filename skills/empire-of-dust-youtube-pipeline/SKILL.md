---
name: empire-of-dust-youtube-pipeline
description: 当用户要求用 Empire of Dust 的剧本源文件先拆出每集四段 Seedance 2.0 prompts，再首选在 Matrix 中生成 4 个 `Seedance 2.0 / 480p / 9:16 / 15s` 分镜视频，拼接并导出 `1080x1920` 字幕成片，发布到 YouTube Shorts、加入 `Empire of Dust` 播放列表、更新 dashboard，并在整季发布完成后生成杀青项目报告书时使用。
seedVersion: 5
---

# Empire of Dust YouTube Pipeline

## 1. 何时使用

当用户要执行以下任一任务时使用本 skill:

- 从 Empire of Dust 剧本文件拆出每集四段 `Seedance 2.0` prompts
- 维护 workspace Files 中的每集 prompts 文件夹：`$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust`
- 首选在 Matrix 中生产某一集的四个分镜视频；仅在 Matrix 不可用或用户指定时使用固定 Flowith 画布
- 将四个 `15s` 片段拼接为一个约 `1 minute` 的完整视频
- 导出 `1080x1920` 且带字幕的最终成片
- 发布到 `YouTube Shorts`
- 将视频加入 `Empire of Dust` 播放列表
- 更新每日 dashboard
- 在整季全部发布完成后输出杀青项目报告书

## 2. 固定资源

所有默认文件都必须优先从 workspace Files 读取。默认根目录：

- Pipeline Files 根目录：
  `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline`

如果当前环境没有 `NEO_WORKSPACE_ROOT`，先把它设为当前 workplace 根目录；不要回退到用户本机 `Downloads` / `Documents` 目录，除非用户明确指定。

- Matrix 视频生成：
  首选在 Matrix 内直接调用视频生成能力创建 Seedance 2.0 短剧视频。
- Flowith fallback 画布 URL:
  `https://flowith.io/conv/51e5ed99-7c7d-4bc9-be3f-d9b44a6a80b1?U2FsdGVkX19fTvXs98QX5+sVRvELaFwypt3KmkTaq8GhGzD/ZJKxZcTaa0234K0ay1y6kOyG8VSOv/hHqeKGcQ==`
- Prompt / 成片生产根目录:
  `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust`
- 剧本总表:
  `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/scripts/empire-of-dust-retention-20ep-dense-master.md`
- 分集剧本目录:
  `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/scripts/empire-of-dust-retention-20ep-dense`
- 默认发布文案表:
  `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/publishing/empire-of-dust-youtube-pack-sheet1.csv`
- 发布文案表回退匹配:
  `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/publishing/empire-of-dust-youtube-pack*.csv`
- 播放列表名称:
  `Empire of Dust`
- 必带简介句:
  `Thanks everyone for loving my original AI short dramas! If you're interested in other storylines, feel free to subscribe to my channel and check out my playlists!`
- 默认杀青报告路径:
  `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust 杀青项目报告书.md`

## 3. Department Ownership

- `Content Generation & Distribution` (`7c4f9a21`)
  Owns the end-to-end Empire of Dust execution loop: script/prompt splitting, Matrix-first Seedance generation, post-production, subtitles, 1080x1920 export, YouTube Shorts upload, title/description/tag verification, `Empire of Dust` playlist confirmation, and publish evidence handoff.
- `Data Analysis & Content Strategy` (`d9a6c417`)
  Owns dashboard updates, analytics review when data access is available, and the end-of-season wrap-up report.
- `CEO Office` (`8591249c`)
  Owns sequencing, schedules, commitments, evidence gates, blocker escalation, and cross-department handoff integrity.

## 4. 不可违反的规则

- 视频生产首选 Matrix 内直接生成，不要默认打开 Flowith 画布。
- 只有当 Matrix 视频生成不可用、用户明确指定 Flowith、或需要沿用某个既有画布上下文时，才使用固定 Flowith fallback 画布。
- 使用 Flowith fallback 时，必须使用完整 URL，不要自己提取 `conv_id` 后切换到别的画布。
- 使用 Flowith fallback 时，优先使用 workspace 内的 `canvas-cowork`：`$NEO_WORKSPACE_ROOT/skills/canvas-cowork/SKILL.md`；如果不存在，停止并报告 workspace 缺少打包后的 `canvas-cowork`，不要自动安装到用户级目录。

- 每一个 `Beat` prompt 文件都必须作为一个独立输入单元处理。
- 真正提交给 `Seedance 2.0` 的内容必须是一字不改的完整 prompt 文件正文。
- 不得在生成前改写、翻译、删减、润色、摘要或补写 prompt 正文。
- 每个 beat 的生成参数固定为:
  - `480p`
  - `9:16`
  - `15s`
- 同一集的 `Beat1`、`Beat2`、`Beat3`、`Beat4` 默认必须在 Matrix 中并行生成；只有 fallback 到 Flowith 时才要求在同一个固定画布中并行生成。
- 最终导出视频必须是单个约 `1 minute` 的 `1080x1920` 竖屏成片。
- 有人物念白的片段必须带字幕。
- 每天只发布一集。
- 剧本有多少集，就运行多少天；不要硬编码集数，即使当前默认是 `20` 集。
- 发布后必须加入 `Empire of Dust` 播放列表。
- 发布前必须由 agent 自动核对 YouTube Studio 中的标题、简介与权威发布文案源逐字一致；发现不一致时先修正再继续，不要让用户代为检查。
- 全部剧集发布完成后，必须输出一份杀青项目报告书。
- 如果关键输入缺失，不得编造。

## 5. 输入优先级

### 5.1 拆分 prompts 时

按以下优先级读取源内容:

1. `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/scripts/empire-of-dust-retention-20ep-dense/episode-*.md`
2. `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/scripts/empire-of-dust-retention-20ep-dense-master.md`
3. `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust` 中已存在的历史 prompt 文件，仅作为格式参考，不作为真值来源

### 5.2 每日生产时

按以下优先级读取当日生成 prompts:

1. `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust` 下对应剧集的四个 beat prompt 文件
2. 如果当日 prompts 缺失，则先回到剧本源文件重新拆出该集 prompts，再开始生成

### 5.3 发布文案时

按以下优先级准备标题、简介、标签:

1. 用户本轮明确给出的发布文案文档
2. `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/publishing/empire-of-dust-youtube-pack-sheet1.csv`
3. `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/publishing/empire-of-dust-youtube-pack*.csv` 的最近匹配文件
4. 如果仍缺失，则根据当集剧本与 prompts 撰写发布文案，并把最终使用版本记录在 dashboard 或当次任务结果中

## 6. 阶段 A：把剧本拆成每集四段 prompts

当用户给到剧本文件，例如:

- `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/scripts/empire-of-dust-retention-20ep-dense-master.md`
- `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/scripts/empire-of-dust-retention-20ep-dense`

就先执行本阶段。

### 6.1 统计剧集

- 优先枚举 `episode-*.md` 文件来确定总集数。
- 如果分集目录不完整，再从 master 文件中解析 `Episode` 分段。
- 总运行天数等于实际可生产剧集数。

### 6.2 生成 prompts 文件夹

必须把每一集拆成如下结构:

- 目录:
  `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode XX`
- 文件:
  - `Beat1 Seedance 2.0 Prompts.md`
  - `Beat2 Seedance 2.0 Prompts.md`
  - `Beat3 Seedance 2.0 Prompts.md`
  - `Beat4 Seedance 2.0 Prompts.md`

其中 `XX` 使用两位数剧集编号，例如 `01`、`06`、`20`。

### 6.3 prompt 写作规则

- 每个 beat 生成一个独立 `.md` 文件。
- 输出格式优先对齐已经存在的示例格式，例如:
  `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode 06/Beat1 Seedance 2.0 Prompts.md`
- 每个文件都要足够完整，能直接整份喂给 `Seedance 2.0`。
- 同一集的四个 beat 之间要保持角色锁、造型锁、环境锁和世界观连续性。
- 如果用户没有要求刷新，则对已存在且完整的 prompt 文件只复用，不重写。
- 如果某一 beat 缺失或明显不完整，只补齐缺失部分，不要无谓重做整集。

## 7. 阶段 B：确定今天要生产哪一集

- 如果用户明确指定了剧集，就生产该集。
- 如果用户没有指定，就按升序选择“尚未发布”的最小剧集编号。
- “尚未发布”以 dashboard、发布记录、已上传结果或播放列表记录为准。
- 每次日更只推进一集。
- 下一次运行时，再继续下一集。

## 8. 阶段 C：生成四个 beat 视频

### 8.1 首选 Matrix 直接生成

- 默认在 Matrix 中直接调用视频生成能力生成短剧 beat，不要先打开 Flowith 画布。
- 每个 beat 使用一个独立 prompt 文件作为输入，提交内容必须是该文件完整正文。
- 生成模型固定为 `Seedance 2.0`。
- 参数固定为 `480p`、`9:16`、`15s`。
- 同一集的 `Beat1`、`Beat2`、`Beat3`、`Beat4` 是独立任务，默认并行提交。
- 生成结果要保存回当集 workspace Files 目录，并保留清晰文件名或记录来对应 beat 顺序。

### 8.2 Flowith fallback

- 只有 Matrix 视频生成不可用、用户明确指定 Flowith、或需要沿用既有画布上下文时，才 fallback 到固定 Flowith 画布。
- fallback 时必须使用 `canvas-cowork` 打开固定生产画布 URL。
- 不要新建画布，不要换到其他画布，除非用户明确要求。
- 如果 `canvas-cowork` 当前能力支持批量提交，优先使用 `submit-batch`。
- fallback 时仍然要保持四个 beat 在同一固定画布中并行生成。

### 8.3 并行失败时的回退

- 如果平台限制导致四个 beat 无法真正并行，可以按顺序重试。
- 回退时仍然不能改 prompt 正文，也不能改参数规格。
- 回退发生后，要在任务结果中明确说明这次没有完成真正并行，以及使用的是 Matrix 还是 Flowith fallback。

### 8.4 生成完成检查

进入后期前，必须确认:

- `Beat1` 到 `Beat4` 都已生成
- 输出都能识别对应 beat 顺序
- 四个片段都成功导出或可供后续导出

## 9. 阶段 D：后期拼接、字幕与 1080p 导出

### 9.1 基础设施

后期字幕默认使用 workspace 内随 workplace 打包的可移植工具，不要只依赖某一集历史产物：

- 主脚本：
  `$NEO_WORKSPACE_ROOT/skills/empire-of-dust-youtube-pipeline/scripts/auto_subtitle_episode.py`
- 依赖清单：
  `$NEO_WORKSPACE_ROOT/skills/empire-of-dust-youtube-pipeline/requirements-subtitles.txt`
- 环境检查 / 恢复脚本：
  `$NEO_WORKSPACE_ROOT/skills/empire-of-dust-youtube-pipeline/scripts/setup_subtitle_env.sh`
- 使用说明：
  `$NEO_WORKSPACE_ROOT/skills/empire-of-dust-youtube-pipeline/references/subtitle-infrastructure.md`

导出 workplace 给别人后，先在 workplace 根目录执行：

```bash
export NEO_WORKSPACE_ROOT="$PWD"
bash skills/empire-of-dust-youtube-pipeline/scripts/setup_subtitle_env.sh
```

基础依赖至少包括：

- `ffmpeg` / `ffprobe`
- `faster-whisper`

如果目标机器缺少 `ffmpeg`，报告需要安装系统级 `ffmpeg`；不要把历史 `subs_clean`、`whisper` 或某集临时 shell 脚本当作可移植基础设施。

### 9.2 拼接规则

- 按 `Beat1 -> Beat2 -> Beat3 -> Beat4` 的顺序拼接。
- 默认用 `auto_subtitle_episode.py` 一次完成逐 beat 转写、SRT 生成、字幕烧录、拼接与 `1080x1920` mp4 导出，例如：

```bash
python3 "$NEO_WORKSPACE_ROOT/skills/empire-of-dust-youtube-pipeline/scripts/auto_subtitle_episode.py" \
  --episode-dir "$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode XX" \
  --output "$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust｜episode XX/Empire of Dust Episode XX final.mp4"
```

- 生成一个完整成片，不要上传散片。

### 9.3 字幕规则

- 有人物念白的片段必须有字幕。
- 没有念白的片段不要强行加无意义字幕。
- 字幕内容必须以最终生成视频里的实际音频为准，不以剧本原文为准。
- 先用 `faster-whisper` 对每个 beat 单独转写并拿到时间轴，再决定该 beat 是否需要字幕。
- 如果剧本文本与识别文本只有轻微差异，可以在**保留原分段和时间轴**的前提下做少量纠字；不要为了贴近剧本而重写整段字幕。
- 不要手工重写字幕分句和时间轴去“还原剧本”，除非已经逐句回听并确认与实际音频一致。
- 如果生成音频出现合句、漏词、额外词或措辞变化，字幕应忠实反映成片音频，而不是强行改回剧本台词。
- 单独烧录每个 beat 的字幕后，要抽查每个 beat 的开口时间、断句和收句是否贴音；至少检查首句是否过早、末句是否被截断。
- 最终字幕应烧录进导出的主成片，除非用户明确要求外挂字幕。

### 9.4 导出规则

- 最终导出规格为 `1080x1920`。
- 保留竖屏比例。
- 优先输出通用上传格式，例如 `mp4`。
- 导出后至少检查:
  - 时长约 `1 minute`
  - 画幅为 `9:16`
  - 四段顺序正确
  - 字幕在需要的片段中可见
  - 逐段抽查字幕是否贴音，至少检查每段首句和尾句
  - 文件可直接上传

## 10. 阶段 E：YouTube Shorts 发布

### 10.1 准备标题、简介、标签

- 先从发布文案文档中取当集对应的标题、简介、标签。
- 如果文档中缺少该集内容，再根据当集剧本与 prompts 撰写。
- 无论文案从哪里来，最终简介都必须包含以下句子:
  `Thanks everyone for loving my original AI short dramas! If you're interested in other storylines, feel free to subscribe to my channel and check out my playlists!`
- 如果简介里已经有这句，就不要重复添加。

### 10.1.1 发布前字段核对

发布文案源（CSV 或用户本轮明确给出的文案）是权威来源。把标题、简介、标签填入 YouTube Studio 后，agent 必须重新读取页面当前输入框里的值，并与权威来源逐字比对。

- 标题必须逐字一致，包括大小写、标点、撇号、竖线、空格和集数格式。
- 简介必须包含权威文案中的每一行，且必带简介句不能丢失或重复。
- 如果页面值和权威来源不一致，由 agent 立即修正并再次读取核对。
- 只有核对一致后才能点击发布或完成最终确认。
- 不要把这一步转交给用户检查；除非 YouTube 页面阻塞、登录、验证码或权限问题需要人工操作。

### 10.2 上传规则

- 上传对象是完整的 `1 minute` 主成片，而不是四个 beat 散片。
- 发布目标是 `YouTube Shorts` 频道。
- 播放列表必须选择 `Empire of Dust`。
- 点击最终发布前，再做一次“权威标题 == YouTube Studio 标题输入框当前值”的精确字符串核对。
- 发布完成后尽量记录:
  - 剧集编号
  - 最终标题
  - 最终简介
  - 最终标签
  - 视频 URL
  - 视频 ID
  - 发布时间

## 11. 阶段 F：每日数据复盘与 dashboard 更新

- 每一集发布后都要回看该视频的当前后台数据。
- 每一集都要更新 dashboard，不要等到整季结束再补。
- 如果用户没有指定 dashboard 位置，就更新默认 dashboard，并在任务结果里说明更新位置。

优先记录这些字段:

- 剧集编号
- 视频标题
- 视频 URL
- 发布时间
- views
- impressions
- average view duration
- likes
- comments
- 备注或异常

如果某些字段暂时没有数据:

- 先写入已有数据
- 将缺失项标记为 `pending`

## 12. 阶段 G：整季完成后的杀青项目报告书

当全部剧集都已发布完成后，`数据分析与内容策略部门` 必须输出杀青项目报告书。

如果用户没有指定报告路径，默认输出到:

- `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust/Empire of Dust 杀青项目报告书.md`

报告至少包含:

- 项目概览
- 总发布周期与总集数
- 最佳表现剧集
- 最弱表现剧集
- 标题与简介包装经验
- 留存、互动、点击或完播层面的有效发现
- 生产链路中的瓶颈
- 对后续短剧任务的建设性建议

## 13. 默认执行顺序

当用户丢给你剧本文件和发布文案文档，并要求开始这套工作流时，默认顺序如下:

1. 检查 Matrix 视频生成能力是否可用；只有需要 Flowith fallback 时才检查 `canvas-cowork`
2. 检查剧本源文件与发布文案文件
3. 拆出全季 prompts 到 `$NEO_WORKSPACE_ROOT/storage/files/empire-of-dust-youtube-pipeline/production/Empire of Dust`
4. 判断今天应当生产的剧集
5. 首选在 Matrix 中并行生成该集四个 beat；必要时 fallback 到固定 Flowith 画布
6. 拼接、加字幕、导出 `1080x1920` 主成片
7. 准备或撰写标题、简介、标签
8. 上传 `YouTube Shorts`
9. 加入 `Empire of Dust` 播放列表
10. 更新 dashboard
11. 第二天继续下一集
12. 全季完成后生成杀青项目报告书

## 14. 失败处理

- 如果 Matrix 视频生成不可用，且用户未允许或无法使用 Flowith fallback，停止在生成阶段并报告阻塞。
- 如果使用 Flowith fallback 时固定画布 URL 无法访问，立即停止，并报告画布阻塞。
- 如果使用 Flowith fallback 时缺少 `canvas-cowork`，立即停止。
- 如果找不到指定剧集的四个 beat prompt 文件，先尝试从剧本源文件补齐；仍失败再停止。
- 如果剧本源文件与分集目录内容冲突，以分集目录为主，master 文件为校验参考，并报告冲突。
- 如果四个 beat 中任意一个生成失败，可以在不改变 prompt 正文和参数的前提下安全重试一次。
- 如果后期基础设施缺失且无法安装，停止在导出阶段，并报告是 `ffmpeg`、字幕对齐工具还是其他依赖缺失。
- 如果发布文案文件找不到，先尝试回退匹配；仍然找不到时，再根据当集内容撰写文案。
- 如果上传成功但播放列表加入失败，保留上传结果，并单独报告播放列表步骤失败。
- 如果 dashboard 不可用，先保留当次数据，再报告更新阻塞。
- 如果整季任务已经全部完成，后续日更任务不再重复上传，而是进入或结束于杀青复盘。

## 15. 完成标准

### 单集完成标准

- 当集四个 beat prompts 已存在且正确
- 四个 beat 已在固定画布中完成生成
- 已完成拼接、字幕与 `1080x1920` 导出
- 已成功上传到 `YouTube Shorts`
- 已加入 `Empire of Dust` 播放列表
- 已更新 dashboard

### 整季完成标准

- 所有剧集都已完成单集完成标准
- 总运行天数与剧集数一致
- 没有遗漏未发布剧集
- 杀青项目报告书已产出
