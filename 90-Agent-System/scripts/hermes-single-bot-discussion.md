---
title: "Hermes Single Bot Discussion Runbook"
created: 2026-06-15
updated: 2026-06-15
status: draft
tags:
  - hermes
  - feishu
  - discussion
  - runbook
---

# Hermes Single Bot Discussion Runbook

## 目标

用一个 Feishu bot 和 `discussionmoderator` profile，在一个群里输出一轮结构化讨论。

群里可见的是一个 bot。

bot 发出的消息内容内部再区分：

- `【主持人 Hermes】`
- `【信号员 Hermes】`
- `【工程师 Hermes】`
- `【运营官 Hermes】`
- `【策略官 Hermes】`

## 适用场景

- Tony 想看一个问题的多视角判断；
- 先验证讨论质量，再决定要不要做多 bot；
- 先做单话题、低噪音试点。

## 不适用场景

- 需要真实多成员群感；
- 需要每个角色单独保留长期会话历史；
- 需要不同飞书身份的独立权限。

## 最小运行方式

### 1. 本地生成讨论内容

在 vault 根目录运行：

```bash
discussionmoderator chat -Q --source tool -q '
你是主持人 Hermes。请使用 `90-Agent-System/prompts/hermes-feishu-discussion-moderator.md` 的规则，
围绕以下单一主题生成一轮飞书群讨论短稿。

主题：<topic>
触发来源：<scout | tony-question | follow-up>

要求：
1. 按顺序输出：
   - 【主持人 Hermes】
   - 【信号员 Hermes】
   - 【工程师 Hermes】
   - 【运营官 Hermes】
   - 【策略官 Hermes】
   - 【讨论收口】
2. 每个角色最多 4 个要点。
3. 整体保持紧凑，不要超过一屏半。
4. 最终动作只能是 watch / study / build / publish / ignore 之一。
5. 不要写 canonical knowledge，不要把讨论内容当作已入库事实。
' 
```

### 2. 发到 Feishu 群

如果已经知道目标群 `chat_id`：

```bash
discussionmoderator chat -Q --source tool -q '...同上...' \
  | hermes send --to 'feishu:<chat_id>'
```

如果是群里的某个 thread：

```bash
discussionmoderator chat -Q --source tool -q '...同上...' \
  | hermes send --to 'feishu:<chat_id>:<thread_id>'
```

## 推荐的第一轮试点方式

先不要自动发群。

更稳的方式是：

1. 先本地生成一轮讨论稿。
2. 肉眼看一遍噪音和收口质量。
3. 确认格式合适后，再 pipe 到 `hermes send`。

## 推荐话题格式

```text
主题：MCP 无状态化值不值得现在投入？
触发来源：tony-question
附加约束：重点比较工程复杂度、长期复利、对当前 Hermes 系统的影响。
```

## 成本控制建议

- 一次只讨论一个主题；
- 每个角色最多 4 个要点；
- 先用 `discussionmoderator` 一次性生成整段，不要让 5 个 profile 分别独立跑；
- 没有明确决策价值的话题，不发群。

## 下一步

这份 runbook 解决的是：

- 单 bot 怎么编排；
- Hermes profile 怎么落；
- Feishu 群消息怎么发。

还没解决的是：

- 目标群 `chat_id` 的确认；
- 是否需要从群内消息自动触发；
- 讨论后 summary 是否自动写入 `00-Inbox-AI/hermes/discussion-summaries/`。
