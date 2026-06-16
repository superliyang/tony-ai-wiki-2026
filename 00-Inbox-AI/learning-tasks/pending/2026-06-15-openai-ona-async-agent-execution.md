---
title: "OpenAI Ona 收购与 Agent 异步持久执行范式"
created: 2026-06-15
updated: 2026-06-15
status: pending
owner: hermes
priority: P2
domain: "AI-Engineering"
review_after: "2026-07-06"
tags:
  - learning-task
  - hermes
  - async-agent
  - agent-execution
  - openai
  - ona
  - long-running-agent
  - codex
sources:
  - "https://www.techtimes.com/articles/318338/20260613/openai-acquires-ona-run-codex-coding-agents-hours-without-your-computer.htm"
---

# OpenAI Ona 收购与 Agent 异步持久执行范式

## Why Now

2026-06-13，OpenAI 收购了 Ona——一家专注于让 Codex 编程 Agent 在开发者电脑关闭后持续运行数小时的公司。这不是一次普通的 AI 收购，而是 **Agent 执行范式的根本性转变信号**。

**为什么这次收购值得深入研究：**

1. **从"同步工具"到"异步员工"** — Agent 不再是"你问-我答"的同步工具，而是能接受任务后离线自主工作数小时的数字代理。这是 Agent 从 Copilot 到 Autopilot 的关键转变。
2. **平台级能力 vs 应用级工程** — 现有 `longrunning-agent-engineering`（pending P2）关注的是"我如何设计系统让它跑一周"（应用层工程），而 Ona 收购代表的是平台层（OpenAI）对"Agent 异步执行"的基础设施级押注。这是范式层的差异。
3. **直接关联 Hermes Cognitive OS** — Hermes 的 cron jobs、Codex 的学习任务处理、OpenHuman 的持续摄入，都涉及"离线运行"模式。理解 OpenAI 如何设计 Agent 的异步执行基础设施，直接影响 Hermes/Codex 的任务编排架构。

**对 Tony/Hermes 的影响：**
- Hermes 的 cron scout 本质上是"定时唤醒-执行-休眠"的异步 Agent。Ona 的"持续运行数小时"模式是否更优？
- Codex 的学习任务处理：当前是 Tony 触发 → Codex 执行。Ona 模式支持"提交任务 → Agent 离线完成 → 推送结果"
- 与 `agent-routing-longrunning`（模型选择）和 `longrunning-agent-engineering`（系统工程）互补：Ona 看平台能力，那两个看应用层

## Source

- URL: 见 frontmatter sources
- Source note: TechTimes 报道（OpenAI Ona 收购），基于 OpenAI 官方公告
- Captured evidence: `00-Inbox-AI/hermes/curated-scout/20260614-210005-summary.md` #4（异步执行），`20260614-160000-afternoon-digest.md`（无直接覆盖，但增量雷达标记了 Ona），`20260615-061431-summary.md`（未直接覆盖）

## Suggested Domain

`AI-Engineering`

## Desired Output

learning package + decision memo

具体应覆盖：
1. Ona 技术解析：Ona 如何实现 Agent 在开发者离线后持续运行？（推测：云端执行环境 + 状态快照 + 结果回调）
2. Agent 异步执行的三种模式对比：
   - Cron 模式（定时唤醒-执行-休眠）→ Hermes 当前模式
   - 持续运行模式（always-on agent with state checkpoint）→ Ona 模式
   - 事件驱动模式（webhook 触发 → agent 执行）→ 混合模式
3. 平台级异步 Agent 的关键基础设施：任务队列、状态持久化、故障恢复、结果通知
4. 行业对比：Anthropic Claude Code 的 async 支持 vs OpenAI Codex + Ona vs Google Gemini CLI
5. 对 Hermes Cognitive OS 的启示：Hermes/Codex 是否需要"离线持续执行"模式？什么场景下 cron 更优，什么场景下 Ona 模式更优？

## Proposed Canonical Destination

- `10-Knowledge/AI-Cognitive-System/05-Topics/Agent 异步执行范式.md`
- `90-Agent-System/decisions/2026-06-xx-agent-execution-model.md`（如需架构决策）

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## Suggested Review Date

`2026-07-06`

## Safety Notes

- Ona 的具体技术实现未公开——产出应标注信息来源的局限性
- OpenAI 收购后的集成进度未知——分析应以"范式讨论"为主，不依赖具体产品细节
- 如涉及对 Hermes/Codex 执行模型做生产变更，需 Tony 审核后执行
- 异步 Agent 的执行环境涉及凭证管理和沙箱安全——这是安全审记的关键点

## Hermes Recommendation

- Decision: `study`
- Rationale: OpenAI 作为 Agent 平台方收购 Ona，代表"Agent 异步持久执行"从工程技巧升级为平台能力。这对 Tony 的 Cognitive OS 有直接架构启示：Hermes 的 cron 模式 vs Codex 的同步触发模式 vs 未来可能的持续运行模式。与 `longrunning-agent-engineering`（应用层工程）互补——本任务看平台层范式，那个任务看应用层实现。

## Follow-Up Proposal

- Suggested review cadence: 3 周后扫描 OpenAI 是否公开了 Ona 集成后的 Codex async 能力
- Suggested spaced review prompt: 「OpenAI 是否在 Codex CLI 中集成了 Ona 的异步能力？Anthropic Claude Code 是否有类似的 async 支持？Hermes/Codex 的当前执行模式是否需要调整？」
