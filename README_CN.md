# AI 短剧 Agent 公司

> [🌐 English](./README.md) | 中文

---

# AI 短剧 Agent 公司

一个完整的 **Matrix 部门模板包**，用于运营 AI 短剧制作公司 —— 从市场调研到剧本生成、视频制作、YouTube 发布和数据分析。

> 基于 [Matrix](https://matrix.build) — AI 公司操作系统。导入这些部门即可快速搭建你的 AI 短剧工作室。

## 你将获得什么

- 🎬 **端到端短剧流水线** — 从主题到 20 集季度剧本到 YouTube Shorts 发布
- 📝 **剧本生成** — 原创剧本，每集 4×15 秒节拍结构，支持中英双语
- 🎨 **分镜提示词** — Seedance 2.0 提示词包，可直接用于 AI 视频生成
- 📊 **分析与策略** — 仪表盘追踪、留存分析、内容策略评审
- 🔬 **市场调研** — 趋势捕捉、爆款机制分析、创意信号处理
- 📺 **YouTube 发布** — 自动上传、播放列表管理、发布证据追踪

## 真实成果

这套系统制作了 **Empire of Dust** YouTube Shorts 系列 —— 累计 70 万+ 播放量。

在线观看：https://www.youtube.com/@BreakDu-f6b/shorts

## 部门结构

```
ai-short-drama-agent-company/
├── skills/                          # 可复用的工作区级技能
│   ├── short-drama-meta-os/         # 主题 → 20 集季度剧本包
│   ├── short-drama-production-pipeline/  # 制作执行与 QA
│   ├── short-drama-research-intake/ # 调研 → 创意燃料
│   ├── seedance-prompt-splitter/    # 剧本 → Seedance 2.0 分镜提示词
│   └── empire-of-dust-youtube-pipeline/  # 完整 YouTube 发布流水线
├── departments/
│   ├── content-generation-and-distribution/
│   │   └── memory/knowledge/        # 制作、QA、发布记忆
│   ├── data-analysis-and-content-strategy/
│   │   └── memory/knowledge/        # 分析、仪表盘、策略记忆
│   └── short-drama-research/
│       └── memory/knowledge/        # 市场调研、趋势分析记忆
└── demo/
    └── empire-of-dust/              # 真实制作示例
        ├── MANIFEST.md
        ├── EPISODE_ARTIFACT_INDEX.md
        ├── episode-01/              # 4 个分镜提示词文件
        ├── episode-02/              # 4 个分镜提示词文件
        └── episode-03/              # 4 个分镜提示词文件
```

## 包含的技能

### `short-drama-meta-os`
将任意用户主题开发为原创爆款短剧项目包，包含 20 集季度、4×15 秒节拍结构、Seedance 2.0 提示词文件夹计划和社媒分发 CSV 草稿。

### `short-drama-production-pipeline`
将已批准的项目包转化为制作执行：验证 Seedance 2.0 分镜提示词、准备参考图需求、协调视频生成交接、拼接、字幕、QA 和分发交接。

### `short-drama-research-intake`
将存储的短剧调研信号转化为安全的创意燃料，用于元系统、制作、打包或分析。

### `seedance-prompt-splitter`
将剧集剧本文件夹转换为每集的 Seedance 2.0 分镜提示词文件夹。

### `empire-of-dust-youtube-pipeline`
完整流水线：拆分剧本为 Seedance 2.0 提示词 → 每集生成 4 个片段 → 拼接为 1080×1920 带字幕成片 → 发布到 YouTube Shorts → 更新播放列表 → 生成季度报告。

## 部门记忆

### Content Generation & Distribution（内容生成与分发）
负责端到端视频生成和分发。记忆包括：
- Empire of Dust 流水线状态与恢复
- 短剧工厂方法
- 媒体 QA 证据要求
- 音频/字幕边界规则
- Apple Silicon 本地音频流水线
- YouTube 和 TikTok 发布证据门控
- Seedance 配额错误处理
- 制作调度与前置条件规则

### Data Analysis & Content Strategy（数据分析与内容策略）
负责仪表盘更新、分析评审和内容策略。记忆包括：
- Empire of Dust 分析模式
- 空闲重踢纪律
- 结晶门控重踢盲区
- 收件箱计数器模式

### Short-Drama Research（短剧调研）
负责市场调研和创意信号捕捉。记忆包括：
- 四拍竖屏剧集引擎
- 品牌短剧市场参考包
- 产品即机制模式
- 海外爆款短剧参考
- 北美科幻日常伦理
- 调研来源边界与存储合约

## 示例：Empire of Dust

`demo/empire-of-dust/` 文件夹包含 Empire of Dust YouTube Shorts 系列前 3 集的真实制作产物：

- `MANIFEST.md` — 项目清单
- `EPISODE_ARTIFACT_INDEX.md` — 完整剧集索引
- `episode-01/` 到 `episode-03/` — 每集包含 4 个 Seedance 2.0 分镜提示词文件（Beat1-Beat4）

每个节拍是 15 秒视频片段提示词，适用于 Seedance 2.0 480p、9:16 竖屏生成。每集 4 个节拍 = 60 秒内容。

**观看真实成果：** https://www.youtube.com/@BreakDu-f6b/shorts

## 使用方法

### 导入 Matrix

1. 打开 [Matrix](https://matrix.build)
2. 创建新工作区或使用现有工作区
3. 创建与上述结构匹配的三个部门
4. 将 `skills/` 复制到工作区技能目录
5. 将每个部门的 `memory/knowledge/` 复制到对应部门根目录
6. 开始制作短剧

### 独立参考

将技能、记忆和示例产物作为参考材料，用于构建你自己的 AI 短剧制作系统。

## 环境要求

- [Matrix](https://matrix.build) 账号（用于完整的 Agent 公司集成）
- Seedance 2.0 或兼容的 AI 视频生成工具
- Matrix 中连接 YouTube 集成（用于发布）

## 开源协议

MIT — 随意使用、fork、发布。