# Build This in Claude: One Bot Per Project, Each With Its Own Memory
## A plan for Lauren Tan's persistent bot team — Chief of Staff, routines, connectors, and bots that launch cloud agents for you

**Source decoded from your Reel (Nov 18, 2026)**
Second Lauren Tan video — a Q&A, different from the talk in the first Reel you sent today. Poster: "Machine Learning & AI" (Nov 12, 2026).

Her line that sums up this one:

> "One bot in a conversation is a tool. Ten bots with their own memory are a company."

And the caption's claim: she gave her bots Gmail, Slack, and her credit card, and they launch **30+ agents before her coffee is ready**. The flow:

**One bot per project → its own memory → a routine watching a Slack channel → cloud agents spawned → review in Cursor**

> "You no longer open Cursor. Your bot opens it for you."

This plan builds *that* system in Claude. It is the companion to the plan from the first Reel (the PR factory: verification, Feature Map, Inner/Outer Loop). That plan was about trusting coding agents. This one is about **persistent bots that live between your coding sessions** — they watch, remember, triage, and start work before you sit down.

---

## 1. What she actually said — decoded from the transcript

| Question in the Q&A | Her answer, in plain words |
|---|---|
| **When is one persistent bot enough, and when does a coordinator + specialist team win — especially on memory and ownership?** | A bot is mainly a way to *organise your thoughts*. You can get very far with one bot. But once you have different projects, codebases, and task types, you naturally split into specialist bots. All her bots share one computer (own screens, same machine), but **each bot has its own memory and its own chat transcript** — and that specialised memory is exactly why the split helps. It's not proven that a team "outperforms" one bot; it's that a team is easier to think with. If you want one front door, add a **Chief of Staff** bot on top that routes to the specialists. |
| **How does Grok Bot fit a developer workflow? Isn't the Cursor Agents window better?** | She still uses Cursor for big engineering projects — its UI is better for tracking lots of subagents. Grok Bot cards get hard to track when you spawn many cloud agents. She uses Grok Bot as the **Outer Loop**: its strength is *connections* — email, calendar, Slack, X, even a credit card. She sets up **routines**: e.g. a bot watches a Slack channel for feedback, and each signal kicks off her Inner Loop — cloud agents running her PStack skills in "potato mode" to research/fix. If she wants depth, she opens that cloud agent's session inside Cursor. Over time, you open the IDE less. |
| **Can you switch models inside the bot?** | No — Grok Bot is Grok. When she needs a different model (e.g. heavy reasoning, or a manager bot), the bot **spawns a cloud agent on that model** instead. The bot stays the organiser; model choice happens at the agent it launches. |
| **PStack for everything, or only big things?** | Depends on the task (her answer is cut off in this clip) — consistent with her first talk: heavy skills for heavy work, light touch for small tasks. |

**Three ideas to steal, in order of importance:**
1. **Memory is per-bot, not global.** One giant memory for everything becomes mush. A project bot that only ever thinks about one codebase/domain remembers that domain deeply.
2. **The bot is the Outer Loop; the IDE is the Inner Loop.** The bot watches the world (Slack, email, calendar) and *starts* work. You review finished work. You stop being the trigger for everything.
3. **Routines are the product.** A bot with no routines is a chatbot you must remember to talk to. A bot with 3–4 good routines is an employee who starts before you do.

---

## 2. How this differs from the first plan — and how they fit together

| | Plan 1 (first Reel) | This plan (second Reel) |
|---|---|---|
| Core unit | A coding task → a PR | A persistent **bot** that owns a project |
| Lives where | Inside one repo's workflow | On one always-on host, across all your projects |
| Memory | Feature Map + codebase | Per-bot memory + transcript + project knowledge |
| Trigger | You / an issue | **Routines**: Slack watch, schedule, email, calendar |
| Human's job | Review PRs | Review a morning queue the bots prepared |
| Scale question | How many coding agents can you trust? | How many projects can one Chief of Staff route between? |

**Build order:** This bot layer sits *on top of* Plan 1. A bot that launches cloud agents into a repo with no verification skill and no paved path (Plan 1, Phases 1–2) just launches slop faster. Do Plan 1's foundation for at least your main repo first, or in parallel with Phase 1 below.

---

## 3. The Claude mapping

Claude has no "Grok Bot" product — you assemble the same thing from four Claude parts. That is actually an advantage: model choice, memory, and permissions are yours, not the platform's.

