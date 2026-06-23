---
title: Agent Platform V1 Cursor 实现任务包
type: project-doc
status: draft
project: Agent Platform
created: 2026-03-25
updated: 2026-03-25
---

# Agent Platform V1 Cursor 实现任务包

## 用法

这个文档不是需求摘要，而是给 `Cursor / Codex / Claude Code` 这种编程 agent 的执行拆分。

推荐按 phase 拆线程，不要一次让 AI 同时实现所有模块。

## Phase 1：Monorepo 与基础骨架

目标：

- 建立 monorepo
- 建立 `apps/`、`packages/`、`infra/`、`agents/`
- 建立基础 CI

交付：

- 目录骨架
- 基础 README
- dev bootstrap script

## Phase 2：Gateway + SDK Contract

目标：

- 定义 `TurnRequest`、`TurnResponse`、`ToolSpec`
- 实现 gateway API
- 建立 thread lookup contract

交付：

- typed schema
- HTTP endpoints
- request normalization

## Phase 3：LangGraph Runtime Wrapper

目标：

- 实现 graph runner
- 接入 checkpoint store
- 支持 interrupt / resume

交付：

- runtime wrapper
- thread persistence
- resume path

## Phase 4：Tool Gateway

目标：

- 实现 MCP registry
- 实现 internal HTTP tools
- 实现 safe CLI executor

交付：

- unified tool dispatcher
- tool policy hooks
- trace hooks

## Phase 5：Langfuse Integration

目标：

- user turn trace
- model span trace
- tool span trace
- prompt version capture

交付：

- Langfuse middleware / callbacks
- basic score hook

## Phase 6：Approval Service

目标：

- 高风险动作审批
- approval status writeback
- runtime resume after approval

交付：

- approval model
- approval endpoints
- runtime callback integration

## Phase 7：Feishu / Lark Adapter

目标：

- 处理消息事件
- 发送同步 / 异步消息
- 映射 channel -> thread

交付：

- channel adapter
- event normalization
- response sender

## Phase 8：Regression Pack

目标：

- 5-10 条稳定任务回归
- 每次 release 对比结果

交付：

- regression suite
- release checklist

## 给 Cursor 的执行原则

- 每个 phase 只改一个清晰 write scope
- 不要在同一轮同时重构 runtime、tool gateway、channel adapter
- 所有新模块都先写 contract，再写实现
- 先让 trace 可用，再谈优化
- 默认用非破坏式提交节奏
