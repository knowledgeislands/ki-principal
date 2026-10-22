# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-eco013-b

**🤖 → 👤 Handoff to supervisor · Run report at 02:59 BST · last mark 02:12 BST**

---

## Done

- Blind review of the cancellation of [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md) (commit `d0836164`). Read only; nothing was changed and nothing was committed.
- **Verdict: REFUSE** pruning the record as it stands. The cancellation itself is sound. **Confidence: high.** Reason: `superseded` is the only honest terminal ending available, but the `ki-accept` prune preflight fails, because live references and one harness specification evidence line still depend on the record and would be orphaned or made false by deleting it.
- Read-only `ki repo audit` runs on ki-principal: `ki-repo-kb-streams` passed and `ki-work-roadmap` passed; neither reported anything on this record.

### Findings

1. **Cancelling it is sound, and "accepted" (`done`) is not available.** Under `ki-accept` §5, delivery closure needs `awaiting-review` and passing governing audits, with no waiver. The record went back to `in-progress` after the failed independent review on 2026-10-20, and `ki-coordination`, `ki-work-package` and `ki-authoring` failed then, including on this work's own package. Getting to `done` would mean repairing those audits and putting a fresh review packet against a skill (`ki-pmo`) that no longer exists, which would be wasted effort. Cancelling is allowed from any open state (`standards-repository-roadmaps.md`, the Cancel row). The `## Cancelled` section correctly says "no delivery acceptance is claimed", so it does not fabricate a `done`.
2. **The shape conforms.** It has `status: cancelled` with `resolution: superseded`, the horizon is removed, `baseline_ref` is kept, `## Cancelled` sits immediately before `## Discussion`, and there is no `resolution_target`. That is correct because the replacing work is in the KI Agentic Harness (`ki-coordination` and `ki-work-package`), which the section describes in plain words as `standards-work-item-format.md` §Cancellation requires. `superseded` fits better than `obsolete`: the need was met and then carried forward, not dropped.
3. **Authority is inferred, not stated outright (medium).** Cancellation needs explicit human approval, and `ACCEPT-BUNDLE` never approves a cancellation. Kris's 02:28 words ("the roadmap is at least half what it is now ... keep pushing, chipping away") do not mention cancelling. "Closing records that are superseded or done" comes from the coordinator's "Taken as" read-back. Under the 14:46 and 02:25 grants, three agreeing high-confidence reviews stand in for Kris's approval, so the cancellation and any prune rest on the full review set agreeing. This review agrees with the cancellation but not with an immediate prune.
4. **Prune blocker: cross-repository evidence dependency.** At `ki-agentic-harness/docs/specs/harness.md:145`, the output-style HARN clause's _Evidence_ line reads "the pilot's live acceptance in a coordinating thread is recorded by KI-PRINCIPAL-ECO-013 in Knowledge Islands Principal." Two problems follow. After a prune this evidence lives only in Git history. Also, the record now states that the live acceptance tests 2 and 3 never ran and that no acceptance is claimed, so the line overstates the record already. `ki-accept` §4 step 5 and the reference preflight require surviving dependent prose to be repaired first, and this repair is the harness's to make. It needs a `messages.md` line to the harness work, repointing to a pinned revision and restating what the record actually holds (test 1 on Claude Code only).
5. **Prune blocker: local links that would dangle.** Three places link to the record's live path and would break on prune: the WEBSITE-SKILL-SYNC line in `+/_WORK/ki/messages.md:15`; `design/change-management-decisions.md:47` (RECAP-AWARE); and `design/roadmap-sweep.md:52`, which also still proposes "close as done". Each needs repointing to a `(pruned)` link pinned at `d0836164` or later, in a commit before the prune.
6. **Prune blocker: message lines that are now false.** AUDIT-FINDINGS lines in seven works' `messages.md` say the findings "hold KI-PRINCIPAL-ECO-013's acceptance" or ask that they be cleared for it: `ki.baseline-rollout`, `ki.portable-specifications`, `ki.agent-host`, `ki.regular`, `ki` (line 17), `ki.timelines` and `ki.mac-studio-setup`. The audit findings still stand on their own, but the reason given no longer holds. Each line needs a one-line correction, or a note that the record was cancelled, before the prune. Separately, `ki.ways-of-working/state.md:30` still lists "Blocked elsewhere: KI-PRINCIPAL-ECO-013 re-review", which is stale now.
7. **Value that would be lost (medium).** The "Pilot lessons for Waves A to D and F" in Discussion exist only in this record. Waves A to F were never captured, and I found no other home for several lessons that still apply to current work:
   - a second session opened on live work answers read-only and never moves the mark (the CODEX-MARK lesson);
   - a skill declaration follows the skill onto `main`, because audits resolve through the dev-linked primary checkout, so a worktree can't audit or conform it;
   - a stray `.claude/settings.local.json` written by `/output-style` silently overrides the tracked coordinator style;
   - shaping a new skill hits known checker edges, and a full test suite can hang;
   - verbatim edits under the Headroom proxy need narrow reads.

   Git history keeps them, but `standards-work-item-format.md` warns that "anything held only here is held nowhere". Before pruning, either route those lessons to their owners (the `ki-coordination` standard, `ki-git` or `ki-delegation`, and the chezmoi Claude Code guide) as message lines, or link them from the Project note through a pinned revision.
8. **Minor record drift.** Outstanding concerns says IDENTITY-PHASE3 is "routed ... in `messages.md`", but it was struck as overtaken under STALE-RESHAPE at the 2026-10-21 01:40 mark. Current state still says "In progress after the failed independent acceptance review". `## Cancelled` claims every leftover was "already routed", which is true only with that correction. None of this blocks the cancellation.
9. **Safe historical mentions.** These need no repair: the bare identifiers in `ki-coordination/references/sources.md` (provenance), the test fixture in `coordination.test.ts`, and the `ki-pmo`/ECO-013 mention in `change-management-decisions.md:30` (a historical quote).

## In Progress

Nothing is running.

Outstanding - no action requested now: the record stays cancelled and retained. It becomes prune-eligible once findings 4 to 7 are repaired in commits before the prune, and the prune commit then contains only the deletion.

## Queries

### ECO013-PRUNE - Prune now or repair references first

**Context:** The cancellation of [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md) as superseded is sound, and "accepted" isn't open to it because of the failed review and governing audits. However, the harness specification cites it as the evidence of acceptance, three local links point at its path, seven message lines say audit findings "hold its acceptance", and its pilot lessons have no other home. `ki-accept` requires those repairs, committed, before a prune.

**Query:** Should the record be pruned now, or after those references and lessons are repaired?

**Options:**

a) (recommended, confidence high - the prune preflight in `ki-accept` is explicit and the dependent references were verified directly) Keep the record cancelled. First, in ki-principal, repoint the three local links to a pinned `(pruned)` revision, correct the seven AUDIT-FINDINGS lines and `state.md`, and send the lessons as message lines to their owners. Send the harness a `messages.md` line to repoint `harness.md:145`. Then prune in a commit containing only the deletion.

b) Prune now as is, and accept the dangling links, the stale "hold acceptance" lines and a harness evidence line that points at a deleted record, relying on Git history alone.

### 🤖 → 👤 Handoff to supervisor · since 02:59 BST

👤 1 with you

- [with you] ECO013-PRUNE · owner · since 02:59
