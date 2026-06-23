---
title: Photon Fusion 与 Realtime
type: system
status: learning
created: 2026-03-28
updated: 2026-03-28
---

# Photon Fusion 与 Realtime

## 这套系统在行业里代表什么

`Photon Fusion` 代表的是“实时联机这件事，真的要单独认真做”的路线。

它解决的是：

- network topology
- state replication
- spawning / simulation
- host / shared / dedicated server 模式选择

这和 `UGS`、`PlayFab` 的重点不同。它更像：

- real-time gameplay runtime
- 联机层的核心技术底座

## 为什么这页对你重要

你们当前做 `skills gaming hackathon`，最容易高估的一件事就是：

- 认为“1v1 对战”就一定要上复杂实时同步

但 `Photon` 文档其实反过来提醒我们：

- 网络拓扑要尽早选
- 不同模式会改变代码和信任边界
- host/client 模式更便宜，但信任性更弱

这对 `skills gaming` 尤其关键，因为：

- 如果公平性是核心卖点
- 你就不能随便接受一个不可信的 host 作为真相来源

## 从官方资料里最重要的 3 个判断

### 1. Topology choice 很早就要定

`Fusion` 明确区分：

- dedicated server
- client host
- shared authority

这不是部署细节，而是玩法和信任模型的一部分。

### 2. Client Host 便宜，但 trust 更弱

这很适合 demo、轻联机、快速验证。

但如果你做的是：

- skill competitions
- money-adjacent fairness claims
- 需要解释胜负的系统

那么 host trustworthiness 会直接变成产品问题。

### 3. Single / async / pseudo-competitive 往往更适合第一版

对你们当前场景，最稳的路径通常还是：

- 单人 run
- 服务端收分
- 异步匹配或排行榜对比
- 用 competition shell 讲清楚竞争感

而不是一上来做复杂实时 PvP。

## 一句判断

`Photon Fusion` 非常值得学，但它更像你“理解实时游戏的正确边界”的老师，
而不一定是这次 `skills gaming` demo 的默认首选。

## 关联

- [[../05-Topics/前沿游戏技术全景：AI、LiveOps、Realtime 与创作者工具|前沿游戏技术全景：AI、LiveOps、Realtime 与创作者工具]]
- [[../05-Topics/Session Pacing、Replayability 与 Skill Expression|Session Pacing、Replayability 与 Skill Expression]]
- [[Tournament、Matchmaking 与 Fairness]]
- [[Score Submission、Fairness Validation 与 Replayability]]
- [[../10-Projects/Hackathon Game/推荐方向：Word Sprint Duel V1|推荐方向：Word Sprint Duel V1]]

## 资料

- [Fusion 2 Network Topologies](https://doc.photonengine.com/fusion/current/manual/network-topologies)
- [Fusion 2 Network Runner](https://doc.photonengine.com/fusion/current/manual/network-runner)
- [Fusion 2 Getting Started](https://doc.photonengine.com/fusion/current/tutorials/host-mode-basics/1-getting-started)
- [Fusion 2 What's New in 2.1](https://doc.photonengine.com/fusion/current/getting-started/preview-2-1/whats-new-2-1)
