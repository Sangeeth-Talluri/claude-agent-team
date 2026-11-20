# Adoption backlog

Running list of adoption points from the daily scans. One checkbox per point, with its source link and the date it was found. Items are never repeated — check here before adding a new one.

## 2026-11-20

- [ ] Add a pre-flight security scan skill (`.claude/skills/security-scan/SKILL.md`) to both control planes — scan prompts, hooks, MCP config, permissions, and secrets before any bot runs. Target: `sre-agent-control-plane/` and `general-agent-control-plane/`. Source: https://github.com/affaan-m/ECC — 2026-11-20
- [ ] Add a failed-CI triage bot (`sre-agent-control-plane/.claude/agents/ci-triage.md`) — read the failed run, trace the cause, open a fix PR for human review, never auto-merge. Source: https://github.com/Tracer-Cloud/opensre — 2026-11-20
- [ ] Add a live hook-event timeline to the SRE control plane — stream the existing hook events (`sre-agent-control-plane/.claude/hooks/`) into a live timeline/graph of tool calls and subagent branches. Source: https://github.com/patoles/agent-flow — 2026-11-20
- [ ] Tighten `plans/claude-automate-anything-prompt.md` with the Superpowers bar — written spec in readable chunks with human sign-off, a junior-readable implementation plan, true red/green TDD before implementation. Source: https://github.com/obra/superpowers — 2026-11-20
- [ ] Mirror Anthropic's coordinator pattern in the bot-company Chief of Staff — proactive status pushes, one branch per bot, overlaps as merge conflicts, `/fork`-style alternate implementations. Target: `bot-company/chief-of-staff/` and `plans/claude-persistent-bot-team-plan.md`. Source: https://emergent.sh/news/claude-code-projects-adds-coordinator-btw — 2026-11-20
