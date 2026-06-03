---
title: Claude Code 后端与事件链路任务包
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Claude Code 后端与事件链路任务包

## 使用方式

把它当成后端和 repo-level worker 的任务包。

## Prompt 1：搭 FastAPI skeleton

目标：

- 建一个最小 `FastAPI` 服务
- 提供：`/tournament/current`、`/match/submit-score`、`/events`、`/result/{match_id}`、`/eligibility`

要求：

- 先保证接口 contract 清晰
- 不做真钱逻辑
- 不做复杂持久化

## Prompt 2：实现 score submit contract

目标：

- 定义 score payload
- 做最小 sanity checks
- 返回结果解释结构

要求：

- 规则尽量可解释
- 错误分支要清楚

## Prompt 3：实现 event ingestion

目标：

- 设计事件 schema
- 提供统一事件接收接口
- 支持最小 append-only 存储

要求：

- 先易于 demo 和调试
- 事件命名稳定

## Prompt 4：eligibility 与异常分支

目标：

- 做 unsupported region / placeholder eligibility response
- 明确 error shape
- 让客户端能展示清晰提示

## Prompt 5：文档与 contract 输出

目标：

- 生成接口说明
- 生成示例 payload
- 生成本地运行说明

## 关联

- [[Word Sprint Duel V1 技术选型与主机方案]]
- [[Word Sprint Duel V1 客户端、服务端与数据任务拆分]]
- [[Word Sprint Duel V1 埋点、结果解释与公平性最小方案]]
