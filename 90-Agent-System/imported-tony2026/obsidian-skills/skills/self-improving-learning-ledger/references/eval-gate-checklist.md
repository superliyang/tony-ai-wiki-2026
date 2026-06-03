# Eval Gate Checklist

Use this checklist before enabling a promoted rule or a newly extracted skill.

## 1. Provenance And Scope

- Is the original source recorded?
- Is the scope explicit: session, project, team, or global?
- Does the candidate depend on any untrusted tool or browser output?

## 2. Safety And Boundary Review

- Could this candidate amplify prompt injection or memory poisoning?
- Could it leak information across users, repos, or tenants?
- Could it silently write to a durable surface that is too broad?

## 3. Regression Checks

- Is there at least one positive test case?
- Is there at least one negative or adversarial test case?
- Is there one failure mode from a past incident library entry that should be replayed here?

## 4. Rollout Plan

- Will the first rollout be shadow-only, canary, or small-scope active?
- Who owns the rollback?
- What exact artifact gets removed or demoted if the rollout fails?

## 5. Observability

- What signal tells us the candidate is helping?
- What signal tells us it is harming behavior?
- Where will those observations be recorded: learning ledger, errors file, or incident note?

## 6. Ship / No-Ship Rule

Ship only when all six are true:

- provenance is clear
- scope is bounded
- regression checks exist
- rollback path is explicit
- blast radius is acceptable
- promotion is better than simply keeping the item in the ledger
