---
name: using-our-skills
description: The router for this control plane. Read first on any new task — it maps the task to the skill that owns it and states the shared operating rules once, so no other skill has to repeat them.
---
# Using Our Skills — the router

Every task that arrives here routes to exactly one owning skill. Route first,
then work. If a task spans two rows, the earlier phase owns it until its
Verification section is satisfied, then hand off.

## Routing table

| The task is… | Owning skill |
|---|---|
| A vague symptom ("exports are broken", "the app is slow since Tuesday"), or any bug, report, or change where the place in the code is not yet named | `repo-map` — read the map first, then continue to the row below that fits |
| Diagnosing anything: a bug, a failure, a performance problem — any "what is causing this?" | `investigate-first` — no cause may be named before it runs |
| Fixing a bug whose cause is established | `debug` (it pulls in `investigate-first` in full) |
| A live production problem affecting real users right now | `production-issue` — the human commands; the agent scribes and fetches |
| Building a new feature | `feature-dev` |
| Reviewing a change or PR | `code-review` |
| Making something faster or cheaper | `perf` |
| Proving something works, is fast enough, or is safe to ship | `verify` |

## Shared operating rules (from this repo's CLAUDE.md — stated once, here)

- Never force-push. Never push directly to `main` / `master`. Work happens on
  branch `claude/<task-id>` in a git worktree; pull requests are how code lands.
- Spec first for anything non-trivial (`specs/TEMPLATE.md`); a human approves
  the spec before code.
- No evidence bundle = no PR. The verifier is never the agent that wrote the
  code.
- Destructive data changes need human approval first — dropping tables or
  columns, deleting or rewriting stored data, irreversible migrations, bulk
  deletes. If the repo has a database: migrations reversible and backward
  compatible, no destructive change in the same release that stops using it.
- Production deploys are done or approved by a human. Agents prepare releases;
  they do not ship them.
- New dependencies need a justification in the PR: what it does, why the
  standard library / existing deps do not cover it, and that it is maintained.
- Banned: workaround/temporary comments without a linked issue, silent error
  swallowing, disabling or weakening a failing test to make checks pass,
  skipping lint/typecheck instead of fixing the finding.
- Dangerous operations are blocked by hook and listed in
  `.claude/rules/dangerous-operations.md`. Do not try to route around them.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "This task is simple; I do not need to route it" | Routing is one table lookup. Simple tasks routed wrong are how a diagnosis starts without investigate-first. |
| "Two skills fit; I will blend them" | One owner per phase. Finish the owning skill's Verification, then hand off — blending is how steps get skipped. |
| "The shared rules are in CLAUDE.md; I know them" | They are restated here because this is the file read at task start. Knowing them is shown by following them, starting with the branch and the evidence bundle. |

## Verification

Done means:
- The report names the skill the task routed to, and the routing matches the table above.
- Any handoff between skills happened only after the previous skill's Verification section was satisfied.
