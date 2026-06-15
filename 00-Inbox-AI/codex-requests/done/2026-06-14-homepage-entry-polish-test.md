---
title: "Codex Request - Homepage Entry Polish Test"
created: 2026-06-14
status: done
owner: hermes
request_type: map-maintenance
priority: P2
domain: Personal-Knowledge-System
source_refs:
  - 00-Home/今日入口.md
  - 20-Maps/领域平铺图谱.md
desired_outputs:
  - 00-Home/今日入口.md
publish_to_feishu: false
safety_note: "Navigation-only request. Do not publish or touch secrets."
---

# Codex Request - Homepage Entry Polish Test

## Completion

Status: done

Outputs:

- [[00-Home/今日入口]]

Change:

- Added a first-screen note making [[20-Maps/领域平铺图谱]] the default knowledge homepage.

Feishu:

- Not requested.

## Task

Codex should make a tiny UX polish to [[00-Home/今日入口]] so the first screen more clearly says that [[20-Maps/领域平铺图谱]] is now the main knowledge homepage.

## Why It Matters

This tests whether Hermes can create a bounded Codex request that Codex consumes through `00-Inbox-AI/codex-requests/`.

## Source Context

- [[00-Home/今日入口]]
- [[20-Maps/领域平铺图谱]]
- [[00-Inbox-AI/codex-requests/README]]

## Desired Output

- Minimal edit to [[00-Home/今日入口]].
- Move this request to `done/` with output links.

## Acceptance Criteria

- [ ] First screen still stays short.
- [ ] `领域平铺图谱` is clearly positioned as the knowledge homepage.
- [ ] No Feishu publish.
