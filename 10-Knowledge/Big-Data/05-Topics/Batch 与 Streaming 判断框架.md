---
title: Batch 与 Streaming 判断框架
type: topic
status: active
domain: Big-Data
updated: 2026-04-25
---

# Batch 与 Streaming 判断框架

## 这页解决什么问题

很多人把 batch 和 streaming 当成技术偏好：

- Spark vs Flink
- 离线 vs 实时
- 旧架构 vs 新架构

更稳的判断是：

> 业务是否真的需要低延迟、连续状态和实时反馈？

## Batch 适合什么

Batch 适合：

- 日报、月报、财务结算、监管报送
- 大规模历史重算
- 可容忍分钟到小时级延迟的分析
- 需要稳定回放和低复杂度的链路
- 对成本敏感、对实时性不敏感的任务

Batch 的优势：

- 模型简单
- 容易重跑
- 容易校验
- 成本相对可控
- 适合做最终口径和审计口径

Batch 的弱点：

- 不能支撑低延迟动作
- 对连续状态支持弱
- 问题发现可能滞后

## Streaming 适合什么

Streaming 适合：

- 实时风控
- 实时推荐
- 实时运营触达
- 实时监控与告警
- 用户行为实时反馈
- 事件驱动业务流程

Streaming 的优势：

- 延迟低
- 能维护连续状态
- 能快速触发业务动作
- 能更接近事件发生时处理

Streaming 的代价：

- 状态管理复杂
- event time 和 late data 难处理
- exactly-once 不是免费午餐
- 回放、补数和纠错更复杂
- 运维和调试成本更高

## 最重要的 6 个判断维度

### 1. Latency

- 小时级：通常 batch 足够
- 分钟级：micro-batch 或 near-real-time 可能足够
- 秒级或更低：考虑 streaming

### 2. State

- 只做聚合报表：batch 更简单
- 需要持续维护用户、账户、设备、session 状态：streaming 更自然

### 3. Correctness

- 财务、清结算、监管：通常需要 batch 做最终校准
- 风控、推荐、告警：允许先实时行动，再离线校正

### 4. Replay

- 如果经常需要重算历史，batch 更稳
- 如果 streaming 链路也要支持 replay，需要事件日志、状态恢复和版本化设计

### 5. Cost

- Streaming 是持续运行成本
- Batch 是周期性资源成本
- 成本不仅是机器，还包括工程复杂度和 on-call 成本

### 6. Business Action

- 如果数据只是“被看见”，不一定需要 streaming
- 如果数据会立刻触发拦截、推荐、报价、告警或调度，streaming 价值更高

## 最常见的架构：Hybrid

成熟平台通常不是 batch 或 streaming 二选一，而是：

- streaming 做实时特征、实时告警、实时动作
- batch 做历史回放、最终口径、离线训练、成本优化
- 两者通过统一数据模型、统一 catalog 和统一质量规则收敛

## 一个快速决策句式

如果业务问题是：

- “明天早上要看准确报表”：优先 batch
- “用户当前行为要立刻影响体验”：优先 streaming
- “实时先动作，最终要可审计”：streaming + batch 校准
- “只是想看起来先进”：先不要 streaming

## 关联

- [[../06-Maps/Batch Streaming 判断图|Batch Streaming 判断图]]
- [[数据生命周期与 Data Lifecycle]]
- [[大数据决策导航]]

