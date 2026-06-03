---
title: AI Coding 团队落地路线图
type: map
status: active
tags:
  - ai/map
  - ai/coding-agent
  - ai/engineering
created: 2026-05-16
updated: 2026-05-16
---

# AI Coding 团队落地路线图

## 图谱意图

这是一张 `roadmap`，回答一个问题：

> 团队如何从个人试用 coding agent，走到可治理、可评估、可规模化的 AI Coding 工作方式？

## 图谱

```mermaid
flowchart LR
  P0["P0 个人试用<br/>单人 / 单仓 / 低风险"]
  P1["P1 项目规则<br/>CLAUDE.md / 命令 / 边界"]
  P2["P2 任务闭环<br/>Bugfix / Test / Review"]
  P3["P3 能力沉淀<br/>Skills / Subagents / Hooks"]
  P4["P4 工作流接入<br/>PR / CI / Issue / Docs"]
  P5["P5 团队治理<br/>Policy / Eval / Metrics"]

  P0 --> P1 --> P2 --> P3 --> P4 --> P5

  P0a["选低风险任务"]
  P0b["人工全量 review"]
  P1a["项目记忆"]
  P1b["敏感路径"]
  P2a["标准任务 brief"]
  P2b["验证命令"]
  P3a["高频 skill"]
  P3b["质量 hook"]
  P4a["PR workflow"]
  P4b["CI log / Issue MCP"]
  P5a["Eval Pack"]
  P5b["ROI / Risk 指标"]

  P0 --> P0a
  P0 --> P0b
  P1 --> P1a
  P1 --> P1b
  P2 --> P2a
  P2 --> P2b
  P3 --> P3a
  P3 --> P3b
  P4 --> P4a
  P4 --> P4b
  P5 --> P5a
  P5 --> P5b

  P5 -.复盘回写.-> P1
  P5 -.能力升级.-> P3

  classDef phase fill:#edf7ed,stroke:#2f8f46,color:#111827
  classDef item fill:#fff4e5,stroke:#d97706,color:#111827
  classDef control fill:#f5e8ff,stroke:#7e22ce,color:#111827

  class P0,P1,P2,P3,P4 phase
  class P0a,P0b,P1a,P1b,P2a,P2b,P3a,P3b,P4a,P4b item
  class P5,P5a,P5b control
```

## 落地判断

- 如果没有 `P1 项目规则`，不要急着上团队插件
- 如果没有 `P2 任务闭环`，不要把 agent 接入 PR / CI
- 如果没有 `P5 团队治理`，不要给 agent 高权限工具和生产数据
- 最好每一阶段都有明确验收指标，而不是靠“感觉效率变高”

## 阶段验收

| 阶段 | 验收问题 |
|---|---|
| P0 | 是否能稳定完成低风险任务 |
| P1 | 项目规则是否足够让 agent 自己进入状态 |
| P2 | 是否有标准 brief、验证命令和 review 输出 |
| P3 | 是否沉淀出复用 skill / subagent / hook |
| P4 | 是否能安全接入 PR、CI、issue、docs |
| P5 | 是否有 eval、权限、审计、ROI 和失败复盘 |

## 相关

- [[../07-Topics/Claude Code Harness 工程实践|Claude Code Harness 工程实践]]
- [[../07-Topics/Harness Engineering|Harness Engineering]]
- [[Coding Agent Workflow Engineering Map]]
- [[AI Coding 安全治理决策图]]
- [[../../AI-Learning/06-Topics/AI Coding 专家能力体系|AI Coding 专家能力体系]]

