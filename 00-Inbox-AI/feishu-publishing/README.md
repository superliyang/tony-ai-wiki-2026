---
title: "Feishu Publishing"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - inbox
  - feishu
  - publishing
---

# Feishu Publishing

这里存放发布操作队列、发布记录和失败记录。真正的可阅读发布正文放在 `output-feishu/`。

## Folders

| Folder | Meaning |
|---|---|
| `pending/` | 待处理的发布操作记录 |
| `published/` | 已发布记录，包含飞书 URL 和 source note |
| `failed/` | 发布失败记录和重试建议 |

## Rule

```text
Obsidian is the personal knowledge production center.
GitHub private repo is the long-term versioned fact source.
output-feishu is the publishable intermediate layer.
Feishu knowledge base / docs are the online reading and collaboration surface.
Feishu CLI is the automated sync executor.
```

## Related

- [[90-Agent-System/workflows/feishu-publishing]]
- [[90-Agent-System/integrations/Feishu]]
- [[output-feishu/README]]
