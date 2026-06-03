---
title: BloodHound
type: project
status: learning
domain: Security
category: 授权攻防、AD 与对抗模拟
organization: SpecterOps
repo: https://github.com/SpecterOps/BloodHound
local_fit: medium
mac_fit: low
production_fit: medium
learning_fit: high
updated: 2026-05-05
---

# BloodHound

## 它是什么

BloodHound 用图模型分析 Active Directory 攻击路径，帮助识别从普通权限到高权限的可达路径。

## 为什么现在值得关注

- AD 攻击路径是企业内网安全的核心问题之一。
- 它体现了“权限图”和“攻击路径”思维。

## 它在 stack 的哪一层

- 更像 `子系统`：AD 攻击路径分析和风险可视化。

## 最适合它的场景

- 授权 AD 安全评估。
- 紫队演练中的路径验证。
- 身份权限治理和过权分析。

## 风险与边界

- 数据采集必须授权。
- 发现路径后要转成权限治理、检测规则和修复计划。

## 关联

- [[../01-Categories/授权攻防、AD 与对抗模拟|授权攻防、AD 与对抗模拟]]
- [[../../05-Topics/身份与访问安全|身份与访问安全]]

