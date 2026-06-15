---
title: "Output Public"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - output
  - public-projection
  - feishu
---

# Output Public

`output-public/` stores general cleaned, filtered, publish-ready projections generated from the Obsidian vault.

For Feishu specifically, use [[output-feishu/README]].

## Role

```text
Obsidian Vault
  ↓
export / clean / filter
  ↓
output-public/ or output-feishu/
  ↓
Feishu CLI upload
  ↓
Feishu docs / wiki / drive
```

This directory is not the source of truth. It is the public or semi-public output buffer.

## Rules

- Only place publish-ready content here.
- Remove secrets, local auth state, personal account files, and runtime logs.
- Avoid unreviewed AI inbox material unless Tony explicitly asks to publish that exact item.
- Keep source references back to vault notes.
- Use Feishu as online projection, not canonical storage.
- Use `output-feishu/` as the concrete Feishu publishing buffer.

## Current Outputs

- [[output-feishu/ai-first-cognitive-system/2026-06-14-ai-first-cognitive-system-online-review]]
