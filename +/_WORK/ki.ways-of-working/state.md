---
id: ki.ways-of-working
state: with-worker
since: 2026-10-22T01:12:00Z
received: 2026-10-22T01:11:00Z
beat: null
mark: 2026-10-22T01:12:00Z
method_read: eff6163b
---

# ki.ways-of-working state

## Now

- 02:12 BST mark: the work folder is tidy (wow-tidy-deep-2 and -3 removed 471 reports and briefs, each with a byte-identical runtime copy); seven entries remain. A `git pull --rebase` begun at 01:19 by no run of this work stopped half-way in tools-ki and ki-principal; the coordinator aborted both, restoring each main, and `ki` runs again.
- wow-day-impl-fix-5 is finishing the fifth fix of the first-stage agent control contract on tools-ki 6c4d2a1a; it cannot integrate because origin/main gained 51725e8b from another session.
- `ki agent send` fails while ki.mac-studio-setup's events.jsonl has lost an observed terminal outcome.
- Writers, one per repository; a run not named here stops:
  - tools-ki: wow-day-impl-fix-5, in its own worktree (local main 6c4d2a1a, 2 ahead and 1 behind origin; v0.13.0 ready for Kris to tag at 65e06273).
  - tools-rig: none (v0.8.0 green at a2bc1093; tagging waits on RIG-RELEASE-REVIEW-BOUNDARY).
  - ki-design: none.
  - ki-agentic-harness: none (KI-HARNESS-GOV-209 kept until the eight-principal rollout is homed by a line to State of play).
  - ki-principal: wow-principal-rebase, integrating origin/main (local main 111 ahead, 10 behind), no push.

## Next steps

- Coordinator, overnight: receive fix-5; one run rebases this work's unpublished tools-ki commits and the fix onto origin/main 51725e8b in a worktree and re-verifies; three fresh blind re-reviews. On acceptance by all three, one run checks the unpushed tools-ki range holds only this work's and 51725e8b's line and pushes fast-forward; one Harness alignment line; native-evidence runs (CONTROL-EVIDENCE a), DEFAULTS-HANDOFF a)). If round five still finds blocking defects, raise convergence to Kris as a query; no sixth fix.
- Coordinator: prune KI-HARNESS-GOV-209 once State of play homes its rollout; remove the GRANT-INTERIM sentence once tools-ki v0.13.0 is installed.
- Kris: TOOLSKI-TAG, RIG-RELEASE-REVIEW-BOUNDARY, TAGS and the seven parked queries, re-asked at 02:02; visual checks for KI-OBSERVA-BRG-005, KI-PRINCIPAL-OPS-014 and KI-DESIGN-ICO-001; the GOV-227 session on design/gov-227-storage-schema.md.
- Blocked elsewhere: KI-PRINCIPAL-ECO-013 re-review; KI-HARNESS-GOV-224's follow-up with ki.observatory.

## Held

- PAPERCLIP-REQ, on hold while Kris gets KI stable; not tied to a Wave (2026-10-19).
- Parked queries in `queries.md`, Kris to come back to them.
- Email-routing records stay with hnr.email-routing.
