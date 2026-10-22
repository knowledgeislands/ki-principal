# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › work-package-revise

**🤖 → 👤 Handoff to supervisor · Run report at 13:46 BST · last mark 13:37 BST**

---

## Done

- The [design note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md) now follows your 13:37 BST answers. The concept and skill are the work package, `ki-work-package`, and the place is still the work folder. A package has exactly four files: `work.md`, `queries.md`, `messages.md` and `decisions.md`. State, next steps and held items sit in `work.md` below Goals and Scope, and there is no `state.md`. The live folders move in one gated pass. A new section covers the rename, and the parts the reviews agreed are unchanged.
- Settled by your answers and closed: PACKAGE-NAME and MESSAGES-FILE. STATE-FILE comes back only as a confirmation. FILES-AT-CREATION, PICKUP-READS, STATE-HISTORY and MIGRATE-PATH are reworked. RENAME-ORDER, MIGRATE-GATE and MIGRATE-SELF are new.
- One consequence of keeping state in `work.md`: `ki work status` and the Observatory keep reading the state fields where they are now. Nothing has to change in their reader before the pass, so the risky tolerance step from the earlier plan has gone.
- Live-session check, 13:42 BST. `ki agent status` shows agents in this work only: this run, and `query-review-3`, which is waiting for it. Ways of working is the only work With worker. Seven works are with you and three are on hold, as is `kb.regular.acquire-intake` in `personal/acquire`. Two caveats. `ki` sent to you at 13:31 and `ki.knowledge-acquisition` at 13:23, so their sessions may still be open. `ki.chezmoi` holds another session's uncommitted files. "Not active" holds for runs and moves, but not necessarily for open sessions.
- Rename inventory: 44 files in the harness and 5 in tools-ki name `ki-work-folder`. Ten `.ki.toml` files declare it, eight of them in other territories. The chezmoi source has no reference.
- Commit db12ad33 in ki-principal, by explicit path. The Markdown gate passed after a fix to one indentation. Not pushed: `main` is 2 commits ahead, mine and this work's own 13:37 mark commit a9b75552.

## In Progress

Nothing is running. `query-review-3` is waiting for this run to finish, so it can blind-review the queries in the companion [blind file](/Users/krisbrown/.local/state/ki/agents/ways-of-working/work-package-revise.blind.md).

Outstanding - no action requested now:

- Single-reviewer points from the merge are now in the note as written: `ki.regular` gains a `decisions.md`; "more than eight open queries" moves to the `ki-coordination` rubric; there is no fixed count of goals; and the register's token figure is marked as still to be measured. Fable's point about repeating `id` in `state.md` no longer applies.
- Corrected in the note: `ki.chezmoi` has eight lines from 18 October, and `ki.baseline-rollout` has WAVE-1's proposed scope but no query block.
- I left another session's uncommitted files in `+/_WORK/ki.chezmoi/` alone: `decisions.md`, `apply-owned-drift.report.md`, `briefs/apply-owned-drift.md` and `coverage-implement.report.md`.

## Queries

### STATE-FILE - Confirm that state stays in `work.md`

**Context:** You named four files for a package and no state file. So the state fields (state, target, hold, since, mark and so on) stay in the front matter of `work.md`, as they are today. The state prose sits in the same file, below the definition: `## Goals` and `## Scope` first, then `## Now`, `## Next steps` and `## Held`. Territory work also gets a `## Queue` for its ordered list of Project work. One gain: `ki work status` and the Observatory already read these fields from `work.md`, so they keep working with no change. One cost: `work.md` changes at every move. Because the definition sits at the top and rarely changes, each move's change stays in the lower half of the file. The earlier plan had a separate `state.md`, and both reviews had agreed to it.

**Query:** Do you confirm that the state fields and state sections stay in `work.md`, with no fifth file?

**Options:**

a) (recommended, confidence high - it is your four-file answer, and it removes the one reader change the earlier plan needed) Yes. The front matter holds identity, the routing description, the state fields and `method_read`. The body runs Goals, Scope, Now, Next steps and Held, and territory work adds Queue.

b) Bring back a separate `state.md` as a fifth file, so that `work.md` holds only the definition.

### FILES-AT-CREATION - Whether all four files exist from the start

