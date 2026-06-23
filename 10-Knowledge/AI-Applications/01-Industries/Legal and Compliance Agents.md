---
title: Legal and Compliance Agents
type: industry
status: learning
tags:
  - ai/applications
  - ai/agent
  - industry/legal
created: 2026-03-23
updated: 2026-03-24
---

# Legal and Compliance Agents

## 这个行业方向是什么

`Legal and Compliance Agents` 指的是把 agent 用在合同审查、案例检索、法规解释、法律文书草拟、差异对比、政策问答与合规支持上的应用方向。

## 为什么这个方向天然适合 agent

- 法律与合规工作里有大量文本密集型、结构化、来源可追溯的任务
- 很多任务需要跨大量文档做比对、检索、总结与论证
- 如果把检索、引用、草拟和差异检测做对，能显著减少律师或合规团队的低效劳动

## 为什么这个方向风险也很高

- 法律和合规场景不能容忍“似是而非”的输出
- 引用、依据、 jurisdiction 差异、政策边界都很关键
- 这里真正需要的是有来源、可审查、可追责的辅助系统，而不是流畅但不可靠的对话机器人

## 适合先落地的任务

- 合同条款差异识别
- 判例和法规检索
- 文书草拟与摘要
- 合规检查和政策解释辅助
- 大规模文档集合中的关键信息提取

## 关键价值指标

- draft quality：草稿质量
- citation quality：引用与依据质量
- review time reduction：审查时间下降
- hallucination / unsupported claim rate：无依据输出比例
- human acceptance：律师/合规团队采纳率

## 行业深水区判断

- 法律与合规 agent 的价值，很大程度来自“带证据的推理”和“显式引用”
- 如果系统不能很好地处理 citation、source grounding 和 review handoff，就很难进入真实生产环境
- 这个行业很适合研究 custom model、domain adaptation 和 high-trust review workflow

## 代表案例

- [[../04-Case-Studies/Harvey Legal Work Platform|Harvey Legal Work Platform]]
- [[../04-Case-Studies/Ironclad Contract Review Workflow|Ironclad Contract Review Workflow]]

## 相关

- [[../03-Workflows/Contract Operations Agent Workflow|Contract Operations Agent Workflow]]
- [[../03-Workflows/Procurement Agent Workflow|Procurement Agent Workflow]]
- [[../05-Topics/Agent Productization|Agent Productization]]
- [[../05-Topics/Agent Failure Cases and Deployment Pitfalls|Agent Failure Cases and Deployment Pitfalls]]
- [[../06-Maps/Regulated Industry Agent Map|Regulated Industry Agent Map]]
