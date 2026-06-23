---
title: "Codex Request Quality Gate"
created: 2026-06-14
updated: 2026-06-16
status: active
tags:
  - workflow
  - codex
  - quality-gate
  - automation
---

# Codex Request Quality Gate

这个 workflow 用来检查 Hermes 写给 Codex 的 request 是否足够可执行。

## Goal

```text
Hermes request
  -> quality check
  -> pass / needs-info / duplicate / blocked
  -> Codex Request Consumer
```

Quality Gate 不处理 request 本身，只判断 request 是否适合进入 Codex Consumer。

## Reads

- `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/`
- `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/accepted/`
- `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/10-Generated/learning-tasks/`
- historical `00-Inbox-AI/` only when doing cleanup

## Writes

- `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/40-Logs/quality-reports/`

## Checks

每个 pending request 至少检查：

- 是否有 `request_type`;
- 是否有 `priority`;
- 是否有 `domain`;
- 是否有 `source_refs`;
- 是否有 `desired_outputs`;
- 是否有 `publish_to_feishu`;
- 是否有 `safety_note`;
- 是否可能和已有 pending / done / accepted 项重复；
- 是否需要 Tony review；
- 是否包含不能发布到飞书的 raw inbox / secret / OAuth / token / credential 风险。

## Output Shape

```text
date:
pending_count:
pass:
needs_info:
duplicate:
blocked:
recommended_next_request:
```

## Guardrails

- 不直接处理 request；
- 不直接写 canonical knowledge；
- 不直接发飞书；
- 不删除 request；
- 遇到不合格 request，写报告即可，必要时建议 Hermes 补充信息。
