---
title: AI Security Telemetry、Escalation 与 Incident Response
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
  - ai/incident-response
created: 2026-03-27
updated: 2026-03-27
---

# AI Security Telemetry、Escalation 与 Incident Response

## 为什么这一层值得单独看

没有 telemetry，AI security 只能停留在“设计上应该安全”。

真正的生产系统必须回答：

- 我们怎么知道 injection 正在变多
- 什么叫安全事件
- 谁会被通知
- 出问题时怎么降级和回滚

## 应该观测什么

### 1. 输入风险信号

- jailbreak / injection 命中率
- 高风险来源域名或文档命中率
- retrieval 内容里的 instruction-like patterns

### 2. 动作风险信号

- 被 policy 拦截的 tool call
- 被人工审批拒绝的高风险动作
- 频繁触发 read-only fallback 的 agent

### 3. 状态风险信号

- memory 写入失败与 redaction 命中
- 敏感字段进入长期记忆的尝试
- 异常 state mutation

### 4. 供应链风险信号

- artifact 扫描失败
- 未签名或 provenance 不完整的模型 / adapter / image
- 关键依赖漂移

## 一套最小 escalation 规则

- 单次低风险命中：记录与观测
- 连续命中异常升高：升级到 on-call / platform owner
- 发生越权动作或数据泄露迹象：进入 security incident
- 发现 release gate 缺口：阻断发布或切回安全模式

## Incident Response 最小动作

1. 暂停高风险工具或切只读
2. 保全 trace、prompt、tool call、approval log
3. 明确影响范围：用户、工具、数据、memory、artifact
4. 快速修补 rule / policy / prompt / gateway
5. 补进 regression suite，避免同类问题再次上线

## 关联

- [[Agent 上线门槛与安全 Release Gates]]
- [[Prompt Injection Defense 与 Tool Safety]]
- [[Guardrails、Policy Enforcement 与 Security Gateways]]
- [[AI 安全案例与失败模式]]
- [[../08-Maps/Enterprise AI Security Operating Model Map|Enterprise AI Security Operating Model Map]]
