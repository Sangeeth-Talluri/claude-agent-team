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
