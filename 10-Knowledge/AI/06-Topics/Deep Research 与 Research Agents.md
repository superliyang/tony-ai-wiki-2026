---
title: Deep Research 与 Research Agents
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/research-agent
created: 2026-04-13
updated: 2026-04-13
---

# Deep Research 与 Research Agents

## 这个主题是什么

`Deep Research` 和 `Research Agents` 讨论的不是“模型能不能搜一下网页”，而是系统能不能围绕复杂问题做持续研究：

- 拆解研究任务
- 多步检索和转向
- 读取网页、PDF、图像、文件
- 做来源筛选
- 做中间分析
- 写出带证据的结果

## 为什么它在 2025-2026 变成独立主线

因为这一波变化已经不再只是：

- search tool
- browse mode
- citation feature

而是开始出现完整的 `research lane`。

最有代表性的锚点是 [[../04-Papers/Deep Research System Card|Deep Research System Card]]，它把：

- web browsing
- file reading
- python analysis
- long-horizon reasoning
- citations

收成同一个 agentic capability。

## 你先要抓住什么

- `research agent` 不等于 `RAG`
- `research agent` 也不等于 `browser agent`
- 研究型 agent 的价值在于：`能不能在长任务里维持目标、过滤证据、组织输出`

## 它和相邻概念怎么分

### `RAG`

更像：

- 从预先准备好的知识库中找资料
- 偏内部知识、偏检索增强

### `browser / computer use`

更像：

- 对网页和界面进行动作执行
- 偏动作面和环境交互

### `deep research`

更像：

- 面向复杂问题的研究型工作流
- 偏证据收集、来源对比、综合分析和成文输出

## 一个成熟 research agent 往往会包含什么

- `goal decomposition`
- `search / browse / fetch`
- `source selection`
- `note / state management`
- `analysis tool`，例如 python
- `citation and report synthesis`
- `approval / safety boundary`

## 真正难的地方

- 什么来源可信，什么只是噪音
- 多步研究过程中何时该转向
- 什么时候该停止继续搜索
- 长任务里的状态如何保持而不被污染
- 如何防 prompt injection、来源污染和数据泄露

## 为什么它会自然连到 memory 和 context management

因为 research agent 很少是短任务。

它天然会遇到：

- 长上下文膨胀
- tool results 积累
- 中间结论和最终结论分层
- 持续研究中的 session continuity
- recall / compaction / artifact separation

所以你如果只把它理解成“search with citations”，就会低估它真正的工程难度。

## 为什么它也会自然连到治理

研究型 agent 的风险面通常比普通问答更大：

- 外部来源可能带 prompt injection
- 模型可能在长链里漂移
- 可能碰到隐私与受限内容
- 带 citation 的结果更容易被人误信为“已经核实”

所以这条线会直接连到：

- eval
- safeguards
- approval
- transparency

## 代表锚点

- [[../04-Papers/Deep Research System Card|Deep Research System Card]]
- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]
- [[../09-Systems/OpenAI API|OpenAI API]]

## 推荐继续往下读

- [[Agent]]
- [[Browser Agents 与 Computer Use]]
- [[Agent Memory]]
- [[上下文工程]]
- [[MCP（Model Context Protocol）]]
- [[模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act]]
- [[../11-Recent-Supplements/2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime|2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime]]

## 相关

- [[RAG]]
- [[Browser Agents 与 Computer Use]]
- [[Agent Memory]]
- [[上下文工程]]
- [[../07-Maps/AI Agent Capability Map|AI Agent Capability Map]]
