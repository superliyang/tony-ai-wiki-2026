---
title: Codex 异步并行任务包
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Codex 异步并行任务包

## 适合交给 Codex 的任务

### 1. QA checklist

- tutorial walkthrough checklist
- score submit failure checklist
- result explanation sanity checklist

### 2. 文档与 release materials

- README polish
- demo script
- change summary
- review checklist

### 3. 非阻塞脚本

- event schema validator
- mock payload generator
- local data seeding script

### 4. 结构化复盘

- 哪些系统是 V1 真做
- 哪些系统是接口占位
- 哪些争议点已经被覆盖

## 使用原则

- 不把阻塞主线的核心玩法判断交给它
- 不把最终公平性定义交给它
- 适合做 sidecar / async worker

## 关联

- [[AI Coding Tools 选型与协作分工]]
- [[Word Sprint Duel V1 AI 协作任务包]]
