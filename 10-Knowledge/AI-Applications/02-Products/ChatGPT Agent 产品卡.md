---
title: ChatGPT Agent 产品卡
type: product
status: learning
tags:
  - ai/product
  - ai/agent
company: OpenAI
target_users:
  - knowledge workers
  - analysts
  - operators
core_features:
  - browser-based online task execution
  - file analysis
  - apps and connectors
  - terminal support
value_proposition: 把复杂在线任务交给一个通用 agent 去研究、浏览、操作，再由用户在关键节点确认
pricing: depends on ChatGPT plan and usage limits
related_models: []
related_workflows:
  - Research Agent Workflow
  - Enterprise Operations Agent Workflow
created: 2026-03-22
updated: 2026-03-22
---

# ChatGPT Agent 产品卡

## 简介

`ChatGPT Agent` 更像一个面向通用知识工作者的 cloud agent。它适合处理跨网页、文件、数据源和轻度操作的复杂任务，而不是只做对话问答。

## 核心功能

- visual browser 浏览网页
- code interpreter 做分析和代码执行
- app / connector 连接数据源
- terminal 执行受支持命令
- 关键节点停下来等用户澄清或确认

## 最适合的使用方式

- 研究型任务
- 信息整合与报告生成
- 需要连接多数据源的分析工作
- 轻量运营与流程辅助

## 价值点

- 降低通用知识工作里的多步操作负担
- 对非技术用户也相对友好
- 能把“研究 + 操作 + 汇总”收在一个统一入口里

## 边界与注意点

- 更像云端通用 agent，不是仓库深度绑定型 coding agent
- 一旦接入登录态、邮件、第三方 app，就要重点考虑 prompt injection 和审批问题
- 更适合做“受监督的复杂任务”，而不是完全无人值守的高风险流程

## 使用场景

- 市场和竞品研究
- 跨系统的信息搜集和整理
- 内部运营辅助
- 个人知识工作助理

## 竞争与差异

- 和 `Claude Code`、`Cursor` 比，它不是默认围绕代码仓库展开
- 和 `OpenClaw` 比，它更偏托管式 cloud product，而不是 self-hosted runtime

## 来源

- 官方帮助文档：[ChatGPT agent](https://help.openai.com/en/articles/11752874-chatgpt-agent)

## 相关

- [[../../AI-Learning/09-Systems/ChatGPT Agent|ChatGPT Agent]]
- [[../03-Workflows/Research Agent Workflow|Research Agent Workflow]]
- [[../03-Workflows/Enterprise Operations Agent Workflow|Enterprise Operations Agent Workflow]]
