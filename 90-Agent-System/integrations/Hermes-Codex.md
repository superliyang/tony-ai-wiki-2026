---
title: "Hermes Codex Integration"
created: 2026-06-04
updated: 2026-06-04
status: active
tags:
  - integrations
  - hermes
  - codex
  - learning-automation
---

# Hermes Codex Integration

This page defines the integration boundary between Hermes and Codex.

## Contract

Hermes is the scheduled discovery, reminder, and recall agent. Codex is the deep research, restructuring, and crystallization agent.

Hermes should create tasks. Codex should create packages. Tony should approve canonical promotion.

## Hermes Writes

- `00-Inbox-AI/signals/`
- `00-Inbox-AI/candidates/`
- `00-Inbox-AI/learning-tasks/pending/`
- `00-Inbox-AI/learning-tasks/follow-up/`
- `00-Inbox-AI/review-queue/pending/`
- `00-Inbox-AI/reports/`
- `00-Inbox-AI/hermes/`
- `00-Inbox-AI/agent-memory/candidates/`
- `00-Inbox-AI/agent-memory/projections/`

## Codex Writes

- `00-Inbox-AI/learning-tasks/in-progress/`
- `00-Inbox-AI/learning-tasks/accepted/`
- `00-Inbox-AI/review-queue/`
- canonical knowledge areas after Tony review;
- maps, playbooks, project pages, workflows, and Git checkpoints.

## Handoff File

The handoff file is Markdown with frontmatter, stored in:

```text
00-Inbox-AI/learning-tasks/pending/YYYY-MM-DD-topic-slug.md
```

## Required Frontmatter

```yaml
status: pending
owner: hermes
priority: P1
domain: AI-Engineering
review_after: 2026-06-10
```

## Codex Consumer Behavior

When Codex processes the queue:

1. Read `90-Agent-System/仓库地图.md`.
2. Read `90-Agent-System/当前状态.md`.
3. Pick at most one task unless Tony asks for a batch.
4. Create a learning package.
5. Create or update a review item.
6. Do not promote canonical knowledge until Tony accepts.
7. Push coherent changes to GitHub.

## Hermes Follow-Up Behavior

After a package is accepted, Hermes reads follow-up proposals and writes reminder items into:

```text
00-Inbox-AI/learning-tasks/follow-up/
```

Hermes may notify Tony, but should not rewrite canonical knowledge.

## Scheduled Task Design

Hermes tasks are split by purpose:

- core radar;
- topic scout;
- growth track;
- learning task generation;
- follow-up review;
- memory review;
- weekly synthesis.

The task matrix lives at:

- [[00-Inbox-AI/hermes/automations/hermes-cron-matrix]]
