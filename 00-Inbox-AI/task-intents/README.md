---
title: "Task Intents"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - inbox
  - task-intent
  - hermes
  - codex
---

# Task Intents

`task-intents/` 是 Tony 自然语言请求进入 AI 工作流前的意图层。

## Why

不要让所有事情都变成“调研”。Hermes 先判断 Tony 这次要的是：

```text
research / project / organize / writing / learning / reflection / publish
```

然后再决定是否创建 Codex request。

## Folders

| Folder | Meaning |
|---|---|
| `pending/` | Hermes 写入、等待 Codex 或 Tony 处理的任务意图 |
| `resolved/` | 已经被 Codex request、review item、项目页或反馈闭环吸收的任务意图 |
| `templates/` | 任务意图模板 |

## Intent Types

| Intent | Meaning | Downstream |
|---|---|---|
| `research` | 理解新领域、新工具、新趋势 | `codex-requests` / research note |
| `project` | 推进个人项目或系统建设 | project companion / `40-Projects/` |
| `organize` | 整理材料、地图、入口、旧库 | gardener / maps |
| `writing` | 输出文章、分享、方案、邮件 | `50-Outputs/` or `output-feishu/` |
| `learning` | 学习路径、练习、复盘问题 | learning task / MOC |
| `reflection` | 周复盘、项目复盘、判断变化 | `60-Review/` or review queue |
| `publish` | 飞书在线阅读版本 | `output-feishu/` |

## Rule

```text
Task intent records the user's intent.
Codex request records the executable work.
Feedback log records whether the result helped.
```

## Template

- [[00-Inbox-AI/task-intents/templates/task-intent-template]]

