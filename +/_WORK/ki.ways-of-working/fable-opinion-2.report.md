# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › fable-opinion-2

**🤖 → 🧑 Handoff to supervisor · Run report at 06:36 BST · last mark 22:34 BST**

---

## Done

This is an advisory opinion for the ways-of-working coordinator. I read the tools-burndown and ki-burndown-2 run reports, the ways-of-working decisions log from PRE-APPROVALS on, the tools-burndown work file and the mgit-review and rig-target-speed reports, and each record named below in its own repository, plus the Git history of tools-ki, tools-mgit and tools-rig. I changed nothing except this report and ran nothing that writes. One commit carries this report.

### How the pre-approvals fit

- [ACCEPT-NIGHT](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md) names two records only, KI-HARNESS-GOV-210 and [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md). It does not, by its letter, cover any record below. What it does give is the method Kris chose for overnight acceptance: an independent review that passes, and any finding leaves the record for Kris.
- FABLE-OPINION ("it can be your approval for now") and KEEP-PUSHING ("tools burned down, you can get through the roadmap as far as you can", "stopping only on reserved items") are what cover the three acceptances and the adoption. Acceptance and adoption are not on the reserved list. Each is a record status change, reversible by an edit, with no release, no prune and no live change behind it.
- So the honest framing is: covered by KEEP-PUSHING and FABLE-OPINION, taken under ACCEPT-NIGHT's condition, logged as provisional for Kris to confirm. Nothing is pruned tonight, so every provisional acceptance can be reopened in the morning by editing the record.
- The ki-accept skill says human approval is the default and is never inferred from a clean gate. Kris's spoken words of 18 October are that approval, provisionally, and the decisions log entry is where the coordinator records it.

### 1. Accepting KI-TOOL-KI-CLI-126 (tools-ki)

**Covered by:** KEEP-PUSHING and FABLE-OPINION, under ACCEPT-NIGHT's condition. Not named by ACCEPT-NIGHT.

**Review:** none yet. [KI-TOOL-KI-CLI-126](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-126-unavailable-store-breaks-repair.md) has been Awaiting review since 16 October with four Verify steps recorded, but no run has reviewed it independently of its author. Run one first.

**Recommendation:** a) (confidence medium - every criterion but one is verified, the code has shipped in v0.10.5 and v0.11.0 and has run daily since, but the one unverified criterion is the one Kris's own CLI126-DELIVER decision named) Launch a short read-only review run on the record against its Requirements and the CI-STORE decision. If it finds nothing, accept provisionally on this opinion, log it, and in the log name the open point: the GitHub-hosted ki-principal CI run on main has not been observed reaching its audit step, because no overnight run has network. Kris confirms in the morning by glancing at ki-principal's latest CI run. Any finding leaves the record for Kris. b) Leave it for Kris, which also leaves -131 and -136 unbuilt tonight.

**Provisional action tonight:** yes, after the review passes. The reason to act on this one and not on the wider ki-accept group is that it gates work: the roadmap audit refuses -131 as an active record while its blocker is not done, so acceptance is the only way to -131 and -136 tonight.

### 2. Accepting KI-TOOL-MGIT-CLI-017 (tools-mgit) and KI-TOOL-RIG-CORE-060 (tools-rig)

**Covered by:** KEEP-PUSHING and FABLE-OPINION, under ACCEPT-NIGHT's condition. Not named by ACCEPT-NIGHT. Both were the next step in the tools-burndown plan before Kris's hold, and the hold was lifted by KEEP-PUSHING.

**Review:** passed for both.

- [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md): the mgit-review run of 17 October gave the verdict "ready for Kris's ki-accept", with no blocking or medium findings and four low ones, now captured as [KI-TOOL-MGIT-CLI-022](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-022-external-member-review-findings.md). The record's one outstanding concern, that the chezmoi-managed consumer manifest must not gain the external member until a release reaches every machine, is a release and chezmoi matter, both reserved, and acceptance does not trigger it.
- [KI-TOOL-RIG-CORE-060](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md): reviewed on 18 October at 30fbebf by a session that had not written it, no findings, recorded in the record. Its one outstanding concern is a note for a future record, not a defect. It is on main and pushed.

**Recommendation:** a) (confidence high - independent review passed on both, no release, live run or chezmoi change follows, and acceptance is reversible by edit) Accept both provisionally on this opinion, commit each acceptance in its own repository by explicit path, push fast-forward, log both as provisional. Do not prune either. b) Leave both for Kris; nothing depends on them tonight, so this costs only morning time.

**Provisional action tonight:** yes, directly, no further review needed.

### 3. Adopting KI-TOOL-MGIT-CLI-018 to -022 out of triage

