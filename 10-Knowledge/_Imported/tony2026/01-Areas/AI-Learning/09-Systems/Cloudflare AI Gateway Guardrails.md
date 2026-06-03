---
title: Cloudflare AI Gateway Guardrails
type: system
status: learning
tags:
  - ai/system
  - ai/security
  - ai/gateway
created: 2026-03-27
updated: 2026-03-27
---

# Cloudflare AI Gateway Guardrails

## 它是什么

`Cloudflare AI Gateway Guardrails` 代表了一类更偏流量入口与策略编排的 AI 安全网关：

- 在请求进入模型前或返回后做规则判断
- 把模型调用、安全策略、日志和边缘入口绑定在一起
- 更适合多模型、多应用、多租户场景

## 为什么值得看

因为它强调的不是“模型本身多安全”，而是：

- 谁能发起请求
- 请求要经过哪些规则
- 哪些结果要被阻断、改写、审计或降级

## 它最值得抓住的点

- gateway-first 的部署方式
- guardrails 与请求路由、日志、策略的组合
- 适合接在 `LLM gateway / app edge / org policy` 这一层

## 更适合放在哪一层

- request gateway layer
- edge policy layer
- multi-model control layer

## 关联

- [[../06-Topics/AI Security|AI Security]]
- [[../../AI-Engineering/07-Topics/Guardrails、Policy Enforcement 与 Security Gateways|Guardrails、Policy Enforcement 与 Security Gateways]]
- [[../../AI-Engineering/07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
- [[../../AI-Engineering/08-Maps/AI Security 控制点图|AI Security 控制点图]]

## 资料

- [Cloudflare AI Gateway Guardrails](https://developers.cloudflare.com/ai-gateway/features/guardrails/)
