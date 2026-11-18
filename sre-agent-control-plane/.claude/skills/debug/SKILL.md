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