**Context:** The earlier plan required five files at creation. Codex called that overbuilt for small work: `ki.regular` is 103 words and has no decisions log. With state back in `work.md`, a package is the four files you named. Creating all four at once, with the three detail files saying `None`, means no reader ever meets a missing file and no sender ever has to create one. `ki.regular` would gain a `decisions.md` when it migrates.

**Query:** Should every work package have all four files from creation?

**Options:**

a) (recommended, confidence high - you described the package as these four files, and the fifth file Codex objected to has gone) Yes. All four exist at creation, and `queries.md`, `messages.md` and `decisions.md` start as `None`.

b) Create only `work.md` at first, and the other three when something is first written to them.

### QUERIES-FILE - Full query text in `queries.md`

**Context:** You asked for "a Q one, like the decisions one", and `queries.md` is now one of the four files. One question is still open: what the file holds. In 6 of the 11 live works, open queries appear only as tags. Their text sits in run reports, in reports outside the repository, in a design note, or only in the last Summary. `ki.chezmoi` keeps 12 of its 25 reports alive only because they hold queries. The design gives every open and parked query its full text in `queries.md`, copied in when a report is received. The owner report's Queries section is drawn from that file. When you answer a query, its block is deleted in the same commit that logs your answer.

**Query:** Should `queries.md` hold every open and parked query in full?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes. Each block keeps its tag and its source report. Reports can then be pruned once their outcome has a home.

b) Make `queries.md` an index of tags that point at reports; less copying, but reports stay alive for their queries.

### PARKED-HOME - Where parked items go

**Context:** Today's `Parked` sections mix five things: parked queries, work waiting on a condition, to-do lists for a particular screen, ideas, and items already resolved. The design splits them by kind, so no fifth file is needed. Parked queries go to `queries.md`, and so do side topics you park before they have become queries. Work waiting on a condition goes to a `## Held` section in `work.md`, each item with its release condition. Ideas go to the Project note or a record. Resolved items are deleted by the work's own worker. Compared with the version both reviews saw, only one thing has changed: `## Held` sits in `work.md`, because there is no `state.md`.

**Query:** Should `Parked` be split by kind across `queries.md` and `work.md`?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes. Parked queries and tangents go under `queries.md` `## Parked`, held work under `work.md` `## Held` with its release, and ideas to the Project note or a record. There is no `parked.md`.

b) One `parked.md` for everything parked, as a fifth file.

### DESCRIPTION-SHAPE - The routing description

**Context:** State of play now routes new work to existing works, but no work says what it takes. Like a skill, each `work.md` gains a required `description` in its front matter. State of play reads only the descriptions unless two of them match. The design's version runs to 500 characters: what the work does, "Takes ...", and "Not for ..." naming the neighbouring works by id. Below it, a `## Scope` section gives `In:` and `Out:` lines by id. Codex agrees, provided the 500 is guidance and the shape is tested against a few ambiguous examples. Fable says that is the same boundary written twice, and the two will drift apart. It would keep ids in Scope only and make the description about 300 characters of plain prose. Your answers did not touch this query.

**Query:** Should the description name neighbouring works by id, or leave that to Scope?

**Options:**

a) (recommended, confidence medium - routing reads only the descriptions first, so the exclusions have to be there to settle most cases without opening a folder; held by the design and Codex) A description of up to 500 characters with "Takes ... Not for ..." naming neighbours by id, plus `## Scope`, tested against a handful of ambiguous routing examples.

b) (Fable) A description of about 300 characters in plain prose with no ids. `## Scope` alone names the neighbours, and the rubric checks that every id resolves.

c) Route on the Project note's `outcome` alone. That leaves regular and territory work uncovered.

### ROUTE-RECEIPT - What a work must do with routed work

**Context:** You said that if State of play decides a piece of work is yours, "you have to accept it". The design reads this as follows. The receiving work deals with every routed line in its `messages.md` at its next start-up or owner message. It records one outcome: a next step in `work.md`, a query to you in `queries.md`, or a return to State of play with a reason. Routing gives no permission beyond what the work's existing decisions cover. Paused work keeps the line waiting without waking. Work that already has an owner does not pass through State of play. A unit can be returned only once; after that it comes to you. Compared with what the reviews saw, only the file names have changed.

**Query:** Is receipt compulsory, with a recorded outcome and no new authority?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes, as above. The outcome is named in the commit that removes the line, and State of play shows any lines nobody has picked up.

