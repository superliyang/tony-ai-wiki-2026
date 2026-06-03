---
title: AI Coding 专家能力验收矩阵
type: evaluation
status: active
tags:
  - ai/evaluation
  - ai/coding-agent
  - ai/governance
created: 2026-05-16
updated: 2026-05-16
---

# AI Coding 专家能力验收矩阵

## 这张矩阵判断什么

这张矩阵不是评测某个模型的绝对能力，而是评测一个人或团队是否已经具备“可落地的 AI Coding 能力”。

它连接三层：

- 个人能力：能否完成真实 repo 任务
- 工程机制：能否沉淀 skills、subagents、hooks、MCP 和评测
- 团队治理：能否控制权限、风险、质量和 ROI

## 验收维度

| 维度 | Level 1：能用 | Level 2：能复用 | Level 3：能团队化 |
|---|---|---|---|
| 任务建模 | 能写清目标 | 能写标准 brief | 能形成团队模板 |
| 上下文工程 | 能找相关文件 | 能维护 repo map / memory | 能治理项目记忆和恢复机制 |
| 工具面 | 能跑命令 | 能区分权限和风险 | 能制定工具权限策略 |
| 扩展面 | 会用现成扩展 | 能写 skill / subagent / hook | 能打包团队 plugin |
| 验证 | 会跑测试 | 能设计任务级验收 | 能接 eval pack / release gate |
| 安全 | 知道危险命令 | 能设审批和阻断 | 能做审计、回滚、事故复盘 |
| 协作 | 能写 PR summary | 能处理 review follow-up | 能嵌入 PR / CI / issue 流 |
| 复盘 | 能总结一次任务 | 能抽出复用规则 | 能维护失败案例库 |

## 指标建议

### 质量指标

- task completion rate
- test pass after patch
- review rework rate
- unnecessary file touch rate
- hallucinated explanation rate

### 安全指标

- unsafe command attempt rate
- sensitive path violation
- secret exposure attempt
- unapproved external write
- rollback readiness

### 效率指标

- time to first useful patch
- human review time saved
- repeated task automation rate
- skill reuse count
- PR cycle time impact

### 团队指标

- onboard time for new repo
- team adoption rate
- policy exception count
- incident / near-miss count
- cost per accepted change

## 最小验收门槛

个人可用：

- 完成 3 个低风险 repo 任务
- 测试或验证记录清楚
- 无危险命令直接执行
- 无明显无关文件修改

项目可用：

- 有项目级规则文件
- 有至少 2 个复用 skills
- 有至少 1 个 review / test subagent
- 有至少 1 个安全或质量 hook
- 有任务记录模板和复盘机制

团队试点：

- 有权限策略
- 有敏感路径策略
- 有 PR / CI 接入边界
- 有 eval pack 或验收矩阵
- 有暂停和退出条件

## 评分方式

每个维度按 `0-3` 分：

- `0`：没有机制
- `1`：个人临时能做到
- `2`：项目内可重复
- `3`：团队内可治理

建议门槛：

- `>= 12`：个人可用
- `>= 18`：项目可用
- `>= 22`：团队试点
- `>= 26`：可扩大推广

## 与任务包的关系

- 用 [[Coding Agent Eval Pack：Repo 修复、测试与小型重构|Coding Agent Eval Pack]] 测 agent 具体任务表现
- 用本矩阵判断个人和团队是否具备落地能力
- 用 [[../06-Projects/AI Coding Lab/AI Coding Lab 实战任务记录模板|AI Coding Lab 实战任务记录模板]] 保留过程证据

## 关联

- [[../06-Projects/AI Coding Lab/项目总览|AI Coding Lab]]
- [[../06-Projects/AI Coding Lab/AI Coding Lab 专家验收清单|AI Coding Lab 专家验收清单]]
- [[../08-Maps/AI Coding 团队落地路线图|AI Coding 团队落地路线图]]
- [[../08-Maps/AI Coding 安全治理决策图|AI Coding 安全治理决策图]]

