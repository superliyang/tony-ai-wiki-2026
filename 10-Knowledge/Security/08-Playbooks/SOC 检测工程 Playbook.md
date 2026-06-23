---
title: SOC 检测工程 Playbook
type: playbook
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# SOC 检测工程 Playbook

> 用途：把 SOC 从“收日志和看告警”升级为“围绕攻击路径设计检测、分诊、响应和复盘”的工程体系。

## 一句话

检测工程的核心不是告警越多越好，而是：

`关键资产 + 攻击场景 + 必要日志 + 检测逻辑 + 分诊上下文 + 响应动作 + 复盘改进`

## 检测工程流程

### 1. 选择检测场景

优先从高风险场景开始：

- 高权限账号异常登录。
- MFA fatigue。
- 云 access key 泄露。
- 数据批量导出。
- 管理后台异常操作。
- CI/CD secret 使用异常。
- Kubernetes cluster-admin 滥用。
- 横向移动。
- 勒索前兆。
- 供应链投毒。

不要先写“万能规则”，先写能解释、能响应的场景。

### 2. 明确攻击路径

每个场景要写清：

- 初始入口。
- 权限提升。
- 横向移动。
- 目标资产。
- 数据访问或破坏。
- 逃逸和持久化。

输出：

- detection hypothesis。
- expected telemetry。
- response action。

### 3. 确认日志源

优先日志源：

- IdP / SSO / MFA。
- 云审计日志。
- EDR / XDR。
- 网络流量和 DNS。
- API gateway。
- 应用审计日志。
- 数据库审计。
- CI/CD 日志。
- Kubernetes audit log。
- WAF / CDN。

判断标准：

- 是否能定位主体。
- 是否能定位资源。
- 是否有时间线。
- 是否能关联上下文。
- 是否保留足够时间。

### 4. 编写检测逻辑

检测逻辑要包括：

- 触发条件。
- 排除条件。
- 严重级别。
- 所需字段。
- 关联窗口。
- 误报预期。
- 分诊步骤。
- 响应动作。

规则不是写完就结束，要有 owner 和生命周期。

### 5. 分诊和上下文

一个可运营告警必须能回答：

- 谁触发？
- 访问了什么？
- 是否异常？
- 是否涉及高权限或敏感数据？
- 是否有近期变更、漏洞、工单或发布？
- 需要谁处理？

如果告警只有“异常”两个字，没有上下文，就是成本黑洞。

### 6. 响应动作

每条高价值检测都应该有响应动作：

- 强制登出。
- 禁用账号。
- 轮换密钥。
- 隔离主机或 workload。
- 阻断 IP / domain。
- 暂停 pipeline。
- 冻结数据导出。
- 升级 incident。

### 7. 测试和调优

测试方式：

- tabletop。
- purple team。
- attack simulation。
- replay historical logs。
- controlled test。

调优维度：

- precision。
- recall。
- mean time to triage。
- false positive rate。
- alert fatigue。

## 检测规则模板

```text
规则名称：
检测目标：
攻击场景：
数据源：
触发逻辑：
排除逻辑：
严重级别：
分诊步骤：
响应动作：
误报来源：
Owner：
复查周期：
```

## 优先检测场景

### 身份

- impossible travel。
- MFA 多次失败后成功。
- 新设备登录高权限账号。
- 高权限角色突然授予。
- 离职账号活动。

### 云

- 创建新 access key。
- 禁用日志。
- 修改安全组为公网开放。
- 大量读取对象存储。
- 新建高权限角色。

### 应用/API

- 权限拒绝激增。
- 单用户批量访问不同租户数据。
- 数据导出异常。
- 管理接口非预期调用。
- SSRF/注入特征命中。

### 终端

- credential dumping 行为。
- 可疑 PowerShell。
- 横向移动工具。
- 勒索加密行为。
- EDR 被禁用。

### CI/CD 与供应链

- fork PR 访问 secret。
- release workflow 异常触发。
- artifact 被覆盖。
- 新增未知依赖。
- 构建脚本下载外部 payload。

## SOC 成熟度

### Level 1：告警接收

- 工具产生告警。
- 人工查看。
- 缺少上下文。

### Level 2：规则运营

- 有规则 owner。
- 有分诊流程。
- 有基础响应 playbook。

### Level 3：场景驱动

- 按攻击路径设计检测。
- 日志源和规则持续调优。
- 事件复盘反哺规则。

### Level 4：检测工程平台化

- detection-as-code。
- 自动测试。
- 规则版本管理。
- 告警到响应动作闭环。

## 指标

- MTTD。
- MTTR。
- false positive rate。
- alert-to-incident conversion rate。
- detection coverage。
- log source coverage。
- rules with owner。
- stale rule count。
- time to triage。

## 常见误区

- 日志全收但没人分析。
- 规则越多越安全。
- 告警没有 owner。
- 没有分诊上下文。
- 没有响应动作。
- 事件复盘不更新规则。

## 关联

- [[../05-Topics/安全运营、检测与响应|安全运营、检测与响应]]
- [[../06-Maps/安全运营与事件响应闭环图|安全运营与事件响应闭环图]]
- [[../06-Maps/红队蓝队紫队演练闭环图|红队蓝队紫队演练闭环图]]
- [[./红队蓝队紫队演练路径 Playbook|红队蓝队紫队演练路径 Playbook]]
- [[./安全事件响应 Playbook|安全事件响应 Playbook]]
- [[../05-Topics/安全指标与成熟度模型|安全指标与成熟度模型]]
