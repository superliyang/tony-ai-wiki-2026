---
title: AI 架构师专题分解图
type: map
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 架构师专题分解图

```mermaid
flowchart TB
  Core["AI 架构师能力"]

  subgraph App["应用架构"]
    RAG["RAG 架构"]
    Agent["Agent 架构"]
    Workflow["Workflow / HITL"]
  end

  subgraph Platform["平台架构"]
    Ops["LLMOps / AgentOps"]
    Cost["成本 / 延迟 / 容量"]
    Gateway["Model / Tool Gateway"]
  end

  subgraph Governance["治理架构"]
    Data["数据治理"]
    Security["AI 安全治理"]
    Eval["Eval / Release Gate"]
  end

  subgraph Output["架构师输出"]
    Review["架构评审"]
    Design["设计模板"]
    Landing["0 到 1 落地"]
  end

  Core --> App
  Core --> Platform
  Core --> Governance
  App --> Output
  Platform --> Output
  Governance --> Output
```

## 读图方式

- 应用架构回答“AI 怎么完成任务”。
- 平台架构回答“AI 怎么稳定、低成本、可观测地运行”。
- 治理架构回答“AI 怎么安全、合规、可审计地上线”。
- 架构师输出是评审、设计和落地，而不是停留在概念学习。

## Drill-down

- [[../05-Topics/RAG 架构师视角|RAG 架构师视角]]
- [[../05-Topics/Agent 架构师视角|Agent 架构师视角]]
- [[../05-Topics/LLMOps 与 AgentOps 架构师视角|LLMOps 与 AgentOps 架构师视角]]
- [[../05-Topics/AI 安全治理架构师视角|AI 安全治理架构师视角]]
- [[../05-Topics/AI 成本、延迟与容量架构师视角|AI 成本、延迟与容量架构师视角]]
- [[../05-Topics/AI 数据治理架构师视角|AI 数据治理架构师视角]]

