---
title: Flink 与流处理
type: topic
status: active
domain: Big-Data
updated: 2026-04-25
---

# Flink 与流处理

## 这页解决什么问题

Flink 不要先理解成“比 Spark 更实时”。

更稳的入口是：

> Flink 是面向有状态 stream processing 的计算引擎，核心能力是用低延迟方式处理持续到来的事件，并维护可恢复状态。

## Flink 在大数据链路里的位置

常见链路：

`Kafka / CDC -> Flink -> 实时指标 / 风控决策 / 推荐特征 / 实时数仓 / Lakehouse`

Flink 通常承担：

- 实时聚合
- 实时规则计算
- 实时特征
- session / window 计算
- CDC 数据同步
- 实时数仓明细和聚合层
- 事件驱动业务流程的一部分

## Flink 适合什么

适合：

- 秒级或更低延迟
- 有状态计算
- 事件时间处理
- 迟到数据处理
- 实时风控
- 实时推荐
- 实时告警
- CDC 流处理

不适合：

- 只是每天出一次报表
- 没有清晰事件模型的临时分析
- 不需要低延迟动作的场景
- 团队无法承担状态、回放和 on-call 复杂度的场景

## 关键概念

### Event Time

`event time` 是事件实际发生时间，不是系统处理时间。

它解决的问题是：

- 数据可能延迟到达
- 事件可能乱序
- 业务窗口应该按发生时间计算

### Watermark

`watermark` 是系统对“事件时间进度”的判断。

它帮助 Flink 决定：

- 什么时候关闭窗口
- 迟到数据如何处理
- 结果什么时候可以输出

### State

Flink 的核心价值之一是状态。

状态可以是：

- 用户最近行为
- 账户风险分
- 会话窗口
- 去重集合
- 聚合中间值

状态让实时计算强大，也让恢复、扩容和一致性更复杂。

### Checkpoint

Checkpoint 用于故障恢复。

它让 Flink 能在失败后从一致状态继续处理，但也会带来存储、延迟和调优成本。

### Window

窗口把无限事件流切成可计算范围。

常见窗口：

- tumbling window
- sliding window
- session window

窗口选择应该来自业务语义，而不是默认参数。

## Flink 链路最该问的问题

1. 业务是否真的需要低延迟动作
2. 事件时间字段是否可靠
3. 乱序和迟到数据怎么处理
4. 状态大小会不会持续膨胀
5. checkpoint 成本是否可接受
6. 失败后是否能从 Kafka 或日志回放
7. 实时结果和离线最终口径如何对齐

## Flink 和 Kafka 的关系

Kafka 常作为事件日志和回放来源。

Flink 从 Kafka 消费事件，进行状态计算，然后输出到：

- Kafka 新 topic
- OLAP / serving store
- lakehouse table
- alerting system
- feature store

Kafka 负责事件轨道，Flink 负责流式计算。

## Flink 和 Spark 的关系

- Flink：实时、有状态、event time、低延迟动作
- Spark：批处理、历史重算、大规模离线建模
- 组合：Flink 出实时结果，Spark 做最终校准和回补

## 最常见的误区

### 误区 1：实时指标一定比离线指标更好

实时指标更快，但不一定更准。最终口径经常仍需要离线校准。

### 误区 2：Exactly-once 等于业务绝对不会重复

计算引擎的 exactly-once 不自动等于外部系统副作用 exactly-once。业务写入仍要幂等。

### 误区 3：Flink 能解决所有数据新鲜度问题

如果上游事件埋点、CDC、schema 和质量不稳，Flink 只会更快地放大问题。

## 关联

- [[Kafka 与事件日志]]
- [[Batch 与 Streaming 判断框架]]
- [[../06-Maps/Batch Streaming 判断图|Batch Streaming 判断图]]
- [[数据生命周期与 Data Lifecycle]]

