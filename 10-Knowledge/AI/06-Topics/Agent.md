---
title: Agent
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
created: 2026-03-01
updated: 2026-04-14
---

# Agent

## 这个主题是什么

`Agent` 关注模型如何结合工具、记忆、规划与执行，完成多步任务。

## 为什么重要

- 它把模型从回答问题推进到执行工作
- 也是 AI 产品和自动化工作流的关键方向
- 到了 `2025-2026`，agent 已经不只是 tool loop，而是在往 `research agent`、`coding agent`、`browser / computer-use agent`、`voice agent` 和 `长期运行工作台` 分化

## 你先要抓住什么

- agent 不等于“一个更聪明的聊天机器人”
- agent 的核心在于：给定目标后，系统能否自己拆任务、调用工具、根据结果继续推进
- 一个 agent 通常由模型、工具、状态、执行循环和约束机制共同组成

## 常见组成

- 模型：负责理解目标、生成计划、决定下一步
- 工具：搜索、代码执行、数据库、浏览器、API
- 记忆：保存任务上下文或历史结果
- 控制层：限制权限、管理循环、处理失败

## 最近两年最值得补的新判断

- agent 不再等于“会调工具的聊天模型”
- `deep research` 说明长任务研究已经成了正式能力 lane
- `memory / context management` 已经开始成为 runtime 一等层
- `MCP` 和 `A2A` 说明 agent 生态正在协议化，而不是只靠单一框架
- 真正成熟的 agent 已经天然连到 `approval`、`audit`、`release gate` 和 `governance`

## 关键问题

- agent 什么时候比普通 prompt 更有价值
- 为什么很多 agent demo 看起来厉害，但真实生产中很难稳定
- tool use、reasoning、memory 各自扮演什么角色
- `research agent`、`browser agent`、`workflow agent`、`coding agent` 的边界怎么分
- 什么时候应该用 local sub-agent，什么时候应该走 `A2A`

## 当前关联模型 / 产品

- [[ChatGPT]]
- [[OpenAI API]]
- [[Claude Code]]
- [[DeepSeek API]]
- [[OpenClaw]]

## 作为系统案例

- `OpenClaw` 很适合拿来理解“agent 从概念走向长期运行系统”这一层
- 它强调 gateway、channels、tools、sessions 和 memory，而不只是一个 tool loop demo
- 如果你想继续拆系统层，进入 [[OpenClaw 工作原理与架构]]

## 最近值得接回的路线

- [[Deep Research 与 Research Agents]]
- [[Agent Memory]]
- [[上下文工程]]
- [[MCP（Model Context Protocol）]]
- [[A2A（Agent-to-Agent）与协作协议]]
- [[../../AI-Engineering/07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]
- [[../11-Recent-Supplements/2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime|2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime]]

## 相关

- [[RAG]]
- [[Coding Agents]]
- [[Developer Tools]]
- [[Reasoning Models]]
- [[Browser Agents 与 Computer Use]]
- [[OpenClaw]]
- [[OpenClaw 工作原理与架构]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
- [[../../AI-Engineering/07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]
