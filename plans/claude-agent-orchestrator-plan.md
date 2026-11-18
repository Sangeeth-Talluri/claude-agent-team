# Build the Same Agent System in Claude
## A plan to implement Lauren Tan's agent + orchestrator — in Claude Code and the Claude Agent SDK

**Source decoded from your Reel (Nov 18, 2026)**
Lauren Tan — engineer on Grok Bot at SpaceXAI, previously Cursor, Meta, Netflix, React Compiler core team. In one month she merged ~2,000–2,500 production pull requests with AI agents.

Her point was *not* "spawn more agents." It was:

> "Don't increase the number of agents until you can trust them. Running 100 agents is easy. Making 100 agents not create 100 piles of errors for humans to clean up is hard."

This plan rebuilds her exact system, piece by piece, using Claude's native tools — no Grok Bot, no Cursor Cloud Agents, no custom agent framework to invent from scratch.

---

## 1. What she actually built — decoded

| # | Her system | What it really does |
|---|---|---|
| 1 | **Trust ladder** | She started at 1–5 babysat agents. She only scaled after verification worked. Scale is earned, not configured. |
| 2 | **Verification skill — "ControlGlass"** | A CLI inside a skill folder, built on Chrome DevTools Protocol. The agent runs the app itself, takes performance traces and heap snapshots, and returns *evidence*, not claims. She stopped being the human who checks the work. |
| 3 | **Feature Map** | Materialised memory stored inside the skill: what every feature is, how a user reaches it, keyboard shortcuts, DOM elements to click. Without it, an agent given a vague Slack screenshot just guesses. Auto-maintained by an automation. |
| 4 | **Engineer skills — "PStack"** | Playbooks that teach agents to work like senior engineers: debugging, feature development, prototyping, performance, review. |
| 5 | **Dune — agent-friendly framework** | A locked-down codebase where the easy path *is* the right path, and bad patterns are categorically impossible. Strict boundaries (e.g. main-process code can never be imported into the renderer). Even comments were banned — agents were using comments to justify workarounds, then copying them everywhere. |
| 6 | **Codebase as memory** | Agents copy patterns they see. Good patterns spread. So do workarounds — "like a virus." Therefore: delete tech debt, keep one paved path, and appoint a **gardener** whose job is killing new anti-patterns early. |
| 7 | **Static analysis as hard gates** | Lint rules, compiler diagnostics, CI. Every time you correct an agent, the fix is not a note — it becomes a lint rule, a type, or an architecture change so the mistake cannot recur. |
| 8 | **Inner Loop / Outer Loop** | **Inner Loop:** agents write code, test, fix, open PRs. **Outer Loop:** Grok Bot + connectors (Slack, Linear, email, X, bug reports) find and organise the work. |
| 9 | **Chief of Staff agents** | 10+ orchestrator agents on top, continuously triaging incoming signals, classifying problems, and assigning tasks to the coding agents below. |
| 10 | **Routines / automations** | Subscriptions to Slack threads, Sentry alerts, etc., that automatically kick off a cloud agent to reproduce a bug and open a PR. |

**Her correction hierarchy (use this order every time an agent is wrong):**
1. Make it impossible in the architecture / data structures
2. Add a static-analysis / lint / CI rule
3. Add a rule, BugBot check, or skill
4. Only last: rely on a style guide / human review

---

## 2. The Claude mapping — same system, Claude parts

This is the core of the plan. Every piece she built has a direct Claude equivalent.

