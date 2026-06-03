---
title: Anthropic Procurement Scaling with Zip
type: case
status: learning
tags:
  - ai/case-study
  - ai/procurement
  - ai/vendor-onboarding
industry: enterprise-operations
problem: rapid organizational growth makes procurement intake, supplier onboarding, and approval coordination harder to scale consistently
solution: Anthropic used Zip's intake-to-procure and supplier onboarding capabilities to standardize procurement workflows and create a foundation for more agentic procurement work
stack:
  - Zip intake-to-procure
  - supplier onboarding workflows
  - procurement orchestration
results:
  - Anthropic's customer story emphasizes a more structured procurement operating model and a path from AI consultant patterns toward more agentic procurement support
lessons:
  - procurement AI maturity usually starts with intake and policy structure before autonomous actions
  - supplier onboarding and review packets are critical prerequisites for deeper procurement agents
  - orchestration quality matters as much as model quality in procurement operations
related_topics:
  - Enterprise Operations Agents
  - Operations Agents
created: 2026-03-24
updated: 2026-03-24
---

# Anthropic Procurement Scaling with Zip

## 背景

采购场景很容易被误解成“让模型看合同”，但组织真正先卡住的，往往是 intake 分散、供应商资料不全、审批路径不清楚，以及 procurement 和 business team 之间缺少统一工作流。

## 做了什么

- Zip 的官方客户故事把 Anthropic 描述成一个正在扩大采购运营规模的团队
- 重点不是“单点问答”，而是 `intake-to-procure`、supplier onboarding 和更结构化的审批/编排能力
- Zip 同时强调了从 `AI consultant` 走向更 `agentic procurement` 的演化路径

## 为什么值得学

- 它说明 procurement agent 不应该一开始就追求自动批准，而应该先把 intake、supplier onboarding、policy routing 和 review packet 标准化
- 这也解释了为什么 procurement 深水区通常会拆出 `Vendor Onboarding` 和 `Supplier Risk` 两条 workflow
- 对我们研究 AI 应用层很重要的一点是：agent 往往建立在已有的 process system 上，而不是替代流程本身

## 迁移启发

- 第一阶段先做 intake / onboarding / review preparation
- 第二阶段再把 supplier risk、renewal、obligation 和 policy routing 接进来
- 最后才讨论 approval-gated action 和更长期的 internal runtime

## 来源

- Zip 客户案例：[Anthropic](https://ziphq.com/customers/anthropic)
- Zip 产品页：[Supplier Onboarding](https://ziphq.com/products/supplier-onboarding)

## 相关

- [[../03-Workflows/Procurement Agent Workflow|Procurement Agent Workflow]]
- [[../03-Workflows/Vendor Onboarding Agent Workflow|Vendor Onboarding Agent Workflow]]
- [[../03-Workflows/Supplier Risk Agent Workflow|Supplier Risk Agent Workflow]]
- [[../05-Topics/Assistant-to-Runtime Migration in High-Trust Domains|Assistant-to-Runtime Migration in High-Trust Domains]]
