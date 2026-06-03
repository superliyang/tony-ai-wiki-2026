---
name: ai-agent-learning-system
description: Build or evolve a layered AI agent learning system in an Obsidian vault by separating abstract agent capabilities, concrete systems, engineering patterns, and application cases. Use when Codex needs to study AI agents deeply, compare agent products, extract engineering abstractions, connect them to real business workflows, and keep the vault restartable with maps, progress memory, and safe Git-backed maintenance.
---

# AI Agent Learning System

## Overview

Use this skill when the user is not asking for one isolated AI agent note, but for a durable AI agent study system.

This skill turns AI agent research into four connected layers:

- abstract capabilities
- concrete systems and products
- engineering patterns and governance
- application, industry, and ROI layers

Pair this skill with [$obsidian-learning-methodology](/Users/tony/.codex/skills/obsidian-learning-methodology/SKILL.md) when the whole vault topology is still being decided, and with [$knowledge-vault-research-sync](/Users/tony/.codex/skills/knowledge-vault-research-sync/SKILL.md) when the work needs wikilink validation, progress-note refreshes, and safe Git checkpoints.

## Core Outcome

A good run of this skill should leave behind:

- a cleaner AI agent learning path
- better separation between topics, systems, engineering, and applications
- updated indexes and maps
- refreshed `学习进度.md` and `恢复笔记.md` when the path changes
- comparison notes, case studies, or templates that make future study easier

## Autonomous Expansion Mode

When the user wants Codex to keep going without interruption, expand the AI agent vault in coherent versions rather than isolated edits.

In this mode:

- inspect which layer is weakest right now: capabilities, systems, engineering, or applications
- choose one slice that makes the overall path more teachable
- finish that slice end-to-end, including indexes, maps, progress, and resume pages
- reflect on what still blocks the agent line from feeling complete
- continue if the next slice is obvious
- stop only when a meaningful version boundary has been reached

Prefer this priority order when choosing the next slice:

1. fix topology problems or mixed layers
2. complete the missing layer for the current study line
3. add comparison or governance pages that make the line teachable
4. add applications and cases that prove real-world value
5. update templates and state pages so the line is restartable

Read [references/autonomous-delivery-loop.md](references/autonomous-delivery-loop.md) when using this mode.

## Default Vault Topology

For Tony's current vault, prefer this split:

### 1. Capability Layer

Use `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Learning/06-Topics` for abstract agent ideas such as:

- `Tool Use`
- `Agent Memory`
- `Planning and Control`
- `Multi-Agent Systems`
- `Agent`
- `AI Assistant`
- `Coding Agents`

### 2. System Layer

Use `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Learning/09-Systems` for concrete products, runtimes, and platforms such as:

- `OpenClaw`
- `ChatGPT Agent`
- `Claude Code`
- `Codex`
- `Cursor`
- `Devin`
- `Manus`

### 3. Engineering Layer

Use `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Engineering/07-Topics` for reusable patterns such as:

- runtime architecture
- session and memory design
- tool calling and action execution
- planning loops and state machines
- human approval gates
- long-running agent operations
- evaluation, reliability, failure recovery
- cost, latency, and safety tradeoffs

### 4. Application Layer

Use `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Applications` for where agents actually create value:

- application topics
- industries
- products and workflows
- case studies
- ROI templates
- failure reviews

## Workflow

### 1. Decide the learning layer first

Before editing, ask:

- is this an abstract capability
- is this a concrete system or product
- is this an engineering pattern
- is this an application, industry, workflow, or case study

Do not put a concrete system into the topic layer if it really belongs in `09-Systems`.

### 2. Expand in this order

Prefer this sequence when growing the AI agent vault:

1. topic indexes and maps
2. capability notes
3. concrete systems and comparison pages
4. engineering abstractions extracted from systems
5. application notes, industries, and case studies
6. templates, ROI, and failure-analysis assets

### 3. Always connect the layers

When a new AI agent note is added, consider whether these should also be updated:

- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Learning/09-Systems/系统索引.md`
- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Learning/07-Maps/AI Agent Systems Map.md`
- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Engineering/07-Topics/主题索引.md`
- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Engineering/08-Maps/地图索引.md`
- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Applications/05-Topics/主题索引.md`
- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Applications/06-Maps/地图索引.md`

### 4. Compare systems with stable dimensions

When writing comparison notes, keep the dimensions stable across products:

- task scope
- tool access
- memory model
- runtime model
- autonomy level
- approval model
- deployment mode
- observability and governance
- reliability and failure recovery
- target user or team

Read [references/comparison-dimensions.md](references/comparison-dimensions.md) when writing system comparison notes.

### 5. Preserve restartability

Update area state pages when the user's study route changes meaningfully:

- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Learning/学习进度.md`
- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Learning/恢复笔记.md`
- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Engineering/学习进度.md` when relevant
- `/Users/tony/Documents/vault/tony2026/01-Areas/AI-Applications/学习进度.md` when relevant

### 6. Prefer governance-aware application notes

For agent applications, do not stop at use cases. Also track:

- ROI proof
- adoption friction
- deployment pitfalls
- failure modes
- approval gates
- evaluation requirements

Read [references/applications-spine.md](references/applications-spine.md) when extending the application layer.

## Working Rules

- Keep abstract capabilities separate from products.
- Pull reusable engineering ideas out of product pages.
- Prefer source-backed case studies over generic hype notes.
- Update maps and indexes whenever topology changes.
- Treat progress and resume notes as first-class memory, not optional extras.
- Use Chinese explanatory writing with English technical terms preserved where helpful.
- In autonomous mode, do not pause after every page; stop when one agent-learning slice is truly teachable.

## When To Use This Skill

Use this skill when the user asks for things like:

- “继续完善 AI Agent 这条线”
- “把 OpenClaw / Codex / Cursor 这些系统梳理清楚”
- “把 agent 的工作原理、工程抽象和落地场景打通”
- “把 AI Agent 研究过程沉淀成可复用的学习系统”
- “给 AI Agent 建立知识图谱、地图、比较页、进度页”

## References

- AI agent topology: [references/layered-ai-agent-topology.md](references/layered-ai-agent-topology.md)
- Comparison dimensions: [references/comparison-dimensions.md](references/comparison-dimensions.md)
- Applications spine: [references/applications-spine.md](references/applications-spine.md)
- Update loop: [references/update-loop.md](references/update-loop.md)
- Autonomous batch loop: [references/autonomous-delivery-loop.md](references/autonomous-delivery-loop.md)
