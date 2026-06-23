---
title: Word Sprint Duel V1 实现蓝图
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Word Sprint Duel V1 实现蓝图

## 产品结构

### Client

- start screen
- tutorial / onboarding
- single duel session
- result screen
- daily qualifier progress bar

### Backend Placeholder

- tournament metadata API
- score submission API
- result shaping API
- event logging endpoint
- unsupported-region placeholder response

### Data Layer

- session_start
- session_end
- score_submitted
- qualifier_progress_updated
- unsupported_region_seen

## 技术重点

- score 结构要尽量简单可解释
- result 反馈要快
- logging 要够清楚，方便 demo 和复盘
- 所有高风险真钱相关能力都只留接口，不在 V1 真做

## 验收标准

- 玩家 30 秒内能开始第一局
- 一局结束后结果明确
- 能讲清 skill 是什么
- 能讲清未来怎么扩 reward / qualifier / liveops
