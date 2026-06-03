---
title: DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback
type: candidate-note
status: pending-review
topic: AI-Engineering
source: arXiv AI Agents
source_url: https://arxiv.org/abs/2605.22781v1
published_at: 2026-05-21T17:36:17Z
captured_at: 2026-05-23T15:09:51+00:00
importance_score: 5
---

# 这是什么

LLM-powered AI agents require high-frequency state exploration (e.g., test-time tree search and reinforcement learning), relying on rapid checkpoint and rollback (C/R) of the complete sandbox state, including files and process state (e.g., memory, contexts, etc.). Existing mechanisms duplicate the entire state, causing hundreds of milliseconds to seconds of latency per C/R, which severely bottlenecks deep search and large-scale fan-outs. This paper observes that subsequent checkpoints in AI a...

# 为什么值得关注

AI-Engineering: 命中 Agent, Eval, Evaluation, Sandbox；Security: 命中 bot

# 和现有知识库的关系

- 建议先放入 `AI-Engineering` 候选池，后续由人工判断是否合入正式专题。

# 建议进入哪个专题

- AI-Engineering

# 建议动作

- [ ] 忽略
- [ ] 加入学习队列
- [ ] 合入正式专题
- [ ] 生成 Playbook
- [ ] 生成对比表

Agent 建议动作：`review`

# 原始来源

- 来源：arXiv AI Agents
- 链接：https://arxiv.org/abs/2605.22781v1
- 发布时间：2026-05-21T17:36:17Z

# Agent 判断依据

- importance_score: 5
- topic_scores: {'AI-Engineering': 15, 'Security': 2}
- semantic_topic: 
- ai_reason: AI-Engineering: 命中 Agent, Eval, Evaluation, Sandbox；Security: 命中 bot
- captured_date: 2026-05-23
