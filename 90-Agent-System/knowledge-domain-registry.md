---
title: "Knowledge Domain Registry"
created: 2026-06-16
updated: 2026-06-16
status: active
tags:
  - agent-system
  - knowledge-domain
  - routing
---

# Knowledge Domain Registry

这份注册表给 Hermes、Codex 和 Tony 共用，用来判断候选内容应该进入哪个知识体系。

## Rule

```text
先查已知领域。
能进入已知领域，就按该领域体系扩展。
不能进入已知领域，先写 domain proposal，不直接开新目录。
```

## Known Domains

| Domain | Formal Entrance | Main Structure | Intake Notes |
|---|---|---|---|
| AI | [[10-Knowledge/AI/专题总览]] | Companies / People / Models / Papers / News / Topics / Maps / Templates | broad AI 留这里；工程实现转 AI Engineering，开源项目转 AI Open Source |
| AI Engineering | [[10-Knowledge/AI-Engineering/专题总览]] | Stacks / Frameworks / Training / Evaluation / Deployment / Projects / Topics / Maps / Templates | 工程主题、生产实践、系统设计进入这里；开源项目卡片转 AI Open Source |
| AI Open Source | [[10-Knowledge/AI-Open-Source/专题总览]] | Categories / Organizations / Projects / Patterns / Case Studies / Maps / Watchlist | 开源项目必须进入项目体系，不做散点笔记 |
| Advertising | [[10-Knowledge/Advertising/专题总览]] | Topics / Maps / Templates / Cases / Playbooks / Runbooks | 已相对成熟，新增内容要挂到现有 topic/map |
| International Payments | [[10-Knowledge/International-Payments/专题总览]] | Foundations / Payment Methods / Routing / Risk / Settlement / Maps / Templates / Onboarding / Market Cases | 支付成功率、3DS、拒付、路由、对账 |
| Security | [[10-Knowledge/Security/专题总览]] | Standards / Tools / Controls / Open Source Tools / Topics / Maps / Templates / Playbooks / Case Studies / Interview Kit | 风险、权限、控制点、incident response；AI agent security 可双链 AI Engineering |
| Personal Knowledge System | [[10-Knowledge/Personal-Knowledge-System/专题总览]] | 方法、模板、跨工具协作 | Obsidian / Codex / Hermes / Feishu 协作经验 |

## AI Open Source Routing

AI Open Source 是一个控制塔，不是 repo bookmark list。

| Candidate | Target |
|---|---|
| repo / project | `10-Knowledge/AI-Open-Source/03-Projects/` |
| company / community / org | `10-Knowledge/AI-Open-Source/02-Organizations/` |
| project class | `10-Knowledge/AI-Open-Source/01-Categories/` |
| reusable engineering pattern | `10-Knowledge/AI-Open-Source/04-Patterns/` |
| stack combination | `10-Knowledge/AI-Open-Source/05-Case-Studies/` |
| comparison / ecosystem map | `10-Knowledge/AI-Open-Source/06-Maps/` |
| active tracking item | `10-Knowledge/AI-Open-Source/09-Watchlist/` |

When Hermes finds a strong project such as Unsloth, Codex should not create a loose note. It should update the project system: project card, category, organization, watchlist, and relevant pattern.

## Unknown Domain Proposal

未知领域先进入 working vault：

```text
/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/YYYY-MM-DD-domain-proposal.md
```

Do not create a new formal domain until proposal review.

## Promotion Checklist

Use [[90-Agent-System/workflows/knowledge-intake-and-promotion]] for the full staging-to-formal process.
