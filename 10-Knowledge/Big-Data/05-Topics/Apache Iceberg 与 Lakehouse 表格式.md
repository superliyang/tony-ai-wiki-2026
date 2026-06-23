---
title: Apache Iceberg 与 Lakehouse 表格式
type: topic
status: active
domain: Big-Data
updated: 2026-04-25
---

# Apache Iceberg 与 Lakehouse 表格式

## 这页解决什么问题

学习 lakehouse 时，最容易把它误解成：

> 把 Parquet 文件放到对象存储里，就变成了 lakehouse。

不够。

Lakehouse 需要表格式来管理文件、schema、snapshot、事务和元数据。Apache Iceberg 就是这类开放表格式的代表之一。

## Iceberg 在大数据链路里的位置

常见链路：

`Object Storage -> Iceberg Table -> Spark / Flink / Trino / Warehouse / Catalog`

Iceberg 不是计算引擎，而是数据表的管理层。

它让多个计算引擎可以围绕同一份开放存储数据协作。

## 表格式解决什么

### 1. Snapshot

表不是一堆文件，而是一组可追踪的 snapshot。

这带来：

- time travel
- rollback
- 可审计变更
- 更安全的读写隔离

### 2. Schema Evolution

真实数据会变：

- 新增字段
- 字段重命名
- 类型调整
- 上游语义变化

表格式需要让 schema 变化更可控，而不是让下游直接崩掉。

### 3. Partition Evolution

早期分区设计可能不适合未来查询。

表格式希望支持更灵活的分区演进，避免一次分区设计永久绑死。

### 4. ACID-like Table Operations

Lakehouse 要支持更安全的写入、更新和删除。

这对以下场景重要：

- 多任务写入
- CDC 同步
- 数据修正
- 隐私删除
- 合规处理

### 5. File and Metadata Management

开放存储容易出现：

- 小文件
- 过期文件
- metadata 膨胀
- 查询规划慢

表格式提供维护入口，但仍需要平台定期 compaction、expire snapshot 和监控。

## Iceberg 适合什么

适合：

- 多引擎访问同一份数据
- 对象存储上的开放 lakehouse
- 大规模分析表
- 需要 schema / partition evolution
- 需要 time travel / snapshot / rollback
- Spark、Flink、Trino 等多引擎协作

不适合：

- 小团队完全不需要开放存储和多引擎复用
- 只做简单 BI 且 warehouse 已经足够
- 没有 catalog、权限、维护能力的“裸表格式”堆砌

## Iceberg、Delta、Hudi 怎么看

不要一开始陷入宗教战争。

先问：

- 你的主要写入模式是 batch、streaming，还是 CDC upsert
- 你的主要查询引擎是什么
- 你是否需要开放生态和多引擎兼容
- 你的 catalog 和权限体系怎么做
- 谁负责 compaction、snapshot 清理和表维护

这几个表格式的价值都在 lakehouse 管理层，差异要放在具体平台上下文里判断。

## Iceberg 不是 Lakehouse 全部

Iceberg 只是表格式。

Lakehouse 还需要：

- object storage
- catalog
- compute engines
- query engines
- access control
- governance
- data quality
- orchestration
- cost management

如果这些不补，Iceberg 只会让文件管理更像表，但不会自动变成可信数据平台。

## 最常见的误区

### 误区 1：有 Iceberg 就有 Lakehouse

Iceberg 是关键部件，不是完整平台。

### 误区 2：表格式能自动解决数据治理

它能改善表管理，但 owner、quality、lineage、permission 仍要设计。

### 误区 3：所有数据都该迁进 Iceberg

迁移要看访问模式、复用价值、成本和治理收益。

### 误区 4：只看读性能

还要看写入模式、并发、维护、catalog、权限和团队经验。

## 关联

- [[Warehouse、Data Lake 与 Lakehouse]]
- [[Spark 与批处理]]
- [[Flink 与流处理]]
- [[数据治理与指标可信度]]

