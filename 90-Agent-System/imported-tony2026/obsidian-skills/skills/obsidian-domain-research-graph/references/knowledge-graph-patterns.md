# Knowledge Graph Patterns

## Core Principle

Every note type should exist because it answers a different kind of question.

- `Topic`: what does this concept mean
- `Entity`: who or what is this concrete thing
- `System`: how is capability packaged into a product or platform
- `Map`: how do the pieces relate
- `Index`: where should I go next

## Useful Relation Types

Choose only the relation types that matter for the domain.

- entity -> system
- company -> model
- company -> person
- topic -> system
- topic -> paper
- workflow -> tool
- tool -> framework
- region -> market case
- scenario -> runbook

## Good Graph Behavior

A graph is healthy when:

- new notes have an obvious home
- entity notes do not duplicate topic notes
- maps explain structure at a glance
- indexes give reading order, not just lists
- relationships can be followed in more than one direction

## Common Failure Modes

- concrete products mixed into abstract topic folders
- entity pages used as dumping grounds for all related concepts
- maps that duplicate indexes without adding structure
- progress notes that are never updated after topology changes
- too many note types with no clear boundary
