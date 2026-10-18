# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-feedback-plan

**🤖 → 🧑 Handoff to supervisor · Run report at 18:17 BST · last mark 02:27 BST**

---

## Done

- Captured unit 3 as [KI-OBSERVA-BRG-002](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-002-capture-feedback.md), Capture feedback, adopted it to Now under OBS-SLICE and shaped it with an embedded Mermaid model. It is chained behind [KI-OBSERVA-VIS-024](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-024-review-queue.md) by sequencing, as VIS-024 was behind VIS-023.
- The plan: comment on any block of a document read in the Documents, Knowledge Bases or Work Instruments. Each document has one draft, kept in the Observatory's state and never in a repository. One `feedback.send` operation, confirmed with a shown plan, writes `+/_WORK/<id>/feedback/<date>-<slug>.md` and one `## Messages` line into the work that produced the document. It commits only those two paths, with hooks run, and keeps a receipt. Pushing stays with the governed push.
- The plan settles OBS-REVIEW-OPEN. Review-queue rows for work-folder reports open read-only in a report reader built on the Work Instrument's report rendering. The Knowledge Bases and Documents Instruments keep refusing `+/`, intake rows still show only a path, and captures never open.
- Live-artifact consolidation is out of scope and named as a follow-on in the record's Discussion, quoting your words.
- Captured [KI-OBSERVA-OPS-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-003-observatory-serving-location.md), Observatory serving location, as unadopted triage. It covers where the service is served from and live reload.
- Commits: `d00a64f` reserves the two numbers, `81e7fb0` captures the serving record, `d8cd581` captures Capture feedback, and `8868339` adopts and shapes it. All four are pushed fast-forward to `origin/main`, which is level.
- Checks: rumdl is clean. `ki repo audit` adds no finding; its one failure is the existing title of KI-OBSERVA-VIS-022.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- KI-OBSERVA-BRG-002 stays at `draft`. Under ki-plan, a record becomes Ready only after the plan is approved, so OBS-FEEDBACK-PLAN is that approval.
- The Project note's line for unit 3 still sends feedback to the capture landing. The Observatory work should reword it once OBS-FEEDBACK-HOME is answered.
- I wrote this report only to the state folder, as the progress protocol requires. Homing it into `+/_WORK/ki.observatory/` is the launcher's job.
- No service restart is due, because no code changed.

## Queries

### OBS-FEEDBACK-PLAN - Approve the Capture feedback plan

**Context:** [KI-OBSERVA-BRG-002](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-002-capture-feedback.md) is shaped, with Steps, Files touched, a Verify section that never sends to a real work folder, and one detached delivery run. Approval sets it to Ready and lets that run deliver it. The two forks are OBS-FEEDBACK-HOME and OBS-FEEDBACK-PUSH below, and the plan takes option a) of each. **Query:** Do you approve the plan so the record can be set to Ready? **Options:** a) (recommended, confidence medium - the design reuses the existing Bridge gate and Messages channel, but nobody has tried commenting in the running service yet) approve it as written and set KI-OBSERVA-BRG-002 to Ready b) approve it with changes you name, and the record is reshaped before Ready c) keep it in draft until you have used the Review queue and Work Instrument in the running service

### OBS-FEEDBACK-HOME - Where the feedback package lands

**Context:** The work model reads a work's `## Messages` section at its next pick-up, so feedback reaches the agent there. A Messages line is about 60 words at most and links its detail, so the package needs a file. The ki-work-folder closed list has no feedback kind, and it names coordinating work, not the owner through the Observatory, as the Messages sender. The Project note first said the territory's capture landing, which Knowledge acquisition decides. **Query:** Where should the consolidated package be written? **Options:** a) (recommended, confidence medium - it matches your words "give that back ... to the agent", but needs a harness change first) in the producing work's folder as `feedback/<date>-<slug>.md`, with the Messages line linking to it. The Observatory work asks the harness owner to add the kind and the owner as a sender before delivery lands. b) in the territory's capture landing, with the Messages line linking to it. This needs no work-folder change, but feedback for an agent then goes through Stage and Harvest like captured knowledge. c) in the Messages line alone, with the comments inlined. This needs no new file, but a line is too short for a consolidated review.

### OBS-FEEDBACK-PUSH - Whether sending feedback also pushes

**Context:** Under the plan, `feedback.send` is a `mutate` operation that commits two paths. The Repositories Instrument's push is `destructive` and needs the repository named back. Until a push, a work picked up on another host does not see the feedback. **Query:** Should sending feedback stop at the commit? **Options:** a) (recommended, confidence high - it keeps the write reversible and leaves one way for anything to leave the machine) stop at the commit, and end the receipt with a pointer to the governed push b) push as part of `feedback.send`, making it `destructive` and pushing anything else unpushed on that branch

### 🤖 → 🧑 Handoff to supervisor · since 18:17 BST

🧑 3 with you

- [with you] OBS-FEEDBACK-PLAN · owner · since 18:17
- [with you] OBS-FEEDBACK-HOME · owner · since 18:17
- [with you] OBS-FEEDBACK-PUSH · owner · since 18:17
- [committed] roadmap records, pushed
