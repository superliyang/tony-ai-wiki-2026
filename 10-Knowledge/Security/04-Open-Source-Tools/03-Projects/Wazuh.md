---
title: Wazuh
type: project
status: learning
domain: Security
category: SecOps、检测工程与威胁情报
organization: Wazuh
repo: https://github.com/wazuh/wazuh
local_fit: medium
mac_fit: medium
production_fit: medium
learning_fit: high
updated: 2026-05-05
---

# Wazuh

## 它是什么

Wazuh 是开源安全平台，常被用于 SIEM/XDR、终端监控、合规和云工作负载安全学习。

## 为什么现在值得关注

- 适合搭建蓝队实验室，把 endpoint、日志、规则和告警串起来。
- 能帮助理解商业 XDR/SIEM 背后的基础对象。

## 它在 stack 的哪一层

- 更像 `平台`：SecOps 数据汇聚、检测和告警平台。

## 核心组件与架构

- agent：终端采集。
- manager：规则、分析和告警。
- indexer/dashboard：查询和可视化。
- integrations：云、容器、合规、响应集成。

## 最适合它的场景

- 蓝队实验室。
- 小规模开源 SIEM/XDR 验证。
- 学习检测规则、告警分诊和合规检查。

## 风险与边界

- 生产级 SOC 还需要日志治理、规则调优、case management 和响应流程。

## 关联

- [[../01-Categories/SecOps、检测工程与威胁情报|SecOps、检测工程与威胁情报]]
- [[../../08-Playbooks/SOC 检测工程 Playbook|SOC 检测工程 Playbook]]

