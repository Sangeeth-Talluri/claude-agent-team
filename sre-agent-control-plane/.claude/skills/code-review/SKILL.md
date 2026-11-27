---
name: code-review
description: Review backend/SRE changes — spec match, paved path, migration and query safety, failure modes, evidence completeness.
---
# Code Review (backend / SRE)

Review in the reviewer agent's order: spec match → paved path → database safety
(migration reversible? EXPLAIN sane?) → failure modes (timeouts, retries,
idempotency, partial failure) → SLO/runbook → evidence completeness.

Backend-specific traps to always look for:
- Retries without idempotency, or without backoff, on a non-idempotent operation
- A transaction that spans a network call
- A migration that locks a large table during business hours
- A new consumer that is not safe to replay (Kafka/PubSub redelivery)
- A terraform change whose plan destroys or replaces a stateful resource
- Errors swallowed at a boundary where an alert should fire

Numbered findings, specific lines. Missing evidence blocks. Style nits do not.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "The migration looks standard; no need to check reversibility" | Standard-looking migrations lock large tables too. Reversibility and lock behaviour are checked on every migration, not sampled. |
| "The author surely made the retries idempotent" | Retries without idempotency are the first trap on this skill's list precisely because authors forget them. Check the operation, not the intention. |
| "There is no evidence bundle, but the diff looks fine" | Missing evidence blocks. A good-looking diff is not evidence. |
| "The style is rough; I will spend the review on that" | Style nits do not block and do not lead. Spec match, safety, and failure modes come first, in the reviewer agent's order. |

## Verification

Done means:
- Numbered findings exist, each tied to a specific line.
- Every trap on this skill's list is explicitly cleared or flagged — none silently skipped.
- The verdict (block / approve) names the evidence it rests on; missing evidence is itself a blocking finding.