| Lauren / Grok Bot | Claude build | Notes |
|---|---|---|
| Persistent bot per project | **One Claude Agent SDK app per bot** (TypeScript `@anthropic-ai/claude-agent-sdk` / Python `claude-agent-sdk`), each with its own system prompt, its own session store, its own workspace folder | A bot = a folder + a config + a memory store + a set of routines. Not a chat window you keep open. |
| All bots share one computer | **One always-on host** — a small VM, a home server, or a Mac/PC that stays on. All bots run there as separate processes/containers | Same as hers: shared machine, shared tools, isolated memory and transcripts. |
| Each bot's own memory | **Three files/stores per bot** (§5): curated `MEMORY.md`, session transcripts (SDK session resume), and project knowledge (`CLAUDE.md` + Feature Map in the repo) | Never one shared memory file for all bots. Shared *read-only* company knowledge is a separate, fourth store (§5). |
| Chief of Staff pattern | **One router bot** — the only bot you normally talk to. Small/fast model for classification, flagship model when it must reason about priorities | It owns no project itself. It routes, summarises across bots, and prepares your morning brief. |
| Connections: Gmail, Slack, calendar, X, card | **MCP servers per bot, scoped** — Gmail MCP, Slack MCP, Google Calendar MCP, GitHub MCP, X via API/MCP where available | Each bot gets *only* the connectors its project needs, with the narrowest scopes (§7). A coding bot for Repo A does not get your Gmail just because the Chief of Staff has it. |
| Routines (watch Slack, kick off work) | **Three trigger types, all native:** 1) **Claude Routines / scheduled tasks** for time-based jobs, 2) **webhook listeners** in your bot host for Slack Events API / GitHub events, 3) **GitHub Actions** for repo events | Slack watching cannot be done by polling a chat — use Slack's Events API (Socket Mode is easiest for a home host) → webhook → bot. |
| Cloud agents the bot launches | **Claude Agent SDK `query()` workers** in git worktrees on the host, or **Claude Code cloud sessions / Routines** for jobs that should run off-host | This is where model switching happens — exactly her answer: the bot stays one model; each launched agent is configured per-task (flagship for planning/review, mid for coding, small/fast for research/triage). |
| Review in Cursor | **A review queue, not an IDE you open cold** (§8): draft PRs + agent session links + a one-page brief per finished job, delivered by the Chief of Staff | Solves the problem *she named*: tracking 30 spawned agents as loose cards is painful. A queue with states beats cards. |
| Credit card given to bots | **A virtual card per bot with a hard limit — never your real card** (§7) | Same capability (bots can pay for an API, a domain, a dataset), completely different risk. Virtual cards (e.g. a card-issuing service with per-card caps) can be frozen per-bot in one click. |

---

## 4. Target architecture

```
                        YOU
                         │  talk to one bot
                         ▼
                 CHIEF OF STAFF BOT                 ← flagship model when reasoning,
                 - routes by project                 small/fast for classification
                 - owns NO project
                 - makes your morning brief
                         │
        ┌────────────────┼────────────────┬──────────────────┐
        ▼                ▼                ▼                  ▼
   PROJECT BOT A    PROJECT BOT B    PROJECT BOT C      OPS / LIFE BOT
   (e.g. main       (e.g. side       (e.g. research /   (email, calendar,
    work repo)       project)         content)           scheduling)
   own MEMORY.md    own MEMORY.md    own MEMORY.md      own MEMORY.md
   own transcript   own transcript   own transcript     own transcript
   own routines     own routines     own routines       own routines
   own connectors   own connectors   own connectors     own connectors
        │                │                │                  │
        └────────────────┴───────┬────────┴──────────────────┘
                                 ▼
                    SHARED HOST (one machine, all bots)
                    - shared read-only COMPANY KNOWLEDGE store
                    - cloud-agent launcher (Agent SDK, worktrees)
                    - review queue + status board
                    - policy: budgets, concurrency, approvals, kill switch
                                 │
                                 ▼
                    CLOUD AGENTS (spawned per task, then gone)
                    plan → implement → verify → review  (Plan 1, Inner Loop)
                                 │
                                 ▼
                    REVIEW QUEUE → draft PRs, briefs, decisions
                    waiting for you — with your coffee
```

**Ownership rule (her "memory and ownership" question, made enforceable):**
- One bot owns one project/repo/domain. Two bots never edit the same repo at the same time — the launcher enforces a per-repo lock.
- A bot may *read* another bot's public summary (the Chief of Staff publishes these), but never writes into another bot's memory.
- If a task spans two projects, the Chief of Staff splits it into two owned tasks with a shared task ID — it does not create a shared-memory free-for-all.

---

## 5. Memory design — the heart of this build

Each bot has exactly three memory layers, plus one shared layer for the whole "company":

