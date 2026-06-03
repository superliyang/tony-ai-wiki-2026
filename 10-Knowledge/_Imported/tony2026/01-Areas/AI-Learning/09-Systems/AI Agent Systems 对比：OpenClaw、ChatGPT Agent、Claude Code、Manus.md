---
title: AI Agent Systems 对比：OpenClaw、ChatGPT Agent、Claude Code、Manus
type: topic
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/comparison
created: 2026-03-22
updated: 2026-03-22
---

# AI Agent Systems 对比：OpenClaw、ChatGPT Agent、Claude Code、Manus

## 这页解决什么问题

当我们说 “AI Agent” 时，很多不同东西都会被混在一起：

- 通用 assistant 的 agent mode
- coding agent
- 自托管 runtime
- 自主执行型 task agent

这页就是把这 4 个典型对象拆开：

- [[OpenClaw]]
- [[ChatGPT Agent]]
- [[Claude Code]]
- [[Manus]]

## 一句话定位

- `OpenClaw`：self-hosted、multi-channel 的 personal agent runtime
- `ChatGPT Agent`：cloud-hosted 的通用 assistant agent mode
- `Claude Code`：developer-facing coding agent
- `Manus`：更强调自主完成任务与结果交付的 general agent

## 先看最重要的比较表

| 维度 | OpenClaw | ChatGPT Agent | Claude Code | Manus |
|---|---|---|---|---|
| 核心形态 | runtime / gateway | ChatGPT 内的 agent mode | coding agent | autonomous task agent |
| 部署形态 | self-hosted / local-first | cloud-hosted | 本地开发工作流 | 云端产品 + sandbox |
| 主入口 | messaging / app / CLI | ChatGPT | terminal / repo | task-oriented product UI |
| 核心卖点 | 长期在线、跨渠道、可塑性强 | 通用产品体验 + 可执行能力 | 代码理解、修改、执行 | 自主完成任务并交付结果 |
| 强项 | session / memory / hooks / heartbeat | 通用入口、产品一体化 | 开发者生产力 | autonomy / result delivery |
| 最适合学习什么 | runtime architecture | agent 产品化 | coding workflow | autonomous execution |

## OpenClaw 代表什么

OpenClaw 最值得学的，不是“它是不是最强”，而是它把 agent 暴露成了一个可以被拆解的系统：

- gateway
- sessions
- markdown memory
- hooks / heartbeat / cron
- multi-channel presence

所以它特别适合学习：

- runtime
- session design
- long-running agent operations

## ChatGPT Agent 代表什么

ChatGPT Agent 更适合用来理解：

- 主流通用 assistant 如何把 agent 能力并入主产品
- agent 能力如何在强治理的云端产品里被交付
- assistant 和 agent 的边界如何逐步模糊

它强调的是：

- 产品统一入口
- 通用任务执行
- 产品化与治理

## Claude Code 代表什么

Claude Code 很适合拿来理解：

- agent 在高价值垂直场景里如何真正产生生产力
- 为什么 terminal、repo、command feedback 会成为 agent 设计核心

它强调的是：

- developer workflow
- action in terminal
- codebase awareness

## Manus 代表什么

Manus 的叙事更偏：

- 自主完成任务
- 在 sandbox 环境中执行
- 交付完整工作结果

它很适合用来理解：

- autonomous task completion
- sandbox agent execution
- result-oriented product packaging

## 如果用一句更“拓扑化”的方式理解

- `ChatGPT Agent`：通用入口型
- `Claude Code`：垂直工作流型
- `Manus`：自主执行型
- `OpenClaw`：运行时基础设施型

## 学习建议

如果你想学：

- `assistant 产品化`：先看 [[ChatGPT Agent]]
- `coding agent`：先看 [[Claude Code]]
- `runtime 设计`：先看 [[OpenClaw]]
- `autonomous task operator`：先看 [[Manus]]

## 推荐阅读顺序

1. [[ChatGPT Agent]]
2. [[Claude Code]]
3. [[Manus]]
4. [[OpenClaw]]
5. [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]

## 关联地图

- [[../07-Maps/AI Agent Systems Map|AI Agent Systems Map]]
- [[../07-Maps/AI Agent Product Positioning Map|AI Agent Product Positioning Map]]
- [[../../AI-Engineering/08-Maps/Agent Runtime Engineering Map|Agent Runtime Engineering Map]]

## 官方资料

- OpenClaw: [Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- OpenAI: [ChatGPT agent](https://help.openai.com/en/articles/11752874-chatgpt-agent)
- Anthropic: [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- Manus: [Welcome - Manus Documentation](https://manus.im/docs)
