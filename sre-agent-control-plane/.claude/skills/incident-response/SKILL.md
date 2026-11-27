---
name: incident-response
description: Support a live incident — timeline, impact, mitigation before root cause, and a blameless record. Agents assist; humans command.
---
# Incident Response (agent's role)

The human incident commander commands. The agent is the scribe and the fetcher.

1. **Timeline as you go:** timestamped entries — signal, action, result.
   Facts only; mark anything unverified as (unconfirmed).
2. **Impact statement, kept current:** who/what is affected, since when,
   which SLO is burning.
3. **Mitigation before root cause.** Rollback, flag-off, scale, failover —
   the agent prepares these options with their risks; a human approves and acts.
   Agents never execute production mitigations themselves.
4. **Fetch, don't guess:** logs, metrics, recent changes — quoted, via
   investigate-first discipline, in parallel where possible.
5. **After:** draft the post-incident review from the timeline — what happened,
   what worked, action items with owners. No blame language, ever.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "Find the root cause first; then we will know how to fix it" | Mitigation before root cause. Always, in that order. |
| "I will just run the rollback myself to save time" | Agents never execute production mitigations. Prepare the option with its risks; a human approves and acts. |
| "The timeline can be reconstructed afterwards from chat" | Timeline as you go. Reconstruction from memory is how facts get invented; anything unverified is marked (unconfirmed). |
| "The impact is roughly the checkout flow" | The impact statement is kept current and names who/what is affected, since when, and which SLO is burning. Roughly is not a statement. |

## Verification

Done means:
- A timestamped timeline exists, with unverified entries marked (unconfirmed).
- A current impact statement names the affected users/services and the SLO that is burning.
- Every mitigation taken was prepared with its risks and approved and executed by a human.
- A post-incident review draft exists: what happened, what worked, action items with owners, and no blame language.
