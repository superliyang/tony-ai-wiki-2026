---
title: "Hermes Codex Request Generator"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - prompt
  - hermes
  - codex
  - handoff
---

# Hermes Codex Request Generator

Use this prompt when Hermes has found a high-value signal or synthesis that should be handled by Codex.

## Goal

Create one precise Codex request, not a vague report.

## Required Reads

- [[AGENTS]]
- [[90-Agent-System/仓库地图]]
- [[90-Agent-System/当前状态]]
- [[90-Agent-System/integrations/Hermes-Codex]]
- [[90-Agent-System/workflows/hermes-codex-feishu-pipeline]]
- [[00-Inbox-AI/codex-requests/README]]

## Output Path

Write exactly one file under:

```text
00-Inbox-AI/codex-requests/pending/
```

Use:

```text
YYYY-MM-DD-short-topic.md
```

## Request Quality Bar

The request must include:

- what Codex should do;
- why it matters now;
- source refs;
- target domain;
- desired output shape;
- whether Tony approval is needed;
- whether Feishu publish is requested;
- safety note.

## Do Not

- Do not ask Codex to browse or research without a clear question.
- Do not ask Codex to promote canonical knowledge from raw material unless Tony already accepted it.
- Do not request Feishu publication for raw private inbox material.
- Do not create more than one request unless explicitly asked.

