---
title: "「编码即接口」范式：Agent 与基础设施交互的下一个抽象层"
created: 2026-06-11
updated: 2026-06-11
status: pending
owner: hermes
priority: P2
domain: "Agent-Engineering"
review_after: "2026-06-25"
tags:
  - learning-task
  - hermes
  - code-as-interface
  - agent-engineering
  - mcp
  - tool-use
  - paradigm-shift
sources:
  - "https://opentools.ai/news/perplexity-search-as-code-ai-models-write-search-pipelines"
  - "https://arxiv.org/abs/2605.28617"  # Lacuna
  - "https://github.com/github/github-mcp-server/releases/tag/v1.2.0"  # GitHub MCP Server
---

# 「编码即接口」范式：Agent 与基础设施交互的下一个抽象层

## Why Now

2026-06-06 至 06-10，三条独立技术线索汇聚于同一个方向：**代码正取代传统 API 调用，成为 Agent 与基础设施之间的新接口层**。这不是渐进优化，而是抽象层的范式转移。

三条线索：

1. **Perplexity Search as Code** (06-06/08) — AI 模型用 Python 编写自定义搜索管道并在沙箱中执行。200 个 CVE 追踪：100% 准确率，仅 42,900 tokens（标准管道的 15%）。核心理念：给 Agent 代码生成能力，而不是预定义 API。

2. **Lacuna: 类型检查的 Agent 安全编程** (arXiv 2605.28617) — Agent 动作为「类型化程序空洞」，编译时类型检查拒绝 8.6% 不安全生成，平均 0.7 次重试修正。Agent 安全从运行时守卫→编译时检查。

3. **GitHub MCP Server 1.2.0** (06-08/09) — 从「HTTP API 调用 GitHub」到「Agent 编写并执行 Git 脚本」。工具调用从「REST endpoint」走向「代码执行」。

**为什么这条主线对 Tony 至关重要**：
- Hermes 作为 Agent，每天通过 MCP Server 调用数十种工具。当前模式是「结构化 JSON 工具调用」，但 Code-as-Interface 模式是「Agent 写代码来操作工具」。
- 如果这个范式成立，Hermes 的工具调用架构需要从「tool schema」进化到「code sandbox」。
- Lacuna 的类型检查思路直接启示 Hermes 的安全边界设计。

核心问题：**Code-as-Interface 是什么？它比传统 API 工具调用好在哪？对 Hermes 的工具架构意味着什么？**

## What To Learn

**学习路径**:
1. 精读 Perplexity Search as Code 文章 — 理解「Agent 写搜索代码」vs「Agent 调用搜索 API」的本质差异
2. 阅读 Lacuna 论文摘要 — 理解类型化程序空洞如何实现编译时 Agent 安全
3. 理解 GitHub MCP Server 1.2.0 的代码执行模式 vs 传统 REST 模式
4. 对比当前 Hermes MCP 工具调用模式与 Code-as-Interface 的架构差异
5. 产出：Code-as-Interface 范式评估 + Hermes 工具架构进化建议

**关键维度**:
- Token 效率：代码表达 vs JSON schema 表达 vs 自然语言表达
- 安全模型：沙箱隔离 vs URI 白名单 vs 类型检查
- 表达能力：代码的图灵完备性 vs API 的有限接口
- 可观测性：代码执行 trace vs API 调用日志
- 工程成熟度：沙箱技术（gVisor/Firecracker）的现状

## Expected Output

一篇 2-3 页的中文评估备忘录，包含：
1. Code-as-Interface 范式的定义、三种实现路线对比
2. 与传统 API 工具调用的对比分析（token 效率、安全性、表达力）
3. 对 Hermes 工具架构的进化建议（渐进路线 vs 激进路线）
4. 写入 `00-Inbox-AI/hermes/` 待审核

## 参考优先级

- P0 (必读): Perplexity Search as Code 文章 + Lacuna 摘要
- P1 (建议): GitHub MCP Server 1.2.0 release notes
- P2 (速览): 沙箱技术对比（gVisor vs Firecracker vs WASM）

## Suggested Domain

`Agent-Engineering`

## Desired Output

decision memo

## Proposed Canonical Destination

- `10-Knowledge/AI-Engineering/05-Topics/code-as-interface-paradigm.md`
- `30-Playbooks/Agent-Engineering/tool-architecture-patterns.md`（更新 Hermes 工具架构模式）

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## Suggested Review Date

`2026-06-25`

## Safety Notes

Code-as-Interface 的核心安全挑战是代码沙箱隔离。研究需评估当前沙箱技术的成熟度，以及 Hermes 工具调用从「声明式 schema」转向「代码执行」的安全风险增量。

## Hermes Recommendation

- Decision: `study`
- Rationale: 三条独立信号（Perplexity、Lacuna、GitHub MCP）在同周指向同一方向——这不是单一公司的产品发布，而是抽象层的范式转移。Tony 的 Hermes 重度依赖工具调用架构，理解这个范式是制定工具架构路线图的必要前置。价值高于单一模型/产品新闻。

## Follow-Up Proposal

- Suggested review cadence: 2 周
- Suggested spaced review prompt: 「如果 Hermes 的工具调用从 JSON schema 改为 code sandbox，最大的架构挑战是什么？」
