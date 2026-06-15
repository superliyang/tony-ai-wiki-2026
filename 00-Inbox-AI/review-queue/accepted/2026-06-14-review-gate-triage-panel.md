---
title: "Tony Review: Review Gate Triage Panel"
created: 2026-06-14
updated: 2026-06-14
status: accepted
type: review-triage-panel
source: codex
decision: "default recommendations accepted"
decided: 2026-06-14
tags:
  - review
  - triage
  - learning-task
  - ai-first
---

# Tony Review: Review Gate Triage Panel

## Decision

Tony accepted the default recommendations on 2026-06-14.

这个面板把 5 个 substantive review 压成一次轻量判断。目标不是现在读完所有 package，而是让队列开始流动。

建议 Tony 只选：

```text
accept
accept-with-verification
watch
defer
discard
```

## Recommended Batch Decision

我的默认建议：

| Review | Recommended Decision | Why |
|---|---|---|
| Agent 记忆架构 | `accept -> build` | 直接影响 Hermes/Codex 记忆边界，是当前 Cognitive OS 的核心底座 |
| MCP 协议演进 | `watch -> build-checklist` | 重要但 spec/生态仍在变化，应先做接入审查清单，不急着升级 |
| 广告投放领域结晶 | `accept-with-verification` | 结构价值高，但数字、benchmark、比例必须做 URL 级来源校验 |
| AI 递归自我改进 | `watch -> governance-gate` | 话题重要，但事实不宜写死；更适合沉淀为 self-improvement gate |
| Agent 模型架构 | `accept -> build` | Hermes 已经遇到模型/路由问题，应该转成模型路由矩阵和评测样例 |

## 1. Agent 记忆架构

Source review:

- [[00-Inbox-AI/review-queue/pending/2026-06-05-agent-memory-architecture-review]]
- [[00-Inbox-AI/learning-tasks/accepted/2026-06-05-agent-memory-architecture-package]]

### One-Line Conclusion

Agent memory 不是“存聊天记录”，而是一个需要 review、TTL、遗忘、来源、置信度和注入预算的长期治理系统。

### Why It Matters

这是 Tony AI First Cognitive System 的地基之一。Hermes、OpenHuman、Codex 都会产生记忆候选；如果没有 promotion gate，长期系统会被未经审查的偏好、旧事实和推断污染。

### Recommended Decision

```text
accept -> build
```

### Follow-Up If Accepted

- 生成 `Agent Memory schema`。
- 生成 `Agent 记忆晋升与遗忘流程` playbook。
- 更新 Hermes memory review 输出规则：daily review 进入 `00-Inbox-AI/hermes/memory-review/`，高置信候选才进入 review queue。

### Main Risk

不要把任何 runtime memory store 直接接到 canonical vault。Obsidian/GitHub 仍然是长期事实源。

## 2. MCP 协议演进

Source review:

- [[00-Inbox-AI/review-queue/pending/2026-06-05-mcp-protocol-evolution-review]]
- [[00-Inbox-AI/learning-tasks/accepted/2026-06-05-mcp-protocol-evolution-package]]

### One-Line Conclusion

MCP 正从本地工具协议变成 Agent infrastructure 协议，但当前更适合 watch 和制定接入审查清单，不适合直接升级核心依赖。

### Why It Matters

Hermes/Codex/Cursor 的工具调用、remote MCP server、权限、日志、回滚都会受 MCP 生态演进影响。

### Recommended Decision

```text
watch -> build-checklist
```

### Follow-Up If Accepted

- 建立 `MCP 接入审查清单`。
- 建立 MCP watchlist，重点跟踪 Streamable HTTP、stateless MCP、header routing、remote managed MCP server。
- 暂不升级核心 Hermes MCP 依赖，先做测试环境验证。

### Main Risk

部分来源仍需 freshness / URL 校验；不要把 RC 或二级媒体信息写成正式架构事实。

## 3. 广告投放领域结晶

