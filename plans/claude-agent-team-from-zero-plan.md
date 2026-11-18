# Plan 3: Build an AI Engineering Team From Zero in Claude
## Loops and graphs, spec-first work, skill evals, a PM agent — and auto-merge you have to earn

**This is the third plan in this folder, and it builds on the first two. It does not repeat them.**

- **Plan 1** — `claude-agent-orchestrator-plan.md` — the PR factory: verification skill, Feature Map, paved-path codebase, Inner Loop / Outer Loop, draft PRs only.
- **Plan 2** — `claude-persistent-bot-team-plan.md` — persistent bots: one bot per project, its own memory, a Chief of Staff bot, routines, connectors, a review queue.
- **Plan 3 (this file)** — the team at full strength: how work flows through **loops and graphs** instead of a single chat, how **specs** come before code, how **skills stay good over time (evals)**, what a **PM agent** does, how each agent gets its **own sandbox**, and how a team earns the right to **auto-merge ~20 PRs overnight** — plus how non-engineers can ship code safely inside all of this.

**Source decoded from your Reel (Nov 18, 2026)**
Third Lauren Tan video — a longer tutorial / talk, posted Sep 11, 2026 by Phan Đông Giang. The caption (Vietnamese) makes the claim plainly:

> "99% of GrokBot users use only 1% of its true power. They run one agent, with no loop and no graph."

She now runs 20+ agents as a standing team: a Chief of Staff agent, a PM agent, and 20+ worker agents. Each bot has its own virtual machine, logs itself into Slack and GitHub, runs browser tests, and sends screenshots to prove its results. Overnight the team finishes and merges about 20 pull requests into main. Her stated secret: **not the model — the harness, the specs, and the verification system.**

---

## 1. What she actually said — decoded

This talk is the "from zero to trusted team" journey, told in order. The parts that are *new* compared with the first two videos:

### 1a. AI is a pair, not a replacement for your thinking
She starts here on purpose. The best use of an agent is like pair programming — it must not replace the act of thinking. That is why her workflow begins with a **spec**: the agent writes the spec first, the human reviews the *spec*, and only then does code happen. Reviewing a one-page spec is cheap. Reviewing 800 lines of code written from a wrong idea is not.

### 1b. The trust curve is a management problem
If a manager does not trust their team, they micromanage — they watch every output and check every line. Low trust with agents looks the same: you sit in the loop, you watch everything, you cannot run things in parallel, because you cannot scale past an agent you do not trust. She says she has now climbed the curve far enough that her agents **auto-merge PRs**: she woke up to ~20 PRs already landed on main, reviewed them *after* landing, and they were good. She is clear there is **no shortcut** up this curve, and she warns people not to jump from a few local agents straight to hundreds of cloud agents — it just wastes a lot of tokens.

### 1c. Verification closes the loop
Without a verification skill, *you* are the verifier: the agent writes code, you run the app, you copy back screenshots and console errors, one slow round at a time. You are the bottleneck and nothing can run in parallel. Her ControlGlass skill (Plan 1) lets the agent run the app itself — browser, simulator, CLI, whatever the user touches — and check its own work. That closed loop proves code is at least *correct* (not yet that it is *good*), and it is the first step of trust.

Her example agent, **Benny**, shows where this leads: Benny takes every incoming bug report, goes off in the cloud **on its own computer**, runs the app with the same control skills, and tries to reproduce the bug. In one case Benny found the bug was *already fixed on main* — so the only action needed was to ship a new build. That one automatic check saved about an hour of a human asking "is this fixed or not?" — and it helps the whole team, not just her.

### 1d. Skills are built from watching agents fail
Her plugin PStack was not designed up front. It grew one skill at a time, each one from a failure she *watched happen*. Example: agents would confidently name a cause — "the smoking gun" — for the hundredth time, without reading the code that was actually involved. So she built a skill that forces the agent to stop guessing: read the real code, search properly, use subagents, gather evidence first. Her method is active, not passive: open the tool calls, read the thinking, note exactly where the agent goes wrong — like a senior engineer watching a junior pair-program — then write the skill that fixes that one failure. She compares the new job to a head chef: you design the kitchen, the stations, and the tasks; you no longer cook every dish.

