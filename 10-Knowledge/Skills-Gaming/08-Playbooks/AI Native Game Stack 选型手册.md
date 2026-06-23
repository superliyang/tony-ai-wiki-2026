---
title: AI Native Game Stack 选型手册
type: playbook
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# AI Native Game Stack 选型手册

## 原则

- 先决定玩法，再决定 AI
- 先决定 demo path，再决定 agent
- 先把 AI 用在提效层，再考虑用在 runtime 层

## 当前最稳的组合

### 一人 hackathon 默认组合

- `Google AI Studio`：策划、文案、素材、语音、宣传
- `Unity AI` 或 `Roblox Assistant`：如果主战场就在对应编辑器内
- `ACE / Inworld / Convai`：只作为 optional host / guide / NPC 参考，不强行塞进 V1

## 对 skills gaming 的特别提醒

这个赛道最先赢的从来不是“AI 最多”，而是：

- 最快理解玩法
- 最清楚公平性
- 最顺的结果反馈
- 最可信的比赛和奖励逻辑

## 关联

- [[../05-Topics/Game Agent、AI NPC 与创作助手|Game Agent、AI NPC 与创作助手]]
- [[../05-Topics/Google AI Studio 全家桶与一人游戏制作|Google AI Studio 全家桶与一人游戏制作]]
- [[../07-Templates/AI Stack Brief 模板|AI Stack Brief 模板]]
