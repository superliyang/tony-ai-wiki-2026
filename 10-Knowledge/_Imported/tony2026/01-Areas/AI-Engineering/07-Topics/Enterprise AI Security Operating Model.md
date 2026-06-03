---
title: Enterprise AI Security Operating Model
type: topic
status: learning
tags:
  - ai/engineering
  - ai/security
  - ai/operating-model
created: 2026-03-27
updated: 2026-03-27
---

# Enterprise AI Security Operating Model

## 为什么这页重要

AI Security 真正难的部分，往往不是买哪个工具，而是：

- 谁负责威胁建模
- 谁维护 release gate
- 谁审批高风险上线
- 谁对 incident 和 exception 兜底

也就是说，企业最终需要的不是一组散工具，而是一套 operating model。

## 一套常见的组织分层

### 1. 产品 / 应用团队

负责：

- 定义业务目标
- 标出高风险动作与高风险数据
- 配合安全评审

### 2. 平台 / Agent 平台团队

负责：

- 统一 tool / memory / approval control points
- 提供 guardrails、gateway、tracing、release gate 能力
- 把安全控制做成平台默认值

### 3. Security / AppSec / GRC 团队

负责：

- threat modeling 方法
- review board 与例外机制
- 红队策略与 incident policy

### 4. 风险 owner / 业务 owner

负责：

- 在高风险用例上拍板是否上线
- 决定何时进入更高门槛的人审与审计模式

## operating model 真正要解决的 4 个问题

### 1. 谁来定义默认安全底座

不能让每个 agent 团队各自发明：

- prompt injection 处理方式
- tool safety 规则
- memory redaction 规则
- release gate 规则

### 2. 谁来批准例外

现实里总会出现：

- 为了速度，临时放宽 guardrails
- 某个高价值 workflow 想跳过人工审批
- 某个团队想先不上完整 red-team

这些都需要正式的 exception owner。

### 3. 谁来盯生产事件

AI incident 常常跨边界：

- 输入风险
- 数据访问
- tool misuse
- hallucinated action
- policy bypass

所以 incident 不能只归模型团队，也不能只归 SRE。

### 4. 谁来维护上线门槛

release gate 必须有 owner，不然很快就会沦为“建议项”。

## 一个很实用的落地判断

- 低风险 internal copilot：安全控制可以轻一些，但必须有日志和 kill switch
- tool-using agent：必须进入 platform + security 联合治理
- 高风险 external / regulated workflow：必须进入正式 review board 与 exception 管理

## 关联

- [[AI Security Threat Modeling]]
- [[AI 安全案例与失败模式]]
- [[Agent 上线门槛与安全 Release Gates]]
- [[AI Security Telemetry、Escalation 与 Incident Response]]
- [[../08-Maps/Enterprise AI Security Operating Model Map|Enterprise AI Security Operating Model Map]]
- [[../06-Projects/AI Security Governance/项目总览|AI Security Governance]]

## 资料

- [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [OWASP GenAI Security Project](https://genai.owasp.org/)
