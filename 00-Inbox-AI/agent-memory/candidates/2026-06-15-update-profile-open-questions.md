---
title: "Memory Candidate: 更新 profile.md Open Questions — 06/14 batch 已给出优先级"
created: 2026-06-15
status: pending-review
source: memory-review-scout
type: replace
target: "00-Inbox-AI/agent-memory/profile.md"
---

# Candidate: 更新 profile.md 的 Open Questions

## 建议操作

**replace** — 将 `profile.md` 的 "Open Questions" 区段从：

```
## Open Questions

- Which learning domains should have the highest priority this month?
- Which accepted/discarded Scout v2 candidates should be used to tune future recommendations?
```

替换为：

```
## Current Priorities (via 06/14 Review Gate Batch)

Tony implicitly prioritized 5 learning tasks through review gate triage on 2026-06-14:

1. Agent Memory Architecture (P1: accept → build schema + memory gate)
2. Hermes Model Routing (P1: accept → build routing matrix + eval samples)
3. MCP Protocol Evolution (P2: watch → build access checklist)
4. AI Recursive Self-Improvement (P2: watch → build governance gate)
5. Advertising Domain Crystallization (P3: accept-with-verification → source verification)

Execution is staged: P1 gates reduce review queue noise first, then P2 checklists, then P3 verification.

## Open Questions

- Which accepted/discarded Scout v2 candidates should be used to tune future recommendations?
- Should the task-intent routing preference (research/project/organize/writing/learning/reflection/publish) be hardened as a negative-signals rule?
```

## 变更理由

1. **第一个问题已部分回答**: "Which learning domains should have the highest priority this month?" — Tony 在 06/14 通过 batch review 给出了明确的优先级排序（Agent Memory > Agent Model > MCP > RSI > Advertising）

2. **移除已回答问题可减少 agent 误判**: 如果 agent 读取 Open Questions 后认为 Tony 仍需要建议优先级，可能产生无效的优先级推荐

3. **同时补充一个新的 Open Question**: task-intent routing preference 在 `preferences.md` 中被记录为正偏好，但缺少 `negative-signals.md` 配对——这应成为 Tony 的决策点

4. **与 F1 互补**: F1 建议记录 batch review 到 memory-changelog，本 candidate 让 profile.md 的 Open Questions 与新的系统状态对齐

## 关联发现

memory-review-2026-06-15 的 F1 + F5

## 备注

- 如果 Tony 不接受 F1 的 batch review 记录，本 candidate 的 "Current Priorities" 区段可改为更通用的措辞
- 新增的 Open Question（task-intent routing 是否需要 negative-signals 配对）来自 F5——这是一个诚实的未知决策点
