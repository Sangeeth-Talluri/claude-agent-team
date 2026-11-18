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
