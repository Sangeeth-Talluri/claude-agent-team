---
name: perf
description: Performance work on backend services and databases — measure with real traces and query plans, change one thing, measure again.
---
# Performance (backend / SRE)

1. **Numbers first.** No optimisation without a baseline from the verify skill:
   query-plan output, a trace, or the SLO check over a stated window.
   "Feels slow" is a starting point, never evidence.
2. **Find the real hotspot.** For databases: EXPLAIN (ANALYZE only on staging /
   read replicas — never prod), index usage, lock waits, N+1 patterns in traces.
   For services: CPU/memory profiles, downstream call fan-out, queue lag.
3. **One change at a time**, then the same measurement again, same window shape.
   Report before/after side by side with the raw logs in evidence.
4. **Cost honesty:** an index is not free (write cost, size); a cache is not free
   (staleness, invalidation). State the trade you are making in the PR.
5. If the numbers do not improve, revert and say so. A negative result written
   down is worth more than a kept change that does nothing.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "This query is obviously the bottleneck" | Numbers first. No optimisation without a baseline produced by a verify check: query-plan output, a trace, or the SLO check over a stated window. |
| "EXPLAIN ANALYZE on prod is the most accurate measurement" | Never on prod. Staging or read replicas only — accuracy is not a licence. |
| "I will batch a few optimisations together and measure once" | One change at a time, then the same measurement again, same window shape. Batched changes make the result unreadable. |
| "It did not help, but it is harmless to keep" | If the numbers do not improve, revert and say so. A written-down negative result beats a kept change that does nothing. |

## Verification

Done means:
- Baseline and after measurements come from the same check over the same window shape and sit side by side, with the raw logs in the evidence bundle.
- The trade being made (index write cost and size, cache staleness and invalidation) is stated in the PR.
- A change that did not improve the numbers is reverted, and the negative result is written down.
