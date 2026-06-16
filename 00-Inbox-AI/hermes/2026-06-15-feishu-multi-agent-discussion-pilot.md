---
title: "飞书多 Agent 讨论组试点方案"
created: 2026-06-15
updated: 2026-06-15
status: proposal
author: codex
tags:
  - feishu
  - hermes
  - multi-agent
  - discussion
  - proposal
---

# 飞书多 Agent 讨论组试点方案

这个方案的目标不是“再造一个知识库”，而是先做一个：

```text
多 Agent 讨论层
-> Tony 追问 / 判断
-> Hermes 收口
-> Codex 只在需要时结晶
```

## 一句话定义

飞书群负责：

- 多视角讨论；
- 快速碰撞；
- 暂时性判断；
- Tony 主动提问；
- 决定是否值得进入正式学习/项目/入库流程。

Obsidian 负责：

- 审核后的长期知识；
- 结构化地图；
- playbook / project / canonical note。

## 试点结构

先从 **4 个角色 Agent + 1 个收口 Agent** 开始。

### 1. `Scout`

职责：

- 抛出新信号；
- 解释“发生了什么”；
- 给出原始来源；
- 不负责下结论。

最常见开场：

```text
今天发现一个值得讨论的信号：
- 它是什么
- 来源是什么
- 为什么可能重要
```

### 2. `Engineer`

职责：

- 从技术实现角度判断；
- 解释难点、可行性、系统影响；
- 回答“值不值得深挖 / 做实验 / 改架构”。

最常见问题：

- 这东西技术上新在哪里？
- 如果接到 Tony 系统里，最先碰到什么难点？
- 它和已有方案相比到底强在哪？

### 3. `Operator`

职责：

- 从流程、维护、风险、可靠性、依赖、长期运维角度判断；
- 回答“做出来之后会不会很麻烦”。

最常见问题：

- 运行成本如何？
- 会不会引入新的 review / 安全 / 维护负担？
- 这件事更像 demo、能力补丁，还是长期系统能力？

### 4. `Strategist`

职责：

- 从 Tony 的长期能力建设、路径选择、优先级角度判断；
- 回答“这件事对 Tony 值不值得”。

最常见问题：

- 它对 Tony 的核心主线有什么帮助？
- 这是短期热点，还是长期能力资产？
- 现在该 `watch`、`study`、`build` 还是 `ignore`？

### 5. `Moderator`

职责：

- 不参与内容辩论；
- 控制轮次；
- 防止复读；
- 最后做 5 行收口。

这个角色最适合由 Hermes 承担。

## 推荐的发言顺序

不要让所有 Agent 自由抢话。

建议固定成：

```text
Scout 开题
-> Engineer 技术判断
-> Operator 落地风险
-> Strategist 优先级判断
-> Tony 追问 / 插话 / 质疑
-> Moderator 收口
```

## Hermes 应该怎么接

Hermes 不应该扮演“所有 Agent 的大脑”，而应该扮演：

```text
主持人 + 调度器 + 讨论结果收口器
```

也就是 Hermes 主要负责三件事：

1. 触发讨论
2. 控制轮次
3. 把讨论结果写回 `00-Inbox-AI/`

## 与 Hermes 的结合方式

### 模式 A：Hermes 发现信号，主动发起群讨论

链路：

```text
curated-scout / signals
-> Hermes 选 1 个高信号
-> 发到飞书群
-> 按角色顺序组织 3-4 轮回应
-> Moderator 收口
-> 写一个轻量讨论记录到 00-Inbox-AI/
```

适用：

- 每天 1 次以内；
- 只挑最高价值信号；
- 避免把群刷成新闻播报。

### 模式 B：Tony 在飞书群里直接提问

链路：

```text
Tony 提问
-> Hermes 先做 task intent routing
-> 判断这是 discussion / learning / project / publish 哪一类
-> 如果是 discussion
   -> 拉起多 Agent 讨论
   -> Moderator 收口
-> 如果是 executable work
   -> 转 task-intent / codex-request
```

适用：

- 你自己抛一个技术或判断问题；
- 希望大家先辩，不急着立刻入库。

## 群聊后的收口格式

