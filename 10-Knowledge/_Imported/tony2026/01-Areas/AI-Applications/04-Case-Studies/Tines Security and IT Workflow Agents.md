---
title: Tines Security and IT Workflow Agents
type: case
status: learning
tags:
  - ai/case-study
  - ai/it-ops
  - ai/security-ops
industry: enterprise-operations
problem: security and IT teams rely on long, repetitive workflows across many tools and alerts
solution: Tines used Claude to help teams reduce complex multi-step workflows and move faster through security and IT operations
stack:
  - Claude
  - workflow automation platform
results:
  - customers reduced a 120-step workflow to a single step according to Anthropic's official case
  - some multi-day processes were reduced to minutes according to Anthropic's official case
lessons:
  - IT and security ops value comes from reducing workflow friction, not just answering questions
  - bounded automation plus evidence-rich handoff is the right pattern
related_topics:
  - Enterprise Operations Agents
created: 2026-03-23
updated: 2026-03-23
---

# Tines Security and IT Workflow Agents

## 背景

IT 和安全运营里的高成本，不只是分析难，而是太多流程跨很多工具、步骤冗长、上下文切换频繁。

## 做了什么

- Tines 使用 Claude 来帮助安全和 IT 团队构建 workflow automation
- 价值点不是“一个万能聊天机器人”，而是把复杂的多步骤流程压缩成更短、更可审计的执行路径
- 这非常接近我们在 IT / security ops workflow 里需要的模式：triage、enrichment、runbook、handoff

## 结果

- Anthropic 官方案例披露：有客户把 120 步 workflow 缩成 1 步
- Anthropic 官方案例披露：一些原来需要几天的流程被缩短到几分钟

## 为什么值得学

- 它说明 IT / security ops 场景的核心收益是 workflow compression，而不是“模型回答更聪明”
- 这类场景特别适合 bounded automation、tool chaining 和审批门设计
- 也说明 enterprise agent 不一定以终端聊天界面为中心，workflow 平台也可以是核心承载面

## 迁移启发

- 先从 runbook 明确、结果可核验的流程切入
- 把 evidence、action log 和 escalation 设计为默认产物
- 优先缩短最冗长、最重复、最容易出错的多工具流程

## 来源

- 官方案例：[Tines](https://www.anthropic.com/customers/tines)

## 相关

- [[../03-Workflows/IT and Security Operations Agent Workflow|IT and Security Operations Agent Workflow]]
- [[../01-Industries/Enterprise Operations Agents|Enterprise Operations Agents]]
- [[../../AI-Engineering/07-Topics/Task Success and Failure Recovery|Task Success and Failure Recovery]]
