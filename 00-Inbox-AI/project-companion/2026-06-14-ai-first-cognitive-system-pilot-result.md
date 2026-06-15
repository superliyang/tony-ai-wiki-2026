---
title: "Project Companion Pilot Result - AI First Cognitive System"
created: 2026-06-14
status: completed
source: codex-project-companion
project: "AI First Cognitive System"
tags:
  - project-companion
  - ai-first
  - pilot-result
---

# Project Companion Pilot Result - AI First Cognitive System

## Project Status

`active`

The project has enough structure to operate:

- vault map and fixed entrances exist;
- Hermes/Codex learning chain exists;
- memory protocol exists;
- review queue exists;
- Personal Agent capability mapping exists;
- Project Companion workflow exists.

## Main Finding

The next constraint is flow, not structure.

Queue snapshot before creating this pilot review item:

| Queue | Count |
|---|---:|
| `learning-tasks/pending/` | 42 files, including `.gitkeep` |
| `learning-tasks/in-progress/` | 6 files, including `.gitkeep` |
| `review-queue/pending/` | 17 files |

The strongest bottleneck is `review-queue/pending/`: Codex packages are ready, but accepted/promoted knowledge is not moving.

## Bottlenecks

- Substantive learning package reviews are mixed with noisy daily memory reviews.
- Hermes is producing useful scout and synthesis output, but normalized `signals/` and `candidates/` are still underused.
- Project Companion should remain manual until the first cycle proves useful.
- Hermes CLI exists, but current default provider/model configuration appears broken, so direct Hermes oneshot execution should wait.

## Actions Taken

- Updated [[40-Projects/AI-First-Cognitive-System/README]] with current status and bottlenecks.
- Created [[40-Projects/AI-First-Cognitive-System/下一步]].
- Kept `hermes-project-companion-scout` paused.
- Created a review item for Tony's smallest decision.

## Hermes Live Test

Codex triggered a Hermes oneshot live test after the pilot.

Result:

```text
No new file created.
Existing pilot result already captures the current project-continuity signal.
```

This confirms Hermes can run the Project Companion scout on demand without automatically creating duplicate notes.

## Recommended Next Decision

Do not activate the scheduled Hermes Project Companion scout yet.

Instead:

1. run Project Companion on demand when Tony asks;
2. clean review gate and memory-review routing;
3. consider scheduled weekly scout only after repeated on-demand runs stay low-noise.