我建议固定成一个非常短的结构。

```text
结论：
- relevance: high / medium / low
- action: watch / study / build / ignore
- why: 一句话
- next step: 一句话
- codex needed: yes / no
```

## 建议写回的位置

群聊内容本身不要默认入库。

推荐只写一个收口 note 到：

```text
00-Inbox-AI/hermes/discussion-summaries/YYYY-MM-DD-topic.md
```

如果当前还没有这个目录，可以先临时写到：

```text
00-Inbox-AI/hermes/
```

## 什么情况下转下游

### 转 `learning-tasks/pending/`

当满足：

- 有明确学习价值；
- 不是一时热点；
- 值得 Codex 做 package。

### 转 `codex-requests/pending/`

当满足：

- 这是一个可执行动作；
- 需要 Codex 真做事，而不只是理解主题。

例如：

- 做一个 map；
- 做一份对比；
- 做一个 project companion update；
- 做一份 publish-ready output。

### 转 `review-queue/pending/`

当满足：

- 讨论已经收敛成“需要 Tony 拍板”的决策项；
- 不是纯学习，而是 promote / defer / build / discard 的判断。

### 不转任何队列

如果只是：

- 新鲜但不重要；
- 观点碰撞但没形成下一步；
- 与当前主线弱相关；

那就只保留讨论摘要，不再进入系统下游。

## 群里的推荐规则

### 规则 1：最多 1 个主话题

同一时间只讨论一个话题。  
不要在一个 thread 里混：

- 新技术；
- 项目推进；
- 学习路径；
- 发布输出。

### 规则 2：每个 Agent 只说自己那一层

例如：

- `Engineer` 不做商业判断；
- `Strategist` 不展开实现细节；
- `Operator` 不抢技术首判；
- `Scout` 不直接说“应该入库”。

### 规则 3：Tony 可以随时插入三个动作

建议用最简单的群内控制词：

```text
继续
反方
收口
```

含义：

- `继续`：再补一轮
- `反方`：要求给反对观点
- `收口`：Moderator 直接总结

### 规则 4：默认不自动入库

群里出现的任何结论，默认都只是：

```text
讨论结论，不是 canonical knowledge
```

## 为什么这个方案适合你现在

- 你现在缺的不是更多后台 job，而是一个“多角度判断面”。
- 你已经有 Hermes 的发现能力，也有 Codex 的结晶能力，中间正好缺一个讨论层。
- 飞书比 Obsidian 更适合实时碰撞和追问。

## 最小试点建议

先跑一个最小版本：

### 常驻

- `Scout`
- `Engineer`
- `Operator`
- `Strategist`
- `Moderator`

### 节奏

- 每天最多 1 次主动话题；
- Tony 可随时主动发起 1 个问题；
- 每个话题最多 4 轮；
- 每次都必须有收口。

### 输出

- 群讨论
- 1 个讨论摘要
- 只有在明确值得时，才进 `learning-tasks` / `codex-requests` / `review-queue`

## 我对 Hermes 的建议

如果你真要结合 Hermes，我建议把 Hermes 先定义成：

```text
Hermes = Moderator + Router + Summary Writer
```

而不是让 Hermes 同时扮演全部专家角色。

原因很简单：

- 这样最稳；
- 最容易控噪音；
- 最容易和你现有的 task intent / Codex request / review queue 体系接上；
- 也最容易以后再细分成更多角色。

## 下一步

如果这版方向对，你下一步最值得做的不是立刻造 5 个独立系统，而是：

1. 先确定 4 个群内角色的中文名字；
2. 定义 Moderator 的收口模板；
3. 约束 Hermes 在什么情况下发起群讨论；
4. 再决定要不要把讨论摘要落到单独目录。

我建议先试 3 天，再看群是否真的带来更好的判断，而不是更多噪音。

## 推荐命名

我建议群里不要用太硬的英文代号，也不要起得太像“人格 bot”。

最稳的一套是：

