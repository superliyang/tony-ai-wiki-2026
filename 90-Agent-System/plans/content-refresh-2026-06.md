---
title: "内容更新迭代计划"
created: 2026-06-18
updated: 2026-06-18
status: active
tags:
  - agent-system
  - content-refresh
  - knowledge-maintenance
---

# 内容更新迭代计划

这份计划用于把主知识库从“结构已整理”推进到“内容持续新鲜”。当前日期是 2026-06-18。最近已经完成的是正式域骨架；真正需要更新的是过去几个月快速变化的正文事实、项目状态、工具选择和领域判断。

## 判断

主库现在有两个层次：

| 层次 | 状态 | 更新方式 |
|---|---|---|
| 结构层 | 刚完成一轮整理，基本可用 | 小修导航，不大改目录 |
| 内容层 | 需要刷新，尤其是 fast-moving 领域 | 按领域小批调研、提升、回链 |

不要把“更新内容”做成新闻堆积。每次更新都应该回答：

```text
这个变化是否改变我的判断、学习路径、项目选择或系统设计？
```

## Freshness Tiers

| Tier | 领域 | 刷新频率 | 原因 |
|---|---|---|---|
| F1 快速变化 | AI, AI Engineering, AI Open Source | 每 2-4 周 | 模型、agent 工具、开源项目、eval/serving 栈变化快 |
| F2 中速变化 | Security, International Payments, Advertising | 每 1-2 月 | 法规、平台规则、欺诈、支付市场、投放生态会变 |
| F3 慢速变化 | Personal Knowledge System, Playbooks, Agent System | 按系统变更触发 | 主要跟随自己的工作流演化 |
| F4 旧库保留 | Big Data, Cloud Native, Engineering Management, English, Macro Insight | 按需触发 | 暂不默认更新，避免主库发散 |

## Refresh Batch Order

### Batch 0: Freshness Audit

目标：先知道哪些内容最该更新。

输出：

- [[20-Maps/内容更新雷达]]
- 每个核心领域的 `学习进度.md` 加一段 `Freshness`。
- working vault 中生成调研任务清单。

### Batch 1: AI / AI Engineering

目标：刷新模型、agent runtime、evaluation、serving、memory、tool use 的判断。

重点问题：

- 最近模型能力和产品形态是否改变学习路径？
- Agent runtime / workflow / harness 的主流做法是否变化？
- eval、observability、release gate 工具是否有新的事实和取舍？
- 本地 AI / Mac AI lab 是否需要更新工具链？

目标入口：

- [[10-Knowledge/AI/学习路径]]
- [[10-Knowledge/AI-Engineering/学习路径]]
- [[10-Knowledge/AI-Engineering/04-Evaluation/评测索引]]
- [[10-Knowledge/AI-Engineering/05-Deployment/部署索引]]

### Batch 2: AI Open Source

目标：把 Hermes / Codex 的开源项目发现变成项目体系，而不是散点 repo。

重点问题：

- 哪些项目进入 Watchlist？
- 哪些项目已经降温、停滞或被替代？
- 哪些项目体现新的工程模式？
- Unsloth 这类项目是否值得成为第一批正式项目卡？

目标入口：

- [[10-Knowledge/AI-Open-Source/学习路径]]
- [[10-Knowledge/AI-Open-Source/03-Projects/项目索引]]
- [[10-Knowledge/AI-Open-Source/04-Patterns/模式索引]]
- [[10-Knowledge/AI-Open-Source/09-Watchlist/Watchlist 索引]]

### Batch 3: Security

目标：刷新 AI / agent security、供应链安全、合规和 incident case。

重点问题：

- Agent tool permission、sandbox、MCP / connector 风险是否需要新控制点？
- 安全事件和供应链案例是否改变 playbook？
- AI 产品安全控制清单是否需要更新？

目标入口：

- [[10-Knowledge/Security/学习路径]]
- [[10-Knowledge/Security/03-Industry-Controls/行业控制索引]]
- [[10-Knowledge/Security/08-Playbooks/Playbook 索引]]
- [[10-Knowledge/Security/09-Case-Studies/案例复盘索引]]

### Batch 4: International Payments / Advertising

目标：刷新业务领域里会影响判断的变化。

重点问题：

- 支付成功率、3DS、拒付、PSP / acquirer、市场本地化是否有新变化？
- 广告投放平台、归因、SKAN、fraud、增量实验是否有新规则或新口径？

目标入口：

- [[10-Knowledge/International-Payments/学习路径]]
- [[10-Knowledge/Advertising/专题总览]]

## Research And Promotion Workflow

每个 batch 都走同一条链路：

1. Hermes 或 Codex 先在 working vault 做调研。
2. 原始材料进入 `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/10-Generated/`。
3. 候选进入 `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/`。
4. Codex 判断内容类型：project / topic / pattern / map / playbook / case-study。
5. 只把稳定判断提升到主库。
6. 更新专题总览、学习路径、索引、地图和恢复笔记。
7. 记录 promotion log。

完整流程见 [[90-Agent-System/workflows/knowledge-intake-and-promotion]]。

## Source Quality Rule

更新内容时区分三类来源：

| Source Type | 用途 | 处理 |
|---|---|---|
| Primary / Official | 模型、API、法规、平台规则、项目 release | 可作为事实依据 |
| High-signal Analysis | 趋势、比较、生态判断 | 只能作为判断参考 |
| Social / Newsletter / Blog | 发现线索 | 进入候选，不直接写成结论 |

凡是会随时间变化的内容，都必须写明 `as_of: 2026-06-18` 或具体来源日期。

## Update Output Shape

每轮更新不追求“补全”，只交付一个 bounded slice：

| Output | Example |
|---|---|
| refreshed index | `AI-Open-Source/09-Watchlist/Watchlist 索引.md` |
| new project card | `AI-Open-Source/03-Projects/Unsloth.md` |
| updated pattern | `AI-Open-Source/04-Patterns/单 GPU 微调内存优化.md` |
| updated map | `20-Maps/核心知识网络.md` |
| progress update | `10-Knowledge/*/学习进度.md` |

## Human Review Questions

Tony 每轮只需要判断这些：

1. 这个方向是否值得继续跟？
2. 它改变了我们的学习路径吗？
3. 它应该进入主库，还是留在 working vault？
4. 它是否值得输出到飞书？

## Current Next Step

建议先跑 Batch 0，然后从 Batch 1 开始。

最小下一步：

1. 建立 [[20-Maps/内容更新雷达]]。
2. 为 Hermes 生成 AI / AI Engineering / AI Open Source 的调研任务。
3. 用一个具体项目或主题跑完整更新链路。
