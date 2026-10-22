# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › work-package-revise-2

**🤖 → 👤 Handoff to supervisor · Run report at 14:01 BST · last mark 13:37 BST**

---

## Done

- STATE-FILE is closed by your 13:52 BST answer. `state.md` is back, so a work package has five files: `work.md` (what the work is), `state.md` (where it stands), `queries.md`, `messages.md` and `decisions.md`.
- The [design note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md) now follows that answer. Wherever `state.md` returns, it restores the design both reviews agreed. `work.md` holds the definition: identity, the routing description, Goals and Scope. `state.md` holds the state fields, with `id` repeated and `method_read`, followed by Now, Queue for territory work, Next steps and Held. History is kept out of `state.md`, and Held sits there. The readers change before any folder moves. The rename, the gate and the pass are reworked around that.
- Readers checked, read-only, at 13:55 BST. Three things read the state fields from `work.md` today. The first is `ki work status` in tools-ki. tools-ki is written only by `ki.tools-burndown`, so its reader change, release and install are a handoff to that work. The second is the Observatory. It belongs to apps-observatory.local and is owned by `ki.observatory`. It takes its state from `ki work status`, so it follows tools-ki, but it also dates review-held folders by `work.md`'s change time. Its handoff is therefore a confirmation plus a small date fix. The third is the harness rubric, which is this work's own. Neither handoff has been sent; each goes out only once you approve RENAME-ORDER.
- Live-session check at 13:55 BST. The only agents running are in this work. Three other works committed in the half hour before: `ki` at 13:31, `ki.knowledge-acquisition` at 13:23 and 13:45 (its state still says On hold), and `ki.chezmoi` at 13:53. The `ki.chezmoi` commit included that session's files that had been uncommitted this morning, so no work folder had uncommitted changes at 13:55.
- Queries: FILES-AT-CREATION, PARKED-HOME, REFRESH-TARGET, PICKUP-READS, STATE-HISTORY, RENAME-ORDER, MIGRATE-PATH, MIGRATE-GATE and MIGRATE-SELF are reworked. The query-review-3 lifts to high stay on PICKUP-READS, STATE-HISTORY and MIGRATE-SELF, because only the file changed there. They drop back to medium on RENAME-ORDER, MIGRATE-PATH and MIGRATE-GATE, where the substance changed. The other queries are carried over unchanged, with their confidence and review marks. QUERIES-FILE and ROUTE-RECEIPT have one file-name correction each.
- The four reworked medium queries are in the [blind file](/Users/krisbrown/.local/state/ki/agents/ways-of-working/work-package-revise-2.blind.md) for `query-review-4`.
- Commit 3d12ecc5 in ki-principal, by explicit path. The Markdown check passed with no issues. Not pushed. `main` is 8 commits ahead. Six are this work's own. Two belong to other sessions: 585a7d1d (`ki.knowledge-acquisition`) and 82db4e67 (`ki.chezmoi`).

## In Progress

Nothing is running from this run. `query-review-4` is waiting for it to finish, so it can blind-review the four queries in the blind file.

Outstanding - no action requested now:

- The handoffs to `ki.tools-burndown` (the reader in `ki work status`, released and installed) and to `ki.observatory` (a check of the Work Instrument and the date fix) are written into the note only. Once you approve, the coordinator sends them as Messages lines.
- I edited nothing except the design note and this run's two output files.

## Queries

### FILES-AT-CREATION - Whether all five files exist from the start

**Context:** After your 13:52 answer, a work package has five files: `work.md` (what the work is), `state.md` (where it stands), `queries.md`, `messages.md` and `decisions.md`. The design creates all five when the work is set up, and the last three start out saying `None`. That way no reader ever finds a file missing, and another work sending a message never has to create one. Codex's earlier objection comes back with the fifth file: five compulsory files are too much for small work. `ki.regular` is 103 words long and has no decisions log today. Fable accepted all five. There is a middle way: require only the files that someone other than the worker writes to or always reads, which are `work.md`, `state.md` and `messages.md`.

**Query:** Should every work package have all five files from the moment it is created?

**Options:**

a) (recommended, confidence medium - an empty file costs one line, while optional files mean every reader, sender and check has to handle a missing one; Codex disagrees) Yes. All five exist at creation, and `queries.md`, `messages.md` and `decisions.md` start as `None`.

b) Only `work.md` and `state.md` exist at creation. The other three are created when something is first written to them.

c) `work.md`, `state.md` and `messages.md` exist at creation, so no other work ever has to create a file. `queries.md` and `decisions.md` are created when first written.

### QUERIES-FILE - Full query text in `queries.md`

