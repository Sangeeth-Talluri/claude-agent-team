---
name: perf
description: Performance work in any codebase — measure with a real benchmark or profile before changing anything, change one thing, measure again, keep both outputs as evidence.
---
# Performance

1. **Numbers first.** No optimisation without a baseline: a benchmark run, a
   profile, or a timing measurement over a stated input/window, produced by a
   verify check so the raw output lands in the evidence bundle.
   "Feels slow" is a starting point, never evidence.
2. **Find the real hotspot** from the profile/benchmark breakdown — the slowest
   operation, the repeated work (N+1 calls, re-renders, re-reads), the wait on
   I/O. Do not optimise the part that merely looks slow in the code.
3. **One change at a time**, then the same measurement again, same conditions.
   Report before/after side by side; the benchmark output from BOTH runs stays
   in the evidence bundle.
4. **Cost honesty:** a cache is not free (staleness, invalidation); an index or
   a bigger instance is not free (write cost, money); a faster path that drops
   correctness is not faster, it is wrong. State the trade in the PR.
5. If the numbers do not improve, revert and say so. A negative result written
   down is worth more than a kept change that does nothing.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "This function obviously dominates the runtime" | Numbers first. No optimisation without a baseline — a benchmark run, a profile, or a timing measurement over a stated input/window — produced by a verify check. |
| "The code that looks slow must be the hotspot" | Hotspots come from the profile or benchmark breakdown, not from reading code. Do not optimise the part that merely looks slow. |
| "Two changes, one measurement — saves a run" | One change at a time, then the same measurement again under the same conditions. Both outputs stay in the evidence bundle. |
| "No improvement, but the change is harmless to keep" | If the numbers do not improve, revert and say so. A written-down negative result beats a kept change that does nothing. |

## Verification

Done means:
- Baseline and after measurements sit side by side in the report, and the benchmark output from both runs is in the evidence bundle.
- The trade being made (cache staleness, index write cost, spend, any correctness risk) is stated in the PR.
- A change that did not improve the numbers is reverted, and the negative result is written down.
