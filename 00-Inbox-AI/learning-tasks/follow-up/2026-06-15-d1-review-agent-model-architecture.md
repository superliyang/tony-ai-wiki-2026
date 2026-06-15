---
title: "Day-1 复习：面向 Agent 的模型架构"
review_date: 2026-06-15
review_stage: "day-1"
source_package: "00-Inbox-AI/learning-tasks/accepted/2026-06-08-agent-model-architecture-package.md"
accepted_date: 2026-06-14
created: 2026-06-14
type: follow-up-review
---

# D+1 复习：面向 Agent 的模型架构 — 从对话模型到长期执行模型

## 为什么现在应该复习

此包区分了「对话模型 vs Agent 友好模型」的评价维度，引入了 KV cache / prefill-decode / continuous batching 等推理概念，并建议了 Hermes 模型路由矩阵。首次复习的点不是背技术细节，而是检验你能不能回答「什么样的模型对 Hermes 这种长期执行 agent 才是好模型」。

## 3 个复习问题

1. **为什么「长上下文」不是 Agent 友好性的充分条件？** 至少说出 3 个额外要求。
2. **Hermes 的每日 scout、learning-task 生成、promotion gate 审查分别应该路由到哪种模型？** (提示：参看 Hermes Model Routing 表)
3. **prefill 是 compute-bound、decode 是 memory-bound — 这对长期 agent 任务意味着什么？**

## Obsidian 动作

在 `00-Inbox-AI/` 里新建 `Agent 模型 D+1 自测.md`，用「如果我只能给 Hermes 选 2 个模型，我会选哪两个、分别做什么」作为开头一句话，然后列出你的理由（≤5 句话）。

## 建议 Codex 更新

- 如果 Tony 确认路由逻辑合理，建议 Codex 生成 `30-Playbooks/Hermes 模型路由清单.md` 初稿
- 暂不建议 canonicalize — D+7 用 3 个真实任务测试路由后再定
