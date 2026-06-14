---
title: "Memory Candidate: 记录实际 Scout cron job 名到 canonical memory"
created: 2026-06-12
status: pending-review
source: memory-review-scout
type: add
target: "00-Inbox-AI/agent-memory/user-profile-and-ai-cognitive-system.md"
---

# Candidate: 在 canonical memory 中记录实际运行的 Scout job 名

## 建议操作

**add** — 在 `user-profile-and-ai-cognitive-system.md` 的 "Two Scout loops" 部分，将当前的两个 loop 扩展为三个，明确标注实际 cron job 名：

现有：
```
- `curated-ai-scout`: external world -> `00-Inbox-AI/review-queue/pending/` -> Feishu.
- `memory-review-scout`: internal memory review -> candidate memory updates -> Tony confirmation.
```

建议改为：
```
Three active scout loops:

- `hourly-ai-scout`: 高频外部信号扫描（每小时，exa + Camofox fallback，24h→7d 窗口）。产出到 `00-Inbox-AI/hermes/hourly-scout/`。
- `daily-ai-learning-scout` (canonical 中曾称 `curated-ai-scout`): 每日策展雷达（08:30 cron，RSS + Exa → LLM → 中文投递）。产出到 `00-Inbox-AI/hermes/curated-scout/`，通过 Feishu 推送。
- `memory-review-scout`: 内部记忆审查 → 候选更新 → Tony 确认。
```

同时，在 `hermes-soul.md` 的 "Scout Tools & State" 中同步更新（见关联 candidate 2026-06-05-align-scout-naming）。

## 变更理由

1. **Canonical 与实际运行不匹配**: canonical memory 只记录了 `curated-ai-scout` 和 `memory-review-scout`，但实际运行中的 cron job 名是 `daily-ai-learning-scout`（产出每天 3 轮 digest）和 `hourly-ai-scout`（每小时搜索）。新 agent 阅读 canonical 后会寻找不存在的 `curated-ai-scout` cron job。

2. **与 pending C2 互补而非替代**: C2 (2026-06-05) 提议全面重命名对齐（包括将 `daily-ai-learning-scout` 改为 `daily-ai-curated-scout`）。本候选采取更保守的方案：保留现有 cron job 名不变，只将实际运行名记录到 canonical，并添加曾用名映射。这样可以先消除"canonical 完全不知道实际 job 名"的问题，后续再讨论是否统一命名。

3. **阻塞新 agent onboarding**: 未来如果 Codex 或新 agent 需要理解系统架构，canonical memory 应该是准确的入口。当前 canonical 会误导 agent 去寻找不存在的 scout。

## 关联发现

memory-review-2026-06-12 的 F2

## 备注

- 与 C2 不冲突——C2 是全部重命名方案，本候选是增量记录
- 如果 Tony 偏好 C2 方案（统一命名），接受 C2 后本候选自动失效
- 接受后需同步更新 `hermes-soul.md` 的 Scout Tools & State 区段
