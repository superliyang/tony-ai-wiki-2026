---
title: Plugin、Memory 与 Background Task 失效模式
type: topic
status: learning
tags:
  - ai/engineering
  - ai/plugins
  - ai/memory
  - ai/background
created: 2026-03-28
updated: 2026-03-28
---

# Plugin、Memory 与 Background Task 失效模式

## 为什么这三层经常一起出问题

因为它们都不是“主推理回路”的显性部分，却会决定系统是否稳定：

- plugin 决定 capability 能否被正确加载和消费
- memory 决定长期行为是否被污染
- background task 决定任务能否脱离前台继续推进

它们单看都像配角，合在一起却经常决定 runtime 是否可用。

## Plugin failure：不是“加载失败”这么简单

### `OpenClaw` 给出的一个很清楚的工程提醒

官方文档明确写了：

- native plugins 与 Gateway 同进程运行
- plugin bug 可以 crash 或 destabilize gateway
- malicious plugin 等价于在进程内执行任意代码
- workspace plugin 可以 shadow bundled plugin
- `plugins.allow` 信任的是 plugin id，不是来源本身

这意味着 plugin failure 至少分成 4 类：

### 1. load failure

- manifest 合法但 runtime register 失败
- config 合法，但 capability 冲突
- 依赖装上了，行为还是起不来

### 2. ownership failure

- 重复 provider id
- 重复 capability ownership
- shadowing 后实际跑的是另一份代码

### 3. stability failure

- 插件没有直接报错，但让 gateway 变慢、变脆、内存上涨
- hook 太重导致生命周期事件堆积

### 4. trust-boundary failure

- 开发时把 workspace plugin 当成生产默认
- allowlist 太粗
- plugin source provenance 不清

## Memory failure：最危险的是“看起来没坏”

### `Claude Code` 这一线的提醒

官方 memory docs 很清楚：

- `CLAUDE.md` 和 auto memory 是两套系统
- auto memory 按 project / worktree 维度落盘
- `MEMORY.md` 只有前 200 行或 25KB 在 session start 时保证加载
- topic files 是按需读取，不是启动即注入

这说明 memory 失败不只是“没记住”，更包括：

### 1. scope failure

- 本该 repo-shared 的规则只写进 auto memory
- 本该临时的偏好却进入长期 memory

### 2. load failure

- 关键记忆写进了 topic file，但启动时并不会自动出现
- 以为模型知道，实际上当前 turn 根本没召回

### 3. pollution failure

- 错误结论被写进 durable memory
- 临时 workaround 被误当成长期规则

### 4. compaction failure

- 长任务压缩前没有把重要内容转成 memory / artifact
- 压缩后上下文“表面还在”，但关键结构已经丢了

### `OpenClaw` 这一线的提醒

官方文档明确写了：

- memory 的 source of truth 是 workspace 里的 Markdown 文件
- `memory_get` 对不存在的文件会优雅降级
- pre-compaction memory flush 在只读 workspace 下会被跳过

这说明 OpenClaw 这类 runtime 的 memory 失败更多来自：

- workspace 不可写
- flush 被跳过
- daily log 和 `MEMORY.md` 角色混淆
- memory plugin 切换后 recall 行为变化

## Background task failure：最痛的不是失败，而是“卡着不交代”

### `OpenAI shell/background` 路线给的提醒

官方 docs 强调：

- shell 一定要 sandbox
- network access 默认关闭，需要 allowlist
- commands 非交互式
- 需要 timeout、audit、stdout/stderr 捕获

这意味着 background task 的典型失败是：

### 1. environment failure

- 本地能跑，容器里跑不了
- 网络默认关，任务 silently 退化
- CLI 需要交互，结果永远卡住

### 2. visibility failure

- 任务还在执行，但用户不知道做到哪一步
- 只看到“in progress”，没有关键事件和中间产物

### 3. control failure

- 没有 cancel
- 没有 budget
- 没有 step / time limits
- 失败后不能接着跑

### 4. handoff failure

- 背景任务做完了，但没能回到：
  - review
  - artifact store
  - chat summary
  - PR / channel notify

## 三层连锁失败通常长什么样

### 路径 1：plugin -> memory

插件版本切换后，召回逻辑或 memory adapter 行为变化，结果 durable memory 还在，但 recall 结果已经变了。

### 路径 2：memory -> background

后台任务依赖长期上下文，但 compaction 前没有 flush，任务恢复时上下文断裂。

### 路径 3：plugin -> background -> blast radius

一个 hook/plugin 被放进 gateway 主流程后，在 background / cron 里放大副作用，最终不是单个任务坏，而是一类自动化都变脆。

## 怎样把这类失败挡在前面

### plugin 层

- capability ownership 明确
- shadowing 可见
- plugin allow/deny 最小化
- 对 plugin source 做更清楚的 provenance 控制
- 把 heavy hooks 从主流程剥离

### memory 层

- durable memory write policy 更保守
- session / memory / artifact 明确分层
- compaction 前有显式 flush 规则
- audit memory writes

### background 层

- detached task 必须可取消
- progress 必须外显
- artifacts 必须回流
- 环境、网络、权限都必须显式声明

## 学这一页最该形成的判断力

### 判断 1：现在的问题到底是 plugin failure、memory failure，还是 background control failure

三者常常会被混在一起，但修法完全不同。

### 判断 2：哪些层应该 fail closed，哪些可以 degrade gracefully

- destructive tool approval：应 fail closed
- memory file 不存在：可以 graceful degrade
- plugin capability ownership 冲突：应 hard error

### 判断 3：哪类失败必须在 UI 上让用户看见

尤其是 background black-box failure，不可见往往比出错本身更伤信任。

## 推荐怎么连着读

1. [[Session and Memory Design]]
2. [[Background Agents]]
3. [[Agent Runtime 失败模式、事故复盘与 Postmortems]]
4. [[Runtime 发布门槛、灰度与 Blast Radius 控制]]
5. [[Long-Running Agent Operations]]

## 相关主题

- [[Session and Memory Design]]
- [[Background Agents]]
- [[Long-Running Agent Operations]]
- [[Task Success and Failure Recovery]]
- [[Agent Runtime 失败模式、事故复盘与 Postmortems]]
- [[Runtime 发布门槛、灰度与 Blast Radius 控制]]

## 资料

- [OpenClaw Plugin Internals](https://docs.openclaw.ai/plugins/architecture)
- [OpenClaw Hooks](https://docs.openclaw.ai/automation/hooks)
- [OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)
- [OpenClaw Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- [Claude Code memory docs](https://code.claude.com/docs/en/memory)
- [Claude Code hooks reference](https://code.claude.com/docs/en/hooks)
- [Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents)
- [OpenAI Shell tool docs](https://developers.openai.com/api/docs/guides/tools-shell)
