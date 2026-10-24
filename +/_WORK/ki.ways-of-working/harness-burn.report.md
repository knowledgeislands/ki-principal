# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › harness-burn

**🤖 → 👤 Handoff to supervisor · Run report at 08:48 BST · last mark 08:48 BST**

---

## Done

- **Classified all 25 open harness records** (table below). Only two could be worked without an owner decision.
- **[KI-HARNESS-GOV-170](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-170-keep-resolution-targets-local.md) delivered and awaiting review, on local `main`:** Ready in `e66f3130`, delivered in `4a10ba07`. A `resolution_target` must now name a record in the same repository. Another repository's work is described in plain words under `## Cancelled`. A `superseded` or `duplicate` record may leave the target out. The checks:
  - `bun run test`: 1,372 pass.
  - `bunx tsc --noEmit`: passes.
  - Isolated-home audits of `ki-work-roadmap`, `ki-accept`, `ki-skills` and `ki-authoring`: no FAIL.
  - `ki-work-roadmap` rubric regeneration: no diff.
  - Pre-commit hooks: passed on both commits.
  - The worktree was removed and the branch deleted.
- **Handoff line in [ki.ways-of-working messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md), ki-principal `53184b64`:** tagged TOOLS-KI-RESOLUTION-LOCAL, for routing to ki.tools-burndown. tools-ki's `src/core/work/items.ts` still rejects a targeted resolution that has no target, so it needs the matching change. No record in the estate cites a target in another repository, so the new failure breaks nothing today.
- **[KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md) not delivered:** it stopped at planning and needs an owner decision (query GOV209-OWNER below). Nothing was written for it.
- **Stopped at 08:47 BST,** about an hour early: no workable record was left.
- **Nothing pushed:**
  - ki-agentic-harness `main` is 32 commits ahead of its upstream. Two are mine; the rest are other sessions' stacked commits.
  - ki-principal is 83 ahead, with one of them mine.

### Classification

| Class | Records |
| --- | --- |
| Accepted, not pruned | [KI-HARNESS-GOV-196](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-196-scratch-output-in-temp.md) (cancelled), [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md), [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md), [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md), [KI-HARNESS-GOV-214](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md), [KI-HARNESS-GOV-215](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-215-pmo-12-to-fail.md), [KI-HARNESS-GOV-216](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-216-three-part-updates.md) (cancelled), [KI-HARNESS-GOV-220](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-220-coord-1-undeclared-warn-level.md), [KI-HARNESS-GOV-221](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-221-ki-diagrams-mermaid-fence-warning.md), [KI-HARNESS-GOV-222](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) (cancelled), [KI-HARNESS-GOV-223](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-223-island-maturity-declaration.md), [KI-HARNESS-GOV-226](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-226-banner-rendered-glyphs.md) (cancelled) |
| Needs Kris | [KI-HARNESS-GOV-219](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-219-feedback-work-folder-kind.md) and [KI-HARNESS-GOV-224](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md) (awaiting acceptance), [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) (close-out), [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) (open questions), [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) (triage, needs adoption), [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md) (schema), [KI-HARNESS-OPS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md) (needs splitting), [KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md) (scaffold ownership) |
| Blocked on another repository or a date | [KI-HARNESS-GOV-204](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-204-pretooluse-quietening-hook.md) (evidence review on 24 October), [KI-HARNESS-GOV-228](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-228-home-work-spec.md), [KI-HARNESS-GOV-229](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-229-home-acquire-spec.md) and [KI-HARNESS-GOV-230](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-230-knowledge-package-skill.md) (waiting on SPEC-TEXT in ki.portable-specifications; GOV-228 also on the ENTRY-NAMES rename) |
| Workable now | [KI-HARNESS-GOV-170](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-170-keep-resolution-targets-local.md) (delivered in this run) |

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The tools-ki change for TOOLS-KI-RESOLUTION-LOCAL is waiting in the ki.ways-of-working message queue, to be routed to ki.tools-burndown.
- The twelve accepted records in the table are waiting for pruning.
- [ki.ways-of-working queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/queries.md) has an uncommitted change from another session. I left it alone.

