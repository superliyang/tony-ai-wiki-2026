---
title: "Single Bot Discussion Setup"
created: 2026-06-15
updated: 2026-06-15
status: draft
source: codex
---

# Single Bot Discussion Setup

已确定先采用：

```text
1 个 Feishu bot
+ discussionmoderator profile
+ 群内角色标签输出
```

## 当前定义

- Hermes 原生 profile：
  - `discussionsignaler`
  - `discussionengineer`
  - `discussionoperator`
  - `discussionstrategist`
  - `discussionmoderator`
- 群内可见角色名：
  - `信号员 Hermes`
  - `工程师 Hermes`
  - `运营官 Hermes`
  - `策略官 Hermes`
  - `主持人 Hermes`

## 运行方式

执行入口见：

- [[90-Agent-System/scripts/hermes-single-bot-discussion]]

## 当前结论

- 先不用多 bot。
- 先验证讨论质量。
- 先不要接 cron。
- 第一轮更适合半人工触发。
