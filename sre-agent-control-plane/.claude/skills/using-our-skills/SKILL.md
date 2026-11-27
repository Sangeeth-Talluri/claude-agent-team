---
name: using-our-skills
description: The router for this control plane. Read first on any new task — it maps the task to the skill that owns it and states the shared operating rules once, so no other skill has to repeat them.
---
# Using Our Skills (backend / SRE) — the router

Every task that arrives here routes to exactly one owning skill. Route first,
then work. If a task spans two rows, the earlier phase owns it until its
Verification section is satisfied, then hand off.

## Routing table

| The task is… | Owning skill |
|---|---|
| A vague symptom ("checkout is slow", "the nightly job is late"), or any alert, bug, or change where the service is not yet named | `service-map` — read the map first, then continue to the row below that fits |
| Diagnosing anything: a bug, an alert, a performance problem — any "what is causing this?" | `investigate-first` — no cause may be named before it runs |
| Fixing a bug whose cause is established | `debug` (it pulls in `investigate-first` in full) |
| A live incident in progress | `incident-response` — the human commands; the agent scribes and fetches |
| Building a new backend feature | `feature-dev` |
| Reviewing a change or PR | `code-review` |
| Making something faster or cheaper | `perf` |
| Proving something works, is fast enough, or is safe to ship | `verify` |

## Shared operating rules (from this repo's CLAUDE.md — stated once, here)

- Work in a git worktree on branch `claude/<task-id>`. Draft PRs only. Never
  push to main.
- Spec first for anything non-trivial (`specs/TEMPLATE.md`); a human approves
  the spec before code.
- No evidence bundle = no PR. The verifier is never the agent that wrote the
  code.
- Database rules are non-negotiable: no query without an index story (EXPLAIN
  in the evidence), migrations reversible and backward compatible, and agents
  never write to a production database — read-only staging is the ceiling.
- Agents prepare changes; they do not approve or submit them. A new alert
  ships with a runbook link, or it does not ship.
- Banned: workaround/temporary comments without a linked issue, silent error
  swallowing, disabling a failing test to make CI pass, new dependencies
  without naming why in the PR.
- Dangerous operations are blocked by hook and listed in
  `.claude/rules/dangerous-operations.md`. Do not try to route around them.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "This task is simple; I do not need to route it" | Routing is one table lookup. Simple tasks routed wrong are how a diagnosis starts without investigate-first. |
| "Two skills fit; I will blend them" | One owner per phase. Finish the owning skill's Verification, then hand off — blending is how steps get skipped. |
| "The shared rules are in CLAUDE.md; I know them" | They are restated here because this is the file read at task start. Knowing them is shown by following them, starting with the worktree and the evidence bundle. |

## Verification

Done means:
- The report names the skill the task routed to, and the routing matches the table above.
- Any handoff between skills happened only after the previous skill's Verification section was satisfied.
