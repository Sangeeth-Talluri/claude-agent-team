# Dangerous Operations — agents never run these
Enforced by `.claude/hooks/block-dangerous.sh` (PreToolUse). Keep the two in sync.

- `terraform apply` / `terraform destroy` — plan is fine; humans apply
- `kubectl delete` / `kubectl drain`, `helm uninstall` — humans only
- `DROP DATABASE` / `DROP TABLE` / `TRUNCATE TABLE` in any client
- Force pushes, and any direct push to `main` / `master`
- `rm -rf /`, disk formatting, raw disk writes
- TODO(owner): add your repo's own — prod DB clients, cloud delete commands,
  feature-flag flips in prod, queue purges, cache flushes on shared clusters

If a task genuinely needs one of these, the agent stops, writes down exactly
what should be run and why, and a human runs it. That is not a failure —
that is the system working.
