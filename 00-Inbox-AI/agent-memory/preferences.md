---
title: "Agent Memory Preferences"
created: 2026-06-01
updated: 2026-06-14
status: active
tags:
  - ai-first
  - memory
  - preferences
---

# Agent Memory Preferences

## Positive Preferences

- Prefer proactive recommendations backed by current signals.
- Prefer staging and review before changing canonical notes.
- Prefer Markdown and Git-backed memory over opaque-only agent memory.
- Prefer practical learning plans and implementation steps over abstract tool stacking.
- Prefer systems that become more useful through accepted and discarded decisions.
- Prefer curated learning radar over high-frequency search-result streams.
- Prefer English-first international sources with Chinese synthesis and important English terms preserved.
- Prefer learning candidates that can become point, line, surface, or body level study paths.
- Prefer shared Markdown memory for durable user preferences because Hermes, Codex, and other agents do not automatically share private conversation memory.
- Prefer the `Tony AI Cognitive System: Capture -> Recall -> Judge -> Crystallize -> Reuse` role boundary.
- Prefer OpenHuman and Hermes for broad capture, Hermes for recall/scout, Tony for direction judgment, Codex for final crystallization, Obsidian for reviewed reuse, GitHub for durable history, and ECC for repeatable capability.
- Prefer the access-layer split: Obsidian = personal knowledge production center; GitHub private repo = long-term versioned fact source; `output-feishu/` = publishable intermediate layer; Feishu knowledge base / docs = anywhere access, mobile reading, sharing, and collaboration; Feishu CLI = automated sync executor.
- Prefer a task-intent layer before research: Tony's requests should be routed as `research`, `project`, `organize`, `writing`, `learning`, `reflection`, or `publish` instead of defaulting every request to research.

## Output Preferences

- Use Chinese explanations with important English technical terms preserved.
- Write vault documentation primarily in Chinese because Tony's English is not strong; preserve important English technical terms such as `agent memory`, `workflow`, `review queue`, `projection`, `canonical memory`, `scout`, and `playbook`.
- Simple short notes, file labels, command snippets, and tool-native names may remain in English when that is clearer or more conventional.
- Give clear next steps.
- Keep architecture decisions explicit.
- Record durable decisions into the vault when they affect the system design.
- When Tony says "记住这个", "以后按这个来", "这是我的偏好", or "这很重要", update `00-Inbox-AI/agent-memory/`.
- When a decision changes architecture, automation, or source-of-truth boundaries, update `00-Home/当前主线.md` and `00-Inbox-AI/agent-memory/memory-changelog.md`.
- When publishing to Feishu, use `output-feishu/` as the cleaned intermediate layer and keep Obsidian + GitHub as source of truth.
- After a meaningful AI output, lightweight feedback such as `有用`, `太长`, `太浅`, `跑偏`, `继续放大`, `入库`, `发飞书`, or `暂停` should influence future Hermes routing and Codex output shape.

## Operating Rules

- Hermes may perform staged scouting and recall: scheduled inspection, candidate generation, staged reports, review-queue entries, memory-review suggestions, and notifications.
- Hermes default writable areas are `00-Inbox-AI/hermes/`, `00-Inbox-AI/review-queue/pending/`, `00-Inbox-AI/candidates/`, `00-Inbox-AI/signals/`, `00-Inbox-AI/reports/`, `00-Inbox-AI/agent-memory/candidates/`, and `00-Inbox-AI/agent-memory/projections/`.
- Hermes must not directly write canonical knowledge or system layers: `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`, unless Tony explicitly asks or Codex has promoted reviewed material.
- Hermes must not directly edit canonical shared memory files under `00-Inbox-AI/agent-memory/*.md`; it may write memory candidates and projections only.
- Hermes must not write the legacy vault `/Users/tony/Vault/tony2026`, `00-Inbox-AI/openhuman/`, or `00-Inbox-AI/ecc/`.
- Codex should crystallize accepted decisions into clear wiki notes, indexes, maps, logs, memory files, skills, or playbooks.
- Codex may do ad hoc research/scouting when Tony asks or when crystallizing an accepted candidate, but Codex is not the long-running patrol or scheduled scouting agent.
- Tony should not need to browse information streams manually; the system should bring candidate directions to him for judgment.
- OpenHuman and Hermes may capture broadly, but captured material is candidate context until reviewed.
- Tony's lightweight decision commands include `深入`, `watch`, `discard`, `promote`, and `build learning map`.
