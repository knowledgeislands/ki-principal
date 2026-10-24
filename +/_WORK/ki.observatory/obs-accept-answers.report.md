# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-accept-answers

**🤖 → 👤 Handoff to supervisor · Run report at 20:03 BST · last mark 19:02 BST**

---

## Done

- **Accepted:** KI-OBSERVA-BCN-007, KI-OBSERVA-BRG-003, KI-OBSERVA-VIS-025 and KI-OBSERVA-VIS-026 are now done.
- **Captured as triage:** [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) holds the five Act board parts that have no source yet. [KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md) makes feedback send write to `messages.md`. [KI-OBSERVA-VIS-043](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-043-review-queue-reads-queries.md) makes the Review queue read `## Open` in `queries.md`.
- **Merged:** each target now carries its source's outcome, acceptance checks, gates and dependencies as a later phase or step, including the go Kris must give under DESIGN-APPLY. The sources are cancelled as merged.
  - VIS-040 and INT-004 → [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md), now titled "Two-way live-artifact adapter".
  - VIS-035 and VIS-036 → [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md). It also gained the body sections a Ready record needs; their absence was the audit failure already on `main`.
  - VIS-037 → [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md).
  - VIS-021 → [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md), as a tool-storage phase that does not wait on the consolidation.
  - VIS-039 → [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md), as its Council step.
  - VIS-029, VIS-032, VIS-033 and VIS-034 stay in triage.
- **Answers folded in:**
  - CONDITION-TOML → [KI-OBSERVA-BCN-008](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BCN-008-beacon-signal-anatomy.md) and VIS-030. Both depend on the harness defining the maturity scale and tools-ki reading and auditing it; neither repository's records are linked.
  - NEW-MARK → BCN-008.
  - LARGE-SCREEN → BCN-008, APP-044, VIS-030 and VIS-031.
  - RUN-EVIDENCE → VIS-031.
  - STEP3-LATER → INT-003 and [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md).
- **Pruned (10):** BCN-007, BRG-003, VIS-021, VIS-025, VIS-026, VIS-035, VIS-036, VIS-037, VIS-039 and VIS-040. Their surviving links in this repository now point to the commit where each record reached its final state. KI-OBSERVA-INT-004 is kept as cancelled because ki-principal's `design/live-artifacts.md` links to it.
- **Record count:** 34 before and 27 after (34, plus 3 captured, minus 10 pruned).
- **Commits:** five, all local in apps-observatory.local: `5e0e2f6`, `f0251b6`, `af3493b`, `02cb729` and `4da194b`. Nothing is pushed, under PUSH-KRIS. Only roadmap documents changed, so the service needs no restart.
- **Checks:** `ki repo audit` passes with the existing warnings, `bun run test` passes and `rumdl` finds no issue.

## In Progress

Nothing.

## Queries

**LARGE-SCREEN-EXISTING**

**Context:** LARGE-SCREEN removes the 760 px column-dropping scheme. The scheme already exists in shipped tables, in PDR-KI-OBSERVA-002 and in the width test. I wrote into KI-OBSERVA-APP-044 that its Product Decision Record retires that rule and its test.

**Query:** Should the scheme already shipped be retired too, or should only new work stop declaring dropped columns?

**Options:**
a) (recommended, confidence medium - one rule to maintain, and it matches "no column-dropping scheme") Retire it through APP-044's decision record, as now written.
b) Keep the shipped narrow behaviour and its test, and only stop new records from declaring dropped columns; I would reword APP-044.

### 👤 With supervisor · since 20:03 BST

👤 1 with you

- [with you] LARGE-SCREEN-EXISTING · owner · since 20:03 BST
- [committed] apps-observatory.local, five local commits, not pushed (Kris pushes)
