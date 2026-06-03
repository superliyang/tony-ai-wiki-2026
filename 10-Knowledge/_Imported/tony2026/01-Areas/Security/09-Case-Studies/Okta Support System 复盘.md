---
title: Okta Support System 复盘
type: case-study
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# Okta Support System 复盘

## 案例定位

Okta Support System 事件是“身份供应商的支持系统和客户上传文件成为攻击路径”的案例。

它训练的是：

- 身份系统周边系统同样是高价值资产。
- 支持工单、HAR 文件、截图、录屏可能包含敏感 token。
- 日志完整性和客户通知速度会直接影响响应质量。

## 资料入口

- Okta root cause and remediation：<https://sec.okta.com/articles/2023/11/unauthorized-access-oktas-support-case-management-system-root-cause/>

## 资产

- 支持系统。
- 客户上传文件。
- session token、cookie、HTTP header、HAR 文件。
- 客户租户、管理员账号、身份配置。
- 支持人员账号和浏览器配置。

## 攻击面

- 客户支持门户。
- 支持人员工作站和浏览器 profile。
- 上传附件。
- 支持工单访问权限。
- 客户文件下载和处理流程。

## 攻击链抽象

```text
支持系统凭据/环境风险 -> 访问客户上传文件 -> 提取敏感令牌或上下文 -> 尝试访问客户环境 -> 客户侧检测和响应
```

## 控制缺口

- 支持系统未按身份核心系统同等级保护。
- 客户上传文件可能包含 session token 等敏感信息。
- 支持人员浏览器和个人 profile 隔离不足。
- 日志覆盖和可见性不足会影响调查时间线。
- 客户安全联系人和通知机制需要足够及时。

## 正确响应

### 立即动作

- 确认支持系统访问范围。
- 识别受影响客户和文件。
- 让客户轮换可能暴露的 session、token、cookie。
- 检查客户环境异常登录和身份配置变更。
- 强化支持系统访问控制和日志。

### 后续动作

- 支持系统按 crown jewel 周边系统治理。
- 客户上传文件自动脱敏或敏感内容提示。
- 支持人员设备、浏览器、profile 强隔离。
- 对支持系统访问做细粒度审计。
- 建立客户安全联系人和分级通知流程。

## 可迁移教训

- 身份系统的“周边流程”也可能变成身份攻击入口。
- 支持文件、日志、截图、HAR 文件不能当作普通附件处理。
- 客户支持系统需要最小权限、强审计和数据保留策略。
- 供应商安全事件也会变成客户侧 incident response。

## 自我演练

- 支持系统能访问哪些客户数据？
- 客户上传文件是否可能包含 token、cookie、密钥？
- 支持人员是否能批量下载客户附件？
- 支持系统日志是否能还原谁访问了什么文件？
- 如果身份供应商通知风险，客户侧如何快速验证影响？

## 关联

- [[../05-Topics/身份与访问安全|身份与访问安全]]
- [[../08-Playbooks/零信任落地 Playbook|零信任落地 Playbook]]
- [[../08-Playbooks/数据安全与隐私评审 Playbook|数据安全与隐私评审 Playbook]]
- [[../08-Playbooks/SOC 检测工程 Playbook|SOC 检测工程 Playbook]]
