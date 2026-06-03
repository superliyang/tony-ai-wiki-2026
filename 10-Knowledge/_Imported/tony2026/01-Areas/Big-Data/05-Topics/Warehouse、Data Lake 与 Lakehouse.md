---
title: Warehouse、Data Lake 与 Lakehouse
type: topic
status: active
domain: Big-Data
updated: 2026-04-25
---

# Warehouse、Data Lake 与 Lakehouse

## 这页解决什么问题

很多团队会把 warehouse、data lake、lakehouse 当成代际替换：

- warehouse 旧
- data lake 便宜
- lakehouse 新

更准确的看法是：它们解决的问题不同，组织能力要求也不同。

## Warehouse：强分析体验与治理

Warehouse 更适合：

- BI 报表
- 稳定指标
- 多团队 SQL 分析
- 权限、审计、性能和治理要求高的场景

它的优势：

- SQL 体验好
- 性能和并发能力成熟
- 权限、审计、数据模型相对集中
- 对分析师和业务团队友好

它的代价：

- 存储和计算成本可能高
- 半结构化 / 非结构化数据灵活性较弱
- 原始数据沉淀和多引擎复用不一定自然

## Data Lake：低成本与多格式沉淀

Data lake 更适合：

- 原始数据长期沉淀
- 日志、文件、半结构化数据、多媒体数据
- 数据科学和探索性处理
- 多引擎共享底层对象存储

它的优势：

- 成本低
- 格式灵活
- 适合保存原始数据
- 适合多团队、多用途探索

它的风险：

- 容易变成 data swamp
- 表管理、事务、schema 演进弱
- 权限、质量、catalog 如果缺失，复用会很差

## Lakehouse：开放存储上的表管理与治理能力

Lakehouse 想解决的是：

> 能不能在 data lake 的开放存储上，获得接近 warehouse 的表管理、事务、治理和查询体验？

关键组件：

- 开放对象存储
- 表格式：Iceberg / Delta / Hudi 类能力
- catalog
- query engine
- compute engine
- permission / governance

Lakehouse 的价值：

- 一份数据支持多种计算引擎
- 更容易兼顾 BI、ML、AI 和数据科学
- 存储和计算解耦
- 原始数据和建模数据可以在同一底座上管理

Lakehouse 的挑战：

- 组件更多，集成复杂
- 性能、权限、并发、catalog 需要整体设计
- 团队如果没有平台能力，可能只是把复杂度搬到自己身上

## 怎么选择

### 优先 Warehouse

如果你的核心问题是：

- BI 报表稳定
- 指标口径治理
- 分析师 SQL 体验
- 权限审计
- 快速交付业务看板

### 优先 Data Lake

如果你的核心问题是：

- 原始数据种类多
- 成本敏感
- 先沉淀再探索
- 数据科学和离线处理较多

### 优先 Lakehouse

如果你的核心问题是：

- 多引擎复用同一份数据
- BI、ML、AI 共用数据底座
- 希望开放存储 + 表管理 + 治理统一
- 团队有能力管理 catalog、表格式和多引擎兼容

## 最常见的误区

### 误区 1：Lakehouse 自动替代 Warehouse

不一定。很多组织仍然需要 warehouse 提供稳定 BI 和治理体验。

### 误区 2：Data Lake 只要便宜存储就够了

没有 catalog、quality、lineage 和 owner，便宜存储很快会变成低信任数据堆。

### 误区 3：表格式就是 Lakehouse

表格式只是关键部件之一。Lakehouse 还需要 catalog、权限、计算、治理和运维能力。

### 误区 4：选型只看性能 benchmark

真实选型还要看团队能力、成本模型、生态、治理需求和迁移路径。

## 关联

- [[../06-Maps/Warehouse Lakehouse 判断图|Warehouse Lakehouse 判断图]]
- [[数据生命周期与 Data Lifecycle]]
- [[数据治理与指标可信度]]
- [[大数据决策导航]]

