---
title: "Tony User Profile and AI Cognitive System"
created: 2026-06-02
updated: 2026-06-03
status: active
tags:
  - ai-first
  - memory
  - user-profile
  - cognitive-system
---

# Tony User Profile and AI Cognitive System

This is a durable, reviewable memory for Hermes, Codex, Cursor, Claude Code, and other agents working in Tony's AI-first knowledge workspace.

## User Profile

Tony is building an AI-first personal knowledge and learning operating system, not just an Obsidian note collection.

Tony wants agents to:

- monitor the outside world so he does not need to manually browse feeds;
- identify worthwhile new technologies, research directions, tools, and engineering practices;
- explain why something matters in Chinese while preserving important English technical terms;
- recommend what to study, watch, discard, promote, or build;
- help turn a chosen signal into structured domain learning using point, line, surface, and body levels;
- preserve important decisions in Markdown/Git-backed memory so future agents understand him better.

Tony prefers systems that compound. A good answer or report should become future context, reusable knowledge, a map, a playbook, a skill, or a decision record when it matters.

## Legacy Knowledge Base

Tony's old mature vault is `/Users/tony/Vault/tony2026`.

It is broad and already contains serious restartable learning systems. The largest legacy domains include:

- AI-Learning: companies, people, models, systems, papers, concepts, timelines, and maps.
- AI-Engineering: agent engineering, AI systems, evaluation, workflows, memory, coding agents, and architecture patterns.
- International-Payments: payment success rate, 3DS, risk, chargebacks, reconciliation, compliance, operations, and technical architecture.
- Security, AI-Applications, Cloud-Native, AI-Open-Source, AI-Architect, Big-Data, Engineering-Management, Macro-Insight, and other support domains.

The legacy vault is not a temporary archive. It is a source of mature structure and prior thinking. Many domains already have:

- `专题总览.md`
- `学习进度.md`
- `恢复笔记.md`

That means new work should not start by summarizing every legacy note. Start from the domain overview, progress, and resume notes, then promote only high-value maps, playbooks, systems, comparisons, and learning paths into the new vault.

The legacy vault remains read-only unless Tony explicitly asks otherwise.

## New Knowledge Workspace

Tony's current main vault is `/Users/tony/Vault/tony-ai-wiki-2026`.

This vault is meant to be:

- Obsidian-readable;
- GitHub-publishable;
- agent-operable;
- self-contained without symlinks or live coupling back to the old vault;
- strict about staging before canonical promotion.

Canonical durable knowledge belongs in `10-Knowledge/`. Agent-generated material belongs in `00-Inbox-AI/` until reviewed.

The old vault `/Users/tony/Vault/tony-wiki-2026` has been replaced by this new vault.

## AI Cognitive System

Tony's system is named:

```text
Tony AI Cognitive System: Capture -> Recall -> Judge -> Crystallize -> Reuse
```

It should behave like a personal AI cognitive operating system:

```text
AI discovers signals
Human decides what matters
The vault preserves reviewed knowledge
Agents reuse the knowledge in future work
Feedback improves the assets
```

The role split is:

- OpenHuman: ingestion and Memory Tree layer; writes only to staging by default.
- Hermes: Recall / Scout layer; proactive runner, scheduled jobs, staged scouting, Feishu/Weixin messaging, candidate recommendations, review-queue entries, and memory-review suggestions.
- Tony: Judge; decides which candidate directions deserve deeper learning, watching, discarding, promotion, or map-building.
- Codex: Crystallize; final knowledge engineer for accepted decisions, wiki notes, maps, indexes, logs, memory files, skills, and playbooks. Codex may do ad hoc research when Tony asks or when crystallizing accepted candidates, but should not own long-running scheduled scouting.
- ECC: procedural engineering capability layer; turns repeated experience into skills, rules, and playbooks after review.
- Obsidian Markdown: reviewed knowledge surface and reuse surface.
- GitHub: durability, backup, publication, and history.
- Cursor/Claude Code: additional curation and engineering agents that should follow the same memory protocol.

Operating principle:

```text
OpenHuman 负责"记得住"
Hermes 负责"想得起"
ECC 负责"做得对"
Obsidian 负责"沉得下"
GitHub 负责"传得久"
```

More strictly:

```text
Information is not knowledge.
Knowledge is not an asset.
An asset is not capability.
Capability must be reused, verified, and improved.
```

## Shared Memory Bus

OpenHuman, Hermes, Codex, Cursor, Claude Code, and other agents should not rely on private hidden memory to understand Tony. They should read and write the shared Markdown memory bus:

```text
00-Inbox-AI/agent-memory/profile.md
00-Inbox-AI/agent-memory/preferences.md
00-Inbox-AI/agent-memory/learning-themes.md
00-Inbox-AI/agent-memory/negative-signals.md
00-Inbox-AI/agent-memory/user-profile-and-ai-cognitive-system.md
00-Home/当前主线.md                              (hot cache equivalent)
00-Inbox-AI/review-queue/
```

