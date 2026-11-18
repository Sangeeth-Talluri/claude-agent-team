---
name: verify
description: Run this repo's verification checks and produce an evidence bundle. Use before opening any PR, after any fix, and whenever asked whether something works, is fast enough, or is safe to ship.
---
# Verify — the verification skill

Claims are not verification. This skill runs the real checks and files the output
as evidence under `evidence/<task-id>/` (report.json + one log per check).

## Commands
    python3 .claude/skills/verify/scripts/verify.py list
    python3 .claude/skills/verify/scripts/verify.py run <check> --task <task-id>
    python3 .claude/skills/verify/scripts/verify.py all --task <task-id>

Standard checks (each is just a command in `verify.config.yaml` — see the example
file, and STACK_EXAMPLES.md at the kit root for per-stack commands):
- `tests` — the repo's test suite (or the scoped subset for this task)
- `lint` — linters / static analysis
- `typecheck` — the type checker, if the stack has one
- `build` — the real build/compilation step
- `smoke` — run the built thing and assert a real response (health route, CLI
  invocation, app start) — "it compiled" is not a smoke check

Repos add their own checks in the same file — `e2e`, `bench`, `audit`,
per-area test scopes, a data-migration dry run — the CLI treats every entry
the same way: the command's exit code is the verdict.

## How to read results
- Exit code is the verdict. A check that is NOT CONFIGURED (exit 2 from the CLI)
  means the check does not exist yet — say that plainly; never report it as passed.
- For `tests`: quote the failing test names and the first real error, not a summary.
- For `smoke`: the response/status you asserted on goes in your summary.
- For benchmark-style checks: report before/after numbers side by side, with the
  raw output in the log.

## Evidence bundle shape
evidence/<task-id>/report.json — per check: status, exit code, duration, log file.
evidence/<task-id>/<check>.log — the full raw output. Summaries never replace logs.
