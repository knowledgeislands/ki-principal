# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › work-package-merge

**🤖 → 👤 Handoff to supervisor · Run report at 12:45 BST · last mark 12:04 BST**

---

## Done

- Stocktake headline: the 11 live work files run from 103 to 1,577 words (about 440 on average). Into `work.md` go run evidence (commit SHAs, test counts, hashes), dated logs in `Next steps` (4 of 11), open query tags whose text sits elsewhere or nowhere (6 of 11), stale Messages (the 18 October MIGRATED line in 5), and a `Parked` section holding five kinds of thing. None of them says what the work is for or what it takes.
- Codex review: the package model and the definition/state split fit Kris's intent, but the migration is not yet safe for running sessions. Main material change: readers and writers must be upgraded and quiesced before any folder splits. It also differs on the name (use "work package" for the concept) and calls five compulsory files overbuilt.
- Fable review: the model is right and close to Kris's words, keep "work folder", but the migration is unsafe as written. Main material change: a session that has been sent to Kris still holds the old shape in memory and would rewrite a folder migrated from outside, so the outside run may touch only held work that has no session. It also differs on the description shape (ids in Scope only) and names three gaps: parked tangents, the turn budget and the territory queue.
- The design note is amended where both reviews agreed: readers accept both shapes first, one authoritative copy per kind, no outside migration while a session is live, lost query tags raised rather than dropped, and a routed unit returned only once. Commit 48a56fbf in ki-principal, by explicit path. Repository audit passed with no failures. Not pushed: `main` is now 25 commits ahead, including other sessions' commits stacked beneath, so you decide the push.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Single-reviewer points that implementation can settle without a decision unless you object. Fable: `state.md` repeats `id`, `ki.regular` gains a `decisions.md`, and "more than eight open queries" moves to the `ki-coordination` rubric. Codex: no fixed count of two to four goals, and the 150-token register figure gets measured.
- Stocktake drift since 12:20 BST, not corrected in the note because only one reviewer reported each item. `ki.observatory` has moved on. `ki.timelines` also lacks a `mark` field. `ki.chezmoi` has eight 18 October lines, not seven. `ki.baseline-rollout` holds WAVE-1's proposed scope; only its query block is missing.
- Another session's uncommitted files in `+/_WORK/ki.chezmoi/` were left untouched.

## Queries

### PACKAGE-NAME - What to call the packaged folder

**Context:** You asked whether work folders are "work packages". The name "work folder", with its skill `ki-work-folder`, was settled on 18 October, and the clean-up after that rename is still going on. In project management a work package is the smallest deliverable in a breakdown. In this model that is the work item, the one level that has no folder. The reviews split: Fable agrees with the design, and Codex would use the word for the idea without renaming anything.

**Query:** Keep "work folder", or use "work package" for the idea?

**Options:**

a) (recommended, confidence medium - the clash with the project-management meaning and the rename cost are concrete; held by the design and Fable) Keep "work folder" and `ki-work-folder`, describe the shape as "packaged like a skill", and call `work.md` the "definition" in the Work Process Words table.

b) (Codex) Define "work package" once as the name of the idea, and keep the folder and skill names as they are.

c) Rename the idea and the skill to "work package", keeping the path; this is one more rename across the harness, `ki`, chezmoi and configuration.

### STATE-FILE - Where the moving state fields live

**Context:** Today `work.md` holds both what the work is and where it stands, and its front matter (state, target, hold, mark and so on) changes at every move. `ki work status` reads those fields from `work.md` alone. The design moves them, with the "now, next steps, held" prose, into a new `state.md`. `work.md` then becomes a short definition that rarely changes, and Git history separates "what this work is" from "what happened to it". Both reviews agree, provided the `ki work status` reader changes first. That condition is now in the note.

**Query:** Should the state fields and state prose move together into `state.md`?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Move the state fields to `state.md` front matter, with `## Now`, `## Next steps` and `## Held`, once the reader accepts both shapes. Fable also adds `## Queue` for territory work, whose ordered Project queue does not fit a five-line `## Now`.

b) Keep the state fields in `work.md` and move only the prose; no reader change, but `work.md` still changes at every move.

### FILES-AT-CREATION - Whether every work starts with all five files

