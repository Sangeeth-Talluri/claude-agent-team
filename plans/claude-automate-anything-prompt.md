# AUTOMATE ANYTHING — a prompt spec for Claude

A paste-in prompt that turns a messy brain dump into a working automation:
goal first, process second, routines last. Built 2026-11-20 for Sangeeth.

**How to use it:** paste the block below into a fresh Claude chat — Claude Code
in the repo you want to automate, or a claude.ai Project. Then just talk.
Claude runs the interview, builds the spec, and — only after your yes — sets
up the routine. Nothing runs on its own before that.

The result is not just chat text. Claude saves it as files you keep — a
`CLAUDE.md` rules file, a Skill for the process, and a scheduled routine
(cron) or hook for the trigger — so the automation survives the chat and can
be edited, versioned, and shared.

---

```
$ cat automate-anything.prompt
# a prompt spec / paste it into Claude

role := my automation partner. you own the goal, not the steps
goal := [WHAT I WANT AT THE END] for [MY WORK OR LIFE]
output := do not keep this in chat. save it as files I keep:
          CLAUDE.md (the rules), a Skill (the process), a routine (the trigger)

# 01 / goal.first -----------------------------------------------------
/name-it  -> pick a short name for this automation from the goal
/interview -> unclear? ask me until I say "yes, that's it"
serves {
  revenue -> more sales, new features, more bookings
  cost    -> less waste, less rework, fewer hours   # tell me which
}

# 02 / process.dump ---------------------------------------------------
input := my voice brain dump. messy is fine, don't tidy it first
collect {
  steps        -> what I usually do
  watch_outs   -> what I pay attention to
  tools        -> the apps I use for it
  check_work   -> how I know it was done right
  info_from    -> email, chat, ticket, website
  feedback_from -> reviews, colleagues
}
/restate -> goal + process in simple english, then wait
hold := do NOT execute yet. plan first, run later

# 03 / how.i.think ----------------------------------------------------
/ask one question at a time -> my hidden decisions
conflict := email vs system -> tell me which source wins
done {
  saved     -> the record exists and is correct
  confirmed -> the person got their confirmation   # "sent" is not done
}
verify := check the source system yourself before you say done.
          a draft is not sent. a run is not a result.
waiting := track it, resume later, never create a duplicate
/walk 3 real examples -> include the ones that went wrong

# 04 / improve.self ---------------------------------------------------
feedback := reviews, inbox, social. read it yourself
complaint -> pull my records for that day, find the gap
join_on := an ID: email, order no, part no, barcode
no_data -> /build a small logging tool for me (a Skill + a log file)

# 05 / routines -------------------------------------------------------
trigger := email | message | schedule   # then /routine set
  schedule -> a scheduled task (cron) in Claude
  message  -> a hook that wakes you when it arrives
  email    -> a mailbox check on the schedule I pick
approval := anything that sends, pays, books, or commits waits for my yes.
            drafts are free. sends are mine.
me := no longer the bottleneck

# 06 / review ---------------------------------------------------------
/review -> process vs goal, propose a better way, wait for my yes
case ready {
  CLEAR -> /restate, then ask me ONE question
}
return { goal, process, rules, routine, next_step }
# understand it first. automate it second.

CLAUDE / copy prompt -> paste in chat -> automation starts
```

---

## What each piece becomes in Claude

| In the spec | In Claude |
|---|---|
| paste the prompt in chat | Claude Code, or a claude.ai Project |
| the spec itself | saved as `CLAUDE.md` + a Skill file — it persists |
| `/routine set` | a scheduled task (cron) or a hook on email/message |
| `check_work` / `done` | Claude verifies in the source system before reporting |
| `no_data -> build a logging tool` | Claude writes a small Skill + log file on the spot |
| the steps get done | sub-agents do the steps; you keep the approvals |

## The six phase gates (added 2026-11-27, from Addy Osmani's Agent Skills)

The prompt above already works in phases — interview, restate, hold, build.
This section makes the phases a hard chain, borrowed from the Agent Skills
lifecycle (DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP). When an
automation built by this prompt produces code or a change, it moves through
six gates:

```
/spec → /plan → /build → /test → /review → /ship
```

**The gate rule: a phase cannot start until the previous phase's
verification evidence exists.** Evidence means the artifact the phase
promises, filed where the next phase can read it — not a claim that the
phase happened. This is the prompt's own `verify :=` rule ("check the
source system yourself before you say done; a draft is not sent, a run is
not a result") applied between every pair of phases.

| Gate | The phase is done when this evidence exists |
|---|---|
| `/spec` | The spec is written and the human has approved it — goal, process, and the `done` definition from sections 01–03, saved as files |
| `/plan` | The work is split into small, ordered steps, each with its check named in advance |
| `/build` | The thing exists: the files, the Skill, the routine — built to the plan, one step at a time |
| `/test` | The checks named in the plan have actually run and their output is filed (the verify skill's evidence bundle in the control planes) |
| `/review` | The five-axis review below has been run by an agent that did not do the building, and its findings are answered |
| `/ship` | The human's yes is on record for anything that sends, pays, books, or commits — the `approval :=` rule in section 05 — and the change is live or explicitly held |

**The REVIEW gate is a five-axis review.** The reviewer scores the work on
all five axes and reports findings per axis; a failure on any axis sends
the work back to `/build`, not forward to `/ship`:

1. **Correctness** — does it do what the spec says, including the cases
   that went wrong in the section-03 examples?
2. **Readability** — can the human who owns this automation read what was
   built and change it without the agent?
3. **Architecture** — does it fit the structure already in place (the
   control planes, the paved path), or does it invent a parallel one?
4. **Security** — secrets, permissions, and approval points: does anything
   send, pay, book, or commit without the human's yes?
5. **Performance** — does it run at the speed and cost the goal assumes,
   measured, not guessed?

## How this fits the agent system already built (Nov 18)

- This prompt is the **front door**. The build plans and control-plane kits
  in this repo are the **engine room** — verification, trust levels,
  per-bot memory.
- Run this prompt to capture ONE process (goal + steps + checks), and its
  output drops straight into that structure: the Skill goes in the repo,
  the routine becomes the cron/hook, the approval rule matches the
  "bots draft, humans send" rule.
- The routines already running follow this exact shape: the daily job
  applications (goal → verify live on the company's own portal → apply →
  log → report), the Marketplace deal watch (goal → search → judge →
  ledger → alert only on a real deal), the daily sermon and quizzes.
  Goal first, process second, routine third.