| Lauren / Grok Bot / Cursor | Claude equivalent | Notes |
|---|---|---|
| Coding agents (Inner Loop) | **Claude Code subagents** in `.claude/agents/*.md` for interactive work; **Claude Agent SDK `query()` workers** for headless/automated work | Each worker gets its own context window, its own tools, its own worktree. Only its final result returns to the orchestrator. |
| Grok Bot (Outer Loop) | **A small orchestrator service you own**, built on the Claude Agent SDK (TypeScript: `@anthropic-ai/claude-agent-sdk`, Python: `claude-agent-sdk`) | This is the piece you build. It is not a Claude Code chat session — it is a program that calls the SDK. |
| Chief of Staff agents (10+) | **Triage subagents** in the orchestrator — small/fast model class, structured output only | They never write code. They classify, de-duplicate, prioritise, enrich, and enqueue. |
| Connectors (Slack, Linear, email, X, Sentry) | **MCP servers** in `.mcp.json` — Slack, Linear, GitHub, Sentry, Datadog, Gmail MCP servers | MCP is Claude's standard connector protocol. Same servers work in Claude Code and in the Agent SDK. |
| Skills (ControlGlass, PStack) | **Claude Skills** — `.claude/skills/<name>/SKILL.md` + scripts/CLI in the same folder | Identical concept, identical folder pattern. A skill's CLI must be deterministic — agents must not re-write the script every session. |
| Feature Map | `.claude/skills/feature-map/` — `FEATURE_MAP.md` + a generator script + a scheduled refresh | See §5. |
| Rules / CLAUDE context | **`CLAUDE.md`** at repo root (always loaded) + `.claude/rules/` for path-specific rules | Knowledge goes here. Keep `CLAUDE.md` short (<200 lines) — put procedures in skills, not here. |
| Lint / CI / BugBot enforcement | **Hooks** in `.claude/settings.json` (`PreToolUse`, `PostToolUse`, `Stop`) + your normal CI | Hooks are guarantees, not requests. A hook can block a tool call, force formatting, run tests before stopping, and reject a PR with no evidence bundle. |
| Cloud Agents | **Git worktree per task + Claude Routines / scheduled tasks + GitHub Actions (`anthropics/claude-code-action`)** for cloud runs | Start with Routines + GitHub Actions. Graduate to your own SDK service when you need a real queue, budgets, and state. |
| Agent Teams (parallel peers) | **Claude Code Agent Teams** (experimental, shared task list, peer messaging) — optional, later | Useful for parallel review/debate. Costs roughly 7× a normal session. Do not start here. |
| Dune framework | **Your "Paved Path Kit"** (§6) — strict types, architecture-boundary lint, scaffolding CLI | You do not need a new framework. You need conventions + enforcement for *your* stack. |

**Rule of thumb from Claude practice, and it matches Lauren exactly:**
Knowledge → `CLAUDE.md` / skills. Enforcement → hooks / lint / CI. Isolation → subagents. Outside systems → MCP.

---

## 3. Target architecture

```
                 OUTER LOOP  (find and organise work)
  Slack ─┐
  Linear ├─ MCP / webhooks ─►  INTAKE  ─►  CHIEF OF STAFF TRIAGE AGENTS
  GitHub ┤                                    (small/fast model, JSON out)
  Sentry ┤                                         │
  Email ─┘                                         ▼
                                            TASK QUEUE / STATE
                                     (Postgres first; Temporal later if needed)
                                     task = { id, source, title, evidence,
                                              feature_map_refs, risk, budget }
                                                   │
                                                   ▼
                 INNER LOOP  (do and prove the work)
                                            ORCHESTRATOR SERVICE
                                     (Claude Agent SDK — you own this code)
                                      ┌────────────┼────────────┐
                                      ▼            ▼            ▼
                                  PLANNER      IMPLEMENTER   IMPLEMENTER
                                  (flagship)   (mid model)   (mid model)
                                                   │   each in its own
                                                   │   git worktree,
                                                   │   branch claude/<id>
                                                   ▼
                                  VERIFIER  (separate agent, never the author)
                                  runs the verification skill, collects
                                  evidence bundle: tests, traces, screenshots,
                                  logs, perf numbers — PASS / FAIL + reasons
                                                   │
                                                   ▼
                                  REVIEWER  (flagship, reads diff + evidence only)
                                                   │
                                          ┌────────┴────────┐
                                          ▼                 ▼
                                    DRAFT PR opened     FAIL → back to
                                    (never auto-merge   implementer, max
                                     at Levels 1–2)     2 loops, then human

                 GARDENER  (weekly, separate routine)
  Scans merged agent PRs for copied anti-patterns → opens cleanup PRs →
  proposes a new lint rule / hook for every repeated human correction.
```