**Context:** You asked for "a Q one, like the decisions one", and `queries.md` is now one of the five files. One question is still open: what the file holds. In 6 of the 11 live works, open queries appear only as tags. Their text sits in run reports, in reports outside the repository, in a design note, or only in the last Summary. `ki.chezmoi` keeps 12 of its 25 reports alive only because they hold queries. The design gives every open and parked query its full text in `queries.md`, copied in when a report is received. The owner report's Queries section is drawn from that file. When you answer a query, its block is deleted in the same commit that logs your answer.

**Query:** Should `queries.md` hold every open and parked query in full?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes. Each block keeps its tag and its source report. Reports can then be pruned once their outcome has a home.

b) Make `queries.md` an index of tags that point at reports; less copying, but reports stay alive for their queries.

### PARKED-HOME - Where parked items go

**Context:** Today's `Parked` sections mix five things: parked queries, work waiting on a condition, to-do lists for a particular screen, ideas, and items already resolved. The design splits them by kind instead of giving them a file of their own. Parked queries go to `queries.md`, and so do side topics you park before they have become queries. Work waiting on a condition goes to a `## Held` section in `state.md`, each item with its release condition. Ideas go to the Project note or a record. Resolved items are deleted by the work's own worker. With `state.md` back, this is the version both reviews saw and agreed.

**Query:** Should `Parked` be split by kind across `queries.md` and `state.md`?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes. Parked queries and side topics go under `## Parked` in `queries.md`. Held work goes under `## Held` in `state.md`, with its release. Ideas go to the Project note or a record. There is no `parked.md`.

b) One `parked.md` for everything parked, as a sixth file.

### DESCRIPTION-SHAPE - The routing description

**Context:** State of play now routes new work to existing works, but no work says what it takes. Like a skill, each `work.md` gains a required `description` in its front matter. State of play reads only the descriptions unless two of them match. The design's version runs to 500 characters: what the work does, "Takes ...", and "Not for ..." naming the neighbouring works by id. Below it, a `## Scope` section gives `In:` and `Out:` lines by id. Codex agrees, provided the 500 is guidance and the shape is tested against a few ambiguous examples. Fable says that is the same boundary written twice, and the two will drift apart. It would keep ids in Scope only and make the description about 300 characters of plain prose. Your answers did not touch this query.

**Query:** Should the description name neighbouring works by id, or leave that to Scope?

**Options:**

a) (recommended, confidence medium - routing reads only the descriptions first, so the exclusions have to be there to settle most cases without opening a folder; held by the design and Codex) A description of up to 500 characters with "Takes ... Not for ..." naming neighbours by id, plus `## Scope`, tested against a handful of ambiguous routing examples.

b) (Fable) A description of about 300 characters in plain prose with no ids. `## Scope` alone names the neighbours, and the rubric checks that every id resolves.

c) Route on the Project note's `outcome` alone. That leaves regular and territory work uncovered.

### ROUTE-RECEIPT - What a work must do with routed work

**Context:** You said that if State of play decides a piece of work is yours, "you have to accept it". The design reads this as follows. The receiving work deals with every routed line in its `messages.md` at its next start-up or owner message. It records one outcome: a next step in `state.md`, a query to you in `queries.md`, or a return to State of play with a reason. Routing gives no permission beyond what the work's existing decisions cover. Paused work keeps the line waiting without waking. Work that already has an owner does not pass through State of play. A unit can be returned only once; after that it comes to you. This is the version both reviews saw.

**Query:** Is receipt compulsory, with a recorded outcome and no new authority?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes, as above. The outcome is named in the commit that removes the line, and State of play shows any lines nobody has picked up.

b) Deal with routed lines only at the next mark; less interruption, slower routing.

### REFRESH-TARGET - How method changes reach each work

**Context:** When the method changes, each live work has to re-read it. Only 3 of the 11 works record which revision they last read, so nobody can tell who is behind. The design adds a `method_read` field to the front matter of `state.md`, beside the other fields that change as the work moves. That is where both reviews saw it. After a change, one dated REFRESH line goes only to the works that are behind and affected. Updating the field counts as the confirmation. Held work is not woken, and the start-up check stays as a fallback. Codex's two conditions are written in. One revision covers `ki-coordination` and `ki-work-package` together. A line that replaces an earlier, unread one keeps every pending change from it.

**Query:** Should refresh be targeted through `method_read`?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes, as above, with `method_read` in `state.md`.

b) Broadcast every change to every live work and ask each to acknowledge in one line.

### INBOX-CHECK - Whether a coordinator checks its inbox at each wake

