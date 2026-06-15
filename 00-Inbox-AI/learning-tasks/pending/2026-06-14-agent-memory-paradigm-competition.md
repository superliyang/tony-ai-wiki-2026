---
title: "Agent 记忆的范式之争：KV-Cache 原生 vs 图谱/文档架构"
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
  - agent-memory
  - kv-cache
  - memart
  - mragent
  - engram
  - paradigm-competition
sources:
  - "https://openreview.net/pdf?id=YolJOZOGhI"
  - "https://arxiv.org/html/2606.06036v1"
  - "https://arxiv.org/html/2606.09900v1"
  - "https://arxiv.org/html/2606.06787"
  - "https://arxiv.org/html/2606.06090v1"
  - "https://arxiv.org/html/2606.07711"
---

# Agent 记忆的范式之争：KV-Cache 原生 vs 图谱/文档架构

## Why Now

2026 年 6 月 12-14 日，出现了 8 篇 Agent 记忆相关的 arXiv 论文，标志着 Agent 记忆研究从"百花齐放"进入"范式竞争"阶段。两条清晰的竞争路线浮现：

**路线 1: 图谱/文档派**
- MRAgent: Cue-Tag-Content 图谱 + 主动重建 (+23.3% LoCoMo)
- Infini Memory: 主题文档记忆架构 (64.7% MemoryAgentBench)
- Engram: 双时态知识图谱 (8× fewer tokens, +10.4 分)
- AdMem: 统一语义/情景/程序性 + 多 Agent
- 核心思路: 记忆与模型分离，通过结构化检索提供上下文

**路线 2: KV-Cache 原生派**
- MemArt: 将记忆存储在模型的 KV Cache 中 (91-135× prefill 减少, +11% 准确率)
- 核心思路: 记忆嵌入模型内部，通过潜在空间注意力分数检索

对 Tony/Hermes 的影响：
- Hermes 当前使用基于文件的记忆系统（memory tool），更接近"文档派"
- MemArt 的 KV-Cache 原生范式如果成熟，可能从根本上改变 Agent 架构设计
- 这场范式之争的结果将决定下一代 Agent 系统的技术栈选择

## Source

- URL: 见 frontmatter sources
- Source note: arXiv 论文 ×6 + OpenReview ×1
- Captured evidence: 详见 `00-Inbox-AI/hermes/curated-scout/20260614-090000-morning-digest.md` 主线 D

## Suggested Domain

`Agent-Architecture`

## Desired Output

- comparison map（两条路线的技术对比 + 优劣分析 + 对 Hermes 的技术启示）

## Proposed Canonical Destination

- `10-Knowledge/AI/06-Maps/Agent-Memory-Paradigm-Comparison.md`

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## Suggested Review Date

`2026-07-05`

## Safety Notes

无。

## Hermes Recommendation

- Decision: `study`
- Rationale: Agent 记忆是 Hermes 的核心架构组件。MemArt 的 KV-Cache 原生范式如果被验证为可行且高效，可能成为 2027 年 Agent 系统的标准架构。需要提前理解两条路线的优劣，为 Hermes 的架构演进提供决策依据。可与已有的 `agent-memory-architecture-package`(P1 in-progress) 互补——本任务聚焦"范式对比"而非"实施指南"。

## Follow-Up Proposal

- Suggested review cadence: 7 月再扫描一次 Agent 记忆论文，看范式竞争是否有新进展
- Suggested spaced review prompt: "KV-Cache 原生 Agent 记忆的最新进展？MemArt 是否有后续工作？图谱/文档派是否有反击？"
