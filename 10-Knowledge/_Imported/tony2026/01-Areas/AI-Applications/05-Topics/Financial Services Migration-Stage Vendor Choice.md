---
title: Financial Services Migration-Stage Vendor Choice
type: topic
status: learning
tags:
  - ai/applications
  - ai/finance
  - ai/high-trust
  - ai/vendor-selection
  - ai/migration
created: 2026-03-24
updated: 2026-03-24
---

# Financial Services Migration-Stage Vendor Choice

## 一句话结论

金融服务场景通常适合 `ChatGPT Agent -> evidence-backed workflow -> approval-gated internal workflow -> private runtime` 这条路径，而不是一开始就跳到最重的 runtime 形态。

## 阶段 1：Read-only assistant

- 更适合：`ChatGPT Agent`
- 原因：最先创造价值的通常是 advisor prep、knowledge access、meeting summary 和 policy support
- 代表案例：[[../04-Case-Studies/Morgan Stanley Wealth Management Assistant|Morgan Stanley Wealth Management Assistant]]

## 阶段 2：Workflow assistant

- 更适合：`ChatGPT Agent`，或早期 internal workflow prototype
- 原因：这时关键是把 evidence-backed packet、research memo 和 client-facing prep 结构化
- 判断重点：review handoff 是否清晰，source grounding 是否稳定

## 阶段 3：Approval-gated action

- 更适合：bounded `ChatGPT Agent` workflow，或更受控的 internal runtime
- 原因：一旦涉及 CRM action、workflow routing 或敏感知识系统写入，审计和审批变成第一优先级
- 判断重点：哪些动作只能建议，哪些动作可以执行

## 阶段 4：Runtime with control plane

- 更适合：`OpenClaw` 这类更可控的 runtime，外加治理层
- 原因：当组织需要长期 internal orchestration、private memory 和 tool policy 时，前台 assistant 已经不够
- 这时 `Claude Code / Cursor / Codex` 也更像 build layer，而不是业务终端层

## 相关

- [[Financial Services Agent Vendor Choice]]
- [[Financial Services Assistant-to-Runtime Path]]
- [[Migration-Stage Vendor Selection in High-Trust Domains]]
- [[../04-Case-Studies/Morgan Stanley Wealth Management Assistant|Morgan Stanley Wealth Management Assistant]]
