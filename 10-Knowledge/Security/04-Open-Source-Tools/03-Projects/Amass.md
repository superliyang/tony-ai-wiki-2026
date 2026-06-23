---
title: Amass
type: project
status: learning
domain: Security
category: 攻击面发现与资产测绘
organization: OWASP
repo: https://github.com/owasp-amass/amass
local_fit: high
mac_fit: high
production_fit: medium
learning_fit: high
updated: 2026-05-05
---

# Amass

## 它是什么

OWASP Amass 是攻击面映射和资产发现工具，常用于子域名、DNS、OSINT 和外部资产发现。

## 为什么现在值得关注

- 是理解 ASM/EASM 的经典开源入口。
- 能和 ProjectDiscovery 工具链组合成外部攻击面流程。

## 它在 stack 的哪一层

- 更像 `子系统`：资产发现和攻击面测绘组件。

## 最适合它的场景

- 授权资产盘点。
- 外部暴露面基线。
- 漏洞管理前置资产发现。

## 风险与边界

- 发现资产不等于确认归属，需要去重、验证和 owner 归属。
- 外部枚举和扫描必须遵守授权范围。

## 关联

- [[../01-Categories/攻击面发现与资产测绘|攻击面发现与资产测绘]]
- [[../../05-Topics/漏洞管理与攻击面管理|漏洞管理与攻击面管理]]

