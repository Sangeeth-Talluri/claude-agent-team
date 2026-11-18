# Claude Agent Team — plans and scaffolds

Building Lauren Tan's AI agent system (SpaceXAI / Grok Bot) in Claude:
a trusted team of agents that find work, do it, prove it, and — only when
they have earned it — merge it.

## What's here

| Folder | What it is |
|---|---|
| `plans/` | The three build plans + addendum, decoded from Lauren Tan's talks. **Plan 1:** the PR factory (verification skill, Service/Feature Map, paved path, Inner/Outer Loop). **Plan 2:** persistent bots — one bot per project, its own memory, Chief of Staff, routines, review queue. **Plan 3:** the team at full strength — loops and graphs, spec-first, skill evals, PM agent, auto-merge trust ladder. Plus the Reel 5 addendum (three-tier org). |
| `bot-company/` | Plan 2 scaffolded: Chief of Staff + Project Bot + Ops/Life Bot — bot configs, prompts, per-bot memory, routines, company rules/approvals, and the shared platform (launcher, queue, policy). |
| `sre-agent-control-plane/` | Plan 1 scaffolded for a backend / SRE / database repo: `CLAUDE.md`, 6 subagents, 8 skills (including a working verification CLI with evidence bundles), guard hooks that block dangerous operations, and spec templates. Copy its contents into a work repo root to use it (see its `INSTALL.md`). |

## Build order
1. Repo foundation + verification skill (Plan 1, Phases 0–2) in one pilot repo.
2. Inner Loop with draft PRs only (Plan 1, Phase 4).
3. One persistent bot + Chief of Staff (Plan 2, Phases 0–1).
4. Routines and the morning launch (Plan 2, Phase 3).
5. Loops/graphs, skill evals, and the auto-merge ladder (Plan 3) — last, on evidence.

## Non-negotiables (all three plans)
- The verifier is never the agent that wrote the code.
- No evidence bundle = no PR.
- One task = one worktree = one branch = one budget.
- Bots draft; humans send, post externally, and merge — until trust metrics say otherwise.
- Payments, if ever, are virtual cards with hard caps. Never a real card in a prompt or a file.
