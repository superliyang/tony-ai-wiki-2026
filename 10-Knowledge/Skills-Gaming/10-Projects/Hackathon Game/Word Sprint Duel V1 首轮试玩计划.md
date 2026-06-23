---
title: Word Sprint Duel V1 首轮试玩计划
status: learning
created: 2026-03-28
updated: 2026-03-28
---

# Word Sprint Duel V1 首轮试玩计划

## 目标

不是证明这款游戏已经完成，而是尽快回答 5 个最关键的问题：

1. 玩家 10 秒内能不能理解目标
2. 第一局能不能顺利打完
3. 输赢是不是“看起来公平”
4. 结果页能不能让人看懂并愿意再来一局
5. 哪些问题是玩法问题，哪些只是 UI / 文案问题

## 测试对象

建议至少找 3 类人：

- 完全不懂 `skills gaming` 的同事
- 懂休闲游戏但不懂你们项目的同事
- 会从系统和公平性角度挑问题的人

## 每轮最少样本

- 快速内测：`5-8` 人
- 第一轮结构化反馈：`8-12` 人

## 试玩脚本

### Step 1：只给一句介绍

- “这是一款短局对战型单词技能游戏，你要尽快完成并获得更高分。”

不要先解释太多规则。

### Step 2：观察首局

只看：

- 是否迷路
- tutorial 哪里卡
- 是否能顺利开始
- 是否能打完第一局

### Step 3：看结果页

问 3 个问题：

- 你知道自己为什么赢/输吗
- 你知道怎么做得更好吗
- 你想不想马上再来一局

### Step 4：补充问答

- 哪一步最困惑
- 哪一刻最爽
- 哪一刻最不服
- 如果只改一件事，应该改什么

## 必记指标

- `tutorial_start`
- `tutorial_complete`
- `match_start`
- `match_end`
- `result_received`
- `rematch_clicked`
- `submit_error`

## 手工观察指标

- 10 秒理解率
- 首局完成率
- 结果理解率
- 愿意重赛比例
- 最大困惑点分布

## 第一轮成功标准

- 至少 `70%` 的人能独立完成第一局
- 至少 `60%` 的人能说清楚输赢原因
- 至少一半的人愿意点击 `再来一局`
- 没有出现明显“这像运气不是 skill”的集中反馈

## 第一轮之后只做 3 类修改

- onboarding clarity
- result explainability
- pacing / penalty / CTA

不要第一轮就大改核心玩法。

## 关联

- [[Word Sprint Duel V1 埋点、结果解释与公平性最小方案]]
- [[Word Sprint Duel V1 参数、词库与节奏调优表]]
- [[Word Sprint Duel V1 首轮试玩复盘]]
- [[../../05-Topics/Game Feel、Onboarding 与 First Match Design|Game Feel、Onboarding 与 First Match Design]]
