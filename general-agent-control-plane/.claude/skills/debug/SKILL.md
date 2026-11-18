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
