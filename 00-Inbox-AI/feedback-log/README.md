---
title: "Feedback Log"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - feedback
  - ai-first
  - learning-loop
---

# Feedback Log

这里记录 Tony 对 AI 产出的轻量反馈。

## Why

系统不能只会“生产文档”，还要知道哪些产出真的有用。

## Feedback Commands

| Command | Meaning |
|---|---|
| `有用` | 这个方向和格式可以保留 |
| `太长` | 下次压缩 |
| `太浅` | 下次需要更深、更具体 |
| `跑偏` | 意图识别或材料选择错了 |
| `继续放大` | 需要 Codex 继续深入 |
| `入库` | 可以进入 canonical knowledge |
| `发飞书` | 需要生成 `output-feishu/` |
| `暂停` | 这个方向先停 |

## Output Shape

```yaml
date:
source_output:
feedback:
decision:
next_system_adjustment:
```

## Rule

反馈不等于正式 review，但可以成为下一次 Hermes 意图路由和 Codex 输出格式的依据。

