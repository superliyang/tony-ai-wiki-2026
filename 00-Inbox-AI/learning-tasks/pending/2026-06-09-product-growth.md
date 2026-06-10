---
date: 2026-06-09
track: 产品思维
type: growth-learning-package
status: pending-review
sources: exa-search
---

# 产品思维：从问题出发，而非从方案出发

## 今日产品主题

**"用户说想要 A，但真正付费的是 B"——产品决策中的「四层欲望」与「问题驱动」双重框架**

当代产品管理面临两个根本性扭曲：
1. **方案前置**：AI 狂热让团队从「我们有什么技术」出发找问题，而非从问题出发找方案
2. **数据幻觉**：把用户说的（Layer 1 陈述偏好）当成用户会做的（Layer 4 行为偏好）来做决策

这两个扭曲叠加，导致 95% 的 AI 产品试点零业务影响（MIT 2025 研究），以及无数「用户调研说会买、上线后无人付费」的产品死亡案例。

---

## 为什么值得学

Tony 正在构建的是「AI First 知识操作系统」——一个同时涉及 AI 技术和用户行为设计的复杂产品。这个领域最容易掉进的坑正好就是这两个：

- **方案前置陷阱**：因为「AI First」这个定位，自然倾向从 AI 能力倒推功能，而非从知识工作者的真实痛点出发
- **用户反馈失真陷阱**：知识管理工具的用户「说想要」的和「实际用的」往往差距巨大（每个人都说要整理知识，实际用的功能可能是快速搜索和粘贴）

这篇文章的三篇核心来源分别覆盖了这两个陷阱的诊断和解法。

---

## 3 个核心概念

### 概念 1：问题驱动五步法（Problem-First Framework）

**来源**：Tim Feeley (Chrome Enterprise PM), "The Problem-First PM in a Solution-First Era"

产品决策的正确顺序：

```
1. Personas  → 具体的人 + 具体任务 + 具体约束（不是市场细分标签）
2. Problems  → 他们在工作流中哪里断裂？做不了什么？什么太慢？
3. Evidence  → 数据证明问题存在（不是销售电话里的 anecdote）
4. Impact    → 解决后对用户和业务分别值多少？
5. Hypotheses → 可测试的多种方案（AI 只是其中一种候选）
```

关键洞察：**AI 应该在第 5 步出现，而不是第 1 步。** 前 4 步的输出可能是「不需要 AI，删掉一个界面就行」。

### 概念 2：用户欲望四层模型（Four Layers of Desire）

**来源**：Yu-kai Chou (Octalysis 框架创始人), "Why Do User Surveys Lie?"

| 层级 | 定义 | 准确度 | 获取方式 |
|------|------|--------|----------|
| Layer 1 | 用户告诉你的 | ~20% | 问卷/访谈第一回答 |
| Layer 2 | 用户以为自己想要的 | 仍不匹配行为 | 真诚自我报告 |
| Layer 3 | 用户真正想要的 | 高但不完整 | 深度追问（4 层 why） |
| Layer 4 | 用户实际花时间/钱做的事 | 唯一可靠信号 | 行为观察/数据分析 |

**核心机制**：陈述偏好不需要付出代价（CD8 Loss & Avoidance 不激活），实际行为需要付出真金白银/时间/注意力——这个「代价不对称」是 Layer 1 和 Layer 4 永远不一致的根本原因。

> 「问卷不问你是否愿意每天花 3 小时点击虚拟奶牛，因为你会说 '你把我当什么人？' 但 FarmVille 巅峰 8000 万 MAU 就是这么干的。」

### 概念 3：北极星指标的欺骗性（North Star Metric Pitfalls）

**来源**：Vestd / FounderMetrics, "North Star Metrics That Don't Mislead"

判断一个指标是不是「虚荣指标伪装成北极星」的三条规则：

1. **「不用改善用户体验就能提升」→ 危险指标**。注册数、下载量、页面浏览都属于这一类
2. **北极星应该随阶段变化**——种子期的好指标在规模化阶段可能是毒药
3. **好北极星让领导层不舒服**——如果你的北极星从不挑战你的假设，它大概率没在工作

实战测试：
> 如果这个数字上升了，用户真的变得更好吗？
> 这个指标能不能在不改善产品的情况下提升？
> 它帮团队决定「不做什么」吗？
> 一年后它还重要吗？

---

## 1 个真实案例

### FarmVille 悖论——问卷数据粉碎机

**背景**：2009 年 Zynga 推出的社交农场游戏

**如果只靠问卷**：
- 问：「你会每天花 3 小时点击虚拟奶牛吗？」→ 几乎 100% 回答「不会，你当我傻吗」
- 问：「你会花真钱买不存在的虚拟谷仓吗？」→ 回答者觉得被冒犯
- 结论：这个产品不该做。数据验证完毕。

**实际结果**：
- 巅峰 8000 万+ 月活用户
- 大量用户日均 3-4 小时在线
- 可观的虚拟物品付费转化

