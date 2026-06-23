---
title: Coding Agent Workflow Engineering Map
type: map
status: learning
tags:
  - ai/map
  - ai/coding-agent
  - ai/engineering
created: 2026-03-22
updated: 2026-03-22
---

# Coding Agent Workflow Engineering Map

```mermaid
flowchart TD
  A["Human Owner"] --> B["Task Decomposition"]
  B --> C["Interactive Pair Agent"]
  B --> D["Background Implementer Agent"]
  B --> E["Reviewer Agent"]

  C --> C1["terminal / IDE collaboration"]
  D --> D1["cloud env / sandbox / worktree"]
  E --> E1["PR review / bug finding / test gaps"]

  D --> F["Patch / PR / Artifact"]
  E --> F
  F --> G["CI / Tests / Policy Checks"]
  G --> H["Human Review and Merge"]

  D1 --> I["environment consistency"]
  D1 --> J["budget / timeout / approvals"]
  F --> K["result handoff"]
  G --> L["traceability / auditability"]
```

## 怎么读这张图

- 这张图关注的是 coding agent 怎么进入真实软件工程流程
- 左边更偏任务拆分与角色分工
- 中间更偏执行环境和结果回收
- 右边更偏治理、审查和合并控制

## 相关

- [[../07-Topics/Background Agents|Background Agents]]
- [[../07-Topics/Delegation and Task-Oriented Agents|Delegation and Task-Oriented Agents]]
- [[../07-Topics/Multi-Agent Coding Workflow|Multi-Agent Coding Workflow]]
- [[../07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
- [[../07-Topics/Planning Loops and State Machines|Planning Loops and State Machines]]
- [[Agent Runtime Engineering Map]]
