---
title: 扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation
type: topic
status: learning
tags:
  - ai/engineering
  - ai/plugins
  - ai/skills
  - ai/automation
created: 2026-04-03
updated: 2026-04-03
---

# 扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation

## 为什么扩展面是 agent 工程的分水岭

单轮 agent 很容易做。

真正难的是：

- 方法能否沉淀
- 能力能否安装
- runtime 能否被事件驱动
- 系统能否在后台和定时流程里持续运转

这些都属于扩展面，而不是最内层 prompt。

## 五类扩展对象

### Skills

沉淀工作方法、模板、脚本与领域知识。

### Plugins

把 skills、hooks、scripts、apps 收成一个可发现、可安装的壳层。

### Hooks

在 runtime 关键事件点插入观察、校验、记忆写入或审计逻辑。

### Apps

提供更成熟的业务接入对象模型。

### Automation

把一次性动作变成 recurring workflow。

## 一个更实用的判断

不是所有经验都值得变 plugin。

通常更稳的演进是：

1. 先写成 prompt pattern
2. 再沉淀成 skill
3. 必要时再包装成 plugin
4. 确认 runtime 事件稳定后再接 hooks
5. 最后才做 automation 和 rollout


## plugin 壳层里最容易被忽略的一层

对 `plugin` 来说，`listed`、`installed`、`loaded`、`fired` 是四个不同阶段。

很多误判都发生在这里：

- 看到 plugin 出现在 marketplace，就以为 hook 一定生效
- 看到 skill 被发现，就以为 runtime 一定已经挂上事件

这也是我们后面把 `plugin installation reality` 单独拆成一页的原因。

## 这条线为什么和自改进系统强相关

`self-improving-learning-ledger`、`Self-Improving-Agent`、`OpenClaw` 分层记忆这些例子，都说明：

- 记忆写入不只是 memory 设计
- 还必须依赖扩展面来捕获信号、做 promotion gate、做 regression

## 推荐继续读

- [[技能、插件、应用与自动化：Harness 的扩展面]]
- [[Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
- [[Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot]]
- [[Plugin 安装、发现与 Runtime Reality]]
- [[Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[../../AI-Learning/06-Topics/Agent 扩展面：Skills、Plugins、Hooks 与 Automations|Agent 扩展面：Skills、Plugins、Hooks 与 Automations]]
