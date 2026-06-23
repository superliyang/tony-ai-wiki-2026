---
title: AI 产品安全控制清单
type: industry-control-checklist
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# AI 产品安全控制清单

> AI 产品安全的核心是：保护训练/检索/推理链路、用户数据、模型行为、工具调用、agent 权限和安全评测证据。

## 保护对象

- 用户 prompt、上传文件、对话历史、企业知识库、向量库。
- 模型、系统提示词、工具调用、agent workflow、插件和连接器。
- 训练数据、微调数据、评测集、标注数据和反馈数据。
- 推理服务、API key、模型网关、缓存、日志和观测数据。
- 安全策略、内容过滤、权限边界、人工审核和事故证据。

## 主要威胁

- Prompt injection、jailbreak、越权工具调用。
- RAG 数据泄露、跨租户检索、向量库权限错误。
- 上传文件恶意内容、文档解析漏洞、数据投毒。
- 模型输出敏感数据、幻觉导致错误业务动作。
- Agent 被诱导发邮件、转账、删数据、调用内部系统。
- 模型供应链、插件、连接器和第三方模型风险。

## 控制清单

| 控制域 | 必做控制 | 证据 |
|---|---|---|
| 数据边界 | 用户数据分类、租户隔离、RAG 权限过滤、日志脱敏 | 数据地图、检索测试、DLP 报告 |
| Prompt 与上下文 | 系统提示保护、上下文最小化、注入检测、输出过滤 | 安全评测、红队样例、策略版本 |
| 工具调用 | 最小权限、用户确认、动作分级、dry-run、回滚 | 工具权限矩阵、调用日志、审批记录 |
| Agent 安全 | 任务边界、预算/频率限制、人工中断、异常行为检测 | workflow 设计、监控指标、case |
| 模型与供应链 | 模型来源、依赖、插件、连接器、第三方 API 评估 | 供应商评估、SBOM、风险登记 |
| 评测与红队 | jailbreak、数据泄露、越权、滥用、偏见和安全性评测 | eval 报告、缺陷清单、修复记录 |
| 隐私与合规 | 用户同意、保留删除、训练使用边界、DSAR | 隐私评审、删除记录、政策版本 |
| 检测响应 | 异常 prompt、敏感输出、工具滥用、批量导出告警 | SIEM 规则、审计日志、响应记录 |

## 平台组合

- IAM / Policy：用户、租户、工具、agent 和连接器权限。
- AppSec / DevSecOps：AI 网关、插件、文件解析、供应链。
- DLP / DSPM：prompt、文件、知识库、日志和向量库敏感数据。
- SIEM / Observability：prompt 安全事件、工具调用、异常输出。
- GRC / AI Governance：模型卡、风险登记、安全评测、政策证据。
- AI Eval / Red Team：jailbreak、prompt injection、RAG 泄露和滥用测试。

## 关键指标

- 高危工具调用必须确认的覆盖率。
- RAG 权限过滤测试通过率。
- Prompt injection / jailbreak 回归通过率。
- 敏感输出拦截率和误杀率。
- AI 安全事件 MTTD / MTTR。
- 模型/插件/连接器风险评估覆盖率。

## 常见陷阱

- 把 AI 安全只理解成内容安全，不管权限、数据和工具调用。
- RAG 只做向量检索，不做文档级、段落级、租户级权限过滤。
- Agent 工具权限过大，没有用户确认、回滚和审计。
- 安全评测只做上线前一次，不做版本回归。
- 日志里保存完整 prompt、文件和敏感输出，形成新的数据泄露面。

## 官方参考入口

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [CISA Secure by Design](https://www.cisa.gov/securebydesign)

## 关联

- [[./行业控制清单索引|行业控制清单索引]]
- [[../05-Topics/应用安全与 API 安全|应用安全与 API 安全]]
- [[../05-Topics/数据安全与隐私保护|数据安全与隐私保护]]
- [[../../AI-Engineering/08-Maps/AI Security 控制点图|AI Security 控制点图]]

