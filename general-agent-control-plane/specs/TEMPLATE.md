# Spec — TODO: <task title>
<!-- Plan 3, spec-first: a human approves this BEFORE code is written.
     Keep it to one page. If it needs more, the task is probably two tasks. -->

## Problem
What is wrong or missing, in plain words, with the evidence that shows it.

## Proposed change
What will be built/changed — modules, entry points, data, interfaces, from the Repo Map.

## NOT doing
What is explicitly out of scope for this task.

## Data & compatibility
Stored-data changes (reversible? backward compatible?), public API/schema changes
(additive?), dependency changes, rollout order, how it turns off / rolls back.

## Acceptance checks
Each check must be runnable by the verify skill. List them:
- [ ] tests: <scope>
- [ ] lint / typecheck / build: <as applicable>
- [ ] smoke: <what it proves>
- [ ] <repo-specific check>: <as applicable>

## Risks
What could go wrong, who notices first, and the rollback.
