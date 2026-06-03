---
title: AI 安全案例与失败模式
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
created: 2026-03-27
updated: 2026-03-27
---

# AI 安全案例与失败模式

## 为什么要单独看案例

AI security 如果只停留在“原则”，很容易显得抽象。

真正拉开团队差距的，是能不能把威胁翻译成：

- 真实 failure mode
- 可观测的控制点
- 可以放进 release gate 的检查项

## 一组很典型的失败模式

### 1. prompt injection 直接升级成动作风险

当系统能调用搜索、文件、浏览器、终端或内部 API 时，攻击不再只是“让模型说错话”，而是：

- 诱导错误调用工具
- 外带敏感数据
- 绕过原本的人审和权限边界

### 2. guardrails 只有内容过滤，没有动作约束

很多系统会做输出审核，但对 tool call、approval、memory 更新没有同等约束。

### 3. 模型与 artifact 的来源不透明

如果没有扫描、签名、版本和 provenance，风险会进入：

- model 文件
- adapter
- prompt 包
- eval 数据集
- 部署镜像

### 4. 安全评测和上线门槛脱节

有些团队会做 red team，但结果没有进入：

- CI / release gate
- canary 规则
- production rollback 条件

## 从案例里能学到什么

- `Azure AI Content Safety` 代表托管式输入风险检测层
- `Cloudflare AI Gateway Guardrails` 代表 gateway-first 的多模型控制层
- `NeMo Guardrails` 代表应用内 guardrails / dialogue policy 层
- `ModelScan` 代表模型 artifact 供应链层
- `Promptfoo` 代表 pre-release eval / red-team / regression 层

## 最重要的工程结论

成熟的 AI 安全体系，通常不是一个产品解决，而是至少 5 个控制点一起工作：

1. 输入与上下文检测
2. tool / action 安全控制
3. guardrails / gateway 策略层
4. artifact / supply chain 完整性
5. eval / release gate / rollback 闭环

## 关联

- [[AI Security Threat Modeling]]
- [[Prompt Injection Defense 与 Tool Safety]]
- [[Guardrails、Policy Enforcement 与 Security Gateways]]
- [[Model Supply Chain Security]]
- [[AI Security Evaluation 与 Red Teaming]]
- [[Agent 上线门槛与安全 Release Gates]]
- [[../08-Maps/AI Security 控制点图|AI Security 控制点图]]
