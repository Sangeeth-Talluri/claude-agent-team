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
