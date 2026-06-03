# Skills Gaming Hackathon Local Workspace

This folder is local-only and intentionally excluded from Git.

## Goal

Bootstrap a runnable local implementation workspace for `Word Search Duel V1`.

## Structure

- `docs/`: build-oriented notes
- `backend/`: FastAPI backend plus static demo frontend
- `shared/contracts/`: event and result contracts
- `client-unity-placeholder/`: Unity-side placeholder structure
- `tools/`: bootstrap, run, and smoke-test scripts

## Quick start

1. `./tools/bootstrap_backend.sh`
2. `./tools/run_backend.sh`
3. Open [http://127.0.0.1:8000](http://127.0.0.1:8000)
4. Optional smoke test: `./tools/smoke_test_demo.sh`

## Current demo

- start -> tutorial -> word-search match -> result
- 7x7 scan boards with target words
- score submission and result explanation
- event ingestion to local jsonl file
- eligibility placeholder
