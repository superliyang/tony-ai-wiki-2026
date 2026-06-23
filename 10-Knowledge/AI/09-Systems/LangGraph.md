---
title: LangGraph
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/langgraph
created: 2026-03-25
updated: 2026-03-29
---

# LangGraph

## 它是什么

`LangGraph` 是 LangChain 生态里的 graph-based agent runtime。官方定位强调它适合构建 stateful、long-running、可恢复的 agent workflow。

如果你把 `ADK` 看成 agent framework，把 `Langfuse` 看成 observability / eval 平台，那么 `LangGraph` 更像是：

- 状态图 runtime
- durable execution 内核
- checkpoint / interrupt / resume 的执行层

## 为什么它在 Agent 平台里特别重要

Agent 平台一旦从 demo 进入真实系统，就会很快碰到这些问题：

- thread state 怎么存
- task 中断之后怎么恢复
- 人审之后怎么继续
- 一个长任务如何跨多轮、多工具、多审批点继续跑

这正是 `LangGraph` 最有代表性的地方。

## 它最值得抓住的 4 个点

### 1. Graph 不是为了炫技，而是为了显式控制状态迁移

在简单 demo 里，agent 看起来像一个循环：`think -> call tool -> think -> answer`。

但平台化之后，你会需要更清楚的：

- state
- node
- edge
- checkpoint
- retry / interrupt / resume

`LangGraph` 的 graph 结构，本质上是在给这些状态迁移一个工程化表达。

### 2. Durable execution 是它最像平台内核的地方

官方文档把 `durable execution` 单独拿出来讲，这很关键。因为这意味着：

- 任务不是一次性函数调用
- agent thread 可以被持久化
- 异步等待、人审、失败恢复都能进入正式生命周期

### 3. Human-in-the-loop 是一等公民

`LangGraph` 官方文档专门讲 `human-in-the-loop` 和 `interrupts`。这对于平台特别重要，因为真实企业环境里，很多 agent 不是“不让人介入”，而是“允许在关键点介入”。

### 4. 它的 memory 价值在于把 `checkpoint` 和 `long-term memory` 分开

很多人第一次看 `LangGraph`，会只记得 graph 和 durable execution。

但如果从 memory design 角度看，它更重要的是：

- `checkpointer` 代表短期 thread / workflow state
- `store` / memory 代表长期可召回信息
- `add-memory` 这条文档线说明它并不把所有历史都混成一个 context bucket

这让它很适合和 `LangMem` 一起读。

### 5. 它更像平台 runtime，而不是 end-user product

`LangGraph` 很强，但它不是：

- 完整的 observability product
- 完整的 prompt / eval product
- 完整的 channel product

所以它很适合做平台的执行内核，但仍然需要和：

- `Langfuse`
- channel adapters
- approval / policy services
- tool gateway

这些层组合起来。

## 在 Agent 平台里，我会怎么放它

如果现在要搭一个可以承接 `Feishu / Web / API` 的 agent platform，我会优先把 `LangGraph` 放在：

- `thread runtime`
- `checkpoint / resume engine`
- `interrupt / approval continuation engine`
- `workflow graph layer`

## 为什么它比“纯 SDK-first agent loop”更适合作平台底座

因为平台真正痛的部分，不在“我能不能调用一次模型”，而在：

- 会话状态
- 审批点
- 长任务恢复
- 失败重试
- 任务 legibility

这些点上，`LangGraph` 的官方能力说明明显更接近平台 runtime。

## 什么时候 LangGraph 不够

- 你需要更标准化的 `A2A` 生态互操作时
- 你需要更完整的 trace / prompt / eval / scoring 平台时
- 你需要完整 end-user product 或 channel layer 时

所以它不是一切，但它非常适合做中间那层“运行内核”。

## 推荐继续往下读

- [[Google Agent Development Kit（ADK）]]
- [[LangMem]]
- [[Langfuse]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]

## 关联

- [[../06-Topics/Agent 平台|Agent 平台]]
- [[../06-Topics/Agent Memory|Agent Memory]]
- [[Google Agent Development Kit（ADK）]]
- [[LangMem]]
- [[Langfuse]]
- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]

## 资料

- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangGraph Add Memory](https://docs.langchain.com/oss/python/langgraph/add-memory)
- [LangGraph Durable Execution](https://docs.langchain.com/oss/python/langgraph/durable-execution)
- [LangGraph Human-in-the-Loop](https://docs.langchain.com/oss/python/langgraph/human-in-the-loop)
