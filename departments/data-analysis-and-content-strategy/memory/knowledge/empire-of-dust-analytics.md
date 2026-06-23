---
title: Empire of Dust 数据复盘、dashboard 字段与杀青报告结构
confidence: H
tag: knowledge
created: 2026-04-23
source: 部门初始化时从 Empire of Dust YouTube 流水线与复盘流程固化；2026-05-07 Ep13 dashboard 处理确认发布档案与真实表现分析必须分开表述
description: Dashboard 字段、杀青报告结构、真实指标边界与部门协作边界
---

# Empire of Dust 数据与策略参考

## Dashboard 每集字段

- 剧集编号
- 视频标题
- 视频 URL
- 发布时间
- views
- impressions
- average view duration
- likes
- comments
- 备注 / 异常

缺失字段标 `pending`，不编造。

如果收到较后集数的完整发布结果，但中间集数缺少发布档案，不要把 dashboard 做成连续已完成状态：只更新有证据的剧集，把缺口剧集显式标为发布档案待补 / early metrics pending，并在回执中说明边界。

## 真实表现分析边界

本部门完成发布档案记录，不等于已经完成 YouTube 表现分析。只有从 YouTube Studio 或可信后台来源拿到 views、impressions、average view duration、likes、comments 等实际指标后，才能说完成了性能复盘；否则只能表述为“发布信息已记录，早期指标 pending”。

## 默认输出

- Dashboard 位置：若用户未指定，更新工作区默认 dashboard，并在任务结果里说明更新位置。
- 杀青报告默认路径：`/Users/flowith-mac-mini-001-user/Downloads/Empire of Dust /Empire of Dust 杀青项目报告书.md`

## 杀青报告结构

- 项目概览
- 总发布周期与总集数
- 最佳表现剧集
- 最弱表现剧集
- 标题与简介包装经验
- 留存 / 互动 / 点击 / 完播层面的有效发现
- 生产链路瓶颈
- 对后续短剧任务的建设性建议

## 协作对象

- 上游：`内容分发部门` id `b3e2d81f`（发布结果来源）
- 上游：`内容生产部门` id `7c4f9a21`（生产链路瓶颈来源）
- 出口：CEO Office id `8591249c`（执行视角的汇报）


<!-- backlinks:auto -->
## Backlinks

- [[youtube-studio-scraping-boundary]]
<!-- /backlinks:auto -->
