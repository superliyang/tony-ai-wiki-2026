# AI First Cognitive System 在线回顾版

> 这是一份从 Tony AI Wiki 发布到飞书的在线阅读版。Vault / GitHub 仍是 source of truth，飞书只作为临时回顾和移动端阅读 surface。

## 当前判断

Tony 的 AI First Cognitive System 已经跨过第一阶段：结构已经能运转，接下来重点不是继续增加 Agent 名称，而是让队列流动起来。

核心原则：

```text
workflow first, persona second
```

也就是说，`tony-gardener`、`tony-research-scout`、`tony-project-companion` 等名字是能力别名，不是第二套组织架构。

## 当前系统分工

| Layer | Role |
|---|---|
| Obsidian / Vault | 长期知识主库、可审查 Markdown |
| GitHub | 历史、回滚、checkpoint |
| Hermes | scout、recall、digest、候选生成、提醒 |
| Codex | 结晶、整理、promote、项目推进、Git 维护 |
| Feishu | 在线回顾版、临时阅读、分享 surface |

## 已经建好的能力

| Capability | Current Status |
|---|---|
| Hermes / Codex learning chain | 已建立 |
| Personal Agent capability map | 已建立 |
| Project Companion workflow | 已建立，支持按需运行 |
| Review gate triage | 已完成第一轮 substantive review |
| Feishu publishing workflow | 正在首发试运行 |

## Review Gate 第一轮决策

Tony 已同意默认建议：

| Topic | Decision | Next Action |
|---|---|---|
| Agent Memory | accept -> build | 建 Agent Memory schema 与晋升/遗忘流程 |
| Agent Model Architecture | accept -> build | 建 Hermes 模型路由矩阵和评测样例 |
| MCP Protocol Evolution | watch -> build-checklist | 建 MCP 接入审查清单 |
| Recursive Self-Improvement | watch -> governance-gate | 建 Agent 自我改进审查清单 |
| Advertising Domain | accept-with-verification | 先做来源校验，再考虑正式入库 |

## 当前瓶颈

系统已经能产生材料，当前瓶颈从“有没有结构”变成了：

```text
accepted package -> build / promote / verification
```

也就是：review gate 已经打开，下一步要执行 accepted build queue。

## 下一步执行顺序

1. Agent Memory Gate
2. Hermes Model Routing
3. MCP Access Checklist
4. Agent Self-Improvement Gate
5. Advertising Source Verification

## 发布说明

- Source vault: `/Users/tony/Vault/tony-ai-wiki-2026`
- Source project: `40-Projects/AI-First-Cognitive-System/README.md`
- Source decision: `00-Inbox-AI/review-queue/accepted/2026-06-14-review-gate-batch-decision.md`
- Sync mode: one-way
- Published by: Codex via `lark-cli`

