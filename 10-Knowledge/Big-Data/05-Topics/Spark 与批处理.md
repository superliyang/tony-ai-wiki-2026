---
title: Spark 与批处理
type: topic
status: active
domain: Big-Data
updated: 2026-04-25
---

# Spark 与批处理

## 这页解决什么问题

Spark 不要只理解成“大数据计算框架”。

更稳的入口是：

> Spark 是面向大规模数据集的分布式计算引擎，最常见价值是把离线数据转换、聚合、建模和重算做成可扩展任务。

## Spark 在大数据链路里的位置

Spark 常见位置：

`Data Lake / Warehouse / Kafka 落盘数据 -> Spark Job / Spark SQL -> 清洗表 / 聚合表 / Feature / Dataset`

它通常承担：

- ETL / ELT
- 大规模 join
- 历史重算
- 离线指标
- 特征生成
- 数据质量校验
- Lakehouse 表写入

## Spark 适合什么

适合：

- 大规模批处理
- 复杂数据转换
- 大表 join
- 历史回补
- 离线特征
- SQL + DataFrame 混合开发
- 和 lakehouse 表格式配合

不适合：

- 低延迟单条查询
- 强事务业务系统
- 毫秒级实时决策
- 小数据量但极复杂的交互分析

## 关键概念

### Job / Stage / Task

Spark 会把一个计算拆成 job、stage 和 task。

学习 Spark 时要理解：

- 哪些操作会触发 shuffle
- 哪些 stage 是瓶颈
- task 是否数据倾斜

### Shuffle

Shuffle 是 Spark 性能和稳定性的关键成本。

常见触发：

- join
- groupBy
- distinct
- repartition

优化 Spark，很多时候就是减少不必要 shuffle，或者让 shuffle 更均匀。

### DataFrame / SQL

现代 Spark 使用中，DataFrame 和 Spark SQL 通常比低层 RDD 更常见。

它们的价值：

- 更接近分析和数仓语言
- 可以让 optimizer 接管一部分执行计划
- 更容易和表格式、catalog、BI 工具衔接

### Partition

Partition 决定并行度和数据分布。

常见问题：

- partition 太少：并行度不足
- partition 太多：调度开销大
- key 分布不均：数据倾斜

### Cache / Persist

当同一份中间结果被反复使用时，cache 可以减少重复计算。

但 cache 不是万能加速器，会占用内存，也可能造成资源压力。

## Spark 最常见的工程问题

### 数据倾斜

某些 key 过热，导致少数 task 极慢。

处理思路：

- 识别倾斜 key
- salting
- broadcast join
- 预聚合
- 调整分区

### 小文件问题

大量小文件会拖慢查询和调度。

处理思路：

- compact
- 控制写入分区
- 合理设置 file size
- 使用 lakehouse 表维护能力

### 重算成本

离线任务失败或逻辑变更后，经常需要 backfill。

所以 Spark 任务需要：

- 幂等写入
- 明确分区
- 可重跑
- 可校验

## Spark 和 Flink 的关系

不要把 Spark / Flink 简化成谁更先进。

- Spark 更常见于大规模离线处理、SQL、历史重算、batch ETL
- Flink 更常见于低延迟 streaming、状态计算、event time 和实时业务动作
- 很多平台会同时使用：Spark 做离线校准，Flink 做实时计算

## 学 Spark 先抓什么

1. 批处理场景和数据生命周期
2. DataFrame / SQL 的执行模型
3. shuffle、partition、join、数据倾斜
4. 文件布局和 lakehouse 表写入
5. 调度、重跑、质量校验和成本

## 关联

- [[Batch 与 Streaming 判断框架]]
- [[Warehouse、Data Lake 与 Lakehouse]]
- [[Apache Iceberg 与 Lakehouse 表格式]]
- [[数据生命周期与 Data Lifecycle]]

