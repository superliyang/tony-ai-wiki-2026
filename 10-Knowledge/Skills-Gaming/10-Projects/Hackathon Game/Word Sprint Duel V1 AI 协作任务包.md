---
title: Word Sprint Duel V1 AI 协作任务包
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Word Sprint Duel V1 AI 协作任务包

## 可以交给 AI 的任务

### 1. 玩法与文案

- tutorial copy
- end-of-match copy
- qualifier copy
- store / pitch copy

### 2. 美术与界面

- UI direction board
- color tokens
- card / tile / word-cell variants
- result screen composition

### 3. 工程

- mock API definitions
- event schema
- frontend state transitions
- QA checklist

### 4. Pitch

- one-page brief
- 3-minute demo narration
- product comparison against existing portfolio patterns

## 不建议完全交给 AI 的任务

- final game feel judgment
- final fairness judgment
- final scope cuts
- final product positioning call

## 推荐 AI 工具组合

- `Google AI Studio / Gemini`: brief、文案、规则解释、QA checklist
- `Imagen`: UI 风格探索、活动图、icon 方向
- `TTS`: tutorial host、announcer
- `Veo`: 8s-30s pitch trailer
- `Unity AI / Roblox Assistant`: only if the implementation host is Unity or Roblox
- `ACE / Inworld / Convai`: optional only, for host / guide / NPC shell, not core duel logic

## 工具分工建议

- `Cursor`: Unity 客户端主实现
- `Claude Code`: FastAPI、事件、日志、脚本和文档整理
- `Codex`: 可异步处理测试、文档、非阻塞修复任务
- `Google AI Studio`: copy、素材、语音、trailer
- `ACE / Inworld / Convai`: 仅做可选壳层参考，不进入核心 duel 判定
