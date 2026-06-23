---
title: Kimi
type: system
status: learning
tags:
  - ai/product
  - ai/system
  - organization/moonshot-ai
  - ai/agent
organization: "[[Moonshot AI]]"
modality:
  - chat
family: Kimi
related_papers:
  - "[[Kimi Technical Report]]"
related_people:
  - "[[杨植麟]]"
created: 2026-03-01
updated: 2026-03-28
---

# Kimi

## 简介

`Kimi` 是 [[Moonshot AI]] 最有代表性的产品节点，也是 long-context 产品路线的重要观察对象。

但如果只把它看成“长上下文产品”，已经不够了。最近更值得关注的是：Moonshot 正在把 `Kimi Open Platform` 往更 agent-friendly 的方向推进。

## 为什么重要

- 它让 long context 第一次以很直观的产品形态被大量讨论
- 它是中国 AI assistant 产品路线中的代表样本之一
- 近半年开始出现更明显的 `CLI + Playground + MCP` 扩展信号

## 现在更值得注意的 4 个点

### 1. Kimi Playground 正式上线

Moonshot 官方 changelog 记录：`2025-07-17` 官方发布了 `Kimi Playground`。

### 2. Playground 已支持 third-party MCP server

同一条官方 changelog 还记录：`Kimi Playground` 支持 third-party MCP server configurations。

这很关键，因为它说明 Moonshot 不是只做封闭聊天产品，而是开始把自己接到更广的工具协议生态。

### 3. Open Platform 已记录 CLI support

官方 changelog 记录：`2025-10-27` 文档更新了 `kimi CLI support`。

这说明 Moonshot 也在主动进入：

- coding / terminal workflow
- agent toolchain
- developer-first interaction surface

### 4. Moonshot 在主动解读 OpenClaw

Moonshot 官方博客还发布了 `What is OpenClaw` 一类文章，讨论如何把 `OpenClaw` 与 `Kimi K2.5` 一起运行。

这虽然不是 Moonshot 自己的 runtime，但说明它在积极布局 agent ecosystem，而不是只盯自己的网页入口。

## 你可以把 Kimi 当成什么来理解

现在更准确的理解是：

- `Kimi` 仍然是 Moonshot 的核心 assistant / open platform 品牌
- `long context` 仍然是它的基础差异点
- 但产品层已经在往 `CLI + Playground + MCP-friendly platform` 发展

## 它和 OpenClaw 的关系怎么理解

- `OpenClaw` 是 self-hosted runtime / gateway
- `Kimi` 更像 model + platform provider

所以两者不是直接替代关系，而更像：

- `Kimi` 提供模型与平台能力
- `OpenClaw` 提供 runtime、skills、plugins、apps、automation

## 它和 Codex / Claude Code / Gemini CLI 的差异

- `Codex`、`Claude Code`、`Gemini CLI` 更偏开发者主入口
- `Kimi` 目前更偏 open platform / playground / model provider，再逐步长出 CLI 和 MCP 能力

## 什么时候优先研究它

- 你想看中国模型厂商如何把 assistant 变成 open platform
- 你关心 `long context + MCP + CLI` 这一组合
- 你想跟踪 Moonshot 如何接入更广的 agent ecosystem

## 推荐继续往下读

- [[Moonshot AI]]
- [[OpenClaw]]
- [[Gemini CLI]]
- [[Grok Agent Tools API]]
- [[Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
- [[../06-Topics/Long Context|Long Context]]
- [[../06-Topics/AI Assistant|AI Assistant]]

## 相关

- [[Moonshot AI]]
- [[Long Context]]
- [[AI Assistant]]
- [[China AI Ecosystem]]
- [[OpenClaw]]
- [[Codex]]
- [[Claude Code]]
- [[Gemini CLI]]

## 资料

- [Kimi Open Platform release log](https://platform.moonshot.ai/blog/posts/changelog)
- [What is OpenClaw | Moonshot](https://platform.moonshot.ai/blog/posts/what-is-openclaw)
- [New Kimi K2 Models & Updated Pricing](https://platform.moonshot.ai/blog/posts/Kimi_API_Newsletter)
