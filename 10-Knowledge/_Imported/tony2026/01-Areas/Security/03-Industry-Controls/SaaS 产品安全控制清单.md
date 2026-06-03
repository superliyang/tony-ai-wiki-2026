---
title: SaaS 产品安全控制清单
type: industry-control-checklist
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# SaaS 产品安全控制清单

> SaaS 安全的核心是：租户隔离、企业客户数据保护、身份集成、供应链安全、可审计控制和客户信任。

## 保护对象

- 租户数据、客户配置、企业账号、管理员权限、API token。
- 多租户隔离边界、数据库行级权限、对象存储路径。
- SSO/SAML/OIDC/SCIM 集成、客户审计日志、管理员操作。
- 代码仓、CI/CD、制品、云账号、第三方 SaaS 和供应商。
- 客户合规证据：SOC 2、ISO 27001、渗透测试、数据处理协议。

## 主要威胁

- 租户越权、IDOR、broken access control。
- 管理员账号接管、API token 泄露。
- 多租户数据混淆、日志/分析平台泄露客户数据。
- CI/CD secret 泄露、依赖投毒、云配置错误。
- 客户集成错误：Webhook、SCIM、SAML 配置缺陷。
- 客户审计无法证明控制有效。

## 控制清单

| 控制域 | 必做控制 | 证据 |
|---|---|---|
| 租户隔离 | tenant_id 强制校验、行级权限、对象存储隔离 | 架构评审、测试用例、代码审查 |
| 身份集成 | SSO/SAML/OIDC、SCIM、MFA、管理员审计 | 配置记录、登录日志、审计日志 |
| API 安全 | OAuth scope、rate limit、token 轮换、Webhook 验签 | API 评审、网关策略、测试报告 |
| 安全开发 | SAST/SCA/Secret Scan、IaC Scan、release gate | CI 报告、修复 SLA、例外记录 |
| 云安全 | CSPM、CIEM、KMS、日志、备份和恢复 | 云基线、修复工单、恢复演练 |
| 客户数据保护 | 加密、DLP、数据保留、删除、导出审批 | 数据地图、删除记录、DLP 报告 |
| 检测响应 | 管理员异常、租户越权、批量导出、云变更检测 | SIEM 规则、case、响应记录 |
| 信任与合规 | SOC 2/ISO 证据、状态页、事故通报流程 | GRC 控制库、审计证据、客户包 |

## 平台组合

- IAM / SSO / SCIM：企业客户身份集成和生命周期。
- AppSec / DevSecOps：租户隔离测试、API 安全、依赖和 secret。
- CNAPP：云账号、K8s、对象存储、IAM、IaC。
- SIEM / XDR：管理员行为、客户数据访问、云控制面。
- DLP / DSPM：客户数据发现、导出和保留删除。
- GRC：SOC 2、ISO 27001、客户安全问卷和证据包。

## 关键指标

- 租户隔离测试覆盖率。
- 企业客户 SSO/MFA 覆盖率。
- 高危 AppSec 问题进入生产数量。
- 客户数据批量导出告警数量。
- 云高危配置修复 SLA。
- 客户安全问卷复用率和证据自动化率。

## 常见陷阱

- 只做基础 Web 安全，低估租户隔离和企业身份集成。
- 客户审计日志不完整，导致客户无法自证安全。
- SOC 2 当成一次性项目，控制和证据没有平台化。
- 研发、云、安全、GRC 各自为战，客户问题来时临时拼材料。

## 官方参考入口

- [AICPA SOC Suite of Services](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP API Security](https://owasp.org/API-Security/)
- [Cloud Security Alliance Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix)

## 关联

- [[./行业控制清单索引|行业控制清单索引]]
- [[../05-Topics/应用安全与 API 安全|应用安全与 API 安全]]
- [[../05-Topics/云原生与基础设施安全|云原生与基础设施安全]]
- [[../02-Tools/GRC、合规与证据平台|GRC、合规与证据平台]]

