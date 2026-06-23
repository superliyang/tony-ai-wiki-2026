---
title: 经济、奖励与 Progression 设计
type: topic
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# 经济、奖励与 Progression 设计

## 这页为什么关键

前面我们已经把：

- 市场
- 玩法
- 合规边界
- 技术架构

都铺开了。

接下来真正决定“玩家会不会回来、产品能不能长出来”的，是：

- rewards 怎么给
- progression 怎么体现
- event cadence 怎么组织

## 从官方动作里提炼出的 3 条经济设计主线

### 1. `Skillz`：真钱不是默认开启，而是增长后的 milestone

从 `Unlock Real Prizes` 和 `Currency Modes` 看，`Skillz` 的逻辑是：

- 先有 free / virtual-currency competition
- 再看 DAU、对战量、skill algorithm、quality 等门槛
- 达到条件后才可能 unlock real prizes

这对你很重要，因为它说明：

- 真实奖励不是玩法的起点，而是产品验证后的升级层
- 对 hackathon 来说，最合理的是把 reward architecture 讲清楚，而不是一上来真做真钱

### 2. `WorldWinner`：loyalty、progressive payout、club 分层是真正的 retention 机器

从 `Lifetime Rewards`、`Progressive Payouts`、首页上的 `Premier Club` 看：

- 奖励系统本身就是 meta loop
- 奖励不只是现金，还包括 rewards points、tiers、club 身份感
- payout 的 framing 会影响 excitement，而不是只是影响经济数值

### 3. `Papaya`：大赛和晋级叙事会把日常对局放大成长期目标

`World Solitaire Championship` 最值得学的是：

- 日常 app 内比赛可以通向更大的 live event 或高荣誉事件
- progression 不一定只靠等级，也可以靠 qualifier path、ticket、championship ladder

## 对 hackathon 最有用的 4 层设计

### 1. Session reward

一局结束给什么反馈：

- score
- rank
- improvement delta
- streak / momentum

### 2. Daily progression

今天回来有什么目标：

- daily challenge
- qualifier
- streak reward
- mission goal

### 3. Meta reward

长期玩下去获得什么：

- loyalty points
- tiers
- badge / club status
- unlockable cosmetic or prestige markers

### 4. Championship narrative

为什么这不只是重复刷局：

- seasonal ladder
- monthly finals
- special event
- championship qualification

## 对你们这次项目最稳的经济建议

### 应该做的

- 先做一种清楚的单局奖励反馈
- 加一个轻量 daily goal 或 qualifier 概念
- 在 pitch 里讲出长期 progression 的想象空间

### 不应该做的

- 一上来做复杂货币体系
- 一上来做太多可兑换资产
- 一上来做强真钱承诺

## 一句最关键的判断

对 hackathon 来说，最好的经济设计不是“复杂”，而是：

- 让玩家看懂为什么现在继续玩、明天还会来、未来还有更高层目标

## 关联

- [[留存、LiveOps 与用户获取]]
- [[Prize Framing 与 Reward Psychology]]
- [[../09-Concepts/最终 shortlist：推荐方向与原因|最终 shortlist：推荐方向与原因]]
- [[../10-Projects/Hackathon Game/项目总览|Hackathon Game]]

## 资料

- [Skillz Unlock Real Prizes](https://docs.skillz.com/docs/unlock-real-prizes/)
- [Skillz Currency Modes](https://docs.skillz.com/docs/28.0.17/skillz-currency-modes/)
- [WorldWinner Lifetime Rewards](https://corp.worldwinner.com/lifetime-rewards/)
- [WorldWinner Progressive Payouts](https://corp.worldwinner.com/introducing-progressive-payouts/)
- [Papaya World Solitaire Championship](https://www.papaya.com/world-solitaire-championship)
