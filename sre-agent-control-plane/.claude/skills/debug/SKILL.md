---
name: debug
description: Systematic debugging for backend services — reproduce first, then logs/metrics/traces, recent changes, and the smallest fix that the evidence supports.
---
# Debug (backend / SRE)

1. **Reproduce or characterise.** A bug you cannot reproduce gets a
   characterisation instead: exact conditions, frequency, first-seen time.
   Use the Service Map to get from symptom to service.
2. **Investigate first** — the investigate-first skill applies in full.
3. **Bisect with evidence:** recent deploys/config/migrations in the window;
   error budgets and dashboards for the service's SLO.
4. **Fix small.** The smallest change the evidence supports. No drive-by refactors.
5. **Prove it:** verify skill — the failing check now passes, plus the scoped
   test suite. Evidence bundle attached to the PR.
6. **Write the trap down:** if this failure could recur, propose the rule, test,
   alert, or correction-log entry that would catch it next time.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "I know this bug pattern; I can skip reproducing" | Reproduce or characterise first. An unreproduced bug gets a characterisation — exact conditions, frequency, first-seen time — never a guess dressed as a fix. |
| "The fix is obvious from the error message" | Obvious fixes skip investigate-first. Two candidate causes and a separating check come before any fix. |
| "While I am here, I will clean up the surrounding code" | Fix small. The smallest change the evidence supports; no drive-by refactors. |
| "Tests pass locally; that is proof enough" | Proof is the verify skill's evidence bundle: the failing check now passing, plus the scoped suite. |

## Verification

Done means:
- The reproduction or characterisation is written down before the fix.
- The evidence bundle shows the previously failing check passing and the scoped test suite green.
- The recurrence trap is proposed as a rule, test, alert, or correction-log entry — or explicitly judged unnecessary, with the reason stated.
