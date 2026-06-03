---
title: 云原生安全基线 Playbook
type: playbook
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# 云原生安全基线 Playbook

> 用途：为云账号、Kubernetes、容器、网络、存储、IaC、CI/CD 和运行时工作负载建立最低安全基线。

## 一句话

云原生安全不是“云上再放一个防火墙”，而是：

`身份最小权限 + 配置默认安全 + 工作负载可验证 + 网络可隔离 + 运行时可检测 + 变更可审计`

## 基线范围

- 云账号和组织结构。
- IAM、角色、service account。
- 网络、VPC、安全组、负载均衡。
- 存储桶、数据库、消息队列。
- Kubernetes 集群。
- 容器镜像和 registry。
- IaC。
- CI/CD。
- runtime security。
- 日志与审计。

## 基线检查

### 1. 云账号与 IAM

最低要求：

- root/admin 账号强 MFA。
- 人员账号和机器账号分离。
- 最小权限角色。
- 高权限操作审批和审计。
- 长期 access key 有 owner、过期和轮换。
- 跨账号访问可追踪。

高风险信号：

- admin 权限泛滥。
- access key 长期未轮换。
- service account 被多人共享。

### 2. 网络与暴露面

最低要求：

- 生产、测试、办公、管理网络隔离。
- 安全组默认拒绝。
- 管理端口不暴露公网。
- 公网入口有 owner 和用途。
- WAF / DDoS / CDN 按业务风险配置。

高风险信号：

- `0.0.0.0/0` 暴露管理端口。
- 数据库公网可达。
- 测试环境能访问生产数据。

### 3. 存储与数据

最低要求：

- 存储桶默认私有。
- 数据库不公网暴露。
- at-rest encryption。
- 备份加密和恢复演练。
- 敏感数据访问审计。

高风险信号：

- 公开 bucket。
- 快照共享不受控。
- 备份无访问控制。

### 4. Kubernetes

最低要求：

- RBAC 最小权限。
- 禁止默认 service account 过权。
- secrets 管理和加密。
- network policy。
- admission control。
- 镜像来源限制。
- privileged container 限制。
- audit log。

高风险信号：

- cluster-admin 过多。
- pod 可默认访问云 metadata。
- 容器 privileged 运行。
- 没有 network policy。

### 5. 容器与镜像

最低要求：

- 镜像扫描。
- 基础镜像来源可信。
- 不以 root 运行。
- read-only filesystem。
- 最小化镜像。
- registry 权限最小化。
- 高危漏洞阻断或例外审批。

高风险信号：

- latest tag 上生产。
- 镜像含 secret。
- 未签名镜像可部署。

### 6. IaC 与 CI/CD

最低要求：

- IaC scanning。
- policy-as-code。
- CI/CD secret 最小权限。
- 生产变更审批。
- 构建和发布日志可审计。
- 高风险变更可回滚。

高风险信号：

- 手工改生产。
- CI 能直接获取生产 admin secret。
- Terraform state 暴露敏感信息。

### 7. 运行时检测

最低要求：

- 云审计日志接入。
- Kubernetes audit log。
- 容器异常行为检测。
- 高权限 API 调用告警。
- 公网暴露变更告警。
- 数据访问异常告警。

高风险信号：

- 出事后无法还原谁改了什么。
- 没有云控制面日志。
- runtime 告警无人分诊。

## 落地顺序

1. 云账号和 IAM 清理。
2. 公网暴露面盘点。
3. 存储和数据库公开访问治理。
4. Kubernetes RBAC、secret、network policy 基线。
5. 镜像扫描和部署准入。
6. IaC scanning 和生产变更审计。
7. 云日志、运行时检测和 incident playbook。

## 关键产物

- 云资产清单。
- 云 IAM 权限矩阵。
- 公网暴露面清单。
- Kubernetes 安全基线。
- 容器镜像安全策略。
- IaC policy。
- 云审计日志和告警规则。

## 指标

- admin 权限账号数量。
- 长期 access key 数量和老化。
- 公网暴露资产数量。
- 公开 bucket 数量。
- 高危镜像漏洞数量。
- privileged workload 数量。
- IaC policy violation 数量。
- 云审计日志覆盖率。

## 关联

- [[../05-Topics/云原生与基础设施安全|云原生与基础设施安全]]
- [[../../Cloud-Native/03-Topics/云原生安全|云原生安全]]
- [[../05-Topics/身份与访问安全|身份与访问安全]]
- [[./供应链安全评审 Playbook|供应链安全评审 Playbook]]
- [[./安全事件响应 Playbook|安全事件响应 Playbook]]
