---
title: Guardrails、Policy Enforcement 与 Security Gateways
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
  - ai/guardrails
created: 2026-03-26
updated: 2026-03-26
---

# Guardrails、Policy Enforcement 与 Security Gateways

## 为什么 guardrails 不是“加一层过滤器”那么简单

在成熟系统里，guardrails 更像：

- policy enforcement layer
- action gateway
- security boundary

它不只是拦内容，还负责：

- 限制行为
- 限制工具
- 限制敏感上下文暴露
- 把风险事件显式化

## 一个成熟 guardrails 层通常管什么

- input validation
- topic / jailbreak detection
- output moderation
- tool-call policy checks
- escalation / human approval hooks

## 为什么这层容易做错

- 只拦输出，不控动作
- 只控 prompt，不控 tool output
- 只做正则和关键词，不做策略分层

## 关联

- [[Prompt Injection Defense 与 Tool Safety]]
- [[AI Security Evaluation 与 Red Teaming]]
- [[../../AI-Learning/09-Systems/NVIDIA NeMo Guardrails|NVIDIA NeMo Guardrails]]
