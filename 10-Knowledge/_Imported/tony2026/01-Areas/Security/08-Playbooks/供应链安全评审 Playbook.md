---
title: 供应链安全评审 Playbook
type: playbook
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# 供应链安全评审 Playbook

> 用途：评审代码、依赖、构建、镜像、发布、第三方 SDK、SaaS 和供应商是否可信。

## 一句话

供应链安全要保护的是“从代码进入到产物上线”的整条信任链：

`代码 -> 依赖 -> 构建 -> artifact -> 镜像 -> 发布 -> 运行 -> 第三方`

## 评审对象

- 开源依赖。
- 内部包和共享库。
- 容器镜像。
- CI/CD workflow。
- 构建 runner。
- artifact registry。
- 第三方 SDK。
- SaaS 集成。
- 外包交付物。
- 供应商系统访问。

## 核心检查面

### 1. 依赖可信

要问：

- 依赖来源是否可信？
- 是否锁定版本？
- 是否存在 dependency confusion 风险？
- 是否启用 SCA 和 license 检查？
- 是否有高危漏洞升级机制？

高风险信号：

- 生产依赖未锁版本。
- 内部包名和公共仓库冲突。
- 使用无人维护或可疑包。
- 依赖升级无测试和回滚。

### 2. 代码与仓库安全

要问：

- 分支保护是否开启？
- PR 是否要求 review？
- secret scanning 是否覆盖？
- 高风险目录是否有 CODEOWNERS？
- 外部贡献者和机器人权限是否最小化？

高风险信号：

- 直接 push main。
- CI 对 fork PR 暴露 secret。
- bot token 权限过大。

### 3. 构建环境可信

要问：

- 构建 runner 是否隔离？
- 构建脚本能否访问生产 secret？
- 构建过程是否可复现、可审计？
- 是否区分 trusted 和 untrusted build？

高风险信号：

- 公共 runner 可接触敏感凭据。
- 构建脚本下载未经校验的外部脚本。
- 构建环境长期复用且不可清理。

### 4. 产物可信

要问：

- artifact 是否签名？
- 是否有 provenance？
- 是否生成 SBOM？
- 部署时是否验证签名和来源？
- 镜像是否扫描漏洞和恶意内容？

高风险信号：

- 生产能部署未签名 artifact。
- 镜像来源不明。
- registry 权限过大。

### 5. 发布链路安全

要问：

- 谁能触发生产发布？
- 发布是否需要审批？
- 发布凭据如何管理？
- 是否支持回滚？
- 发布事件是否可审计？

高风险信号：

- CI/CD token 能直接改生产。
- 发布和审批同一个人完成。
- 生产发布无审计日志。

### 6. 第三方与供应商

要问：

- 第三方 SDK 收集什么数据？
- SaaS 是否接触敏感数据？
- 供应商是否有安全证明？
- 合同是否包含安全、隐私、通报、审计条款？
- 第三方访问权限是否可回收？

高风险信号：

- SDK 默认收集用户标识或设备信息。
- 供应商账号长期有效。
- 第三方 webhook 无签名校验。

## 分级控制

### 最低控制

- SCA。
- secret scanning。
- branch protection。
- 依赖锁定。
- 高危漏洞 SLA。
- CI/CD secret 最小权限。

### 进阶控制

- SBOM。
- artifact signing。
- provenance。
- CODEOWNERS。
- trusted build isolation。
- deployment approval。

### 高成熟控制

- 签名验证强制执行。
- policy-as-code。
- hermetic / reproducible build。
- 第三方风险持续监控。
- 供应链事件响应演练。

## 评审输出模板

```text
系统/仓库：
供应链范围：
依赖风险：
构建风险：
产物风险：
发布风险：
第三方风险：
阻断项：
风险接受项：
补偿控制：
Owner：
复查时间：
```

## 常见攻击路径

- dependency confusion。
- typosquatting。
- maintainer account takeover。
- malicious postinstall script。
- CI secret exfiltration。
- compromised build runner。
- unsigned artifact replacement。
- malicious third-party SDK。

## 关联

- [[../05-Topics/供应链安全|供应链安全]]
- [[../05-Topics/安全工程与 DevSecOps|安全工程与 DevSecOps]]
- [[../05-Topics/云原生与基础设施安全|云原生与基础设施安全]]
- [[./应用与 API 安全评审 Playbook|应用与 API 安全评审 Playbook]]
