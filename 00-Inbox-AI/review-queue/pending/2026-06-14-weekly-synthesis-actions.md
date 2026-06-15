---
title: "Tony Attention: Weekly Synthesis Actions 2026-06-14"
created: 2026-06-14
status: pending
type: weekly-synthesis-actions
source: "00-Inbox-AI/reports/2026-06-14-weekly-synthesis.md"
tags:
  - weekly-synthesis
  - action-items
  - review
---

# Tony Attention: Weekly Synthesis Actions 2026-06-14

## 本周报告已生成

完整报告：[[00-Inbox-AI/reports/2026-06-14-weekly-synthesis]]

## 需要 Tony 处理的决策

### 🔴 已有 Pending Review（需决策）

1. **[[00-Inbox-AI/review-queue/pending/2026-06-14-trust-aware-agent-memory-review|Agent 记忆可信检索]]**
   - Codex 推荐：`study → build`
   - 理由：直接补强已接受的 Agent Memory Gate，不增加新方向
   - 若不处理：并入下周 follow-up

2. **[[00-Inbox-AI/review-queue/pending/2026-06-14-project-companion-pilot-review|Project Companion Pilot]]**
   - Codex 推荐：`manual-on-demand`
   - 理由：先清 review backlog，暂不开启新 cron

### 🟡 新建议（本次周报提出）

3. **Pending Learning Task Triage**
   - 问题：43 个 pending task 积压，部分已被覆盖
   - 建议：执行一次批量 triage，标记 duplicate/discard
   - 若同意，Hermes/Codex 可执行

4. **启用 Follow-Up Review Cron**
   - 问题：5 个 accepted 项无周期性提醒
   - 建议：激活 `hermes-follow-up-review` cron job
   - 若同意，按 accepted 项的 follow-up date 设置

## 执行队列状态

Accepted Batch Decision 的 5 项需要 Codex 开始 build：
- P1: Agent Memory Gate + Hermes Model Routing
- P2: MCP Access Checklist + Self-Improvement Gate
- P3: Advertising Source Verification

若 Tony 没有额外指令，Codex 将按 P1→P2→P3 顺序开始执行。
