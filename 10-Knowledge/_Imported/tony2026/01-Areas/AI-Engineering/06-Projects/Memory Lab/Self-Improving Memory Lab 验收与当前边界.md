---
title: Self-Improving Memory Lab 验收与当前边界
type: project
status: learning
project: Memory Lab
created: 2026-04-03
updated: 2026-04-03
---

# Self-Improving Memory Lab 验收与当前边界

## 这页要回答什么

这页不讲概念，而是明确回答：

- 我们的 `self-improving-memory-lab` 到底已经验证了什么
- 哪些能力只是脚本层通过
- 哪些能力已经接近真实工作流
- 哪些能力还不能假装已经生效

## 当前插件位置

- source：`/Users/tony/plugins/self-improving-memory-lab`
- cache：`/Users/tony/.codex/plugins/cache/tony-local/self-improving-memory-lab/local`
- installed：`/Users/tony/.agents/plugins/plugins/self-improving-memory-lab`
- marketplace：`/Users/tony/.agents/plugins/marketplace.json`

## 我们真正已经验证过的

### 1. 结构与安装态

- source / cache / installed 三处已经能对齐
- plugin manifest 能被解析
- plugin doctor 可以报告 drift、cache 状态和 probe 状态

### 2. hook-shaped event capture

- `UserPromptSubmit` 风格事件可以写入：
  - `/Users/tony/plugins/self-improving-memory-lab/.learnings/LEARNINGS.md`
- `PostToolUse` 风格事件可以写入：
  - `/Users/tony/plugins/self-improving-memory-lab/.learnings/ERRORS.md`

### 3. bounded self-improvement pipeline

当前这条链已经跑通：

`hook-shaped input -> ledger -> shadow review -> consolidation -> manual verify -> candidate skill -> incident replay`

### 4. 影子评审与聚类

- repeated preferences 会被 consolidation 聚成 cluster
- cluster 经人工确认后，可以从 `watch_cluster` 升到 `candidate_shadow_rollout`
- high-risk poisoning / flaky tool failure 不会直接晋升 durable rule

### 5. candidate skill generation

- verified cluster 现在能产出 review-only candidate skill
- 生成结果带 `Source Cluster`、`Eval Gate`、`Boundaries`
- 也就是说，这已经不是“空 stub”，而是一个可 review 的候选技能

### 6. incident replay regression

- incident pack replay 已经可用
- naming preference / poisoning / flaky retry 这类场景能被稳定回放
- 这让插件不只是“会跑一次”，而是开始有 regression gate 的味道

## 还没有最终证实的

### 1. 真实 live Codex hook firing

我们还没有抓到真实 live session 吐出的 debug snapshot：

- `/Users/tony/plugins/self-improving-memory-lab/.learnings/debug`

这意味着：

- `listed / installed / loaded` 基本已接近清楚
- 但 `fired` 这层还没被最终证实

### 2. 无感跨线程自动记忆

当前不能假装说：

- 只要新开线程，插件就会自动带着所有上下文继续工作

现在更靠谱的事实是：

- 知识库记忆已经可用于跨线程恢复
- 插件自学习能力已经可用于实验、记录、影子评审和候选 skill 生成
- 但跨线程自动继承仍处于验收期

## 当前最靠谱的使用姿势

1. 用知识库页做主记忆
- `学习进度.md`
- `恢复笔记.md`
- `当前工作台.md`

2. 用插件做旁路自学习
- 捕获 repeated preference
- 捕获 poisoning / failure
- 做 shadow review
- 做 consolidation
- 做 candidate skill

3. 不要让插件直接写 durable global rules
- 先 local
- 先 project-scoped
- 先 review
- 先 replay

## 当前推荐的验收命令

### 结构与安装态

```bash
python3 /Users/tony/plugins/self-improving-memory-lab/scripts/plugin_doctor.py
```

### 端到端实验

```bash
/Users/tony/plugins/self-improving-memory-lab/scripts/test_end_to_end.sh
```

### incident pack 回归

```bash
/Users/tony/plugins/self-improving-memory-lab/scripts/test_incident_pack.sh
```

### 更贴近真实研究工作的验收

```bash
/Users/tony/plugins/self-improving-memory-lab/scripts/test_real_workflow_acceptance.sh
```

### live hook probe

```bash
/Users/tony/plugins/self-improving-memory-lab/scripts/prepare_real_hook_probe.sh
# 然后在新会话里真实触发一次插件相关工作流
/Users/tony/plugins/self-improving-memory-lab/scripts/inspect_real_hook_probe.sh
```

## 最新一次 realistic workflow 验收（2026-04-03）

我们用：

```bash
/Users/tony/plugins/self-improving-memory-lab/scripts/test_real_workflow_acceptance.sh
```

实际验证了一轮更像真实工作的流程，结果是：

- 2 条重复偏好被捕获到 `LEARNINGS.md`
- 1 条泛化工作流提醒被保守跳过，没有乱写入 durable preference
- 1 条 `MCP` poisoning 事件被正确写入 `ERRORS.md`
- 1 条 `browser` flaky / failure 事件被正确写入 `ERRORS.md`
- consolidation 后，重复偏好 cluster 达到 `candidate_shadow_rollout`
- 生成了 1 个 candidate skill：
  - `/var/folders/wj/9cqvxh390n5687tnjn35m3h00000gn/T/self-improving-memory-lab-real-workflow/candidates/scoped-user-preference-guard/SKILL.md`
- hook bridge 在这轮验收里实际写出了 2 个 debug snapshots：
  - `last-user-prompt-submit.json`
  - `last-post-tool-use.json`

这轮结果说明两件事：

1. 插件在 `hook-shaped workflow` 下已经具备真实自学习能力
2. 它目前是保守型系统，不会把所有输入都误当成 durable memory

## 一句话结论

现在这套东西已经是一个可用的 `bounded self-improvement lab`，但还不是可以无脑信任的“自动进化系统”。

最可靠的结论是：

- 知识库级记忆：已经生效
- 插件级自学习：实验链已经生效
- live hook 自动触发：仍需继续验收
