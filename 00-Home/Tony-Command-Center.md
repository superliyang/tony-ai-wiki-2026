---
title: "Tony Command Center"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - home
  - command-center
  - ai-first
  - workflow
---

# Tony Command Center

这页回答一个问题：

```text
我现在想让 AI 帮我做什么？
```

它不是按 Agent 名字进入，而是按任务意图进入。

## 选择任务

| 我现在想... | Intent | Hermes 该做什么 | Codex 该做什么 | 典型输出 |
|---|---|---|---|---|
| 研究一个主题 | `research` | 拆问题、找资料、写 request | 放大、对比、沉淀 | research note / MOC / Feishu |
| 推进一个项目 | `project` | 识别项目状态和卡点 | 更新项目页和下一步 | project next actions |
| 整理一堆材料 | `organize` | 标记来源和混乱点 | 清洗、归类、建索引 | map / index / cleanup batch |
| 写一篇东西 | `writing` | 收集观点和素材 | 改成可发布版本 | article / sharing / Feishu |
| 学会一个东西 | `learning` | 拆学习目标 | 学习路径、练习、复盘题 | learning path |
| 做一次复盘 | `reflection` | 收集本周/项目事实 | 提炼判断和决策变化 | review note / decision |
| 发布到飞书 | `publish` | 确认可发布对象 | 写 `output-feishu/` 并发布 | Feishu doc |

## 默认流程

```text
Tony message
  -> Hermes classifies intent
  -> Hermes writes task intent
  -> Hermes writes Codex request when useful
  -> Codex processes request
  -> Codex writes knowledge / project / output-feishu
  -> Tony gives feedback
  -> feedback improves next routing
```

## 快速说法

| 你可以这样说 | 系统理解 |
|---|---|
| “帮我研究一下 X” | `research` |
| “这个项目下一步怎么推” | `project` |
| “这堆东西帮我整理一下” | `organize` |
| “把这个改成能发出去的文章” | `writing` |
| “我想学 X，给我路径” | `learning` |
| “帮我复盘一下最近这件事” | `reflection` |
| “这个同步到飞书” | `publish` |

## 反馈口令

每次产出后，Tony 可以只给一句反馈：

```text
有用 / 太长 / 太浅 / 跑偏 / 继续放大 / 入库 / 发飞书 / 暂停
```

反馈记录在：

- [[00-Inbox-AI/feedback-log/README]]

任务意图记录在：

- [[00-Inbox-AI/task-intents/README]]

