---
title: Supplier Risk Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/procurement
  - ai/supplier-risk
inputs:
  - supplier profile and onboarding data
  - contract metadata and renewal timing
  - third-party risk signals
  - internal policy and risk thresholds
steps:
  - gather supplier profile, scope, and business dependency context
  - collect structured and unstructured risk signals from internal and external sources
  - classify risks such as compliance, continuity, security, concentration, and contractual exposure
  - prepare an evidence-backed risk memo with recommended escalation path
  - route high-risk items to procurement, security, legal, or business owner and log disposition
tools:
  - supplier onboarding systems
  - risk and compliance data providers
  - contract repositories
  - policy repositories and approval systems
outputs:
  - supplier risk memo
  - risk flag register
  - escalation packet
  - review log
evaluation:
  - analyst time saved
  - evidence completeness
  - escalation precision
  - review turnaround time
risks:
  - false confidence from weak evidence
  - stale external risk data
  - missing concentration or dependency signals
  - unclear escalation ownership
related_products:
  - ChatGPT Agent 产品卡
  - OpenClaw 产品卡
created: 2026-03-24
updated: 2026-03-24
---

# Supplier Risk Agent Workflow

## 简介

`Supplier Risk Agent Workflow` 不是一个自动打分黑箱，而是一个把 supplier risk review 资料化、证据化、可升级的工作流。它最有价值的地方，是把本来分散在供应商资料、合同、第三方风险源和内部政策里的信息先汇总成一份可被采购和风险团队消费的 memo。

## 步骤

1. 识别 supplier 的业务角色、依赖度、 spend 规模和 renewal 时间点
2. 拉取 onboarding 数据、合同条款、外部风险信号和内部历史问题
3. 对 security、compliance、operational dependency、commercial exposure 等风险做分类
4. 生成 evidence-backed risk memo、risk flags 和建议 escalation path
5. 把高风险供应商升级到 procurement、security、legal 或业务 owner 处理，并保留审计轨迹

## 工具链

- supplier onboarding and vendor master systems
- risk intelligence and compliance data sources
- contract and renewal repositories
- workflow, ticketing, and approval systems

## 评估

- analyst review 时间是否缩短
- risk memo 是否足够可复核
- escalation 是否更精准
- 高风险 supplier 是否更早被识别出来

## 风险

- 引用过期的外部信息
- 只给结论不给证据，导致 reviewer 不信任
- 忽略 concentration risk、关键 dependency 或合同层的责任暴露
- 把需要深判断的风险 review 误当成自动批准流程

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]：适合把 supplier risk 信息汇总成 analyst-ready memo
- [[../02-Products/OpenClaw 产品卡|OpenClaw 产品卡]]：适合内部长期运行、系统编排和更私有的 risk workflow

## 来源

- Zip 产品页：[Supplier Onboarding](https://ziphq.com/products/supplier-onboarding)
- ServiceNow 产品页：[AI Control Tower](https://www.servicenow.com/products/ai-control-tower.html)

## 相关

- [[Vendor Onboarding Agent Workflow]]
- [[Procurement Agent Workflow]]
- [[../07-Templates/高信任供应商评审模板|高信任供应商评审模板]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