**Non-negotiable design rules**
1. **Verifier is never the implementer.** Same-agent self-grading is how 100 agents produce 100 piles of slop.
2. **No evidence bundle = no PR.** Evidence is files, not prose: test output, trace, screenshot, log excerpt, perf before/after.
3. **Draft PRs only at first.** Auto-merge is a Level 3 privilege, earned by metrics (§8), and never for auth, payments, migrations, or infra deletes.
4. **One task = one worktree = one branch = one budget.** Max turns, max cost, max wall-clock per task, enforced by the orchestrator, not by a prompt.
5. **Every human correction enters the Correction Log** and must graduate to a rule, lint, type, test, or skill within a week — or it will be re-taught forever.

---

## 4. Repository layout (the control plane)

```
your-repo/
├── CLAUDE.md                        # Always-true facts: stack, commands, paved path, banned patterns
├── .mcp.json                        # Shared MCP servers: github, linear, slack, sentry
├── .claude/
│   ├── settings.json                # Hooks: format, lint, test gate, evidence gate, secret block
│   ├── agents/
│   │   ├── planner.md               # Flagship model, read + plan tools only
│   │   ├── implementer.md           # Mid model, full code tools, worktree only
│   │   ├── verifier.md              # Read + verify CLI only, cannot edit source
│   │   ├── reviewer.md              # Flagship, diff + evidence only, no edit
│   │   ├── triage.md                # Small/fast, structured JSON output only
│   │   └── gardener.md              # Weekly anti-pattern scan
│   ├── skills/
│   │   ├── verify/                  # ← your ControlGlass
│   │   │   ├── SKILL.md
│   │   │   └── scripts/verify.mjs   # Deterministic CLI: run app, trace, screenshot, report
│   │   ├── feature-map/
│   │   │   ├── SKILL.md
│   │   │   ├── FEATURE_MAP.md       # Generated + hand-curated
│   │   │   └── scripts/generate.mjs
│   │   ├── debug/SKILL.md           # ┐
│   │   ├── feature-dev/SKILL.md     # │  ← your PStack
│   │   ├── perf/SKILL.md            # │
│   │   └── code-review/SKILL.md     # ┘
│   └── rules/
│       └── correction-log.md        # Every human correction, dated, with its graduation status
└── orchestrator/                    # The Outer Loop service (Phase 5+)
    ├── src/
    │   ├── intake/                  # Webhook receivers: GitHub, Slack, Sentry, Linear
    │   ├── triage.ts                # Chief of Staff agents
    │   ├── queue.ts                 # Task store (Postgres)
    │   ├── run-task.ts              # Spawns an SDK worker in a worktree
    │   └── policy.ts                # Budgets, concurrency, risk gates, kill switch
    └── package.json                 # @anthropic-ai/claude-agent-sdk
```

---

## 5. The two skills that create trust

### 5a. Verification skill (your ControlGlass)

Build this *before* you build the orchestrator. It is the whole game.

