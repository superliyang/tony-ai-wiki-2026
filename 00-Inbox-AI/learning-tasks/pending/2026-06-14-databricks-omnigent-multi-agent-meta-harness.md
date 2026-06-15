---
title: "Databricks Omnigent：多 Agent 编排的元框架层——组合、控制与协作"
created: 2026-06-14
updated: 2026-06-14
status: pending
owner: hermes
priority: P2
domain: "Agent-Architecture"
review_after: "2026-07-05"
tags:
  - learning-task
  - hermes
  - multi-agent
  - orchestration
  - meta-harness
  - databricks
  - omnigent
  - open-source
  - agent-composition
sources:
  - "https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents"
  - "https://github.com/omnigent-ai/omnigent"
  - "https://omnigent.ai/"
---

# Databricks Omnigent：多 Agent 编排的元框架层——组合、控制与协作

## Why Now

2026 年 6 月 13 日，Databricks 以 Apache 2.0 协议开源了 **Omnigent**——一个位于现有 Agent harness（Claude Code、Codex、Pi、OpenAI Agents SDK 等）之上的"元框架"。这不是又一个 Agent 框架，而是一个**元编排层**：

- **定位**: meta-harness，位于单个 Agent harness 之"上"，解决跨 harness 的组合、治理和协作问题
- **核心洞察**: 最好的结果不再来自单一模型在单一 harness 中运行——Harvey、Anthropic Research、Databricks Genie 都采用了多 Agent 编排模式
- **关键能力**: 多 Agent 组合（一行切换 harness）、有状态上下文安全策略、实时多人协作、OS 级沙箱、成本预算控制
- **开源**: Apache 2.0，GitHub 公开

对 Tony/Hermes 的影响：
- **直接关联主题**: 多 Agent 编排是 Tony 的五大核心主题之一
- **Hermes/Codex 架构**: Hermes → Codex → OpenHuman 的 Agent 链是否需要一个 meta-harness 层来统一策略、权限和协作？
- **范式信号**: Databricks（5000+ 工程师团队）的内部实践 + 开源 = 标志着"多 Agent 编排"从实验模式走向工程化标准
- **与现有 pending 互补**: `agent-platform-industrialization` 看平台层，本任务看编排层；`code-as-interface-agent-paradigm` 看 Code 作为 Agent 接口，Omnigent 看如何统一不同 harness 的接口

## Source

- URL: 见 frontmatter sources
- Source note: Databricks 官方博客 + GitHub 仓库 + 文档站，非第三方转载
- Captured evidence: 详见 `00-Inbox-AI/hermes/curated-scout/20260614-160000-afternoon-digest.md` 增量信号 #3 和 `20260614-150025-summary.md` #3

## Suggested Domain

`Agent-Architecture`

## Desired Output

comparison map + decision memo

具体应覆盖：
1. Omnigent 架构解析（Runner → Server → Policy → Collaboration 四层）
2. 与现有 Agent 编排框架的对比定位（LangChain/LlamaIndex/CrewAI/AutoGen → 为什么 Omnigent 是"元层"而非"又一个框架"）
3. 关键设计决策：统一 API 包装 CLI agents + SDKs、有状态策略引擎、OS 沙箱
4. 对 Hermes/Codex Agent 链的启示：是否需要 meta-harness 层？哪些 Omnigent 模式可直接借鉴？
5. 行业信号：Databricks 进入 Agent 编排标准制定意味着什么？

## Proposed Canonical Destination

- `10-Knowledge/AI-Cognitive-System/06-Maps/Agent-Orchestration-Frameworks-Comparison.md`（新增或更新）
- `90-Agent-System/decisions/`（如需做架构决策）

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## Suggested Review Date

`2026-07-05`

## Safety Notes

- Omnigent 处于 alpha 阶段，功能可能不稳定——产出应标注状态
- 如涉及将 Omnigent 集成到 Hermes/Codex 流程，需先评估安全边界（OS 沙箱、权限模型）
- 分析应区分"Omnigent 当前能力"与"行业趋势判断"

## Hermes Recommendation

- Decision: `study`
- Rationale: Omnigent 不是增量改进，是范式层级的提升——"meta-harness"概念可能定义下一代 Agent 系统的编排标准。Databricks 的工程实力（5000+ 工程师内部使用后开源）赋予其超出普通开源项目的可信度。Tony 的多 Agent 编排主题需要系统性地理解这一新范式，而非仅在 scout digest 中追踪。可与 `agent-platform-industrialization`（platform 层）和 `code-as-interface-agent-paradigm`（Code 接口）互补。

## Follow-Up Proposal

- Suggested review cadence: 3 周后扫描 Omnigent GitHub 的 issue/PR 活跃度和社区采用情况
- Suggested spaced review prompt: 「Omnigent 社区采用情况？是否有其他 meta-harness 竞品出现？Databricks 是否将其集成到 Databricks 平台？」
