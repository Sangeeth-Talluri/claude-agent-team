---
name: investigate-first
description: Use before diagnosing any bug, failure, or performance problem. Stops the agent from naming a cause before it has read the code and gathered evidence.
---
# Investigate First — the anti-hallucination skill

Built from a common observed failure: an agent confidently naming
a "smoking gun" it never actually verified. That is banned here.

## The rule
You may not state a cause until you have, in this order:
1. Read the actual code on the path the symptom travels (name the files).
2. Looked at the real signal: the failing test output, logs, an error report,
   a profiler trace, or the user's exact repro steps — quoted, not paraphrased
   from memory.
3. Checked what changed recently (commits, releases, dependency updates, config)
   in the window where the symptom started.
4. Formed at least TWO candidate causes and said what evidence would separate them.

## Language rules
- "The cause is X" requires evidence from steps 1–3 that rules out the alternative.
- Otherwise say "candidates are X and Y; the check that separates them is Z" — and run it.
- Use subagents to search in parallel when the codebase is large. Searching is
  cheap; confident guessing is expensive.

## Done means
A short evidence note: files read, signals quoted, candidates, the separating
check, and its result. That note goes in the task's evidence bundle.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "This stack trace points straight at the cause" | A trace is a signal, not a verdict. Read the actual code on the path the symptom travels first, and name the files. |
| "I have read the code; that is enough to name the cause" | Steps 1–3 all precede a cause: the code, the real signal quoted (not paraphrased from memory), and what changed recently. Then at least two candidates. |
| "One candidate is clearly stronger; the second is a formality" | The second candidate is what makes the separating check real. No separating check, no cause statement. |
| "Summarising the failing output is faster than quoting it" | Signals are quoted — the failing test output, the error report, the user's exact repro steps. Paraphrase from memory is the failure this skill exists to stop. |

## Verification

Done means:
- An evidence note exists listing: files read, signals quoted, at least two candidate causes, the separating check, and its result.
- Any sentence of the form "the cause is X" cites evidence from steps 1–3 that rules out the alternative candidate.
- The evidence note is filed in the task's evidence bundle.
