---
name: code-review
description: Review changes in any repo — spec match, paved path, data and dependency safety, failure handling, evidence completeness.
---
# Code Review

Review in the reviewer agent's order: spec match → paved path → safety
(destructive data changes? irreversible migration? secrets in the diff?) →
dependencies (new ones justified? lockfile changes explained?) → failure
handling → evidence completeness.

Traps to always look for, in any stack:
- A test disabled, skipped, or weakened to make checks pass
- Errors swallowed silently at a boundary where a caller or user should see them
- Retries without idempotency, or without backoff, on an operation that is not
  safe to repeat
- A destructive data change bundled into the same change that stops using the
  data (no rollback path)
- Secrets, tokens, or real user data committed in code, fixtures, or snapshots
- A new dependency that duplicates the standard library or an existing dep
- A change much larger than the spec — scope creep hides bugs

Numbered findings, specific lines. Missing evidence blocks. Style nits do not.
