---
name: feature-dev
description: Build a backend feature the paved-path way — spec first, backward compatibility, migration safety, observability included.
---
# Feature Development (backend / SRE)

1. **Spec first** (specs/TEMPLATE.md). Human approves the spec before code.
   Non-trivial = touches data, an API contract, a topic schema, or infra.
2. **Compatibility:** API/topic changes are additive first; consumers before
   producers on rollout; the old version keeps working until the new one is proven.
3. **Data:** migration reversible + backward compatible (CLAUDE.md rules);
   new queries ship with EXPLAIN in the evidence.
4. **Observability is part of the feature:** logs with trace IDs, a metric or
   dashboard that shows it working, an alert with a runbook if it can page.
5. **Verify:** tests + smoke + (if applicable) slo/tf-plan/k8s-dryrun checks,
   evidence bundle in the draft PR.
6. **Rollout note in the PR:** how it turns on, how it turns off, what you watch
   for the first hour.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "It is a small feature; a spec is overhead" | Non-trivial is defined by what the change touches — data, an API contract, a topic schema, infra — not by diff size. Spec first; a human approves it before code. |
| "Consumers can be updated after the producer ships" | Consumers before producers on rollout. The old version keeps working until the new one is proven. |
| "Observability can be a follow-up ticket" | Observability is part of the feature: logs with trace IDs, a metric or dashboard, an alert with a runbook if it can page. There is no follow-up ticket. |
| "The migration worked on staging; reversibility is fine" | Reversible and backward compatible is a CLAUDE.md rule, and new queries ship with EXPLAIN in the evidence — staging success proves neither. |

## Verification

Done means:
- An approved spec (specs/TEMPLATE.md) exists for the change.
- The draft PR carries the evidence bundle: tests + smoke, plus slo / tf-plan / k8s-dryrun checks where applicable, and EXPLAIN output for new queries.
- The rollout note states how the feature turns on, how it turns off, and what is watched for the first hour.