**Context:** The design creates `work.md`, `state.md`, `queries.md`, `messages.md` and `decisions.md` with every work, the last three saying `None`. That way no reader meets a missing file and no sender ever creates one. Codex calls this overbuilt for small work: `ki.regular` is 103 words and has no decisions log at all. Codex would create the detail files only when first needed. Fable accepted the five files.

**Query:** Are all five files required from creation?

**Options:**

a) (recommended, confidence medium - an empty file costs one line, while optional files make every reader, sender and rubric check handle absence; held by the design, not contested by Fable) Require all five at creation.

b) (Codex) Require `work.md` and `state.md` only; create `queries.md`, `messages.md` and `decisions.md` when first written.

### QUERIES-FILE - A queries file beside the decisions file

**Context:** You asked for "a Q one, like the decisions one". In 6 of the 11 live works, open queries appear only as tags. Their text sits in run reports, in reports outside the repository, in a design note or only in the last Summary. `ki.chezmoi` keeps 12 of its 25 reports alive only because they hold queries. The design gives every open and parked query its full text in `queries.md`, copied in when a report arrives. The owner report's Queries section is rendered from that file. An answered query is deleted in the same commit that records your answer.

**Query:** Should `queries.md` hold every open and parked query in full?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes. Each block keeps its tag and source. Reports can then be pruned once their outcome has a home.

b) Make `queries.md` an index of tags pointing at reports; less copying, but reports stay alive for their queries.

### PARKED-HOME - Where parked items go

**Context:** Today's `Parked` sections mix five things: parked queries, work waiting on a condition, to-do lists for a particular screen, ideas, and items already resolved. Your read-back said "parked items in their own files". The design splits them by kind instead of making a `parked.md`, which would keep the mix. Both reviews agree. Fable notes a gap: a side topic you park before it has become a query has no home. Codex adds that every held item needs its release condition.

**Query:** Should `Parked` be split by kind rather than given its own file?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Split it. Parked queries and parked side topics go to `queries.md` `## Parked`. Held work goes to `state.md` `## Held`, each with its release condition. Ideas go to the Project note or a record. Resolved items are deleted, and there is no `parked.md`.

b) One `parked.md` for everything parked, as the read-back said.

### MESSAGES-FILE - Where the inbox lives

**Context:** Other works and State of play write their messages into the same `work.md` that its own session rewrites at every move. Stale lines pile up: eight from 18 October in `ki.chezmoi`, and the MIGRATED line in five works. The design gives each work its own `messages.md`. Appending a line there is the only write another work may make in the folder, which a check can then verify by path. Both reviews agree.

**Query:** Should the inbox move to its own `messages.md`?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes. Senders may only append a line or replace their own unread line (Fable). Appends and removals happen one at a time, and the receiver records where a line went before removing it (Codex).

b) Keep a `## Messages` section, moved into `state.md`.

### DESCRIPTION-SHAPE - The routing description

**Context:** State of play now routes new work to existing works, but no work says what it takes. Like a skill's description, the design adds a required `description` to `work.md` of up to 500 characters: what the work does, "Takes ...", and "Not for ..." naming neighbouring works by id. Below it, a `## Scope` section gives `In:` and `Out:` lines by id. Routing reads only the descriptions unless two of them match. Codex agrees, with 500 as guidance and a test against ambiguous examples. Fable sees two statements of one boundary that will drift. It would keep ids in Scope only and make the description about 300 characters of plain prose.

**Query:** Should the description name neighbouring works, or leave that to Scope?

**Options:**

a) (recommended, confidence medium - routing reads only the descriptions first, so the exclusions have to be there to decide most cases without opening a folder; held by the design and Codex) A description of up to 500 characters with "Takes ... Not for ..." naming neighbours by id, plus `## Scope`, tested against a handful of ambiguous routing examples.

b) (Fable) A description of about 300 characters in plain prose with no ids; `## Scope` alone names neighbours, and the rubric checks every id resolves.

c) Route on the Project note's `outcome` alone, which leaves regular and territory work uncovered.

### ROUTE-RECEIPT - What a work must do with routed work

