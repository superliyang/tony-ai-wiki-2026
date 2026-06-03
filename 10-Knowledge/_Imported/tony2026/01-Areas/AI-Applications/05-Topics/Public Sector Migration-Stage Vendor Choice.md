---
title: Public Sector Migration-Stage Vendor Choice
type: topic
status: learning
tags:
  - ai/applications
  - ai/public-sector
  - ai/high-trust
  - ai/vendor-selection
  - ai/migration
created: 2026-03-24
updated: 2026-03-24
---

# Public Sector Migration-Stage Vendor Choice

## 一句话结论

公共部门的阶段性选型通常首先被 `approved cloud / deployment boundary / audit model` 决定，所以产品迁移往往比商业环境更保守。

## 阶段 1：Read-only assistant

- 更适合：`ChatGPT Agent`，前提是 approved cloud 可行
- 原因：policy navigation、secure knowledge work、staff productivity 最适合先起步
- 代表案例：[[../04-Case-Studies/ChatGPT Gov and Federal Workforce Deployment|ChatGPT Gov and Federal Workforce Deployment]]

## 阶段 2：Workflow assistant

- 更适合：bounded assistant + workflow assist
- 原因：这时最大的价值仍然是 case prep、document triage、admin routing，而不是自治执行
- 判断重点：输出能否归档、审计和复核

## 阶段 3：Approval-gated action

- 更适合：非常收敛的 action scope
- 原因：越权和审计缺口在公共部门的代价很高
- 判断重点：role boundary、incident path 和 policy compatibility

## 阶段 4：Runtime with control plane

- 更适合：私有或强控制 internal runtime，加上 system-of-record / control-plane 视角
- 原因：真正进入 runtime 时，组织关注点已经转向长期治理，而不只是 productivity

## 相关

- [[Public Sector Agent Vendor Choice]]
- [[Public Sector Assistant-to-Runtime Path]]
- [[Migration-Stage Vendor Selection in High-Trust Domains]]
- [[../04-Case-Studies/ChatGPT Gov and Federal Workforce Deployment|ChatGPT Gov and Federal Workforce Deployment]]
