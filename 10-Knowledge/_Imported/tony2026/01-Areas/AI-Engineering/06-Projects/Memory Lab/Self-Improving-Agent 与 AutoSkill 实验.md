---
title: Self-Improving-Agent 与 AutoSkill 实验
type: project
status: learning
project: Memory Lab
created: 2026-03-29
updated: 2026-03-29
---

# Self-Improving-Agent 与 AutoSkill 实验

## 这个实验想验证什么

不是验证“agent 会不会神奇地自己变强”，而是验证一条更具体的工程链路：

- 能不能稳定记录 learnings
- 能不能把高价值经验 promotion 到 durable rules
- 能不能只把少数真正稳定的模式抽成 skill
- 能不能给 skill extraction 加上 eval gate 和 rollback discipline

## 实验分成 4 段

### 实验 1：learning ledger

建立最小 `.learnings/`：

- `LEARNINGS.md`
- `ERRORS.md`
- `FEATURE_REQUESTS.md`

验证：

- 条目格式是否可检索
- recurrence / status / provenance 是否足够支撑后续判断

### 实验 2：promotion gate

挑选几条 learning，分别尝试 promotion 到：

- `MEMORY.md`
- `AGENTS.md`
- `TOOLS.md`

验证：

- 哪些信息属于 durable memory
- 哪些信息属于 workflow rules
- 哪些 promotion 会污染默认行为

### 实验 3：skill extraction

从已验证 learning 中选一条 recurring、non-obvious、broadly applicable 模式，手工写成最小 `SKILL.md`。

验证：

- skill 是否能在新 session 独立理解
- 是否真的比写进 `AGENTS.md` 更合适
- 是否有 project-specific leakage

### 实验 4：eval gate + rollback

给 skill extraction 加一层评测：

- fresh session readability
- task success delta
- hallucination / over-generalization check
- conflict with existing skills

如果失败，回退到：

- 仅保留 learning
- 或仅保留 promotion rule

## 后续怎么连接到我们自己的 skill / plugin

这页实验的价值，不只是研究别人怎么做。

它也可以直接变成我们后面自己实现能力时的蓝图：

- 先做 `.learnings` learning ledger
- 再做 promotion policy
- 再做最小 skill extraction helper
- 最后给 skill extraction 加 eval gate 与 rollback

如果后面我们真的要自己做 `skill` 或 `plugin`，这页就可以直接变成需求清单。

## 推荐观察指标

- 重复错误是否下降
- 同类任务首轮成功率是否上升
- 新 session 是否更快进入正确工作模式
- skill 数量是否失控
- 规则冲突是否增加

## 什么时候算成功

- 不是 skill 越多越成功
- 而是 agent 的默认行为更稳定，同时治理成本没有明显失控

## 推荐前置阅读

1. [[../../07-Topics/记忆架构：State、Memory、Artifact 与 Context|记忆架构：State、Memory、Artifact 与 Context]]
2. [[../../07-Topics/记忆写入、召回、压缩与 Consolidation|记忆写入、召回、压缩与 Consolidation]]
3. [[../../07-Topics/记忆评测、污染、遗忘与纠偏|记忆评测、污染、遗忘与纠偏]]
4. [[../../07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
5. [[../../../AI-Learning/09-Systems/Self-Improving-Agent（ClawHub Skill）|Self-Improving-Agent（ClawHub Skill）]]
