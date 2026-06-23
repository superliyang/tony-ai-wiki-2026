---
title: Agent 核心开源样本对比：LangGraph、AutoGen、OpenHands、browser-use、MCP Servers、A2A
type: case-study
status: learning
created: 2026-04-03
updated: 2026-04-03
---

# Agent 核心开源样本对比：LangGraph、AutoGen、OpenHands、browser-use、MCP Servers、A2A

## 为什么这 6 个要放在一起看

这 6 个项目或协议经常同时出现在“Agent 开源栈”讨论里，但它们分别代表的层其实完全不同。

如果不拆开看，很容易出现这种误解：

- 把 `LangGraph` 当成通用 multi-agent 协议
- 把 `AutoGen` 当成 browser runtime
- 把 `MCP Servers` 当成完整 agent framework
- 把 `A2A` 当成 tool protocol

这页的目标，就是先把“它们各自代表哪一层”这件事钉死。

## 一张先抓住差异的表

| 样本 | 它代表的核心层 | 最适合学什么 | 不该把它误认为 |
| --- | --- | --- | --- |
| `LangGraph` | state graph / orchestration runtime | 有状态编排、graph-based agent flow、durable execution | 全部 agent 问题的统一答案 |
| `AutoGen` | multi-agent interaction pattern | agent 协作、角色分工、会话式 orchestration | browser / coding / tool protocol 本身 |
| `OpenHands` | coding agent execution stack | coding agent 落地、repo task execution、software task loop | 通用 agent orchestration framework |
| `browser-use` | browser action surface | browser-grounded agent、网页动作面、UI automation | agent memory / protocol / orchestration 全栈 |
| `MCP Servers` | tool integration protocol plane | 标准化工具接入、共享服务面、tool contract | agent-to-agent 协作协议 |
| `A2A` | agent-to-agent protocol plane | agent 间协作、任务移交、跨 agent 边界 | tool calling 协议 |

## 最实用的理解方式

### LangGraph

你该从它学的是：

- graph orchestration
- stateful execution
- durable / resumable flow
- agent runtime how-to

如果你的问题是“多步流程怎么稳定跑”，它很关键。

### AutoGen

你该从它学的是：

- multi-agent collaboration
- roles and delegation
- conversation-driven orchestration

如果你的问题是“多个 agent 如何分工”，它很关键。

### OpenHands

你该从它学的是：

- coding agent 的任务推进方式
- repo / issue / patch / execution 闭环
- agent 落到软件工程任务后的真实样子

如果你的问题是“coding agent 到底怎么落地”，它很关键。

### browser-use

你该从它学的是：

- browser 作为动作面
- 网页任务执行
- UI-grounded agent 的工程边界

如果你的问题是“agent 怎么真正操作网页”，它很关键。

### MCP Servers

你该从它学的是：

- tool 接入标准化
- 共享服务面
- tool schema / protocol / reuse

如果你的问题是“能力如何被规范接入”，它很关键。

### A2A

你该从它学的是：

- agent 间协议
- 任务委托与移交
- 不同 agent 之间的协作边界

如果你的问题是“agent 和 agent 怎么说话”，它很关键。

## 读这 6 个最稳的顺序

### 如果你先想建立 stack 判断

1. [[../03-Projects/LangGraph|LangGraph]]
2. [[../03-Projects/AutoGen|AutoGen]]
3. [[../03-Projects/OpenHands|OpenHands]]
4. [[../03-Projects/browser-use|browser-use]]
5. [[../03-Projects/MCP Servers|MCP Servers]]
6. [[../03-Projects/A2A|A2A]]

### 如果你先想建立“层次感”

1. `orchestration/runtime`: [[../03-Projects/LangGraph|LangGraph]]
2. `multi-agent collaboration`: [[../03-Projects/AutoGen|AutoGen]]
3. `coding agent execution`: [[../03-Projects/OpenHands|OpenHands]]
4. `browser action`: [[../03-Projects/browser-use|browser-use]]
5. `tool protocol`: [[../03-Projects/MCP Servers|MCP Servers]]
6. `agent protocol`: [[../03-Projects/A2A|A2A]]

## 最常见的 4 个误区

### 误区 1：把协议当成产品

`MCP` 和 `A2A` 更像协议面，不是完整产品栈。

### 误区 2：把动作面当成 runtime

`browser-use` 很强，但它解决的是 browser 动作，不是整套 memory / orchestration / governance。

### 误区 3：把 orchestration 当成 coding agent 落地

`LangGraph` 和 `AutoGen` 能讲很多编排问题，但不自动等于 `OpenHands` 这种软件工程执行闭环。

### 误区 4：一上来同时追太多项目

更稳的做法是先用这 6 个建立层次感，再决定往哪一层深挖。

## 读完这页后你应该能自己回答

- 这 6 个样本分别处在 agent stack 的哪一层
- 你当前更该学 orchestration、browser action、tool protocol，还是 coding agent execution
- 为什么它们值得一起跟，但不该混成一个“agent framework 桶”

## 关联

- [[../06-Maps/Agent 系统核心 8 关系图|Agent 系统核心 8 关系图]]
- [[../03-Projects/项目索引|项目索引]]
- [[../04-Patterns/State Graph 与 Agent Runtime 模式|State Graph 与 Agent Runtime 模式]]
- [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]]
- [[../../AI-Engineering/07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]
- [[../../AI-Engineering/07-Topics/A2A 与 Multi-Agent Coordination|A2A 与 Multi-Agent Coordination]]
