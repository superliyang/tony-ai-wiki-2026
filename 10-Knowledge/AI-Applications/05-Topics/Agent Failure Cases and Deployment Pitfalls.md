---
title: Agent Failure Cases and Deployment Pitfalls
type: topic
status: learning
tags:
  - ai/applications
  - ai/agent
  - ai/failure
created: 2026-03-22
updated: 2026-04-03
---

# Agent Failure Cases and Deployment Pitfalls

## 这个主题是什么

`Agent Failure Cases and Deployment Pitfalls` 关注的不是模型答错一两次，而是 agent 落地后为什么会在业务上失败、组织上失败、治理上失败。

## 为什么重要

- 很多 agent 项目不是技术不可行，而是上线方式错误
- 失败往往不是一个 bug，而是任务边界、知识源、审批机制、指标体系一起出了问题
- 如果只看成功案例，很容易误以为“能力更强的模型”就能自动解决落地问题

如果你想把失败当成可复用的复盘资产，而不是事故集，先看 [[../../AI Failure Packet：任务边界、事实源、审批、回滚与责任|AI Failure Packet：任务边界、事实源、审批、回滚与责任]]。

## 典型失败模式

### 1. 任务边界过宽

- 把高风险、不确定、需要深度判断的任务直接交给 agent
- 没有区分“建议模式”和“执行模式”

### 2. 单一事实源缺失

- policy、pricing、合同、客服口径来自多个来源
- agent 回答与正式规则冲突

### 3. 没有升级与审批机制

- 复杂问题不转人工
- 高风险动作没有 approval gate
- 失败恢复路径不明确

### 4. 只看对话效果，不看业务结果

- 用户觉得“看起来聪明”，但真正解决率低
- 没有跟踪 adoption、ROI、handoff quality 和 error cost

### 5. 评测缺失

- 上线前没有任务级 eval
- 上线后没有 drift 监控
- 没有针对高风险边界做回归测试

## 典型案例

- [[../04-Case-Studies/Air Canada Chatbot Liability Case|Air Canada Chatbot Liability Case]]
- [[../04-Case-Studies/Klarna AI Customer Service Assistant|Klarna AI Customer Service Assistant]]
- [[../04-Case-Studies/OpenAI In-House Data Agent|OpenAI In-House Data Agent]]

## 从失败中提炼出的上线原则

- 先选高频、可验证、可回退的任务
- 把知识源统一到单一事实源
- 默认先做人机协作，再逐步扩大自动执行范围
- 为高风险场景设计 policy tests、approval gates 和 escalation paths
- 衡量解决率、接管率、错误成本，而不是只看回答是否流畅

## failure packet 读法

### 任务边界

- 失败常常从边界没切清开始

### 事实源

- 没有单一事实源时，系统迟早会与正式规则冲突

### 审批与升级

- 高风险动作必须有 gate，复杂问题必须能升级

### 回滚与恢复

- 没有 fallback path 的系统，不适合快速放大

### 责任与后果

- 用户会把 agent 输出当成组织输出，责任不会因为“那只是 AI”而消失

## 相关

- [[Agent Productization]]
- [[Agent Adoption and Change Management]]
- [[Agent ROI and Value Capture]]
- [[../../哪些 AI 失败案例最值得反复复盘|哪些 AI 失败案例最值得反复复盘]]
- [[../../AI Failure Packet：任务边界、事实源、审批、回滚与责任|AI Failure Packet：任务边界、事实源、审批、回滚与责任]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
- [[../../AI-Engineering/07-Topics/Task Success and Failure Recovery|Task Success and Failure Recovery]]
