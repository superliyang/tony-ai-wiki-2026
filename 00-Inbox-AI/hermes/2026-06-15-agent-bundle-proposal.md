---
title: "Agent 编组提案：3 个常驻 + 2 个按需"
created: 2026-06-15
updated: 2026-06-15
status: proposal
author: codex
tags:
  - agents
  - hermes
  - codex
  - proposal
  - ai-first
---

# Agent 编组提案：3 个常驻 + 2 个按需

这不是再造一批人格化 Agent，而是把现有 Hermes / Codex / Tony 流程压缩成更稳的编组。

核心原则：

```text
一个 Agent 只回答一个核心问题。
一个 Agent 只拥有一个主输出面。
先保流速，再扩数量。
```

## 推荐编组

### 3 个常驻 Agent

| Agent | Primary Owner | 只回答什么问题 | 主输入 | 主输出 | 建议频率 |
|---|---|---|---|---|---|
| `tony-radar` | Hermes | 过去 24 小时里，什么外部变化值得 Tony 看？ | RSS / Exa / 最近 scout 历史 | `00-Inbox-AI/hermes/curated-scout/` + `00-Inbox-AI/signals/` | `09:00 / 15:00 / 21:00` |
| `tony-review-compressor` | Codex | Tony 今天只该看哪 3 个判断？ | `review-queue/`, `learning-tasks/`, `codex-requests/` | `00-Inbox-AI/review-queue/triage/` | `daily` |
| `tony-learning-planner` | Hermes | 哪些高信号该转成可执行 learning task？ | `signals/`, `candidates/`, `curated-scout/` | `00-Inbox-AI/learning-tasks/pending/` | `daily evening` |

### 2 个按需 Agent

| Agent | Primary Owner | 只回答什么问题 | 触发方式 | 主输出 |
|---|---|---|---|---|
| `tony-project-companion` | Hermes + Codex | 哪个项目最可能断线，下一步是什么？ | `manual-on-demand` | `00-Inbox-AI/project-companion/`，必要时再进 `40-Projects/` |
| `tony-publisher` | Codex | 哪个内容值得做成可读、可分享的 online projection？ | `manual-on-demand` | `output-feishu/` + `00-Inbox-AI/feishu-publishing/` |

## 为什么是这 5 个

- 它们已经对应你现有的真实瓶颈：`radar`、`review gate`、`learning task quality`、`project continuity`、`publishing`。
- 它们都能绑定到现成目录，不需要为每个 Agent 再起一套新结构。
- 它们的输出可以在 30 秒内被 Tony 判断“看 / 不看 / 下游处理”。

## 不建议现在常驻化的 Agent

### 1. `tony-memory-governor`

原因：

- memory review 现在噪音还偏高；
- 一旦做成高频常驻，容易继续污染 `review-queue/pending/`；
- 更适合先作为 `Hermes memory review + Tony rule gate`，不要当独立人格 Agent 扩张。

### 2. `tony-toolsmith`

原因：

- 改 rules / prompts / skills / integrations 是高杠杆动作；
- 适合明确需求时由 Codex 直接做，不适合日常常驻巡逻。

### 3. `tony-writing-partner`

原因：

- 这个能力很有用，但天然是 request-driven，不是 schedule-driven；
- 先保持成 ChatGPT Desktop / Codex 的调用入口，比做成 cron Agent 更稳。

## 具体边界

### A. `tony-radar`

- 目标：稳住高频外部扫描，不承担知识结晶。
- 允许写：
  - `00-Inbox-AI/hermes/curated-scout/`
  - `00-Inbox-AI/signals/`
  - `00-Inbox-AI/candidates/`
- 不允许写：
  - `learning-tasks/accepted`
  - `review-queue/accepted`
  - `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`
- 成功标准：
  - 每次最多 12 条；
  - 有 skip 机制；
  - 飞书只是投递，不是事实源。

### B. `tony-review-compressor`

- 目标：减小 Tony 的判断面。
- 允许写：
  - `00-Inbox-AI/review-queue/triage/`
- 不允许写：
  - `accepted/`, `discarded/`, `deferred/`
- 成功标准：
  - 永远只给 top 3；
  - 明确 `accept / defer / discard-candidate`；
  - 指出缺失上下文，但不替 Tony 决定。

### C. `tony-learning-planner`

- 目标：把高信号变成 Codex 可消费任务。
- 允许写：
  - `00-Inbox-AI/learning-tasks/pending/`
- 不允许写：
  - `in-progress/`, `accepted/`
  - canonical knowledge
- 成功标准：
  - 每轮 `0-3` 个 task；
  - 必须去重；
  - 优先与你当前主线强相关主题。

### D. `tony-project-companion`

- 目标：保持项目不断线，而不是做项目百科。
- 默认模式：`manual-on-demand`
- 先不建议上周扫 cron，直到 review gate 更顺。
- 输出先停在：
  - `00-Inbox-AI/project-companion/`
- 只有在 Tony 明确要推进时，Codex 再写 `40-Projects/`。

### E. `tony-publisher`

- 目标：把“值得读 / 值得分享”的内容做成 projection。
- 默认模式：`manual-on-demand`
- 输出：
  - `output-feishu/`
  - `00-Inbox-AI/feishu-publishing/`
- 绝不把 Feishu 当 source of truth。

## 建议的启用策略

### 现在就常驻

1. `tony-radar`
2. `tony-review-compressor`
3. `tony-learning-planner`

### 先按需

1. `tony-project-companion`
2. `tony-publisher`

## 你现在最值得避免的事

- 不要为每个 alias 新建目录。
- 不要让多个 Agent 同时写 `review-queue/pending/`。
- 不要让 Scout、Learning、Project、Publishing 混在一个 prompt 里。
- 不要让 Agent 自动进入 canonical promotion。

## 如果要继续扩

只有满足下面条件，才值得加第 6 个 Agent：

1. 它有独立主输出目录；
2. 它不会和现有 Agent 抢解释权；
3. 它的产出可以被 Tony 在 30 秒内判断；
4. 它解决的是当前真实瓶颈，而不是“看起来也许有用”。

## 我的建议

如果你今天就要继续推进，我建议你把心智模型改成：

```text
常驻 = radar / review-compress / learning-plan
按需 = project / publish
高风险动作 = codex 直做，不常驻化
```

这样你是在“加编组密度”，不是“加系统复杂度”。
