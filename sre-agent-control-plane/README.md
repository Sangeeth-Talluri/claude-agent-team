# SRE Agent Control Plane — backend / SRE track
## The repo-level scaffold from Plan 1, tailored to a backend / SRE / database repo

Copy this folder's contents into the **root of your work repo** (see `INSTALL.md`).
It gives Claude Code everything Lauren Tan's system needs, in backend/SRE form:

| Piece (Plan 1) | Here | Web track equivalent you're NOT using |
|---|---|---|
| Codebase memory | `CLAUDE.md` + `.claude/rules/` | same |
| Verification skill | `.claude/skills/verify/` — a working CLI that runs your tests, smoke checks, query plans, SLO checks, terraform plan, k8s dry-run, migration lint and writes an **evidence bundle** | Playwright / Chrome DevTools traces |
| Feature Map | `.claude/skills/service-map/SERVICE_MAP.md` — services, endpoints, datastores, topics, jobs, SLOs, runbooks | UI feature map |
| Engineer skills (PStack) | `debug`, `feature-dev`, `perf`, `code-review`, `incident-response`, plus `investigate-first` (her anti-hallucination skill) | same, web-flavoured |
| Agents | `.claude/agents/` — triage, planner, implementer, verifier, reviewer, gardener | same |
| Enforcement | `.claude/settings.json` hooks + two guard scripts: dangerous-command block, evidence gate | same |
| Spec-first (Plan 3) | `specs/TEMPLATE.md` — no code before an approved spec for anything non-trivial | same |
| Skill evals (Plan 3) | `.claude/skills/verify/evals/` starter | same |

## Tailored to your world, not a generic template
Database and SRE rules are baked in: migrations must be reversible and backward
compatible, new queries need an EXPLAIN, terraform is plan-only for agents,
no production writes ever, SLOs and runbooks are part of "done".

## Status
Scaffold — prompts, rules, and hooks are ready to use; the verify CLI is real code
(tested) but does nothing until you give it your repo's commands in
`.claude/skills/verify/verify.config.yaml` (a filled example ships next to it).
Nothing here touches production, and the guard hook blocks the dangerous commands
even in local sessions.
