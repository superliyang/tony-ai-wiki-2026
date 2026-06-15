---
title: "Task Intent Routing"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - workflow
  - hermes
  - codex
  - task-intent
---

# Task Intent Routing

这个 workflow 解决当前系统“只有调研链路”的问题。

## Goal

```text
Tony message
  -> classify intent
  -> choose downstream
  -> Codex request or feedback/review item
```

## Intent Types

| Intent | Use When | Downstream |
|---|---|---|
| `research` | Tony 想理解一个主题 | `codex-requests` as `learning-package` or `map-maintenance` |
| `project` | Tony 想推进一个项目 | `codex-requests` as `project-companion` |
| `organize` | Tony 想整理材料或入口 | `codex-requests` as `map-maintenance` or gardener report |
| `writing` | Tony 想输出文章、分享、方案 | `codex-requests` as `writing-output` |
| `learning` | Tony 想系统学会一个东西 | `learning-tasks` or `codex-requests` as `learning-package` |
| `reflection` | Tony 想复盘判断、项目、阶段 | review note / reflection request |
| `publish` | Tony 想在线阅读或分享 | `codex-requests` as `feishu-publish` |

## Hermes Behavior

Hermes should:

1. read Tony's message;
2. classify the task intent;
3. if confidence is low, ask one clarifying question;
4. write a task intent into `00-Inbox-AI/task-intents/pending/`;
5. create a Codex request only when the task is executable;
6. preserve source refs and safety notes.

Hermes should not turn every message into research.

## Codex Behavior

Codex should:

1. read the task intent when present;
2. check whether a Codex request already exists;
3. process one bounded request;
4. write output to the correct layer;
5. ask for feedback or create a review item when the result needs Tony's judgment.

## Feedback Loop

After output, Tony feedback goes to:

```text
00-Inbox-AI/feedback-log/
```

Feedback should influence future routing:

- `太长`: shorten future output;
- `太浅`: add examples, trade-offs, source refs;
- `跑偏`: improve intent classification;
- `继续放大`: create follow-up Codex request;
- `入库`: create promotion request;
- `发飞书`: create Feishu publish request.