`00-Home/当前主线.md` is short-term shared context. `agent-memory/` is durable user/system memory. `review-queue/` is the human judgment surface.

## Learning Model

Tony's preferred learning loop is not passive reading. It is:

1. Scout: monitor external signals and detect promising directions.
2. Candidate: propose a learnable topic with a clear reason.
3. Human judgment: Tony decides whether to go deeper.
4. Domain learning: expand from point to line, surface, or body depending on scope.
5. Knowledge asset: produce maps, indexes, notes, comparisons, playbooks, or skills.
6. Feedback memory: accepted, deferred, and discarded decisions improve future recommendations.

Point, line, surface, body means:

- Point: one paper, tool, feature, repo, model, architecture pattern, or concept.
- Line: a connected chain such as Agent Memory methods, MCP security, coding agent benchmarks, or eval workflows.
- Surface: a subdomain map such as Agent infrastructure, AI Engineering, RAG systems, or international payment risk operations.
- Body: a full domain system such as AI Engineering, International Payments, AI Open Source, or Personal AI Knowledge OS.

## Domain Learning Template

The new vault should keep the old vault's restartable domain-learning style. A mature domain should usually have:

```text
10-Knowledge/<domain>/
├── 专题总览
├── 主题索引
├── 学习路径
├── 地图 / 对比
├── 关键系统 / 项目 / 公司 / 人物 / 论文
├── 实践 playbook
├── 学习进度
└── 恢复笔记
```

The exact path can vary with the current vault topology, but the domain must remain restartable: an agent should know what the domain is, what Tony has learned, what is next, what is weak, and how to resume.

## Scout Preference

Tony does not want hourly search-result noise. He wants a curated learning radar.

AI Scout should:

- prioritize high-quality English sources and international signals;
- translate and explain in Chinese;
- preserve key English terms;
- merge duplicate signals;
- summarize as "one-sentence signal + why it matters";
- recommend direct triggers such as `深入 Agent Memory`;
- deliver mainly through Feishu;
- reserve Weixin for important alerts after rate-limit and access policy are hardened.

The current active external-signal implementation is AI Scout v2 / `curated-ai-scout`.

Two Scout loops should be kept distinct:

- `curated-ai-scout`: external world -> `00-Inbox-AI/review-queue/pending/` -> Feishu. It finds candidate learning directions from RSS, Exa, papers, blogs, products, and engineering sources.
- `memory-review-scout`: internal memory review -> candidate memory updates -> Tony confirmation. It should inspect recent conversations, accepted/discarded decisions, Scout feedback, and staged agent outputs, then propose updates to `agent-memory/`.

`memory-review-scout` should not automatically rewrite canonical `10-Knowledge/`; it should propose memory candidates for Tony to accept, discard, or ask Codex to crystallize.

## Tony Judgment Commands

Tony should be able to steer the system with lightweight commands:

```text
深入 <candidate topic>
watch <number or topic>
discard <number or topic>
promote <number or topic>
build learning map <number or topic>
```

Interpretation:

- `深入`: start a focused learning session or research plan.
- `watch`: keep the topic on the watchlist and use it as weak positive feedback.
- `discard`: use it as negative feedback for future recommendations.
- `promote`: prepare reviewed wiki promotion.
- `build learning map`: expand a candidate into point, line, surface, or body structure.

## Memory Boundary

Hermes does not automatically remember all Codex conversations. Important cross-agent memory must be written into shared Markdown files.

Use this rule:

- If Tony says "记住这个", "以后按这个来", "这是我的偏好", or "这很重要", write it into `00-Inbox-AI/agent-memory/`.
- If the decision changes architecture, automation, or source-of-truth boundaries, update `00-Home/当前主线.md` and `00-Inbox-AI/agent-memory/memory-changelog.md`.
- Do not store secrets, tokens, local auth files, or runtime account state.
- Do not let hidden app memory become the source of truth.

## Iron Rules

- Hermes should not directly write formal `10-Knowledge/` notes. Hermes can run staged scouting, stage reports, create review-queue entries, recall, recommend, and notify.
- Codex should not be responsible for long-running patrol or scheduled scouting. Codex can perform ad hoc research when Tony asks or when crystallizing accepted work.
- Tony should not need to browse raw information streams. The system should bring curated candidate directions to Tony.
- OpenHuman and Hermes may capture broadly, but captured material is candidate context until reviewed.
- Obsidian/GitHub-backed Markdown is the durable source of truth.

## How Agents Should Work With Tony

When helping Tony:

- be proactive, but avoid noisy automation;
- treat source quality and learning value as more important than raw novelty;
- do not auto-promote staged content into `10-Knowledge/`;
- preserve source links for external claims;
- prefer Chinese explanations with English technical terms preserved;
- create concrete next steps and durable artifacts;
- when a topic is accepted, build a restartable learning path rather than a one-off summary;
- update shared memory when a preference or durable decision is discovered.
