---
title: AI Coding 专家能力图谱
type: map
status: active
tags:
  - ai/map
  - ai/coding-agent
  - ai/workbench
created: 2026-05-16
updated: 2026-05-16
---

# AI Coding 专家能力图谱

## 图谱意图

这是一张 `capability-map`，回答一个问题：

> 个人如何从“会用 coding agent”成长为“能设计 AI Coding 工作台”的专家？

## 图谱

```mermaid
flowchart TB
  Start["AI Coding 专家"]

  A["任务建模<br/>目标 / 范围 / 验证"]
  B["上下文工程<br/>Repo / Issue / Memory"]
  C["工具面设计<br/>Shell / Git / MCP"]
  D["扩展面沉淀<br/>Skills / Agents / Hooks"]
  E["验证治理<br/>Tests / Review / Gates"]
  F["团队落地<br/>Plugin / Policy / Metrics"]

  A1["Task Brief"]
  A2["Repo Map"]
  B1["CLAUDE.md / AGENTS.md"]
  B2["Session Summary"]
  C1["Least Privilege"]
  C2["Read-only First"]
  D1["Skill Library"]
  D2["Subagent Roles"]
  E1["Eval Pack"]
  E2["Audit / Rollback"]
  F1["Team Workflow"]
  F2["Incident Library"]

  Start --> A --> B --> C --> D --> E --> F

  A --> A1
  A --> A2
  B --> B1
  B --> B2
  C --> C1
  C --> C2
  D --> D1
  D --> D2
  E --> E1
  E --> E2
  F --> F1
  F --> F2

  E -.失败复盘.-> D
  F -.团队反馈.-> B

  classDef goal fill:#e8f1ff,stroke:#3973d6,color:#111827
  classDef core fill:#edf7ed,stroke:#2f8f46,color:#111827
  classDef detail fill:#fff4e5,stroke:#d97706,color:#111827
  classDef control fill:#f5e8ff,stroke:#7e22ce,color:#111827

  class Start goal
  class A,B,C,D,F core
  class A1,A2,B1,B2,C1,C2,D1,D2,F1,F2 detail
  class E,E1,E2 control
```

## 怎么读

- 左到右是成长路径：先会描述任务，再会管理上下文，再会控制工具，最后形成团队能力
- `扩展面沉淀` 是分水岭：没有沉淀，AI Coding 只是一次次临时对话
- `验证治理` 是上线门槛：没有测试、review、审计、回滚，就不能进入真实工程机制

## 推荐钻取

- [[../06-Topics/AI Coding 专家能力体系|AI Coding 专家能力体系]]
- [[Claude Code 生态能力图]]
- [[../../AI-Engineering/08-Maps/AI Coding 团队落地路线图|AI Coding 团队落地路线图]]
- [[../../AI-Engineering/08-Maps/AI Coding 安全治理决策图|AI Coding 安全治理决策图]]

