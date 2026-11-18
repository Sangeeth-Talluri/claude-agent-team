# Bot Company — your persistent Claude bot team

Built from the plan: `~/workspace/claude-orchestrator-plan/claude-persistent-bot-team-plan.md`
(Lauren Tan's system, rebuilt in Claude: one bot per project, each with its own memory,
a Chief of Staff front door, routines that start work before you do.)

## The team (3 starter bots)

| Bot | Folder | Owns | Talk to it for |
|---|---|---|---|
| Chief of Staff | `chief-of-staff/` | Routing, priorities, your brief. Owns NO project. | Everything — it is the front door |
| Project Bot — Main | `bots/project-main/` | ONE repo (set it in its `bot.yaml`) | Feedback, bugs, features for that repo |
| Ops / Life Bot | `bots/ops-life/` | Inbox, calendar, follow-ups | Email triage, meeting prep, drafts |

## How it works

- Each bot = `bot.yaml` (identity, connectors, budgets, approvals) + `PROMPT.md` (how it thinks)
  + `MEMORY.md` (its own curated memory — never shared, never merged with another bot's).
- Shared company knowledge lives in `company/` — read-only for project bots.
- Shared machinery lives in `platform/` — launcher, queue, connectors, policy.
  Bots never bypass the platform: budgets, repo locks, and approval gates are enforced there,
  in code — not in prompts.
- Every bot launches cloud agents only through `platform/launcher/` (one task = one worktree
  = one branch = one budget), and every launched job lands in `platform/queue/`.

## Standing safety shape (already set in the files)

- Email: bots read and draft. **Sending always needs your tap.**
- Slack: bots read their own channels. External/public posts need your tap.
- GitHub: bots open **draft PRs only**. Merge is human.
- Payments: **virtual card per bot only**, with a hard cap set in `company/APPROVALS.md`.
  Never a real card number, never in a prompt or a file in this repo.
- Secrets: only in the host's `.env` (see `.env.example`). Never in git, prompts, or memory.

## Start here

1. Read `NEXT_STEPS.md` — the short checklist of decisions only you can make
   (host, repo, Slack workspace).
2. Fill the `TODO(owner)` markers — search the folder for `TODO(owner)`.
3. Phase 1 from the plan = Chief of Staff only, read-only Gmail + Calendar,
   morning brief. Everything else bolts onto that.

## Status

Scaffold only — folders, configs, prompts, routines, and platform skeletons.
No bot is running yet, no connector is connected yet, nothing is scheduled yet.
