---
title: Agent 架构师视角
type: topic
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# Agent 架构师视角

> Agent 的架构核心不是“让模型自主思考”，而是设计可控的任务边界、工具权限、状态流转、人工审批和失败恢复。

## 架构师要回答的问题

- Agent 要完成的是建议、辅助、半自动执行，还是全自动执行？
- Agent 可以看哪些数据、调用哪些工具、做哪些动作？
- 高风险动作如何审批、回滚和审计？
- Agent 失败时是重试、降级、人工接管，还是终止？
- Agent 的状态、记忆和产物如何管理？

## Agent 架构分层

| 层 | 架构关注点 |
|---|---|
| 任务层 | task scope、成功标准、不支持范围 |
| 规划层 | plan、step、state machine、workflow |
| 上下文层 | session、memory、retrieval、artifact |
| 工具层 | tool registry、tool gateway、permission、rate limit |
| 执行层 | action、approval、rollback、idempotency |
| 观测层 | trace、tool call、cost、latency、failure |
| 治理层 | policy、audit、kill switch、incident response |

## 关键设计决策

### Workflow 还是 autonomous agent

- 大多数企业场景优先 workflow + bounded model decision。
- 自主 agent 适合探索、研究、开发辅助，不适合直接执行高风险业务动作。
- 能用确定性流程解决的，不要强行交给模型规划。

### 工具权限怎么设计

- 工具要分 read、suggest、write、execute、external-impact 等等级。
- 高风险工具必须有审批和审计。
- 工具调用要有输入校验、幂等、回滚和速率限制。

### 记忆怎么设计

- session memory、user memory、project memory、global memory 要分层。
- 共享记忆要防 poisoning、越权和隐私泄露。
- 记忆写入应经过规则、评测或人工确认。

### 失败恢复怎么设计

- 模型失败：fallback / retry / smaller scope。
- 工具失败：重试、补偿事务、人工接管。
- 业务失败：回滚、通知、审计、事故复盘。

## 常见失败模式

- Agent 权限过大，一开始就能写生产数据。
- 没有状态机，所有流程靠 prompt 维持。
- 没有 tool call trace，出事后无法复盘。
- 没有人工审批，自动化越过业务责任边界。
- 没有 eval，只看 demo 成功案例。

## 架构师交付物

- Agent task boundary
- Agent workflow / state machine
- Tool permission matrix
- Approval and rollback policy
- Agent eval suite
- Runtime incident runbook

## 关联

- [[../08-Playbooks/AI 架构评审 Playbook|AI 架构评审 Playbook]]
- [[../../AI-Engineering/08-Maps/Agent Runtime Engineering Map|Agent Runtime Engineering Map]]
- [[../../AI-Engineering/08-Maps/Agent 协作、记忆与信任边界图|Agent 协作、记忆与信任边界图]]
- [[../../AI-Engineering/09-Templates/Agent 上线门槛模板|Agent 上线门槛模板]]

