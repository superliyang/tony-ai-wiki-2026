---
title: Codecov Bash Uploader 复盘
type: case-study
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# Codecov Bash Uploader 复盘

## 案例定位

Codecov Bash Uploader 是“CI/CD 脚本被篡改，进而影响客户流水线凭据”的供应链案例。

它训练的是：

- CI/CD 环境变量和 secret 为什么是高价值资产。
- 从公网下载脚本直接执行为什么危险。
- 供应商脚本也属于你的构建攻击面。

## 资料入口

- Codecov post-mortem：<https://about.codecov.io/apr-2021-post-mortem/>
- Codecov security update：<https://about.codecov.io/security-update/>
- CISA alert：<https://www.cisa.gov/news-events/alerts/2021/04/30/codecov-releases-new-detections-supply-chain-compromise>

## 资产

- CI/CD 环境变量。
- 云凭据、部署 token、包仓库 token。
- 构建日志、测试覆盖率上传脚本。
- 供应商脚本和下载地址。

## 攻击面

- CI/CD pipeline。
- 第三方 bash uploader。
- 环境变量。
- 外部脚本下载和执行。
- 构建 runner 网络出口。

## 攻击链抽象

```text
第三方脚本被篡改 -> CI 执行脚本 -> 环境变量被读取 -> 凭据外泄 -> 下游系统被访问
```

## 控制缺口

- CI secret 范围过大。
- 下载脚本没有校验 checksum 或固定版本。
- 第三方 CI 工具权限没有最小化。
- 构建环境网络出口和敏感变量访问缺少限制。
- 凭据轮换和影响判断困难。

## 正确响应

### 立即动作

- 判断是否在影响时间窗口使用过相关 uploader。
- 轮换 CI 环境变量中的凭据、token、key。
- 检查云、代码仓库、包仓库、部署系统访问日志。
- 检查异常发布、异常资源创建、异常数据访问。

### 后续动作

- 禁止 curl pipe bash 式高风险执行。
- 固定版本和 checksum。
- 使用短期凭据和 workload identity。
- 限制 CI job 的 secret 暴露范围。
- 将构建脚本纳入供应链安全评审。

## 可迁移教训

- CI/CD 是生产环境的入口，不只是工程效率工具。
- 环境变量里的 secret 一旦被脚本读取，就可能跨系统扩散。
- 第三方脚本要按依赖和供应商处理。
- 凭据轮换能力是 incident response 的一部分。

## 自我演练

- CI/CD 中有哪些长期凭据？
- 哪些 job 能访问生产部署权限？
- 是否使用外部脚本直接执行？
- 是否能按 job、分支、环境限制 secret？
- 如果供应商脚本被篡改，多久能轮换所有相关凭据？

## 关联

- [[../05-Topics/供应链安全|供应链安全]]
- [[../05-Topics/安全工程与 DevSecOps|安全工程与 DevSecOps]]
- [[../08-Playbooks/供应链安全评审 Playbook|供应链安全评审 Playbook]]
- [[../08-Playbooks/安全事件响应 Playbook|安全事件响应 Playbook]]
