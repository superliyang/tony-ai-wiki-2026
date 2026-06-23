---
title: Runtime 发布门槛、灰度与 Blast Radius 控制
type: topic
status: learning
tags:
  - ai/engineering
  - ai/rollout
  - ai/agent-runtime
created: 2026-03-28
updated: 2026-03-28
---

# Runtime 发布门槛、灰度与 Blast Radius 控制

## 为什么 agent runtime 的 rollout 比普通 API 更危险

普通 API 的 rollout 出问题，通常影响的是：

- 某个 endpoint
- 某个 schema
- 某个服务的延迟或错误率

agent runtime 的 rollout 更复杂，因为它同时影响：

- capability 是否可见
- 工具是否可调用
- 权限是否正确
- memory / session 是否还能兼容
- background task 是否还能恢复

所以 runtime rollout 的单位不是“发一个新版本”，而是“改变一组能力边界”。

## 发布门槛至少要有 5 层

### 1. offline eval gate

发布前先过：

- dataset eval
- trace grading
- regression suites
- golden tasks

### 2. action-surface gate

新的 shell、browser、MCP、plugin、channel 命令不能只看“能不能执行”，还要看：

- approval 是否正常
- audit 是否完整
- timeout / cancel 是否生效
- network / filesystem policy 是否被正确约束

### 3. state-compatibility gate

任何影响 session、memory、artifact schema 的改动，都要先验证：

- 老 session 能否继续
- compaction 后能否恢复
- 老 artifacts 是否还能读取

### 4. rollout gate

先灰度，再放量：

- internal only
- project allowlist
- tenant allowlist
- feature flag segment
- default on

### 5. incident gate

上线前必须清楚：

- 谁能回滚
- 回滚多快
- 回滚后缓存多久清干净
- 是否需要清 session / clear cache / rotate permissions

## 现在业内常见的控制方法

### `OpenAI` 这一路线

从官方 docs 和状态事故可以看到：

- agent quality 强调 evals 与 trace grading
- shell/container 强调 environment policy 与 network allowlist
- 企业事故里明确强调：
  - multi-phase rollout
  - rollback mechanisms
  - permission anomaly metrics
  - feature-flag defensive gating

这说明 OpenAI 路线的发布门槛很清楚地分成：

- quality gate
- policy gate
- rollout gate

### `Claude Code` 这一路线

从官方 docs 看，最强控制点是：

- managed settings
- permissions deny / sandbox settings
- hooks in lifecycle
- worktree isolation
- memory / CLAUDE.md scope split

这条路线很适合做 repo-local 和 org-local gate：

- pre tool use deny
- permission review
- post tool use failure logging
- pre compact guard
- worktree-based rollout

### `OpenClaw` 这一路线

OpenClaw 更像长期在线 gateway，所以发布门槛更多会压在：

- plugin allow / deny
- plugin source / shadowing control
- node pairing / auth
- workspace / hook trust boundary
- hook-pack install rules
- session patch privilege

这条路线的重点不是“模型够不够好”，而是 control plane 能否把扩展面控制住。

### `ADK` 这一路线

ADK 的文档把 evaluation、deployment、artifacts、state 都放进了一个开发生命周期里。

这意味着它天然适合：

- 用 eval 作为发布前门槛
- 用 app/deploy 单元做版本边界
- 用 artifact / session schema 做 compatibility check

## blast radius 该怎么定义

### capability blast radius

- 一个 provider 挂了
- 一个 tool family 挂了
- 一整个 runtime surface 挂了

### tenant blast radius

- internal only
- single project
- single tenant
- enterprise-wide

### execution blast radius

- 同步会话受影响
- 背景任务受影响
- 只有 browser surface 受影响
- 只有 plugin surface 受影响

### state blast radius

- 只影响新 session
- 影响活跃 session
- 污染 durable memory
- 让老 artifacts 不可读

## 一个更稳的 rollout 策略

### 第 0 层：local / lab

- 本地 harness
- golden tasks
- 红队和失败样本

### 第 1 层：internal canary

- 少量开发者
- 少量固定任务
- 强 trace 和人工 review

### 第 2 层：allowlist tenant / project

- 明确租户
- 明确 capability set
- 新旧版本并行

### 第 3 层：default on but reversible

- 默认打开
- 保留快速关停与回退
- 强 anomaly alerts

### 第 4 层：fully promoted

- 发布完成
- 但 incident runbook 仍然要在线

## 什么时候不能继续放量

以下任一项不稳，都不应继续：

- approval 被绕过
- session 恢复失败率明显升高
- tool failure 无法分型
- plugin 加载异常无可观测性
- memory 写入污染率上升
- rollback 需要人工逐台清缓存

## 一个非常实用的发布检查清单

### quality

- 关键任务 eval 通过
- regression 无明显回退
- trace grading 无高优先级失败

### policy

- shell / browser / MCP / plugin 权限验证通过
- 审批点生效
- audit 字段完整

### state

- session 续跑通过
- compaction / resume 通过
- artifact schema backward-compatible

### rollout

- feature flag 可单独关闭
- 租户维度可灰度
- canary 指标已定义

### incident

- rollback owner 已明确
- cache 清理路径已演练
- kill switch 已验证

## 学这一页最该形成的判断力

### 判断 1：这次发布改的是“答案质量”，还是“能力边界”

后者通常更危险。

### 判断 2：这个功能最小可以灰度到哪一层

越复杂的 capability，越不该一上来全量。

### 判断 3：回滚是真回滚，还是“理论上可以回滚”

如果还要靠人工清大量缓存、修 session、改 memory，那就不算真正可回滚。

## 推荐怎么连着读

1. [[Agent Runtime 失败模式、事故复盘与 Postmortems]]
2. [[Agent 上线门槛与安全 Release Gates]]
3. [[AI Security Telemetry、Escalation 与 Incident Response]]
4. [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
5. [[Eval Harness 与 Regression Suites]]

## 相关主题

- [[Agent Runtime Architecture]]
- [[Agent Runtime 失败模式、事故复盘与 Postmortems]]
- [[Agent 上线门槛与安全 Release Gates]]
- [[Eval Harness 与 Regression Suites]]
- [[AI Security Telemetry、Escalation 与 Incident Response]]

## 资料

- [OpenAI Agent evals](https://developers.openai.com/api/docs/guides/agent-evals)
- [OpenAI Shell tool](https://developers.openai.com/api/docs/guides/tools-shell)
- [OpenAI RBAC incident write-up](https://status.openai.com/incidents/01K6KAAN7WXN69E8JET8PYB0D5/write-up)
- [Claude Code hooks reference](https://code.claude.com/docs/en/hooks)
- [Claude Code memory docs](https://code.claude.com/docs/en/memory)
- [OpenClaw Plugin Internals](https://docs.openclaw.ai/plugins/architecture)
- [OpenClaw Hooks](https://docs.openclaw.ai/automation/hooks)
- [ADK evaluation docs](https://google.github.io/adk-docs/evaluate/)
- [ADK deployment docs](https://google.github.io/adk-docs/deploy/agent-engine/deploy/)