b) Deal with routed lines only at the next mark; less interruption, slower routing.

### REFRESH-TARGET - How method changes reach each work

**Context:** When the method changes, each live work has to re-read it. Only 3 of the 11 works record which revision they last read, so nobody can tell who is behind. The design adds a `method_read` field, which now sits in `work.md` front matter. After a change, one dated REFRESH line goes only to the works that are behind and affected. Updating the field is the confirmation, held work is not woken, and the start-up check stays as a fallback. Codex's two conditions are written in. One revision covers `ki-coordination` and `ki-work-package` together. A line that replaces an earlier, unread one keeps every pending change from it.

**Query:** Should refresh be targeted through `method_read`?

**Options:**

a) (recommended, confidence high - reviewed: Codex and Fable agree) Yes, as above.

b) Broadcast every change to every live work and ask each to acknowledge in one line.

### INBOX-CHECK - Whether a coordinator checks its inbox at each wake

**Context:** You asked whether a work refreshes itself, so that routed work gets picked up. Today, nothing prompts a work to look at its messages except its next start-up or a message from you. A coordinator wakes every five minutes only while it has runs going. Once it has sent the work to you, or the work is on hold, it does not wake at all, and that is where almost every live work is now. Neither review proposed a rule for this; the merge raised it. Codex flagged the gap next to it: a work that can be routed to does not necessarily have a live session, so unread inboxes need to be visible. With `messages.md`, the check at each wake is cheap: compare that file's last commit, and the method revision, with what the work last read.

**Query:** Should each five-minute wake check for new messages and method changes?

**Options:**

a) (recommended, confidence medium - it costs one comparison per wake and closes the gap for busy works, while showing unread age covers idle ones without new wake-ups) At each wake, check whether `messages.md` or the method has changed since the last read. Act on a new line at once, under ROUTE-RECEIPT, without stopping running work. For works that are not waking, State of play shows how old their unread lines are and gives you the resume line.

b) As a), and also keep a light inbox-only wake every 15 minutes while the work is with you. This reverses today's "no heartbeat otherwise" and costs tokens in every idle session.

c) No standing rule; works pick up messages at start-up or at your next message, as today.

### PICKUP-READS - Keeping a coordinator's reads within its turn budget

**Context:** A coordinator may make at most five tool calls per turn. The output style limits its reads to the work file, `ki agent status`, one report and one short file. It limits its writes to the work file, the decisions log and a brief. Under the package, picking up a work means reading four files, and a send writes up to three of them. Fable warned that unless the budget is rewritten, the five calls are spent before the first launch. Codex warned that reading every decision and query at each message from you brings the context burden back. It would read only what has changed since start-up. With state staying in `work.md`, pick-up is the four files rather than five, but the problem is the same. A third possibility is a `ki` command that prints a package and what has changed since the last read, in one call.

**Query:** How should the turn budget and reading rule change for the package?

**Options:**

a) (recommended, confidence medium - it combines both reviewers' compatible fixes without new tooling) One read of the package's four files counts as one call, and writes to the package's files with a brief count as one write set. After start-up, the coordinator reads only what has changed since its last read, plus the entries that bear on the question.

b) Keep the budget as written and accept fewer launches per turn.

c) As a), and add a `ki work` command that prints the package and its changes since the last read in one call; one more tools-ki change.

### STATE-HISTORY - Where "what happened since the mark" goes

**Context:** Four works use `Next steps` as a running log, because a Summary needs "what happened since the mark" and nowhere else holds it. With state staying in `work.md`, the rule now applies to its state sections, `## Now`, `## Next steps` and `## Held`. Fable said the replacement source has to be named, or the log simply moves into `## Now`. The recap would read the folder's Git history and the run reports. Codex said a strict ban on dates, commit identifiers and test counts is overbuilt. It would warn on bulk history and still allow a link to the evidence.

**Query:** How is history kept out of `work.md`?

**Options:**

a) (recommended, confidence medium - the two reviews address different halves of one rule and do not conflict) The recap since the mark reads `git log` of the folder and the run reports, and `## Now` holds only the present. A check warns on bulk history in the state sections, but not on a single link to a report or commit.

b) A strict pattern check on dates, commit identifiers and test counts, with no stated recap source.

