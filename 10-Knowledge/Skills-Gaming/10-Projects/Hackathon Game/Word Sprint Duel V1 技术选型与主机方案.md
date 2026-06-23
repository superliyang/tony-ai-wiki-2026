---
title: Word Sprint Duel V1 技术选型与主机方案
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Word Sprint Duel V1 技术选型与主机方案

## 推荐主方案

### Client

- `Unity`
- 2D UI-first 实现
- `TextMeshPro`
- 最少动画、最少特效、最少状态分支

### Backend

- `FastAPI`
- 简单 REST API
- 内存态或轻量持久化都可接受
- 目标是把 score submission、result shaping、event logging 跑通

### Data / Logging

- 先以 append-only 事件流思路设计
- demo 阶段可先写本地文件、SQLite 或轻量表
- 不需要一开始就上完整 analytics stack

### AI Production Stack

- `Google AI Studio / Gemini`：brief、规则解释、文案、任务拆分
- `Imagen`：UI 风格探索与宣传素材
- `TTS`：tutorial host、announcer
- `Veo`：pitch trailer

## 为什么我推荐这条主方案

因为它最适合你现在的组合能力：

- 你对系统、接口、事件链路敏感
- 你不需要先把引擎生态玩到最深
- 你更需要一条能稳定做出 demo 的路线

`Unity + FastAPI` 的好处是：

- 客户端表现足够像游戏
- 服务端逻辑足够好讲清
- score、result、logging、eligibility 这些你擅长的链路可以自然落地

## 不推荐的 V1 路线

### 不建议重做复杂后端平台

- 不做完整 tournament platform
- 不做真钱 wallet
- 不做复杂 anti-cheat service
- 不做实时 multiplayer

### 不建议重押复杂 AI NPC

- 不要让 `ACE / Inworld / Convai` 进入核心 duel loop
- 它们最多做 host / guide / announcer shell

## 备选方案

### 备选 A：Web-first

如果团队对 Unity 很不熟，备选可以是：

- `Phaser` 或轻量 web game stack
- `FastAPI` backend
- 更快做出玩法 proof

代价是：

- 成品观感可能没那么像移动游戏
- 后续迁到 app/game shell 的距离更远

### 备选 B：Roblox-first

如果团队本来就在 Roblox 生态，可以考虑：

- `Roblox Studio Assistant`
- built-in `MCP`
- 更 agentic editor workflow

但这条更像平台/生态选择，不一定适合当前赛道目标。

## 结论

默认主机方案就定成：

- `Unity client`
- `FastAPI backend`
- `simple event/log store`
- `Google AI Studio` 负责创作提效

## 关联

- [[Word Sprint Duel V1 实现蓝图]]
- [[Word Sprint Duel V1 客户端、服务端与数据任务拆分]]
- [[Word Sprint Duel V1 埋点、结果解释与公平性最小方案]]
