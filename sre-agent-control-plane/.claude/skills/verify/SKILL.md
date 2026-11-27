---
name: verify
description: Run this repo's verification checks and produce an evidence bundle. Use before opening any PR, after any fix, and whenever asked whether something works, is fast enough, or is safe to ship.
---
# Verify — the backend/SRE verification skill

Claims are not verification. This skill runs the real checks and files the output
as evidence under `evidence/<task-id>/` (report.json + one log per check).

## Commands
    python3 .claude/skills/verify/scripts/verify.py list
    python3 .claude/skills/verify/scripts/verify.py run <check> --task <task-id>
    python3 .claude/skills/verify/scripts/verify.py all --task <task-id>

Standard checks (each is just a command in `verify.config.yaml` — see the example):
- `tests` — the repo's test suite (or the scoped subset for this task)
- `lint` — linters / static analysis
- `smoke` — hit the staging/local service and assert a real response
- `query-plan` — EXPLAIN (not EXPLAIN ANALYZE on prod — ever) for new/changed queries
- `slo` — query the observability system for the service's key SLI over a window
- `tf-plan` — `terraform plan` in a sandbox workspace; a plan that destroys is a FAIL
- `k8s-dryrun` — `kubectl apply --dry-run=server` / manifest lint
- `migration-lint` — migration tool's validate/dry-run + a reversibility check

## How to read results
- Exit code is the verdict. A check that is NOT CONFIGURED (exit 2 from the CLI)
  means the check does not exist yet — say that plainly; never report it as passed.
- For `query-plan`: look for sequential scans on large tables, missing indexes,
  and row estimates wildly off. Quote the plan lines in your summary.
- For `slo`: report the number and the window, and the before/after if you have both.
- For `tf-plan`: count adds/changes/destroys out loud. Any destroy needs a human.

## Evidence bundle shape
evidence/<task-id>/report.json — per check: status, exit code, duration, log file.
evidence/<task-id>/<check>.log — the full raw output. Summaries never replace logs.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "It compiles and the tests passed locally; that is verified" | Claims are not verification. The checks run through verify.py and their output is filed as evidence. |
| "That check is not configured; I will mark it passed" | NOT CONFIGURED (exit 2) means the check does not exist yet. Say that plainly; never report it as passed. |
| "My summary of the log is enough" | Summaries never replace logs. The full raw output goes in the bundle, one log per check. |
| "The tf-plan has destroys, but they are expected" | Any destroy needs a human. Adds, changes, and destroys are counted out loud, every time. |

## Verification

Done means:
- evidence/<task-id>/report.json exists with, per check: status, exit code, duration, and log file — plus one raw log per check run.
- Every verdict reported is the check's exit code, and unconfigured checks are reported as unconfigured.
- For query-plan, slo, and tf-plan results, the plan lines / SLI number and window / add-change-destroy counts are quoted in the summary.
