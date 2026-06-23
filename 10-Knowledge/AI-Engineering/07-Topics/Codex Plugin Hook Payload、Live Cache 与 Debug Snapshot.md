---
title: Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot
type: topic
status: learning
tags:
  - ai/engineering
  - ai/plugins
  - ai/harness
  - ai/memory
created: 2026-03-31
updated: 2026-04-03
---

# Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot

## 这页要回答什么

当我们把一个本地 plugin 接进 `Codex` 时，真正难的往往不是：

- 会不会写 `hook_capture.py`

而是：

- 当前会话到底在用源码目录还是 cache 目录
- hook 事件真实 payload 长什么样
- debug snapshot 写到哪里
- installed path 和 source path 是否其实是同一个东西

## 这次本地实验里踩到的关键坑

### 1. live cache 可能不是源码目录

我们这次确认到，当前会话实际使用的本地 plugin cache 在：

- `/Users/tony/.codex/plugins/cache/tony-local/self-improving-memory-lab/local`

这意味着：

- 你改源码目录并不等于当前会话立刻使用了最新版本

### 2. installed path 可能是 symlink

这次本地安装路径：

- `/Users/tony/.agents/plugins/plugins/self-improving-memory-lab`

实际是指回源码目录的软链。

所以如果同步脚本把它当独立副本处理，就可能误删源码里的 `.codex-plugin`。

### 3. debug snapshot 是做 runtime 适配的第一手材料

我们给 hook bridge 加的不是“花哨日志”，而是为了回答：

- payload 是扁平 JSON 还是嵌套 JSON
- user prompt 是 `prompt`、`userPrompt`、`message` 还是更深层字段
- tool 结果是 `stderr`、`result`、`output` 还是别的 key
- 当前事件到底有没有真的触发


## 2026-04-03 当前验收结论

这一轮我们把本地 plugin manifest 里的无效占位清掉了：

- `mcpServers` 的 `[TODO: ./.mcp.json]`
- `apps` 的 `[TODO: ./.app.json]`

原因很简单：Codex 的 manifest 解析器会把这类占位当成非法路径，然后在日志里报：

- `ignoring mcpServers: path must start with ./ relative to plugin root`
- `ignoring apps: path must start with ./ relative to plugin root`

清掉之后，`source / cache / installed` 三处 manifest 已经对齐，也不再带这个无效配置噪声。

但当前最诚实的结论仍然是：

我们后来还从日志里确认到另一层更具体的问题：

- `codex_core::plugins::manager` 曾明确报过 `failed to load plugin: plugin is not installed`

这说明：

- plugin 已出现在 marketplace
- 不等于当前会话已经完成 install

所以我们又把本地 marketplace policy 从 `AVAILABLE` 调整成了 `INSTALLED_BY_DEFAULT`，目的是让后续新会话先越过“安装态不明确”这一层，再专心验证 hook 触发。

- `plugin path / live cache / installed symlink` 已经验证通了
- `hook bridge` 已经验证可运行
- `debug snapshot` 写入路径已经准备好
- 但是当前会话里仍然**没有抓到真实 live hook snapshot**

也就是说，现在已经能确定：

- 插件被 Codex 解析过
- skill 能被发现
- 但 `UserPromptSubmit` / `PostToolUse` 在这条 live path 里是否稳定原生触发，仍然需要继续验真

这一步非常重要，因为它把问题缩小成了：

- runtime 事件触发条件
- hook 生命周期
- 当前会话是否需要刷新才能重新挂载 hooks

而不再是插件文件结构本身。

## 当前本地路径

- source plugin：
  - `/Users/tony/plugins/self-improving-memory-lab`
- live cache：
  - `/Users/tony/.codex/plugins/cache/tony-local/self-improving-memory-lab/local`
- installed path：
  - `/Users/tony/.agents/plugins/plugins/self-improving-memory-lab`

## 我们现在补上的工程动作

### sync

- `/Users/tony/plugins/self-improving-memory-lab/scripts/sync_live_plugin.py`

作用：

- 把 source plugin 同步到 live cache
- 避免“源码改了，当前会话还在跑旧缓存”
- 自动识别 installed path 指回 source 的情况并跳过危险同步

### doctor

- `/Users/tony/plugins/self-improving-memory-lab/scripts/plugin_doctor.py`

作用：

- 检查 source / cache / installed 三处是否都完整
- 检查 `hook_capture.py` 的关键 marker 是否存在
- 检查 debug snapshot 是否已经出现

### real-hook probe

- `/Users/tony/plugins/self-improving-memory-lab/scripts/prepare_real_hook_probe.sh`
- `/Users/tony/plugins/self-improving-memory-lab/scripts/inspect_real_hook_probe.sh`

作用：

- 先清空 debug 目录并同步 live cache
- 再在下一次真实用户提示或真实工具路径之后检查 snapshot

## 当前最真实的一个结论

到这一步，我们已经证明：

- 插件源码、cache、installed path 可以被对齐
- debug snapshot 能为真实 payload 适配做准备

但还没有完全证明：

- 当前会话里的每次工具调用都会稳定触发 plugin hook

这不是失败，而是说明：

- “会话里可见插件”
  不自动等于
- “当前所有 tool path 都会触发 hooks”

## 为什么这对 Self-Improving Systems 很重要

如果不知道真实 runtime payload，就很容易出现：

- 以为在学，其实没接上 runtime
- 以为写进 memory 了，其实写的是测试路径
- 以为能自动 rollout，结果只是脚本局部跑通

所以 `hook payload + live cache + debug snapshot` 是 self-improving plugin 从 lab 走向可用 runtime 的必修课。

## 推荐继续读

- [[Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
- [[Plugin、Memory 与 Background Task 失效模式]]
- [[../06-Projects/Memory Lab/Codex Hook Payload 兼容与 Live Cache 调试|Codex Hook Payload 兼容与 Live Cache 调试]]
- [[../06-Projects/Memory Lab/Self-Improving Memory Lab 插件实战|Self-Improving Memory Lab 插件实战]]
- [[../../AI-Learning/09-Systems/Codex Skills 与 Plugins|Codex Skills 与 Plugins]]
- [[../../AI-Learning/09-Systems/Self-Improving Memory Lab Plugin|Self-Improving Memory Lab Plugin]]
