---
title: 漏洞管理与攻击面管理 Playbook
type: playbook
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# 漏洞管理与攻击面管理 Playbook

> 用途：把“扫出漏洞”升级为“知道暴露了什么、风险有多大、谁负责、何时修复、如何验证和复盘”。

## 一句话

漏洞管理不能只看 CVSS；真正的排序要看：

`资产重要性 + 暴露面 + 可利用性 + 威胁情报 + 业务影响 + 补偿控制 + 修复成本`

## 两个对象

### 攻击面管理

回答：我们暴露了什么？

- 域名、子域名、IP、端口。
- Web、API、管理后台。
- 云资产、存储桶、数据库、负载均衡。
- SaaS、第三方集成、供应商入口。
- 移动端、客户端、SDK。
- CI/CD、代码仓库、artifact registry。

### 漏洞管理

回答：这些资产有什么弱点？

- CVE。
- 错误配置。
- 弱口令和身份风险。
- 暴露密钥。
- 依赖漏洞。
- Web/API 漏洞。
- 云和容器风险。

## 流程

### 1. 资产发现

输入：

- CMDB。
- 云账号。
- DNS 和证书。
- 代码仓库。
- CI/CD。
- API 网关。
- WAF/CDN。
- 外部扫描。

输出：

- 资产清单。
- owner。
- 环境：生产、测试、办公、第三方。
- 暴露位置：公网、内网、第三方、仅本地。

### 2. 暴露面识别

重点看：

- 公网入口。
- 管理后台。
- 未认证 API。
- 远程管理端口。
- 存储桶和数据库公开访问。
- 过期域名和 dangling DNS。
- 第三方回调和 Webhook。

输出：

- exposed asset list。
- unknown owner list。
- shadow IT list。

### 3. 扫描与情报关联

数据源：

- SAST / DAST / SCA。
- cloud posture scanning。
- container image scanning。
- IaC scanning。
- secret scanning。
- EDR / runtime signals。
- threat intelligence。

不要只收集结果，要合并去重并绑定资产和 owner。

### 4. 风险分级

排序维度：

- 是否公网暴露。
- 是否有在野利用。
- 是否有 PoC。
- 是否影响高权限或敏感数据。
- 是否在关键业务路径。
- 是否可横向移动。
- 是否有 WAF、隔离、只读、鉴权等补偿控制。
- 是否有监管或客户审计影响。

建议分级：

- `P0`：正在被利用或已造成影响。
- `P1`：公网可利用，影响高权限、敏感数据或关键业务。
- `P2`：条件利用但影响明确。
- `P3`：低影响或有强补偿控制。

### 5. 修复与例外

每个风险必须有：

- owner。
- SLA。
- 修复方式。
- 验证方式。
- 临时补偿控制。
- 例外理由和到期时间。

例外不能是“以后再说”，必须是有期限的风险接受。

### 6. 验证与复盘

验证：

- 复扫。
- 配置检查。
- exploit 验证。
- 日志确认没有被利用。
- 补偿控制测试。

复盘：

- 为什么这个漏洞存在？
- 为什么扫描现在才发现？
- 为什么没有默认安全配置？
- 是否需要 release gate 或基线改进？

## SLA 建议

| 优先级 | 典型情况 | 建议动作 |
|---|---|---|
| P0 | 正在利用、数据泄露、关键系统接管 | 立即响应，按事件处理 |
| P1 | 公网可利用、高敏数据、高权限 | 24-72 小时内止血或修复 |
| P2 | 条件利用，中等影响 | 7-30 天修复 |
| P3 | 低影响或强补偿控制 | 纳入 backlog 和周期治理 |

## 指标

- unknown asset count。
- exposed asset count。
- critical exposure count。
- P1/P2 漏洞数量。
- SLA breach rate。
- mean time to remediate。
- reopened vulnerability count。
- exception aging。
- owner coverage。
- exploit-in-the-wild coverage。

## 关键产物

- 资产和攻击面清单。
- 漏洞优先级列表。
- 修复 SLA 看板。
- 例外登记册。
- 暴露面趋势报告。
- 根因复盘和 release gate 改进项。

## 常见误区

- 只看扫描器分数。
- 资产没有 owner。
- 测试环境公网暴露但没人管。
- 修复后不验证。
- 例外永久化。
- 不检查是否已经被利用。

## 关联

- [[../05-Topics/漏洞管理与攻击面管理|漏洞管理与攻击面管理]]
- [[../06-Maps/攻击面与控制点图|攻击面与控制点图]]
- [[./安全快速诊断 Playbook|安全快速诊断 Playbook]]
- [[./安全事件响应 Playbook|安全事件响应 Playbook]]
