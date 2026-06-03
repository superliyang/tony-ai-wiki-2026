---
title: Falco
type: project
status: learning
domain: Security
category: 云原生、Kubernetes 与 IaC 安全
organization: Falco Security
repo: https://github.com/falcosecurity/falco
local_fit: medium
mac_fit: medium
production_fit: medium
learning_fit: high
updated: 2026-05-05
---

# Falco

## 它是什么

Falco 是云原生运行时安全工具，通过系统调用和规则检测容器、Kubernetes 和主机上的异常行为。

## 为什么现在值得关注

- 运行时安全是 CNAPP/CWPP 的关键层。
- Falco 是理解 Kubernetes runtime detection 的高价值开源样本。

## 它在 stack 的哪一层

- 更像 `子系统`：运行时检测和告警组件。

## 核心抽象

- rule：行为检测规则。
- source：syscall、Kubernetes audit、cloudtrail 等。
- output：日志、告警、SIEM、response pipeline。

## 最适合它的场景

- Kubernetes runtime detection 实验。
- 容器逃逸、异常 shell、敏感文件访问等检测。

## 风险与边界

- 上生产前要做规则调噪。
- 需要和 SIEM、工单、响应 playbook 接起来。

## 关联

- [[../01-Categories/云原生、Kubernetes 与 IaC 安全|云原生、Kubernetes 与 IaC 安全]]
- [[../../08-Playbooks/云原生安全基线 Playbook|云原生安全基线 Playbook]]