### STEWARD-HOME - Who carries method changes after Ways of working closes

**Context:** You decided that Ways of working goes away once the method is defined, and that State of play takes over its stewardship. State of play does no work itself, so someone still has to carry out each accepted improvement. Nobody knows yet how much the method will change once it has settled. Your answers did not touch this query.

**Query:** How should State of play get method improvements done after Ways of working closes?

**Options:**

a) (recommended, confidence medium - reviewed: Codex and Fable agree; lifted from low) State of play keeps a method backlog and sends each accepted improvement out as small regular work, or into the Project it most affects, with design reviews for changes of shape. Lasting method authority stays in the skills and decision records.

b) A standing regular work for method upkeep under an Activity note, set up only if the volume shows it is needed.

### RENAME-ORDER - The order and reach of the `ki-work-package` rename

**Context:** Renaming the skill `ki-work-folder` to `ki-work-package` touches 44 files in the harness: the skill itself, its standard, rubric and scripts, other skills that point to it, a hook test, diagrams and the skills list. It also touches 5 files in tools-ki (help text, man page, changelog, two records) and ki-principal's configuration. Ten repositories declare the skill in `.ki.toml`, eight of them in other territories (er-, hnr-, si-, legal-, personal-, tmx- and va-principal, and `personal/acquire`). This Capital has no authority to write in those. The chezmoi source does not name the skill. The skill's standard is also being rewritten for the package shape, so renaming in the same change means each file is touched once. The name changes wherever text names the skill or the concept. "Work folder" stays wherever it names the directory. Historical text keeps the old name: past decisions, past design notes, changelog entries and finished records.

**Query:** In what order, and how far, should the rename go?

**Options:**

a) (recommended, confidence medium - each file moves once, nothing breaks in the other territories, and the migration brief can cite the final name) First, one harness change renames the skill and rewrites its standard together, and accepts the old `[skills.ki-work-folder]` declaration as a temporary alias. Then ki-principal's configuration, the Work Process note and GDR-KI-PRINCIPAL-009 change under one Enactment record. Then tools-ki's help text. Then the harness is reinstalled, with checks that no stale skill remains, that `ki repair` is clean and that `chezmoi diff` shows no drift. Then the migration pass. The other territories update through handoffs, and the alias is removed once none declares the old name.

b) Migrate the folders under the old skill name first, and rename afterwards as a separate change.

c) Rename everywhere in one approved sweep with no alias, including the eight other territories' configuration.

### MIGRATE-PATH - What the one-pass migration does to each folder

**Context:** You decided that the live folders can move in one pass, because no other thread is active. The state fields stay where they are, so status views keep working throughout. In each folder, the pass would add a drafted routing description to `work.md` and set `method_read` empty, so the work's next start-up reads the new standard. It would draft Goals and Scope from the Project note and any scope text, and cut Next steps to what is still to do. It would move Messages into `messages.md`, dropping only the old 18 October MIGRATED line, and add one FIRST-STEP line asking the worker to confirm the drafts. It would split Parked into `queries.md` and `## Held`, flagging rather than deleting anything that looks resolved. It would copy every open query's full text into `queries.md`, raising any lost one as a query to you rather than dropping it, and create `decisions.md` where it is missing.

The pass would prune no report, strike no decision and move no design file. Those judgements wait for each work's own next mark. After each folder it checks that the rubric passes and that the work's state is unchanged, and it stops at the first failure. It commits once per folder. The order is this work first as the pilot, then State of play (`ki`), whose description routing matches against, then the held works, then the works with you. Left outside the pass are `kb.regular.acquire-intake`, which belongs to the personal territory; the six folders under `+/_WORK_REVIEW/`; the review-held twin of `ki.baseline-rollout`; and the seven other Capitals still on the old checkpoint shape.

**Query:** Should the pass make only these mechanical moves, in this order?

**Options:**

a) (recommended, confidence medium - mechanical moves are safe from outside, while pruning and resolving need each work's own judgement) Yes, as above, with this work as the pilot and the pass stopping at the first failure.

b) As a), and the pass also tidies: it prunes reports whose queries have been copied, strikes decisions that have a home elsewhere, and deletes resolved parked items. One pass leaves every folder clean, at the cost of outside judgement in eleven works.

### MIGRATE-GATE - What must hold before the pass launches