| Role | 群内显示名 | 为什么这样叫 |
|---|---|---|
| `Scout` | `信号员 Hermes` | 一看就知道它负责发现新信号，不负责拍板 |
| `Engineer` | `工程师 Hermes` | 直接对应技术实现、架构、难点判断 |
| `Operator` | `运营官 Hermes` | 这里的“运营”更偏运行、维护、流程、成本，不是市场运营 |
| `Strategist` | `策略官 Hermes` | 明确它负责优先级、长期价值、资源判断 |
| `Moderator` | `主持人 Hermes` | 负责控场、追问、收口，不抢观点 |

如果你想稍微更有“团队感”，可以用这套备选：

| Role | 备选显示名 |
|---|---|
| `Scout` | `雷达员 Hermes` |
| `Engineer` | `架构师 Hermes` |
| `Operator` | `运行官 Hermes` |
| `Strategist` | `参谋 Hermes` |
| `Moderator` | `协调员 Hermes` |

我的默认建议还是第一套，因为更直接，不容易误解。

## 最终收口格式

我建议最终收口分成两层：

### 1. 群里显示层

群里显示短版，方便你快速扫一眼：

```text
【讨论收口】
- 主题：MCP 无状态化
- 结论：值得继续跟
- 动作：study
- 原因：对 Agent 工具接入和状态治理影响很大
- 下一步：让 Codex 做一份 MCP 接入审查清单草案
```

### 2. 结构化记录层

写回 `00-Inbox-AI/` 时，用一个 YAML-first 格式，方便以后被 Hermes / Codex / 脚本再利用。

推荐模板：

```yaml
topic: "MCP 无状态化"
date: "2026-06-15"
source_trigger: "scout" # scout | tony-question | follow-up
discussion_id: "2026-06-15-mcp-stateless"
participants:
  - signaler: "信号员 Hermes"
  - engineer: "工程师 Hermes"
  - operator: "运营官 Hermes"
  - strategist: "策略官 Hermes"
  - moderator: "主持人 Hermes"

judgment:
  relevance: high # high | medium | low
  confidence: medium # high | medium | low
  action: study # watch | study | build | publish | ignore
  urgency: this-week # now | this-week | later

why:
  summary: "MCP 无状态化会影响工具接入、会话边界和运行时复杂度。"
  technical_angle: "降低状态耦合，但需要重新看鉴权、上下文恢复和工具路由。"
  operational_angle: "长期可能更稳，但短期会增加接入 checklist 和测试负担。"
  strategic_angle: "对 Tony 的 Agent infrastructure 判断有长期价值。"

disagreement:
  present: true
  key_tension: "工程简化 vs 生态未稳定，适合 watch+study，不适合立刻升级。"

next_step:
  owner: "Codex"
  downstream: "codex-request" # none | learning-task | codex-request | review-queue
  requested_output: "MCP 接入审查清单草案"
  path_hint: "30-Playbooks/MCP 接入审查清单.md"

promotion_gate:
  canonical_candidate: false
  review_needed: true
  publish_needed: false

refs:
  source_notes:
    - "00-Inbox-AI/hermes/curated-scout/20260615-090000-digest.md"
  related_queue_items:
    - "00-Inbox-AI/review-queue/accepted/2026-06-14-review-gate-batch-decision.md"
```

## 为什么用这个格式

- `judgment` 让你快速看结论；
- `why` 把不同角色的价值保留下来；
- `disagreement` 记录真正值得记住的分歧；
- `next_step` 直接决定是否转下游；
- `promotion_gate` 明确“讨论结论”不等于“知识入库”。

## 群里收口时的固定动作词

为了让 Hermes 更容易工作，我建议收口时固定只输出这些动作之一：

```text
watch
study
build
publish
ignore
```

对应含义：

- `watch`: 值得持续关注，但先不转任务
- `study`: 值得转成 learning / research
- `build`: 值得转成可执行实现任务
- `publish`: 值得做成分享或 online projection
- `ignore`: 先不继续投入

## 我的默认建议

如果你现在就要试，我建议你先用：

- `信号员 Hermes`
- `工程师 Hermes`
- `运营官 Hermes`
- `策略官 Hermes`
- `主持人 Hermes`

然后收口时统一输出：

```text
主题 / 结论 / 动作 / 原因 / 下一步
```

落盘时再转成上面的 YAML 结构。
