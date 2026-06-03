---
title: Healthcare Migration-Stage Vendor Choice
type: topic
status: learning
tags:
  - ai/applications
  - ai/healthcare
  - ai/high-trust
  - ai/vendor-selection
  - ai/migration
created: 2026-03-24
updated: 2026-03-24
---

# Healthcare Migration-Stage Vendor Choice

## 一句话结论

医疗场景更适合长期停留在 `bounded assistant / workflow assistant` 阶段，只有在隐私、review 和 override 机制都成熟后，才适合进入更重的 runtime 形态。

## 阶段 1：Read-only assistant

- 更适合：`ChatGPT Agent`
- 原因：documentation relief、claims support、internal knowledge assist 最容易先创造价值
- 代表案例：[[../04-Case-Studies/Oscar Healthcare Operations Assistant|Oscar Healthcare Operations Assistant]]

## 阶段 2：Workflow assistant

- 更适合：`ChatGPT Agent` 或非常受控的 internal workflow
- 原因：医疗更看重 bounded workflow，而不是高自治
- 判断重点：是否有明确 reviewer、evidence trail 和访问边界

## 阶段 3：Approval-gated action

- 更适合：受限 action workflow，而不是广义 autonomous runtime
- 原因：很多写入和动作都会间接影响 patient 或 payer outcome
- 判断重点：human override、incident path 和 PHI control 是否成熟

## 阶段 4：Runtime with control plane

- 更适合：强控制、低副作用的 internal runtime
- 原因：如果真进入 runtime，重点已不是效率，而是 privacy、auditability 和 safe orchestration

## 相关

- [[Healthcare Agent Vendor Choice]]
- [[Healthcare Assistant-to-Runtime Path]]
- [[Migration-Stage Vendor Selection in High-Trust Domains]]
- [[../04-Case-Studies/Oscar Healthcare Operations Assistant|Oscar Healthcare Operations Assistant]]
