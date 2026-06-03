---
title: Self-Improving Systems 学习图
type: map
status: learning
tags:
  - ai/map
  - ai/memory
  - ai/self-improving
created: 2026-03-31
updated: 2026-03-31
---

# Self-Improving Systems 学习图

## 学习主线

1. `AI 记忆设计`
2. `Agent Memory`
3. `大模型记忆、项目记忆与 Chat Memory`
4. `自我进化与持续学习的记忆设计`
5. `从 Learnings 到 AutoSkill：技能自提炼`
6. `记忆污染、Memory Poisoning 与自改进风险`
7. `Self-Improving Systems`
8. `Learnings、Promotion 与 Skill Extraction Pipeline`
9. `自改进记忆的 Incident Library、Poisoning 与 Failure Cases`
10. `自改进 Skill 的 Eval Gate、Release Gate 与 Rollback`
11. `Incident-Fed Evals、Shadow Rollout 与 Promotion Regression`
12. `Codex Plugin Hook Payload、Live Cache 与 Debug Snapshot`
13. `Memory Lab`
14. `Self-Improving Memory Lab 插件实战`
15. `Codex Hook Payload 兼容与 Live Cache 调试`

## 关键系统样本

- [[../09-Systems/OpenClaw 的分层记忆设计|OpenClaw 的分层记忆设计]]
- [[../09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
- [[../09-Systems/Self-Improving-Agent（ClawHub Skill）|Self-Improving-Agent（ClawHub Skill）]]
- [[../09-Systems/LangMem|LangMem]]
- [[../09-Systems/Codex Skills 与 Plugins|Codex Skills 与 Plugins]]
- [[../09-Systems/Self-Improving Memory Lab Plugin|Self-Improving Memory Lab Plugin]]
- [[../09-Systems/self-improving-learning-ledger 技能|self-improving-learning-ledger 技能]]

## 最应该关注的边界

- 先 capture，再 promote
- 高风险 incident 先 block，再 replay
- cluster 不等于 rollout
- manual verify 不是多余步骤
- live cache 和真实 runtime payload 是工程真问题
