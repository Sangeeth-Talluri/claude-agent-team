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
