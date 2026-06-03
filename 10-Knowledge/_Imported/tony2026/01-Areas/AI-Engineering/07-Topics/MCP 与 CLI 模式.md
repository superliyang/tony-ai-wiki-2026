---
title: MCP 与 CLI 模式
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/mcp
  - ai/cli
created: 2026-03-25
updated: 2026-03-25
---

# MCP 与 CLI 模式

## 先给结论

`MCP vs CLI` 这场争论里，很多人其实把两个不同层次的东西放在一起比了。

- `CLI` 更像直接动作面
- `MCP` 更像协议化接入层

所以它们不是天然互斥，更准确的理解应该是：

- 什么时候直接给 agent 一个 shell / CLI 更合适
- 什么时候把能力封成 MCP server 更合适
- 什么时候两者都不够，还需要更完整的 harness / app server

## CLI 模式本质上是什么

`CLI mode` 的核心是：让 agent 直接在本地或受控环境里执行命令。

它的优势通常是：

- 本地文件系统与工作目录控制更直接
- 适合已有脚本、已有工具链、已有 repo workflow
- 对 coding agent、ops agent 很自然
- 调试和迭代快

它的代价是：

- 动作面往往更宽
- 权限与 blast radius 更大
- 不容易天然形成可复用的团队级协议接口

## MCP 模式本质上是什么

`MCP mode` 的核心是：通过 host / client / server 结构，把工具、资源和提示模板按协议暴露给 AI 应用。

它的优势通常是：

- 接口边界更清晰
- 更容易复用给多个 host 或多个 agent
- 本地能力和远程服务都能统一接入
- 更适合团队沉淀可共享的 integration layer

它的代价是：

- 本地强动作场景里，可能没有 CLI 直接
- 并不是所有复杂 session / diff / approval 语义都天然适合装进 MCP
- 仍然需要权限、信任和 server 生命周期管理

## 为什么它们经常被误解成二选一

因为在很多团队里，实际问题是：

- “我要不要直接让 agent 跑命令？”
- “还是我应该先把内部系统封成 MCP server？”

表面在争协议，实际上在争：

- 工具边界要多窄
- 团队复用性要多高
- 本地自治还是平台化治理
- 速度优先还是标准化优先

## 一个更清晰的判断框架

### 更偏向 CLI 的场景

- 单机、本地 repo、开发者个人工作流
- 已有脚本与命令行工具很多
- 任务高度依赖工作目录、进程、文件系统
- 目标是先把 agent 跑通，而不是先平台化

### 更偏向 MCP 的场景

- 需要给多个 agent host 复用同一能力
- 需要接远程服务或共享服务
- 希望把工具边界收敛成结构化协议
- 想把企业内部系统接入沉淀成标准层

### 更偏向 Harness / App Server 的场景

- 任务对象不只是“调一个工具”，而是完整任务会话
- 你需要 diff、artifact、approval、logs、review loop
- 你需要更强的任务生命周期、会话控制和可观测性

## 当前争论里最值得抓住的一点

真正的分水岭常常不是 `MCP or CLI`，而是：

- `direct execution surface`
- `protocolized integration surface`
- `full agent task/runtime surface`

这三者分别解决的是不同层的问题。

## 安全与治理的真实差异

### CLI 风险更像什么

- 命令执行面太宽
- 文件系统和进程权限需要额外收紧
- 更依赖 sandbox、approval、allowlist

### MCP 风险更像什么

- server 是不是可信
- server 暴露了哪些工具/资源
- 远程连接与凭证如何治理
- 团队是否会无约束地批准整个 server

## 我更推荐的工程态度

- 不要先选阵营，先看任务面
- 不要把 MCP 当成万能银弹
- 也不要把 CLI 当成“最真实所以一定最好”
- 对复杂 agent 系统，往往会出现混合形态：
  - shell 做本地动作
  - MCP 做共享集成
  - harness / app server 管任务对象与反馈循环

## 推荐继续往下读

- [[Harness Engineering]]
- [[Tool Calling and Action Execution]]
- [[Human-in-the-Loop and Approval Gates]]
- [[../../AI-Learning/06-Topics/MCP（Model Context Protocol）|MCP（Model Context Protocol）]]
- [[../../AI-Learning/06-Topics/上下文工程|上下文工程]]

## 系统案例

- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]

## 相关

- [[Harness Engineering]]
- [[Tool Calling and Action Execution]]
- [[Human-in-the-Loop and Approval Gates]]
- [[Session and Memory Design]]
- [[../08-Maps/Agent Context and Integration Engineering Map|Agent Context and Integration Engineering Map]]
