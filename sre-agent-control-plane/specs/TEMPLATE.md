# Spec — TODO: <task title>
<!-- Plan 3, spec-first: a human approves this BEFORE code is written.
     Keep it to one page. If it needs more, the task is probably two tasks. -->

## Problem
What is wrong or missing, in plain words, with the evidence that shows it.

## Proposed change
What will be built/changed — services, endpoints, data, infra, from the Service Map.

## NOT doing
What is explicitly out of scope for this task.

## Data & compatibility
Migrations (reversible? backward compatible?), API/topic changes (additive?),
rollout order, how it turns off.

## Acceptance checks
Each check must be runnable by the verify skill. List them:
- [ ] tests: <scope>
- [ ] smoke: <what it proves>
- [ ] query-plan / slo / tf-plan / k8s-dryrun / migration-lint: <as applicable>

## Risks
What could go wrong, who notices first, and the rollback.
