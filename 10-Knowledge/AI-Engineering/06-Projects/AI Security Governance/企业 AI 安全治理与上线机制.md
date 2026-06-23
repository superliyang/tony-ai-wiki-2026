---
title: 企业 AI 安全治理与上线机制
type: project-doc
status: learning
created: 2026-03-27
updated: 2026-03-27
---

# 企业 AI 安全治理与上线机制

## 目标

为一个已经开始做 `LLM app / agent` 的企业建立第一阶段安全治理模型。

## 典型需求

- 统一 threat modeling 和 review language
- 给 agent / tool / memory / artifact 建立默认控制点
- 把 red-team、regression、approval 和 rollout 变成正式上线门槛
- 建立 incident 和 exception owner

## 推荐机制

### 路线 A：platform-led

- 平台团队维护 control points 与默认 release gates
- 安全团队做 review board 和例外审批
- 应用团队按风险等级接入

适合：已有平台团队、agent 数量会增长的组织。

### 路线 B：security-led

- 安全团队主导评审标准和 blocking rules
- 平台团队提供落地能力
- 高风险项目逐个过 gate

适合：高合规或 agent 仍处早期探索阶段的组织。

### 路线 C：pilot-first

- 先挑一条高风险但边界清晰的 workflow
- 建一套最小 review + telemetry + rollback 闭环
- 用 pilot 反推平台默认值

适合：还没有成熟 operating model，但想避免抽象治理空转的团队。

## 不推荐的误区

- 只有内容审核，没有动作 gate
- 只有 policy 文档，没有 telemetry owner
- 只有 red-team 报告，没有 ship / no-ship 决策人
- 把所有 AI 风险都塞给模型团队或 AppSec 团队单独承担

## 关联

- [[Agent 安全评审任务包]]
- [[../../07-Topics/Enterprise AI Security Operating Model|Enterprise AI Security Operating Model]]
- [[../../07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
