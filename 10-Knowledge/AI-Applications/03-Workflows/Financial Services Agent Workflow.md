---
title: Financial Services Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/finance
inputs:
  - advisor or analyst question
  - approved internal knowledge sources
  - compliance boundary and review rules
steps:
  - scope request and user intent
  - retrieve approved internal content
  - synthesize answer or meeting prep artifact
  - attach evidence or source trail
  - route for human review when recommendation risk is high
tools:
  - internal research corpus
  - policy and compliance documents
  - retrieval systems
  - summarization and meeting-prep tools
outputs:
  - advisor prep memo
  - answer draft
  - source-backed summary
evaluation:
  - adoption by advisors or analysts
  - retrieval quality
  - factual consistency
  - compliance incident rate
risks:
  - unsupported recommendations
  - source drift
  - weak review handoff
related_products:
  - ChatGPT Agent 产品卡
  - OpenClaw 产品卡
created: 2026-03-23
updated: 2026-03-23
---

# Financial Services Agent Workflow

## 简介

金融服务 workflow 里，agent 最先创造稳定价值的地方通常不是自动交易或自动决策，而是把内部知识访问、客户会议准备、研究摘要和流程导航做成高可信助手。

## 步骤

1. 接收顾问、研究员或运营人员的问题
2. 限定可访问的数据范围与知识来源
3. 检索内部研究、产品材料、流程文档和历史问答
4. 生成 source-backed summary、meeting prep memo 或 answer draft
5. 对靠近建议、推荐或高风险沟通的输出执行人工审核

## 工具链

- internal research corpus
- advisor knowledge systems
- compliance and policy repositories
- retrieval, summarization, and multilingual support tools

## 评估

- 顾问或分析师是否真的采用
- 检索与摘要质量是否稳定
- 是否显著缩短信息获取和准备时间
- 是否把合规风险维持在可接受范围内

## 风险

- 生成看起来流畅但没有依据的建议
- 引用或知识源不一致
- 没有把评测做成上线前置和上线后持续机制
- 高风险输出缺少显式 handoff

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]
- [[../02-Products/OpenClaw 产品卡|OpenClaw 产品卡]]

## 代表案例

- [[../04-Case-Studies/Morgan Stanley Wealth Management Assistant|Morgan Stanley Wealth Management Assistant]]

## 相关

- [[../01-Industries/Financial Services Agents|Financial Services Agents]]
- [[../05-Topics/Agent ROI and Value Capture|Agent ROI and Value Capture]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
