---
title: Agent Platform V1 需求文档
type: project-doc
status: draft
project: Agent Platform
created: 2026-03-25
updated: 2026-03-25
---

# Agent Platform V1 需求文档

## 1. 背景

我们已经完成了 `Agent` 体系的知识结构化：从 `prompt`、`context`、`MCP`、`CLI`、`browser / computer use` 到 `harness`、`eval`、`memory`、`security`、`A2A`。下一步不该直接在知识库里写代码，而应该沉淀一套可交付给 AI 编程助手落地的项目方案。

## 2. 项目目标

构建一个面向内部使用的 `Agent 平台 V1`，具备以下能力：

- 支持 `Feishu / Lark` 作为主要交互入口
- 支持 `Web / Internal API` 作为后续扩展入口
- 支持单 agent + approval + long-running thread
- 支持 `MCP`、内部 SDK / HTTP tools、受控 `CLI`
- 支持 `Langfuse` tracing / prompt / eval 基础接入
- 为后续 `ADK adapter` 和 `A2A` 做架构预留

## 3. 目标用户

- 平台团队 / AI Infra 团队
- 需要搭内部 agent 的业务开发团队
- 需要通过 Feishu 调用 agent 的内部员工
- 后续通过 Cursor / Codex 落地实现的工程团队

## 4. 核心场景

### 4.1 Feishu 研究助手

- 用户在 Feishu 里给 agent 发问题
- agent 能调内部检索、web search、MCP tools
- 结果支持同步回复和异步回推

### 4.2 审批门槛下的操作型 agent

- agent 可以提议执行动作
- 高风险动作必须审批
- 审批通过后继续原 thread

### 4.3 长任务执行

- 任务可能跨多轮、多工具、多审批点
- 任务断开或重试后，可以从 checkpoint 恢复

### 4.4 观测与回归

- 所有关键链路可 trace
- prompt / tool / model / user turn 可回放
- 基础回归集可用于版本升级验证

## 5. 非目标

V1 不追求：

- 多 agent 自动协作大编排
- 全自动 browser / computer use 生产化
- 全面支持所有渠道
- 自带完整 BI / admin console
- 成为统一企业 agent marketplace

## 6. 功能需求

### 6.1 Channel

- Feishu / Lark app bot 接入
- 接收用户消息事件
- 发送消息、卡片、异步通知
- 将 channel 事件归一化成平台内部 `TurnRequest`

### 6.2 Session / Thread

- 每个用户会话映射到 thread
- thread 可关联 tenant、user、channel、task
- thread 支持中断恢复

### 6.3 Runtime

- 基于 `LangGraph` 执行 graph
- 支持 interrupt / resume
- 支持 long-running state

### 6.4 Tools

- 支持 `MCP servers`
- 支持 internal SDK / HTTP tools
- 支持 safe CLI executor
- 支持 tool policy / timeout / budget

### 6.5 Approval

- 高风险工具调用前可触发审批
- 审批结果绑定到原 thread
- 拒绝、超时、重试可记录

### 6.6 Observability

- 接入 `Langfuse`
- 支持 trace、prompt version、tool span
- 支持基础 score / regression run

### 6.7 Security

- tool allowlist
- CLI sandbox
- secret isolation
- audit trail

## 7. 成功标准

### 7.1 MVP 成功标准

- 单个 Feishu agent 可稳定对话
- 至少跑通 3 类工具面：`MCP`、HTTP tool、safe CLI
- 至少支持 1 个审批节点
- 所有请求都有 trace
- 一套基础 regression suite 可以跑通

### 7.2 工程成功标准

- `LangGraph` 不与业务逻辑深耦合
- `ToolSpec` 与 channel model 统一
- `Langfuse` 从第一天接入，而不是后补
- 架构上可容纳 `ADK adapter`

## 8. 风险

- 把 Feishu webhook 当成完整 channel runtime，会导致后续 thread / approval 混乱
- 过早双主运行时，会让平台 contract 不稳定
- 没有统一 SDK contract，会导致 graph、tool、channel 三边耦合失控
- 没有 trace / eval，会让平台很快不可调试

## 9. 版本边界

### V1.1

- Feishu channel
- LangGraph runtime
- Langfuse tracing
- 基础 tools
- 基础 approval

### V1.2

- regression suite
- artifact store
- prompt versioning
- richer tool gateway

### V1.3

- ADK adapter
- remote workers
- A2A experiments
