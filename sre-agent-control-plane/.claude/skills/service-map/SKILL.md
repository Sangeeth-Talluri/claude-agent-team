---
name: service-map
description: The map of this system's services, endpoints, datastores, topics, jobs, and SLOs. Read it before investigating any alert, bug, or change — and when a report names a symptom instead of a service.
---
# Service Map — this repo's Feature Map, in backend form

`SERVICE_MAP.md` (next to this file) is materialised memory: how the system is
actually wired, written for an agent that just arrived. A vague report
("checkout is slow", "the nightly job is late") is useless without it; with it,
the agent can go from symptom → service → datastore → check to run.

Rules:
- Read it before investigating. Name the map entries you used in your report.
- If reality disagrees with the map, say so — that is a gardener finding.
- Keep entries short and factual. Runbook *links*, not runbook copies.
