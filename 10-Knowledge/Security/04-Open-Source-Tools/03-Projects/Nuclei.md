---
title: Nuclei
type: project
status: learning
domain: Security
category: 攻击面发现与资产测绘
organization: ProjectDiscovery
repo: https://github.com/projectdiscovery/nuclei
local_fit: high
mac_fit: high
production_fit: medium
learning_fit: high
updated: 2026-05-05
---

# Nuclei

## 它是什么

Nuclei 是 ProjectDiscovery 生态里的模板化漏洞扫描器，用 YAML DSL 把检测逻辑标准化。

## 为什么现在值得关注

- 社区模板生态活跃，适合快速验证常见暴露面和已知漏洞。
- 能和 subfinder、httpx、naabu 等工具组成攻击面验证链路。

## 它在 stack 的哪一层

- 更像 `子系统`：攻击面验证与漏洞检测组件。
- 上游接资产发现，下游接漏洞管理、工单和复测。

## 核心组件与架构

- template：检测规则。
- target：扫描目标。
- engine：请求发送、匹配、提取和结果输出。
- workflow：组合多个模板和前置条件。

## 最适合它的场景

- 授权范围内的暴露面验证。
- 漏洞管理里的趋势漏洞快速排查。
- 红蓝紫演练中的检测覆盖验证。

## 风险与边界

- 不等于完整漏洞管理平台。
- 对生产目标扫描要控制速率、模板范围和授权边界。

## 关联

- [[../01-Categories/攻击面发现与资产测绘|攻击面发现与资产测绘]]
- [[../../08-Playbooks/漏洞管理与攻击面管理 Playbook|漏洞管理与攻击面管理 Playbook]]

