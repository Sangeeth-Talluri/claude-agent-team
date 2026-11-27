---
name: debug
description: Systematic debugging for any codebase — reproduce first, then evidence, recent changes, and the smallest fix that the evidence supports.
---
# Debug

1. **Reproduce or characterise.** A bug you cannot reproduce gets a
   characterisation instead: exact conditions, frequency, first-seen time,
   and the input/state that triggers it. Use the Repo Map to get from
   symptom to module.
2. **Investigate first** — the investigate-first skill applies in full.
3. **Bisect with evidence:** recent commits, releases, dependency and config
   changes in the window; the failing check's own output, not a summary of it.
4. **Fix small.** The smallest change the evidence supports. No drive-by refactors.
5. **Prove it:** verify skill — the failing check now passes, plus the scoped
   test suite. A regression test that fails without the fix is the best proof;
   add one where the test setup allows it. Evidence bundle attached to the PR.
6. **Write the trap down:** if this failure could recur, propose the rule, test,
   or correction-log entry that would catch it next time.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "I have seen this bug before; skip the repro" | Reproduce or characterise first: exact conditions, frequency, first-seen time, and the input/state that triggers it. |
| "The fix is clear from the stack trace" | The investigate-first skill applies in full: two candidate causes and a separating check before any fix. |
| "A quick refactor here will prevent this whole class of bug" | Fix small. The smallest change the evidence supports; no drive-by refactors. |
| "It works now; a regression test is extra" | A regression test that fails without the fix is the best proof there is. Add one where the test setup allows it. |

## Verification

Done means:
- The reproduction or characterisation is written down before the fix.
- The evidence bundle shows the previously failing check passing, plus the scoped test suite green.
- A regression test that fails without the fix exists, or its absence is explained.
- The recurrence trap is proposed as a rule, test, or correction-log entry — or explicitly judged unnecessary, with the reason stated.
