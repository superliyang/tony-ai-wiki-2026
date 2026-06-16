---
title: "Tony Review: OpenAI Dreaming 记忆范式"
created: 2026-06-15
updated: 2026-06-15
status: pending
owner: codex
source_package: "00-Inbox-AI/learning-tasks/in-progress/2026-06-15-openai-dreaming-memory-package.md"
source_task: "00-Inbox-AI/learning-tasks/pending/2026-06-06-openai-dreaming-memory-paradigm.md"
recommendation: "study -> build"
priority: P2
tags:
  - review
  - agent-memory
  - dreaming
  - memory-consolidation
---

# Tony Review: OpenAI Dreaming 记忆范式

## Decision Needed

是否把 Dreaming-style memory consolidation 纳入 Tony Cognitive OS 的 Agent Memory build line？

建议：`study -> build`

## Why This Matters

OpenAI 的 Dreaming release 明确把记忆问题从“保存单条事实”推进到“后台合成、更新和保持当前性”。这对你的系统有直接意义：

- Hermes/OpenHuman 会持续产生候选记忆；
- Codex 需要 review、去重、脱敏、归类；
- 如果没有 consolidation layer，候选记忆会逐渐重复、过期、互相冲突；
- 如果 consolidation layer 绕过 review，又会污染长期事实源。

因此最合适的位置是：

```text
candidate memories
  -> dreaming-style consolidation
  -> Tony/Codex review
  -> reviewed runtime memory or canonical promotion
```

## Recommended Decision

选择 `build`，但限制为 **reviewed consolidation job**：

- daily lightweight memory digest；
- weekly duplicate/conflict/stale detection；
- 输出到 `00-Inbox-AI/agent-memory/digests/` 和 `00-Inbox-AI/review-queue/pending/`；
- 不直接写 `10-Knowledge/`；
- 不自动修改 Hermes 全局记忆；
- 不发布 private/secret-adjacent 内容到 Feishu/Weixin。

## Decision Options

```text
study  = 先保留为正式学习笔记，不马上实现
build  = 设计 Hermes/Codex memory consolidation job 的最小实现
watch  = 继续观察 OpenAI/Anthropic/Google 是否公开类似机制
defer  = 等 Agent Memory gate 先落地
discard = 不继续处理
```

## Proposed Build Slice

如果选择 `build`，第一步只做 dry-run：

1. 新建 `00-Inbox-AI/agent-memory/digests/README.md`。
2. 定义 memory digest 模板。
3. 从最近 30 条 Hermes/Codex 候选中生成一份 dry-run digest。
4. Codex 标记 duplicate / stale / conflict / promote-candidate。
5. Tony review 后再决定是否自动化。

## Safety Notes

- OpenAI 未公开 Dreaming 的完整内部实现；不要把本包当成复刻方案。
- Memory consolidation 只能生成候选和 review item，不能直接成为 canonical truth。
- 私密、账号、路径、权限、cron、发布、工具配置类记忆必须保守处理。
- 这项工作应和昨日 `trust-aware-agent-memory` package 合并理解：consolidation 负责整理记忆，admission gate 负责运行时是否注入。

## Output Package

[[00-Inbox-AI/learning-tasks/in-progress/2026-06-15-openai-dreaming-memory-package]]
