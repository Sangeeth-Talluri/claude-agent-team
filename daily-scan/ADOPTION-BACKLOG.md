# Adoption backlog

Running list of adoption points from the daily scans. One checkbox per point, with its source link and the date it was found. Items are never repeated — check here before adding a new one.

## 2026-11-20

- [ ] Add a pre-flight security scan skill (`.claude/skills/security-scan/SKILL.md`) to both control planes — scan prompts, hooks, MCP config, permissions, and secrets before any bot runs. Target: `sre-agent-control-plane/` and `general-agent-control-plane/`. Source: https://github.com/affaan-m/ECC — 2026-11-20
- [ ] Add a failed-CI triage bot (`sre-agent-control-plane/.claude/agents/ci-triage.md`) — read the failed run, trace the cause, open a fix PR for human review, never auto-merge. Source: https://github.com/Tracer-Cloud/opensre — 2026-11-20
- [ ] Add a live hook-event timeline to the SRE control plane — stream the existing hook events (`sre-agent-control-plane/.claude/hooks/`) into a live timeline/graph of tool calls and subagent branches. Source: https://github.com/patoles/agent-flow — 2026-11-20
- [ ] Tighten `plans/claude-automate-anything-prompt.md` with the Superpowers bar — written spec in readable chunks with human sign-off, a junior-readable implementation plan, true red/green TDD before implementation. Source: https://github.com/obra/superpowers — 2026-11-20
- [ ] Mirror Anthropic's coordinator pattern in the bot-company Chief of Staff — proactive status pushes, one branch per bot, overlaps as merge conflicts, `/fork`-style alternate implementations. Target: `bot-company/chief-of-staff/` and `plans/claude-persistent-bot-team-plan.md`. Source: https://emergent.sh/news/claude-code-projects-adds-coordinator-btw — 2026-11-20

## 2026-11-21

- [ ] Add TokenEconomizer-style cost hooks to both control planes — session-start learned-facts injection, unused-tool pruning, loop guard on repeated failures, per-session cost ledger. Target: `sre-agent-control-plane/.claude/hooks/` and `general-agent-control-plane/.claude/hooks/`. Source: https://github.com/microsoft/TokenEconomizer — 2026-11-21
- [ ] Add tiered model routing to the bot-company Chief of Staff — size each task Light/Regular/Heavy, hand it to a bot locked to the matching tier (Haiku/Sonnet/Opus), escalate-only, tiny shared context file, model tag on every reply. Target: `bot-company/chief-of-staff/` and `plans/claude-persistent-bot-team-plan.md`. Source: http://dev.to/kronx26/i-routed-claude-code-tasks-to-cheaper-models-heres-what-15-requests-saved-published-true-tags-53e7 — 2026-11-21
- [ ] Add a context offload + summarization rule to both control planes — summarize long threads, offload tool outputs to disk, persistent memory across sessions. Target: `sre-agent-control-plane/` and `general-agent-control-plane/`. Source: https://github.com/langchain-ai/deepagents — 2026-11-21
- [ ] Add the operator + audited-merge discipline to the automate-anything prompt — main session never writes code, parallel lanes against one shared contract, every merge audited, root cause before every fix. Target: `plans/claude-automate-anything-prompt.md`. Source: https://github.com/tusharsrivastava/shark-skills — 2026-11-21
- [ ] Add room-scoped agent visibility to the bot-company design — each bot only sees the rooms/channels it belongs to; admin controls which connectors are on. Target: `bot-company/`. Source: https://github.com/sandbox-quantum/switch — 2026-11-21
