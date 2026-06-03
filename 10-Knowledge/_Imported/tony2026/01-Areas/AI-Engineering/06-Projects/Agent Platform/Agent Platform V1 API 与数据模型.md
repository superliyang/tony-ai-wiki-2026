---
title: Agent Platform V1 API 与数据模型
type: project-doc
status: draft
project: Agent Platform
created: 2026-03-25
updated: 2026-03-25
---

# Agent Platform V1 API 与数据模型

## 1. 核心对象

### TurnRequest

```json
{
  "tenant_id": "t_123",
  "channel": "feishu",
  "user_id": "u_123",
  "conversation_id": "c_123",
  "thread_id": "th_123",
  "message_id": "m_123",
  "text": "帮我总结这个文档",
  "attachments": [],
  "metadata": {}
}
```

### TurnResponse

```json
{
  "thread_id": "th_123",
  "status": "completed",
  "content": "这是总结结果",
  "artifacts": [],
  "approval_required": false
}
```

### ToolSpec

```json
{
  "tool_id": "search_internal_docs",
  "transport": "http",
  "risk_level": "low",
  "timeout_ms": 10000,
  "requires_approval": false
}
```

### ApprovalRequest

```json
{
  "approval_id": "ap_123",
  "thread_id": "th_123",
  "tool_id": "deploy_change",
  "reason": "high-risk action",
  "status": "pending"
}
```

## 2. 平台 API

### POST `/v1/turns`

用途：从 channel adapter 或 internal API 提交一个 turn。

### POST `/v1/approvals/{approval_id}/approve`

用途：批准高风险动作。

### POST `/v1/approvals/{approval_id}/reject`

用途：拒绝高风险动作。

### GET `/v1/threads/{thread_id}`

用途：读取 thread 状态与最近 artifact。

### GET `/v1/tasks/{task_id}`

用途：读取长任务状态。

## 3. 数据表建议

### threads

- id
- tenant_id
- channel
- user_id
- conversation_id
- status
- current_state
- created_at
- updated_at

### turns

- id
- thread_id
- role
- content
- input_payload
- output_payload
- created_at

### approvals

- id
- thread_id
- tool_id
- reason
- status
- approver_id
- created_at
- resolved_at

### artifacts

- id
- thread_id
- artifact_type
- storage_uri
- metadata

### tool_calls

- id
- thread_id
- tool_id
- transport
- status
- trace_id
- latency_ms

## 4. 设计原则

- `thread_id` 是平台一等公民
- channel-specific id 不作为唯一事实来源
- 审批和工具调用都必须可 trace
- artifact 走对象存储，不走数据库大字段
