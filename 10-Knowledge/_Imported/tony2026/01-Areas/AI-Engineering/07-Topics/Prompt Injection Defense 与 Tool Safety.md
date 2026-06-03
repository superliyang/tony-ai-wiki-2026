---
title: Prompt Injection Defense 与 Tool Safety
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
  - ai/prompt-injection
created: 2026-03-26
updated: 2026-03-26
---

# Prompt Injection Defense 与 Tool Safety

## 这页最关键的前提

外部内容默认不可信。

这包括：

- 用户输入
- 网页内容
- 文档内容
- retrieval 结果
- tool 返回内容

## 为什么 tool safety 是核心

在 agent 系统里，prompt injection 的危险不只是让模型“说错话”，而是：

- 诱导模型错误使用工具
- 把高权限动作伪装成正常动作
- 泄露系统 prompt 或敏感上下文

## 防御层次

### 1. 最小权限

- 工具按能力拆分
- 高风险动作默认禁用或审批

### 2. 上下文隔离

- 不可信内容和系统策略分层
- 工具输出不直接等同于可信指令

### 3. 运行时检查

- 对高风险 tool call 做 policy check
- 对输出做内容与动作双重检查

### 4. 审批与审计

- 敏感操作必须可中断
- 要记录触发了什么内容、什么工具、什么审批

## 关联

- [[Security and Privacy]]
- [[AI Security Threat Modeling]]
- [[Guardrails、Policy Enforcement 与 Security Gateways]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[MCP 与 CLI 模式]]
- [[../08-Maps/AI Security Engineering Map|AI Security Engineering Map]]
