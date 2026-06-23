---
title: AI Coding Workbench
type: topic
status: active
tags:
  - ai/topic
  - ai/coding-workbench
created: 2026-03-25
updated: 2026-03-25
---

# AI Coding Workbench

## 这个主题是什么

`AI Coding Workbench` 关注的不是单个 coding model，而是“模型 + 工具 + runtime + session + eval + approval + artifacts” 组合成的一整套工作台。

## 为什么重要

过去半年最明显的变化之一，就是 frontier 公司不再只发布“更强的 coding 模型”，而是在发布：

- coding SDK
- terminal / IDE / app server
- session 与 checkpoint
- approval / sandbox
- eval harness
- team integration

也就是说，coding 竞争正在从“模型质量”快速转向“工作台质量”。

## 最近半年为什么这个主题突然更重要

在 `2025-09-25` 到 `2026-03-25` 之间，这条线明显升温：

- [[OpenAI]]：`Codex GA`、`GPT-5.2-Codex`、`GPT-5.3-Codex`、`Codex harness / App Server`
- [[Anthropic]]：`Claude Sonnet 4.5`、`Claude Agent SDK`、`Xcode` 原生接入
- [[Google DeepMind]]：`Gemini 3` 和 `Google Antigravity`
- [[Alibaba Cloud]]：`Qwen Code`
- [[Moonshot AI]]：`Kimi CLI support`
- [[MiniMax]]：`M2.5` 把 coding 和 agent tool use 拉成主叙事

## 你先要抓住什么

- workbench 不等于一个聊天框加一个模型
- 真正的 coding workbench 至少要包含：`task surface + tool surfaces + environment + memory + feedback loop + approval boundary`
- coding agent 的长期竞争力，很可能取决于工作台，而不只是模型本身

## 关键组成

1. `model layer`
- coding / reasoning / tool-use capable model

2. `runtime layer`
- thread
- session
- checkpoint
- resume
- app server

3. `tool layer`
- CLI
- IDE actions
- MCP tools
- browser / computer use

4. `control layer`
- approval
- sandbox
- budgets
- permissions

5. `feedback layer`
- tests
- eval harness
- regression suite
- trace / observability

## 这一层怎么和其他主题连接

- 如果你想理解“为什么 prompt engineering 不够了”，就连到 [[提示词工程]] 和 [[上下文工程]]。
- 如果你想理解“工具接入怎么标准化”，就连到 [[MCP（Model Context Protocol）]]。
- 如果你想理解“为什么工作台最终会变成平台”，就连到 [[Agent 平台]]。
- 如果你想看工程抽象，就连到 [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]] 和 [[../../AI-Engineering/07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]]。

## 当前最值得对照看的系统

- [[../09-Systems/Codex|Codex]]
- [[../09-Systems/Claude Code|Claude Code]]
- [[../09-Systems/Cursor|Cursor]]
- [[../09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]
- [[../09-Systems/LangGraph|LangGraph]]
- [[../09-Systems/OpenClaw|OpenClaw]]

## 相关

- [[Coding Agents]]
- [[Agent 平台]]
- [[Developer Tools]]
- [[API Economy]]
- [[过去半年全球 AI 前沿动态（2025-09-25 至 2026-03-25）]]
- [[../07-Maps/AI 前沿主题演化图|AI 前沿主题演化图]]