**Context:** At 13:42 BST, background agents were running only in this work. Every other work was either with you or on hold. Two caveats, though. State of play (`ki`) sent its work to you at 13:31, six minutes before your answer, and `ki.knowledge-acquisition` at 13:23. Their sessions may still be open, holding the old shape in memory. A session resumed after the pass could rewrite its migrated `work.md` from memory. Separately, `ki.chezmoi` has another session's uncommitted changes from this morning: a modified decisions log, two new reports and a brief. The pass must not commit or overwrite those.

**Query:** What must hold before the migration pass launches?

**Options:**

a) (recommended, confidence medium - it closes the two real gaps found, at the cost of one confirmation from you) All of these must hold. The rename and new standard have landed and been installed. `ki agent status` shows no other agent running or queued. No work other than this one is With worker. Every target folder is clean, and the pass refuses any dirty folder, so `ki.chezmoi`'s files are either committed by their session or that folder is skipped. You confirm that no other session will be resumed until the pass has committed, and that any open session is resumed only through its send line, which re-reads from the files. You approve the exact folder set.

b) Launch on `ki agent status` alone, trusting "no other thread is active", and let the pass skip any folder it finds dirty.

### MIGRATE-SELF - How this live session takes part

**Context:** Ways of working is the only work With worker, and its coordinator session is live. It would otherwise keep writing its own `work.md` and decisions log while the pass rewrites that same folder. The coordinator does no substantive work itself, so it cannot migrate its own folder by hand. `query-review-3`, the blind review of these queries, is still to run, and it must finish before anything touches this folder.

**Query:** How does this session take part in the pass?

**Options:**

a) (recommended, confidence medium - the coordinator stays a dispatcher and never writes over the pass, and the pilot is still checked before the rest move) The coordinator logs your approval and commits it. It waits for `query-review-3` to finish and receives its report, then launches the pass with its own folder first as the pilot. It writes nothing in the folder until the pass reports. It then re-reads all four files before any write, and acts on its own FIRST-STEP line.

b) Run this folder alone as a separate pilot first, show you the result, then launch the pass for the other ten. This is safer but adds one more approval and run.

### FIELDS-MIGRATE-ORDER - Which repository the field migration starts in

**Context:** The new work-record fields need a migration run in each repository, each approved by you. These are priority, size and kind, plus the retired horizons. Personal-principal holds 22 of the 49 retired horizons and uses both ways of classifying a record. In knowledge-base repositories, kind and size can be proposed now. In code repositories they must wait for the next `ki` release. The coordinator would pilot on personal-principal, which clears the most debt and tests the kind and size proposals. Codex, in query-review-2, would first run a bounded mechanical pilot on apps-markhowarth.com's four records, all of which have retired horizons. Your answers did not touch this query.

**Query:** Should the field migration start with a small pilot or with personal-principal?

**Options:**

a) (recommended, confidence medium - a four-record run tests the run's shape cheaply before the largest one, at the cost of one extra approval; held by Codex) apps-markhowarth.com first, as a mechanical pilot. Then personal-principal, hnr-principal, 5g-emerge-phase2 and legal-principal. Then the remaining retired horizons, and kind and size in code repositories after the `ki` release.

b) (coordinator) personal-principal first as the pilot, with all fixes plus kind and size proposals. Then hnr-principal, legal-principal, tmx-principal, er-principal and va-principal. Then the mechanical-only runs.

### 🤖 → 👤 Handoff to supervisor · since 13:46 BST

👤 16 with you · 🤖 1 queued · ⬆️ 1 unpushed

- [with you] STATE-FILE, FILES-AT-CREATION, QUERIES-FILE, PARKED-HOME, DESCRIPTION-SHAPE, ROUTE-RECEIPT, REFRESH-TARGET, INBOX-CHECK · owner · since 13:46
- [with you] PICKUP-READS, STATE-HISTORY, STEWARD-HOME, RENAME-ORDER, MIGRATE-PATH, MIGRATE-GATE, MIGRATE-SELF · owner · since 13:46
- [with you] FIELDS-MIGRATE-ORDER · owner · since 12:14
- [queued] query-review-3, blind review of the six changed medium queries · run/query-review-3 · since 13:38
- [committed] revised design note in ki-principal
- [unpushed] ki-principal, 2 commits ahead, this work's own
