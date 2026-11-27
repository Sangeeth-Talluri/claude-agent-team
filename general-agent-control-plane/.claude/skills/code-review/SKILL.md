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

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "That skipped test is probably just flaky" | A test disabled, skipped, or weakened to make checks pass is the first trap on this skill's list. Flaky is a finding, not a reason to wave it through. |
| "The lockfile changed a lot; that is normal for a PR this size" | Dependencies are reviewed: new ones justified, lockfile changes explained. Unexplained is a finding. |
| "There is no evidence bundle, but the change is small" | Missing evidence blocks, at any size. |
| "I will lead with the style issues; they are easy to list" | Style nits do not block and do not lead. Spec match, safety, and failure handling come first, in the reviewer agent's order. |

## Verification

Done means:
- Numbered findings exist, each tied to a specific line.
- Every trap on this skill's list is explicitly cleared or flagged — none silently skipped.
- The verdict (block / approve) names the evidence it rests on; missing evidence is itself a blocking finding.
