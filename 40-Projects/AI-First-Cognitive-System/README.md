---
title: "AI First Cognitive System"
created: 2026-06-03
updated: 2026-06-14
status: active
tags:
  - project
  - ai-first
  - cognitive-system
---

# AI First Cognitive System

## Goal

Build Tony's personal AI First cognitive system around Codex, ChatGPT Desktop, Hermes, Obsidian, and GitHub.

## Current Scope

- Minimal vault structure.
- Shared memory synchronization between Codex and Hermes.
- Human-readable home and maps.
- AI-readable agent roles and workflows.
- Gradual promotion from the legacy vault.
- Personal Agent capability mapping: workflow first, persona second.
- Project Companion workflow as the missing project-continuity layer.

## Current Principle

```text
Keep the system small enough to use, structured enough to compound.
```

## Current Status

`active`

The system has crossed the first setup threshold: vault structure, imported legacy knowledge, Hermes/Codex handoff, shared memory protocol, review queue, and Personal Agent capability mapping all exist.

The current bottleneck is not more structure. It is flow:

```text
Hermes discovers
-> Codex packages
-> Tony reviews
-> Codex promotes
```

Right now the queue is heavy at the review gate:

- `00-Inbox-AI/learning-tasks/pending/`: 42 files, including `.gitkeep`
- `00-Inbox-AI/learning-tasks/in-progress/`: 1 file, `.gitkeep` only
- `00-Inbox-AI/learning-tasks/accepted/`: 6 files, including `.gitkeep`
- `00-Inbox-AI/review-queue/pending/`: 13 files after substantive review triage
- `00-Inbox-AI/review-queue/accepted/`: 7 files
- accepted review flow: now open; promotion/build work remains

## Current Bottlenecks

- Substantive review backlog has been triaged; build/promotion execution is now the bottleneck.
- Memory review daily items are too noisy in `review-queue/pending/`.
- Hermes has strong scout output, but `signals/` and `candidates/` are still not consistently used as normalized queues.
- Project Companion is still manual; the Hermes project scout job is intentionally paused.

## Next Actions

See [[40-Projects/AI-First-Cognitive-System/下一步]].

Top three:

1. Run a 20-minute review triage on the 5 substantive learning package reviews.
2. Decide whether memory-review daily items should stop entering `review-queue/pending/`.
3. Keep `hermes-project-companion-scout` paused, but allow narrow Hermes/Codex on-demand Project Companion runs when Tony asks.

## Related

- [[60-Agents/Personal-Agent-Capabilities]]
- [[90-Agent-System/workflows/project-companion]]
- [[90-Agent-System/workflows/feishu-publishing]]
- [[00-Inbox-AI/project-companion/2026-06-14-ai-first-cognitive-system-pilot]]
- [[00-Inbox-AI/project-companion/2026-06-14-ai-first-cognitive-system-pilot-result]]

## Online Review

- [Feishu: AI First Cognitive System 在线回顾版](https://my.feishu.cn/docx/MnQSdu6fro5BKQxyXNNcQfranhc)
