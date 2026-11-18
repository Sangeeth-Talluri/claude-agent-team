// Policy enforcement — the part that must NOT live in a prompt.
// Every launch goes through checkLaunch(). If it throws, no agent starts.
import type { Task } from "./types";

// TODO(platform): load platform/policy/policy.yaml + the bot's bot.yaml at startup.
export function checkLaunch(task: Task, ctx: {
  killSwitch: boolean;
  botSpentTodayUsd: number; botDailyCapUsd: number;
  runningAgentsForBot: number; botConcurrencyCap: number;
  repoLockedByOther: boolean;
  humanApprovedHighRisk: boolean;
}): void {
  if (ctx.killSwitch) throw new Error("Kill switch is on — no launches.");
  if (ctx.botSpentTodayUsd >= ctx.botDailyCapUsd)
    throw new Error(`Daily budget reached for this bot. Task ${task.id} stays queued.`);
  if (ctx.runningAgentsForBot >= ctx.botConcurrencyCap)
    throw new Error("Bot concurrency cap reached.");
  if (ctx.repoLockedByOther)
    throw new Error("Repo is locked by another agent. One writer per repo.");
  if (task.risk === "high" && !ctx.humanApprovedHighRisk)
    throw new Error("High-risk task needs the owner's approval before a worker starts.");
}
