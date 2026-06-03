---
title: AI 记忆设计
type: topic
status: learning
tags:
  - ai/topic
  - ai/memory
  - ai/agent
created: 2026-03-29
updated: 2026-03-29
---

# AI 记忆设计

## 这个主题是什么

`AI 记忆设计` 关注的不是“模型会不会记住”，而是我们怎样把 `weights`、`context`、`session state`、`durable memory`、`artifacts`、`background consolidation` 这些层组织成一个可靠系统。

如果说 `上下文工程` 在问“当前这一轮要给模型什么信息”，那么 `AI 记忆设计` 在问的是：

- 什么需要跨轮保留
- 什么应该跨会话保留
- 什么必须写盘
- 什么只能当临时状态
- 什么应该由后台整理，而不是热路径直接写入

## 为什么它现在值得单独拆出来学

这条线已经不只是 `RAG` 的附属品了。

最近越来越多 agent / harness / runtime 系统都把 memory 当成一等能力：

- `ChatGPT` 开始把 `saved memories`、`projects`、`chat history` 区分开
- `Claude Code` 把 `CLAUDE.md`、project memory、subagent context 做成正式工作面
- `Google ADK` 明确拆 `state`、`compaction`、`artifacts`
- `LangGraph` / `LangMem` 把短期 state、长期 store、background consolidation 拆成正式运行时问题
- `OpenClaw` 则把 memory 直接做成 workspace 文件、hook、heartbeat、cron 可以长期操作的 durable layer

也就是说，memory 不再只是“给模型多点上下文”，而是 runtime、product、ops、governance 一起交叉的系统层。

## 先抓住 6 个层次

### 1. `weights memory`

模型通过 pretraining、post-training、finetuning 真正“学会”的内容。

### 2. `context / working memory`

只在当前窗口或当前 step 内活跃的信息。

### 3. `session memory`

同一个 thread / task / working tree 内持续有效的状态。

### 4. `durable memory`

跨 session 继续保留的稳定事实、偏好、配置、经验。

### 5. `artifact memory`

文件、截图、diff、报告、structured outputs。它们往往不是“记忆文本”，但会成为未来 recall 的关键依据。

### 6. `background memory`

不是每次都热路径写入，而是把 transcript / trace / artifacts 交给后台抽取、压缩、整理、纠偏。

## 这条线真正难的地方

- 什么该记，什么不该记
- 什么属于 `state`，什么属于 `memory`
- 什么应该压缩成 summary，什么必须保留 raw trace
- 什么适合 per-user，什么适合 per-project，什么适合 per-agent
- 写入和读取的权限边界怎么设计
- 系统怎么防止记忆污染、记忆陈旧和错误自强化

## 一个很重要的判断

`记忆` 不等于“把所有历史塞回上下文”。

真正成熟的系统一般都会同时做这几件事：

- 区分 `hot-path state` 和 `durable memory`
- 让 artifacts 单独存放
- 对长期记忆使用更保守的 `write policy`
- 通过 recall policy / compaction / background jobs 控制成本
- 给记忆加 provenance、过期和撤销能力

## 这条学习线怎么读

### 抽象层

1. [[Agent Memory]]
2. [[大模型记忆、项目记忆与 Chat Memory]]
3. [[自我进化与持续学习的记忆设计]]
4. [[从 Learnings 到 AutoSkill：技能自提炼]]

### 系统层

5. [[../09-Systems/OpenClaw 的分层记忆设计|OpenClaw 的分层记忆设计]]
6. [[../09-Systems/LangMem|LangMem]]
7. [[../09-Systems/LangGraph|LangGraph]]
8. [[../09-Systems/Claude Code|Claude Code]]
9. [[../09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]
10. [[../09-Systems/Self-Improving-Agent（ClawHub Skill）|Self-Improving-Agent（ClawHub Skill）]]

### 工程层

11. [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
12. [[../../AI-Engineering/07-Topics/长期运行 Agent 的记忆系统|长期运行 Agent 的记忆系统]]
13. [[../../AI-Engineering/07-Topics/记忆架构：State、Memory、Artifact 与 Context|记忆架构：State、Memory、Artifact 与 Context]]
14. [[../../AI-Engineering/07-Topics/记忆写入、召回、压缩与 Consolidation|记忆写入、召回、压缩与 Consolidation]]
15. [[../../AI-Engineering/07-Topics/记忆评测、污染、遗忘与纠偏|记忆评测、污染、遗忘与纠偏]]
16. [[../../AI-Engineering/07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]

### 实践层

17. [[../../AI-Engineering/06-Projects/Memory Lab/项目总览|Memory Lab]]
18. [[../../AI-Engineering/06-Projects/Memory Lab/Self-Improving-Agent 与 AutoSkill 实验|Self-Improving-Agent 与 AutoSkill 实验]]

## 为什么 OpenClaw 在这条线里特别重要

`OpenClaw` 值得学，不是因为它抽象地说自己有 memory，而是因为它把 memory 做成了：

- `MEMORY.md`
- `memory/YYYY-MM-DD.md`
- hooks / heartbeat / cron 可以驱动的 durable files
- workspace 中可审计、可编辑、可修正的系统对象

这让我们很容易把“记忆”从神秘概念，拉回到可操作的系统设计。

## 为什么“持续自我进化”要谨慎理解

很多人说到 self-evolving agent，会默认觉得系统会“自己越来越聪明”。

更稳的理解是：

- 一部分能力来自模型本身
- 一部分来自可写的 memory / rules / artifacts
- 一部分来自后台 consolidation 和 reflection
- 一部分来自 eval gate 后的人类修正

也就是说，真正能交付的通常不是“任由 agent 自己写自己”，而是：

`controlled self-maintenance + bounded self-improvement + auditable memory updates`

## 相关地图

- [[../07-Maps/AI 记忆设计图|AI 记忆设计图]]
- [[../07-Maps/AI 记忆学习导航.canvas|AI 记忆学习导航（Canvas）]]
- [[../07-Maps/AI 记忆学习导航.base|AI 记忆学习导航（Base）]]
- [[../../AI-Engineering/08-Maps/AI Memory Engineering Map|AI Memory Engineering Map]]

## 相关

- [[Agent Memory]]
- [[Long Context]]
- [[RAG]]
- [[上下文工程]]
- [[Agent]]
- [[../07-Maps/AI Agent Capability Map|AI Agent Capability Map]]
