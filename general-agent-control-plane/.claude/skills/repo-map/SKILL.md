---
name: repo-map
description: The map of this repo's modules, entry points, commands, datastores, and external APIs. Read it before investigating any bug, report, or change — and when a report names a symptom instead of a place in the code.
---
# Repo Map — this repo's Feature Map

`REPO_MAP.md` (next to this file) is materialised memory: how this codebase is
actually wired, written for an agent that just arrived. A vague report
("exports are broken", "the app is slow since Tuesday") is useless without it;
with it, the agent can go from symptom → module → entry point → check to run.

Rules:
- Read it before investigating. Name the map entries you used in your report.
- If reality disagrees with the map, say so — that is a gardener finding.
- Keep entries short and factual. Doc *links*, not doc copies.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "I know this codebase; skip the map" | Read it before investigating, and name the map entries you used in your report. Memory is not the map. |
| "The report already names a file, so the map step is done" | The map matters most when a report names a symptom instead of a place in the code — that is the route from symptom to module to the check to run. |
| "The map is out of date here; I will just ignore that part" | A disagreement between the map and reality is a gardener finding. Say so; do not silently route around it. |

## Verification

Done means:
- The report names the REPO_MAP.md entries it used to get from symptom to module to check.
- Any place where reality disagreed with the map is recorded as a gardener finding.
