---
title: Air Canada Chatbot Liability Case
type: case
status: learning
tags:
  - ai/case-study
  - ai/failure
industry: customer-support
problem: chatbot gave policy guidance that conflicted with official company policy
solution: none-successful; the important lesson is governance failure
stack:
  - website chatbot
results:
  - company held liable for misinformation
lessons:
  - chatbot outputs are company outputs
  - policy sources and approval boundaries matter
related_topics:
  - Customer Support Agents
  - Agent Failure Cases and Deployment Pitfalls
created: 2026-03-22
updated: 2026-04-03
---

# Air Canada Chatbot Liability Case

## 背景

Air Canada 的网站 chatbot 向用户错误说明了丧亲票价政策，导致用户根据错误信息采取行动，随后公司试图主张 chatbot 应与正式政策区分开来。

## 为什么这个案例重要

这不是一个“模型回答有点奇怪”的小问题，而是一个非常典型的 agent / chatbot 治理案例：

- 输出内容和正式政策不一致
- 用户将 chatbot 视为公司官方接口
- 公司无法通过“那只是机器人说的”来切断责任

## 对我们真正有用的教训

- chatbot 输出在法律和运营上都可能被视为公司输出
- 如果政策、退款、赔付、风控、合同条款来自多个不一致知识源，系统迟早出问题
- 在高风险场景里，必须建立单一事实源、权限边界、升级规则和显式审查点

## rollout packet

### pilot

- 这类场景不适合在没有单一事实源和升级机制时直接大规模试点

### gate

- 高风险政策回答必须有 policy parity test、权限边界和人工升级路径

### review

- 不能只看 chatbot 是否流畅，必须回看它是否与正式政策持续一致

### scale

- 如果单一事实源、审查点和责任边界没立住，就不应该谈规模化

## 这类失败通常暴露什么

- knowledge source 没有统一
- 没有把高风险政策回答限制为只读或只引用官方文档
- 没有做政策级回归测试
- 没有清楚定义“机器人可说什么、不可说什么”

## 迁移启发

- 一旦 agent 进入客服、法律、保险、金融、支付、医疗这些高风险场景，正确性和治理优先级会高于流畅度
- 需要把 policy-as-data、human escalation、policy parity test 视为产品能力，而不是上线前补丁

## 来源

- 法律解读：[BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)
- 新闻报道：[Air Canada ordered to pay customer who was misled by airline’s chatbot](https://www.theguardian.com/world/2024/feb/16/air-canada-chatbot-lawsuit)

## 相关

- [[../01-Industries/Customer Support Agents|Customer Support Agents]]
- [[../05-Topics/Agent Failure Cases and Deployment Pitfalls|Agent Failure Cases and Deployment Pitfalls]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
- [[../../AI Rollout Operating Packet：试点、门禁、复盘与规模化|AI Rollout Operating Packet：试点、门禁、复盘与规模化]]
