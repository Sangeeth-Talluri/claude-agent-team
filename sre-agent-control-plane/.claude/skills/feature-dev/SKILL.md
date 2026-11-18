---
name: feature-dev
description: Build a backend feature the paved-path way — spec first, backward compatibility, migration safety, observability included.
---
# Feature Development (backend / SRE)

1. **Spec first** (specs/TEMPLATE.md). Human approves the spec before code.
   Non-trivial = touches data, an API contract, a topic schema, or infra.
2. **Compatibility:** API/topic changes are additive first; consumers before
   producers on rollout; the old version keeps working until the new one is proven.
3. **Data:** migration reversible + backward compatible (CLAUDE.md rules);
   new queries ship with EXPLAIN in the evidence.
4. **Observability is part of the feature:** logs with trace IDs, a metric or
   dashboard that shows it working, an alert with a runbook if it can page.
5. **Verify:** tests + smoke + (if applicable) slo/tf-plan/k8s-dryrun checks,
   evidence bundle in the draft PR.
6. **Rollout note in the PR:** how it turns on, how it turns off, what you watch
   for the first hour.