**Context:** You said that if State of play decides a piece of work is yours, "you have to accept it". The design reads this as: the receiving work must deal with every routed line at its next start-up or owner message and record one outcome. That outcome is a next step, a query to you, or a return to State of play with a reason. Routing gives no permission to do anything its existing decisions do not cover. Paused work keeps the line waiting without waking. Work already owned does not pass through State of play. Both reviews agree, and both added that a disputed unit should not bounce back and forth. That is now in the note: a unit is returned once, then goes to you.

**Query:** Is receipt compulsory, with a recorded outcome and no new authority?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes, as above. The outcome is named in the commit that removes the line (Fable). State of play shows lines nobody has picked up (Codex).

b) Deal with routed lines only at the next mark; less interruption, slower routing.

### REFRESH-TARGET - How method changes reach each work

**Context:** When the method changes, each live work must re-read it. Only 3 of the 11 works record which revision they last read, so nobody can tell who is behind. The design adds a `method_read` field. After a change it sends one dated REFRESH line only to the works that are behind and affected. Updating the field is the confirmation, held work is not woken, and the start-up check stays as a fallback. Both reviews agree on this direction. Codex asks for two things to be pinned down first: exactly which guidance the revision vouches for, and that merging several pending notices never loses an unread one.

**Query:** Should refresh be targeted through `method_read`?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes, with Codex's two conditions written in: one revision covers `ki-coordination` and `ki-work-folder` in the harness checkout, and a merged notice keeps every pending effect.

b) Broadcast every change to every live work and ask each to acknowledge in one line.

### INBOX-CHECK - Whether a coordinator checks its inbox at each wake

**Context:** You asked whether a work refreshes itself, so that routed work gets picked up. Today nothing prompts that except its next start-up or a message from you. A coordinator only wakes every five minutes while it has runs going. Once it has sent the work to you, or the work is on hold, it does not wake at all, and most live works are in that state now. The note covers start-up and the next safe point, not the wake. Neither review proposed this rule. Codex raised the adjacent gap: being routable does not mean a session is alive, so unattended inboxes need showing and a way to resume or escalate. With `messages.md`, the check is one cheap comparison of that file's last commit, and of the method revision, against the last read.

**Query:** Should each five-minute wake check for new messages and method changes?

**Options:**

a) (recommended, confidence medium - it costs one comparison per wake and closes the gap for busy works, while Codex's escalation covers idle ones without new wake-ups) At each wake, check whether `messages.md` (today the work file) or the method changed since the last read. Act at once on a new line, under ROUTE-RECEIPT and without stopping running work. Re-read the standard and the work's own files when either changed. For works not waking (sent to you or on hold), State of play shows how old their unread lines are and gives you the resume line.

b) As a), and also keep a light inbox-only wake, every 15 minutes, while the work is with you; this reverses today's "no heartbeat otherwise" and costs tokens in every idle session.

c) No standing rule; works pick up messages at start-up or your next message, as today.

### PICKUP-READS - Keeping a coordinator's reads small

**Context:** A coordinator's turn is limited to five tool calls. Its reads are limited to the work file, `ki agent status`, one report and one short file. Under the package, picking up a work means reading four small files, and a send writes three. Fable says the budget must be rewritten, or the five calls are spent before the first launch. Codex says reading every decision and query at each owner message brings back the context burden, and would read only what changed after start-up. The two points fit together.

**Query:** Should the turn budget and reading rule change for the package?

**Options:**

a) (recommended, confidence medium - both reviewers raise the same burden with compatible fixes) One read of a folder's pick-up files counts as one call (Fable). After start-up, the coordinator reads only what changed since its last read, plus the entries that bear on the question (Codex).

b) Keep the budget as written and accept fewer launches per turn.

### STATE-HISTORY - Where "what happened since the mark" goes

**Context:** Four works use `Next steps` as a running log, because a Summary needs "what happened since the mark" and nowhere else holds it. The design bans dated log lines, commit SHAs and test counts from `state.md`, and adds a check that warns on them. Fable says the replacement must be named, or the log simply moves into `## Now`: the recap reads Git history for the folder and the run reports. Codex calls the ban overbuilt. It would warn on bulk and history while allowing evidence links.

**Query:** How is history kept out of `state.md`?

**Options:**

