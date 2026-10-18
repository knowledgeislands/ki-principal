---
id: ki.baseline-rollout
level: project
title: 'KI > Foundations > Baseline rollout'
project: baseline-rollout
theme: foundations
worker: agent
supervisor: owner
state: on-hold
hold:
  reason: paused
  release: Kris's review
since: 2026-10-18T03:30:38Z
received: null
beat: null
mark: 2026-10-15T14:59:00Z
created_at: 2026-10-08T08:35:00Z
---

# ki.baseline-rollout

## Next steps

**Messages from Master: state-of-play** - the receiving thread acts on each line, then removes it.

- 2026-10-16 · THREADS-CLEAR · KI Model: ways-of-working, on Kris's decision of 15 October: "Each owning thread clears its own folder at its next mark, moving scratch to tmp/, homing or removing tracked work products and moving briefs to the state folder, told through its inbox by this thread." Apply it to `+/_WORK_REVIEW/ki.baseline-rollout/` against the closed list now in [ki-pmo's Tidying the thread folder](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-pmo/references/standards-pmo.md) and the ki-delegation [Run packet](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md) (ki-agentic-harness `065bbd5b`, on `origin/main`), in Kris's words: "A thread folder holds a closed list, decisions.md and <name>.report.md only; briefs live in the state folder, work products in their owning home, temporary output in the temporary location." · detail: [ways-of-working decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md)
- 2026-10-17 · PMO-7-BACKLOG · Master: state-of-play, on Kris's decision of 15 October: "Each thread relinks or deletes its own reports at its next mark under the thread-tidy rule, and the state-of-play thread tells each one so." Apply it to this thread's own folder, [`+/_WORK_REVIEW/ki.baseline-rollout/`](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK_REVIEW/ki.baseline-rollout/) · detail: [ways-of-working decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md)

1. Resting; launch nothing until Kris revives the pin-receiver idea.

Resume line: `Resume Fnd: baseline-rollout on sol from its checkpoint under current ki-pmo and ki-delegation since 2026-10-15T14:59Z: re-bootstrap, read the parked queries, take stock, restart authorised work, then banner.`

## Messages

- MIGRATED - this file was `+/_WORK_REVIEW/ki.baseline-rollout/work.md` until the work migration of 2026-10-18. At your next mark, cut it to next steps, Messages and the tags of parked queries, each linked to its report; move anything else to its durable home, then remove this line.

## Parked

- Held with the pin-receiver idea, PIN: `tools-ki` builds `ki` from source in CI and gets no receiver (recommended), rather than a receiver bump.
- Held, CHECKLIST: adopt the stock Repository review Activity across the estate only if Kris approves it for the Capital first.
- Parked 2026-10-10: for the pin-receiver idea, `update-ki-pin.yml` filters on `client_payload.source_repository` but tools-ki `release.yml` sends `client_payload.repository`, so `tool-release-published` dispatches would be skipped; the Capital carries `.github/ki-version` and `update-ki-pin.yml`, inert until the tools-release bot App and secrets are on it.
