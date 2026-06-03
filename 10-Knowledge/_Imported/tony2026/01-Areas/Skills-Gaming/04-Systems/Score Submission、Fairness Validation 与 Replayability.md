---
title: Score Submission、Fairness Validation 与 Replayability
type: topic
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Score Submission、Fairness Validation 与 Replayability

## 为什么这是 skills gaming 的技术核心

在普通休闲游戏里，score 只是结果。
在 `skills gaming` 里，score 是产品信任的一部分。

## 从 Skillz 官方文档最值得学什么

### 1. score submission 要进入主流程，而不是可有可无

`Skillz` 文档强调：

- 比赛结束后要尽快提交最终 score
- score submission 不应该依赖玩家额外操作才能继续流程

这说明：

- 结果提交本身就是核心 loop 的一部分
- 不能把它做成“顺手上报一下”

### 2. fairness 要在技术上可验证

`Skillz` 的 `Random and Fairness` 文档强调：

- 同一场比赛里的随机数序列必须对双方一致
- fairness 不是口头承诺，而是 runtime 行为约束

### 3. anti-cheat 不是只靠服务端

`Skillz` 官方 anti-cheating 文档提到：

- 运行时内存修改
- duplicated values / consistency checks
- gameplay variables tampering

这意味着：

- 客户端也必须有自校验思路
- 服务端也要有审计和异常检测思路

## 对 hackathon 的最实用做法

V1 可以这样：

- 明确 score 只由少量核心变量组成
- 结果页前就完成 score submission
- 保留一份可回放或可解释的 match summary
- 对明显异常值做简单 sanity check

## 关联

- [[Tournament、Matchmaking 与 Fairness]]
- [[Wallet、Payout、Risk 与 Anti-Cheat]]
- [[../05-Topics/Skills Game 技术架构主线|Skills Game 技术架构主线]]

## 资料

- [Skillz Set Up Core Loop and Gameplay](https://docs.skillz.com/docs/play-and-compare-gameplay/)
- [Skillz Random and Fairness](https://docs.skillz.com/docs/2025.0.19/randomness/)
- [Skillz Anti-Cheating Techniques](https://docs.skillz.com/docs/anti-cheating-techniques-overview/)
- [Skillz Brick Breaker Example](https://docs.skillz.com/docs/29.2.22/brick-break-example/)
