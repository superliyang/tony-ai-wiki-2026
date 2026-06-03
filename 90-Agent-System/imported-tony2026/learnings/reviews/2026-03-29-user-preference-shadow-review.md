# Shadow Review

## Candidate

- title: User prefers shadow-reviewed preference capture
- ledger: `.learnings/LEARNINGS.md`
- promotion report: `.learnings/reviews/2026-03-29-user-preference-promotion-report.md`
- review timestamp: 2026-03-29 08:46:59 PDT
- execution path: requested self-improving-memory-lab plugin was unavailable, so the review was completed with the local `self-improving-learning-ledger` skill.

## Automated Recommendation

- score: 71
- recommendation: shadow
- rationale: explicit user request provides verified provenance and the fallback execution path is now recorded, but this preference has only been seen once and should stay bounded to project scope.

## Eval Gate Check

- provenance: pass; the preference came from an explicit user request in this session.
- scope: pass; the candidate is limited to this project and is not promoted to any global memory surface.
- untrusted inputs: pass; the learning is based on direct user instruction, not browser or MCP output.
- regression checks: pass; positive check is whether future preference-capture requests use a review-first flow, negative check is whether contradictory user requests prevent reuse of this learning.
- rollback: pass; delete or demote the ledger entry and stop applying it if later requests conflict.
- blast radius: pass; shadow-only review with no durable rule write outside `.learnings`.

## Decision

Keep this item as a shadow candidate only.

Do not promote to a durable rule or reusable skill until the same preference is observed again in a separate run or explicitly confirmed as a standing preference.

## Observability

- helping signal: future runs that involve preference capture naturally follow a review-first flow and match the user's stated intent.
- harming signal: the user asks for direct promotion or indicates this preference was only for this one run.
- recording location: append follow-up confirmations or contradictions to `.learnings/LEARNINGS.md`; log failures to `.learnings/ERRORS.md` if a promoted form ever causes drift.
