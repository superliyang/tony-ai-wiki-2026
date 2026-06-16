---
title: "Hermes Discussion Profiles Created"
created: 2026-06-15
updated: 2026-06-15
status: draft
source: codex
type: setup-summary
---

# Hermes Discussion Profiles Created

已创建一组用于飞书多 Agent 讨论试点的 Hermes 原生 profile。

这些 profile 是 Hermes runtime 层能力，不是 canonical agent spec。

## Profile 对照

| Hermes profile id | 群内角色名 | 用途 |
|---|---|---|
| `discussionsignaler` | `信号员 Hermes` | 讲清楚信号、来源、变化点、为什么现在值得讨论 |
| `discussionengineer` | `工程师 Hermes` | 讲技术含义、实现难点、系统连接点 |
| `discussionoperator` | `运营官 Hermes` | 讲执行摩擦、维护负担、流程风险 |
| `discussionstrategist` | `策略官 Hermes` | 讲长期价值、机会成本、动作倾向 |
| `discussionmoderator` | `主持人 Hermes` | 控顺序、压分歧、最终收口成单动作 |

## 创建方式

使用 Hermes 原生命令：

```bash
hermes profile create --clone --description "..." discussionsignaler
hermes profile create --clone --description "..." discussionengineer
hermes profile create --clone --description "..." discussionoperator
hermes profile create --clone --description "..." discussionstrategist
hermes profile create --clone --description "..." discussionmoderator
```

对应角色边界已写入各自的 `SOUL.md`。

## 相关参考

- [[00-Inbox-AI/hermes/discussion-pilot/README]]
- [[00-Inbox-AI/hermes/discussion-pilot/信号员-Hermes]]
- [[00-Inbox-AI/hermes/discussion-pilot/工程师-Hermes]]
- [[00-Inbox-AI/hermes/discussion-pilot/运营官-Hermes]]
- [[00-Inbox-AI/hermes/discussion-pilot/策略官-Hermes]]
- [[00-Inbox-AI/hermes/discussion-pilot/主持人-Hermes]]
- [[00-Inbox-AI/hermes/2026-06-15-feishu-multi-agent-discussion-pilot]]
- [[90-Agent-System/prompts/hermes-feishu-discussion-moderator]]

## 下一步建议

先不要把这 5 个 profile 接到自动 cron。

更稳的试运行方式是：

1. 用 `discussionmoderator` 做一轮半人工主持。
2. 话题只选一个。
3. 讨论结束后只生成一份讨论摘要，不直接 promote。
