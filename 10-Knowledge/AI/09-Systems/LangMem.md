---
title: LangMem
type: system
status: learning
tags:
  - ai/system
  - ai/memory
  - ai/agent
  - ai/langchain
created: 2026-03-29
updated: 2026-03-29
---

# LangMem

## 它是什么

`LangMem` 是 LangChain / LangGraph 生态里专门把 memory 提升为正式系统能力的一层。它不是单纯的 vector store，也不是“长上下文替代品”，而是围绕 agent memory 的：

- extraction
- write policy
- retrieval
- background processing
- evaluation

去组织一个更明确的 memory pipeline。

## 为什么它值得单独看

如果只看 `LangGraph`，你会更容易把注意力放在 graph、checkpoint、interrupt、resume。

而 `LangMem` 值得学的地方是：它把 memory 从“顺手加一下”推进成：

- 可区分的 memory 类型
- 明确的 hot-path / background 写入策略
- 与 agent success / failure 直接相关的系统层

## 你可以把它理解成什么

- `LangGraph` 更像运行内核
- `LangMem` 更像 memory subsystem / memory toolkit

它帮助你把“状态管理”和“长期记忆管理”从一个模糊大桶里拆开。

## 它最值得抓住的几个点

### 1. memory 不是一个桶，而是多种类型

LangMem 的文档路线很强调：agent 需要的不只是“历史越多越好”，而是不同类型的 memory。

常见可对应到：

- semantic memory
- episodic memory
- procedural memory

### 2. 写入可以分热路径和后台

有些记忆适合在任务中即时写入；有些更适合先记 trace，再后台 consolidation。

这让 memory system 更像一个长期运行的 pipeline，而不是“模型临时写几句话”。

### 3. 它把 memory 和 eval 绑在一起

一条 memory 值不值得保留，不能只看“写得出来”，还要看：

- 是否提升任务完成率
- 是否降低重复错误
- 是否引入污染
- 是否导致过拟合某个局部经验

## 它最适合拿来学什么

- memory taxonomy
- write / retrieve / consolidate 的完整闭环
- 长期运行 agent 的 memory subsystem 怎么组织
- 为什么“更多记忆”不等于“更好 agent”

## 和 OpenClaw 的差异

- `OpenClaw` 更像 explicit workspace-based durable memory
- `LangMem` 更像 abstract memory toolkit / subsystem thinking

一个更适合学“可审计、文件化、可操作的分层记忆”，一个更适合学“memory pipeline 的抽象设计”。

## 推荐继续往下读

- [[LangGraph]]
- [[../06-Topics/AI 记忆设计|AI 记忆设计]]
- [[../06-Topics/Agent Memory|Agent Memory]]
- [[OpenClaw 的分层记忆设计]]
- [[../../AI-Engineering/07-Topics/记忆架构：State、Memory、Artifact 与 Context|记忆架构：State、Memory、Artifact 与 Context]]
- [[../../AI-Engineering/07-Topics/记忆写入、召回、压缩与 Consolidation|记忆写入、召回、压缩与 Consolidation]]
- [[../../AI-Engineering/07-Topics/记忆评测、污染、遗忘与纠偏|记忆评测、污染、遗忘与纠偏]]

## 官方资料

- [LangMem Docs](https://langchain-ai.github.io/langmem/)
- [LangMem Quickstart](https://langchain-ai.github.io/langmem/guides/quickstart/)
- [LangGraph Memory](https://docs.langchain.com/oss/python/langgraph/add-memory)
