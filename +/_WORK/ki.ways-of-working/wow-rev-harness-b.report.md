# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-harness-b

**🤖 → 👤 Handoff to supervisor · Run report at 02:59 BST · last mark 02:12 BST**

---

## Done

Blind acceptance review, read-only, against harness `main` at `9eb5a1e7`. Harness tests were rerun independently and pass: 1,414 passed, none failed. Nothing was changed, committed, accepted or pruned.

| Record | Verdict | Confidence | Reason |
| --- | --- | --- | --- |
| [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) (`ed49d2f26b62`) | REFUSE | medium | The level-check rule is real, but `[behind]` is missing from the banner's ordered item list and from the generated coordinator style, and pruning would delete the only home of the deferred questions. |
| [KI-HARNESS-OPS-010](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-010-receiver-local-acquisition-triage.md) (`d2e2a8964c48`) | REFUSE | medium | The rule and rubric are delivered, but they clash with `ki-repo-kb`'s triage guidance and neither links to the other, so receivers do not have "one `ki-acquire` rule". |
| [KI-HARNESS-OPS-011](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-011-separate-agent-session-acquisition.md) (`55efe0c86d31`) | ACCEPT | medium | Both goals are met and the decision record was edited in place as its standard requires; one useful piece of detail was dropped, and nothing else is wrong. |
| [KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md) | ACCEPT (prune) | high | It was done in `52779419` before any prune, no trade or record depends on it, and the rollout stays enforced: the PRINCIPAL-5 audit flags any principal that has not conformed. |

### Findings - KI-HARNESS-GOV-189

1. `skills/change-management/ki-coordination/references/standards-coordination.md:277`: `[behind]` is added in its own sentence before the banner paragraph. The paragraph at line 279, which says list items "come in this order and only where they apply", still leaves it out of the housekeeping items, so its position in the list is undefined and the standard contradicts itself.
2. `output-styles/ki-coordinator.md:48`, generated from the `output-style` source at `standards-coordination.md:600`: the coordinator's style lists the housekeeping items and the territory sweep items but not `[behind]`. It also does not mention the level check at a mark or at resume. Coordinators follow this style, so the rule the record's Goal asks for (line 23, "carries unresolved behind findings visibly in its active banner") will mostly not show up. The record decided the generated surfaces needed no change (record line 98); that was the wrong call for this boundary, which names the `[behind]` item (line 39).
3. Prune blocker, record lines 118-133: Kris's GOV189-SCOPE a) reads "keep the two open questions in its Discussion for a later record". Those questions are queue export and re-import, and host-bound agents. The 14 October DONE-on-handover decision and the decisions-log transfer notes are also only recorded here, and nothing else holds them. Pruning would delete them all.
4. Delivered correctly: the rule section (`standards-coordination.md:968`), the mark pointer (line 859), the resume and departure pointer (line 933), unknown-not-level handling, and the On hold carve-out. All of these match the narrowed boundary.

### Findings - KI-HARNESS-OPS-010

1. `skills/acquire/ki-acquire/references/standards-acquisition.md:37` asks the receiver to record a disposition in the capture package's README. `skills/repo-structure/ki-repo-kb/references/standards-acquired-triage.md:11` says triage grants no permission to "rewrite capture bytes", and line 9 says to write nothing into the packet when parking. The two rules contradict each other.
2. `skills/repo-structure/ki-repo-kb/SKILL.md:46` and `standards-acquired-triage.md:5` present file, turn into work or park as "the receiver disposition". The new rule (`standards-acquisition.md:46`) calls those only intake handling and sets four other dispositions. Neither file links to the other, and a receiver's guidance for `+/_ACQUIRED/` never reaches the `ki-acquire` rule. The fix is in `ki-repo-kb`, which is outside the record's boundary (record line 31), so it needs a boundary decision.
3. Minor: `skills/acquire/ki-acquire/references/rubric.md:50`. The ACQUIRE-5 description no longer says that dispatch is a Git move into `+/_ACQUIRED/`, and no longer lists the forbidden operations. The review prompt still lists them, so the criterion still works.

### Findings - KI-HARNESS-OPS-011

1. `skills/environment/ki-housekeeping-claude/SKILL.md:31`: the change removed the only harness statement that the repository/session form of `claude_code_session_read` gives the full session, while its legacy project/session form is a bounded preview. `mcp-housekeeping-claude/README.md:78` describes the tool only as a "Preview head/tail". The new reference, `standards-agent-session-acquisition.md:13`, says "proven provider route" without naming that form. This does not block acceptance, because read-back verification would catch a preview being used in place of the full session.
2. The decision record was amended in place and its `date` bumped. That matches the `ki-decision-records` living-record rule and the "current as-of date" rule. The ChatGPT and Codex routes are kept as they were, and no adapter or importer was changed.

### Findings - KI-HARNESS-GOV-209

1. The GOV209-ROLLOUT line (`ki-principal/+/_WORK/ki/messages.md:54`) says GOV-209 "is pruned once that home is cited", and the record now has that citation. The message queue is not a lasting home, but PRINCIPAL-5 (`skills/repo-structure/ki-repo-kb-principal/scripts/rubric/items/principal.ts:95`) keeps flagging every principal that has not conformed. The rollout therefore cannot be lost when the record is pruned. The only other mention of GOV-209 is a test fixture string.

## In Progress

Nothing is running.

Outstanding - no action requested now: the KI-HARNESS-OPS-011 finding 1 detail can be restored in any later edit of `ki-acquire`.

## Queries

### GOV189-DEFERRED-HOME - Where do the deferred host-move questions go?

**Context:** Kris narrowed [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) and kept two open questions in its Discussion "for a later record": queue export and re-import, and host-bound agents. The 14 October DONE-on-handover decision and the decisions-log transfer notes are also only in that record. A banner fix (`[behind]` in the ordered item list and the generated style) is needed in any case before acceptance.

**Query:** Once the banner fix lands, should the deferred material get its own record before GOV-189 is accepted and pruned?

**Options:**

a) (recommended, confidence medium - this follows the words of GOV189-SCOPE a) and loses nothing; the alternative is cheaper but depends on a Project note being kept up) Return GOV-189 to in-progress for the banner fix, capture one triage record holding the deferred host-move questions and the two 14 October notes, then accept and prune GOV-189.

b) Move the deferred material into the Mac Studio Setup Project note instead of a record, then accept and prune GOV-189 after the banner fix.

### OPS010-SEAM - Reconcile the two receiver triage rules

**Context:** [KI-HARNESS-OPS-010](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-010-receiver-local-acquisition-triage.md) has receivers write dispositions into the capture package. `ki-repo-kb`'s receiver triage, which came from GOV-209, forbids rewriting capture bytes and treats file, work or park as the disposition. Neither links to the other, and `ki-repo-kb` is outside OPS-010's boundary.

**Query:** Should OPS-010 be widened to cover `ki-repo-kb`'s receiver triage and reconcile the two rules before acceptance?

**Options:**

a) (recommended, confidence medium - this is a small edit, and the Goal promises one rule that the receiver can see) Return OPS-010 to in-progress with its boundary widened. `ki-repo-kb`'s triage reference should link to the `ki-acquire` rule, call file, work or park intake handling, and allow the disposition note in the package README, kept apart from the preserved source.

b) Accept OPS-010 as it is and capture the reconciliation as separate work.

### 🤖 → 👤 Handoff to supervisor · since 02:59 BST

👤 2 with you

- [with you] GOV189-DEFERRED-HOME · owner · since 02:59
- [with you] OPS010-SEAM · owner · since 02:59
