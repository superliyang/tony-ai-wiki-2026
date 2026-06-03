---
title: NVIDIA NeMo Guardrails
type: system
status: learning
tags:
  - ai/system
  - ai/security
  - ai/guardrails
created: 2026-03-26
updated: 2026-03-26
---

# NVIDIA NeMo Guardrails

## 它是什么

`NVIDIA NeMo Guardrails` 是一个围绕 LLM / agent 安全控制、内容约束和对话规则的 guardrails 系统。

## 为什么它值得看

因为它代表了一类典型安全控制层：

- 不直接替代模型
- 也不替代 runtime
- 而是在模型与应用之间增加安全控制逻辑

## 它最值得抓住的点

- 对话与内容规则
- topic / jailbreak detection
- tracing 与可观测性
- 与 agent / workflow 系统的组合方式

## 它更适合放在哪一层

- guardrails layer
- policy enforcement layer
- security gateway layer

而不是把它误解成完整平台或完整安全体系本身。

## 关联

- [[../06-Topics/AI Security|AI Security]]
- [[../06-Topics/Prompt Injection 与 Jailbreaks|Prompt Injection 与 Jailbreaks]]
- [[../../AI-Engineering/07-Topics/Guardrails、Policy Enforcement 与 Security Gateways|Guardrails、Policy Enforcement 与 Security Gateways]]
- [[../../AI-Engineering/07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]

## 资料

- [NVIDIA NeMo Guardrails Docs](https://docs.nvidia.com/nemo/guardrails/latest/index.html)
- [NeMo Guardrails Tracing](https://docs.nvidia.com/nemo/guardrails/latest/user-guides/tracing/index.html)
- [NeMo Microservices Guardrails](https://docs.nvidia.com/nemo/microservices/latest/guardrails/index.html)
