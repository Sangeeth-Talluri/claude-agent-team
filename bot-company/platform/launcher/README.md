# Launcher

The only way any bot starts a cloud agent. Responsibilities:
- Enforce policy (`policy.ts`): kill switch, budgets, concurrency, repo locks, risk gates.
- Give every task its own git worktree + branch (`claude/<task-id>`).
- Stream the agent's progress into the queue so the status page and the morning brief
  are always current.
- Refuse to open a PR without an evidence bundle.

Skeleton stage: types + policy checks are real shapes; the SDK wiring in
`run-task.ts` is a commented flow to implement in Phase 5 of Plan 1 / Phase 3 of Plan 2.
