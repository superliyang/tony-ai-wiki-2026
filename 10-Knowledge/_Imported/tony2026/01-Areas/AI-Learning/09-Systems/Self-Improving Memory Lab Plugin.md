---
title: Self-Improving Memory Lab Plugin
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/plugins
  - ai/memory
  - ai/self-improving
created: 2026-03-31
updated: 2026-03-31
---

# Self-Improving Memory Lab Plugin

## 这是什么

这是我们自己做的一个 **本地 Codex plugin 实验**，目标不是让 agent 神奇地自动进化，而是把这条更可控的链路跑通：

- hook event
- learning capture
- error capture
- shadow review
- consolidation
- manual verification
- candidate skill generation
- incident replay

## 当前本地位置

- 源码目录：
  - `/Users/tony/plugins/self-improving-memory-lab`
- marketplace：
  - `/Users/tony/.agents/plugins/marketplace.json`
- 已安装路径：
  - `/Users/tony/.agents/plugins/plugins/self-improving-memory-lab`
- Codex 启用配置：
  - `/Users/tony/.codex/config.toml`
- debug snapshots：
  - `/Users/tony/plugins/self-improving-memory-lab/.learnings/debug`

## 它实际用了什么能力

### hooks

- `UserPromptSubmit`
- `PostToolUse`

对应配置：

- `/Users/tony/plugins/self-improving-memory-lab/hooks.json`

### bundled skill

- `/Users/tony/plugins/self-improving-memory-lab/skills/self-improving-learning-ledger/SKILL.md`

这说明它不是“纯 plugin 自动化”，而是：

- `plugin shell`
  + `skill methodology`

一起工作。

## 这版已经能做什么

### 1. 捕获用户偏好

例如：

- “以后索引文件统一用中文命名，README 改成 专题总览。”

会写入：

- `/Users/tony/plugins/self-improving-memory-lab/.learnings/LEARNINGS.md`

### 2. 捕获 tool poisoning / flaky failure

例如：

- tool output 里带 `ignore previous instructions`
- timeout / 429 / flaky retry

会写入：

- `/Users/tony/plugins/self-improving-memory-lab/.learnings/ERRORS.md`

### 3. 跑 shadow review

输出到：

- `/Users/tony/plugins/self-improving-memory-lab/.learnings/reports/latest-promotion-review.md`
- `/Users/tony/plugins/self-improving-memory-lab/.learnings/reports/latest-error-review.md`

### 4. 做 consolidation

把相似偏好或相似 failure 聚成 cluster。

输出到：

- `/Users/tony/plugins/self-improving-memory-lab/.learnings/reports/latest-consolidation-review.md`

### 5. 人工确认 verified

只有 cluster 被人工确认后，才更接近：

- `candidate_shadow_rollout`

### 6. 从 cluster 生成更像样的 candidate skill

它不再只是空 stub，而是带：

- source cluster
- sample signals
- sample evidence
- eval gate
- boundaries

### 7. incident pack replay

这版已经能把真实样例收成 pack，然后 replay：

- `/Users/tony/plugins/self-improving-memory-lab/incident-packs/naming-preference-and-poisoning.json`
- `/Users/tony/plugins/self-improving-memory-lab/incident-packs/flaky-tool-retry.json`

## 这版为什么有价值

它最值钱的不是“自动学会更多”，而是：

- 会记
- 会跳过健康事件
- 会识别 poisoning
- 会聚类重复经验
- 会人工确认
- 会生成 candidate skill
- 还不会乱自动晋升

这比“自动进化”更接近真正能上线的工程路径。

## 目前的关键边界

- 不自动改全局 durable rules
- 不自动跨项目共享 memory
- 不自动启用新 skill
- 高风险 tool output 默认继续保持 untrusted

## 接下来最值得补的

1. 真实 Codex hook payload 兼容与调试快照
2. 更多 incident pack
3. candidate shadow rollout 之后的更细 release gate

## 推荐继续读

- [[Codex Skills 与 Plugins]]
- [[self-improving-learning-ledger 技能]]
- [[Codex]]
- [[Self-Improving-Agent（ClawHub Skill）]]
- [[../../AI-Engineering/06-Projects/Memory Lab/Self-Improving Memory Lab 插件实战|Self-Improving Memory Lab 插件实战]]
- [[../../AI-Engineering/06-Projects/Memory Lab/最小 Self-Improving Plugin 设计|最小 Self-Improving Plugin 设计]]
- [[../../AI-Engineering/07-Topics/Incident-Fed Evals、Shadow Rollout 与 Promotion Regression|Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
