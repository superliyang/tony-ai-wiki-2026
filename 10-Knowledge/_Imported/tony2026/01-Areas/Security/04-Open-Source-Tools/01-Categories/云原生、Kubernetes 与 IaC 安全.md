---
title: 云原生、Kubernetes 与 IaC 安全
type: category
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# 云原生、Kubernetes 与 IaC 安全

## 解决什么问题

- 云账号、Kubernetes、容器、IaC、运行时和合规基线的可见性。
- 用开源工具理解 CNAPP 的组成：CSPM、KSPM、CWPP、IaC、Runtime。

## 代表项目

- [Prowler](https://github.com/prowler-cloud/prowler)：云安全和合规扫描。
- [Checkov](https://github.com/bridgecrewio/checkov)：IaC 和云配置扫描。
- [kube-bench](https://github.com/aquasecurity/kube-bench)：Kubernetes CIS Benchmark 检查。
- [Kubescape](https://github.com/kubescape/kubescape)：Kubernetes 安全平台。
- [Falco](https://github.com/falcosecurity/falco)：云原生运行时安全。
- [Terrascan](https://github.com/tenable/terrascan)：IaC 合规和安全扫描。
- [ThreatMapper](https://github.com/deepfence/ThreatMapper)：开源 CNAPP 学习样本。
- [tfsec](https://github.com/aquasecurity/tfsec)：Terraform 安全扫描，现已并入 Trivy 方向。
- [Steampipe](https://github.com/turbot/steampipe)：用 SQL 查询云资源和策略。

## 典型组合

`Checkov / Trivy IaC -> Prowler -> kube-bench / Kubescape -> Falco -> SIEM / 工单`

## 风险与边界

- 云扫描结果必须结合账号、标签、owner、数据敏感性和公网暴露排序。
- 运行时检测进入生产前要先调噪，否则会造成告警疲劳。

