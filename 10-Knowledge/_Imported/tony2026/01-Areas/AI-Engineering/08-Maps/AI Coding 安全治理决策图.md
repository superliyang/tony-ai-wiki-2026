---
title: AI Coding 安全治理决策图
type: map
status: active
tags:
  - ai/map
  - ai/coding-agent
  - ai/security
  - ai/governance
created: 2026-05-16
updated: 2026-05-16
---

# AI Coding 安全治理决策图

## 图谱意图

这是一张 `decision-map`，回答一个问题：

> 当 coding agent 要获得文件、命令、MCP、PR、CI、数据库等能力时，应该如何决定权限和门禁？

## 图谱

```mermaid
flowchart TB
  Q["权限决策问题<br/>Agent 要做什么动作？"]

  S1["读上下文<br/>文件 / 文档 / Issue"]
  S2["改代码<br/>Patch / Refactor / Test"]
  S3["跑命令<br/>Shell / Git / Build"]
  S4["接外部系统<br/>MCP / CI / Logs"]
  S5["影响协作流<br/>PR / Review / Merge"]
  S6["触达敏感面<br/>Secret / Prod / Data"]

  G1["默认只读"]
  G2["限定路径"]
  G3["人工审批"]
  G4["自动测试"]
  G5["审计日志"]
  G6["禁止或隔离"]

  O["允许执行<br/>低风险闭环"]
  R["需要升级审批<br/>中高风险动作"]
  B["阻断执行<br/>高危或越界"]

  Q --> S1 --> G1 --> O
  Q --> S2 --> G2 --> G4 --> O
  Q --> S3 --> G3 --> R
  Q --> S4 --> G1 --> G5 --> R
  Q --> S5 --> G3 --> G5 --> R
  Q --> S6 --> G6 --> B

  O -.失败或异常.-> R
  R -.发现越界.-> B
  R -.审批通过.-> O

  classDef question fill:#e8f1ff,stroke:#3973d6,color:#111827
  classDef surface fill:#fff4e5,stroke:#d97706,color:#111827
  classDef guard fill:#f5e8ff,stroke:#7e22ce,color:#111827
  classDef allow fill:#edf7ed,stroke:#2f8f46,color:#111827
  classDef block fill:#fee2e2,stroke:#dc2626,color:#111827

  class Q question
  class S1,S2,S3,S4,S5,S6 surface
  class G1,G2,G3,G4,G5,G6 guard
  class O allow
  class R guard
  class B block
```

## 决策原则

- 读上下文：默认允许，但要控制敏感路径和数据范围
- 改代码：限定目录和任务范围，必须能 diff 和 review
- 跑命令：危险 shell / destructive git 默认人工审批
- 接外部系统：先只读，再逐步开放写入动作
- 影响协作流：PR comment 可以低风险，merge / release 必须人工控制
- 触达敏感面：secret、生产数据、支付、安全配置默认阻断或隔离环境执行

## 推荐门禁组合

- `低风险任务`：只读上下文 + 限定文件修改 + 局部测试
- `中风险任务`：人工审批 + CI / review + 审计日志
- `高风险任务`：sandbox / worktree / staging + 安全审查 + release gate
- `禁止任务`：生产 secret、生产写库、绕过鉴权、破坏性 Git 历史改写

## 相关

- [[../07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]
- [[../07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]
- [[../07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
- [[AI Coding 团队落地路线图]]
- [[../../AI-Learning/06-Topics/AI Coding 专家能力体系|AI Coding 专家能力体系]]