**为什么问卷全错了**：
Layer 1 的自我形象（「我不是那种浪费生命的人」）和 Layer 4 的实际行为（晚上 9:37 疲惫地回家，点击奶牛是大脑最解压的事）是同一个人的两个版本。两者都真实——但只有 Layer 4 驱动行为。

**产品启示**：用户调研的价值不在「听他们说什么」，而在「看他们已经在用什么 workaround 解决问题」。如果用户已经在用丑陋低效的方式做某件事，那就是真实需求——比任何问卷都可靠。

---

## 1 个反直觉点

### 「数据驱动」可能是最大的产品陷阱

**反直觉事实**：拥有大量用户数据（问卷、NPS、访谈记录）的产品团队，反而更容易做出错误决策——不是因为数据不够，而是因为大多数数据只捕捉了 Layer 1（用户说的），但团队把它当作 Layer 4（用户做的）来使用。

**Yu-kai Chou 的诊断公式**：
> 如果你的数据活在 CD1（史诗意义/使命感）领域——比如「95% 的人说环保很重要」——那它告诉你的只是「什么是社会可接受的宣称」。如果它活在 CD8（损失规避）领域——比如「15% 的人愿意为环保多付钱」——那它告诉你的是「人们真正会为什么付钱」。这两个答案几乎不可能来自同一个人。

**实践含义**：
- 「我们有数据」是最危险的产品决策前缀——如果数据是 Layer 1 的话
- 做决定前先问：这个数据来自哪一层？对应的行为数据在哪里？
- 一个 50 人的行为观察 > 1000 份问卷

---

## 和 Tony 工作连接

**AI 知识 OS 的直接应用**：

1. **Inbox → Wiki 的 promote 流程**：当前设计中，Hermes 推荐 → Tony 审阅 → Codex 结晶。这个过程最该优化的不是「更多 AI 功能」，而是——Tony 在审阅环节的真实摩擦是什么？是阅读速度？判断成本？上下文缺失？这些才是问题驱动的起点。

2. **Agent-memory 系统的指标选择**：当前用什么衡量这个知识 OS 是否「好用」？如果是「AI 生成了多少内容」→ 这是 Layer 1 虚荣指标。真正的 Layer 4 北极星可能是「Tony 完成一次知识检索并做出决策的时间缩短了多少」。

3. **用户即设计师**：Tony 既是这个产品的用户也是设计者——这意味 Layer 1（你觉得你想要什么功能）和 Layer 4（你实际每天怎么用这个系统）的撕裂风险最大。需要刻意用行为观察替代自我报告。

---

## 可实践小动作

**本周可做的一件事**：

打开你的 Obsidian，花 10 分钟记录：
> 「过去一周，我在这个知识系统中做的最频繁的 3 个操作是什么？」
> 「有没有哪个操作，我用了一个丑陋的 workaround（比如手动复制粘贴到某个地方）？」
> 「有没有功能是我'以为会用的'但实际一次都没用过？」

这三个问题的答案就是你自己的 Layer 4 数据——比你对自己产品偏好的任何「想法」都更可靠。如果发现 workaround，那就是下一个功能该解决的问题。

---

## 是否建议 Codex 深挖

**建议，方向如下**：

1. **四层欲望模型 × Octalysis** → 深挖 Yu-kai Chou 的 Octalysis 框架（8 个核心驱动力），产出「AI 知识 OS 的 Core Drive 诊断报告」——当前系统在 CD2（成就感）、CD4（所有权）、CD8（损失规避）上的设计是怎样的？

2. **North Star 审计** → Codex 审计当前 agent-memory / review-queue 系统的指标，判断哪些是 Layer 1 虚荣指标，提出一个阶段匹配的北极星指标草案。

3. **Problem Statement 练习** → 用 Tim Feeley 的四要素格式（persona + task + blocker + evidence），为「Tony 的知识管理」写 3 个真实的问题陈述。

---

## 来源 URL

1. Tim Feeley, "The Problem-First PM in a Solution-First Era" (2026-03-07)
   https://timfeeley.com/the-problem-first-pm-in-a-solution-first-era/

2. Yu-kai Chou, "Why Do User Surveys Lie? The 4 Layers of Desire" (2026-04-19)
   https://yukaichou.com/gamification-analysis/four-layers-of-desire-why-user-surveys-lie/

3. Vestd / Graham Charlton, "North Star Metrics That Don't Mislead" (2025-12-22, updated 2026-01-09)
   https://www.vestd.com/blog/north-star-metrics-that-dont-mislead

4. LogRocket / Raluca Piteiu-Apostol, "Feature Factory vs. Product Discovery: A 3-Lens Framework for PMs" (2026-04-22)
   https://blog.logrocket.com/product-management/product-discovery-framework-pms/

5. Chris Spiek, "Workarounds as Evidence of Real Need" (2026-03-07)
   https://chrisspiek.substack.com/p/workarounds-as-evidence-of-real-need

6. Paul Syng, "Why What Your Company Sells Doesn't Match What Customers Actually Buy" (2026-03-05)
   https://paulsyng.com/blog/sell-vs-buy-gap/

7. Amplitude, "What Makes a Good vs Bad North Star Metric" (2024-08-15)
   https://amplitude.com/blog/good-bad-north-star-metric
