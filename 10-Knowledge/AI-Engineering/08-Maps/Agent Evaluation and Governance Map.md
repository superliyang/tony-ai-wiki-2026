---
title: Agent Evaluation and Governance Map
type: map
status: learning
tags:
  - ai/map
  - ai/agent
  - ai/evaluation
created: 2026-03-22
updated: 2026-03-25
---

# Agent Evaluation and Governance Map

```mermaid
flowchart TD
  A["Agent Runtime"] --> B["Agent Evaluation and Reliability"]
  A --> C["Task Success and Failure Recovery"]
  A --> D["Cost, Latency, and Safety Tradeoffs"]
  A --> E["Human-in-the-Loop and Approval Gates"]
  A --> F["Eval Harness / Regression"]

  B --> B1["task completion"]
  B --> B2["tool success rate"]
  B --> B3["repeatability"]

  C --> C1["retry / re-plan / rollback"]
  C --> C2["escalation"]
  C --> C3["stuck-session handling"]

  D --> D1["cheap vs strong"]
  D --> D2["fast vs safe"]
  D --> D3["throughput vs control"]

  E --> E1["approval gates"]
  E --> E2["audit / review"]

  F --> F1["trace grading"]
  F --> F2["regression suite"]
  F --> F3["promotion gate"]
```

## 怎么读这张图

- 左边是 agent 系统进入生产后的四个核心治理问题
- 上面更偏“怎么评这个系统到底稳不稳”
- 下面更偏“当系统真的跑起来时，怎么在成本、速度和风险之间做决策”
- 这张图最适合和 `Agent Runtime Engineering Map` 配合看：前者讲怎么搭，后者讲怎么管

## 推荐顺序

1. [[../07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
2. [[../07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]]
3. [[../07-Topics/Harness Engineering|Harness Engineering]]
4. [[../07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
5. [[../07-Topics/Agent Evaluation and Reliability|Agent Evaluation and Reliability]]
6. [[../07-Topics/Task Success and Failure Recovery|Task Success and Failure Recovery]]
7. [[../07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
8. [[../07-Topics/Cost, Latency, and Safety Tradeoffs|Cost, Latency, and Safety Tradeoffs]]

## 关联

- [[Agent Runtime Engineering Map]]
- [[Harness Feedback Loop Map]]
- [[Coding Agent Workflow Engineering Map]]
- [[../07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
- [[../07-Topics/Safety Evaluation|Safety Evaluation]]
