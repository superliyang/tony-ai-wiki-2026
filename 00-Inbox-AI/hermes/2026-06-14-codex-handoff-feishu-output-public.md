---
title: "Codex Handoff - Feishu Output Layer"
created: 2026-06-14
status: handoff
source: codex
target: hermes
tags:
  - hermes
  - codex
  - handoff
  - feishu
  - output-feishu
---

# Codex Handoff - Feishu Output Layer

Hermes, Codex updated the Feishu publishing design.

## New Canonical Pipeline

```text
Obsidian Vault
  ↓
导出 / 清洗 / 过滤
  ↓
output-feishu/
  ↓
飞书 CLI 上传
  ↓
飞书知识库 / 云文档 / 云空间
```

## Meaning

- Obsidian is Tony's personal knowledge production center.
- GitHub private repo is the long-term versioned fact source.
- `output-feishu/` is the cleaned publish-ready intermediate layer.
- Feishu knowledge base / docs are for anywhere access, mobile reading, and sharing/collaboration.
- Feishu CLI is the automated sync executor.
- `00-Inbox-AI/feishu-publishing/` stores publishing operation records, pending operations, and failures.

## Hermes Boundary

Hermes may:

- read `output-feishu/` when preparing Feishu publishing summaries;
- notify Tony about newly published Feishu docs;
- propose Feishu publishing candidates in `00-Inbox-AI/feishu-publishing/pending/`;
- use `lark-cli` only when following [[90-Agent-System/workflows/feishu-publishing]].

Hermes should not:

- publish directly from canonical notes when a cleaned `output-feishu/` version is needed;
- treat Feishu as canonical memory or knowledge;
- publish raw `00-Inbox-AI/` material unless Tony explicitly approves that exact item;
- write or expose secrets, local auth state, OAuth state, tokens, cookies, or account files.

## First Published Doc

- Output file: [[output-feishu/ai-first-cognitive-system/2026-06-14-ai-first-cognitive-system-online-review]]
- Record: [[00-Inbox-AI/feishu-publishing/published/2026-06-14-ai-first-cognitive-system-online-review-record]]
- Feishu URL: [AI First Cognitive System 在线回顾版](https://my.feishu.cn/docx/MnQSdu6fro5BKQxyXNNcQfranhc)

## Required Startup Reads For Feishu Publishing

Before Hermes publishes or proposes Feishu publishing work, read:

1. [[90-Agent-System/workflows/feishu-publishing]]
2. [[90-Agent-System/integrations/Feishu]]
3. [[output-feishu/README]]
4. [[00-Inbox-AI/feishu-publishing/README]]
