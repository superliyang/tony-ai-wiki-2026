---
title: "Hermes Codex Learning Chain"
created: 2026-06-04
updated: 2026-06-04
status: active
tags:
  - agent-system
  - workflow
  - hermes
  - codex
  - learning-automation
---

# Hermes Codex Learning Chain

This workflow connects Hermes discovery and reminders with Codex research, Tony review, Obsidian/GitHub crystallization, and Hermes follow-up review.

## Goal

```text
Hermes discovers or reminds
-> Hermes creates a learning task
-> Codex turns it into a learning package
-> Tony reviews
-> Codex promotes accepted knowledge
-> GitHub preserves the checkpoint
-> Hermes schedules follow-up review
```

## Directory Contract

| Stage | Owner | Path |
|---|---|---|
| Discovery signal | Hermes | `00-Inbox-AI/signals/` |
| Learning task | Hermes | `00-Inbox-AI/learning-tasks/pending/` |
| Codex work package | Codex | `00-Inbox-AI/learning-tasks/in-progress/` |
| Tony review | Tony / Codex | `00-Inbox-AI/review-queue/pending/` |
| Accepted package | Codex | `00-Inbox-AI/learning-tasks/accepted/` |
| Canonical knowledge | Codex | `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `90-Agent-System/` |
| Follow-up reminder | Hermes | `00-Inbox-AI/learning-tasks/follow-up/` |
| Run artifacts | Hermes / Codex | `00-Inbox-AI/reports/` or `00-Inbox-AI/hermes/` |

## Task Lifecycle

1. Hermes writes a task Markdown file into `00-Inbox-AI/learning-tasks/pending/`.
2. Hermes may notify Tony with the task title, priority, and review link.
3. Codex scans pending tasks on request or scheduled run.
4. Codex moves one accepted task into `in-progress/` and creates a learning package.
5. Codex writes a review item into `00-Inbox-AI/review-queue/pending/`.
6. Tony marks the review decision: `study`, `watch`, `promote`, `build`, `defer`, or `discard`.
7. Codex promotes approved material into canonical vault areas and updates maps.
8. Codex commits and pushes meaningful changes to GitHub.
9. Hermes reads accepted/follow-up metadata and schedules review reminders.

## Hermes Task Requirements

Hermes-created learning tasks must include:

- source URL or source note;
- reason this matters now;
- suggested domain;
- priority;
- proposed review date;
- desired output shape;
- safety note if the task touches private, legal, financial, or security-sensitive material.

Use [[00-Inbox-AI/learning-tasks/templates/hermes-learning-task-template]].

## Codex Package Requirements

Codex learning packages should include:

- one-page executive summary;
- learning objectives;
- key concepts and terminology;
- source-backed research notes;
- comparison or decision map when useful;
- exercises or review questions;
- suggested canonical destination;
- follow-up reminder proposal for Hermes.

Use [[00-Inbox-AI/learning-tasks/templates/codex-learning-package-template]].

## Automation Levels

### Level 1: File Queue

Hermes writes task files. Codex processes them when Tony asks.

This is the safest first version.

### Level 2: Scheduled Codex Consumer

A Codex automation periodically checks `00-Inbox-AI/learning-tasks/pending/`, processes at most one high-priority task, writes a review package, and pushes to GitHub.

Use only after Level 1 produces stable task quality.

### Level 3: Full Feedback Loop

Hermes watches accepted packages and follow-up metadata, then creates spaced-review reminders.

This should stay review-driven: Hermes may remind, but should not promote canonical knowledge.

## Guardrails

- Hermes must not write directly into canonical knowledge directories.
- Codex must not promote without Tony review unless Tony explicitly delegates that class of task.
- Every promoted package must link back to the original Hermes task and sources.
- Every meaningful promotion should update the nearest map or overview.
- GitHub push should run after coherent batches, not after every tiny file.

## Minimum Viable Implementation

1. Create a Hermes task in `00-Inbox-AI/learning-tasks/pending/`.
2. Codex creates the learning package and review item.
3. Tony accepts or edits the review item.
4. Codex promotes and pushes.
5. Hermes creates one follow-up item in `00-Inbox-AI/learning-tasks/follow-up/`.

## Split Cron Strategy

Do not run this as one giant Hermes job. Use the split schedule in:

- [[00-Inbox-AI/hermes/automations/hermes-cron-matrix]]

The split exists so each job has a clear frequency, output cap, and review surface.
