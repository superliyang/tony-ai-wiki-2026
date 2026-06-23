---
title: Security and Privacy
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
created: 2026-03-13
updated: 2026-03-26
---

# Security and Privacy

## 为什么重要

- AI 系统接入真实数据与业务流程后，安全和隐私问题会立刻变成工程问题
- 很多部署失败并不是模型不够强，而是安全边界没定义清楚
- 到 agent 和 LLMOps 阶段，安全已经不只是内容安全，而是系统边界安全

## 系统视角

安全和隐私在 AI 系统里比传统应用更复杂，因为除了常规应用层风险，还多了：

- prompt 注入
- 检索上下文污染
- 模型泄露敏感训练数据
- agent 误调用高权限工具
- 记忆污染
- 模型 artifact 供应链攻击

## 核心问题

- 训练数据、提示词、上下文和日志如何保护
- 提示注入、数据泄露、模型滥用如何防控
- 工具、memory、artifact 和 deployment 分别由谁保护
- 不同行业的合规要求如何影响架构设计

## 关键维度

- 访问控制与隔离
- 数据脱敏与最小化保留
- 攻击面与提示注入
- supply chain 与 artifact safety
- 合规、审计与事件响应

## 典型风险面

- 训练数据与日志泄露
- 推理上下文包含敏感信息
- 用户 prompt 诱导系统越权访问工具或数据
- 缺少审计链，无法追踪谁调用了什么能力
- 不可信模型或 adapter 被引入生产

## 实践中的核心控制点

- 明确权限边界
- 对上下文和工具输出做最小暴露
- 对高风险动作引入审批与策略检查
- 把 artifact、prompt、dataset 都纳入治理
- 记录关键操作链路
- 把安全要求前置到架构设计，而不是上线后补

## 学习这页时最该记住什么

- AI 安全不只关乎输出内容，也关乎系统边界和数据流
- 很多严重问题来自权限设计，而不是模型“说错话”
- 真正成熟的 AI security 必须覆盖 input、context、tool、state 和 artifact

## 相关主题

- [[AI Security Threat Modeling]]
- [[Prompt Injection Defense 与 Tool Safety]]
- [[Guardrails、Policy Enforcement 与 Security Gateways]]
- [[Model Supply Chain Security]]
- [[AI Security Evaluation 与 Red Teaming]]
- [[Safety Evaluation]]
- [[Model Registry and Deployment]]
