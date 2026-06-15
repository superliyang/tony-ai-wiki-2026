---
title: "Hermes Codex Integration"
created: 2026-06-04
updated: 2026-06-14
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

Short version:

```text
Hermes = 发现 / 记录 / 提醒 / 建任务
Codex = 研究 / 拆解 / 入库 / 更新地图 / Git checkpoint
Tony = 判断 / 审核 / 批准 promote
```

Before creating research work, Hermes should classify Tony's task intent:

- [[00-Home/Tony-Command-Center]]
- [[00-Inbox-AI/task-intents/README]]
- [[90-Agent-System/workflows/task-intent-routing]]
- [[90-Agent-System/prompts/hermes-task-intent-router]]

For end-to-end request handling and Feishu output, use:

- [[90-Agent-System/workflows/hermes-codex-feishu-pipeline]]
- [[00-Inbox-AI/codex-requests/README]]

## Hermes Writes

- `00-Inbox-AI/signals/`
- `00-Inbox-AI/candidates/`
- `00-Inbox-AI/task-intents/pending/`
- `00-Inbox-AI/learning-tasks/pending/`
- `00-Inbox-AI/learning-tasks/follow-up/`
- `00-Inbox-AI/project-companion/`
- `00-Inbox-AI/codex-requests/pending/`
- `00-Inbox-AI/feishu-publishing/`
- `00-Inbox-AI/review-queue/pending/`
- `00-Inbox-AI/reports/`
- `00-Inbox-AI/hermes/`
- `00-Inbox-AI/agent-memory/candidates/`
- `00-Inbox-AI/agent-memory/projections/`

## Codex Writes

- `00-Inbox-AI/learning-tasks/in-progress/`
- `00-Inbox-AI/learning-tasks/accepted/`
- `00-Inbox-AI/codex-requests/in-progress/`
- `00-Inbox-AI/codex-requests/done/`
- `00-Inbox-AI/codex-requests/failed/`
- `00-Inbox-AI/review-queue/`
- canonical knowledge areas after Tony review;
- maps, playbooks, project pages, workflows, and Git checkpoints.

## Handoff File

For learning tasks, the handoff file is Markdown with frontmatter, stored in:

```text
00-Inbox-AI/learning-tasks/pending/YYYY-MM-DD-topic-slug.md
```

For broader Codex work, Hermes should use:

```text
00-Inbox-AI/codex-requests/pending/YYYY-MM-DD-topic-slug.md
```

For natural-language Tony requests, Hermes should first write:

```text
00-Inbox-AI/task-intents/pending/YYYY-MM-DD-intent-topic.md
```

Then Hermes creates a Codex request only if the intent is executable and bounded.

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

For Codex requests, Codex should process one file from `00-Inbox-AI/codex-requests/pending/`, move it to `in-progress/`, and finish in `done/` or `failed/` with output links.

## Direct Hermes -> Codex Trigger

Hermes can drive Codex through request files today.

Hermes should not directly launch arbitrary `codex` CLI prompts until a narrow wrapper exists. A safe wrapper must:

- accept exactly one request file;
- constrain writable paths to this vault;
- require review before canonical promotion unless already accepted;
- write a run report;
- route Feishu publishing through `output-feishu/`.

## Hermes Follow-Up Behavior

After a package is accepted, Hermes reads follow-up proposals and writes reminder items into:

```text
00-Inbox-AI/learning-tasks/follow-up/
```

Hermes may notify Tony, but should not rewrite canonical knowledge.

## Hermes Project Companion Behavior

Hermes may detect project-continuity signals and write candidates into:

```text
00-Inbox-AI/project-companion/
```

Hermes should not update `40-Projects/` directly. Codex promotes project candidates into project pages after Tony review or explicit delegation.

## Hermes Feishu Publishing Behavior

Hermes may help with Feishu publishing only through the approved projection chain:

```text
vault -> output-feishu/ -> lark-cli -> Feishu
```

Hermes should not publish directly from canonical notes when a cleaned `output-feishu/` version is needed. Feishu is an online reading projection, not canonical knowledge or memory.

Publishing records live in:

```text
00-Inbox-AI/feishu-publishing/
```

Publish-ready bodies live in:

```text
output-feishu/
```

## If Hermes Wants To Do More

If Hermes has enough material to write a full draft, it should still stay in:

```text
00-Inbox-AI/hermes/
```

Then Hermes creates a matching task in:

```text
00-Inbox-AI/learning-tasks/pending/
```

Codex is responsible for deciding whether the draft becomes:

- a topic note;
- a map;
- a playbook;
- a case;
- a runbook;
- a review item;
- or discarded/deferred material.

## Scheduled Task Design

Hermes tasks are split by purpose:

- core radar;
- topic scout;
- growth track;
- learning task generation;
- follow-up review;
- memory review;
- weekly synthesis.
- project companion scout.
- Feishu publishing.
- task intent routing.

The task matrix lives at:

- [[00-Inbox-AI/hermes/automations/hermes-cron-matrix]]
