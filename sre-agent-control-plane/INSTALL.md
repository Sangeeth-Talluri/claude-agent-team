# Install into your work repo

1. **Copy** (from this folder, into your repo root):
   - `CLAUDE.md`, `.mcp.json`, `specs/`
   - the whole `.claude/` folder
   Merge, don't overwrite, if your repo already has any of these.
2. **Make hooks executable:** `chmod +x .claude/hooks/*.sh`
3. **Fill the TODOs** — search for `TODO(owner)`. The important ones:
   - `CLAUDE.md` — repo name, stack, real build/test/lint commands
   - `.claude/skills/service-map/SERVICE_MAP.md` — your top services to start
   - `.claude/skills/verify/verify.config.yaml` — copy the example file and put
     your real commands in it (test command, smoke URL check, etc.)
4. **First session test:** open Claude Code in the repo and ask for a small,
   safe task. Watch that it (a) follows the paved path in `CLAUDE.md`,
   (b) uses the verify skill, (c) leaves an evidence bundle under `evidence/`.
5. **Then** enable the agents one at a time (Plan 1, Phase 4): planner + verifier
   first, implementer last, draft PRs only.

Keep this folder's origin private: it contains no secrets and no work code, and it
should stay that way — repo-specific filled versions live in your work repo only.
