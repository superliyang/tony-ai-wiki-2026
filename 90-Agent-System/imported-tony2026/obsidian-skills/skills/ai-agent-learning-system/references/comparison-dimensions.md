# Comparison Dimensions

When comparing AI agent systems, try to reuse the same dimensions so notes remain composable.

## Core dimensions

- `task scope`: what kinds of work it is actually designed for
- `tool access`: terminal, browser, IDE, APIs, internal tools
- `memory model`: session-only, workspace memory, long-term memory, user-editable memory
- `runtime model`: cloud agent, local runtime, IDE-native, terminal-first, hybrid
- `autonomy level`: suggestion, partial execution, long-running execution, delegated background tasks
- `approval model`: always human-in-the-loop, configurable approvals, mostly autonomous
- `deployment mode`: consumer SaaS, enterprise SaaS, self-hosted, developer tool
- `observability`: traces, logs, checkpoints, step visibility, reviewability
- `failure recovery`: retries, checkpoints, escalation, resumability
- `target user`: consumer, knowledge worker, developer, ops team, enterprise platform team

## Writing rule

Do not compare systems by vibes only. Fill in at least six of the dimensions above.
