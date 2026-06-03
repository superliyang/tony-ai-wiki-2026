---
title: "Review Queue"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - inbox
  - review-queue
  - ai-first
---

# Review Queue

`review-queue/` 是 Tony 的判断界面。

AI 可以提出候选，但是否进入长期知识、项目、playbook 或记忆，由这里的 review 决定。

## Folders

| Folder | Meaning |
|---|---|
| `pending/` | 等待 Tony 或 Codex review |
| `accepted/` | 已接受，等待或已经提升 |
| `deferred/` | 暂缓，未来可能再看 |
| `discarded/` | 已丢弃，仅保留历史 |

## Decision Labels

- `study`: 值得学习，但不一定马上沉淀。
- `watch`: 保持观察。
- `promote`: 提升到正式知识或地图。
- `build`: 进入项目或实现。
- `discard`: 不再跟进。

## Promotion Target

Accepted items should move toward one of:

- `10-Knowledge/`
- `20-Maps/`
- `30-Playbooks/`
- `40-Projects/`
- `90-Agent-System/`
