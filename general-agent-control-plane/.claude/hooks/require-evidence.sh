#!/usr/bin/env bash
# Stop gate: when a task ID is set (AGENT_TASK_ID), an agent may not finish
# without an evidence bundle, and may not finish with a failing check in it.
# In ordinary interactive sessions (no AGENT_TASK_ID) this passes silently.
if [ -z "${AGENT_TASK_ID:-}" ]; then
  exit 0
fi
report="evidence/${AGENT_TASK_ID}/report.json"
if [ ! -f "$report" ]; then
  echo "No evidence bundle at $report — run the verify skill (.claude/skills/verify) for this task's acceptance checks first." >&2
  exit 2
fi
if grep -q '"status": "fail"' "$report"; then
  echo "Evidence bundle $report contains a FAILING check. Fix it or report the failure honestly — do not finish as if it passed." >&2
  exit 2
fi
exit 0
