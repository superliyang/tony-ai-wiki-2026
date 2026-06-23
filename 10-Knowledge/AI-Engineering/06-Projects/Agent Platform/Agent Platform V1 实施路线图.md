---
title: Agent Platform V1 实施路线图
type: project-doc
status: draft
project: Agent Platform
created: 2026-03-25
updated: 2026-03-25
---

# Agent Platform V1 实施路线图

## Phase 0：设计冻结

目标：

- 冻结 V1 scope
- 冻结核心对象：`TurnRequest`、`TurnResponse`、`ToolSpec`、`ApprovalRequest`
- 确定 `LangGraph-first + Langfuse-first + ADK-adapter-later`

产出：

- PRD
- 架构设计
- API 与数据模型

## Phase 1：平台骨架

目标：

- 建立 gateway service
- 建立 LangGraph runtime wrapper
- 建立 Postgres thread store
- 接入 Langfuse tracing

验收：

- 能跑通单 channel、单 agent、单 thread

## Phase 2：工具与审批

目标：

- 接入 Tool Gateway
- 支持 3 类 tool：`MCP`、HTTP、safe CLI
- 建立 approval service

验收：

- 至少 1 个高风险动作可审批

## Phase 3：Feishu 生产可用最小版

目标：

- 支持 Feishu app bot
- 支持 async reply
- 支持 thread resume

验收：

- 用户能在 Feishu 里完成完整任务闭环

## Phase 4：质量闭环

目标：

- 建立 prompt versioning
- 建立 regression suite
- 建立 release checklist

验收：

- 新版本可回归
- trace / score 可对比

## Phase 5：ADK adapter 与 A2A 试验

目标：

- 增加 ADK adapter
- 允许 remote worker / sub-agent
- 试验 A2A

验收：

- 不破坏现有主 runtime contract