### 1e. Skills are maintained with evals — "unit tests for agents"
This is the biggest new idea in this video. An **eval** tests a skill the way a unit test tests code:

- A coordinator agent first writes a **rubric** — what good behaviour for this skill looks like, scored.
- It spawns many subagents, each in its **own directory**, running tasks with the skill.
- The directories are named so the subagent **cannot tell it is being evaluated** — because agents that know they are being tested change their behaviour.
- A **judge agent on a different model** can cross-check the scores, so the model that ran the work is not grading itself with its own bias.
- You can **hill-climb**: loop the eval, fix the skill, re-run, and keep looping until the score reaches the target (her example: keep going until everything is 10/10). She built and improved her control/verification skill itself this way.
- Run the same eval **across the models you actually use**. A skill that works on one model may fail on another.
- She is honest that maintaining skills is *hard*: it takes taste and close observation, mostly at the start.

### 1f. Start local, then go to the cloud
For building a verification system, start **local**, where you can watch the agent drive the app and see every step. Move to cloud agents only after local trust exists. Cloud agents are where the payoff multiplies — one good verification skill lifts the whole team, because every automation (like Benny) uses it too.

### 1g. The case for rewriting — and the greenfield warning
A new point in this talk: brownfield codebases with big-company guardrails (strict frameworks, conventions, restricted credentials — built so the least experienced engineer cannot cause havoc) are actually a *good* place for agents. The dangerous case is a fresh, vibe-coded prototype with **no guardrails at all**: agents solve each task by the most convenient shortcut, the codebase spirals, and soon nobody — human or agent — understands it. Her GrokBot app began exactly that way, and she invested heavily (she counts 600+ PRs in one refactor) to rebuild it on her strict Dune architecture (Plan 1). After that investment she says she mostly **no longer reads the code** — not because she is careless, but because the constraints and CI do the checking. Small extra facts: she asks agents to split work into **small, atomic PRs** (a clean git history is context, and small PRs are easy to revert), with no hard size cap; PRs she showed ranged from ~50 to ~1,000 lines.

### 1h. The harness makes non-engineers safe contributors
Because Dune is so strict, designers, PMs, and go-to-market staff now ship real features through GrokBot's friendly, chat-like (iMessage-style) interface — one agent per account for GTM staff, and a **PM agent that summarises what a person did overnight** so the PM always knows the state of work. When a PM ships a bug fix and asks her to review, she says it is usually perfect and just gets her stamp. The strictness that annoys human engineers is exactly what makes this safe: agents absorb the annoyance, and the guardrails catch what a non-expert would miss.

### 1i. The honest cost note
She works at an AI lab with effectively unlimited tokens, and she says so. Her answer on cost is an ROI argument, not a denial: setting this up costs a lot of tokens up front (refactors, rules, evals), but it is a one-time investment that lets a small team stay small and lets even mid-tier models do excellent work, because the environment does so much of the checking. Budget for that shape of cost — heavy at the start, cheaper per result later — not for "free."

---

## 2. What's new vs Plans 1–2

