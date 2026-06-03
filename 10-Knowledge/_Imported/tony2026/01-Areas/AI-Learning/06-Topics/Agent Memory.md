---
title: Agent Memory
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/memory
created: 2026-03-22
updated: 2026-04-13
---

# Agent Memory

## 这个主题是什么

`Agent Memory` 关注 agent 如何在长任务、跨回合、跨会话甚至跨天的工作中保留状态、知识和经验，而不是每一轮都像从零开始。

## 为什么它现在比以前更重要

因为越来越多成熟 agent 已经不再把 memory 当成“顺手加的 retrieval”，而是把它当成 runtime 的正式组成部分：

- `Claude Code` 有 `CLAUDE.md`、project memory、subagent context
- `Google ADK` 把 `state`、`compaction`、`artifacts` 拆开
- `LangGraph` / `LangMem` 把短期 state、长期 memory、background consolidation 区分开
- `OpenClaw` 把 memory 做成 workspace durable files，并让 hooks / heartbeat / cron 能持续作用在其上
- `ChatGPT` 也已经把 `saved memories`、`chat history`、`top-of-mind prioritization` 和 `pulse` 这种异步使用方式做成正式产品面

## 2025-2026 新变化最该记什么

最近这波 memory 变化真正说明了三件事：

- `consumer/product memory` 和 `project/runtime memory` 已经明显分化
- memory 的问题开始变成 `谁写、写到哪里、跨什么边界生效`
- 异步整理、压缩、优先级管理开始比“多记一点”更重要

用更具体的话说：

- OpenAI 的 memory 已经明确区分 `saved memories` 与 `reference chat history`
- ChatGPT Plus / Pro 又加入了 `top-of-mind prioritization` 和 `nightly, asynchronous research` 的 `pulse`
- Claude Code 则把 `CLAUDE.md`、`auto memory`、`.claude/rules/`、`per working tree` 讲成正式结构
- Anthropic 的 context docs 也把 `compaction`、`context editing`、`thinking block stripping` 讲成 context management 的一部分

## 你先要抓住什么

- 记忆不等于把所有历史都塞回上下文
- `short-term state`、`session continuity`、`durable memory`、`artifacts` 不是同一个东西
- 成熟系统往往同时拥有：`state`、`checkpoint`、`memory store`、`summary`、`trace`、`artifact store`

## 常见层次

### `working memory`

当前任务临时需要的信息。

### `thread / session memory`

一个会话内持续有效的状态。

### `semantic memory`

稳定事实、偏好、配置、知识。

### `episodic memory`

过去任务和经验记录。

### `procedural memory`

逐渐稳定化的做事方式、rules、checklists、workflow defaults。

### `retrieval memory`

需要时再从外部检索回来的记忆。

## 再往前走一步：记忆和 artifact 要分开

很多系统真正的问题不在“记不住”，而在“把不该当记忆的东西也塞成记忆”。

例如：

- 文件
- diff
- 报告
- 截图
- 原始日志

这些更适合放在 `artifact layer`，再按需 summary 或 recall，而不是直接混成 durable memory。

## 两种很重要的写入方式

### `hot-path memory`

- 在执行过程中即时写入
- 优点是及时
- 问题是更容易污染系统，也更吃 latency

### `background memory`

- 先保留 trace / transcript / artifact
- 再在后台抽取、合并、纠偏
- 更适合长期运行 agent

## 现在最实用的一组边界

### `saved preference memory`

更像 end-user personalization。

### `project memory`

更像 coding / research / team workflow 的长期上下文。

### `runtime memory`

更像 agent 自己的 durable state、artifact recall 和 background consolidation。

### `context compaction`

严格说不等于 memory，但它已经成为 memory system 能否长期工作的关键配套层。

## 真正难的地方

- 什么该记，什么不该记
- 这条内容是 `state` 还是 `durable memory`
- 写入是否可靠、可审计、可修正
- 历史如何压缩，否则上下文成本会失控
- 错误记忆如何撤销、过期、纠偏
- recall 为什么发生、是否值得占用 context budget

## 为什么 OpenClaw 值得学

`OpenClaw` 很适合拿来理解 durable memory，因为它把 memory 放进 workspace 中，变成可读、可写、可编辑的系统对象，而不是把“记忆”神秘化。

## 为什么 LangGraph / LangMem 这类思路也重要

这类系统把 memory 明确拆成：

- 短期 thread/checkpoint
- 长期 store
- hot-path 写入
- background consolidation
- artifact separation

这很能代表 agent 工程的实际方向。

## 为什么“持续自我进化”最后也会回到 memory

很多所谓 self-evolving agent，真正可靠的部分往往不是“模型自己改自己”，而是：

- 持续写经验
- 背景整理经验
- 把有效经验升级成 durable memory 或 procedural rule
- 对高风险变更加 eval / review gate

## 学这页最该记住什么

- 记忆不是“模型自己记住”
- 记忆是系统如何组织状态、事实、经验、恢复能力和可追溯性
- 一个成熟 memory system 同时是 runtime 问题、product 问题、ops 问题和 governance 问题

## 典型系统案例

- [[../09-Systems/OpenClaw|OpenClaw]]
- [[../09-Systems/OpenClaw 的分层记忆设计|OpenClaw 的分层记忆设计]]
- [[../09-Systems/OpenClaw 工作原理与架构|OpenClaw 工作原理与架构]]
- [[../09-Systems/Claude Code|Claude Code]]
- [[../09-Systems/LangGraph|LangGraph]]
- [[../09-Systems/LangMem|LangMem]]
- [[../09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]
- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]

## 从工程角度继续往下读

- [[AI 记忆设计]]
- [[大模型记忆、项目记忆与 Chat Memory]]
- [[Deep Research 与 Research Agents]]
- [[自我进化与持续学习的记忆设计]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/长期运行 Agent 的记忆系统|长期运行 Agent 的记忆系统]]
- [[../../AI-Engineering/07-Topics/记忆架构：State、Memory、Artifact 与 Context|记忆架构：State、Memory、Artifact 与 Context]]
- [[../../AI-Engineering/07-Topics/记忆写入、召回、压缩与 Consolidation|记忆写入、召回、压缩与 Consolidation]]
- [[../../AI-Engineering/07-Topics/记忆评测、污染、遗忘与纠偏|记忆评测、污染、遗忘与纠偏]]

## 相关

- [[Agent]]
- [[Tool Use]]
- [[Planning and Control]]
- [[Long Context]]
- [[RAG]]
- [[A2A（Agent-to-Agent）与协作协议]]
- [[../07-Maps/AI Agent Capability Map|AI Agent Capability Map]]
- [[../07-Maps/AI 记忆设计图|AI 记忆设计图]]
- [[../11-Recent-Supplements/2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime|2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime]]
