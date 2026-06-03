---
title: Open-Source、Self-Hosting 与 Managed LLMOps
type: topic
status: learning
tags:
  - ai/engineering
  - ai/llmops
  - ai/self-hosting
created: 2026-03-26
updated: 2026-03-26
---

# Open-Source、Self-Hosting 与 Managed LLMOps

## 为什么这页重要

企业做 `LLMOps` 时，经常不是功能选型先卡住，而是部署模式先卡住。

尤其当你开始碰到：

- 数据边界
- 合规
- 内部审计
- 多租户隔离
- 私有网络
- 成本归因

你很快就会发现：部署模式本身就是产品选型的一半。

## 三种常见模式

### 1. Open-source self-assembly

特点：

- 自己搭 tracking、eval、observability、deployment
- 灵活
- 成本结构可控
- 但需要更强平台工程能力

典型组合：

- `MLflow`
- `Phoenix`
- `Promptfoo`
- `OpenTelemetry`
- `KServe / Argo CD`

### 2. Self-hosted productized platform

特点：

- 平台能力更完整
- 仍然可控数据边界
- 运维复杂度通常比纯自组装低

典型代表：

- `Langfuse self-hosted`
- `Phoenix self-hosted`
- `W&B self-managed`

### 3. Managed / hosted product

特点：

- 启动快
- 团队负担轻
- 功能成熟
- 但需要接受数据、网络和 vendor dependency 约束

## 这三种模式真正的 tradeoff

### `Open-source` 的优势

- 灵活
- 不容易被单一 vendor 锁住
- 更适合已有平台团队的组织

### `Open-source` 的代价

- 很多整合工作要自己做
- 版本兼容、认证、运维和 UI 体验都要自己兜底

### `Self-hosted product` 的优势

- 比纯开源组装快
- 比完全托管更可控
- 对企业是常见平衡点

### `Managed product` 的优势

- 最快形成生产力
- 适合先证明价值
- 更适合没有专门平台团队的业务线

## 一个实用判断

- 你有平台团队，且监管要求高：优先 `self-hosted`
- 你要先快速证明价值：优先 `managed`
- 你已经有成熟 K8s / observability / delivery 体系：可以接受更多 open-source assembly

## 学习这页最该记住什么

企业不是在选“最先进工具”，而是在选：

- 哪种平台责任分配最适合自己
- 哪种部署模式最符合自己的风险承受能力

## 关联

- [[Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
- [[../06-Projects/Enterprise LLMOps/Enterprise LLMOps 平台选型文档|Enterprise LLMOps 平台选型文档]]
- [[../../Cloud-Native/03-Topics/平台工程|平台工程]]
- [[../../Cloud-Native/03-Topics/Internal Developer Platform|Internal Developer Platform]]
