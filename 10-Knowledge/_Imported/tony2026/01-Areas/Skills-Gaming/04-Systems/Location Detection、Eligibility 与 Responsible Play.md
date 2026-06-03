---
title: Location Detection、Eligibility 与 Responsible Play
type: topic
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Location Detection、Eligibility 与 Responsible Play

## 为什么这页属于系统层

因为这不是纯政策文档，而是必须被做成系统能力：

- eligibility check
- region / game-type gating
- VPN / ISP / GPS edge cases
- support escalation
- self-exclusion and account controls

## 从产品到系统要落什么

### 1. Location eligibility

系统至少要判断：

- 当前位置是否允许 cash play
- 当前游戏类型是否允许
- 当前赛事类型是否允许

### 2. Risk and support workflow

如果玩家被错误拦截：

- 是否能解释原因
- 是否有 support channel
- 是否有 manual review / investigation path

### 3. Responsible play controls

- self-exclusion
- play limits
- behavior review / intervention
- safe messaging and support handling

## 对 hackathon 的建议

V1 不必真的做完整合规系统，但应该在架构和产品里预留：

- eligibility state
- tournament eligibility response
- clear unsupported-region messaging
- support / dispute placeholder flow

## 关联

- [[Tournament、Matchmaking 与 Fairness]]
- [[Wallet、Payout、Risk 与 Anti-Cheat]]
- [[../05-Topics/欧美市场的合规边界与平台约束|欧美市场的合规边界与平台约束]]
