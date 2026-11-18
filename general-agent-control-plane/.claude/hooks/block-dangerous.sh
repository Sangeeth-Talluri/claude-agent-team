#!/usr/bin/env bash
# PreToolUse guard: blocks commands an agent must never run in this repo.
# Reads the hook JSON on stdin. Exit 2 = block the tool call and show the message.
# Edit the pattern list in .claude/rules/dangerous-operations.md first, then here.
input="$(cat)"
patterns=(
  'git push --force'
  'git push -f'
  'git push origin main'
  'git push origin master'
  'rm -rf /'
  'DROP DATABASE'
  'DROP TABLE'
  'TRUNCATE TABLE'
  'aws s3 rb'
  'aws ec2 terminate-instances'
  'aws rds delete-db'
  'gcloud projects delete'
  'gcloud sql instances delete'
  'az group delete'
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
# Pipe-to-shell needs a regex, not a substring: real commands look like
# "curl -fsSL https://… | sh" — flags and a URL sit between curl and the pipe.
if printf '%s' "$input" | grep -qiE '(curl|wget)[^|]*\|[[:space:]]*(sudo[[:space:]]+)?(ba|z)?sh\b'; then
  echo "BLOCKED by .claude/hooks/block-dangerous.sh: command pipes a download into a shell (curl|sh / wget|bash)." >&2
  echo "This operation is on the dangerous-operations list. Download the script, read it, then run it deliberately — or let a human do it." >&2
  exit 2
fi
exit 0