## Queries

### ACCEPT - harness records awaiting acceptance

**Context:** Three harness records are awaiting review:

- [KI-HARNESS-GOV-219](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-219-feedback-work-folder-kind.md) and [KI-HARNESS-GOV-224](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md) were delivered before this run.
- [KI-HARNESS-GOV-170](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-170-keep-resolution-targets-local.md) was delivered in this run.

I moved GOV-170 out of Future on the authority of OVERNIGHT-BURNDOWN, your direction of 20 October about 05:20 BST. Each record has a review packet.

**Query:** Should these three go to independent review and then acceptance?

**Options:**
a) (recommended, confidence medium - each has a full review packet and passing checks, but none has had an independent review yet) Run an independent review of each, oldest first, then accept those that pass.
b) Review GOV-170 only, and leave the other two for their own works.

### GOV209-OWNER - who owns the acquired-area scaffold

**Context:**

- Under the repository rule, a capability that owns a working-area subarea must require its exact README while it is declared, and it restores that README through its own conform.
- [KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md) needs a `+/_ACQUIRED/README.md` scaffold in each territory principal, but it does not say which skill owns it.
- `ki-repo-kb` would put it in every knowledge base, not only principals. `ki-repo-kb-principal` has no scaffold writes today.
- Under either owner, the eight principals that declare the overlay would fail audit until each one is conformed. None of them has the folder yet.
- Acquire's dispatch guide already creates the folder on first delivery.

**Query:** Which skill should own the scaffold, and should it be required in every principal or checked only once the folder exists?

**Options:**
a) (recommended, confidence low - it matches who receives deliveries, but brings eight audit failures until each principal is conformed) Give it to `ki-repo-kb-principal` and require it while the overlay is declared, adding conform support. Put the receiver triage guidance in `ki-repo-kb`.
b) Check the scaffold only once `+/_ACQUIRED/` exists, which means amending the ki-repo rule on specialist subareas.
c) Give it to `ki-repo-kb` for every knowledge base.

### GOV225-CLOSE - close the hook content-claims record

**Context:** [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) has every step done except agreeing with you whether it now closes. Composition is left to KI-TOOL-KI-CLI-165 in tools-ki.

**Query:** Should GOV-225 close now, with composition left to tools-ki?

**Options:**
a) (recommended, confidence medium - all the harness-side steps are done) Move it to awaiting review for acceptance.
b) Keep it open until KI-TOOL-KI-CLI-165 lands.

### GOV189-SCOPE - moving a thread between hosts

**Context:**

- [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) still has two open questions: host-bound agents, and the closing form on the old host.
- Its level check and the `[behind]` marker were already decided under SYNC-GUARD.
- Queue export has a manual route today.

**Query:** Should GOV-189 be narrowed to the decided slice, or wait for your answers to both questions?

**Options:**
a) (recommended, confidence low - the decided slice could be delivered now, but narrowing changes the record's scope) Narrow it to the level check and `[behind]`, and keep the two questions in its Discussion.
b) Answer both questions so the whole record can be planned.

### GOV202-ADOPT - stats badge for skill areas

**Context:** [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) is still in triage, and nobody has adopted it.

**Query:** Should GOV-202 be adopted?

**Options:**
a) (recommended, confidence low - it is small, but I have not judged its value) Adopt it to Next for a later burndown.
b) Cancel it.

### GOV227-SCHEMA - repository storage declarations

**Context:** [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md) needs its schema designed with you before it can be planned.

**Query:** When should the schema be designed?

**Options:**
a) (recommended, confidence medium - the record names you as co-designer) Hold a short design session in its own work.
b) Defer it to Future.

### OPS009-SPLIT - complete AI session acquisition

**Context:**

- [KI-HARNESS-OPS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md) is large and touches sibling repositories.
- It would need splitting into new records, and CAPTURE-GATE stopped this run from creating any.

**Query:** Should OPS-009 be split?

**Options:**
a) (recommended, confidence medium - the record is too large to deliver as one) Split it in a session that is allowed to capture records, with each repository's part captured by that repository.
b) Leave it whole at its current horizon.
