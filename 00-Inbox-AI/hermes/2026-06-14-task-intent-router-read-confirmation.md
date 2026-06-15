---
title: "Hermes Read Confirmation: Task Intent Router"
created: 2026-06-14
updated: 2026-06-14
status: confirmed
source: hermes-oneshot
tags:
  - hermes
  - task-intent
  - confirmation
---

# Hermes Read Confirmation: Task Intent Router

Codex asked Hermes to read the new Task Intent Router protocol in read-only mode.

Hermes confirmed the following operating rules:

1. Tony 发自然语言请求后，Hermes 先分类，不默认当 `research`。
2. 低置信度时只问一个澄清问题。
3. 先写 `00-Inbox-AI/task-intents/pending/YYYY-MM-DD-intent-topic.md`。
4. 只在任务可执行时创建一个 `00-Inbox-AI/codex-requests/pending/` request。
5. 不直接写 canonical wiki，不从 raw inbox 直接发飞书，飞书发布必须走 `output-feishu/`。

## Source Files

- [[00-Inbox-AI/hermes/2026-06-14-codex-handoff-task-intent-router]]
- [[90-Agent-System/prompts/hermes-task-intent-router]]
- [[90-Agent-System/workflows/task-intent-routing]]
- [[00-Inbox-AI/task-intents/README]]

