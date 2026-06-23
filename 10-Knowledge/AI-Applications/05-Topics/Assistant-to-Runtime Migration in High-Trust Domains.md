---
title: Assistant-to-Runtime Migration in High-Trust Domains
type: topic
status: learning
tags:
  - ai/applications
  - ai/high-trust
  - ai/runtime
  - ai/migration
created: 2026-03-24
updated: 2026-03-24
---

# Assistant-to-Runtime Migration in High-Trust Domains

## 这一页在回答什么

这一页回答的是：在金融、医疗、法律/合规、公共部门这类高信任场景里，组织通常怎么从 `assistant mode` 走到 `runtime mode`。这不是一个“直接上 autonomous agent”的故事，而更像一条分阶段的迁移路径。

## 一个先讲清楚的前提

下面的迁移框架，不是某一家厂商官方给出的标准路线，而是我基于官方产品能力、治理产品和行业案例做的归纳。

换句话说：
- `产品能力` 来自官方资料
- `迁移路径` 是结合这些资料和案例做的应用层推断

## 常见的四阶段迁移路径

### 1. Read-only assistant

- 从知识检索、总结、meeting prep、policy navigation 开始
- 目标是先让用户信任 agent 的信息组织能力
- 风险控制重点是 source grounding 和范围限制

### 2. Workflow assistant

- agent 不只是回答问题，而是进入固定流程
- 典型形式是 review packet、risk memo、case draft、exception summary、triage recommendation
- 这时开始需要标准输入、结构化输出和明确的 handoff

### 3. Approval-gated action agent

- agent 可以触发动作，但必须挂审批或双人复核
- 典型形式是工单流转、数据回写、case creation、routing、pre-approved action
- 这一步的重点是 auditability、role boundary 和 failure recovery

### 4. Runtime with control plane

- agent 不再只是前台 surface，而是内部 runtime
- 组织开始关心 session、memory、tool policy、runtime supervision、system of record 和 control tower
- 这里的重点已经不是“它会不会回答”，而是“它如何被治理”

## 哪些条件成熟了，才应该往右走

- source-of-truth 已经清楚，而不是多个系统互相打架
- 输出已经结构化，能被审查、回滚和复核
- approval gate 已经设计好，而不是靠临时人工兜底
- failure mode 和 incident path 已被定义
- 组织知道什么是只读、什么是建议、什么才允许执行

## 产品在迁移路径里的典型角色

- `ChatGPT Agent`：通常更适合阶段 1 和阶段 2，也能进入受限的阶段 3
- `OpenClaw`：当组织进入更强 control、私有 memory、工具编排和长期运行时，会更值得研究
- `Claude Code / Cursor / Codex`：多数时候更像 build layer，用来搭内部 runtime 或 workflow system
- `Workday Agent System of Record / Agent Gateway`、`ServiceNow AI Control Tower`：代表组织开始把 agent 当成需要编排、观测和治理的数字劳动力来管理

## 一个实用判断法

先不要问“要不要 runtime”，先问：

1. 这个场景现在最稳定的价值是不是只读 assist
2. 我们是否已经把输入、输出、review handoff 结构化
3. 是否存在成熟的 approval gate 和 incident path
4. 是否真的需要长期 memory、system action 和 multi-step orchestration
5. 如果需要，再决定是不是进入 runtime 阶段

## 分行业细分页

- [[Financial Services Assistant-to-Runtime Path]]
- [[Healthcare Assistant-to-Runtime Path]]
- [[Legal and Compliance Assistant-to-Runtime Path]]
- [[Public Sector Assistant-to-Runtime Path]]

## 来源

- OpenAI Global Affairs: [Introducing ChatGPT Gov](https://openai.com/global-affairs/introducing-chatgpt-gov/)
- OpenAI: [Providing ChatGPT to the entire U.S. federal workforce](https://openai.com/index/providing-chatgpt-to-the-entire-us-federal-workforce/)
- OpenClaw Docs: [Architecture](https://docs.openclaw.ai/concepts/architecture), [Memory](https://docs.openclaw.ai/concepts/memory), [Heartbeat](https://docs.openclaw.ai/gateway/heartbeat)
- Workday: [Agent System of Record](https://newsroom.workday.com/2025-02-11-The-Next-Generation-of-Workforce-Management-is-Here-Workday-Unveils-New-Agent-System-of-Record?trk=public_post_comment-text)
- Workday: [Agent Gateway](https://newsroom.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces)
- ServiceNow: [AI Control Tower](https://www.servicenow.com/products/ai-control-tower.html)

## 相关

- [[Migration-Stage Vendor Selection in High-Trust Domains]]
- [[High-Trust Agent Vendor Selection]]
- [[Financial Services Agent Vendor Choice]]
- [[Healthcare Agent Vendor Choice]]
- [[Legal and Compliance Agent Vendor Choice]]
- [[Public Sector Agent Vendor Choice]]
- [[../06-Maps/Assistant-to-Runtime Migration Map|Assistant-to-Runtime Migration Map]]
- [[../../AI-Engineering/07-Topics/Long-Running Agent Operations|Long-Running Agent Operations]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