Source review:

- [[00-Inbox-AI/review-queue/pending/2026-06-05-advertising-domain-review]]
- [[00-Inbox-AI/learning-tasks/accepted/2026-06-06-advertising-domain-crystallization-package]]

### One-Line Conclusion

广告投放这批材料结构质量高，适合作为领域学习闭环样板，但必须先校验 benchmark、比例、平台数据和行业数字。

### Why It Matters

这是 Hermes -> Codex -> Tony -> canonical promotion 的领域知识结晶样板。如果跑通，可复制到其他领域。

### Recommended Decision

```text
accept-with-verification
```

### Follow-Up If Accepted

- Codex 做 bounded URL-level source verification。
- 校验后再接受或修正 `10-Knowledge/Advertising/` canonical tree。
- 决定 Advertising playbook 是放 `30-Playbooks/Advertising/` 还是保持 domain-local `10-Knowledge/Advertising/10-Playbooks/`。

### Main Risk

未经校验的数字锚点会污染正式知识库；不应把 5 个 draft 原封 promote。

## 4. AI 递归自我改进

Source review:

- [[00-Inbox-AI/review-queue/pending/2026-06-07-ai-recursive-self-improvement-review]]
- [[00-Inbox-AI/learning-tasks/accepted/2026-06-07-ai-recursive-self-improvement-package]]

### One-Line Conclusion

RSI 作为宏观判断还不能写死；对 Tony 系统最有用的是建立 Agent self-improvement gate。

### Why It Matters

Hermes/Codex/OpenHuman/ECC 都可能提议改 rules、skills、memory、workflow、MCP 接入或模型路由。必须有审查、来源、回滚和权限边界。

### Recommended Decision

```text
watch -> governance-gate
```

### Follow-Up If Accepted

- 建立 `Agent 自我改进审查清单`。
- 建立 RSI watchlist，区分 verified / reported / inferred / speculative。
- 明确 Hermes 不可自动升级自身规则、skills、memory policy 或 automation。

### Main Risk

不要把“AI 已经设计 OpenAI 下一代模型”写成事实；这仍是高影响但未确认信号。

## 5. Agent 模型架构

Source review:

- [[00-Inbox-AI/review-queue/pending/2026-06-08-agent-model-architecture-review]]
- [[00-Inbox-AI/learning-tasks/accepted/2026-06-08-agent-model-architecture-package]]

### One-Line Conclusion

Hermes 不能只用一个默认模型跑所有任务；需要按 scout、learning package、promotion gate、memory review、coding 等工作负载做模型路由。

### Why It Matters

Hermes live test 已经暴露过模型/provider 路径差异；长期 Agent 的成本、延迟、可靠性不能只看单 token 价格或通用聊天榜单。

### Recommended Decision

```text
accept -> build
```

### Follow-Up If Accepted

- 生成 `Hermes 模型路由矩阵`。
- 建立小型评测样例：scout、summarize、review gate、project companion、memory review。
- 记录 `cost_to_correct_task_completion`、retry count、wall-clock time、source quality、human correction rate。

### Main Risk

不要把供应商的 “agent model” 定位等同于真实效果；必须用 Tony/Hermes 自己的任务测。

## Suggested Execution Order

如果 Tony 接受默认建议，Codex 后续按这个顺序处理：

1. Agent 记忆架构：先 build schema / memory gate，因为它能减少 review queue 噪音。
2. Agent 模型架构：建立 Hermes 模型路由矩阵，解决实际运行质量。
3. MCP 协议演进：做接入审查清单和 watchlist。
4. AI 递归自我改进：做 self-improvement gate。
5. 广告投放领域结晶：安排独立 source verification pass。

## Tony Decision Box

Tony 可以直接回复一行：

```text
同意默认建议
```

或者逐项覆盖：

```text
Agent Memory: accept -> build
MCP: watch
Advertising: defer
RSI: watch -> governance-gate
Agent Model: accept -> build
```
