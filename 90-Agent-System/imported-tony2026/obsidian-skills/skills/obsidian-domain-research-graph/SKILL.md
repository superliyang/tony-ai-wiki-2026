---
name: obsidian-domain-research-graph
description: "Research a domain deeply, turn it into an Obsidian knowledge graph, define note layers and relationships, and maintain the graph over time. Use when Codex needs to bootstrap or evolve a domain knowledge base in an Obsidian vault: scoping a field, creating entity/topic/system layers, building indexes and maps, connecting notes with wiki-links, recording progress and resume state, or preparing the domain for periodic updates."
---

# Obsidian Domain Research Graph

## Overview

Use this skill when the goal is not just to write a few notes, but to turn a domain into a durable Obsidian knowledge system.

This skill is for workflows like:

- deeply studying a new field
- creating a domain knowledge graph
- deciding what kinds of notes should exist
- defining note relationships
- setting up indexes, maps, and study paths
- maintaining the graph over time as the domain evolves

For Git checkpointing or periodic GitHub sync, pair this skill with [$knowledge-vault-research-sync](/Users/tony/.codex/skills/knowledge-vault-research-sync/SKILL.md).

## Core Outcome

Turn a domain into four things at once:

- a structured note topology
- a readable learning path
- a usable knowledge graph
- a maintainable update loop

## Autonomous Graph Delivery Mode

When the user wants continuous progress without interruptions, switch from one-note execution to graph-level batch delivery.

In this mode:

- inspect the current graph first
- identify the top topology or coverage gaps
- choose one coherent graph slice to complete
- update the slice end-to-end, including indexes, maps, progress, and resume pages when needed
- reflect on what the graph still cannot explain clearly
- continue until a version-ready improvement has been delivered

Read [references/autonomous-delivery-loop.md](references/autonomous-delivery-loop.md) when using this mode.

## Workflow

### 1. Define the domain boundary

Start by answering:

- what domain are we studying
- what is inside scope
- what is outside scope
- whether the goal is conceptual understanding, market landscape, engineering practice, business application, or a mix

Do not start by creating random notes. Start by deciding what kind of graph this domain needs.

### 2. Choose the right note layers

Most domains should separate at least some of these layers:

- `Foundations`: history, core concepts, canonical distinctions
- `Entities`: companies, people, products, protocols, tools, institutions
- `Topics`: abstract concepts, methods, problem spaces
- `Systems`: concrete products, platforms, services, runtimes
- `Maps`: topology and relationship views
- `Templates`: repeatable note structures
- `Progress`: where the learner currently is
- `Resume`: how to restart quickly after interruption

Do not force every domain to use every layer. Use only the layers that clarify the field.

### 3. Define the graph schema before scaling content

Before creating many notes, decide:

- what note types exist
- what fields matter in frontmatter
- what relationships should be expressed through wiki-links
- which pages are indexes versus entities versus maps

Examples of useful relationship questions:

- which company created which system
- which system belongs to which product category
- which topic explains which systems
- which papers support which models or methods
- which workflows depend on which tools

Use [references/knowledge-graph-patterns.md](references/knowledge-graph-patterns.md) when deciding the relationship structure.

### 4. Build the minimum viable domain skeleton

For a new domain, create at least:

- a domain `专题总览.md`
- one main `主题索引.md`
- one `地图索引.md` if maps will matter
- one `学习进度.md`
- one `恢复笔记.md`
- one recommended path from beginner to intermediate

Do not try to fill every detail before the skeleton exists.

### 5. Add notes in graph-aware order

Prefer this order:

1. create the main indexes and maps
2. add foundational topics
3. add high-value entities or systems
4. connect them with explicit links
5. only then deepen coverage

Each new note should answer at least one graph question, not just add surface-level content.

### 6. Keep the topology clean while expanding

When expanding a vault:

- abstract concepts go in topic pages
- concrete objects go in entity or system pages
- maps explain structure, not detail
- indexes are navigation pages, not dumping grounds

If a note feels “in the wrong layer”, fix the topology rather than forcing more content into the wrong place.

### 7. Preserve learning state

Every mature domain should preserve three memory layers:

- map memory: structure, indexes, recommended routes
- progress memory: current topic, next step, weak points
- resume memory: quick restart note

Whenever the domain topology changes meaningfully, update progress and resume pages.

### 8. Plan the maintenance loop

A good domain graph is not finished once written. Decide how it will stay current:

- what should be updated periodically
- which indexes drift fastest
- which maps need refreshes when new entities appear
- which notes are stable versus volatile

Use [references/update-loop.md](references/update-loop.md) for the maintenance model.

## Working Rules

- Build the graph before optimizing the details.
- Prefer clean layers over dense but confusing coverage.
- Connect notes through meaningful relationships, not decorative links.
- Update indexes and maps when topology changes.
- Keep progress and resume notes small but current.
- In autonomous mode, stop only at coherent version boundaries rather than after isolated note edits.
- When periodic syncing or GitHub checkpoints matter, hand off to [$knowledge-vault-research-sync](/Users/tony/.codex/skills/knowledge-vault-research-sync/SKILL.md).

## Deliverables

A good run of this skill usually leaves behind some mix of:

- a domain README
- indexes
- maps
- entity/topic/system pages
- progress and resume notes
- a clearer ontology for future notes

## References

- Graph patterns: [references/knowledge-graph-patterns.md](references/knowledge-graph-patterns.md)
- Obsidian topology patterns: [references/obsidian-topology-patterns.md](references/obsidian-topology-patterns.md)
- Maintenance loop: [references/update-loop.md](references/update-loop.md)
- Autonomous batch loop: [references/autonomous-delivery-loop.md](references/autonomous-delivery-loop.md)