| Layer | What it is | Who writes it | Lifespan |
|---|---|---|---|
| **1. Transcript** | The bot's own chat/session history (Agent SDK session store) | Automatic | Rolling; summarised when long |
| **2. Curated memory** | `bots/<bot>/MEMORY.md` — decisions, preferences, people, project state, "what we tried and what happened" | The bot, at the end of each significant session, in a short memory-review routine; you can edit it any time | Permanent, human-readable, in git |
| **3. Project knowledge** | The repo's `CLAUDE.md`, Feature Map, skills (from Plan 1) | You + the gardener routine | Permanent, in the repo |
| **Shared: Company knowledge** | `company/` — your goals, contacts, standing rules, approval limits. **Read-only for project bots**; only the Chief of Staff (and you) can change it | You / Chief of Staff | Permanent |

**Memory hygiene rules (write these into every bot's system prompt):**
1. Save decisions and outcomes, not raw chatter. "We chose X because Y, on <date>" — not the whole conversation.
2. When a fact changes, *replace* the old line. Stale memory is worse than no memory.
3. A memory entry the bot is unsure about gets marked `(unconfirmed)` and may not be used as the basis for spending money or sending messages.
4. Nightly routine per bot: compress today's transcript into at most 10 lines of curated memory. If it can't be compressed, it probably wasn't important.

This mirrors how she described it: the transcript is unique to the bot, the memory is specialised to the bot — organisation of thought is the feature.

---

## 6. Bot roster — start with 3, not 10

Her "ten bots" is a grown state. Start here:

| Bot | Owns | Connectors (scoped) | First routines |
|---|---|---|---|
| **Chief of Staff** | Routing, your brief, priorities | Gmail (read), Calendar (read), Slack (read) | Morning brief (7:00), evening wrap (optional) |
| **Project Bot — your main repo** | One codebase end-to-end | GitHub, Slack (one feedback channel), Sentry if you use it | Slack feedback watch, nightly bug-triage sweep |
| **Ops / Life Bot** | Inbox, calendar, follow-ups | Gmail (read + draft, never auto-send), Calendar | Inbox triage twice a day, meeting-prep brief |

Add a new project bot only when a project has: its own repo/workspace, its own recurring signals (a channel, an inbox, a board), and at least one routine you can name. If you can't name the routine, you don't need the bot yet — a Chief of Staff conversation is enough. That is her "one bot is enough" answer, turned into a test.

**When does the team actually beat one bot?** When at least two of these are true: (a) two projects' contexts keep colliding in one transcript, (b) you scroll/search old chats to remind the bot of things, (c) different projects need different connectors or permissions, (d) one project's routines fire while you're deep in another. Until then, one bot + good curated memory wins — simpler and cheaper.

---

## 7. Connectors and the credit card — power with brakes

Per-bot permission matrix. Default is **read-only**; write access is earned per action type.

| Connector | Read | Draft / prepare | Act (send, post, pay) |
|---|---|---|---|
| Gmail | ✅ from day one | ✅ drafts, summaries | ❌ sending always needs your tap |
| Slack | ✅ its channels only | ✅ draft replies | ⚠️ posts to *internal bot* channels only; anything customer/public = your tap |
| Calendar | ✅ | ✅ proposed events | ⚠️ internal holds only; invites to others = your tap |
| GitHub | ✅ | ✅ draft PRs, issue comments drafted | ⚠️ draft PRs yes (Plan 1); merge = human |
| X / social | ✅ | ✅ drafts | ❌ your tap, always |
| **Payment card** | ✅ own transactions | ✅ prepares a purchase with reason + amount | ⚠️ **virtual card only**, per-bot cap (start: $50/transaction, $200/month), every charge reported in the morning brief, one-click freeze |

Why the card rule matters: in her setup the bots hold a real card. In yours, a virtual card per bot gives the same "bot can just handle it" feeling with a hard ceiling — a compromised or confused bot can waste at most its cap, never drain an account, and you can kill one bot's card without touching the others. Set the cap in the card product itself, not in a prompt — prompts are requests, limits must be enforced outside the model. The same principle as Plan 1's hooks: *enforcement lives outside the agent.*

---

## 8. Routines catalog — and the "30 agents before coffee" morning, honestly

### Core routines (build these first)
1. **Slack feedback watch** (per project bot) — Slack Events API → new message in the feedback channel → bot classifies (bug / feature / question / noise) → for a bug: open a task, spawn a cloud agent to *reproduce* it and attach evidence → result lands in the review queue. Nothing is fixed or replied to automatically at first.
2. **Morning launch (the coffee routine)** — 06:45 daily: Chief of Staff + project bots sweep overnight signals (Slack, email, Sentry, GitHub, calendar) → triage → spawn agents for the top items → 07:30 morning brief in your chat: what was found, what agents are running / finished, what needs your decision.
3. **Inbox triage** — twice daily: Ops bot clusters email into *act / reply-draft ready / FYI / ignore*, drafts replies for the middle group, sends nothing.
4. **Nightly memory compression** — per bot, §5 rule 4.
5. **Weekly gardener + memory audit** — from Plan 1: anti-pattern scan + flag stale/contradictory memory entries for your review.

### What "30 agents before coffee" should actually mean in your build
Not 30 coders writing code unsupervised. A realistic, trustworthy morning fan-out looks like:

- ~10 **triage/classify** agents (cheap, small/fast model, read-only)
- ~8 **research/reproduce** agents (read-only + sandbox: reproduce the bug, gather the logs, summarise the thread)
- ~6 **review** agents (review overnight PRs, check CI failures, summarise long threads/docs)
- ~4 **drafting** agents (reply drafts, issue specs, PR descriptions — nothing sent, nothing merged)
- ~2 **implementer** agents (only on pre-approved, low-risk task types, into draft PRs, with Plan 1 verification)

That's 30 agents, a full review queue by 07:30, and zero irreversible actions taken while you slept. Raise the implementer count only on Plan 1's trust metrics.

---

## 9. The review queue — fixing the problem she admitted

She said Grok Bot's spawned-agent cards get hard to track at volume. Don't repeat that in Claude. Your launcher writes every spawned agent into **one queue** (a simple Postgres/SQLite table + a status page, or even a Linear/GitHub project board at first):

`task · bot (owner) · project · source signal · state (queued/running/verifying/done/failed/needs-you) · cost · evidence link · PR/brief link`

The Chief of Staff's morning brief is generated *from this queue*, so the brief and the board can never disagree. You review from the queue, not from 30 separate chat windows — and you only open a full Claude Code session (your "Cursor moment") when a job deserves a deep look, exactly as she opens Cursor for the big ones.

---

## 10. Repository / host layout

```
bot-company/
├── company/                     # Shared, read-only for project bots
│   ├── GOALS.md  PEOPLE.md  RULES.md  APPROVALS.md
├── chief-of-staff/
│   ├── bot.yaml                 # model policy, connectors, routines
│   ├── PROMPT.md                # routing + briefing instructions
│   └── MEMORY.md
├── bots/
│   ├── project-main/
│   │   ├── bot.yaml
│   │   ├── PROMPT.md
│   │   ├── MEMORY.md
│   │   ├── routines/
│   │   │   ├── slack-feedback-watch.yaml
│   │   │   └── nightly-triage.yaml
│   │   └── skills/              # or a symlink to the repo's .claude/skills/
│   └── ops-life/
│       └── … (same shape)
├── platform/                    # The shared machinery (build once)
│   ├── launcher/                # spawns Agent SDK workers in worktrees, enforces locks/budgets
│   ├── queue/                   # task store + status page
│   ├── connectors/              # .mcp.json per bot, generated from bot.yaml
│   └── policy/                  # budgets, concurrency, approval gates, kill switch
└── .env  (host only, never in git — connector tokens, virtual-card API keys)
```

**`bot.yaml` — the whole bot in one file (shape)**
```yaml
name: project-main
owns: [repo: my-main-repo, slack: "#product-feedback"]
model: { default: mid, planning: flagship, triage: small-fast }
connectors: { github: read-write-draft-pr, slack: read, sentry: read }
memory: ./MEMORY.md
routines: [slack-feedback-watch, nightly-triage, morning-launch]
budget: { per_day_usd: 40, max_concurrent_agents: 5 }
approvals: { send_email: human, post_slack_external: human, pay: virtual-card-cap }
```

---

## 11. Phased build plan

### Phase 0 — Design the company on paper (Day 1)
- Name your first 3 bots (§6), what each owns, and one routine each. Write `company/` files (goals, rules, approval limits) — this is the bots' shared brain.
- Pick the host (always-on machine/VM) and confirm it can run Docker + the Agent SDK.
- **Exit gate:** roster + ownership + approval limits written down. No code yet.

### Phase 1 — One persistent bot, with memory (Days 2–3)
- Build the platform skeleton: one Agent SDK app, session store, `MEMORY.md` read/write, nightly compression routine.
- Ship it for the **Chief of Staff only**, with read-only Gmail + Calendar.
- Use it for real for 2 days: route your questions through it, correct its memory by hand.
- **Exit gate:** on day 3, it briefs you accurately on something from day 1 *without you re-explaining it* — memory works.

### Phase 2 — First project bot + repo foundation (Days 4–7)
- Add Project Bot for your main repo. In that repo, do Plan 1 Phases 1–2 (CLAUDE.md, paved path, verification skill, Feature Map) — the bot's launched agents depend on it.
- Connectors: GitHub (draft PRs), Slack (read, one channel).
- **Exit gate:** you can say "look at yesterday's feedback and prepare fixes" and get draft PRs with evidence, prepared by the bot, in the queue.

### Phase 3 — Routines: Slack watch + morning launch (Week 2)
- Slack Events API (Socket Mode) → feedback watch routine (§8.1).
- Morning launch at a fixed time + morning brief generated from the queue.
- Build the review queue status page (simple is fine).
- **Exit gate:** 5 straight weekdays where the brief is waiting for you, is accurate, and contains zero actions taken without approval.

### Phase 4 — Ops bot + email/calendar routines (Week 3)
- Ops/Life bot: inbox triage, meeting prep, draft replies (never auto-send).
- Chief of Staff learns to delegate across bots and merge their summaries into one brief.
- **Exit gate:** you talk to the Chief of Staff for cross-project questions and stop opening the individual bots directly — the front door works.

### Phase 5 — Payments, carefully (Week 4)
- Issue **virtual cards per bot** with low caps (§7). Wire transaction reporting into the morning brief.
- First allowed auto-pay category: one boring, predictable thing (e.g. an API bill, a domain renewal under the cap).
- **Exit gate:** one month of charges, every one expected, every one reported. Only then consider raising a cap.

### Phase 6 — Scale the company (Weeks 5+)
- Add project bots one at a time, using the §6 test (own workspace + own signals + a named routine).
- Raise morning fan-out toward her ~30 by adding *read-only* agent types first (triage, research, review) — implementers last, gated by Plan 1 trust metrics.
- Weekly: gardener routine + memory audit across all bots; you spend 30 minutes approving memory/rule changes — head-chef work.
- **Exit gate:** you start your day from the brief and the queue, and you open an IDE/Claude Code session mainly for deep work and final review — her end state.

**Weekend MVP (if you want the feeling fast):** Phases 0–1 + the morning brief only. One Chief of Staff bot with real memory and read-only email/calendar, briefing you at 7:00. That alone changes how the day starts, and everything else bolts onto it.

---

## 12. Costs and risks — the honest part

- **Always-on means always-spending.** Routines fire whether or not the signals were worth it. Per-bot daily budgets in `bot.yaml` are enforced by the launcher (count tokens/cost per run, hard-stop at cap) — not by asking the bot to be frugal.
- **Memory can go wrong quietly.** A bot that "remembers" a wrong fact will act on it confidently for weeks. The `(unconfirmed)` rule, the weekly memory audit, and keeping curated memory human-readable in git are your defences.
- **Connector scope creep is the main security risk.** Every bot starts read-only and narrow. Re-check scopes monthly. Tokens live in the host's `.env`/secret store, never in prompts, memory, or git.
- **The card is a cap, not a trust exercise.** §7's virtual-card rule is non-negotiable in this plan. Same for email: bots draft, humans send, until a specific, narrow send category has months of perfect drafts — and even then, keep the tap for anything external.
- **Don't build 10 bots.** Build 1, live with it, split only when §6's friction test says so. Her own answer was that one bot can go very far — the team is an organisational convenience that earns its complexity slowly.

---

## 13. What I need from you to start

1. **Your first project bot owns what?** Your main work repo, a side project, or should we start with just the Chief of Staff + Ops (email/calendar) and add code later?
2. **Where will the bots live?** A machine at home that's always on, a small cloud VM, or your work laptop (not always-on — routines would only run when it's awake)?
3. **Which Slack?** A workspace you can add an app to (needed for the feedback-watch routine), or should v1 use GitHub issues/email as the signal source instead?

With those, I can scaffold the actual `bot-company/` folder: the Chief of Staff bot (prompt, memory, morning-brief routine), the `bot.yaml` template, and the launcher skeleton — your Phase 0–1, ready to run.

---
*Plan prepared Nov 18, 2026. Source: Lauren Tan Q&A via the Facebook Reel you shared (read in full — transcript and caption, in Vietnamese; key quotes translated above). Companion to the Nov 18 plan from her first talk (`claude-agent-orchestrator-plan.md`). Claude-side mapping uses the Claude Agent SDK (TypeScript/Python) with per-bot sessions and MCP connectors, Claude Routines/scheduled tasks for time-based triggers, and Slack Events API for channel watching — checked against current Claude sources in the companion plan.*
