---
title: "LLM 前缀缓存工程深度：驱逐策略如何从节省 80% 变成 5%"
created: 2026-06-07
updated: 2026-06-07
status: pending
owner: hermes
priority: P2
domain: "AI-Engineering"
review_after: "2026-06-14"
tags:
  - learning-task
  - hermes
  - llm-inference
  - prefix-caching
  - cost-optimization
  - engineering
  - infrastructure
---

# LLM 前缀缓存工程深度：驱逐策略如何从节省 80% 变成 5%

## Why Now

2026-06-07，DEV Community 发表了一篇 LLM 推理优化的深度工程文章：**大规模前缀缓存（Prefix Caching）——理论上可节省 80% Prefill 成本，但不当的驱逐策略（eviction policy）可以将其效果悄悄降至 5%。**

**为什么这值得 Tony 关注：**

1. **AI 工程化的核心痛点**：Tony 关注 AI 工程化。LLM 推理成本是 AI 系统从原型到生产的关键瓶颈。前缀缓存是当前最有效的 Prefill 成本优化手段之一，但工程实践中充满陷阱。

2. **「理论 vs 工程」的经典案例**：这篇文章不是论文，而是生产环境的血泪教训——它展示了一个技术从「论文里 80% 优化」到「生产里 5% 效果」的典型退化路径。这种「理论到工程的 gap」正是 Tony 关心的 AI 工程化核心问题。

3. **与推理优化信号群联动**：同一扫描窗口内有 Modular 的新型推理路由器、SHBF 稀疏注意力、Gemma4 CUDA 优化等多条推理优化信号。前缀缓存是其中最「工程落地」的一篇。

4. **与 pending 任务的差异**：没有现有 pending 任务覆盖 LLM 推理成本优化这个维度。`agent-routing-longrunning` 关注的是 Agent 层面的路由，不是推理基础设施。

## Source

- URL: https://dev.to/tech_nuggets/prefix-caching-at-scale-when-it-saves-you-80-of-prefill-cost-and-the-eviction-policies-that-5e8
- Source note: `00-Inbox-AI/hermes/curated-scout/20260607-150027-summary.md` (条目 #10)
- Captured evidence: 早间和下午扫描均捕获，被策展人评为「工程实践中的宝贵经验」

## Suggested Domain

`AI-Engineering` / `Infrastructure`

## Desired Output

- learning package

## Proposed Canonical Destination

Hermes 建议但不写入：
- `10-Knowledge/AI-Engineering/05-Topics/LLM 前缀缓存工程实践.md`
- `30-Playbooks/LLM 推理成本优化检查清单.md`

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## Suggested Review Date

`2026-06-14`

## Safety Notes

无隐私/安全/财务/法务风险。纯工程实践研究。

## Hermes Recommendation

- Decision: `study`
- Rationale: 这是 AI 工程化的高价值 practical knowledge，不是新闻摘要。建议 Codex 以本文为主线，横向对比：(1) 不同缓存驱逐策略（LRU/LFU/TTL/混合）的适用场景；(2) Prefix Caching vs KV Cache 的区别与协同；(3) 当前主流推理框架（vLLM, SGLang, TensorRT-LLM）的缓存实现对比。

## Follow-Up Proposal

- Suggested review cadence: 研究完成后一次性 review
- Suggested spaced review prompt: 「前缀缓存的驱逐策略选择——什么场景下 LRU 就够了，什么场景必须用更复杂的策略？」
