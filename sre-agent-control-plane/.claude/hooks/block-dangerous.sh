#!/usr/bin/env bash
# PreToolUse guard: blocks commands an agent must never run in this repo.
# Reads the hook JSON on stdin. Exit 2 = block the tool call and show the message.
# Edit the pattern list in .claude/rules/dangerous-operations.md first, then here.
input="$(cat)"
patterns=(
  'terraform apply'
  'terraform destroy'
  'kubectl delete'
  'kubectl drain'
  'helm uninstall'
  'helm delete'
  'DROP DATABASE'
  'DROP TABLE'
  'TRUNCATE TABLE'
  'git push --force'
  'git push -f'
  'git push origin main'
  'git push origin master'
  'rm -rf /'
  'mkfs'
  'dd if='
)
for p in "${patterns[@]}"; do
  if printf '%s' "$input" | grep -qiF "$p"; then
    echo "BLOCKED by .claude/hooks/block-dangerous.sh: command contains '$p'." >&2
    echo "This operation is on the dangerous-operations list. A human runs it, or approves it explicitly outside the agent session." >&2
    exit 2
  fi
done
exit 0
