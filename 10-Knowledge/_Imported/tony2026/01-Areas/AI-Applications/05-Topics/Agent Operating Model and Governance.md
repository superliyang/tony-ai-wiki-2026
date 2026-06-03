---
title: Agent Operating Model and Governance
type: topic
status: learning
tags:
  - ai/applications
  - ai/agent
  - ai/governance
created: 2026-03-23
updated: 2026-03-23
---

# Agent Operating Model and Governance

## 这个主题在讲什么

这一页讲的不是某个 agent 产品，而是组织如何把一组 agent 真的纳入管理体系：谁负责、谁审批、谁评估、谁看 ROI、谁处理异常、谁决定哪些场景能上线。

## 为什么这是应用层核心问题

- 很多 agent 失败，不是模型不够强，而是组织没有 operating model
- 当 agent 从单点工具变成跨团队资产后，就必须有 owner、评估、权限、审计和变更管理
- 没有治理模型，AI 很容易变成一堆零散试点，而不是持续可控的能力

## 一个可用的组织模型

1. `use case owner`
负责业务目标、成功指标和上线边界。

2. `platform / engineering owner`
负责模型接入、权限、工具、日志、可观测性和成本控制。

3. `risk / legal / security`
负责高风险场景审查、数据边界、合规要求与异常升级。

4. `change / enablement owner`
负责培训、采纳、使用规范和反馈循环。

## 关键治理动作

- 建立 agent inventory：知道组织里到底有哪些 agent 在跑
- 定义 risk tiers：不同风险等级对应不同审批和评测要求
- 把 evals、approval gate、audit log 变成标准能力，不是每个团队重新发明
- 明确 fallback 与人工接管机制
- 让 use case prioritization 和 ROI review 成为固定节奏

## 常见失败模式

- 只上线 demo，没有 owner
- 只看 adoption，不看真实业务结果
- 没有把 review、审计、权限做成平台能力
- 把高风险 agent 当成普通自动化工具去推

## 值得参考的案例

- [[../04-Case-Studies/Zapier Internal AI Agent Rollout|Zapier Internal AI Agent Rollout]]
- [[../04-Case-Studies/Section AI Workforce Transformation|Section AI Workforce Transformation]]
- Workday 明确提出 `Agent System of Record`，把 agent 当成组织里的可管理“数字劳动力”对象来治理：[The Next Generation of Workforce Management is Here – Workday Unveils New Agent System of Record](https://newsroom.workday.com/2025-02-11-The-Next-Generation-of-Workforce-Management-is-Here-Workday-Unveils-New-Agent-System-of-Record?trk=public_post_comment-text)

## 相关

- [[Agent Rollout and Change Program]]
- [[Agent Portfolio and Use Case Prioritization]]
- [[../06-Maps/Agent Organizational Rollout Map|Agent Organizational Rollout Map]]
- [[../../AI-Engineering/07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
