---
title: Plugin 安装、发现与 Runtime Reality
type: topic
status: learning
tags:
  - ai/engineering
  - ai/plugins
  - ai/runtime
  - ai/harness
created: 2026-04-03
updated: 2026-04-03
---

# Plugin 安装、发现与 Runtime Reality

## 这页要回答什么

为什么一个 plugin：

- 出现在 marketplace
- 甚至能被 skill 发现

也不等于：

- 当前会话已经完成安装
- 当前 runtime 已经挂上 hooks
- 当前 tool path 一定会触发事件

## 四个容易混淆的阶段

### 1. Listed

plugin 出现在 marketplace，例如：

- `/Users/tony/.agents/plugins/marketplace.json`

这说明：

- 它可以被发现
- 但不说明当前会话已经在用它

### 2. Installed

plugin 已经被 Codex 当成“已安装对象”接受。

这一步和 `policy.installation`、当前会话刷新、用户安装动作或默认安装策略都有关。

### 3. Loaded

当前会话真正加载了 plugin manifest、skills、hooks、scripts。

这时通常可以观察到：

- cache path 有效
- manifest 被解析
- skill 被注入可用列表

### 4. Fired

最容易被误判的一步。

即使 plugin 已经 loaded，也不等于：

- `UserPromptSubmit` 一定触发
- `PostToolUse` 一定触发
- 当前具体 tool class 一定进入 plugin hook 生命周期

## 我们在 `self-improving-memory-lab` 上学到的事

### 已经确认的

- source / cache / installed 三处路径可以对齐
- manifest 里的非法占位路径会导致解析噪声
- plugin skill 可以被发现
- 真实 runtime 里确实存在“plugin is not installed”这种失败模式

### 还未完全证实的

- 当前 desktop / Codex live path 是否会稳定触发 `UserPromptSubmit`
- 当前 tool 使用路径是否会稳定触发 `PostToolUse`
- 会话刷新前后的 hook 挂载差异

## 一个很重要的工程判断

调 plugin 不能只看“它在目录里”。

更稳的验收顺序应该是：

1. marketplace entry 正确
2. install policy 明确
3. live cache 对齐
4. skill discovery 对齐
5. debug snapshot 目录可写
6. real hook probe 抓到 payload
7. 再谈自动化 rollout

## 对本地 lab 的实际启发

对本地实验插件，`INSTALLED_BY_DEFAULT` 往往比 `AVAILABLE` 更适合作为验真起点。

原因不是它更“正式”，而是它能少掉一层：

- 先证明安装没卡住
- 再专心看 hook 是否真的触发

## 推荐继续读

- [[Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot]]
- [[扩展面设计：Skills、Plugins、Hooks、Apps 与 Automation]]
- [[Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
- [[../06-Projects/Memory Lab/Codex Hook Payload 兼容与 Live Cache 调试|Codex Hook Payload 兼容与 Live Cache 调试]]
- [[../../AI-Learning/09-Systems/Codex Skills 与 Plugins|Codex Skills 与 Plugins]]
