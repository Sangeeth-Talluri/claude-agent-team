---
name: investigate-first
description: Use before diagnosing any bug, alert, or performance problem. Stops the agent from naming a cause before it has read the code and gathered evidence.
---
# Investigate First — the anti-hallucination skill

Built from Lauren Tan's most common observed failure: an agent confidently naming
a "smoking gun" it never actually verified. That is banned here.

## The rule
You may not state a cause until you have, in this order:
1. Read the actual code on the path the symptom travels (name the files).
2. Looked at the real signal: logs, metrics, traces, or the failing test output —
   quoted, with timestamps, not paraphrased from memory.
3. Checked what changed recently (deploys, config, migrations) in the window
   where the symptom started.
4. Formed at least TWO candidate causes and said what evidence would separate them.

## Language rules
- "The cause is X" requires evidence from steps 1–3 that rules out the alternative.
- Otherwise say "candidates are X and Y; the check that separates them is Z" — and run it.
- Use subagents to search in parallel when the codebase is large. Searching is
  cheap; confident guessing is expensive.

## Done means
A short evidence note: files read, signals quoted, candidates, the separating
check, and its result. That note goes in the task's evidence bundle.
