---
title: GRC、合规与证据平台
type: tool-platform
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# GRC、合规与证据平台

> GRC 平台的价值不是“把表格搬到系统里”，而是把控制、风险、责任、例外、证据和审计发现持续联动。

## 能力边界

| 子能力 | 解决的问题 | 常见输出 |
|---|---|---|
| Control Library | 控制要求分散 | 控制库、框架映射 |
| Risk Register | 风险无人跟踪 | 风险、owner、处理计划 |
| Evidence Automation | 审计前手工截图 | 自动证据、证据有效期 |
| Vendor Risk | 第三方风险不可见 | 问卷、评级、合同控制 |
| Policy Management | 制度无人维护 | 政策、例外、确认 |
| Audit Workflow | 审计发现难闭环 | 任务、证据、整改 |
| Continuous Compliance | 合规状态滞后 | 控制有效性仪表盘 |

## 落地闭环

1. 选控制框架：SOC 2、ISO 27001、PCI DSS、HIPAA、GDPR、内部基线。
2. 建控制库：控制目标、控制活动、owner、频率、证据。
3. 接证据源：IdP、云、Git、CI/CD、EDR、HRIS、工单。
4. 建风险登记：风险描述、影响、可能性、处理方式、到期。
5. 管例外：审批、补偿控制、到期复审。
6. 审计闭环：发现、整改、验证、复盘、控制更新。

## 选型检查点

- 是否支持你需要的框架和行业审计？
- 是否能自动采集证据，而不只是上传附件？
- 是否能和工单、云、IdP、CI/CD、HRIS、供应商管理联动？
- 是否支持风险、例外、补偿控制和到期复审？
- 是否能输出管理层视角：风险趋势、控制有效性、审计发现？

## 关键指标

- 证据自动化率
- 控制 owner 覆盖率
- 风险逾期率
- 例外到期复审率
- 审计发现关闭时间
- 控制复用率

## 典型陷阱

- 为了审计上线 GRC，但没有日常控制 owner。
- 控制库很完整，证据仍然靠人工截图。
- 风险登记没有业务影响和处理计划。
- 例外没有到期时间，永久变成默认状态。

## 官方资料入口

- [ServiceNow Integrated Risk Management](https://www.servicenow.com/products/integrated-risk-management.html)
- [Vanta](https://www.vanta.com/)
- [Drata](https://drata.com/)
- [Open Policy Agent Docs](https://www.openpolicyagent.org/docs/latest/)

## 关联

- [[../05-Topics/安全治理、风险与合规|安全治理、风险与合规]]
- [[../05-Topics/安全指标与成熟度模型|安全指标与成熟度模型]]
- [[../01-Standards/安全标准与法规索引|安全标准与法规索引]]
- [[../08-Playbooks/企业安全架构落地 Playbook|企业安全架构落地 Playbook]]

