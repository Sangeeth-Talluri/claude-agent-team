// Shared types for the bot-company platform. Skeleton — Phase 5 of the plan fills this in.
export type BotName = "chief-of-staff" | "project-main" | "ops-life";
export type TaskState =
  | "queued" | "planning" | "implementing" | "verifying"
  | "reviewing" | "pr-open" | "done" | "failed" | "needs-human";

export interface Task {
  id: string;                 // t_<shortid>
  ownerBot: BotName;
  source: "slack" | "github" | "sentry" | "email" | "schedule" | "owner";
  title: string;
  sourceRef: string;          // link back to the Slack message / issue / alert
  featureMapRefs: string[];   // Feature Map entries this task touches (may be empty)
  acceptance: string[];       // checks the verifier must prove, with evidence files
  risk: "low" | "medium" | "high";  // high = human approves BEFORE a worker starts
  budget: { maxTurns: number; maxUsd: number };
  state: TaskState;
}
