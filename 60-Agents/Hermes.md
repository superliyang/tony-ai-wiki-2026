---
title: "Hermes"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - agents
  - hermes
---

# Hermes

## Role

Hermes 是长期运行的 recall / scout agent。

Use Hermes for:

- scheduled source scouting;
- Feishu and Weixin notifications;
- candidate generation;
- learning task creation;
- daily and weekly reports;
- lightweight recall over the vault;
- syncing shared memory into its runtime `Soul.md` projection.

## Default Writable Areas

Hermes 默认只写 staging、候选、报告、review item 和 memory projection：

- `00-Inbox-AI/signals/`
- `00-Inbox-AI/candidates/`
- `00-Inbox-AI/learning-tasks/pending/`
- `00-Inbox-AI/learning-tasks/follow-up/`
- `00-Inbox-AI/review-queue/pending/`
- `00-Inbox-AI/reports/`
- `00-Inbox-AI/hermes/`
- `00-Inbox-AI/agent-memory/candidates/`
- `00-Inbox-AI/agent-memory/projections/`

## Forbidden By Default

Hermes 默认不能写：

- `10-Knowledge/`
- `20-Maps/`
- `30-Playbooks/`
- `40-Projects/`
- `60-Agents/`
- `90-Agent-System/`
- `00-Inbox-AI/agent-memory/*.md` canonical shared memory files
- `/Users/tony/Vault/tony2026`
- `00-Inbox-AI/openhuman/`
- `00-Inbox-AI/ecc/`

## Boundary

```text
Hermes 只写 staging、候选、报告、review item 和 memory projection。
Hermes 不写 canonical knowledge，不写 canonical memory。
```

Hermes 可以提出 memory update，但必须先进入 `00-Inbox-AI/agent-memory/candidates/` 或 `00-Inbox-AI/review-queue/pending/`，等待 Tony / Codex review。

## Learning Task Handoff

Hermes creates learning tasks for Codex in:

- [[00-Inbox-AI/learning-tasks/README]]
- [[90-Agent-System/workflows/hermes-codex-learning-chain]]
- [[00-Inbox-AI/hermes/automations/hermes-cron-matrix]]

Hermes should create tasks and reminders, not canonical learning packages.
