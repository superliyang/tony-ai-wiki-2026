---
title: 数据生命周期与 Data Lifecycle
type: topic
status: active
domain: Big-Data
updated: 2026-04-25
---

# 数据生命周期与 Data Lifecycle

## 这页解决什么问题

很多大数据学习会从工具开始：Kafka、Spark、Flink、Hive、Iceberg。

但真正稳定的入口是问：

> 一条数据从哪里来，怎样被组织信任，最后怎样进入决策或系统动作？

这就是 `Data Lifecycle`。

## 一条完整生命周期

### 1. Source：数据从哪里来

先判断数据源类型：

- 业务交易：订单、支付、退款、库存、账户
- 用户行为：点击、曝光、搜索、停留、转化
- 系统日志：服务日志、调用链、错误、性能指标
- 外部数据：第三方 API、文件、合作方数据
- 人工数据：运营配置、标注、审核结果

关键问题不是“有没有数据”，而是“谁对这个事实负责”。

### 2. Capture：怎样被采集

常见采集方式：

- batch file import
- API pull / push
- log agent
- CDC
- event tracking SDK
- message / event stream

核心约束：

- schema 是否稳定
- 是否允许重复
- 是否保序
- 是否可回放
- 失败后是否可补偿

### 3. Transport：怎样传输和解耦

传输层让数据生产方和消费方解耦。

- 如果只需要任务通知，可以是 queue
- 如果需要可回放事件历史，更像 Kafka / event log
- 如果需要多团队复用，还需要 schema registry、topic 规范和权限

这一层决定后续能不能做实时计算、回放和多消费者复用。

### 4. Store：怎样长期保存

存储层不只是容量问题。

它要回答：

- 原始数据是否保留
- 清洗后的数据放在哪里
- 查询和计算是否共用一份数据
- 元数据、catalog、权限和表格式如何管理

常见形态包括 warehouse、data lake、lakehouse。

### 5. Process：怎样被计算

计算方式取决于业务约束：

- batch：稳定、可回放、成本可控
- streaming：低延迟、状态连续、适合实时动作
- interactive：面向探索分析和临时查询

不要先问“用 Spark 还是 Flink”，先问延迟、吞吐、状态和回放要求。

### 6. Model：怎样变成业务语言

数据建模把原始事实变成组织能共同理解的对象：

- 维度、事实、指标
- ODS / DWD / DWS / ADS
- semantic layer
- metric store
- data product

这一步决定同一个指标是否只有一个可信版本。

### 7. Serve：怎样被使用

数据服务形态包括：

- BI dashboard
- ad hoc query
- API
- reverse ETL
- feature store
- vector store
- eval dataset

不同服务对象需要不同的 SLA、freshness、权限和质量门槛。

### 8. Govern：怎样被信任

治理不是最后补文档，而是贯穿全链路：

- owner
- data contract
- data quality
- lineage
- catalog
- access control
- privacy
- cost

没有治理，数据平台会变成“没人敢信但又没人敢删”的数据沼泽。

### 9. Retire：怎样下线

成熟的数据平台还要能下线：

- 长期无人使用的数据表
- 成本高但价值低的任务
- 过期指标
- 已被替代的数据产品

下线能力是平台健康度的一部分。

## 判断一个数据链路是否成熟

可以用 7 个问题快速检查：

1. 数据事实源是谁
2. schema 变更谁审批
3. 失败后能不能回放
4. 口径是否有 owner
5. 质量问题能否定位到上游
6. 使用方是否知道 freshness 和 SLA
7. 成本是否能按数据产品或团队归因

## 和后续主题的关系

- [[大数据系统主干]] 是全局地图
- [[Batch 与 Streaming 判断框架]] 负责计算模式取舍
- [[Warehouse、Data Lake 与 Lakehouse]] 负责存储形态取舍
- [[数据治理与指标可信度]] 负责信任与组织控制面