a) (recommended, confidence medium - the two reviews address different halves of one rule and do not conflict) State that the recap reads `git log` of the folder and the run reports, and that `## Now` holds the present only (Fable). The check warns on bulk history, not on a single link to a report or commit (Codex).

b) The design as written: a pattern check on dates, SHAs and test counts, with no stated recap source.

### STEWARD-HOME - Who carries method changes after Ways of working closes

**Context:** You decided that Ways of working goes away once the method is defined and that State of play takes its stewardship. State of play does no work itself, so accepted improvements still need someone to carry them out. Nobody knows yet how much the method will change after it settles.

**Query:** How should State of play get method improvements done after Ways of working closes?

**Options:**

a) (recommended, confidence medium - reviewed: Codex and Fable agree; lifted from low) State of play keeps a method backlog and sends each accepted improvement out as small regular work, or into the Project it most affects, with design reviews for changes of shape. Lasting method authority stays in the skills and decision records.

b) A standing regular work for method upkeep under an Activity note, set up only if the volume shows it is needed.

### MIGRATE-PATH - How the live folders move to the new shape

**Context:** Eleven live folders must move. Only a folder's own session may write in it, and a session that has sent its work to you still holds the old shape in memory. Both reviews found the design's order unsafe. The note now says that readers and checks accept both shapes first, and that each folder has one authoritative copy of each kind at a time. Live folders migrate from their own session; the outside run touches only held work with no session; lost query tags are raised, never dropped. On when the window closes, the reviews add complementary points. Codex: count review-held and old-shape folders too, and set pilot exit checks. Fable: write State of play's own description first, and send a nudge if a folder has not moved in seven days, because `ki` and `ki.regular.registry-removal` have not marked in four and five days.

**Query:** Should migration follow the amended path, with both reviewers' window rules?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree; their safeguards are now in the note) Readers and checks first. Pilot `ki.ways-of-working` and `ki.regular.registry-removal` with stated exit checks, after writing State of play's description. Each live work migrates at its own next mark, with a nudge after seven days. Held work moves by one approved run. The window closes on an inventory covering live, review-held and old-shape folders.

b) After the pilot, one approved sweep of all eleven, only once every writer is confirmed idle and you approve the exact set.

### FIELDS-MIGRATE-ORDER - Which repository the field migration starts in

**Context:** The new work-record fields (priority, size, kind and the retired horizons) need a migration run in each repository, each approved by you. Personal-principal holds 22 of the 49 retired horizons and both ways of classifying a record. Kind and size can be proposed now in knowledge-base repositories, but must wait for the next `ki` release in code repositories. The two views differ on where to start. The coordinator, following the fields-follow-up run, would pilot personal-principal, clearing the most debt and testing kind and size proposals. Codex, in query-review-2, would first run a bounded mechanical pilot on apps-markhowarth.com's four records, all with retired horizons.

**Query:** Should the field migration start with a small pilot or with personal-principal?

**Options:**

a) (recommended, confidence medium - a four-record run tests the run's shape cheaply before the largest one, at the cost of one extra approval; held by Codex) apps-markhowarth.com first as a mechanical pilot. Then personal-principal, hnr-principal, 5g-emerge-phase2 and legal-principal. Then the remaining retired horizons, and kind and size in code repositories after the `ki` release.

b) (coordinator) personal-principal first as the pilot, with all fixes plus kind and size proposals. Then hnr-principal, legal-principal, tmx-principal, er-principal and va-principal. Then the mechanical-only runs.

### 🤖 → 👤 Handoff to supervisor · since 12:45 BST

👤 15 with you · ⬆️ 1 unpushed

- [with you] PACKAGE-NAME, STATE-FILE, FILES-AT-CREATION, QUERIES-FILE, PARKED-HOME, MESSAGES-FILE, DESCRIPTION-SHAPE, ROUTE-RECEIPT · owner · since 12:45
- [with you] REFRESH-TARGET, INBOX-CHECK, PICKUP-READS, STATE-HISTORY, STEWARD-HOME, MIGRATE-PATH · owner · since 12:45
- [with you] FIELDS-MIGRATE-ORDER · owner · since 12:14
- [committed] design note amendment in ki-principal
- [unpushed] ki-principal, 25 commits ahead including other sessions'
