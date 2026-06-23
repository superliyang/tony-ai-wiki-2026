---
title: Semantic Layer 与指标治理
type: topic
status: active
domain: Big-Data
updated: 2026-04-26
---

# Semantic Layer 与指标治理

## 这页解决什么问题

`Semantic Layer` 解决的是：

> 指标和业务语义不应该散落在 BI SQL、notebook、ETL 脚本、AI prompt 和 API 里。

它把指标定义、维度关系、口径规则和访问方式集中起来，让不同消费端复用同一套业务语义。

## 为什么需要 Semantic Layer

没有 semantic layer 时：

- BI 看板一套 SQL
- 数据科学 notebook 一套 SQL
- 运营报表一套 SQL
- AI agent 查询一套 prompt / tool logic
- 不同团队对同一指标各算各的

结果是：工具越多，指标越不可信。

## Semantic Layer 管什么

### 1. Metrics

定义指标：

- DAU
- GMV
- 支付成功率
- 留存
- LTV
- 拒付率
- 风控误杀率
- 活动转化率

每个指标应该有 owner、公式、过滤条件、时间窗口和适用范围。

### 2. Dimensions

定义分析维度：

- 时间
- 国家
- 渠道
- 版本
- 用户分层
- 商户
- 支付方式
- 游戏区服
- 实验组

维度不是字段列表，而是业务切分方式。

### 3. Entities

定义业务实体：

- user
- account
- order
- payment
- merchant
- player
- session
- document
- dataset

实体关系决定指标能否正确 join 和归因。

### 4. Access Rules

定义谁能看什么：

- 敏感字段脱敏
- 行列级权限
- 国家 / 区域限制
- 业务域权限
- AI agent 可查询范围

### 5. Serving Contracts

定义消费契约：

- freshness
- latency
- granularity
- allowed dimensions
- fallback
- deprecation

## Semantic Layer 和 BI 的关系

BI 是消费端，不应该是指标真相来源。

更稳的结构是：

`Data Warehouse / Lakehouse -> Semantic Layer -> BI / API / Notebook / Agent`

这样同一套指标可以服务：

- dashboard
- ad hoc analysis
- embedded analytics
- reverse ETL
- AI agent query
- metric alerting

## Semantic Layer 和 AI 的关系

AI agent 要查询业务数据时，semantic layer 很重要。

否则 agent 可能：

- 用错表
- join 错粒度
- 误解指标口径
- 绕过权限
- 生成看似正确但口径错误的 SQL

给 AI 的数据工具，不应该只暴露数据库，而应该暴露受控的业务语义和指标接口。

## 指标治理流程

一个核心指标进入 semantic layer 前，至少要经过：

1. 业务定义
2. owner 确认
3. 源表和血缘确认
4. 计算公式确认
5. 维度和粒度确认
6. 质量规则确认
7. 权限规则确认
8. 下游消费登记

## 最常见的误区

### 误区 1：Semantic Layer 只是统一 SQL

不只是 SQL，它统一的是业务语义、指标口径、实体关系和消费契约。

### 误区 2：有了 dbt 就自动有指标治理

dbt 可以承载建模和测试，但指标治理还需要 owner、业务定义、权限、消费契约和变更流程。

### 误区 3：只给 BI 用

现代 semantic layer 应该服务 BI、API、数据科学、运营自动化和 AI agent。

### 误区 4：先覆盖所有指标

应该先治理高价值、高争议、高复用指标，而不是追求一次性覆盖。

## 和三条案例的关系

- 支付实时风控：approval rate、fraud rate、chargeback rate、false positive 需要统一口径
- 游戏实时运营：DAU、CCU、retention、ARPU、LTV、活动转化率需要统一口径
- AI 数据供给：dataset freshness、eval pass rate、retrieval hit rate、incident regression coverage 需要统一口径

## 关联

- [[数仓建模与指标口径]]
- [[数据治理与指标可信度]]
- [[../09-Case-Studies/AI 数据供给链路|AI 数据供给链路]]
- [[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]