| Topic | Plan 1 / Plan 2 position | What this Reel adds (Plan 3) |
|---|---|---|
| Work shape | One agent does a task; bots route tasks (Plans 1–2) | Work is a **graph**: nodes, branches, fan-out/fan-in, and loops that repeat until a check passes. A single agent with no loop and no graph is the 1% version. |
| Where thinking happens | Plan first, then code (Plan 1 planner agent) | **Spec-first as a formal gate:** a written spec document is a deliverable, a human approves it, and no code starts before approval. |
| Skills | Write skills from your own workflows (Plan 1); memory hygiene (Plan 2) | **Skill evals and maintenance:** every skill gets tests, a rubric, blind trial runs, a cross-model judge, and a hill-climb loop. Skills are *kept* good, not just written. |
| Team roster | Chief of Staff + project bots (Plan 2) | A dedicated **PM agent**: owns the board, the priorities, the status, and the per-person overnight summary. |
| Isolation | One git worktree per task (Plan 1) | **One sandbox per bot/agent:** worktree *plus* a container or VM, with its own logins, so an agent can drive a browser/app and log into Slack/GitHub without touching your machine or another agent's state. |
| Merging | Draft PRs only; human merges (Plan 1, all levels at first) | **Auto-merge as the top of a trust ladder:** ~20 PRs merged overnight, reviewed after landing — earned by metrics, with hard exclusions. |
| Codebase strategy | Make the existing codebase copy-worthy (Plan 1) | The **rewrite decision**: a guardrail-free greenfield codebase may be worth rebuilding on a strict harness early, before agent shortcuts make it unfixable. |
| Who ships code | Engineers, reviewed by engineers | **Non-engineers ship** through a friendly chat front door, protected by the harness — with a different review path, not a weaker one. |
| Cost model | Per-task budgets and caps (Plans 1–2) | The **investment model:** expect a large up-front token spend on harness/evals/refactor; measure ROI per merged result over months, not per day. |

Everything in Plans 1–2 still stands. Plan 3 assumes Plan 1's verification skill and paved path exist for the pilot repo, and Plan 2's queue exists — the PM agent and the auto-merge policy both run on top of that queue.

---

## 3. The Claude mapping — new pieces only

| New piece (this Reel) | Claude build |
|---|---|
| Loop + graph orchestration | **Deterministic workflow scripts on the Claude Agent SDK.** The graph is *code you write*, not a prompt you hope the model follows: a TypeScript/Python script that calls `query()` for each node, passes typed results between nodes, branches on checks, fans out to parallel workers, fans in to a synthesiser, and loops a node until its exit check passes or a max-iteration cap hits. The model decides *inside* a node; the script decides the *shape* of the work. |
| Spec-first gate | **Specs as files:** `specs/<task-id>.md` in the repo (or in the queue), written by a spec agent, reviewed by a human in a pull request or an approval step in the workflow script. The implementer node's input is the *approved* spec file — the script will not start it without an `approved: true` marker and the approver's name. |
| Skill evals | **An `evals/` folder per skill** (§6): test prompts, fixture directories, a rubric file, and a runner script that spawns blind trial agents, scores them, and reports. Runs locally first, in CI or a Claude Routine when a skill changes. |
| PM agent | **An Agent SDK agent on top of Plan 2's queue** (§7): read/write on the task store, read-only on code. It never writes code. |
| Per-bot VM / own computer | **Container per bot, worktree per task** (§8): Docker (or a lightweight VM where a full desktop/browser is needed) per bot from Plan 2; inside it, one git worktree + one Claude session per task. Credentials are per-bot, injected as secrets into its container only. |
| Benny (auto bug reproduction) | A workflow graph, not a single agent: intake node → classify node → **reproduce node in a sandbox with the verification skill** → report node ("reproduced / already fixed on main / cannot reproduce + evidence"). This is the best first graph to build — high value, read-only, no merge rights. |
| Auto-merge | **A policy module in the orchestrator + GitHub branch rules** (§9): the workflow may merge only when every gate in the ladder for that repo/category is green. Enforced by GitHub required checks and a merge-bot identity with narrow rights — never by a prompt instruction to an agent. |
| Friendly front door for non-engineers | The Plan 2 Chief of Staff chat is the front door. Non-engineers talk to it (or file a spec request); they never touch a worktree, a terminal, or a credential. Their work travels the same spec → graph → verification path as everyone else's (§10). |
| Model matrix for evals | Run each eval on the **models you actually deploy** (flagship / mid / small-fast tiers in your Claude plan). Record scores per model in the eval report; a skill must pass on every model that will use it in production. |

---

## 4. Target architecture — the loop/graph layer

Plans 1–2 gave you agents and bots. This layer sits between them: every non-trivial job runs as a **workflow graph** owned by the orchestrator.

