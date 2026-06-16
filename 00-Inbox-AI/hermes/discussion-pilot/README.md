---
title: "飞书多 Agent 讨论组 Prompt Drafts"
created: 2026-06-15
updated: 2026-06-15
status: draft
owner: codex
tags:
  - hermes
  - feishu
  - discussion
  - prompts
---

# 飞书多 Agent 讨论组 Prompt Drafts

这组文件是飞书讨论层的角色草案。

目标：

```text
先有稳定讨论层
-> 再决定是否接入 Hermes 编排
-> 再决定是否进入 task / review / publish / knowledge
```

## 当前角色

- [[00-Inbox-AI/hermes/discussion-pilot/信号员-Hermes]]
- [[00-Inbox-AI/hermes/discussion-pilot/工程师-Hermes]]
- [[00-Inbox-AI/hermes/discussion-pilot/运营官-Hermes]]
- [[00-Inbox-AI/hermes/discussion-pilot/策略官-Hermes]]
- [[00-Inbox-AI/hermes/discussion-pilot/主持人-Hermes]]

## 约束

- 这些角色当前只是讨论层 draft，不是 canonical agent spec。
- 讨论内容默认不自动入库。
- 只有 `主持人 Hermes` 可以做最终收口。
- 只有在收口结论明确时，才允许转 `learning-tasks` / `codex-requests` / `review-queue`。

## 推荐使用方式

1. `主持人 Hermes` 开场并定义问题。
2. `信号员 Hermes` 先给背景与来源。
3. `工程师 Hermes` 讲技术含义。
4. `运营官 Hermes` 讲落地与维护成本。
5. `策略官 Hermes` 讲长期价值与优先级。
6. Tony 插话追问。
7. `主持人 Hermes` 收口。

## 主持 Prompt

- [[90-Agent-System/prompts/hermes-feishu-discussion-moderator]]

## 单 Bot 编排入口

- [[90-Agent-System/scripts/hermes-single-bot-discussion]]
- [[00-Inbox-AI/hermes/2026-06-15-single-bot-discussion-setup]]

## 收口动作词

```text
watch
study
build
publish
ignore
```
