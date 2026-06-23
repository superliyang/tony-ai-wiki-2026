---
title: Tool Use
type: topic
status: draft
tags:
  - ai/topic
  - ai/agent
  - ai/tool-use
created: 2026-03-22
updated: 2026-03-22
---

# Tool Use

## 这个主题是什么

`Tool Use` 关注模型如何不只“说”，而是真的通过浏览器、代码执行、数据库、搜索、API、文件系统等外部能力去完成任务。

## 为什么重要

- 它是 `Agent` 从“会推理”走向“会执行”的关键跳板
- 很多真实 AI 产品的价值，不来自模型本身，而来自模型能否安全、稳定地调工具
- 一旦进入 `tool use`，问题就从 prompt 迅速扩展到权限、失败恢复、结果验证和状态管理

## 你先要抓住什么

- tool use 不是“模型输出一段调用格式”这么简单
- 真正重要的是：工具的选择、参数构造、执行回读、错误处理、结果验证、下一步决策
- 当工具进入 `browser / computer use`、`CLI`、`MCP` 这些不同动作面时，治理方式也会明显不同
- 一个成熟 agent 系统里，tool use 更像受控 action layer，而不是装饰性的 function call demo

## 常见工具类型

- 信息获取：`web search`、`web fetch`、数据库查询、知识库检索
- 环境操作：`shell / exec`、文件读写、代码运行
- 外部系统：HTTP API、业务系统、SaaS 集成
- UI 与界面：浏览器、表单、页面点击、截图、computer use
- 长期任务：消息发送、计划任务、事件触发

## 真正难的地方

- 模型会不会选错工具
- 参数格式是否稳定
- 工具返回结果是否足够结构化，能被下一步消费
- 执行失败时系统如何重试、回滚、请求人工确认
- 工具权限怎么控制，避免 agent 做出高风险动作

## 和普通聊天产品的边界

- 没有 tool use 的系统，更像“推理和表达层”
- 有 tool use 的系统，才开始拥有真正的动作能力
- 但工具越多，并不自动意味着系统越强；关键在 orchestration 和约束机制

## 典型系统案例

- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]
- [[../09-Systems/Codex|Codex]]
- [[../09-Systems/Cursor|Cursor]]
- [[../09-Systems/Claude Code|Claude Code]]
- [[../09-Systems/OpenClaw|OpenClaw]]

## 从工程角度继续往下读

- [[../../AI-Engineering/07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
- [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
- [[../../AI-Engineering/07-Topics/Planning Loops and State Machines|Planning Loops and State Machines]]

## 相关

- [[Agent]]
- [[Agent Memory]]
- [[Planning and Control]]
- [[AI Assistant]]
- [[Coding Agents]]
- [[../07-Maps/AI Agent Capability Map|AI Agent Capability Map]]
