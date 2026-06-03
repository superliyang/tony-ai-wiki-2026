---
title: 云原生安全与 CNAPP 平台
type: tool-platform
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# 云原生安全与 CNAPP 平台

> CNAPP 的价值是把云配置、身份权限、工作负载、Kubernetes、容器镜像、IaC 和运行时放到同一张风险图里。

## 能力边界

| 子能力 | 关注点 | 典型输出 |
|---|---|---|
| CSPM | 云配置与合规基线 | 公开存储桶、弱加密、危险安全组 |
| CIEM | 云权限和身份风险 | 过权角色、长期 key、跨账号访问 |
| CWPP | 主机、容器、工作负载 | 漏洞、恶意进程、运行时异常 |
| KSPM | Kubernetes 安全态势 | RBAC、NetworkPolicy、Pod 安全配置 |
| IaC Security | 代码中的云风险 | Terraform/K8s manifest 修复建议 |
| Image Security | 镜像漏洞和恶意包 | 镜像风险、基础镜像更新 |
| Runtime Detection | 运行时攻击行为 | 容器逃逸、反弹 shell、异常文件访问 |

## 落地闭环

1. 接云账号和组织结构，统一资产、标签、owner。
2. 建云基线：账号、网络、存储、日志、KMS、K8s、CI/CD。
3. 把高危发现转成工单、PR 或自动修复建议。
4. 把 IaC 扫描前移到 PR，减少上线后修复。
5. 把运行时高危行为接入 SIEM/SOC。
6. 用趋势指标证明暴露面和配置风险持续下降。

## 选型检查点

- 是否支持你的云：AWS、Azure、GCP、阿里云、腾讯云或混合云？
- 是否能统一云资产、K8s、容器镜像、IaC、运行时？
- 是否有攻击路径分析，而不是平铺几千条风险？
- 是否能把 owner、标签、业务系统、数据敏感性纳入排序？
- 是否能接入 CI/CD、工单、SIEM、ChatOps 和审计证据平台？

## 关键指标

- 公网暴露高危资产数量
- 高权限云角色数量
- 公开存储桶和弱配置数量
- K8s 高危配置数量
- 镜像高危漏洞平均修复时间
- IaC 阶段拦截率

## 典型陷阱

- 发现很多云风险，但没有 owner 和业务标签。
- 只做上线后扫描，不把 IaC 和 CI/CD 前移。
- 只看配置，不看身份路径和数据敏感性。
- CNAPP 告警不进 SOC，运行时异常无人响应。

## 官方资料入口

- [Wiz](https://www.wiz.io/)
- [Prisma Cloud Docs](https://docs.prismacloud.io/)
- [Aqua Security](https://www.aquasec.com/)
- [Falco Docs](https://falco.org/docs/)

## 关联

- [[../05-Topics/云原生与基础设施安全|云原生与基础设施安全]]
- [[../08-Playbooks/云原生安全基线 Playbook|云原生安全基线 Playbook]]
- [[../05-Topics/漏洞管理与攻击面管理|漏洞管理与攻击面管理]]
- [[../../Cloud-Native/03-Topics/云原生安全|云原生安全]]

