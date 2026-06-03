---
title: 大模型记忆、项目记忆与 Chat Memory
type: topic
status: learning
tags:
  - ai/topic
  - ai/memory
  - ai/product
created: 2026-03-29
updated: 2026-03-29
---

# 大模型记忆、项目记忆与 Chat Memory

## 这页想拆开什么

大家常说“模型记住了我”，但这里其实混了至少四种不同东西：

- 模型参数里的知识
- 聊天历史
- 产品层的 saved memory / project memory
- agent / runtime 的 durable memory

如果不把这些分开，后面讨论 memory design 很容易跑偏。

## 四层最容易混淆的“记忆”

### 1. `weights memory`

这是模型在 pretraining、instruction tuning、preference optimization 之后固化到参数里的知识。

优点：

- 运行时不需要额外 recall
- 泛化能力强

缺点：

- 更新慢
- 不可细粒度审计
- 很难只对一个用户或一个项目生效

### 2. `chat history`

这是产品把对话历史继续留在上下文或 history system 里。

它更像连续会话，不等于 durable memory。

### 3. `saved memory / project memory`

这是产品层对稳定信息的正式抽取和保留。

例如：

- 用户偏好
- 项目范围
- 输出风格
- 持续规则

### 4. `runtime durable memory`

这是 agent / harness / runtime 自己维护的 memory store、workspace files、knowledge store、artifact store。

这一层比普通 chat product 更接近工程系统。

## 为什么 `project memory` 值得单独理解

因为它代表了一个重要转向：

从“产品记住一个用户”，转向“产品记住某个工作空间、任务空间、项目空间”。

这对 coding agent、research agent、team assistant 都很关键。

项目级 memory 最常见保留的是：

- domain glossary
- codebase 约定
- repo 规则
- 当前目标和限制
- 团队默认 workflow

## 三种很典型的系统思路

### ChatGPT / ChatGPT Projects

更偏：

- saved memories
- chat history
- project-scoped context
- 面向 end-user 的 product memory

### Claude Code

更偏：

- `CLAUDE.md`
- project / personal memory
- subagent context inheritance
- terminal-first coding harness 的项目规则记忆

### OpenClaw

更偏：

- workspace files
- `MEMORY.md`
- append-only daily logs
- hooks / heartbeat / cron 可长期操作的 durable memory

## 什么时候不该叫“模型记忆”

如果信息是：

- 由外部文件提供
- 由 project workspace 提供
- 由 memory store / vector / markdown files 提供
- 由系统后台 consolidation 后再召回

那么更准确的名字通常是：

- `product memory`
- `project memory`
- `agent memory`
- `runtime memory`

而不是“模型自己记住了”。

## 一个很实用的判断框架

### 该进参数层的

- 通用能力
- 大范围稳定知识
- 不依赖具体用户/项目的行为偏好

### 该进项目层的

- repo 规范
- 产品文案风格
- 某个研究项目的上下文
- 团队自己的工作习惯

### 该进 durable memory 的

- 用户长期偏好
- 已确认事实
- 长期运行 agent 的经验记录
- 需要跨天延续的规则

### 不该长期保留的

- 临时猜测
- 未核实结论
- 一次性工具输出
- 大段原始日志

## 这页最该形成的判断力

- `chat continuity` 不是 `durable memory`
- `project memory` 比“单用户记住偏好”更适合 agent 工程
- “模型学到的”与“系统运行时保留的”必须分开讨论

## 推荐继续往下读

- [[AI 记忆设计]]
- [[Agent Memory]]
- [[自我进化与持续学习的记忆设计]]
- [[../09-Systems/Claude Code|Claude Code]]
- [[../09-Systems/OpenClaw 的分层记忆设计|OpenClaw 的分层记忆设计]]
- [[../../AI-Engineering/07-Topics/记忆架构：State、Memory、Artifact 与 Context|记忆架构：State、Memory、Artifact 与 Context]]

## 官方资料

- [ChatGPT Projects](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt)
- [ChatGPT Memory FAQ](https://help.openai.com/en/articles/8590148-memory-faq)
- [Claude Code Memory](https://docs.anthropic.com/en/docs/claude-code/memory)
