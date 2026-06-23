---
title: Renewal and Obligation Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/procurement
  - ai/renewals
  - ai/obligations
inputs:
  - active contracts and renewal dates
  - notice windows and renewal types
  - obligation library and compliance requirements
  - supplier performance and business usage data
steps:
  - identify contracts entering the pre-renewal review window
  - extract renewal clauses, notice dates, obligations, and performance commitments
  - combine contract facts with spend, usage, and supplier-performance context
  - generate a renewal packet with options, risks, and required actions
  - route to procurement, finance, legal, or business owner and record the decision
tools:
  - contract repositories and CLM systems
  - obligation tracking tools
  - spend and supplier performance data sources
  - workflow and approval systems
outputs:
  - renewal review packet
  - obligation summary
  - notice calendar
  - decision log
evaluation:
  - missed-renewal reduction
  - review lead time
  - obligation tracking completeness
  - stakeholder decision speed
risks:
  - missed notice windows
  - incomplete obligation extraction
  - renewal decisions made without usage or supplier context
  - weak evidence trail for commercial decisions
related_products:
  - ChatGPT Agent 产品卡
  - OpenClaw 产品卡
created: 2026-03-24
updated: 2026-03-24
---

# Renewal and Obligation Agent Workflow

## 简介

`Renewal and Obligation Agent Workflow` 适合进入 vendor renewal、合同到期提醒、obligation review、续约前商业评估和 notice management 这类流程。它的重点不是替组织自动续约，而是把“什么时候该看、该看什么、该找谁拍板”结构化出来。

## 步骤

1. 找出进入 pre-renewal window 的合同或供应商关系
2. 提取 renewal type、notice deadline、price adjustment、termination、obligation 和 SLA 相关信息
3. 结合 spend、usage、supplier performance 和业务依赖上下文
4. 生成 renewal packet，包括续约建议、obligation gap、notice action 和风险提示
5. 把决策交给 procurement、finance、legal 或业务 owner，并保留最终 disposition

## 工具链

- CLM and contract repositories
- obligation tracking systems
- spend, usage, and supplier performance data sources
- workflow, ticketing, and approval systems

## 评估

- 是否更少错过 renewal 或 notice 窗口
- pre-renewal review 是否更早开始
- obligation summary 是否更完整、可复核
- stakeholder 是否更快完成续约决策

## 风险

- 只看合同文本，不看实际 usage 和 supplier performance
- obligation 抽取不完整，导致后续审查失真
- 续约建议看起来完整，但证据链不足
- 自动化提醒太多，反而让 owner 忽略真正高风险 renewals

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]：适合生成 renewal packet、obligation summary 和 decision memo
- [[../02-Products/OpenClaw 产品卡|OpenClaw 产品卡]]：适合进入更长期的 internal renewal runtime，承接 reminder、workflow orchestration 和私有系统接入

## 来源

- Icertis: [ObligationsAI](https://www.icertis.com/products/applications/supplier-relationship-management/)
- Icertis: [The importance of AI in contract management](https://www.icertis.com/contracting-basics/the-importance-of-artificial-ai-in-contract-management/)
- Ironclad: [Use Automated Emails to Streamline Your Renewals Process](https://support.ironcladapp.com/hc/en-us/articles/34100183090455-Recipe-Use-Automated-Emails-to-Streamline-Your-Renewals-Process)

## 相关

- [[Procurement Agent Workflow]]
- [[Vendor Onboarding Agent Workflow]]
- [[Supplier Concentration Risk Workflow]]
- [[../07-Templates/续约评审模板|续约评审模板]]
