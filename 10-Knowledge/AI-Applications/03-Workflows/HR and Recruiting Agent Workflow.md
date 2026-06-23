---
title: HR and Recruiting Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/hr
inputs:
  - role requirements
  - candidate data or employee request
  - policy and fairness constraints
steps:
  - classify request and workflow stage
  - retrieve approved candidate, policy, or talent data
  - generate scheduling, matching, or support recommendation
  - route high-impact decisions for human review
  - log actions and rationale
tools:
  - ATS or HRIS
  - scheduling systems
  - policy repositories
  - matching and communication tools
outputs:
  - match shortlist
  - scheduling draft
  - employee service response draft
evaluation:
  - recruiter productivity
  - time to schedule or screen
  - candidate experience
  - fairness review outcomes
risks:
  - biased recommendations
  - poor candidate communication
  - weak review boundaries
related_products:
  - ChatGPT Agent 产品卡
  - OpenClaw 产品卡
created: 2026-03-23
updated: 2026-03-23
---

# HR and Recruiting Agent Workflow

## 简介

HR / recruiting workflow 的关键不是把招聘官拿掉，而是把大量协调、筛选、政策解释和内部流动支持做成更快、更一致、更可审查的流程。

## 步骤

1. 判断请求属于招聘筛选、面试协调、人才匹配还是员工服务
2. 读取 ATS、HRIS、政策库和上下文约束
3. 生成 shortlist、调度建议、员工服务答复或内部流动推荐
4. 对高影响判断执行人工复核，特别是候选人推荐和政策敏感场景
5. 记录使用的数据、建议依据和后续动作

## 工具链

- ATS / HRIS
- calendar and scheduling tools
- policy and benefits documentation
- matching and communication workflows

## 评估

- recruiter 是否显著节省时间
- scheduling 和 screening 是否更快更稳定
- candidate experience 是否改善
- 是否能通过 fairness / compliance review

## 风险

- 用脏数据放大偏见
- 候选人沟通语气或信息不一致
- 把本应人工判断的决策自动化过头
- 只看效率，不看公平性与体验

## 最适合的产品

- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]
- [[../02-Products/OpenClaw 产品卡|OpenClaw 产品卡]]

## 代表案例

- [[../04-Case-Studies/micro1 Technical Recruiting Platform|micro1 Technical Recruiting Platform]]

## 相关

- [[../01-Industries/HR and Recruiting Agents|HR and Recruiting Agents]]
- [[../05-Topics/Agent Operating Model and Governance|Agent Operating Model and Governance]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
