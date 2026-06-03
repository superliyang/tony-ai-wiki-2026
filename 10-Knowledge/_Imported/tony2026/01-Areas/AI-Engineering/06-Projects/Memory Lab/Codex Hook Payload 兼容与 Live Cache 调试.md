---
title: Codex Hook Payload 兼容与 Live Cache 调试
type: project
status: learning
project: Memory Lab
created: 2026-03-31
updated: 2026-04-03
---

# Codex Hook Payload 兼容与 Live Cache 调试

## 这页记录什么

这页不讨论抽象 memory theory，而是专门记录本地 `Self-Improving Memory Lab` 插件怎么往真实 `Codex` runtime 适配推进。

## 这次实际确认的路径

- source plugin：`/Users/tony/plugins/self-improving-memory-lab`
- live cache：`/Users/tony/.codex/plugins/cache/tony-local/self-improving-memory-lab/local`
- installed path：`/Users/tony/.agents/plugins/plugins/self-improving-memory-lab`

## 这次最重要的工程认识

### 1. cache drift 是真问题

`Codex` 当前会话可能执行 cache 里的本地插件副本，而不是 source tree。

所以如果只改：

- `/Users/tony/plugins/self-improving-memory-lab/scripts/hook_capture.py`

但不把更新同步到 live cache，当前会话可能继续跑旧逻辑。

### 2. symlink 会误导同步逻辑

installed path 这次实际上是指回 source 的软链，所以同步脚本必须跳过“目标其实就是源码自己”的情况。

### 3. install state 也需要单独验

我们后来从日志里确认到：

- `failed to load plugin: plugin is not installed`

所以验收时不能只看 cache 和 manifest，还要分清：

- listed
- installed
- loaded
- fired

为此，本地 marketplace 已把 lab plugin 调整成 `INSTALLED_BY_DEFAULT`，让后续新会话更容易直接验证 hook。

### 4. real-hook probe 需要两步

不是只写 debug 代码就完事，而是：

1. `prepare`
2. 真会话触发
3. `inspect`

## 当前可用的本地脚本

- sync：
  - `/Users/tony/plugins/self-improving-memory-lab/scripts/sync_live_plugin.py`
- doctor：
  - `/Users/tony/plugins/self-improving-memory-lab/scripts/plugin_doctor.py`
- prepare probe：
  - `/Users/tony/plugins/self-improving-memory-lab/scripts/prepare_real_hook_probe.sh`
- inspect probe：
  - `/Users/tony/plugins/self-improving-memory-lab/scripts/inspect_real_hook_probe.sh`

## 当前最稳的调试流程

1. 先跑：
   - `python3 /Users/tony/plugins/self-improving-memory-lab/scripts/sync_live_plugin.py`
2. 再跑：
   - `/Users/tony/plugins/self-improving-memory-lab/scripts/prepare_real_hook_probe.sh`
3. 然后在 Codex 里走一次真实 prompt / tool path
4. 最后跑：
   - `/Users/tony/plugins/self-improving-memory-lab/scripts/inspect_real_hook_probe.sh`

## 目前观察到的边界

- 本地 e2e 与 incident pack 回归都已通过
- source / cache / installed path 现在能对齐
- 但当前会话下，普通 assistant tool 调用未必等同于 plugin hook 已被原生触发

这说明后面还需要继续区分：

- lab replay
- live runtime event

## 推荐继续读

- [[Self-Improving Memory Lab 插件实战]]
- [[最小 Self-Improving Plugin 设计]]
- [[../../07-Topics/Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot|Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot]]
- [[../../07-Topics/Incident-Fed Evals、Shadow Rollout 与 Promotion Regression|Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
- [[../../../AI-Learning/09-Systems/Self-Improving Memory Lab Plugin|Self-Improving Memory Lab Plugin]]
