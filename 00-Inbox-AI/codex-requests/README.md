---
title: "Codex Requests"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - inbox
  - codex
  - hermes
  - handoff
---

# Codex Requests

这里是 Hermes 驱动 Codex 的请求队列。

## Why

Hermes 不应该直接写 canonical knowledge，但 Hermes 可以发现问题、整理材料、判断任务价值，并创建一个 Codex request。

```text
Hermes produces request
  -> Codex processes request
  -> Codex writes package / review item / canonical note
  -> Codex prepares output-feishu when needed
  -> Feishu CLI publishes online version
```

## Folders

| Folder | Meaning |
|---|---|
| `pending/` | Hermes 创建、等待 Codex 处理的请求 |
| `in-progress/` | Codex 正在处理的请求 |
| `done/` | 已完成请求，记录输出位置 |
| `failed/` | 处理失败或信息不足的请求 |
| `quality-reports/` | Codex Request Quality Gate 输出 |
| `templates/` | 请求模板 |

## Request Types

| Type | Meaning | Typical Output |
|---|---|---|
| `learning-package` | 把一个主题做成学习包 | `00-Inbox-AI/learning-tasks/in-progress/` + review item |
| `knowledge-promotion` | 把已接受内容提升到正式知识库 | `10-Knowledge/`, `20-Maps/`, `30-Playbooks/` |
| `project-companion` | 推进一个项目状态和下一步 | `40-Projects/` + project inbox record |
| `feishu-publish` | 把已清洗内容发布到飞书 | `output-feishu/` + Feishu doc |
| `map-maintenance` | 修地图、入口、导航体验 | `00-Home/`, `20-Maps/`, nearest README |
| `writing-output` | 把观点、草稿、材料变成可发布文字 | `50-Outputs/`, `output-feishu/`, or review item |
| `reflection-note` | 复盘项目、学习、决策、判断变化 | `60-Review/` or review queue |

## Guardrails

- Hermes should classify task intent before creating a broad Codex request.
- Hermes may create requests, but must not mark them `done`.
- Hermes must include enough source context for Codex to work without guessing.
- Codex may process one request at a time unless Tony asks for a batch.
- Codex must not promote to canonical knowledge unless the request is explicitly approved or the material is already accepted.
- Feishu publishing must go through `output-feishu/` first.
- Requests that touch private, security, legal, financial, or credentials material must include a safety note.

## Consumer Rule

Codex should read:

1. [[AGENTS]]
2. [[90-Agent-System/仓库地图]]
3. [[90-Agent-System/当前状态]]
4. This README
5. The target request file

Then Codex should update the request status by moving it to `in-progress/`, and finally to `done/` or `failed/`.
