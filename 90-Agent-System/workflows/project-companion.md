---
title: "Project Companion Workflow"
created: 2026-06-14
updated: 2026-06-16
status: active
tags:
  - agent-system
  - workflow
  - projects
  - project-companion
---

# Project Companion Workflow

这个 workflow 定义 `tony-project-companion` 能力：帮助 Tony 的个人项目不断线，但不把个人知识系统变成公司 PM 系统。

## Goal

```text
发现项目状态
-> 判断是否仍然活跃
-> 更新当前目标、进度和下一步
-> 把卡点放入 review surface
-> 把阶段成果沉淀到知识库或 GitHub
```

## Scope

Project Companion 适合处理：

- `40-Projects/` 下的 active project；
- AI cognitive system、vault migration、tooling、skills、rules、local experiments；
- 从 learning package 或 review queue 转成 build action 的事项；
- 长期未推进但仍有价值的个人项目。

不适合处理：

- 公司级排期、绩效、团队职责矩阵；
- 没有明确下一步的泛泛愿望；
- 未经 Tony 确认的大规模项目结构重组。

## Directory Contract

| Stage | Owner | Path |
|---|---|---|
| Project inbox | Codex / Hermes / ChatGPT | `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/` |
| Active project state | Codex | `40-Projects/<project>/README.md` and optional project files |
| Review decision | Tony / Codex | `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/` |
| Durable system change | Codex | `90-Agent-System/`, `30-Playbooks/`, `10-Knowledge/`, `20-Maps/` |
| Git checkpoint | Codex | Git commit after coherent batches |

## Project State Shape

每个 active project 至少应能回答：

```text
Goal:
Current scope:
Current status:
Next actions:
Open questions:
Related workflows:
```

如果项目很小，可以只维护 `README.md`。只有项目复杂到需要单独追踪时，再添加：

```text
目标.md
进度.md
决策.md
下一步.md
```

## Operating Loop

1. Read [[40-Projects/README]] and the target project README.
2. Read nearby system state when the project touches agent workflows: [[90-Agent-System/当前状态]].
3. Identify one of four project statuses: `active`, `paused`, `candidate`, `archived`.
4. Update the project page with current status and next actions.
5. If a decision is needed, create a review item in the working vault `20-Review-Queue/pending/`.
6. If the work creates reusable method, link or promote it into `30-Playbooks/` or `90-Agent-System/workflows/`.
7. Update maps or current-state pages only when the project surface materially changes.

## Noise Controls

- 每次最多推进一个项目，除非 Tony 明确要求 batch review。
- 不为每个想法创建项目；先放 working vault review queue。
- 项目下一步必须是可执行动作，不写空泛口号。
- 对长期未推进项目，优先提出 `pause / keep / archive / split` 决策，而不是继续追加任务。

## First Target

当前第一目标是 [[40-Projects/AI-First-Cognitive-System/README]]。

这个项目负责把 Codex、ChatGPT Desktop、Hermes、Obsidian 和 GitHub 组织成 Tony 的个人 AI First cognitive system。
