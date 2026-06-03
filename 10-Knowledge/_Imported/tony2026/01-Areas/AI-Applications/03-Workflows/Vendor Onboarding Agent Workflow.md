---
title: Vendor Onboarding Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/procurement
  - ai/vendor-onboarding
inputs:
  - supplier request and intake form
  - legal entity and tax documents
  - security, compliance, and finance requirements
  - procurement policy and approval rules
steps:
  - intake the supplier request and determine onboarding path
  - collect missing supplier documents and normalize submission data
  - run policy, compliance, and risk checks against required systems
  - prepare an onboarding packet with gaps, flags, and recommendation
  - route to procurement, finance, legal, or security for approval and record final decision
tools:
  - procurement intake systems
  - supplier onboarding portals
  - compliance and risk data sources
  - ERP or vendor master systems
  - approval workflow systems
outputs:
  - onboarding packet
  - missing-document checklist
  - supplier profile draft
  - approval and audit trail
evaluation:
  - onboarding cycle-time reduction
  - document completeness rate
  - reviewer acceptance rate
  - duplicate-supplier reduction
risks:
  - incomplete supplier records
  - policy mismatch across teams
  - weak fraud or sanctions screening
  - missing approval evidence
related_products:
  - ChatGPT Agent 产品卡
  - OpenClaw 产品卡
created: 2026-03-24
updated: 2026-03-24
---

# Vendor Onboarding Agent Workflow

## 简介

`Vendor Onboarding Agent Workflow` 适合进入供应商准入、资料收集、合规检查、vendor master 创建和跨团队审批准备这类流程。它的价值不在于替组织自动批准供应商，而在于把 onboarding 过程中最散、最慢、最容易漏的部分结构化。

## 步骤

1. 接收 supplier request，识别是新供应商、变更供应商还是快速采购例外
2. 从 intake form、采购政策和业务上下文里判断需要哪些材料和审批路径
3. 追收税务、实体、保险、安全、隐私或合规材料，并把数据标准化
4. 调用风险、合规和系统校验工具，生成缺口说明和初步 onboarding packet
5. 把最终 packet 交给 procurement、finance、security、legal 等 owner 审批，并保留可审计记录

## 工具链

- procurement intake and orchestration systems
- supplier onboarding portals
- vendor master / ERP systems
- sanctions, compliance, and security review systems
- approval workflow and ticketing systems

## 评估

- supplier onboarding 是否更快
- 缺失材料追收是否更稳定
- reviewer 是否愿意直接在 agent 生成的 packet 上工作
- vendor master 创建和变更是否更少返工

## 风险

- 把未完整验证的 supplier 当成可上线对象
- 跨团队政策不一致，导致 agent 按错误规则走流程
- 供应商同名、实体信息不全或欺诈风险未被及时标记
- onboarding log 不完整，后续审计无法复原

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]：适合 document-heavy intake、材料追收说明、review packet 起草和 analyst-facing assist
- [[../02-Products/OpenClaw 产品卡|OpenClaw 产品卡]]：适合内部系统接入更深、需要长期 session/memory 和更强 control policy 的供应商准入环境

## 来源

- Zip 产品页：[Supplier Onboarding](https://ziphq.com/products/supplier-onboarding)
- Zip 客户案例：[Anthropic](https://ziphq.com/customers/anthropic)

## 相关

- [[Procurement Agent Workflow]]
- [[Supplier Risk Agent Workflow]]
- [[../04-Case-Studies/Anthropic Procurement Scaling with Zip|Anthropic Procurement Scaling with Zip]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
