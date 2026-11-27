---
name: production-issue
description: Support a live production problem in any product — timeline, impact, mitigation before root cause, and a blameless record. Agents assist; humans command.
---
# Production Issue (agent's role)

For any live product — a site, an app, a service, a published tool — that is
misbehaving for real users right now. The human in charge commands. The agent
is the scribe and the fetcher.

1. **Timeline as you go:** timestamped entries — signal, action, result.
   Facts only; mark anything unverified as (unconfirmed).
2. **Impact statement, kept current:** who/what is affected, since when,
   how badly (errors, failed actions, rough user count if known).
3. **Mitigation before root cause.** Rollback, feature-flag off, revert the
   release, scale up, disable the broken path — the agent prepares these
   options with their risks; a human approves and executes them. Agents never
   deploy, roll back, or change production data themselves.
4. **Fetch, don't guess:** logs, error reports, status dashboards, recent
   releases/changes — quoted, via investigate-first discipline, in parallel
   where possible.
5. **After:** draft the post-issue review from the timeline — what happened,
   what worked, action items with owners. No blame language, ever.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "Find the root cause first; then we will know how to fix it" | Mitigation before root cause. Always, in that order. |
| "I will roll back the release myself to save a few minutes" | Agents never deploy, roll back, or change production data. Prepare the options with their risks; a human approves and executes. |
| "The timeline can be written up afterwards from memory" | Timeline as you go. Reconstruction from memory is how facts get invented; anything unverified is marked (unconfirmed). |
| "The impact is obvious from the alert" | The impact statement is kept current: who/what is affected, since when, and how badly. Obvious is not a statement. |

## Verification

Done means:
- A timestamped timeline exists, with unverified entries marked (unconfirmed).
- A current impact statement names who/what is affected, since when, and how badly.
- Every mitigation taken was prepared with its risks and approved and executed by a human.
- A post-issue review draft exists: what happened, what worked, action items with owners, and no blame language.
