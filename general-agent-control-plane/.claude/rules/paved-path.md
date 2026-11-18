# The Paved Path — TODO(owner): name the gold standard for each, with a file link
Agents copy what they see. These are the patterns they must copy — one per job.

- New module / component / endpoint: TODO(owner): link the example to copy
- Data access (if any): TODO(owner): link the example (the one query/model/store
  pattern — no ad-hoc access scattered around)
- Error handling: TODO(owner): link the example (how errors are raised, wrapped,
  and surfaced — never swallowed silently)
- Logging: TODO(owner): link the example (the standard logger/format)
- Config & secrets: TODO(owner): how config is read; secrets only from the secret
  store / environment, never in code or fixtures
- Tests: TODO(owner): link an example unit test and an example integration test
- New dependency: justify it in the PR (what it does, why stdlib/existing deps
  do not cover it, maintenance status) — see CLAUDE.md non-negotiables

A pattern not on this list gets proposed in a PR description and approved by a
human before it becomes a second way of doing the same job.
