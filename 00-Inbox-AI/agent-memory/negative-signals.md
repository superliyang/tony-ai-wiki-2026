---
title: "Agent Memory Negative Signals"
created: 2026-06-01
updated: 2026-06-03
status: active
tags:
  - ai-first
  - memory
  - negative-signals
---

# Agent Memory Negative Signals

This file records what the system should recommend less often.

## Current Negative Signals

- Do not treat tool installation as success by itself.
- Do not let multiple tools write canonical knowledge independently.
- Do not hide important memory only inside app databases.
- Do not connect high-risk integrations before staging and review are tested.
- Do not auto-publish legacy or staged content to GitHub before privacy review.
- Do not treat high-frequency search-result streams as a learning system.
- Do not let Hermes directly write canonical `10-Knowledge/` notes; Hermes should stage reports, candidates, review-queue entries, and recall suggestions.
- Do not make Codex responsible for long-running patrol or scheduled scouting; Codex may still do ad hoc research when Tony asks or when crystallizing accepted work.
- Do not make Tony browse raw information feeds; the system should bring curated candidate directions to Tony for judgment.
- Do not treat OpenHuman Memory Tree or Hermes private memory as final truth.
- Do not let OpenHuman, Hermes, Codex, and other agents form separate memory islands; durable cross-agent memory belongs in shared Markdown.
- Do not write all conversation content into long-term memory without filtering for durable preference, decision, pattern, or learning direction.
