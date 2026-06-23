---
title: Knowledge Graph Schema
type: topic
status: stable
tags:
  - ai/schema
created: 2026-03-01
updated: 2026-03-22
---

# Knowledge Graph Schema

## Core Entities

- `company`
- `person`
- `model`
- `system`
- `paper`
- `news`
- `topic`

## Recommended Relationships

- company -> released -> model
- company -> released / operates -> system
- company -> employs / founded_by -> person
- person -> authored -> paper
- person -> affiliated_with -> company
- model -> based_on -> paper
- model -> belongs_to -> company
- system -> built_on / exposes -> model
- system -> belongs_to -> company
- news -> about -> company / person / model / system / paper / topic
- topic -> includes -> company / person / model / system / paper / news

## Practical Rule

When you create a new note, decide:

1. what entity it is
2. what existing notes it should connect to
3. whether it is stable knowledge or time-sensitive information

## Stable vs Dynamic

- Companies, people, models, systems, papers, topics: relatively stable
- News: dynamic, time-stamped, should always link back to stable entities
