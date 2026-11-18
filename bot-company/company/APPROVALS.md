# Approval Limits — what bots may do alone, and what always needs the owner

| Action | Bot alone? | Rule |
|---|---|---|
| Read email / Slack / calendar / GitHub | Yes | Only the connectors and channels listed in its own `bot.yaml` |
| Draft an email, Slack reply, issue, or PR description | Yes | Drafts are saved, clearly marked as drafts |
| **Send an email** | **No — owner's tap, always** | No exceptions by amount, person, or urgency |
| Post in an internal bot channel | Yes | e.g. the bots' own status channel |
| Post in any external / public / customer channel | No — owner's tap | Includes X / social media, always |
| Open a **draft** PR | Yes | Into the review queue, with evidence attached |
| Merge a PR, push to main | No — human only | At every trust level, for now |
| Create a calendar hold (no invitees) | Yes | Marked "BOT HOLD" |
| Invite people to a meeting | No — owner's tap | |
| Pay for something | Virtual card only, Phase 5+ | Cap: **$50 per transaction, $200 per bot per month** to start. Every charge reported in the next morning brief. Any amount above the cap = owner's tap first. |
| Delete files, messages, issues, or data | No — owner's tap | Includes "cleanup" deletions |
| Change another bot's config, memory, or routines | No | Owner or Chief of Staff (memory summaries only) |

TODO(owner): adjust the payment caps and any row you want stricter or looser.
Stricter is always safe to set without asking anyone.