**Context:** You asked whether a work refreshes itself, so that routed work gets picked up. Today, nothing prompts a work to look at its messages except its next start-up or a message from you. A coordinator wakes every five minutes only while it has runs going. Once it has sent the work to you, or the work is on hold, it does not wake at all, and that is where almost every live work is now. Neither review proposed a rule for this; the merge raised it. Codex flagged the gap next to it: a work that can be routed to does not necessarily have a live session, so unread inboxes need to be visible. With `messages.md`, the check at each wake is cheap: compare that file's last commit, and the method revision, with what the work last read.

**Query:** Should each five-minute wake check for new messages and method changes?

**Options:**

a) (recommended, confidence medium - it costs one comparison per wake and closes the gap for busy works, while showing unread age covers idle ones without new wake-ups) At each wake, check whether `messages.md` or the method has changed since the last read. Act on a new line at once, under ROUTE-RECEIPT, without stopping running work. For works that are not waking, State of play shows how old their unread lines are and gives you the resume line.

b) As a), and also keep a light inbox-only wake every 15 minutes while the work is with you. This reverses today's "no heartbeat otherwise" and costs tokens in every idle session.

c) No standing rule; works pick up messages at start-up or at your next message, as today.

### PICKUP-READS - Keeping a coordinator's reads within its turn budget

**Context:** A coordinator may make at most five tool calls per turn. The output style limits its reads to the work file, `ki agent status`, one report and one short file. It limits its writes to the work file, the decisions log and a brief. Under the package, picking up a work means reading `state.md`, `messages.md`, `queries.md` and `decisions.md`, plus `work.md` at start-up. A send writes up to four of them. Fable warned that unless the budget is rewritten, the five calls are spent before the first launch. Codex warned that reading every decision and query at each message from you brings the context burden back, and would read only what has changed since start-up. With `state.md` back, start-up reads five files and later pick-ups read four, because `work.md` rarely changes. The problem is the same as before. A third possibility is a `ki` command that prints a package, and what has changed since the last read, in one call.

**Query:** How should the turn budget and reading rule change for the package?

**Options:**

a) (recommended, confidence high - reviewed: Fable agrees; only the file count has changed) One read of the package's files counts as one call: all five at start-up, then the four that change, with `work.md` re-read only when it has changed. Writes to the package's files together with a brief count as one write set. After start-up, the coordinator reads only what has changed since its last read, plus the entries that bear on the question.

b) Keep the budget as written and accept fewer launches per turn.

c) As a), and add a `ki work` command that prints the package and its changes since the last read in one call; one more tools-ki change.

### STATE-HISTORY - Where "what happened since the mark" goes

**Context:** Four works use `Next steps` as a running log, because a Summary needs "what happened since the mark" and nowhere else holds it. With `state.md` back, the rule applies to that file: its `## Now`, `## Next steps` and `## Held`. `work.md` holds no state at all. Fable said the replacement source has to be named, or the log simply moves into `## Now`. The recap would read the folder's Git history and the run reports. Codex said a strict ban on dates, commit identifiers and test counts goes too far. It would warn on bulk history and still allow a link to the evidence.

**Query:** How is history kept out of `state.md`?

**Options:**

a) (recommended, confidence high - reviewed: Fable agrees; only the file it applies to has changed) The recap since the mark reads `git log` of the folder and the run reports, and `## Now` holds only the present. A check warns on bulk history in `state.md`, but not on a single link to a report or commit.

b) A strict pattern check on dates, commit identifiers and test counts, with no stated recap source.

### STEWARD-HOME - Who carries method changes after Ways of working closes

**Context:** You decided that Ways of working goes away once the method is defined, and that State of play takes over its stewardship. State of play does no work itself, so someone still has to carry out each accepted improvement. Nobody knows yet how much the method will change once it has settled. Your answers did not touch this query.

**Query:** How should State of play get method improvements done after Ways of working closes?

**Options:**

a) (recommended, confidence medium - reviewed: Codex and Fable agree; lifted from low) State of play keeps a method backlog and sends each accepted improvement out as small regular work, or into the Project it most affects, with design reviews for changes of shape. Lasting method authority stays in the skills and decision records.

b) A standing regular work for method upkeep under an Activity note, set up only if the volume shows it is needed.

### RENAME-ORDER - Readers first, then the `ki-work-package` rename

