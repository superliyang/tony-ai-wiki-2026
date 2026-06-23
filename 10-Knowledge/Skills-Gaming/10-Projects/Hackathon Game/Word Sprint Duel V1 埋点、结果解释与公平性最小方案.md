---
title: Word Sprint Duel V1 埋点、结果解释与公平性最小方案
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Word Sprint Duel V1 埋点、结果解释与公平性最小方案

## 目标

不是做完整 anti-cheat 平台，而是做一个：

- 能解释结果
- 能回看关键过程
- 能处理最明显争议

的最小闭环。

## Score 设计原则

- 核心变量少
- 规则简单
- 输赢原因能一句话说清
- 同一局面下不会出现不一致结论

## Result Explanation

结果页至少应该解释：

- 总分
- 关键得分来源
- 输赢差距
- 是否命中 penalty / bonus

## Fairness 最小方案

### 1. 固定内容池

同一对局双方使用相同题库或相同生成条件。

### 2. 规则固定

- 相同规则
- 相同时间限制
- 相同 scoring formula

### 3. 提交一致性检查

- score 不能超出合理上限
- session duration 不能明显异常
- 关键字段不能为空

## Dispute 最小方案

V1 至少能回答：

- 我为什么输
- 我的分数是怎么来的
- 为什么我不能参加
- 为什么提交失败

## 必埋事件

- `match_start`
- `match_end`
- `score_submitted`
- `score_submit_rejected`
- `result_received`
- `eligibility_denied`
- `client_exception`

## Demo 讲解时最该强调什么

- 我们不是只做了一个小游戏
- 我们还做了结果可解释性
- 我们知道争议会出现在哪里
- 我们提前设计了最小信任闭环

## 关联

- [[Word Sprint Duel V1 客户端、服务端与数据任务拆分]]
- [[../../04-Systems/Score Submission、Fairness Validation 与 Replayability|Score Submission、Fairness Validation 与 Replayability]]
- [[../../04-Systems/Event Logging、Analytics 与 Experiment Hooks|Event Logging、Analytics 与 Experiment Hooks]]
