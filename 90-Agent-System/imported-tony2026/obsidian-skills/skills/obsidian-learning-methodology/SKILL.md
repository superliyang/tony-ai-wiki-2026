---
name: obsidian-learning-methodology
description: Build or evolve a domain-specific Obsidian learning system using layered notes, maps, progress memory, resume memory, and a maintainable update loop. Use when Codex needs to turn a topic into a durable study vault instead of isolated notes, especially for workflows that combine domain research, knowledge graph topology, Obsidian structure, interruption recovery, and periodic Git-backed maintenance.
---

# Obsidian Learning Methodology

## Overview

Use this skill when the goal is to build a reusable learning system, not just to write a few notes.

This skill is the umbrella workflow for turning a domain into:

- a clean Obsidian topology
- a readable learning path
- a knowledge graph with meaningful links
- a progress and resume system
- a repeatable maintenance loop

Use this when the user says things like:

- “帮我把这个领域系统学起来”
- “搭一个可以长期维护的知识库”
- “把这套学习方法沉淀下来”
- “我想中断后还能快速恢复”
- “把研究过程做成可复用的 skill”

## Core Method

Work in this order:

1. define the domain boundary
2. choose note layers
3. create the minimum skeleton
4. connect entities, topics, systems, and maps
5. preserve progress and resume state
6. design the maintenance loop

Do not start by creating many notes. Start by deciding what kind of learning system the domain needs.

## Autonomous Delivery Mode

When the user clearly wants uninterrupted progress, default to autonomous batch delivery rather than step-by-step check-ins.

Use this mode when the user says things like:

- “继续补充”
- “你自己判断下一步”
- “先做完再告诉我”
- “中间不用打断”

In this mode:

- pick one bounded but high-leverage slice at a time
- finish the slice end-to-end before reporting back
- reflect after each slice and choose the next obvious gap
- stop only when a coherent version is ready, risk becomes non-obvious, or a destructive decision needs approval

Read [references/autonomous-delivery-loop.md](references/autonomous-delivery-loop.md) when operating in this mode.

## Canonical Layers

Use only the layers that improve clarity, but prefer this default vocabulary:

- `Foundations`: history, concepts, first principles
- `Entities`: companies, people, institutions, protocols
- `Topics`: abstract themes and problem spaces
- `Systems`: products, platforms, runtimes, concrete tools
- `Maps`: topology and relationship views
- `Templates`: repeatable note structures
- `Progress`: where the learner currently is
- `Resume`: where to restart after interruption

## Standard Workflow

### 1. Scope the domain

Decide:

- what is in scope
- what is out of scope
- whether the domain is mainly conceptual, market-facing, engineering-heavy, or application-heavy

### 2. Pick the topology

Prefer clean separation between:

- abstract topics
- concrete entities and systems
- maps and indexes
- study-state pages

Read [references/layered-vault-pattern.md](references/layered-vault-pattern.md) when you need a topology pattern.

### 3. Build the minimum skeleton

Create at least:

- one domain `专题总览.md`
- one main topic index
- one maps index when maps matter
- one `学习进度.md`
- one `恢复笔记.md`

### 4. Expand in graph-aware order

Prefer this sequence:

1. indexes and maps
2. foundational topics
3. concrete entities or systems
4. comparison notes
5. applied workflows, cases, and templates

### 5. Run the autonomous slice loop when appropriate

When the user wants sustained progress, use this loop:

1. inspect the current graph and state pages
2. choose the next highest-leverage slice
3. complete the slice end-to-end
4. reflect on what is still missing
5. continue if the next step is obvious

A good slice usually updates not just content pages, but also the nearest indexes, maps, and state pages.

### 6. Preserve learning state

Whenever the topology changes meaningfully, refresh:

- the recommended reading path
- `学习进度.md`
- `恢复笔记.md`

### 7. Maintain, don’t just accumulate

A healthy learning vault should support:

- adding new notes without confusion
- pausing and resuming later
- revisiting maps when the field changes
- periodic Git-backed checkpoints

Read [references/session-loop.md](references/session-loop.md) for the default study rhythm.

## When To Pair With Other Skills

Use this skill as the umbrella. Pair it with:

- [$obsidian-domain-research-graph](/Users/tony/.codex/skills/obsidian-domain-research-graph/SKILL.md) when the domain graph itself needs design or refactoring
- [$knowledge-vault-research-sync](/Users/tony/.codex/skills/knowledge-vault-research-sync/SKILL.md) when the work needs wikilink validation, progress-note refreshes, and safe Git checkpoints
- [$domain-learning-system](/Users/tony/Documents/vault/tony2026/obsidian-skills/skills/domain-learning-system/SKILL.md) when you want the vault-side learning templates and examples

## Working Rules

- Build the structure before chasing coverage.
- Keep abstract topics separate from concrete systems.
- Update indexes and maps when topology changes.
- Treat progress and resume notes as first-class memory.
- Prefer a domain that is easy to restart over one that is merely large.
- In autonomous mode, do not stop after every micro-step; stop at natural version boundaries.

## References

- Method overview: [references/method-overview.md](references/method-overview.md)
- Layer patterns: [references/layered-vault-pattern.md](references/layered-vault-pattern.md)
- Session rhythm: [references/session-loop.md](references/session-loop.md)
- Autonomous batch loop: [references/autonomous-delivery-loop.md](references/autonomous-delivery-loop.md)
