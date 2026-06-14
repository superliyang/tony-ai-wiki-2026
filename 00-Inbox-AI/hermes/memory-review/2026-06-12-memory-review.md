---
title: "Memory Review — 2026-06-12"
created: 2026-06-12
source: memory-review-scout
status: review
---

# 记忆审查报告 — 2026-06-12

## 审查范围

- Canonical memory: `profile.md`, `preferences.md`, `learning-themes.md`, `negative-signals.md`, `user-profile-and-ai-cognitive-system.md`
- Projection: `hermes-soul.md`
- Candidates: 5 pending (2026-06-05 → 2026-06-09)
- Recent sessions: 06/07 (LLM推理), 06/10-06/12 (scout digests, memory reviews, learning tasks)
- Memory sync state: last actual change 2026-06-03

## 审查结果

### ⚠️ 严重：Canonical memory 停滞 9 天

所有 5 个 canonical memory 文件最后修改日期为 2026-06-03。memory-sync-state.json 的 hashes 自 06-03 以来未变。同时：
- 5 个 memory candidates 全部 `pending-review`（最早 06/05，已 7 天）
- Tony 在 06/07 做了 LLM推理优化 深度领域学习（~24KB 产出）
- 06/11-06/12 连续两次 memory review 都标记 "决策停滞 — 7 天未做任何判断"

### 发现问题

#### F1 (新): hermes-soul.md "Active Threads" 过时且产生误导

**位置**: `projections/hermes-soul.md` L88-89
**当前内容**:
```
## Active Threads
- Vault is clean and ready — staging directories are empty, no legacy tasks carried over
- Focus: build from current state, not replay old review-queue
```

**问题**: 这已完全不准确。当前状态：
- learning-tasks/pending/ 中 32+ 个 pending 任务
- learning-tasks/in-progress/ 中 5 个 in-progress 任务
- agent-memory/candidates/ 中 5 个 pending-review 候选
- 总 backlog ≈ 42 项未处理

"Vault is clean and ready" 会误导 agent 做出错误的饱和度判断——agent 读到此句可能认为可以继续创建更多候选，而实际上 backlog 已经严重偏高。

**严重性**: 中。该 projection 被用作 agent 初始化上下文，错误的状态信息可能导致错误的行为决策。

#### F2 (新): Canonical memory 不记录实际运行的 Scout cron job 名

**位置**: `user-profile-and-ai-cognitive-system.md` L187-189
**当前内容**:
```
- `curated-ai-scout`: external world -> ...
- `memory-review-scout`: internal memory review -> ...
```

**问题**: 当前实际运行的系统中有 3 个 scout cron job：
- `hourly-ai-scout` — 每小时运行，exa + Camofox 搜索
- `daily-ai-learning-scout` — 每天 08:30，RSS + Exa 策展
- memory-review-scout — 本 job 本身

`daily-ai-learning-scout` 是实际产出大部分 digest 的 job（每天 3 轮：09/15/21），但在 canonical memory 中完全没有记录。`curated-ai-scout` 这个名字在 canonical 中指向"外部信号发现"，但实际运行中的对应 job 是 `daily-ai-learning-scout`。

**严重性**: 中。新 agent 阅读 canonical memory 后会寻找 `curated-ai-scout` cron job，但该名不存在。已有 candidate C2 (2026-06-05) 提出类似问题但未解决。

#### F3 (新): 决策停滞模式应记录为 durable signal

**位置**: 未记录

**问题**: 从 06/05 起 Tony 未对任何 memory candidate、学习任务、或 review-queue 做出判断（深入/watch/discard/promote/build）。06/11 和 06/12 的 memory review 都标记了同一问题。如果这是一个 recurring pattern（例如 Tony 倾向于批量处理而非逐项判断），则应该作为 durable preference 记录，以便：
1. 系统调整推送节奏（批量 > 逐项）
2. 系统在合适的时间点（如周末）推送汇总而非每日催促
3. Agent 不反复发送"决策停滞"警告消耗通知额度

**严重性**: 低-中。当前不构成错误，但持续不记录此 pattern 会导致系统反复做无效通知。

### 已有候选状态

| 候选 | 日期 | 操作 | 状态 | 天数 |
|---|---|---|---|---|
| C1: 添加广告投放到学习主题 | 06/05 | add | pending-review | 7d |
| C2: 对齐 Scout cron job 命名 | 06/05 | replace | pending-review | 7d |
| C3: 重新生成 hermes-soul.md | 06/05 | replace | pending-review | 7d |
| C4: 职业画像回流 canonical | 06/08 | add | pending-review | 4d |
| C5: 添加LLM推理到学习主题 | 06/09 | add | pending-review | 3d |

**注意**: 本次审查不重复提交这些已有候选。F2 与 C2 部分重叠但角度不同（C2 提议全面重命名，F2 只提议在 canonical 中记录实际运行名）。

### 一致性检查

| 检查项 | 结果 |
|---|---|
| Canonical 文件之间一致性 | ✅ 一致（无内部矛盾） |
| Canonical ↔ Projection 一致性 | ⚠️ hermes-soul.md Active Threads + Scout State 过期 |
| Canonical ↔ 运行时实际状态 | ⚠️ Scout 命名不匹配，LLM API key 警告已过时 |
| Canonical ↔ 近期会话行为 | ⚠️ 广告投放/LLM推理两个深度学习未反映 |
| Candidate 重复/冲突 | ✅ 无重复，5 个候选互不冲突 |
| 负信号是否有新需求 | ⚠️ 决策停滞模式未记录 |

## 建议操作

1. **优先处理 C3 + C4 + C1/C5**: 这 4 个候选直接影响 agent 行为正确性和个性化质量
2. **新增 F1-F3**: 本次 3 个新发现写入 candidates/
3. **建立批量审查节奏**: 如果 Tony 偏好周末批量处理，系统应调整推送策略

## 审查结论

**发现 3 个新问题，已写入 3 个候选。** 9 天未更新 canonical memory 是核心瓶颈——5 个 pending 候选等待决策，2 个活跃学习领域未记录，projection 包含过时信息。建议 Tony 尽快完成一轮批量审查。

---

*Hermes memory-review-scout | 2026-06-12 | 扫描范围: 5 canonical + 1 projection + 5 candidates + 8 recent sessions*
