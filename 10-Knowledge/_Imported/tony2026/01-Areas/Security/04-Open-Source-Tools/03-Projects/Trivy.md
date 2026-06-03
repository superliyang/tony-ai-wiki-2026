---
title: Trivy
type: project
status: learning
domain: Security
category: DevSecOps 与供应链安全
organization: Aqua Security
repo: https://github.com/aquasecurity/trivy
local_fit: high
mac_fit: high
production_fit: high
learning_fit: high
updated: 2026-05-05
---

# Trivy

## 它是什么

Trivy 是 Aqua Security 的多合一扫描工具，覆盖漏洞、错误配置、secret、SBOM、容器、Kubernetes、代码仓和云。

## 为什么现在值得关注

- 一个工具可以串起 DevSecOps、云原生和供应链多个控制点。
- 适合从个人实验室过渡到 CI/CD release gate。

## 它在 stack 的哪一层

- 更像 `子系统`：安全扫描和证据生成组件。
- 可嵌入 PR、构建、镜像发布、Kubernetes 检查和云基线。

## 核心组件与架构

- scanner：vulnerability、misconfig、secret、license、SBOM。
- target：filesystem、image、repo、kubernetes、cloud。
- output：SARIF、CycloneDX、SPDX、JSON 等。

## 最适合它的场景

- 容器镜像扫描。
- IaC 和 Kubernetes 配置检查。
- CI/CD 中生成安全证据。

## 风险与边界

- 扫描发现必须绑定 owner、SLA、例外和复测。
- 漏洞优先级不能只看 CVSS，要结合暴露面和可达性。

## 关联

- [[../01-Categories/DevSecOps 与供应链安全|DevSecOps 与供应链安全]]
- [[../01-Categories/云原生、Kubernetes 与 IaC 安全|云原生、Kubernetes 与 IaC 安全]]

