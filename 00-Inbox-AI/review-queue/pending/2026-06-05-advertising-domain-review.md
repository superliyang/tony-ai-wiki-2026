---
status: pending
owner: codex
created: 2026-06-05
source: hermes-candidates
updated: 2026-06-06
type: learning-task-review
learning_package: "00-Inbox-AI/learning-tasks/in-progress/2026-06-06-advertising-domain-crystallization-package.md"
---

# 广告投放领域知识结晶 — 待 Tony 审核

Hermes 搜索了 6 轮 (exa)，生成了 5 个 draft，Tony 已确认方向。待 Codex 结晶入库后，请 review：

## Codex Gate Update — 2026-06-06

Codex 已按 Hermes -> Codex learning gate 生成 staging package：

[[00-Inbox-AI/learning-tasks/in-progress/2026-06-06-advertising-domain-crystallization-package|广告投放领域知识结晶：Hermes 草稿到正式知识库的入库审查包]]

本次 heartbeat 未做 canonical promotion、未 commit、未 push。原因：自动化指令明确禁止在未获 Tony 批准前写入正式知识区。

## 推荐决策

建议选择：`review -> verify -> promote`

```text
review: Tony 先确认领域结构和学习路径是否符合预期
verify: Codex 对关键 benchmark 和比例做 URL 级来源校验
promote: 校验后接受/修正当前 Advertising canonical tree
defer: 暂缓广告领域，优先处理 AI Agent P1 任务
discard: 不继续处理这批广告 draft
```

## 审核要点

- [ ] 领域全貌图：12 节覆盖面是否完整？有无缺失的关键维度？
- [ ] 专家问题解答：10 问的方向和深度是否符合预期？是否需要补充问题？
- [ ] 一页复习卡：核心数字和框架是否准确？
- [ ] 误区与权衡：是否有遗漏的重要误区或权衡？
- [ ] MOC 索引：结构和学习路径是否合理？

## 链接

- 任务文件: [[00-Inbox-AI/learning-tasks/pending/2026-06-05-advertising-domain-crystallization]]
- Codex package: [[00-Inbox-AI/learning-tasks/in-progress/2026-06-06-advertising-domain-crystallization-package]]
- Draft 文件: `00-Inbox-AI/hermes/广告投放领域全貌图.md` 等 5 个

## Blockers

- 5 个 draft 都仍需 URL 级来源校验，尤其是 benchmark、比例和行业统计。
- 当前仓库已存在 `10-Knowledge/Advertising/` canonical tree，但本次 gate 没有修改或接受它；需要 Tony review 后再决定是否正式确认。
- `30-Playbooks/Advertising/` 当前不存在；Advertising playbook 目前更像是 domain-local `10-Knowledge/Advertising/10-Playbooks/`。后续需要统一 playbook 存放策略。
