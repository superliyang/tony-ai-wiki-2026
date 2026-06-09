---
title: "Memory Candidate: 将 Tony 职业画像从 projection 回流 canonical"
created: 2026-06-08
status: pending-review
source: memory-review-scout
type: add
target: "00-Inbox-AI/agent-memory/profile.md"
---

# Candidate: 将 Tony 职业画像从 projection 回流 canonical

## 建议操作

**add** — 在 `profile.md` 的 "Current Understanding" 区域添加 Tony 的职业画像：

> - Tony 是偏架构/平台/工程效率/组织落地的技术管理者，负责基础架构团队。
> - 技术底盘: Java/Go/Spring Boot/MyBatis/Dubbo/APISIX/Nginx/K8s/AWS/Redis/Kafka/RocketMQ。
> - 核心工作: 开发框架/脚手架/Starter、网关建设、稳定性治理、安全架构。
> - AI 理念: AI 从个人工具推进成组织级工程能力。
> - 学习风格: 系统化学习、输出倒逼输入、Obsidian/Cursor 管理知识。
> - 行业: skill gaming / casual gaming。

同时建议在 `user-profile-and-ai-cognitive-system.md` 的 "User Profile" 区域也增加对应条目。

## 变更理由

1. **当前仅有 projection 有职业画像**：`hermes-soul.md`（projection）包含完整的 Tony 角色、技术栈、行业信息，但 canonical `profile.md` 和 `user-profile-and-ai-cognitive-system.md` 完全没有。canonical 仅描述了 Tony 作为「AI knowledge system builder」这一维度。

2. **违反 Memory Protocol 设计意图**：MEMORY-PROTOCOL.md 规定 projection 是 derived runtime copy，canonical 是 source of truth。但当前职业画像的「源」不明——它只在 projection 中存在，不在 canonical 中。这意味 projection 不是从 canonical 派生的，而是独立维护的，恰好违反了「projection must not overwrite canonical shared memory automatically」的原始设计意图。

3. **Agent 决策需要职业上下文**：
   - 没有行业信息 → agent 无法判断推荐是否与 skill gaming 行业相关
   - 没有技术栈 → agent 推荐语言/框架时无法基于 Tony 现有底盘
   - 没有角色信息 → agent 不了解 Tony 需要 team-level 推行方案而非个人实验

4. **来源追踪**：hermes-soul.md 中的职业画像信息未标注来源。推测来自早期对话（vault migration 前），在 `tony-wiki-2026` → `tony-ai-wiki-2026` 迁移时被保留在 projection 但未回流到 canonical。6/3 clean-slate 操作可能无意中移除了 canonical 中的职业描述（如果之前存在的话）。

## 关联发现

memory-review-2026-06-08 的 F4

## 备注

本候选建议的操作是 **add**（新增），不是 replace。当前 canonical 中不存在等效信息，所以是补充而非替换。如果 Tony 认为某些细节不应暴露在 shared memory 中（如具体公司名），可调整为更抽象的版本。

建议 Codex/Claude Code 审核后发现并补充更多维度（团队规模、当前优先级、近期技术决策等）。
