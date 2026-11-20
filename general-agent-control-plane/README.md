# Agent Control Plane — general track (any repo)
## The repo-level scaffold from Plan 1, written to fit any codebase

Copy this folder's contents into the **root of your repo** (see `INSTALL.md`).
It gives Claude Code everything the system needs, in stack-neutral form —
the same design as the backend/SRE kit, with the enforcement pointed at the risks
every repo shares instead of one stack's risks:

| Piece (Plan 1) | Here |
|---|---|
| Codebase memory | `CLAUDE.md` + `.claude/rules/` |
| Verification skill | `.claude/skills/verify/` — a working CLI that runs your tests, lint, typecheck, build, and smoke checks and writes an **evidence bundle** |
| Feature Map | `.claude/skills/repo-map/REPO_MAP.md` — modules, entry points, build/test commands, datastores, external APIs, deploy method, owners |
| Engineer skills (PStack) | `debug`, `feature-dev`, `perf`, `code-review`, `production-issue`, plus `investigate-first` (her anti-hallucination skill) |
| Agents | `.claude/agents/` — triage, planner, implementer, verifier, reviewer, gardener |
| Enforcement | `.claude/settings.json` hooks + two guard scripts: dangerous-command block, evidence gate |
| Spec-first (Plan 3) | `specs/TEMPLATE.md` — no code before an approved spec for anything non-trivial |
| Skill evals (Plan 3) | `.claude/skills/verify/evals/` starter |
| Stack help | `STACK_EXAMPLES.md` — ready-to-copy verify commands for Node/TypeScript, Python, Go, Java, Rust |

## General does not mean vague
The controls stay specific — they are just specific about cross-repo dangers:
force pushes and direct pushes to `main`, `rm -rf /`, piping a downloaded script
into a shell (`curl | sh`), `DROP DATABASE` / `DROP TABLE`, destructive cloud
deletes, unapproved production deploys, and destructive data changes. A control
that names the exact command works every time; "be careful" works never.

## Which kit should you use?
- **This one** for a general codebase — web, mobile, CLI, library, mixed stack.
- **The SRE kit** (`sre-agent-control-plane`) for a backend/SRE/database repo,
  where the sharp edges are migrations, query plans, terraform, and SLOs.
Both share the same tested verify CLI, the same evidence gate, and the same agents.

## Status
Scaffold — prompts, rules, and hooks are ready to use; the verify CLI is real code
(tested) but does nothing until you give it your repo's commands in
`.claude/skills/verify/verify.config.yaml` (a filled example ships next to it, and
`STACK_EXAMPLES.md` has per-stack commands). Nothing here touches production, and
the guard hook blocks the dangerous commands even in local sessions.
