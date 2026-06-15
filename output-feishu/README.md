---
title: "Output Feishu"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - output
  - feishu
  - publishing
---

# Output Feishu

`output-feishu/` 是从 Obsidian vault 导出、清洗、过滤后的飞书发布中间层。

## Role

```text
Obsidian Vault
  ↓
导出 / 清洗 / 过滤
  ↓
output-feishu/
  ↓
飞书 CLI 上传
  ↓
飞书知识库 / 云文档 / 云空间
```

## Source Of Truth

```text
Obsidian = 个人知识生产中心
GitHub private repo = 长期版本事实源
output-feishu = 可发布中间层
飞书知识库 = 任意地方访问 / 移动端阅读 / 分享协作
飞书 CLI = 自动同步执行器
```

## Rules

- 这里只放已经清洗、过滤、准备发布到飞书的 Markdown / assets。
- 不放 token、cookie、OAuth 状态、本地路径中的敏感信息、运行日志。
- 不把这里当知识主库；长期事实仍以 Obsidian + GitHub private repo 为准。
- 飞书上的修改默认不回流为事实，除非 Tony 明确要求导入。

## Current Outputs

- [[output-feishu/ai-first-cognitive-system/2026-06-14-ai-first-cognitive-system-online-review]]
