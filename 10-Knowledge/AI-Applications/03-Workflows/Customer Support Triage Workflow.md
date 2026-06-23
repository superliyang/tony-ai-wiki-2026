---
title: Customer Support Triage Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/support
inputs:
  - customer message
  - account or order context
  - knowledge base articles
steps:
  - classify request
  - retrieve policy context
  - propose answer or next action
  - escalate if risky or unclear
  - log handoff
tools:
  - CRM
  - ticketing system
  - order systems
  - knowledge base
outputs:
  - answer draft
  - ticket routing
  - escalation summary
evaluation:
  - resolution rate
  - escalation quality
  - safety incidents
risks:
  - wrong policy explanation
  - incorrect action execution
  - low customer trust
related_products:
  - ChatGPT Agent 产品卡
created: 2026-03-22
updated: 2026-03-22
---

# Customer Support Triage Workflow

## 简介

客服 triage workflow 适合 agent 的原因是：它高频、边界相对清晰、系统可接，而且很容易衡量转人工率、解决率和错误成本。

## 步骤

1. 识别用户意图与问题类型
2. 读取订单、账户和知识库上下文
3. 给出回答草稿、动作建议或路由决策
4. 对高风险问题直接升级人工
5. 留下结构化交接信息

## 工具链

- CRM / ticket system
- order and account systems
- knowledge base
- policy source of truth

## 评估

- 真正解决率，而不是只看回复率
- 转人工率与交接质量
- 错误政策解释和错误动作次数

## 风险

- policy 与 chatbot 口径不一致
- 没有单一事实源
- 没有为高风险场景设置升级条件

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]

## 相关

- [[../01-Industries/Customer Support Agents|Customer Support Agents]]
- [[../05-Topics/Agent Failure Cases and Deployment Pitfalls|Agent Failure Cases and Deployment Pitfalls]]
- [[../04-Case-Studies/Air Canada Chatbot Liability Case|Air Canada Chatbot Liability Case]]
