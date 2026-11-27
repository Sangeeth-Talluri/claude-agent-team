---
name: feature-dev
description: Build a feature the paved-path way — spec first, compatibility kept, checks green, release and rollback thought through.
---
# Feature Development

1. **Spec first** (specs/TEMPLATE.md). Human approves the spec before code.
   Non-trivial = touches stored data, a public API/schema, user-facing
   behaviour, or a build/release step.
2. **Compatibility:** public API and schema changes are additive first; the old
   version keeps working until the new one is proven. Note anything that breaks
   compatibility in the spec — that needs explicit human sign-off.
3. **Data:** if the feature changes stored data, migrations/schema changes must
   be reversible and backward compatible (CLAUDE.md rules); destructive changes
   are a separate, human-approved step.
4. **Follow the paved path:** copy the gold-standard module/component/test
   patterns named in .claude/rules/paved-path.md.
5. **Verify:** tests + lint + typecheck + build + smoke, evidence bundle in the
   draft PR. New behaviour gets new tests.
6. **Release note in the PR:** how it ships, how it turns off or rolls back,
   and what you watch right after release.

## Rationalizations

| Excuse | Rebuttal |
|---|---|
| "Small feature; skip the spec" | Non-trivial is defined by what the change touches — stored data, a public API/schema, user-facing behaviour, a build/release step — not by size. Spec first; a human approves it. |
| "Breaking the old API is fine; everyone is on the new one" | Additive first; the old version keeps working until the new one is proven. Anything that breaks compatibility is noted in the spec and needs explicit human sign-off. |
| "I will invent a pattern that fits better than the existing one" | Follow the paved path: copy the gold-standard module, component, and test patterns named in .claude/rules/paved-path.md. |
| "The release note can go in the chat thread" | The PR carries the release note: how it ships, how it turns off or rolls back, and what is watched right after release. |

## Verification

Done means:
- An approved spec (specs/TEMPLATE.md) exists for the change.
- The draft PR carries the evidence bundle: tests + lint + typecheck + build + smoke, with new tests for new behaviour.
- The release note in the PR states how the feature ships, how it turns off or rolls back, and what is watched right after release.
