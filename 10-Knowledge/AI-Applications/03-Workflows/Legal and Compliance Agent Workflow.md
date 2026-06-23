---
title: Legal and Compliance Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/legal
inputs:
  - legal or compliance question
  - document set or corpus
  - jurisdiction and policy boundary
steps:
  - define task scope, authority boundary, and jurisdiction
  - retrieve supporting documents, policies, regulations, or case law
  - draft comparison, summary, or analysis with source grounding
  - send to lawyer or compliance reviewer for validation
  - preserve citations, rationale, and review handoff
tools:
  - document repositories
  - case-law or policy search tools
  - comparison and summarization tools
  - review and annotation workflows
outputs:
  - contract diff
  - policy summary
  - citation-backed draft
evaluation:
  - review time reduction
  - citation quality
  - unsupported claim rate
  - reviewer acceptance
risks:
  - hallucinated citations
  - jurisdiction mismatch
  - weak source grounding
related_products:
  - ChatGPT Agent 产品卡
  - OpenClaw 产品卡
created: 2026-03-23
updated: 2026-03-23
---

# Legal and Compliance Agent Workflow

## 简介

法律与合规 workflow 最关键的不是“模型能不能说得像律师”，而是它能不能在检索、引用、差异识别和 review handoff 上真正可靠。这里的价值来自 high-trust assistance，而不是无来源的流畅表达。

## 步骤

1. 确认任务边界、适用 jurisdiction 和输出用途
2. 检索合同、法规、判例、政策或内部合规文档
3. 生成 citation-backed draft、差异分析或要点摘要
4. 交由律师或合规负责人审查、修订与确认
5. 保留引用、依据与审查记录，确保后续可追踪

## 工具链

- contract and document repositories
- policy and case-law search systems
- comparison and redlining tools
- review, annotation, and approval workflows

## 评估

- 是否显著减少审查前置工作量
- 引用和来源是否稳定、可追溯
- 无依据结论比例是否可控
- 律师或合规团队是否愿意把它纳入日常流程

## 风险

- 编造案例或错误引用
- 忽略 jurisdiction 差异
- 输出看似有说服力但没有来源支持
- 把 reviewer handoff 做弱，导致责任边界模糊

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]
- [[../02-Products/OpenClaw 产品卡|OpenClaw 产品卡]]

## 代表案例

- [[../04-Case-Studies/Harvey Legal Work Platform|Harvey Legal Work Platform]]

## 相关

- [[../01-Industries/Legal and Compliance Agents|Legal and Compliance Agents]]
- [[../05-Topics/Agent Productization|Agent Productization]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