```
        SIGNAL (Slack / issue / Sentry / a person's request)
                          │
                          ▼
                   ┌─────────────┐        human gate
                   │  SPEC node  │──────►  spec file ──► YOU approve
                   │ (flagship)  │        (no approval = no code)
                   └──────┬──────┘
                          ▼ approved spec
                   ┌─────────────┐
                   │  PLAN node  │  splits spec into small atomic tasks
                   └──────┬──────┘
                          ▼
              ┌─── FAN-OUT (parallel, one sandbox each) ───┐
              ▼                       ▼                     ▼
        IMPLEMENT node          IMPLEMENT node        IMPLEMENT node
              │                       │                     │
              ▼                       ▼                     ▼
        VERIFY node  ◄── FAIL ──┐  VERIFY node          VERIFY node
              │                 │        │                     │
              └── loop back ────┘        │                     │
                  (max 2 loops,          │                     │
                   then escalate)        │                     │
                          └─── FAN-IN ───┴─────────────────────┘
                                         ▼
                                  REVIEW node (flagship,
                                  diff + evidence only)
                                         │
                          ┌──────────────┴──────────────┐
                          ▼                             ▼
                   MERGE GATE (§9)                 NEEDS HUMAN
                   auto-merge if this              queue + PM agent
                   category has earned it,         summary of why
                   else draft PR for you
                                         │
                                         ▼
                   PM AGENT updates board, writes the
                   overnight summary per person/project
```

**Graph design rules**
1. **The graph is a script, not a conversation.** If a step must always happen (verify, review, gate), it is a node in the script. A node cannot be skipped because an agent "felt done."
2. **Loops always have a cap and an exit test.** Verify-fail loops back at most twice, with the failure evidence attached to the retry. Third failure = escalate to a human with a summary. No open-ended "keep trying."
3. **Fan-out is for independent work only.** Tasks that share files or a design decision go through one implementer, or through a plan node that assigns non-overlapping file ownership first.
4. **Every node writes a typed result** (JSON or a named file) — never "the next agent reads the chat and figures it out." Typed hand-offs are what make a graph debuggable and an eval possible.
5. **Cheap nodes first.** Classify, dedupe, and reproduce (Benny) run before any expensive implementer node is spawned. Most signals should die cheap.

**The three starter graphs (build in this order)**
1. **Bug graph (Benny):** signal → classify → reproduce in sandbox → report. Read-only. No merge rights. Proves sandboxes, verification, and the queue in one go.
2. **Spec-to-PR graph:** the full picture above, ending in a *draft* PR. This is Plan 1's Inner Loop, rewritten as an explicit graph with the spec gate in front.
3. **Overnight graph:** a scheduled run that takes the day's approved specs and low-risk tasks, runs graph 2 at low concurrency, and — only for categories that have earned it (§9) — auto-merges. The PM agent's morning summary is its output.

---

## 5. Spec-first workflow — the cheapest review you will ever do

**The spec file** (one per task, kept in the repo under `specs/` or attached to the queue item):

```markdown
# Spec: <task title>            Status: draft | approved | done
Source: <link to signal>        Approver: <name, filled at the gate>
## Problem        — what is wrong / missing, in 3–5 lines, with evidence links
## Change         — what will be built, and where (files/areas named)
## Not doing      — scope the agent must NOT touch
## Acceptance     — checkable tests: the verify commands + expected results
## Risks          — perf, data, auth, migration flags (any flag = no auto-merge)
```

**Rules**
- The spec agent writes from the signal + Feature Map + code search. It must name real files — a spec that could apply to any repo is rejected.
- **You review the spec, not a plan in chat.** Approve, edit, or reject in the file. Your edits to a spec are gold: log them. Repeated spec corrections become skill or template changes, the same correction-log discipline as Plans 1–2.
- Small tasks (typo, copy change, a test fix with an obvious acceptance check) may use a **spec-lite**: Problem + Acceptance only, approved in the queue with one tap. The gate shrinks; it does not disappear.
- The implementer gets the approved spec and nothing else as its brief. If the spec turns out to be wrong mid-task, the agent stops and requests a spec change — it does not improvise a new design. That stop is a feature: it is the pair-programming respect for thinking that she opened the talk with.

