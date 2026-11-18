# CLAUDE.md — TODO(owner): make every line true for THIS repo, then delete the TODOs
<!-- Keep this file under 200 lines. Procedures belong in skills, not here. -->

## What this repo is
TODO(owner): one or two sentences — service/platform name, what it does, who consumes it.
TODO(owner): environments — dev / staging / prod, and how each is reached.

## Stack
TODO(owner): languages, frameworks, databases, infra (e.g. Go + PostgreSQL + Kafka,
Kubernetes on GKE, Terraform, Liquibase). List only what is actually in this repo.

## Commands (agents must use these, not invent their own)
- Build: TODO(owner)   e.g. `make build`
- Test: TODO(owner)    e.g. `make test` / `pytest -q` / `go test ./...`
- Lint: TODO(owner)    e.g. `make lint`
- Run locally: TODO(owner)

## The paved path (one blessed way per job — details in .claude/rules/paved-path.md)
- API/RPC handler: TODO(owner): point at the one gold-standard handler to copy.
- DB access: TODO(owner): the one data-access pattern. No raw SQL scattered in handlers.
- Migrations: TODO(owner): tool + location. Every migration reversible + backward compatible.
- Background jobs / consumers: TODO(owner): the one pattern (Kafka / Pub/Sub / cron).
- Terraform: TODO(owner): module location. Agents run `plan` only — never apply.
- Logging/metrics/tracing: TODO(owner): the standard library/pattern, with trace IDs.

## Database rules (non-negotiable)
- No query without an index story. New or changed queries ship with EXPLAIN output
  in the evidence bundle (verify skill, `query-plan` check).
- Migrations: reversible, backward compatible with the previous app version,
  no destructive change (drop/rename) in the same release that stops using it.
- Agents never write to a production database. Ever. Read-only staging is the ceiling.

## SRE rules (non-negotiable)
- "Done" includes: tests, evidence bundle, and — for anything user-facing — the SLO
  or dashboard that would show a regression, named in the PR.
- New alert = runbook link in the alert. No exceptions.
- Change follows the team's normal change process. Agents prepare changes;
  they do not approve or submit them.

## Agent rules
- Work in a git worktree on branch `claude/<task-id>`. Draft PRs only. Never push to main.
- Spec first for anything non-trivial: `specs/TEMPLATE.md`, human approves the spec
  before code (Plan 3).
- No evidence bundle = no PR. The verifier is never the agent that wrote the code.
- Banned: workaround/temporary comments without a linked issue, silent error
  swallowing, disabling a failing test to make CI pass, new dependencies without
  naming why in the PR.
- Dangerous operations are blocked by hook and listed in
  `.claude/rules/dangerous-operations.md`. Do not try to route around them.
