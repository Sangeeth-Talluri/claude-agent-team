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
