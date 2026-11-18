# CLAUDE.md — TODO(owner): make every line true for THIS repo, then delete the TODOs
<!-- Keep this file under 200 lines. Procedures belong in skills, not here. -->

## What this repo is
TODO(owner): one or two sentences — project/product name, what it does, who uses it.
TODO(owner): environments — local / staging / production, and how each is reached.

## Stack
TODO(owner): languages, frameworks, and the main libraries that shape how code is
written here (e.g. TypeScript + React + Node, Python + FastAPI, Go, Java + Spring,
Rust). List only what is actually in this repo.

## Commands (agents must use these, not invent their own)
- Build: TODO(owner)       e.g. `npm run build` / `make build` / `cargo build`
- Test: TODO(owner)        e.g. `npm test` / `pytest -q` / `go test ./...`
- Lint: TODO(owner)        e.g. `npm run lint` / `make lint` / `ruff check .`
- Typecheck: TODO(owner)   e.g. `npm run typecheck` / `mypy .` (delete if not applicable)
- Run locally: TODO(owner)

## The paved path (one blessed way per job — details in .claude/rules/paved-path.md)
- New module / component / endpoint: TODO(owner): point at the one gold-standard
  example to copy.
- Data access: TODO(owner): the one pattern, if this repo touches data. No ad-hoc
  queries or file formats scattered around.
- Error handling & logging: TODO(owner): the standard pattern/library.
- Config & secrets: TODO(owner): how config is read; secrets only from the secret
  store / environment, never committed.
- Tests: TODO(owner): where tests live, the one test pattern to copy.

## Non-negotiables
- **Never force-push. Never push directly to `main` / `master`.** Work happens on
  branch `claude/<task-id>` in a git worktree; pull requests are how code lands.
- **Destructive data changes need human approval first** — dropping tables/columns,
  deleting or rewriting stored data, irreversible migrations, bulk deletes.
- **Production deploys are done or approved by a human.** Agents prepare releases;
  they do not ship them.
- **New dependencies need a justification** in the PR: what it does, why the
  standard library / existing deps do not cover it, and that it is maintained.
- If this repo has a database: migrations must be reversible and backward
  compatible with the previous released version; no destructive change in the
  same release that stops using the thing being destroyed.

## Agent rules
- Spec first for anything non-trivial: `specs/TEMPLATE.md`, human approves the spec
  before code (Plan 3).
- No evidence bundle = no PR. The verifier is never the agent that wrote the code.
- Banned: workaround/temporary comments without a linked issue, silent error
  swallowing, disabling or weakening a failing test to make checks pass, skipping
  lint/typecheck instead of fixing the finding.
- Dangerous operations are blocked by hook and listed in
  `.claude/rules/dangerous-operations.md`. Do not try to route around them.
