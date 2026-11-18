-- Review queue — the single source of truth every brief is generated from.
-- SQLite to start; move to Postgres only when more than one host writes to it.
CREATE TABLE IF NOT EXISTS tasks (
  id            TEXT PRIMARY KEY,
  owner_bot     TEXT NOT NULL,
  source        TEXT NOT NULL,
  title         TEXT NOT NULL,
  source_ref    TEXT,
  risk          TEXT NOT NULL DEFAULT 'medium',
  state         TEXT NOT NULL DEFAULT 'queued',
  cost_usd      REAL NOT NULL DEFAULT 0,
  evidence_path TEXT,               -- folder with report.json, screenshots, traces
  pr_url        TEXT,               -- draft PR, when one exists
  created_at    TEXT NOT NULL,
  updated_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_tasks_state ON tasks(state);
CREATE INDEX IF NOT EXISTS idx_tasks_bot   ON tasks(owner_bot);
