---
title: GitHub 开源项目 Intake 工作流
type: workflow
status: active
created: 2026-04-03
updated: 2026-05-16
---

# GitHub 开源项目 Intake 工作流

## 目标

这个工作流用于把一个 GitHub 项目从“看到一个链接”转成“可判断、可复盘、可继续跟踪”的知识资产。

原则：

- 不按 star 数盲收
- 不抄 README
- 不只建项目卡，还要抽象模式
- 不把未验证项目直接放入长期 watchlist

## Step 1：初筛

先回答：

- 它解决什么问题
- 它属于哪一类：runtime、serving、agent、memory、eval、platform、security、developer tool
- 它是底座、壳层、平台还是子系统
- 最近是否仍在维护
- 是否有真实用户或生态位
- 是否和当前学习主线相关

如果这一步答不清，只放入临时候选，不建正式项目卡。

## Step 2：读仓库事实

至少看：

- README
- docs
- examples
- release / tags
- issues / discussions
- package / dependency
- tests
- license

记录事实时区分：

- repo 明确写的事实
- 自己的工程判断
- 尚未验证的推测

## Step 3：建项目卡

使用 [[../07-Templates/开源项目卡片模板|开源项目卡片模板]]。

项目卡必须回答：

- 它解决什么问题
- 为什么现在值得关注
- 它在 stack 的哪一层
- 核心组件与对象模型是什么
- 和相邻项目怎么区分
- 下一步实验怎么做
- 风险和边界是什么

## Step 4：抽象到上层

项目卡建完后，必须判断是否更新：

- 分类页
- 组织页
- 模式页
- 案例页
- 地图 / Canvas / Base
- Watchlist

如果只建项目卡，不抽象模式，这个项目很容易变成孤岛。

## Step 5：适配度打标

按 [[../04-Patterns/项目适配度标签说明|项目适配度标签说明]] 标记：

- `local_fit`
- `mac_fit`
- `production_fit`
- `learning_fit`

不要全部给 high。标签必须服务决策。

## Step 6：决定 watchlist

进入 watchlist 的条件：

- 主线相关
- 维护活跃
- 有持续变化
- 有学习或迁移价值
- 后续确实会复看

不进入 watchlist 的项目仍可保留项目卡，但不占用每周注意力。

## Step 7：设计最小实验

最小实验要明确：

- 本地是否能跑
- 输入是什么
- 输出是什么
- 如何判断成功
- 成本和风险是什么
- 需要记录什么 bad case

## Step 8：复盘和沉淀

复盘问题：

- 这个项目代表什么模式
- 是否值得深入源码
- 是否适合引入工作体系
- 是否需要和其他项目组合
- 是否要升级为 case study

如果研究方法有新的稳定偏好，可以交给 `self-improving-learning-ledger` 旁路沉淀。

## 输出物

- 项目卡
- 分类 / 组织 / 模式更新
- watchlist 判断
- 最小实验建议
- 风险边界

## 关联

- [[../07-Templates/开源项目卡片模板|开源项目卡片模板]]
- [[../07-Templates/组织卡片模板|组织卡片模板]]
- [[../03-Projects/项目索引|项目索引]]
- [[../09-Watchlist/重点 Watchlist|重点 Watchlist]]
