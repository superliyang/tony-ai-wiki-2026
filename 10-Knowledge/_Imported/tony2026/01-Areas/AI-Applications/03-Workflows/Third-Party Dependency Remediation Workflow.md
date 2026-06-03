---
title: Third-Party Dependency Remediation Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/procurement
  - ai/third-party-risk
  - ai/dependency-remediation
inputs:
  - supplier concentration findings
  - business criticality and dependency analysis
  - contracts, renewal timing, and mitigation options
  - risk policy and owner matrix
steps:
  - prioritize the dependency finding by criticality and time sensitivity
  - identify practical mitigation paths such as diversification, renegotiation, contingency plans, or approval-based acceptance
  - prepare a remediation packet with owner, timeline, and required decisions
  - route actions to procurement, security, finance, legal, and business stakeholders
  - track remediation progress, exceptions, and residual risk until closure or acceptance
tools:
  - vendor management systems
  - spend and dependency analytics
  - contract and renewal repositories
  - ticketing and action-tracking systems
  - policy repositories
outputs:
  - remediation plan
  - residual risk memo
  - owner tracker
  - dependency review log
evaluation:
  - mitigation completion rate
  - time-to-remediation
  - reduction in concentrated critical dependencies
  - exception aging
risks:
  - remediation actions with no clear owner
  - mitigation plans disconnected from renewal timing
  - risk acceptance without evidence
  - dependency findings that never translate into operational change
related_products:
  - ChatGPT Agent 产品卡
  - OpenClaw 产品卡
created: 2026-03-24
updated: 2026-03-24
---

# Third-Party Dependency Remediation Workflow

## 简介

`Third-Party Dependency Remediation Workflow` 回答的不是“风险怎么发现”，而是“发现以后怎么办”。它适合进入单一供应商依赖、关键系统绑定、续约集中、备援不足和第三方风险升级之后的治理阶段。

## 步骤

1. 根据业务 criticality、到期时间和 risk exposure 给 dependency finding 排优先级
2. 识别 remediation path：双供应商、替代 vendor、续约重谈、额外 control、短期风险接受等
3. 生成 remediation packet，明确 residual risk、owner、timeline 和所需审批
4. 把动作分配给 procurement、security、finance、legal 和业务 owner
5. 持续跟踪 remediation progress，直到风险关闭或被正式接受

## 工具链

- vendor management systems
- spend and dependency analytics
- contract and renewal repositories
- action-tracking, ticketing, and approval systems
- policy and risk repositories

## 评估

- remediation 是否真正完成
- 高风险依赖是否被有效降低
- exception 是否及时关闭或升级
- owner 是否按时完成行动项

## 风险

- 只产出 memo，不真正落 action
- remediation timeline 与 renewal timing 脱节
- 责任 owner 不清晰，导致 dependency 风险悬空
- 组织把“风险已识别”误当成“风险已治理”

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]：适合 remediation packet、owner summary 和 residual risk memo
- [[../02-Products/OpenClaw 产品卡|OpenClaw 产品卡]]：适合长期追踪 remediation state、连接内部系统和持续运行的治理 workflow

## 来源

- ServiceNow: [What is Third-Party Risk Management?](https://www.servicenow.com/products/governance-risk-and-compliance/what-is-third-party-risk-management.html)
- ServiceNow: [Vendor Risk Management](https://www.servicenow.com/au/products/vendor-risk-management.html)

## 相关

- [[Supplier Concentration Risk Workflow]]
- [[Supplier Governance Operating Rhythm]]
- [[../07-Templates/供应商组合治理评审模板|供应商组合治理评审模板]]
- [[../07-Templates/供应商集中度评审模板|供应商集中度评审模板]]
