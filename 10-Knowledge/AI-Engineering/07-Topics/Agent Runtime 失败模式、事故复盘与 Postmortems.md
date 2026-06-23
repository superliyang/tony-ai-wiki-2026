---
title: Agent Runtime 失败模式、事故复盘与 Postmortems
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-runtime
  - ai/postmortem
created: 2026-03-28
updated: 2026-03-28
---

# Agent Runtime 失败模式、事故复盘与 Postmortems

## 为什么 runtime 这一层一定要补失败案例

当 agent 还只是 demo 时，大家更容易讨论：

- 会不会调工具
- 会不会写代码
- 会不会开浏览器

但一旦进入真实环境，真正把系统打疼的通常不是“模型答错一句”，而是 runtime 层的失败：

- 权限突然错配
- session 状态错乱
- 背景任务变黑盒
- hooks / plugins 带来副作用
- rollout 没控住 blast radius

所以 agent runtime 的成熟度，不只是靠 feature list 判断，更要看它如何面对失败、如何回滚、如何把事故缩在最小范围内。

## 先把失败模式分成 5 类

### 1. control-plane 失败

典型特征：

- 权限、feature flag、RBAC、route policy 配错
- 不是单个任务失败，而是整批 capability 突然不可用
- 往往影响多个工具面与多个租户

这类问题最危险，因为它会把“agent 有没有能力”直接改写掉。

### 2. execution-plane 失败

典型特征：

- shell / browser / MCP / SDK tools 某一条动作面失真
- 任务明明还在跑，但工具返回风格、权限或环境不再稳定
- 常见于环境漂移、container policy、browser state、network policy 变化

### 3. state-plane 失败

典型特征：

- session 丢失
- checkpoint 不一致
- memory 污染
- artifacts 没回流

这类问题会让系统表面上“还能继续说话”，但任务其实已经没法被稳定恢复。

### 4. rollout-plane 失败

典型特征：

- 新能力本身不一定错，但 rollout 太快
- 灰度不足
- 回滚路径不清
- 旧缓存、旧权限、旧 schema 还在污染新行为

### 5. observability-plane 失败

典型特征：

- 出问题了却不知道：
  - 谁受影响
  - 哪个 capability 失效
  - 失败从哪一步开始
  - 是否已恢复

这类问题不会直接造成 bug，但会把一个本可快速处理的问题拖成真正事故。

## 一个公开的 agent/control-plane 事故样本

### `OpenAI Enterprise/Edu RBAC` 事故

来自官方状态页的公开 write-up：

- 2025 年 10 月 2 日，OpenAI 在一次内部 backfill 中发生 permissions misconfiguration
- 企业与教育工作区继承了过于严格的权限
- `Codex`、`Agent Mode`、`Deep Research`、`MCP Connectors` 等功能对部分用户不可用
- 同时某些原本应关闭的功能又短暂暴露出来

官方在复盘里给出的关键信号非常值得学：

- root cause 不在模型，而在 permission rollout
- 恢复不只靠改配置，还要处理 cache propagation delay
- 预防措施集中在：
  - multi-phase rollout
  - rollback 机制
  - permission anomaly metrics
  - feature-flag defensive gating

这说明一件很重要的事：

`Agent runtime` 真正的高风险面，往往不是 reasoning，而是 capability exposure 和 control-plane consistency。

## 从官方文档反推的高频事故类型

下面这些并不是每家都公开写成事故报告；其中很多结论是我基于官方文档和运行模型做的工程推断。

### `Claude Code` 这一线

从官方文档能看到：

- hooks 可以在 `PreToolUse`、`PermissionRequest`、`PostToolUseFailure`、`PreCompact` 等关键点介入
- subagent 可以跑在 `worktree` 隔离环境里
- auto memory 与 `CLAUDE.md` 是不同层

由此可以推断出几类高频失败：

- hook 决策错误，误封或误放高风险工具
- worktree / main tree 假设不一致，导致 review handoff 混乱
- auto memory 记录了临时偏差，后续 session 被污染
- compaction 前该落盘的东西没落，导致长任务断裂

### `OpenClaw` 这一线

从官方 docs 能看到：

- native plugins 与 gateway 同进程运行
- plugins.allow 信任的是 plugin id，而不是来源本身
- workspace plugin 可以 shadow bundled plugin
- hooks、webhooks、cron、nodes、channels 都会汇到 Gateway control plane
- memory flush 在只读 workspace 下会被跳过

由此可以推断出几类典型失败：

