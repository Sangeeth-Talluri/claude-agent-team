# Connectors (MCP)

- One `.mcp.json` **per bot**, generated from `mcp.template.json`, containing only the
  servers that bot's `bot.yaml` lists. A bot never receives a connector "just in case".
- Prefer **one Slack app per bot** (separate tokens in `.env`) so a bot can only ever
  act as itself, in its own channels.
- Start every connector **read-only**. Add draft/write scopes one at a time, per bot,
  and note the change in that bot's `MEMORY.md` decisions log.
- Tokens live in the host `.env` only. If a token ever appears in a prompt, a memory
  file, or git history, rotate it — do not just delete the line.
