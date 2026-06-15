---
title: "Day-1 复习：Agent 记忆架构 — 持久化、上下文管理与隐私边界"
review_date: 2026-06-15
review_stage: "day-1"
source_package: "00-Inbox-AI/learning-tasks/accepted/2026-06-05-agent-memory-architecture-package.md"
accepted_date: 2026-06-14
created: 2026-06-14
type: follow-up-review
---

# D+1 复习：Agent 记忆架构 — 持久化、上下文管理与隐私边界

## 为什么现在应该复习

此包可能是 5 个包里对你 Cognitive OS 最直接可落地的——它给了 memory 的 4 层区分（session / working / long-term / canonical）、5 种存储方案的比较、7 个 gap 和补救 control、以及一个 concrete memory schema。D+1 复习关键是检验你是否理解了「记忆晋升闸门」的设计——而这正是 Hermes 当前最需要补的工程缺口。

## 3 个复习问题

1. **Session context、working memory、long-term memory、canonical knowledge 四者的写入权限各归谁？**
2. **Hermes Gap Analysis 里的 7 个缺口，哪两个最紧急？** (提示：memory_type 缺失 和 删除/遗忘流程缺失)
3. **为什么「把所有消息写入向量库」是错误做法？** (参考 Mem0 文章的观点)

## Obsidian 动作

打开 `00-Inbox-AI/agent-memory/`（如不存在则创建），放入一个 `D+1 记忆自检.md`：写下你认为 Hermes 当前最容易被「过期记忆」污染的两个场景，各用 1 句话描述。

## 建议 Codex 更新

- 如果 Tony 批准 memory schema，建议 Codex 生成 `30-Playbooks/Agent 记忆晋升与遗忘流程.md`
- 暂不建议 canonicalize 到 `10-Knowledge/`——等 D+7 用一个实际 Hermes/Codex 流程验证 schema 后再入库
