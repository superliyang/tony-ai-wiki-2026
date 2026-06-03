# Tony AI Wiki Agent Guide

This repository is Tony's AI First knowledge system. Agents should respect the three-layer design:

| Layer | Paths | Rule |
|---|---|---|
| Knowledge assets | `10-Knowledge/`, `30-Playbooks/`, `40-Projects/` | Preserve context, promote only bounded slices, link sources |
| Human navigation | `00-Home/`, `20-Maps/` | Keep entry points readable and current |
| AI collaboration | `00-Inbox-AI/`, `60-Agents/`, `90-Agent-System/` | Follow protocols, state boundaries, keep review gates visible |

## Legacy Vault

Old `tony2026` material has been imported, not destroyed or flattened.

- Knowledge source: `10-Knowledge/_Imported/tony2026/`
- Migration map: `20-Maps/旧库迁移地图.md`
- Agent workflow: `90-Agent-System/workflows/legacy-vault-migration.md`

Before changing imported content, read the migration workflow. Prefer creating reviewed, crystallized notes in current formal domains and linking back to imported source notes.

## Fixed Entrances

- Repository map: `90-Agent-System/仓库地图.md`
- Current state: `90-Agent-System/当前状态.md`
- Naming conventions: `90-Agent-System/命名规范.md`
- Cross-tool map: `20-Maps/跨工具协作地图.md`
- Next actions for humans: `00-Home/下一步.md`

## Editing Style

- Prefer Chinese explanatory text with English technical terms preserved where useful.
- Use Obsidian wikilinks for internal notes.
- Keep AI-generated material in `00-Inbox-AI/` until it is reviewed or explicitly promoted.
- Update maps and domain overviews when the structure changes.