**Covered by:** FABLE-OPINION, with KEEP-PUSHING for the building. This is the weakest of the four fits. Adopting new work is a selection decision that ki-next reserves to the owner, and Kris has not seen the final record set: it came out of MGIT-PLAN, whose option a) the tools-burndown run took provisionally on my earlier opinion. Against that, -018 and -019 were captured earlier from Kris's own asks and only reworded, -022 holds the findings of a review Kris will confirm with -017, and -021 is a prerequisite of [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md).

**Review:** none applies before adoption. Each record has Goal, Context, Boundary and Discussion only, so each needs ki-plan to Ready before building, and an independent review before any acceptance, which stays with Kris.

**Recommendation:** a) (confidence medium - the shape is twice provisional and changes a tool Kris uses by hand every day, but nothing ships and every build stops at Awaiting review) Adopt all five into Next and plan them to Ready tonight, provisionally on this opinion, recorded in each record's Discussion. Build in this order, each to Awaiting review only, pure Bash, Bats fixtures only, no release: [KI-TOOL-MGIT-CLI-022](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-022-external-member-review-findings.md), [KI-TOOL-MGIT-CLI-021](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-021-estate-overview.md), [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md), [KI-TOOL-MGIT-CLI-019](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-019-pass-through-escape-hatch.md), then [KI-TOOL-MGIT-CLI-020](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-020-safe-parallel-sync.md). Two conditions: -019 keeps -B and --bare as deprecated aliases with a warning rather than removing them, so a provisional build cannot break Kris's hands; and -020 is built only if its tests can run wholly in disposable fixtures, with no mgit sync against the real estate. b) Adopt and build only -022 and -021 tonight, which are the bounded ones with a clear reason, and leave -018, -019 and -020 for Kris's morning. c) Leave all five for Kris.

**Provisional action tonight:** yes for the adoption and planning. For the building, a) with its two conditions, or b) if the coordinator wants the narrower footprint.

### Other tools-burndown rows that can still move tonight without Kris

- [KI-TOOL-KI-CLI-131](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-131-host-absent-store-state.md) then [KI-TOOL-KI-CLI-136](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-136-errors-suggest-fixes.md), once -126 is accepted. -131 is planned and only needs setting Ready unchanged. Both to Awaiting review, isolated HOME and XDG fixtures, no change on vega or either Mac.
- [KI-TOOL-KI-CLI-147](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-147-agent-state-folder-tooling.md), agent state-folder tooling, split out of -137 tonight. Internal to ki agent, low risk. Adopt and plan provisionally, build to Awaiting review.
- [KI-TOOL-KI-CLI-146](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-146-ki-quiet-setting.md), the KI_QUIET setting Kris asked for under KI-QUIET. Adopt and plan provisionally, build to Awaiting review. Lower value than -131 and -136.
- Independent review runs, read-only, over the Awaiting-review records so that Kris's morning ki-accept sitting is short: in tools-ki -123, -130, -133, -135, -137, -138, -141, -142, -143 and -144; in tools-rig -042, -047, -052, -054, -055 and -058. A review needs no approval at all. I do not recommend accepting these on an opinion: nothing depends on them, and ACCEPT-NIGHT's naming of two records is a signal that Kris wanted to see the rest.
- [KI-TOOL-RIG-CORE-061](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-061-removal-lock-diagnostics.md), captured at 06:32 with the lock work, can be planned provisionally if a Rig agent has nothing else.

Not buildable tonight, so the coordinator need not look again: -134's grant texts wait on KI-HARNESS-GOV-201; -139's citations wait on another territory's decisions move; -140 waits on -021 and KI-HARNESS-GOV-203, which is in Kris's HARNESS-ACCEPT sitting; -145 waits on KI-HARNESS-GOV-199; KI-TOOL-RIG-CLI-026, KI-TOOL-RIG-CORE-048 and KI-TOOL-RIG-DIST-011 are held by Kris; v0.11.1 is TOOLS-RELEASE, left for Kris.

One caution for the tools-ki rows: the installed ki runs from the tools-ki primary checkout, so every agent on this Mac runs whatever is on main. Chain the tools-ki runs one at a time, commit only green states, and keep the agent commands out of the diff where the record allows.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- For Kris's morning, on top of the existing provisional list: the three acceptances, the five mgit adoptions and any -146, -147 or -061 adoption, each logged as provisional on this opinion by the coordinator if taken.
- The ki-principal CI run on main, to close -126's one unobserved criterion.

## Queries

No outstanding queries.

### 🤖 → 🧑 Handoff to supervisor · since 06:36 BST

🧑 0 with you · 🏁 run finished

- [committed] fable-opinion-2 report in ki-principal, pushed