---

## 6. Skill evals — unit tests for your skills

This is the maintenance system Plans 1–2 were missing. A skill without evals will silently rot as the codebase, the models, and the product change.

### Layout — one `evals/` folder inside each skill

```
.claude/skills/<skill-name>/
├── SKILL.md
├── scripts/…                      # the skill's deterministic tools (Plan 1)
└── evals/
    ├── rubric.md                  # scored behaviours: what 10/10 looks like, what is an automatic fail
    ├── cases/
    │   ├── case-01/               # a task prompt + fixture files + expected evidence
    │   ├── case-02/
    │   └── …                      # 5–10 cases to start, incl. 2 known past failures
    └── results/                   # dated reports, per model (git-ignored trial workdirs)
```

### How a run works
1. **Runner script** (deterministic, yours) creates a fresh, neutrally-named trial directory per case — the trial agent must not be able to tell from paths or prompts that it is an eval.
2. A **coordinator agent** runs each case agent with the skill under test, in a sandbox (§8), on a named model.
3. The coordinator scores against `rubric.md`. A **judge agent on a different model** re-scores a sample (or all cases for critical skills, e.g. verification). Disagreements above a threshold are flagged for a human, not averaged away.
4. **Report:** one page — score per case, per model; the failures in plain words; links to trial evidence. The report is the deliverable, not just a number.
5. **Hill-climb loop (bounded):** on failure, you (or a skill-fixer agent, supervised) edit the skill, and the runner re-runs *only the failing cases plus one passing control case*. Loop cap: 3 rounds per session. Target: all cases at the pass bar (set yours — e.g. ≥9/10 with zero automatic fails) on every production model.

### Gates and cadence
- **No eval pass, no merge:** a pull request that changes a skill must include a fresh eval report for that skill. Put this in the same hook/CI layer as Plan 1's evidence gate.
- **Automatic fails** are behaviours that score 0 regardless of anything else — for the anti-hallucination skill: naming a cause without a code citation; for verification: claiming PASS without an evidence file; for any skill: touching a file outside its scope.
- **Cadence:** evals run (a) on every skill change, (b) monthly for the top 3 skills whether or not they changed (models drift under you), and (c) whenever a production failure is traced to a skill — that failure becomes a new case *before* the skill is fixed, so the fix is tested against the real failure.
- **Start small and local,** exactly as she advises: 5 cases for your verification skill, run on your machine, watched by you. The eval system itself is a skill-shaped tool — build the manual version first, automate the runner second.

---

## 7. The PM agent — the team's memory of the work itself

Plan 2's Chief of Staff routes *conversations*. The **PM agent** owns the *work*: it is a standing agent whose whole job is the state of the board. It writes no code and reviews no diffs.

**It runs on Plan 2's queue** — same task store, same states — and adds:

| Duty | How it works |
|---|---|
| Board hygiene | Every morning and evening: stale tasks flagged, blocked tasks named with their blocker, duplicates merged, tasks missing a spec or an acceptance check sent back before they reach an implementer. |
| Priority order | Keeps one ranked list per project, from rules you set (severity, user impact, age). It proposes re-ranking; you approve ranking changes that affect other people. |
| Overnight summary per person | "What <name>'s agents did last night": tasks finished, PRs landed / waiting, evidence links, spend. This is the summary her PMs use — a human always knows what the team did without reading 30 transcripts. |
| Capacity and cost report | Weekly: tasks by outcome, cost per landed PR, loop/escalation rate, which categories are close to (or losing) auto-merge rights under §9. |
| Standup brief | One short brief per project for the Chief of Staff's morning message — the PM agent writes it, the Chief of Staff delivers it. |

**Limits, on purpose:** the PM agent cannot approve specs, cannot merge, cannot change budgets, and cannot assign work to a human. It reports and organises. The moment it needs a decision, it puts a named question in the queue for you. Build it *after* the queue has real traffic (end of Plan 2 / start of this plan) — a PM agent over an empty board is theatre.

---

## 8. Sandbox isolation — one bot, one computer; one task, one worktree

