// run-task — one call = one task = one isolated git worktree = one branch.
// Shape only (Claude Agent SDK). See Plan 1 §10 and Plan 2 §4 before wiring for real.
//   import { query } from "@anthropic-ai/claude-agent-sdk";
// Flow:
//   1. checkLaunch(task, ctx) from ./policy — throws = task stays queued, owner is told why.
//   2. Create worktree:  git worktree add worktrees/<task.id> -b claude/<task.id>
//   3. Run the implementer via query({ prompt, options: { cwd: worktree,
//        allowedTools: [...bot's scoped tools...], maxTurns: task.budget.maxTurns,
//        agents: { verifier, reviewer } } })
//   4. Verifier runs SEPARATELY and must produce evidence/<task.id>/report.json.
//      No report = no PR (platform/policy/policy.yaml: pr_requires_evidence_bundle).
//   5. Open a DRAFT PR with the evidence bundle linked. Never merge.
//   6. Write the final state back to the queue (platform/queue) — the Chief of Staff
//      brief is generated from the queue, so this write is what makes the work visible.
export {};
