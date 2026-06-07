---
title: "长周期 Agent 系统工程模式：任务规划、状态持久化与故障恢复"
created: "2026-06-06"
updated: "2026-06-06"
status: pending
owner: hermes
priority: P2
domain: "Multi-Agent-Orchestration"
review_after: "2026-06-20"
tags:
  - learning-task
  - hermes
  - long-running-agents
  - agent-engineering
  - task-orchestration
  - fault-tolerance
  - state-management
---

# 长周期 Agent 系统工程模式：任务规划、状态持久化与故障恢复

## Why Now

2026-06-06，一篇关于「构建可运行一周的 Agent 系统」的工程实践文章引发关注。这不是框架文档或学术论文 — 而是**一线工程师的系统化实战总结**，覆盖了超长周期 Agent 面临的核心工程挑战：任务分解、状态检查点、错误恢复、资源预算管理。

时机成熟的原因：
1. **Agent 正从「单轮对话」走向「长周期任务」** — Stripe Minions 每周合并 1300+ PR，Codex/Claude Code 需要数小时完成复杂重构，Hermes 的 cron scout 要跨天追踪信号
2. **理论基础已有** — Agent Memory (`agent-memory-architecture` P1)、模型架构 (`agent-model-architecture` P1)、路由优化 (`agent-routing-longrunning` P2) 三个 pending 任务覆盖了「记忆」「模型」「路由」维度，但缺少**系统工程视角** — 如何把这些组件串成一个能跑一周不崩的系统
3. **Tony 的 Hermes Cognitive OS 直接受益** — cron jobs、多 agent 编排、长时间运行的学习任务都需要这些工程模式

**为什么独立于 `agent-routing-longrunning`**：那个任务关注的是模型选择和推理优化（vLLM 会话感知路由 + Nemotron 3 Ultra）。本任务关注的是**系统级工程** — 不是"选哪个模型跑得快"，而是"怎么设计系统让它跑一周不崩"。

## Source

- URL: https://levelup.gitconnected.com/building-a-week-long-running-agentic-system-2ad79f8190bb
- Source note: 2026-06-06 下午 curated-scout 增量雷达 #4
- Captured evidence: `00-Inbox-AI/hermes/curated-scout/20260606-150000-afternoon-digest.md` #22-#24

## Suggested Domain

`Multi-Agent-Orchestration`

## Desired Output

playbook

## Proposed Canonical Destination

- `30-Playbooks/Agent-Engineering/longrunning-agent-patterns.md`
- `20-Maps/agent-architecture-decision-map.md`（更新）

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## 研究路径建议

1. 精读源文章，提取核心工程模式：
   - 任务规划与分解策略（DAG vs 线性流水线 vs 自适应重规划）
   - 状态持久化方案（检查点设计、增量状态 vs 全量快照）
   - 错误恢复机制（重试策略、优雅降级、人工介入触发条件）
   - 资源管理（上下文窗口预算、token 成本控制、内存管理）
2. 横向对比 Stripe Minions 的长周期任务管理模式（已在 `deepdive-growth` 中覆盖）
3. 研究分布式系统中的经典容错模式（Saga、Circuit Breaker、Bulkhead）在 Agent 场景的适用性
4. 对照 Hermes 当前的 cron job 架构，识别可改进的工程点
5. 产出：长周期 Agent 系统工程模式 playbook + Hermes 改进建议

## Suggested Review Date

`2026-06-20`

## Safety Notes

无敏感内容。研究的是通用工程模式，适用于 Tony 的个人 Agent 系统设计。

## Hermes Recommendation

- Decision: `study`
- Rationale: Tony 的 Hermes Cognitive OS 正在从「单次任务」走向「持续运行」— cron scouts 跨天追踪、多 agent 编排、长时间研究任务。长周期 Agent 的工程模式是必须掌握的基础能力。与 `agent-routing-longrunning`（路由/推理优化）、`agent-memory-architecture`（记忆持久化）、`deepdive-growth`（Stripe Minions 工业化实践）形成 Agent 工程四件套。

## Follow-Up Proposal

- Suggested review cadence: 2 周
- Suggested spaced review prompt: 「长周期 Agent 的哪个工程模式对 Hermes cron jobs 最有直接改进价值？」