Her bots each have their own VM and log themselves in. The Claude version, in two layers:

**Layer 1 — per bot (from Plan 2's roster): a container by default, a VM when needed**
- Default: one **Docker container per bot** on the shared host — its own filesystem, its own installed tools, its own MCP credentials injected as secrets at start, network allowlist per bot.
- Use a **lightweight VM** instead when the bot must drive a real desktop app or a full browser with a persistent logged-in profile (the Benny case: reproduce in a browser, screenshot the result). A container with a headless browser covers most web work; reserve VMs for the bots that truly need a desktop.
- Logins (Slack, GitHub, etc.) are **bot identities** where the service allows it (a GitHub bot account / app, a Slack app), never your personal password, and never a shared login across bots. A bot's token can do only what that bot's job needs — same scoped-permission matrix as Plan 2, now enforced by which secrets its container receives.

**Layer 2 — per task: a worktree and a clean run**
- Inside the bot's sandbox, each task still gets its own **git worktree + branch** (Plan 1). The sandbox isolates *environment*; the worktree isolates *code*. You need both: two tasks in one container without worktrees corrupt each other; two worktrees on your laptop without a sandbox share your logins and your files.
- Trial/eval runs (§6) get the same treatment: fresh directory, sandbox, no production credentials, ever.
- **Cleanup is part of the graph:** the final node deletes the worktree on success, archives the evidence + transcript to the queue, and reports sandbox cost/time. A sandbox that is not cleaned up is a cost leak and a future confusion source.

---

## 9. The auto-merge trust ladder — earning the overnight 20

She auto-merges because she climbed to it. This ladder makes the climb explicit, measurable, and reversible. A repo (and inside it, a *category* of change) sits at exactly one level. Levels are per repo + category: "docs and tests in Repo A" can be at Level 3 while "anything in Repo A" is still Level 1.

| Level | What happens | Entry criteria (all must hold) |
|---|---|---|
| **0 — Observe** | Agents prepare draft PRs; human reviews and merges everything (Plan 1 start). | — |
| **1 — Trusted drafts** | Draft PRs routinely need no substantive rewrite. Human still merges all. | ≥20 consecutive agent PRs in this category; ≥85% merged with no substantive human rewrite; 100% with complete evidence bundles; 0 regressions traced to agent PRs. |
| **2 — Merge on green, reviewed after** | The workflow merges when CI + verification + reviewer node are all green. Human reviews landed PRs next morning from the PM summary; any bad landing is reverted and investigated same-day. | Level 1 held for 2 more weeks; small atomic PRs only (set a diff ceiling, e.g. ≤300 lines, one concern per PR); a tested one-command revert path; on-call owner named. |
| **3 — Overnight auto-merge** | The overnight graph (§4, graph 3) merges approved-spec work unattended, up to a nightly cap (start: 5 PRs/night, raise toward her ~20 only as the record holds). Morning = PM summary + spot review. | ≥50 auto-merged PRs at Level 2 with 0 Sev-1/Sev-2 regressions and ≤2% revert rate; evals green for every skill in the path; nightly cap, cost cap, and a kill switch all tested — actually tested, by pulling them. |

**Hard exclusions — never auto-merge, at any level, ever:**
auth / permissions, payments and billing, data migrations and schema changes, deletes of data or infrastructure, dependency *major* upgrades, changes to CI / hooks / the merge policy itself, and anything whose spec carries a Risks flag (§5). These always land as draft PRs for a human, full stop.

**Demotion is automatic, not a discussion:** one regression traced to an auto-merged PR drops that category one level and freezes auto-merge for it until a post-mortem adds (a) a new eval case or CI check that would have caught it, and (b) 10 clean Level-appropriate PRs. This is the rule that keeps the ladder honest — and it mirrors her own logic: trust is personal, evidence-based, and lost faster than it is earned.

**What "reviewed after landing" requires to be safe:** small PRs (atomic, easy to revert), rich git history, evidence bundles attached to the queue item (not just the PR), and the PM agent's per-person overnight summary as the review checklist. If any of those four is missing in your setup, you are not at Level 2 yet, whatever the metrics say.

---

## 10. Non-engineers shipping safely

The pattern from the talk, with the guardrails named:

1. **Front door is chat.** A designer, PM, or GTM teammate talks to the Chief of Staff bot (Plan 2) or files a spec request. They never see a terminal, a worktree, or a credential.
2. **Their work takes the same road:** spec (they approve the spec in plain language — this is where their expertise applies) → graph → verification → review node → merge gate. Non-engineer work starts at Level 0/1 and earns levels by the same metrics; the *person's* job title changes nothing in §9.
3. **The harness carries the engineering weight:** paved path, banned patterns, strict CI (Plans 1–2) are what make a non-expert's change safe. If a non-engineer's PR fails, the first question is "what check was missing?" — not "why did they try?"
4. **Named human reviewer of record** for every non-engineer PR until that person's category reaches Level 2. Her PMs' fixes got her stamp; the stamp is a real step, not a courtesy.
5. **The PM agent summarises their work too** — one agent per account / per person (§1h) means their overnight summary is separate, readable, and theirs.

Done well, this is the highest-leverage outcome in the whole talk: the team's shipping speed stops being limited by engineer headcount for the long tail of small, well-specified changes.

---

## 11. Phased build plan

*Assumes: Plan 1 Phases 0–4 done for the pilot repo (verification skill, paved path, Inner Loop as draft PRs), and Plan 2 Phases 0–3 done (Chief of Staff, one project bot, queue, morning brief). If those are not done, finish them first — Plan 3 on an empty foundation is the "jump to 100 agents" mistake she warns against.*

### Phase 1 — Rewrite the Inner Loop as a graph (Week 1)
- Turn Plan 1's implementer → verifier → reviewer chain into an explicit workflow script (§4): typed hand-offs, verify loop capped at 2, escalation path.
- Build the **Benny bug graph** first and run it on real incoming reports for one week.
- **Exit gate:** Benny correctly reports reproduced / already-fixed / cannot-reproduce with evidence on ≥80% of a week's real bug signals, at a cost per report you accept.

### Phase 2 — Spec-first gate (Week 2)
- Add the spec file format (§5), the spec agent, and the approval marker to the graph. No approved spec, no implementer node.
- Log every human spec edit for two weeks; fold the repeats into the spec template and the spec skill.
- **Exit gate:** 10 tasks run spec-first; zero tasks where the implementer had to invent design mid-task; your average spec review takes <10 minutes.

### Phase 3 — Evals for the first two skills (Weeks 3–4)
- Build `evals/` for the verification skill and the anti-hallucination/debug skill (§6): rubric, 5–10 cases each (including real past failures), a local runner, cross-model judge.
- Hill-climb both skills to your pass bar on every model you deploy.
- Add the CI/hook rule: skill changes require a fresh eval report.
- **Exit gate:** both skills pass on all production models; one deliberately broken skill edit is caught by the evals (test the test).

### Phase 4 — Sandboxes per bot (Week 5)
- Move each Plan 2 bot into its own container; give the bug-graph bot a browser-capable sandbox (VM if needed) with bot-identity logins for Slack/GitHub.
- Add graph-level cleanup: worktree removal, evidence archival, cost reporting per run.
- **Exit gate:** two bots run tasks at the same time with zero shared state; killing one bot's container mid-task loses only that task, which the queue marks failed and can retry.

### Phase 5 — PM agent (Week 6)
- Build the PM agent on the queue (§7): board hygiene, priority list, per-person overnight summary, weekly capacity/cost report.
- Feed its summary into the Chief of Staff's morning brief; retire any hand-written status you were doing.
- **Exit gate:** two full weeks where the morning brief + PM summary are the only status you read, and nothing real was missed.

### Phase 6 — Earn Level 2 in one narrow category (Weeks 7–9)
- Pick the safest high-volume category (docs, tests, or small UI fixes with strong verification). Confirm Level 1 metrics from your Plan 1 records, then turn on merge-on-green for that category only, with the diff ceiling and revert path in place.
- Review landed PRs every morning from the PM summary — actually do it; this review is the price of Level 2.
- **Exit gate:** ≥20 merge-on-green landings, 0 regressions, revert path used or drill-tested once.

### Phase 7 — Overnight run + first non-engineer shipper (Weeks 10+)
- Turn on the overnight graph for Level 2 categories with a nightly cap of 5. Raise the cap only on §9's Level 3 criteria.
- Onboard one non-engineer (a PM or designer) through the §10 path, with you as reviewer of record.
- Monthly rhythm settles in: skill evals, ladder review with the PM agent's report, one demotion/promotion decision per category, gardener routine from Plans 1–2.
- **Exit gate:** a full month of overnight runs inside caps, a PM summary you trust, and at least one non-engineer change landed safely through the full path.

---

## 12. Risks and costs — the honest part

- **Up-front token spend is real.** Refactoring toward a strict harness cost her hundreds of PRs; evals and hill-climbing burn tokens on work that ships no features. She had unlimited tokens at a lab; you do not. Stage the spend: evals for two skills first, sandbox the one bot that needs it, one category up the ladder. Measure cost per *landed, unreverted* PR monthly — that is the only cost number that matters.
- **Graphs can hide waste.** A badly designed graph loops, retries, and fans out expensively while looking organised. Every loop needs a cap, every graph a per-run budget, and the PM agent's weekly report must show loop/escalation rates — a rising rate means the graph or a skill is failing, not that you need more agents.
- **Evals can be gamed — including by accident.** Agents behave differently when they detect evaluation; that is why trial setups are blind (§6). Also rotate and refresh cases: a skill tuned to pass 10 frozen cases has learned the test, not the job. Add every real production failure as a case.
- **Auto-merge fails socially before it fails technically.** One bad overnight landing that surprises a teammate will cost more trust than the metrics say. Keep caps low, summaries loud, and demotion automatic (§9) — and tell the team the ladder exists before Level 2, not after the first incident.
- **Spec gate can become theatre.** If specs are approved unread to keep work moving, you have rebuilt the original problem one step earlier. Watch spec-edit rates: specs that are *never* edited are probably not being read.
- **Non-engineer access widens the blast radius of a bad harness.** Every §10 shipper is safe exactly to the extent Plans 1–2's checks are real. Do not onboard non-engineers to impress anyone before Phase 6's record exists.

---

## 13. What is needed from the user to start

1. **Confirm the foundation:** is Plan 1's verification skill + paved path live in the pilot repo, and is Plan 2's queue running? If not, which of those do we finish first — Plan 3's Phase 1 needs both.
2. **Pick the first graph:** Benny-style bug reproduction (recommended — read-only, fast payoff) or the full spec-to-PR graph?
3. **Name the first auto-merge candidate category** — docs, tests, or another low-risk, high-volume change type in the pilot repo — and the human who will be its reviewer of record at Level 2.
4. **Set the first budgets:** per-run cost cap for graphs, nightly PR cap for the overnight run (suggested start: 5), and the monthly token budget for evals/hill-climbing.
5. **One non-engineer volunteer** for Phase 7 — a PM, designer, or other teammate who will ship through the chat front door, or "not yet" (the plan works without this; it is the last phase, not the first).

With those answers, the first buildable pieces are: the workflow-script skeleton for the bug graph, the spec template + spec agent, and `evals/` for the verification skill — Plan 3, Phases 1–3, ready to run on the pilot repo.

---
*Plan 3, prepared Nov 18, 2026. Source: Lauren Tan tutorial via the Facebook Reel shared Nov 18 (posted Sep 11, 2026 by Phan Đông Giang; full transcript read and summarised — no transcript text reproduced). Companions: `claude-agent-orchestrator-plan.md` (Plan 1) and `claude-persistent-bot-team-plan.md` (Plan 2), same folder. Claude-side mapping: Claude Agent SDK workflow scripts for loops/graphs, Claude Code skills with per-skill `evals/`, git worktrees inside per-bot containers/VMs, GitHub required checks + a narrow merge-bot identity for the auto-merge gates.*
