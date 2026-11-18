# Dangerous Operations — agents never run these
Enforced by `.claude/hooks/block-dangerous.sh` (PreToolUse). Keep the two in sync.

- Force pushes (`git push --force`, `-f`, `--force-with-lease`), and any direct
  push to `main` / `master`
- `rm -rf /`, disk formatting, raw disk writes
- Piping a downloaded script into a shell: `curl | sh`, `curl | bash`,
  `wget | sh`, `wget | bash` — download it, read it, then run it, if at all
- `DROP DATABASE` / `DROP TABLE` / `TRUNCATE TABLE` in any client
- Destructive cloud deletes: terminating instances, deleting databases, buckets,
  resource groups, or whole projects (`aws ec2 terminate-instances`,
  `aws rds delete-db*`, `aws s3 rb`, `gcloud projects delete`,
  `gcloud sql instances delete`, `az group delete`, and their equivalents)
- TODO(owner): add your repo's own — production deploy commands, package-registry
  publishes, data-backfill scripts, bulk email/notification sends

Not hook-blockable, same rule — these need explicit human approval outside the
agent session, every time:
- Production deploys and rollbacks
- Destructive data changes: irreversible migrations, bulk deletes/updates,
  rewriting or backfilling stored data
- Publishing a release (package registry, app store, container registry `latest`)

If a task genuinely needs one of these, the agent stops, writes down exactly
what should be run and why, and a human runs it. That is not a failure —
that is the system working.
