---
title: Personal Assistant Agent Workflow
type: workflow
status: learning
tags:
  - ai/workflow
  - ai/personal-assistant
inputs:
  - user intent
  - personal context
  - calendar or note context
steps:
  - interpret request
  - gather context
  - propose or perform bounded actions
  - summarize and remind
tools:
  - calendar
  - notes
  - tasks
  - browser
outputs:
  - summary
  - task updates
  - reminders
evaluation:
  - reduced cognitive load
  - completion rate
  - user trust
risks:
  - privacy leakage
  - over-automation
  - context drift
related_products:
  - OpenClaw 产品卡
  - ChatGPT Agent 产品卡
created: 2026-03-22
updated: 2026-03-22
---

# Personal Assistant Agent Workflow

## 简介

个人助理型 workflow 关注的是：agent 能不能成为一个长期陪伴式助手，而不只是一次性问答界面。

## 步骤

1. 接收用户请求或周期性触发
2. 获取个人上下文、日程或任务信息
3. 生成建议、提醒或下一步动作
4. 在边界内执行轻量操作或等待确认
5. 把结果沉淀到记忆或任务系统里

## 工具链

- notes
- calendar
- reminders / tasks
- browser
- memory / workspace

## 评估

- 是否降低了用户的组织负担
- 是否真的提高了任务完成率
- 用户是否愿意持续交给它更多事情

## 风险

- 个人数据和隐私边界
- 记忆不准导致长期行为失真
- 看起来很聪明，但长期信任不足

## 最适合的产品

- [[../02-Products/OpenClaw 产品卡|OpenClaw 产品卡]]
- [[../02-Products/ChatGPT Agent 产品卡|ChatGPT Agent 产品卡]]

## 相关

- [[../05-Topics/Personal Assistant Agents|Personal Assistant Agents]]
- [[../../AI-Engineering/07-Topics/Session and Memory Design|Session and Memory Design]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]