- plugin shadowing 让实际运行的不是你以为的那份插件
- hook / plugin 代码本身 destabilize gateway
- automation 太多时，事件风暴和 session patch 冲突更明显
- memory flush 被跳过后，长任务在 compaction 后丢失关键上下文

### `OpenAI tools/runtime` 这一线

从官方 docs 能看到：

- `shell` 明确要求 sandbox、allow/deny policy、审计日志
- hosted container 默认没有外网，network policy 需要显式 allowlist
- agent evals 明确强调 trace grading 和 reproducible evaluations

由此可以推断出几类失败：

- shell executor 没做真正隔离，动作面超出预期
- rollout 时 network policy 变化导致一批工具突然不可用
- evaluator 不完善时，workflow regression 会先在线上暴露

### `Google ADK` 这一线

从官方 docs 能看到：

- session state、artifacts、callbacks、evaluation 都是一级能力
- deployment、evaluation、web UI 都在同一开发生命周期里

这意味着 ADK 路线的高频失败更像：

- callback / state schema drift
- artifact contract 变化后下游看不懂
- eval 没接进发布流程，导致部署前没有真实回归门槛

## 事故复盘时最该问的 8 个问题

1. 故障属于 control plane、execution plane、state plane 还是 rollout plane
2. 影响的是 capability availability，还是 result quality
3. 受影响的是所有用户、某些租户、还是某类 session
4. 任务是否还能恢复，还是只能重跑
5. 中间 artifacts 是否保住了
6. 失败是否可观测，还是只能靠用户报障
7. rollback 是 feature-level、route-level，还是只能整版回退
8. 预防措施是否进入 release gate，而不只是写在 postmortem 里

## 一个更稳的复盘框架

### 事故摘要

- 何时开始
- 何时发现
- 何时缓解
- 何时完全恢复

### blast radius

- 哪些用户 / agent / tools / channels 受影响
- 是否跨租户
- 是否跨环境

### runtime breakdown

- 入口层
- 状态层
- 工具层
- 权限层
- 观测层
- 交付层

### why it escaped

- 没有 eval
- 没有 canary
- 没有 approval gate
- 没有 anomaly alert
- 没有 rollback rehearsal

### concrete prevention

- 新增哪条 guardrail
- 哪个 feature flag 改成更细粒度
- 哪个指标变成 hard gate
- 哪个 artifact / trace 成为必留存

## 学这一页最该形成的判断力

### 判断 1：故障真正属于哪一层

如果把所有 agent 问题都归因到模型，你会错过真正的工程原因。

### 判断 2：哪些 failure 可以接受，哪些必须在 release 前挡住

- 文风轻微漂移：可以容忍
- 权限错配导致 capability 全掉：必须挡在上线前
- memory 污染造成跨任务误导：必须有 write policy
- background task 黑盒且不可取消：必须先补 controls

### 判断 3：事故后的真正资产是什么

不是“写了一篇复盘”，而是：

- 新的 metric
- 新的 release gate
- 新的 rollback step
- 新的 audit field

## 推荐怎么连着读

1. [[Runtime 发布门槛、灰度与 Blast Radius 控制]]
2. [[Plugin、Memory 与 Background Task 失效模式]]
3. [[Agent 上线门槛与安全 Release Gates]]
4. [[Enterprise AI Security Operating Model]]
5. [[AI Security Telemetry、Escalation 与 Incident Response]]

## 相关主题

- [[Agent Runtime Architecture]]
- [[Background Agents]]
- [[Session and Memory Design]]
- [[Task Success and Failure Recovery]]
- [[Long-Running Agent Operations]]
- [[Runtime 发布门槛、灰度与 Blast Radius 控制]]
- [[Plugin、Memory 与 Background Task 失效模式]]

## 资料

- [OpenAI Status: Enterprise/Edu RBAC incident write-up](https://status.openai.com/incidents/01K6KAAN7WXN69E8JET8PYB0D5/write-up)
- [OpenAI Shell tool docs](https://developers.openai.com/api/docs/guides/tools-shell)
- [OpenAI Agent evals docs](https://developers.openai.com/api/docs/guides/agent-evals)
- [Claude Code hooks reference](https://code.claude.com/docs/en/hooks)
- [Claude Code memory docs](https://code.claude.com/docs/en/memory)
- [Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents)
- [OpenClaw Plugin Internals](https://docs.openclaw.ai/plugins/architecture)
- [OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)
- [OpenClaw Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- [ADK evaluation docs](https://google.github.io/adk-docs/evaluate/)
