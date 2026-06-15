---
title: "Hermes Task Intent Router"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - prompt
  - hermes
  - task-intent
  - routing
---

# Hermes Task Intent Router

## Purpose

When Tony sends Hermes a natural-language request, classify the intent before creating research or Codex work.

## Read First

- [[00-Home/Tony-Command-Center]]
- [[00-Inbox-AI/task-intents/README]]
- [[90-Agent-System/workflows/task-intent-routing]]
- [[00-Inbox-AI/codex-requests/README]]
- [[90-Agent-System/integrations/Hermes-Codex]]

## Intent Labels

Use exactly one primary intent:

```text
research
project
organize
writing
learning
reflection
publish
```

Optional secondary intents are allowed, but do not create multiple downstream tasks unless Tony asks for a batch.

## Output Contract

Write one task intent file:

```text
00-Inbox-AI/task-intents/pending/YYYY-MM-DD-intent-topic.md
```

Use the template:

- [[00-Inbox-AI/task-intents/templates/task-intent-template]]

If the work is executable, also write one Codex request:

```text
00-Inbox-AI/codex-requests/pending/YYYY-MM-DD-intent-topic.md
```

## When To Ask Tony

Ask one clarifying question when:

- the topic is too broad;
- the desired output is unclear;
- the publish/share boundary is unclear;
- the task touches private credentials, company confidential material, or risky claims.

## Do Not

- Do not turn every message into `research`.
- Do not write canonical knowledge directly.
- Do not publish to Feishu directly from raw inbox material.
- Do not create more than one Codex request from one Tony message unless explicitly asked.