**Context:** Renaming the skill `ki-work-folder` to `ki-work-package` touches 44 files in the harness: the skill, its standard, rubric and scripts, other skills that point to it, a hook test, diagrams and the skills list. It also touches 5 files in tools-ki and ki-principal's configuration. Ten repositories declare the skill, eight of them in other territories (er-, hnr-, si-, legal-, personal-, tmx- and va-principal, and `personal/acquire`), and this Capital may not write in those. The standard is being rewritten for the package anyway, so renaming in the same change touches each file only once. Historical text keeps the old name. With `state.md` back, the state fields move out of `work.md`, and three things read them there today. The first is `ki work status` in tools-ki. The second is the Observatory in apps-observatory.local, which takes its state from `ki work status` but also dates review-held folders by when `work.md` last changed. The third is the harness rubric. All three must read both shapes before any folder moves, or the status views lose the works that have moved. The rubric is this work's own. tools-ki is written only by `ki.tools-burndown`, so its reader change is a handoff to that work, which must also release and install `ki`. The Observatory belongs to `ki.observatory`, so its check and small date fix are a handoff there. The migration pass then waits on both works.

**Query:** In what order should the readers change and the rename land, and how far should the rename go?

**Options:**

a) (recommended, confidence medium - Fable reviewed the rename order, but the pass now waits on two other works and a `ki` release, which no review has seen) First, send both reader handoffs, so they run alongside the rest. Then one harness change renames the skill, rewrites its standard and makes the rubric read both shapes. It accepts the old `[skills.ki-work-folder]` declaration as a temporary alias. Next, ki-principal's configuration, the Work Process note and GDR-KI-PRINCIPAL-009 change under one Enactment record. Then `ki.tools-burndown` lands, releases and installs the tools-ki reader and help text. Then the harness is reinstalled and checked: no stale skill, `ki repair` clean, and `chezmoi diff` showing no drift. The readers are also tested on a scratch copy of the work folders outside the repository. Then the pass. The other territories update through handoffs, and the alias is removed once none of them declares the old name.

b) Do not wait for the readers. Rename, then run a first pass that moves only Messages, Parked and the queries into their own files, leaving the state fields in `work.md`. A second pass moves the state fields into `state.md` once the readers have landed. The tidying comes sooner, but there are two passes.

c) Migrate the folders under the old skill name first, and rename afterwards as a separate change.

d) Once the readers have landed, rename everywhere in one approved sweep with no alias, including the eight other territories' configuration.

### MIGRATE-PATH - What the one-pass migration does to each folder

**Context:** You decided that the live folders can move in one pass, because no other thread is active. With `state.md` back, the pass also moves the state fields out of `work.md`, which is why it waits until the readers accept both shapes (RENAME-ORDER). In each folder, `work.md` keeps the work's identity and gains a drafted routing description, plus Goals and Scope drafted from the Project note and any scope text. The state fields move unchanged into a new `state.md`. Its `method_read` is left empty, so the work's next start-up reads the new standard. Next steps is cut to what is still to do. Messages move into `messages.md`, dropping only the old 18 October MIGRATED line. One FIRST-STEP line is added, asking the worker to re-read all five files before any write and to confirm the drafts. Parked splits into `queries.md` and `## Held` in `state.md`, and anything that looks resolved is flagged rather than deleted. Every open query's full text is copied into `queries.md`, and any query whose text is lost is raised with you. `decisions.md` is created where it is missing.

Moving the state fields brings a new risk. A session that still has the old shape in mind could write state fields back into `work.md`, leaving the work with two states. To catch this, the rubric fails any folder whose `work.md` carries a state field alongside a `state.md`, so the problem shows at that session's next commit. The pass prunes no report, strikes no decision and moves no design file; those judgements wait for each work's own next mark. After each folder, it checks that the rubric passes, and that `ki work status` and the Observatory show the same state, holder and time as before, now read from `state.md`. It stops at the first failure and commits once per folder. The order is this work first as the pilot, then State of play (`ki`), then the held works, then the works with you. Left outside the pass are `kb.regular.acquire-intake` in the personal territory, the six folders under `+/_WORK_REVIEW/`, the review-held twin of `ki.baseline-rollout`, and the seven other Capitals still on the old checkpoint shape.

**Query:** Should the pass make only these mechanical moves, in this order?

**Options:**

a) (recommended, confidence medium - mechanical moves leave judgement with each work, but moving the state fields is new since the reviews, and the guard against a stale session is a rubric check rather than a lock) Yes, as above, with this work as the pilot and the pass stopping at the first failure.

b) As a), and the pass also tidies: it prunes reports whose queries have been copied, strikes decisions that have a home elsewhere, and deletes resolved parked items. One pass leaves every folder clean, at the cost of outside judgement in eleven works.

### MIGRATE-GATE - What must hold before the pass launches

