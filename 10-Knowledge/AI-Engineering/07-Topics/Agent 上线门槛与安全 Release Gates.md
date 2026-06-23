---
title: Agent 上线门槛与安全 Release Gates
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
  - ai/agents
created: 2026-03-27
updated: 2026-03-27
---

# Agent 上线门槛与安全 Release Gates

## 为什么 agent 需要单独的 release gate

传统模型上线更关注：

- 质量指标
- 延迟与成本
- 稳定性

agent 上线则还必须回答：

- 它能调用什么工具
- 哪些动作必须审批
- memory 会不会放大错误
- 失败后怎么中断、回滚和审计

## 一组最小上线门槛

### 1. 威胁建模完成

- 明确输入面、context 面、tool 面、state 面、artifact 面
- 明确高风险动作与高风险数据

### 2. prompt injection / tool safety 过线

- 对外部内容不默认信任
- 高风险 tool call 有 policy gate 或 human approval

### 3. guardrails 与 gateway 已接入

- 至少要有一层 request / response 或 action policy
- 对异常输出和异常动作有降级策略

### 4. release 前 red-team 与 regression 完成

- 至少有一组固定的 adversarial prompts
- 关键失败模式被纳入 release checklist

### 5. 生产环境具备 kill switch

- 能快速停用工具
- 能切回只读模式
- 能禁用 memory 写入或高风险动作

## 它和普通 eval 的区别

普通 eval 问的是“效果够不够好”。

release gate 问的是“即使出错，系统会不会越界”。

## 关联

- [[AI Security Threat Modeling]]
- [[Prompt Injection Defense 与 Tool Safety]]
- [[AI Security Evaluation 与 Red Teaming]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[Eval Harness 与 Regression Suites]]
- [[../08-Maps/AI Security 控制点图|AI Security 控制点图]]
