---
title: Self-Improving Memory Lab 插件实战
type: project
status: learning
project: Memory Lab
created: 2026-03-31
updated: 2026-04-03
---

# Self-Improving Memory Lab 插件实战

## 这页要回答什么

不是抽象地讨论 self-improving plugin，而是记录我们已经在本机上真正做出来的那条薄实现：

- plugin 安装
- hook capture
- shadow review
- consolidation
- manual verify
- candidate skill generation
- incident pack replay

## 当前本地实现位置

- plugin source：
  - `/Users/tony/plugins/self-improving-memory-lab`
- installed path：
  - `/Users/tony/.agents/plugins/plugins/self-improving-memory-lab`
- local marketplace：
  - `/Users/tony/.agents/plugins/marketplace.json`
- enablement：
  - `/Users/tony/.codex/config.toml`

## 当前链路

### 1. hook capture

- `UserPromptSubmit`
- `PostToolUse`

桥接脚本：

- `/Users/tony/plugins/self-improving-memory-lab/scripts/hook_capture.py`

### 2. learning / error ledger

- `/Users/tony/plugins/self-improving-memory-lab/.learnings/LEARNINGS.md`
- `/Users/tony/plugins/self-improving-memory-lab/.learnings/ERRORS.md`

### 3. shadow review

- `/Users/tony/plugins/self-improving-memory-lab/scripts/run_shadow_review.sh`

### 4. consolidation review

- `/Users/tony/plugins/self-improving-memory-lab/scripts/run_consolidation_review.sh`

### 5. manual verification

- `/Users/tony/plugins/self-improving-memory-lab/scripts/confirm_cluster.sh`

### 6. cluster-based skill generation

- `/Users/tony/plugins/self-improving-memory-lab/scripts/generate_skill_from_cluster.sh`

### 7. incident replay

- `/Users/tony/plugins/self-improving-memory-lab/scripts/run_incident_pack.sh`
- `/Users/tony/plugins/self-improving-memory-lab/scripts/test_incident_pack.sh`

## 现在已经验证过的东西

### 正向偏好

相似表达的用户偏好现在已经能：

- 进入 `LEARNINGS`
- 被 consolidation 聚类
- 经人工确认后升级到 `candidate_shadow_rollout`

### 负向风险

poisoning / flaky failure 现在已经能：

- 进入 `ERRORS`
- 在 consolidation report 中保持更严格的 recommendation
- 不直接走 durable promotion

## 真实像什么，不像什么

### 像什么

- bounded self-improvement workflow
- memory governance lab
- promotion regression gate
- local plugin harness

### 不像什么

- fully autonomous self-evolving agent
- production-grade plugin marketplace app
- 无审查自动升级系统

## 这版最值钱的工程认识

1. `skill` 负责方法，不负责壳层
2. `plugin` 负责 hooks、scripts、orchestration
3. `incident pack` 比“手动记得怎么测”可靠得多
4. `manual verify` 是很重要的边界，不是多余步骤
5. `candidate skill` 必须带 `eval gate`，不然只是在扩大 blast radius

## 新增的验收入口

- `realistic workflow acceptance`：
  - `/Users/tony/plugins/self-improving-memory-lab/scripts/test_real_workflow_acceptance.sh`
- 这条脚本比单纯的 `test_end_to_end.sh` 更像真实研究工作流：
  - repeated preference
  - generic reminder skip
  - poisoning capture
  - browser flaky capture
  - consolidation
  - manual verify
  - candidate skill generation

## 当前最值得继续补的

1. 真实 Codex hook payload 适配与调试快照
2. 更多 replayable incident packs
3. candidate shadow rollout 之后的 release checklist

## 推荐配套阅读

- [[最小 Self-Improving Plugin 设计]]
- [[Incident-Fed Eval 与 Shadow Rollout 实验]]
- [[Memory Poisoning、Shared Memory Boundary 与 Release Gates 实验]]
- [[../../07-Topics/Incident-Fed Evals、Shadow Rollout 与 Promotion Regression|Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
- [[../../../AI-Learning/09-Systems/Self-Improving Memory Lab Plugin|Self-Improving Memory Lab Plugin]]
