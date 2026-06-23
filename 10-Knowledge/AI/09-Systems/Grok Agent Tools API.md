---
title: Grok Agent Tools API
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/xai
  - ai/tools
created: 2026-03-28
updated: 2026-03-28
---

# Grok Agent Tools API

## 它是什么

这页讨论的不是 Grok 聊天产品本身，而是 `xAI` 在 API 层不断推出的一组 `agent tools` 能力：

- `web_search`
- `x_search`
- `code_execution`
- `collections_search`
- `files`
- `remote MCP tools`
- `multi-agent` model mode

## 为什么值得学

`xAI` 这条线很能代表一种趋势：

`不是先做桌面 app 或 terminal 产品，而是先把 server-side agent loop 做强。`

也就是说，xAI 的重点更像：

- API-first
- tool-rich
- server-side execution
- OpenAI-compatible surfaces

## 它的关键能力面

### 1. X Search

官方文档说明 `x_search` 允许 Grok 搜索和分析 `X` 的实时社交内容。

这很特别，因为它把一个强实时外部语料源做成了一等工具。

### 2. Web Search

官方文档明确把 `web_search` 做成工具，而不是单独产品按钮。

### 3. Code Execution

官方文档把 `code_execution` 描述成实时 Python 执行能力，可用于计算、分析、验证和 debugging。

### 4. Collections Search 与 Files

`collections_search` 和 `files` 把 document / knowledge-base / uploaded files 接回 agent loop。

### 5. Remote MCP Tools

官方文档说明 remote MCP server URL 可以直接接到 xAI 的 SDK / compatible Responses API 上。

### 6. Multi-agent model mode

xAI 还直接提供了 multi-agent model mode，文档说明多个 agents 可以并行讨论，并且各自独立调用工具。

## 为什么它和 Harness Engineering 相关

xAI 的启发不在于“它是不是最好的 agent 产品”，而在于它证明了：

- 一套 API 也可以直接暴露 `agent loop`
- 工具面可以高度产品化
- `tool-rich API` 本身就能成为竞争力

所以从 harness 视角看，xAI 更像：

- `server-side agent harness`
- `tool orchestration surface`
- `multi-agent API surface`

## 它和 Codex / Claude Code / Gemini CLI 的差异

- `Codex`、`Claude Code`、`Gemini CLI` 更偏开发者工作入口
- `Grok Agent Tools API` 更偏底层 API 能力面

所以它更适合：

- 平台方
- framework builder
- tool orchestration product

而不是单纯作为最终用户入口。

## 什么时候优先研究它

- 你在搭自己的 agent platform
- 你关心 built-in tools 的 server-side orchestration
- 你想理解 `OpenAI-compatible` tool surface 正在往哪里收敛

## 推荐继续往下读

- [[Agent 能力扩展对比：OpenClaw、Codex、Claude Code、Gemini CLI、Grok、Kimi]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]

## 相关

- [[Codex]]
- [[Claude Code]]
- [[Gemini CLI]]
- [[Kimi]]
- [[OpenClaw]]

## 资料

- [Grok 4.1 Fast and Agent Tools API](https://x.ai/news/grok-4-1-fast/)
- [X Search | xAI](https://docs.x.ai/developers/tools/x-search)
- [Code Execution | xAI](https://docs.x.ai/developers/tools/code-execution)
- [Collections Search | xAI](https://docs.x.ai/developers/tools/collections-search)
- [Files | xAI](https://docs.x.ai/developers/files)
- [Remote MCP Tools | xAI](https://docs.x.ai/docs/guides/tools/remote-mcp-tools)
- [Docs MCP | xAI](https://docs.x.ai/developers/docs-mcp)
- [Multi Agent | xAI](https://docs.x.ai/developers/model-capabilities/text/multi-agent)
- [Use with Code Editors | xAI](https://docs.x.ai/docs/guides/use-with-code-editors)
