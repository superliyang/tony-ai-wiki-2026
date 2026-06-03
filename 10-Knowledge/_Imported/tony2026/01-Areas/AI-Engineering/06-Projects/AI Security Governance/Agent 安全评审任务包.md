---
title: Agent 安全评审任务包
type: project-doc
status: learning
created: 2026-03-27
updated: 2026-03-27
---

# Agent 安全评审任务包

## 目标

把一个待上线 agent 的安全评审拆成可以执行的任务包。

## 任务包结构

### 1. threat modeling

- 明确输入面、tool 面、state 面、artifact 面
- 列出高风险动作和敏感数据

### 2. control review

- 填写 [[../../09-Templates/AI 安全评审模板|AI 安全评审模板]]
- 检查是否有 gateway / guardrails / approval / kill switch

### 3. red-team

- 运行 [[../../09-Templates/Prompt Injection 红队模板|Prompt Injection 红队模板]]
- 补齐 adversarial prompts 与 regression pack

### 4. release decision

- 使用 [[../../09-Templates/Agent 上线门槛模板|Agent 上线门槛模板]]
- 明确 ship / no-ship / limited rollout

### 5. telemetry and incident prep

- 定义 alerts、escalation owner、rollback 条件
- 确保 trace 与审批日志可回放

## 最终交付

- 一份安全评审结论
- 一份例外清单
- 一份 rollout 边界说明
- 一份 incident response 入口说明

## 关联

- [[../../07-Topics/AI Security Telemetry、Escalation 与 Incident Response|AI Security Telemetry、Escalation 与 Incident Response]]
- [[../../07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
