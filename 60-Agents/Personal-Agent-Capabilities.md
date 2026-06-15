---
title: "Personal Agent Capabilities"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - agents
  - capabilities
  - ai-first
---

# Personal Agent Capabilities

这页不是新增一批独立 Agent，而是把 Tony 个人知识系统里的 Agent 能力映射到已经存在的 Hermes / Codex 工作流。

核心原则：

```text
workflow first, persona second
```

Agent 名称可以作为调用入口和心智标签，但不能覆盖现有目录、队列和 review gate。

## Capability Map

| Capability Alias | Primary Owner | Existing Workflow | Output Surface |
|---|---|---|---|
| `tony-research-scout` | Hermes | core radar, topic scout, curated scout | `00-Inbox-AI/hermes/curated-scout/`, `00-Inbox-AI/signals/`, `00-Inbox-AI/candidates/` |
| `tony-learning-coach` | Hermes + Codex | growth track -> learning task -> learning package | `00-Inbox-AI/learning-tasks/` |
| `tony-gardener` | Codex + Hermes | memory review, review queue, knowledge evolution, promotion gate | `00-Inbox-AI/review-queue/`, `10-Knowledge/`, `20-Maps/`, `30-Playbooks/` |
| `tony-project-companion` | Codex | project state review and next-action maintenance | `40-Projects/`, `00-Inbox-AI/project-companion/` |
| `tony-reflection` | Hermes + Tony + Codex | weekly synthesis and review decisions | `00-Inbox-AI/reports/`, `00-Inbox-AI/review-queue/` |
| `tony-toolsmith` | Codex | rules, prompts, skills, scripts, integrations | `90-Agent-System/`, root-level executable assets |
| `tony-system-thinking` | ChatGPT Desktop + Codex | complex problem framing, trade-off mapping, MOC shaping | `00-Inbox-AI/`, `20-Maps/`, `90-Agent-System/decisions/` |
| `tony-writing-partner` | ChatGPT Desktop + Codex | draft, compress, rewrite, publishable output shaping | `00-Inbox-AI/`, future `50-Outputs/` |

## Boundary Rules

- 不为每个 alias 单独创建一套目录、cron 和规则。
- 新 alias 只有在它能绑定到明确队列、产物和 review gate 时才进入系统。
- Hermes 负责长期 scout / recall / reminder，不直接写 canonical knowledge。
- Codex 负责整理、结晶、入库、项目维护和 Git checkpoint。
- Tony 保留 promote / defer / discard / build 的最终判断权。

## Current First-Class Workflows

- [[90-Agent-System/workflows/hermes-codex-learning-chain]]
- [[90-Agent-System/workflows/knowledge-evolution]]
- [[90-Agent-System/workflows/memory-sync]]
- [[90-Agent-System/workflows/project-companion]]
- [[00-Inbox-AI/hermes/automations/hermes-cron-matrix]]

## What To Add Next

优先补齐 `tony-project-companion`，因为 Hermes/Codex 已经覆盖了 research、learning、memory review 和 weekly synthesis，但项目持续推进还没有固定队列。