**Context:** At 13:55 BST, background agents were running only in this work, and every other work was with you or on hold. But three other works had committed in their folders in the previous half hour, so their sessions are open or were open minutes earlier, still working from the old shape. State of play (`ki`) sent its work to you at 13:31. `ki.knowledge-acquisition` committed at 13:23 and 13:45, although its state still says On hold since 18 October. `ki.chezmoi` committed at 13:53. That commit included the other session's files that had been uncommitted this morning, so no work folder had uncommitted changes at 13:55. If one of these sessions is resumed after the pass, it could write the old shape over a migrated folder. With `state.md` back, the pass also needs the readers to have landed first.

**Query:** What must hold before the migration pass launches?

**Options:**

a) (recommended, confidence medium - it closes every gap found, but session safety still rests on your confirmation and a last-commit check rather than anything enforced) All of these must hold. The readers have landed, been installed and been tested on a scratch copy. `ki.observatory` has confirmed its view. `ki agent status` shows no other agent running or queued. No work other than this one is With worker. Every target folder is clean, and the pass refuses any folder that is not. You confirm that no other session will be resumed until the pass has committed, and that any open session is resumed only through its send line, which re-reads from the files. You approve the exact folder set. At launch, the pass records each folder's last commit, and skips and reports any folder that has moved since your approval.

b) Launch once the readers have landed and `ki agent status` is clear, trusting "no other thread is active", and let the pass skip any folder it finds dirty.

c) As a), but leave out any folder that moved in the hour before your approval, and let each of those migrate itself at its own next mark under the new standard.

### MIGRATE-SELF - How this live session takes part

**Context:** Ways of working is the only work With worker, and its coordinator session is live. Otherwise it would keep writing its own files while the pass rewrites that same folder. The coordinator does no substantive work itself, so it cannot migrate its own folder by hand. `query-review-4`, the blind review of the reworked queries, runs after this report and must finish before anything touches this folder. With `state.md` back, the pilot is also the first real test of the new readers on a split folder.

**Query:** How does this session take part in the pass?

**Options:**

a) (recommended, confidence high - reviewed: Fable agrees; only the file count and the pilot's reader check have changed) The coordinator logs your approval and commits it. It waits for the blind review to finish and receives its report. Then it launches the pass with its own folder first as the pilot, checked against the rubric, `ki work status` and the Observatory. It writes nothing in the folder until the pass reports. After that, it re-reads all five files before any write and acts on its own FIRST-STEP line.

b) Run this folder alone as a separate pilot first, show you the result, then launch the pass for the other ten. This is safer but adds one more approval and run.

### FIELDS-MIGRATE-ORDER - Which repository the field migration starts in

**Context:** The new work-record fields need a migration run in each repository, each approved by you. These are priority, size and kind, plus the retired horizons. Personal-principal holds 22 of the 49 retired horizons and uses both ways of classifying a record. In knowledge-base repositories, kind and size can be proposed now. In code repositories they must wait for the next `ki` release. The coordinator would pilot on personal-principal, which clears the most debt and tests the kind and size proposals. Codex, in query-review-2, would first run a bounded mechanical pilot on apps-markhowarth.com's four records, all of which have retired horizons. Your answers did not touch this query.

**Query:** Should the field migration start with a small pilot or with personal-principal?

**Options:**

a) (recommended, confidence medium - a four-record run tests the run's shape cheaply before the largest one, at the cost of one extra approval; held by Codex) apps-markhowarth.com first, as a mechanical pilot. Then personal-principal, hnr-principal, 5g-emerge-phase2 and legal-principal. Then the remaining retired horizons, and kind and size in code repositories after the `ki` release.

b) (coordinator) personal-principal first as the pilot, with all fixes plus kind and size proposals. Then hnr-principal, legal-principal, tmx-principal, er-principal and va-principal. Then the mechanical-only runs.

### 🤖 → 👤 Handoff to supervisor · since 14:01 BST

👤 15 with you · 🤖 1 queued · ⬆️ 1 unpushed

- [with you] FILES-AT-CREATION, QUERIES-FILE, PARKED-HOME, DESCRIPTION-SHAPE, ROUTE-RECEIPT, REFRESH-TARGET, INBOX-CHECK, PICKUP-READS · owner · since 14:01
- [with you] STATE-HISTORY, STEWARD-HOME, RENAME-ORDER, MIGRATE-PATH, MIGRATE-GATE, MIGRATE-SELF · owner · since 14:01
- [with you] FIELDS-MIGRATE-ORDER · owner · since 12:14
- [queued] query-review-4, blind review of the four reworked medium queries · run/query-review-4 · since 13:53
- [committed] design note with `state.md` restored, in ki-principal
- [unpushed] ki-principal, 8 commits ahead, two of them other sessions'
