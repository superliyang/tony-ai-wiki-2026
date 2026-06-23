---
title: On-call 与协同升级机制
type: topic
status: learning
tags:
  - finance/payments
  - payments/governance
  - payments/escalation
created: 2026-03-15
updated: 2026-03-15
---

# On-call 与协同升级机制

## 这页解决什么问题

支付异常真正让团队崩溃的，往往不是系统本身，而是“出了事不知道谁拍板、谁沟通、谁补偿、谁复盘”。这页讲的是 on-call、升级 `escalation` 与 `RACI` 机制。

## 一套实用机制

- 明确值班 owner
- 明确 incident commander
- 明确技术、运营、风控、客服、业务各自负责什么
- 明确什么时候升级到管理层、什么时候同步合作方

## 为什么它是支付团队的硬能力

因为支付异常经常同时影响：

- 收入
- 用户体验
- 商户关系
- 资金风险
- 合规风险

## 一个简单的 RACI 视角

- `Responsible`：谁执行动作
- `Accountable`：谁最终拍板
- `Consulted`：谁必须参与判断
- `Informed`：谁需要被同步

## 常见误区

- 只有技术 on-call，没有业务 on-call
- 异常群拉起来了，但没人真正拍板
- 事中沟通混乱，事后责任不清

## 关联

- [[支付异常排查与事故复盘]]
- [[支付异常响应图]]
- [[支付异常处置记录模板]]
- [[支付周会决策清单]]
