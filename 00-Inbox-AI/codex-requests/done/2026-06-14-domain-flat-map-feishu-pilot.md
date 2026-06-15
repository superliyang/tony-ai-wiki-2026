---
title: "Codex Request - Publish Domain Flat Map Pilot"
created: 2026-06-14
status: done
owner: hermes
request_type: feishu-publish
priority: P1
domain: Personal-Knowledge-System
source_refs:
  - 20-Maps/领域平铺图谱.md
  - 00-Home/今日入口.md
  - 20-Maps/知识导航门户.md
desired_outputs:
  - output-feishu/domain-flat-map-online-review.md
  - Feishu published record
publish_to_feishu: true
safety_note: "Only publish cleaned navigation content. Do not include secrets, OAuth state, local account files, or raw inbox material."
---

# Codex Request - Publish Domain Flat Map Pilot

## Completion

Status: done

Outputs:

- [[output-feishu/knowledge-navigation/2026-06-14-domain-flat-map-online-review]]
- [Feishu: Tony AI Wiki 领域平铺图谱](https://my.feishu.cn/docx/TnSBdlwRboAwKHxu4DjcZKhbntd)
- [[00-Inbox-AI/feishu-publishing/published/2026-06-14-domain-flat-map-online-review-record]]

Result:

```text
Hermes request -> Codex cleaned output -> output-feishu -> Feishu CLI -> Feishu doc
```

## Task

Codex should turn [[20-Maps/领域平铺图谱]] into a cleaned online reading version under `output-feishu/`, then publish it to Feishu with `lark-cli`.

## Why It Matters

Tony wants the complete chain to run:

```text
Hermes produces actionable request
  -> Codex improves / structures content
  -> Obsidian remains source of truth
  -> output-feishu stores cleaned publish version
  -> Feishu CLI uploads online reading version
```

This is a good pilot because the source content is already reviewed enough for navigation use, contains no raw private inbox material, and directly improves Tony's company-computer / mobile reading experience.

## Source Context

- [[20-Maps/领域平铺图谱]]
- [[00-Home/今日入口]]
- [[20-Maps/知识导航门户]]
- [[90-Agent-System/workflows/hermes-codex-feishu-pipeline]]
- [[90-Agent-System/workflows/feishu-publishing]]

## Desired Output

- Create a cleaned Markdown file under `output-feishu/knowledge-navigation/`.
- Keep the domain grouping, but make it suitable for online reading.
- Include source-of-truth note references back to the vault paths.
- Publish to Feishu using `lark-cli docs +create`.
- Write a publication record under `00-Inbox-AI/feishu-publishing/published/`.
- Move this request to `done/` and include output links.

## Acceptance Criteria

- [ ] `output-feishu/knowledge-navigation/` contains the cleaned publish-ready doc.
- [ ] Feishu URL is recorded.
- [ ] Source note remains canonical.
- [ ] No raw inbox material is published.
- [ ] No secrets, OAuth state, local auth files, or tokens are included.

## Suggested Next Action

Codex should process this as the first end-to-end Hermes -> Codex -> Obsidian -> output-feishu -> Feishu pilot.