**Web / Electron / React track (Lauren's case):**
- CLI wraps Playwright + Chrome DevTools Protocol.
- Commands: `verify run <route>`, `verify trace <route>` (perf trace + hotspots), `verify heap`, `verify screenshot <state>`, `verify a11y`.
- Output is always a folder: `evidence/<task-id>/` with `report.json`, screenshots, trace file, console errors, and a one-line verdict per check.
- The skill teaches the agent *how to interpret* a trace, not just how to take one.

**Backend / API / SRE / database track (your day-job case):**
- CLI wraps your test runner, a staging/smoke client, and observability queries.
- Commands: `verify tests <scope>`, `verify smoke <service>`, `verify query-plan <sql-file>` (EXPLAIN, no prod writes), `verify slo <service> <window>` (Datadog/Prometheus via MCP or API).
- Same rule: output is an evidence folder with numbers, not an agent saying "it works."

### 5b. Feature Map

One entry per user-visible feature (web) or per service/endpoint/job (backend):

```markdown
## Checkout — Submit payment
- Reach it: /cart → "Checkout" button [data-testid=checkout-btn], shortcut: none
- Does: validates cart, calls POST /api/payments, shows confirmation or inline error
- States: empty cart (button disabled), card declined (error banner, cart preserved)
- Owned by: src/features/checkout/
- Verify with: verify run /checkout ; verify screenshot checkout-declined
```

A generator script builds the first draft from routes/components/tests; a weekly Routine refreshes it and flags drift in a PR. Curate it by hand once — agents are only as good as this map when the intake is a vague screenshot or a one-line Slack message.

---

## 6. The Paved Path Kit (your Dune, without writing a framework)

Pick the enforcement that fits your stack; the principle is identical:

1. **One blessed way per common job** — data fetching, state, forms, API handler, DB access, background job — documented in `CLAUDE.md`, exemplified by *one* gold-standard module agents will copy.
2. **Architecture boundaries in lint** — e.g. ESLint `no-restricted-imports` / dependency-cruiser (TS), import-linter (Python), ArchUnit (Java). Forbidden import = build failure, not a review comment.
3. **Scaffolding CLI** — `npm run new:feature <name>` (or your equivalent) generates the correct folder, types, test, and wiring. The shortcut becomes the right path.
4. **Ban workaround comments** — a lint/custom rule flags `// workaround`, `// temporary`, `// TODO fix later` in agent PRs. If a workaround is truly needed, it needs a linked issue ID in the comment.
5. **Delete, don't decorate** — schedule the gardener agent weekly; budget human time to delete the top anti-patterns it finds. A codebase agents copy must be a codebase worth copying.

---

## 7. Agent roster

| Agent | Model class | Tools | Can edit code? | Output |
|---|---|---|---|---|
| Triage (Chief of Staff) | Small / fast | MCP read-only (Slack, Linear, GitHub, Sentry) | No | JSON task or "ignore / duplicate / needs-human" |
| Planner | Flagship | Read, search, Feature Map skill | No | Plan + acceptance checks + risk level |
| Implementer | Mid (best coding value) | Full code tools, in worktree only | Yes, its branch only | Code + self-test log |
| Verifier | Mid | Verify skill CLI, test runner, read-only source | No | Evidence bundle + PASS/FAIL per acceptance check |
| Reviewer | Flagship | Diff + evidence bundle only | No | Approve / request changes with numbered findings |
| Gardener | Mid | Read, search, lint tooling | Cleanup PRs only | Anti-pattern report + proposed rules |

Start with **one of each**. Lauren's "10+ Chief of Staff" is a *scaled* state, not a starting state.

---

## 8. Phased build plan

### Phase 0 — Pick the pilot (Days 1–2)
- Choose **one** repo, ideally: active PR flow, tests that run in CI, one owner (you).
- Baseline metrics: PRs/week, % PRs needing human rework, review minutes/PR, regressions/week.
- Decide the track: **Web** (Playwright/CDP verification) or **Backend/SRE** (tests + observability verification). Everything else is the same.
- **Exit gate:** repo named, baseline written down.

### Phase 1 — Foundation: make the codebase copy-worthy (Week 1)
- Write `CLAUDE.md` (stack, commands, paved path, banned patterns). Run `/init` in Claude Code for a draft, then cut it hard.
- Turn on strict lint/types in CI if not already on. Add architecture-boundary rules for the two worst known violations.
- Start `correction-log.md`. Backfill your last 10 agent corrections as rules.
- Add hooks in `.claude/settings.json`: format on edit, lint on stop, block edits outside the worktree, block secret-looking strings.
- **Exit gate:** a fresh Claude Code session, given only the repo, follows the paved path on a sample task with zero human corrections.

### Phase 2 — Verification skill + Feature Map (Weeks 1–2)
- Build `verify` CLI (5 commands max to start) + `SKILL.md` that teaches interpretation.
- Generate Feature Map v1, hand-curate the top 20 features/services.
- Test the pair the Lauren way: feed the agent a vague bug ("checkout feels slow" + a screenshot). It must locate the feature from the map, reproduce it with the CLI, and return evidence — unprompted.
- **Exit gate:** agent self-verifies 5/5 sample tasks with evidence a human accepts without re-running anything.

### Phase 3 — Engineer skills / your PStack (Week 2)
- Write 4 skills from *your own* workflows: `debug`, `feature-dev`, `perf`, `code-review`. Each: steps, what evidence to collect, what "done" means, what to never do.
- Encode your senior-engineer judgement here — this is where your experience becomes the team's leverage.
- **Exit gate:** two different tasks run with only skills (no live coaching) match your quality bar.

### Phase 4 — Inner Loop in Claude Code (Week 3)
- Create the 6 agent definitions in `.claude/agents/`.
- Worktree runner: one script that creates a worktree + branch per task, runs implementer → verifier → reviewer, opens a **draft** PR with the evidence bundle linked.
- Human merges. Always. Measure rework rate.
- **Exit gate:** 10 consecutive agent PRs, ≥70% merged with no substantive human rewrite.

### Phase 5 — Outer Loop v1: one intake only (Week 4)
- Pick **one** source: GitHub Issues (simplest) or Slack (closest to Lauren). Not both.
- Build the orchestrator skeleton on the Agent SDK: webhook → triage agent (JSON) → Postgres task queue → run-task (Phase 4 runner, headless) → draft PR → post the PR + evidence summary back to the source thread.
- Add policy.ts on day one: max 3 concurrent tasks, per-task cost/turn caps, risk gate (auth/payments/migrations/infra = human must approve *before* a worker starts), global kill switch.
- Use Claude Routines / GitHub Actions for scheduled jobs (nightly triage sweep, weekly Feature Map refresh) instead of building your own scheduler.
- **Exit gate:** one real Slack/issue signal travels intake → PR → reply with no human touching the middle, and the human only reviews the PR.

### Phase 6 — Orchestrator hardening (Weeks 5–6)
- State machine per task (queued → planning → implementing → verifying → reviewing → pr-open / failed / needs-human), persisted, resumable after a crash.
- Retry policy: verifier FAIL loops back max 2× with the failure evidence attached; third failure escalates to a human with a summary — never an infinite agent loop.
- Dashboard (even a simple page): tasks by state, cost per merged PR, rework rate, evidence completeness, top failure causes.
- De-duplication and grouping in triage (10 Slack complaints about one bug = 1 task).
- **Exit gate:** system runs a full week unattended at 3–5 concurrency with zero runaway tasks and zero PRs lacking evidence.

### Phase 7 — Scale, carefully (Weeks 7–8+)
- Add intakes one at a time: Sentry alerts (auto-reproduce + PR is the highest-value one), Linear, email.
- Turn on the Gardener weekly routine.
- Raise concurrency only when the trust metrics in §9 stay green for 2 straight weeks.
- Optional: experiment with Agent Teams for parallel review of large PRs.
- **Exit gate:** you are reviewing outcomes and rules, not diffs line-by-line — the Michelin-kitchen shift Lauren describes.

**Solo fast track (if this is a personal project, not a team):** Phases 0–4 only, skip the service — Claude Code + subagents + Routines *is* your orchestrator. Add Phase 5 only when you feel the pain of manually feeding it tasks. That is a working system in ~7 focused days.

---

## 9. Trust metrics — when you are allowed to scale

Scale concurrency only on evidence, exactly as she did:

| Metric | Level 1 → 2 (5–20 agents) | Level 2 → 3 (20–100 agents) |
|---|---|---|
| PRs merged with no substantive human rewrite | ≥70% over last 20 PRs | ≥85% over last 50 PRs |
| PRs with complete evidence bundle | 100% | 100% |
| Regressions traced to agent PRs | ≤1 in last 20 | ≤1 in last 50 |
| Human review time per PR | Falling for 2 weeks | ≤15 min average |
| Repeated correction (same mistake twice) | Logged, rule proposed | Zero repeats without a rule shipped |

If a metric goes red, drop a level. That discipline — not the model — is what got her to 2,000 PRs.

---

## 10. Starter code skeletons

**Subagent definition — `.claude/agents/verifier.md`**
```markdown
---
name: verifier
description: Independently verifies a task in its worktree. Never edits source code.
tools: Read, Bash, Skill
---
You are the verifier. You did not write this code and you must not fix it.
1. Read the task's acceptance checks and the Feature Map entries named in the task.
2. Run the verify skill for each check. Save all output to evidence/<task-id>/.
3. Return PASS or FAIL per check, with the evidence file that proves it.
A claim without an evidence file is a FAIL.
```

**Orchestrator worker — TypeScript, Agent SDK (shape, not full code)**
```ts
import { query } from "@anthropic-ai/claude-agent-sdk";

// One call = one task = one isolated worktree
for await (const msg of query({
  prompt: taskPrompt(task),               // title, source evidence, feature-map refs, acceptance checks
  options: {
    cwd: worktreePath(task.id),           // git worktree on branch claude/<task-id>
    allowedTools: ["Read", "Edit", "Bash", "Skill", "mcp__github__*"],
    maxTurns: 60,                         // hard stop — policy, not hope
    agents: { verifier: verifierDef, reviewer: reviewerDef },
  },
})) { /* stream to task log; persist state transitions */ }
```

**Hook that enforces the evidence gate — `.claude/settings.json` (shape)**
```json
{ "hooks": { "Stop": [ { "hooks": [ {
  "type": "command",
  "command": "test -f evidence/$TASK_ID/report.json || { echo 'No evidence bundle — run the verify skill first.'; exit 2; }"
} ] } ] } }
```

**Task schema (queue row / JSON)**
```json
{ "id": "t_123", "source": "sentry", "title": "Checkout p95 latency regression",
  "evidence_in": ["sentry link", "trace id"], "feature_map_refs": ["Checkout — Submit payment"],
  "acceptance": ["p95 < 800ms on verify trace", "tests pass", "no console errors"],
  "risk": "medium", "budget": { "max_turns": 60, "max_usd": 15 }, "state": "queued" }
```

---

## 11. Costs, risks, and honest warnings

- **Token cost multiplies.** Subagents keep the main context clean, but parallel agents and agent teams can cost ~7–10× a single session. Budgets in policy.ts are not optional.
- **The model is not the bottleneck — your codebase is.** If Phase 1–2 are skipped, a better model just produces slop faster. Her talk is 80% environment, 20% agents.
- **Secrets and permissions:** MCP servers get read-only keys first. Workers run in worktrees with no production credentials. Headless/cloud runs need an explicit allowlist of tools and network destinations.
- **Auto-merge is the last thing you earn**, and some categories (auth, money, migrations, deletes) should stay human-merged permanently.
- **Gardener time is real work.** Budget ~half a day a week of human time at first to delete anti-patterns and ship the rules the correction log produces. That *is* the job now — head chef, not line cook.

---

## 12. What I need from you to start Phase 0–1

1. **Which repo?** A work repo, a personal project, or a fresh demo repo to learn on?
2. **Which track?** Web app (Playwright/CDP verification) or backend / SRE / database (tests + observability verification)?
3. **Solo or team?** Solo = Phases 0–4 fast track. Team/production = full plan including the orchestrator service.

With those three answers I can scaffold the actual control plane for that repo: `CLAUDE.md`, the six agent files, the verify skill skeleton, the hooks, and the correction log — ready for your first supervised task.

---
*Plan prepared Nov 18, 2026. Source: Lauren Tan talk via the Facebook Reel you shared (decoded and read in full, including the transcript and caption). Claude-side facts checked Nov 18, 2026 against current Claude Code / Agent SDK sources: Agent SDK in TypeScript and Python with isolated subagents and MCP support; Claude Code skills in `.claude/skills/`, subagents in `.claude/agents/`, hooks in `.claude/settings.json`; cloud scheduled tasks (formerly Routines) and the Claude Code GitHub Action for headless runs; Agent Teams experimental.*
