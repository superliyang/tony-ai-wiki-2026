---
title: Cursor Unity 客户端 Prompt 包
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Cursor Unity 客户端 Prompt 包

## 使用方式

把下面 prompt 按阶段喂给 `Cursor`，每次只做一个 chunk。

## Prompt 1：搭客户端骨架

目标：

- 用 `Unity` 做一个 2D UI-first 的 skills game prototype
- 建立这些页面：start、tutorial、match、result
- 用最简单的状态机串起来

要求：

- 先做最小可运行版本
- 不做复杂动画
- 不做真钱逻辑
- 所有 API 调用先留接口层
- 所有状态切换要清楚可读

验收：

- 30 秒内能进入第一局
- tutorial -> match -> result 路径完整

## Prompt 2：实现 duel state machine

目标：

- 建一个清晰的客户端状态机：`idle`、`tutorial`、`playing`、`submitting`、`result`、`error`
- 每个状态的进入/退出要明确
- 为后续 score 和 API 调用留出 hook

要求：

- 状态机代码要容易读
- UI 更新和状态切换分离

## Prompt 3：实现最小 score 与 result UI

目标：

- 把 score calculation 接到 result screen
- 结果页显示总分、差距、关键得分来源
- 明确保留 result explanation 区域

要求：

- score 规则先保持简单
- 结果页重点是可解释而不是华丽

## Prompt 4：埋客户端事件

目标：

- 统一发出事件：`session_start`、`tutorial_complete`、`match_start`、`match_end`、`score_submitted`、`result_received`、`submit_error`
- 保证事件结构统一

要求：

- 事件结构独立成一层
- 便于后续接入服务端和分析

## Prompt 5：UI polish

目标：

- 保持风格一致
- 优化 onboarding、result hierarchy、CTA 清晰度
- 不改变核心 loop

要求：

- 优先修信息层级，不优先加花哨效果

## 关联

- [[Word Sprint Duel V1 技术选型与主机方案]]
- [[Word Sprint Duel V1 客户端、服务端与数据任务拆分]]
- [[Word Sprint Duel V1 埋点、结果解释与公平性最小方案]]
