# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › finish-first

**🤖 → 👤 Handoff to supervisor · Run report at 02:53 BST · last mark 02:01 BST**

---

## Done

- Measured 50 roadmap repositories from Git at daily points, 6 to 20 October: the estate's open count went from 198 to 330 between 13 and 20 October (+67%). Over that week 370 records were created and 212 closed; triage went from 30 to 106 and awaiting-review from 13 to 55.
- Traced where the week's 370 new records came from: 102 from handoffs and sweeps, 97 opened for delivery, 85 citing a Kris answer, 55 other captures, 22 run findings and 9 splits or merges. Five commits created 56 of them.
- 27 records were created after CAPTURE-GATE; 21 came from the ki.baseline-rollout sweep under a blanket approval or from Kris answers that the captures cite.
- Wrote [finish-first.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/finish-first.md): the measurements, seven causes of growth, rules R1-R8 (each with its owning standard or tool and its check) and six queries. Committed locally as `aca2c01b` in ki-principal by explicit path. The repository audit and commitlint passed; the first commit attempt failed commitlint on body line length and was re-wrapped.
- Claim-check: corrected the post-gate count from 24 to 27, the choreography wording (five repositories' AGENTS.md carry a choreography section, not seven) and the split example (tools-rig `1eac12d`). The note contains no en-dashes or em-dashes.
- Limitation: the measurement scripts were temporary and are not kept. The note gives the method so the figures can be recomputed from Git; there is still no `ki repo roadmap` history or snapshot command.
- ki-principal `main` is six commits ahead of origin: five are other sessions' commits, already stacked, and the sixth is `aca2c01b`. Nothing was pushed.

## In Progress

Nothing is running.

Outstanding - no action requested now

- All six queries are medium confidence, so under BLIND-REVIEW they need one blind review run before they reach Kris; this is for the coordinator to launch.
- CAPTURE-GATE is still not written into any harness skill, and HOMELESS-STANDING remains queued to home it in `ki-next` and `ki-delegation`. CAPTURE-ORIGIN below would widen that work.
- R4 and OWNER-QUEUE overlap: both feed wow-standards, so WIP-CAP's answer should be folded into the OWNER-QUEUE audit work rather than run separately.

## Queries

### NET-DOWN - A weekly direction target, not a cap

**Context:** ROADMAP-CAP (19 October) set no roadmap cap and no weekly cap measure. On 20 October Kris asked to "see roadmaps going down". A weekly target asks each repository's open count to fall week on week; it is a direction measure, not a limit on size, but it reopens part of ROADMAP-CAP.

**Query:** Should each repository's open count be expected to fall week on week, with a burn query when it does not?

**Options:** a) (recommended, confidence medium - it answers "going down" without a size cap, but it narrows ROADMAP-CAP's "no weekly measure") Show the week-on-week change per repository at every State of play mark (R8); a repository that grew over the week gets one burn query from its owning work; no adoption block. b) Show the counts only, with no target or burn query. c) A hard rule: no adoption to Now in a repository whose open count grew over the past week.

### WIP-CAP - The per-work cap and what it counts

**Context:** FINISH-FIRST's read-back caps a work's Now and awaiting-review counts; OWNER-QUEUE warns over about eight awaiting acceptance and open queries per work. The roadmap standard says of Now, "there is no cap", so R4 amends it. Today apps-observatory.local alone holds 9 awaiting-review records and 11 at Now or awaiting review.

**Query:** What should the per-work cap count, and at what number?

**Options:** a) (recommended, confidence medium - one number is easier to see and check, and eight matches OWNER-QUEUE) One count per work, records at Now plus awaiting-review plus open queries, capped at eight; over it the work only accepts, cancels, merges, prunes, finishes in-progress work and fixes blockers (R4). b) Two caps: at most three records in progress per work, and OWNER-QUEUE's eight for awaiting-review and open queries. c) No cap; the banner shows the count only.

### CAPTURE-ORIGIN - Home CAPTURE-GATE with an origin field

**Context:** CAPTURE-GATE is in briefs only; `ki-next` still captures "without prior approval", and 27 records were created after the gate. R1 writes the gate into `ki-next`, `ki-work-roadmap` and `ki-delegation`, drops the "must survive the session" limb for capture, and adds `origin` and `origin_ref` so the rubric can check it. The field changes the work-item format and the `tools-ki` model.

**Query:** Should CAPTURE-GATE become a standard rule with a checked `origin` field?

**Options:** a) (recommended, confidence medium - a field makes the gate checkable, but it is a format change across `ki-work-roadmap` and `tools-ki`) Write R1 into the standards with `origin: blocker | defect | owner` and `origin_ref`, the rubric warning on new triage without them. b) Write the rule as prose in `ki-next` and `ki-delegation` only, with no field and no rubric check.

### HANDOFF-AS-MESSAGE - Handoffs and sweeps stop creating records in each repository

**Context:** 102 of the week's new records came from handoffs and sweeps, such as one Archify redraw in seven repositories and one design handoff as 33 records across two. R2 makes a sweep one record in its owning repository and a handoff a `messages.md` line. The cross-repository choreography sections in five repositories' AGENTS.md, which let seven repositories add handoff items to one another's roadmaps, would change.

**Query:** Should a sweep be one record in its owning repository, and a handoff a message rather than a record?

**Options:** a) (recommended, confidence medium - it removes the largest source of growth, but five choreography sections change and the receiver loses a record it can see in its own roadmap) Adopt R2: one record per sweep in the owning repository, handoffs as `messages.md` lines, one record per product for a design handoff. b) Keep handoff records, but at most one per receiving repository per sweep, its steps inside it.

### STALE-SWEEP - Re-decide drafts untouched for 30 days

**Context:** 39 Future drafts have a median of 51 days since update; er-agentic-harness holds 21 of them, untouched in the fortnight. R7 brings one cancel-or-keep query per repository each week, recommending cancel as `obsolete` with the idea kept as a Project note bullet.

**Query:** Should drafts at Future, Soon or Hold untouched for 30 days come to Kris weekly as one cancel-or-keep query per repository?

**Options:** a) (recommended, confidence medium - it gives the count a floor that falls, though the first round is large) Yes, at 30 days, recommending cancel with the idea kept. b) Yes, at 60 days. c) No sweep; records stay until a lane chooses to review them.

### ACCEPT-BUNDLE - One acceptance answer per work

**Context:** 55 records await Kris's acceptance, up from 1 on 6 October. `ki-accept` already counts "a standing human grant ... quoted with its source" that "covers the exact record". R5 brings every awaiting-review record of a work in one ACCEPT query that Kris answers once.

**Query:** May each work bring its awaiting-review records as one ACCEPT query, answered in one word, as the approval for the exact records listed?

**Options:** a) (recommended, confidence medium - it fits `ki-accept`'s standing-grant rule and clears the largest queue, but Kris reviews a list rather than each packet) Yes, one ACCEPT query per work at each handoff, oldest first, each line with outcome and concern, the answer quoted with the record list in the decisions log. b) Keep one acceptance per record.

### 🤖 → 👤 Handoff to supervisor · since 02:53 BST

👤 6 with you

- [with you] NET-DOWN · owner · since 02:53
- [with you] WIP-CAP · owner · since 02:53
- [with you] CAPTURE-ORIGIN · owner · since 02:53
- [with you] HANDOFF-AS-MESSAGE · owner · since 02:53
- [with you] STALE-SWEEP · owner · since 02:53
- [with you] ACCEPT-BUNDLE · owner · since 02:53
- [committed] finish-first design note
- [unpushed] ki-principal main
