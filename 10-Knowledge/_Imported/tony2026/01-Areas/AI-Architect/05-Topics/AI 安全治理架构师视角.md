---
title: AI 安全治理架构师视角
type: topic
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 安全治理架构师视角

> AI 安全治理不是上线前加一个内容审核接口，而是围绕数据、上下文、工具、模型行为、权限和审计建立信任边界。

## 架构师要回答的问题

- AI 系统能看到哪些数据？
- AI 系统能调用哪些工具？
- 哪些动作必须人工审批？
- prompt injection、RAG 泄露、tool abuse 怎么防？
- 出现错误输出或越权动作，如何审计和响应？

## 风险面

| 风险 | 说明 |
|---|---|
| Prompt Injection | 用户或文档诱导模型违背原始指令 |
| Jailbreak | 绕过模型安全策略 |
| RAG Data Leakage | 检索出用户无权访问的内容 |
| Tool Abuse | 模型被诱导调用危险工具 |
| Memory Poisoning | 恶意信息进入长期记忆 |
| Sensitive Logs | prompt、文件、输出进入日志泄露 |
| Cross-tenant Leakage | 多租户上下文混淆 |
| Over-automation | 高风险动作缺少人工确认 |

## 控制点

| 控制点 | 架构要求 |
|---|---|
| 输入控制 | 文件扫描、敏感数据识别、prompt injection 检测 |
| 上下文控制 | 最小上下文、权限过滤、引用来源 |
| 模型控制 | system prompt、policy、structured output |
| 工具控制 | 最小权限、审批、速率限制、审计 |
| 输出控制 | 敏感信息过滤、合规检查、人工复核 |
| 运行控制 | trace、告警、kill switch、incident response |
| 治理控制 | release gate、risk register、audit evidence |

## 关键设计决策

### 什么时候必须人工审批

- 外部发送消息。
- 修改生产数据。
- 付款、退款、转账、下单。
- 删除、授权、发布、封禁。
- 访问或导出敏感数据。

### 日志怎么记录

- 记录足够复盘的信息。
- 对敏感字段脱敏。
- 记录权限决策和工具调用。
- 明确保留周期和访问权限。

### 红队怎么做

- prompt injection pack。
- jailbreak pack。
- RAG exfiltration pack。
- tool misuse pack。
- policy bypass pack。

## 常见失败模式

- 只做模型内容安全，不管工具权限。
- RAG 没有文档权限过滤。
- agent 能直接执行高风险动作。
- 日志保存完整用户输入和敏感文件。
- 没有 AI incident response。

## 架构师交付物

- AI threat model
- AI trust boundary map
- Tool permission matrix
- AI security eval pack
- AI release gate
- AI incident response runbook

## 关联

- [[../../AI-Engineering/08-Maps/AI Security Engineering Map|AI Security Engineering Map]]
- [[../../AI-Engineering/08-Maps/AI Security 控制点图|AI Security 控制点图]]
- [[../../AI-Engineering/09-Templates/AI 安全评审模板|AI 安全评审模板]]
- [[../../Security/03-Industry-Controls/AI 产品安全控制清单|AI 产品安全控制清单]]

