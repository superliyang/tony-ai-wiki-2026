---
title: Vault
type: project
status: learning
domain: Security
category: 身份、密钥、证书与策略
organization: HashiCorp
repo: https://github.com/hashicorp/vault
local_fit: medium
mac_fit: medium
production_fit: high
learning_fit: high
updated: 2026-05-05
---

# Vault

## 它是什么

Vault 是 secret 管理、加密服务和动态凭据平台。

## 为什么现在值得关注

- secret 治理是云、CI/CD、微服务和零信任的基础能力。
- 能帮助理解密钥、凭据、租约、轮换、审计和访问策略。

## 它在 stack 的哪一层

- 更像 `底座`：身份、密钥和凭据治理底座。

## 核心抽象

- auth method：认证方式。
- secrets engine：secret 存储或动态凭据。
- policy：访问控制。
- lease：租约和轮换。
- audit device：审计。

## 最适合它的场景

- CI/CD secret 治理。
- 动态数据库凭据。
- 加密服务和证书管理。

## 风险与边界

- 自托管复杂度高，尤其是 HA、unseal、备份、权限和审计。
- Vault 本身会成为关键系统。

## 关联

- [[../01-Categories/身份、密钥、证书与策略|身份、密钥、证书与策略]]
- [[../../05-Topics/密码学、密钥与证书基础|密码学、密钥与证书基础]]

