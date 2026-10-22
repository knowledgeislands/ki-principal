# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-rig064-b

**🤖 → 👤 Handoff to supervisor · Run report at 02:47 BST · last mark 02:12 BST**

---

## Done

Blind review of the cancellation of [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md) in tools-rig `53afaa5c9b`, checked against the ki-work-roadmap and ki-accept standards. Read only: nothing changed, nothing committed.

**Verdict: REFUSE.** Confidence high: the approved course behind SWEEP-CONVERT names this record as the one exception to it, so the reason given for the cancellation is untrue.

Findings:

1. **The reason contradicts the decision it cites.** The reviewed sweep course that Kris approved as SWEEP-CONVERT a) on 20 October lists "every convert except that KI-TOOL-RIG-CORE-064 stays as a narrowed Rig record while its recurring scan goes to `ki.chezmoi` as an Activity" (ki-principal `303f1cc0`, `+/_WORK/ki.ways-of-working/design/roadmap-sweep.md`). ki.chezmoi's Decision 183 says the same: "KI-TOOL-RIG-CORE-064 keeps Rig-managed configuration". SWEEP-CONVERT therefore decided that this record should be kept. It did not approve cancelling it.
2. **The scan had already left the record.** The narrowing on 20 October moved the recurring scan to chezmoi, where it landed in chezmoi `64b0fbb` (KB-DOTFILES-HK-001, "review unmanaged configuration on each Mac"). By 22 October the record held only Rig's capability question: should Rig declare and manage an application's configuration alongside its installation? The cancellation reason ("the recurring scan belongs to the chezmoi repository") is about scope the record no longer had.
3. **No approval covers this cancellation.** ki-accept requires exact human approval of the cancellation `resolution` and says batch authority never substitutes for it. The overnight burndown grant routes follow-ups as messages. It does not authorise cancelling an open triage record, and SWEEP-CONVERT excluded this one.
4. **`superseded` does not fit.** The standard defines `superseded` as "a later record replaces it". Here no record replaces it, and the `## Cancelled` section says none was created. A message line is not a replacing record, and chezmoi's HK-001 replaces the scan, not the Rig capability that was left.
5. **Value is lost.** The ki.chezmoi line reduces the Rig question to one clause and sends it to the wrong owner. Under tools-rig `AGENTS.md`, catalogue and provider capability belong to Rig, while chezmoi keeps its own source semantics. The line drops three things: the record's three planning questions (how to tell configuration from caches and machine state, whether to render through chezmoi or write directly, how to exclude secrets), the In/Out boundary, and the link between Kris's 18 October wish ("it'd be nice if it could also manage config for apps") and the Rig theme. It also tells the receiver to "create no roadmap record", so the question has no way back to tools-rig.
6. **The message line duplicates finished work.** Its first sentence asks ki.chezmoi to maintain a scan that ki.chezmoi adopted on 20 October (Decision 183, `64b0fbb`). The file also still has a stale "None." line above the entry.
7. **Do not prune.** The record is the only full statement of a capability Kris asked for and the sweep chose to keep. A cancelled record is retained until a prune is explicitly selected, and an unsound cancellation is not one to select. Pruning now would lose the question.

Checks: SWEEP-CONVERT scope, failed (record excepted); cancellation authority, failed; `resolution` fit, failed; successor coverage, partial (scan covered, Rig capability not); prune eligibility, refused.

## In Progress

Nothing.

## Queries

**RIG064-RESTORE**

**Context** KI-TOOL-RIG-CORE-064 was cancelled as superseded under SWEEP-CONVERT, but SWEEP-CONVERT explicitly kept it as a narrowed Rig record, and its scan already lives in chezmoi KB-DOTFILES-HK-001.

**Query** How should the cancellation be handled?

**Options** a) (recommended, confidence high - restores the approved SWEEP-CONVERT course without losing the capability) Revert the cancellation in tools-rig so the record is back in triage, with its updated `updated_at` and the 20 October narrowing kept. Then withdraw or correct the 22 October ki.chezmoi line so it neither repeats the scan nor carries the Rig question. b) Cancel it properly: put to Kris as its own cancellation query with `resolution: obsolete` or `rejected`, and keep the capability as an "Idea: Rig-managed application configuration" line on the Rig theme page, as was done for the two other cancelled Rig records on 20 October. c) Keep the cancellation as it stands and prune. Not advised: the stated reason is false and the question is lost.
