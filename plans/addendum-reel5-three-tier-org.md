# Addendum to Plan 3 — the three-tier org (Reel 5, Nov 18, 2026)

**Source:** Facebook Reel posted Nov 8, 2026 by Việt Nguyễn AI
(`facebook.com/reel/1317729023768076/`).

## First, the honest finding

This is **substantially the same 60-minute Lauren Tan tutorial** as the previous Reel
(Plan 3). The transcript is 49,625 characters and matches that talk throughout —
the trust curve, ControlGlass, the Feature Map, PStack, skill evals, and the same
ending (PMs and designers shipping code under Dune's strict rules). It is a repost
with a different short intro and a different caption, not a new talk. No Plan 4 is
needed; everything technical in it is already covered by Plans 1–3.

## What is genuinely new or worth taking from it

### 1. The caption's three-tier org chart (poster's framing — see note below)
- **1 general manager agent** — oversees all work
- **3 project manager agents** — split the work, track progress
- **40+ worker agents** — execute tasks overnight
- She runs them overnight; in the morning she reviews results and decides next steps.

**How this maps onto the bot-company scaffold you already have:**

| Caption tier | Your scaffold today | Change to reach the caption's shape |
|---|---|---|
| 1 general manager | `chief-of-staff/` — already built | None |
| 3 project managers | `bots/project-main/` is PM #1 — it owns one repo, triages, tracks its queue | Add PM #2 and PM #3 only when you have a 2nd and 3rd real project (Plan 2's rule: own workspace + own signals + a named routine). Copy the `bots/project-main/` folder as the template — that is what it was designed for. |
| 40+ workers | Launched per-task through `platform/launcher/`, capped today at 5 concurrent for project-main and 8 total in `platform/policy/policy.yaml` | Raise caps only on Plan 3's trust ladder. 40 workers is a *concurrency* number, not a headcount to hire on day one — the same worker pool, launched 40 times across a night, is the same thing. |

### 2. The originating use case, in her words from this edit's intro
The persistent bot began as: *"what would it look like if your agent was really more
like a colleague… how would I make it so my agent could just automatically fix bugs
for me while I sleep?"* Plus a duty she adds here: engineers are also responsible for
keeping the codebase in a condition where PMs and designers can contribute
high-quality code.

That is already the shape of your scaffold: `nightly-triage` (02:00) →
`morning-launch` (06:45) → Chief of Staff brief (07:00), with draft PRs only.
"Fix bugs while I sleep" becomes safe the moment Plan 3's auto-merge ladder is
earned — and not before.

### 3. The poster's token note
The caption ends by noting the author doesn't have to worry much about tokens.
You do. This changes nothing in the plans — it is why your scaffold has per-bot
daily budgets and per-task caps enforced in `platform/policy/`, and why Plan 3
measures cost per landed, unreverted PR.

## Provenance note
- The three-tier numbers (1 / 3 / 40+) come from the **poster's caption**, not from
  Lauren's spoken transcript in this video — the words "project manager" and the
  number 40 do not appear in what she says here. Plan 3's team description
  (Chief of Staff + a PM agent + 20+ workers) came from the previous poster's
  caption of the same talk. Treat both as "roughly: one manager layer, a small
  PM layer, dozens of workers" — the exact counts are caption-level claims.
- The "fix bugs while I sleep" line **is** in her spoken words in this edit.

*Addendum prepared Nov 18, 2026. No changes made to Plans 1–3 or to the
bot-company scaffold — the three-tier shape is a growth path for the scaffold,
not a redesign.*
