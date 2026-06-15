---
title: "Codex Handoff: Hermes Task Intent Router"
created: 2026-06-14
updated: 2026-06-14
status: active
source: codex
target: hermes
tags:
  - hermes
  - codex
  - task-intent
  - handoff
---

# Codex Handoff: Hermes Task Intent Router

Hermes 之后不要把 Tony 的每个请求都默认当成 research。

## New First Step

Tony 发消息后，Hermes 先读：

- [[00-Home/Tony-Command-Center]]
- [[90-Agent-System/prompts/hermes-task-intent-router]]
- [[90-Agent-System/workflows/task-intent-routing]]
- [[00-Inbox-AI/task-intents/README]]

然后判断 Tony 这次是哪类任务：

```text
research / project / organize / writing / learning / reflection / publish
```

## Write Path

Hermes 先写任务意图：

```text
00-Inbox-AI/task-intents/pending/YYYY-MM-DD-intent-topic.md
```

如果任务已经足够明确，再写一个 Codex request：

```text
00-Inbox-AI/codex-requests/pending/YYYY-MM-DD-intent-topic.md
```

## Boundary

- 一条 Tony 消息默认最多生成一个 Codex request。
- 信息不足时，只问 Tony 一个澄清问题。
- 不直接写 canonical knowledge。
- 不直接从 raw inbox 发布飞书。
- 飞书发布必须走 `output-feishu/`。

## Why

当前系统已经能完成：

```text
Hermes research -> Codex crystallize -> Obsidian -> Feishu
```

但下一步要支持更多使用方式：

```text
研究 / 项目推进 / 整理 / 写作 / 学习 / 复盘 / 发布
```

