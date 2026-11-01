# ki.prj.ways-of-working queries

## Open

### LAYOUT-SHAPE - Which package layout to adopt

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** Kris set on 30 October that a work package keeps only its five files at the top level, with everything else grouped, possibly group first with briefs, design and reports beneath. Three shapes fit. A, kind-first: `reports/`, `briefs/` and `design/` folders, the cheapest change, but a matter stays spread across three folders and the tidy stays file by file. B, group-first with kind subfolders, as sketched: one folder per matter with `briefs/` and `reports/` inside, which needs an estate-wide ignore exception because `reports/` is ignored at any depth. C, group-first and flat: one folder per matter, with `<run>.brief.md` and `<run>.report.md` side by side and design files under plain names, needing no ignore change. The evidence suggests the sprawl comes mainly from retention, so the group earns its cost only as the unit of tidy. No shape has been piloted. Not taken under ACCEPT-BY-CRITERIA on 31 October: it picks a shape other than the group-first layout with briefs and reports beneath that Kris sketched on 30 October, so it is Kris's call and test 3 is not met.

**Query:** Which layout should the pilot use?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: a flat matter folder tests the proposed organisational benefit with fewer structural dependencies; it adds that the pilot should use one small, explicitly bounded matter, and notes that the Context's claims about the sprawl's cause, the migration costs and the ignore behaviour were not verifiable from the packet. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; a flat matter folder tests the group as the unit of tidy with the fewest structural dependencies and avoids the ignore collision, and since nothing has been piloted the pilot takes one small, bounded matter) C, group-first and flat.

b) B, group-first with `briefs/` and `reports/` subfolders, plus the `ki-repo` ignore exception.

c) A, kind-first, with a stricter tidy cadence instead of groups.

### LAYOUT-GROUP-TIDY - Whether closing a group deletes it whole

since 2026-10-30 · from run/package-layout · [design](design/package-layout/design.md)

**Context:** Today's tidy deletes file by file, by explicit path, never folder-wide, and the steward judges each file's durable home. Under a group-first layout, a matter's files usually become homed together. The proposal is that once the steward judges a whole group closed, with outcomes homed, queries copied and design notes graduated or superseded, it deletes the group with one `git rm -r` naming that folder, in one commit, with Git keeping the history. Single-file deletion remains available. Not taken under ACCEPT-BY-CRITERIA on 31 October: it widens a deletion rule to whole folders and rests on LAYOUT-SHAPE, which stays open, so test 4 is not met.

**Query:** Should the tidy rule allow deleting one named, closed group folder whole?

**Blind review (30 October, Codex, high effort):** agrees with a) at medium confidence: one explicit group deletion is reviewable once every contained file has an evidenced disposition; it adds that before the one commit the steward enumerates the group's tracked contents and checks each file's durable home, copied queries and design-note disposition, preserving separately owned or unresolved material, because Git keeps committed versions but proves neither that knowledge was homed nor anything never committed. It recommends the policy only, not the deletion of any existing folder. Confidence lifted to high.

**Options:**

a) (recommended, confidence high - reviewed; one named group deletion stays reviewable when every file in it has an evidenced disposition checked before the commit, and Git keeps history; it widens a deletion rule, deletes no existing folder by itself, and is untested) Yes: a steward may delete one named, closed group in one commit.

b) No: keep file-by-file deletion inside groups.

### IDEAS-REVISIT - Where a future idea lives

since 2026-11-01 · from IDEAS-ROADMAP-PRINCIPLE in the interactive pass; replaces it · to shape with the empty-board design

**Context:** On 31 October Kris said "future ideas could go into the knowledge graph in a way, rather than saying these are things which we're enacting for now" (IDEAS-IN-GRAPH). On 1 November Kris was no longer sure what was meant: ideas may relate to roadmap items, ways of working, work packages and Projects, and perhaps a future idea is "just part of a card at the bottom of it ... things we need to go away and look at in the future in respect to this area". The roadmap standard still offers `Idea:` bullets and `_IDEAS.md`; the capture skill follows IDEAS-IN-GRAPH. IDEAS-HOME in the empty-board design is still open.

**Query:** Where should a future idea live?

**Options:** to be drafted by the empty-board design and reviewed before it comes back; candidates are a "future" section at the foot of the card, Project or work package it concerns, future concepts in the knowledge graph, and the roadmap's idea places as now.

### HOOK-PATCH - Treat a leftover lint-staged patch like a leftover stash

since 2026-11-01 · from run/hook-nostash

**Context:** With `--no-stash`, lint-staged no longer makes a backup stash. While its checks run, it still sets aside the unstaged part of any partly staged file, and it now keeps that part in a patch file at `.git/lint-staged/<id>/unstaged.patch`. In the scratch test, killing lint-staged at that moment left the working file without those edits. Only the patch held them, and `git apply` brought them back exactly. A normal Ctrl-C did not cause this. The standards now cover a leftover `lint-staged automatic backup` stash, but they say nothing about this patch, so an agent tidying `.git` could delete someone's only copy of their unstaged edits.

**Query:** Should the `ki-delegation` standard and the coordinator style also say that a leftover `.git/lint-staged/` patch is reported, never deleted or applied by an agent?

**Options:**

a) (recommended, confidence medium - the loss was reproduced in the scratch repository, but needing a hard kill makes it rare) Add it to the same sentence in both places, so a leftover patch is reported to its owner like a leftover stash and never deleted or applied by an agent, in a small follow-up run.

b) Leave the standards as they are and rely on the general rule against touching other sessions' files.

### SWEEP-GATE - What "both Macs level" means before each repository is swept

since 2026-11-01 · from run/discussions-plan

**Context:** On 31 October Kris asked that the rename sweep wait until "host sync has both Macs level", to avoid clashes between the two Macs, sol and terra. Host sync is not yet running routinely. Sol's sync loop stopped at its session restart on 31 October and has not resumed, and no host-sync executor or schedule has been chosen. A wholesale move of every repository to `~/world/<territory>/<repo>` is also being prepared. The sweep renames a file in 60 work packages across 9 repositories. If either Mac holds unpushed changes to those packages, or the move happens mid-sweep, the two copies drift apart and someone has to merge them by hand.

**Query:** Should each repository's sweep wait for a one-off check that that repository is clean and level on both Macs, or wait until host sync runs routinely and the repository move is finished?

**Options:**

a) (recommended, confidence medium - it meets the aim of Kris's words without waiting on host sync, which has no date; but it reads "host sync" as a check rather than the running service) Just before each repository's run, each Mac's Rig thread or Kris makes a fresh one-off check that the repository is committed, pushed and level on both Macs. The run then renames and pushes at once, and the other Mac pulls before any coordinator there writes. No sweep runs while the `~/world` move is under way.

b) Hold the whole sweep until host sync runs routinely on both Macs and the `~/world` move has finished. The readers and writers (U1 to U5) go ahead meanwhile, and the old and new names live side by side until then.

### HOST-SYNC-CLOSE - Close the parked host-sync design too?

since 2026-11-01 · from run/stocktake

**Context:** On 1 November you closed the four HOST-* questions as superseded: "I think we've moved on from some of these points ... it's a step back from where we are now". Each Mac's Rig sync thread now runs every 15 minutes, with terra seven minutes after sol, and repeats until the Mac and GitHub are level. Sol leads Knowledge Islands, Personal and Legal. One older parked query, HOST-SYNC, still asks which primary or secondary order and offset hosts should publish in, which that rule has already answered. While it stays parked, six design notes stay with it: `host-sync-and-reply-trades`, `host-sync-report` and the four in `host-sync/`. Deleting them is undone easily from Git. One Observatory report links `host-sync-and-reply-trades` by local path.

**Query:** Should the parked HOST-SYNC query be closed as superseded by the same 1 November words, so that the host-sync design notes can go at the next mark?

**Options:**

a) (recommended, confidence high - your 1 November words and the 31 October answers already settle its order, offset and lead host, and Git keeps the notes) Close HOST-SYNC as superseded. Delete the six notes at the next mark, pointing the Observatory report's link to the notes' last revision. Keep `host-reconcile/plan.md` until the sol Rig thread has received the IMPORTANT line that links it.

b) Keep HOST-SYNC parked and the six notes with it until a later design discussion.

### CITED-NOTES - Delete graduated notes that other files still link to?

since 2026-11-01 · from run/stocktake

**Context:** Five design notes have done their job, because their decisions now live in the skills, but other files still link to them by local path. `coordination-lessons` and `method-feedback` are listed as sources by three harness skills that this work owns. `gfm-migration`, `unattended-work` and `work-id-shape-plan` are linked from the tools-burndown, Personal State of play, baseline-rollout and Observatory packages. Deleting a note breaks those links. The standard already handles a removed record the same way: it links the last version on GitHub. Moving a note to a topic folder breaks the links just as deleting it would.

**Query:** May these five notes be deleted once every link to them points to the note's last version on GitHub?

**Options:**

a) (recommended, confidence high - it is the same pinned-link rule the standard uses for pruned records, and nothing is lost from Git) Yes. A run repoints the three harness source lists itself and sends each other package one message line with its pinned link. The notes are deleted at the mark after those links land.

b) No. Keep the five notes until the Project closes.

### OLD-PROPOSALS - What to do with five proposals never decided

since 2026-11-01 · from run/stocktake

**Context:** Five design notes from 21 to 27 October were never adopted or dropped:

- `tags-model`, on subject tags.
- `gov-227-storage-schema`, a storage-schema draft for the [KI-HARNESS-GOV-227](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-227-repository-storage-declarations.md) idea.
- `overload-process`, on what to do when you are overloaded.
- `observatory-review`, a review view in the Observatory, already listed in the Observatory's own ideas file.
- `agent-control-contract`, accepted on 21 October as a tools-ki build contract, though I could not prove it was delivered.

Under IDEAS-IN-GRAPH, future ideas belong in the knowledge graph, not in a work package. Where ideas finally live (IDEAS-HOME) is still open.

**Query:** Should these five become one-line ideas, with the notes then deleted, or stay where they are?

**Options:**

a) (recommended, confidence medium - it empties the folder without losing the ideas, but IDEAS-HOME, which decides their final home, is still open) Record each as one line in the current ideas list, `design/empty-board/ideas.md`, linking the note's last version on GitHub. Leave GOV-227 and the Observatory review view where they already are. First check `agent-control-contract` against tools-ki, and delete only if it was delivered. Then delete the notes.

b) Keep all five in `design/` until IDEAS-HOME is settled.

### TOPIC-SET - Which topic folders to pilot

since 2026-11-01 · from run/stocktake

**Context:** On 1 November you said this work's folders "should really be aligned to the topic", each holding its briefs, design and reports. Once the deletions above are made, what is left falls into the 13 topics in the Findings table. Fine-grained topics close and can be deleted whole sooner, for example `discussions/` once its rollout lands. Coarser topics would mean fewer folders to look through: `work-package/` could take package layout, package definition and discussions, and `agents/` could take landscape, Orca and listening. Whether each topic has `briefs/` and `reports/` subfolders or keeps them side by side stays with LAYOUT-SHAPE.

**Query:** Should this package's pilot use the 13 proposed topics, or a coarser set?

**Options:**

a) (recommended, confidence medium - small topics match how the work closes and make each folder a natural unit to tidy, but you asked for simplicity and fewer folders also serve that) The 13 topics as proposed.

b) A coarser set of about eight: `work-model/`, `work-package/`, `capture-model/`, `empty-board/`, `agents/`, `host-sync/`, `nascent-areas/` and `publication-recovery/`, with `window-31-oct/` folded into `work-model/`.

### PILOT-CONTRACT-LINE - Tell the Orca evaluation about the extra pilot checks

since 2026-10-31 · from run/a-3 · from stocktake; blind review needed

**Context:** Row 2 already sent the ORCA-SUBAGENT-PILOT line to [ki.prj.orca-evaluation's messages](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/messages.md), using the wording drafted before the review. That line asks four things: whether the worker nests in the list, whether it runs without prompts, whether it survives the chat ending, and what it leaves in the inbox. The blind review on ORCA-PLACEMENT added three checks that the pilot must also cover: the run's directories, running without anyone at the keyboard, and authority limits, so that too much access fails as well. These are now in the design note, and the line links to that note, but the line itself does not mention them. The pilot could run without them, and then Part B's route could not be confirmed. This run sent nothing, because the row only asked for the design note.

**Query:** Should the coordinator send ki.prj.orca-evaluation a short follow-up line adding the three checks to the pilot?

**Options:**

a) (recommended, confidence medium - the line is cheap and easy to withdraw, and without it the pilot may miss what the route decision depends on; but it goes beyond the row, so this is the coordinator's call) Send one follow-up line to ki.prj.orca-evaluation's `messages.md` naming the three checks and pointing to section 3 of the design.

b) Send nothing, and rely on the pilot reading the linked design note.

### SYNC-UNPUSHED-EXIT - Should leaving a branch unpushed make sync report failure?

since 2026-10-31 · from run/b-U5 · from stocktake; blind review needed

**Context:** By default sync now leaves branches that are only ahead unpushed. I counted these as "skipped" but let the run finish successfully (exit status 0), the same way sync already treats a pull or push the user declines under `-i`. Other skips, such as local changes or divergence, still make sync exit with status 1. A script that relied on sync's exit status to spot unpublished commits would now have to read the summary at the end. The decision's words say nothing about exit status, so this was my call. It is recorded in [KI-TOOL-MGIT-CLI-033](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-033-sync-push-guard.md) for review.

**Query:** Should an unpushed branch leave sync's exit status successful, as delivered?

**Options:**

a) (recommended, confidence medium - not pushing is now the intended default, so failing every routine run on a repository with local commits would make the exit status meaningless) Keep it as delivered: unpushed branches are reported and counted as skipped but do not fail the run.

b) Make an unpushed branch fail the run (exit status 1), like the other skips, so scripts notice unpublished commits.

### CHECKSUMS-SETTLED - CAPTURE-LEAN also answers the checksum choice

since 2026-11-01 · from run/capture-settled · from stocktake

**Context:** CAPTURE-LEAN was read back in Acquire as "there is no `original.txt` and no checksum file". That covers the brief's CHECKSUMS choice, whose recommended option is to stop writing `SHA256SUMS` for intake captures. This run's brief said to settle only LEAN-CAPTURE and to leave the other choices open with their wording unchanged, so CHECKSUMS is still shown as open.

**Query:** Should the brief also mark CHECKSUMS as settled by CAPTURE-LEAN before the blind reviews?

**Options:**

a) (recommended, confidence high - the read-back says it in so many words, and reviewers would otherwise test something already decided) Yes: a one-line follow-up marks CHECKSUMS as settled for intake captures, quoting CAPTURE-LEAN, and leaves each other route guide to keep or drop the file on its own terms.

b) No: leave CHECKSUMS open for the reviews.

### OBS-FEEDBACK-LINE - Should the Observatory also send feedback as a message line?

since 2026-10-31 · from run/listen-and-awake · from stocktake; blind review needed

**Context:** Under FEEDBACK-AS-MESSAGE on 31 October 2026, Kris said "we can probably drop the feedback idea. We just send a message with it instead." I replaced the hand-written and steward-written feedback files. The Observatory's own feedback-sending feature still writes a separate feedback file plus a message line linking it. It is shipped under its own decision, PDR-KI-OBSERVA-007, and owned by the Observatory work, so I left it alone and kept those files readable for now. Until the Observatory changes, the method has two routes for owner feedback.

**Query:** Should this work send the Observatory work a message asking it to send feedback as a message line only, so that the separate feedback file can be retired?

**Options:**

a) (recommended, confidence medium - it matches Kris's words and removes the second route, but the Observatory may need the separate file for comments anchored to passages, which I have not checked) Send one line to the Observatory work's `messages.md`, asking it to move `feedback-send` to message lines and then retire the `feedback/` kind.

b) Keep the Observatory's feedback file as the one exception, and retire nothing.

### WP-HEARTBEAT - Bring the Work Process note into line with the quiet watcher

since 2026-10-31 · from run/quiet-listen · from stocktake

**Context:** The harness standard no longer has a timed heartbeat. A run finishing, or a new message, is now the only thing that wakes the thread. The [Work Process note](</Users/krisbrown/kis/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) in Knowledge Islands Principal still says, under "Stuck and the heartbeat", that a heartbeat gives "an update on change, at least every 5 minutes and always by 10". That note is canonical content, so changing it goes through the Enactment Process, and this run had no authority in that repository.

**Query:** Should the Work Process note's heartbeat paragraph be changed to match QUIET-LISTEN?

**Options:**

a) (recommended, confidence high - QUIET-LISTEN explicitly replaces the timed heartbeat updates, and the note is the model the standard cites) Yes. Launch a bounded run in Knowledge Islands Principal that rewrites the paragraph so the heartbeat wakes only when a run finishes, citing QUIET-LISTEN as the owner instruction for the Enactment Process.

b) Leave the note as it is for now, and accept that it disagrees with the standard until a wider model refresh.

### RESTART-POLICY - How should the two restart policies coexist?

since 2026-10-31 · from run/restart-review · from stocktake; blind review needed

**Context:** The landed restart rule responds to Kris's immediate enactment instruction through identity changes, repeated compaction and method changes. It excludes age or length alone and can repeat until declined. The parked RESTART design instead proposes four hours or 100 evidenced messages, a single reminder at a safe boundary and no repetition; it remains explicitly design-only. Neither the delivery nor this review answers that query.

**Query:** Should the landed categorical policy remain the current rule while the numerical design stays separately parked?

**Options:**

a) (recommended, confidence medium - preserves the explicit immediate delivery without treating an unanswered design proposal as adopted) Retain the categorical policy for now, record that it does not settle RESTART, and reconcile triggers, safe timing and repetition explicitly before any future numerical adoption.

b) Commission one combined design revision now, covering categorical and numerical triggers, evidence, safe boundaries and repetition, for Kris's review before any further implementation.

c) Request a scoped revision replacing the categorical policy with the numerical proposal; first decide its values, evidence requirements and implementation authority explicitly.

### RESTART-EVIDENCE - Qualify the trigger rationale as a workflow convention?

since 2026-10-31 · from run/restart-review · from stocktake

**Context:** The standard makes categorical necessity claims about a second compaction, changed identity and changed method. The reviewed evidence and passing source tests establish a coherent written rule, but do not validate improved session quality or prove that in-session correction cannot suffice. The parked numerical design already acknowledges this distinction.

**Query:** Should a later authorised wording revision qualify these triggers as provisional workflow heuristics rather than proven necessities?

**Options:**

a) (recommended, confidence high - brings the rationale into line with the evidence without selecting a new threshold or silently changing behaviour) Commission a bounded wording revision describing the triggers as reversible workflow conventions, remove universal claims about fidelity and impossibility of in-session correction, and retain owner discretion; review behavioural changes separately under RESTART-POLICY.

b) Keep the present wording pending specific evidence that validates the claimed necessity and the second-compaction cutoff.

### SPLIT-COMMIT - The split was published inside another session's commit

since 2026-10-31 · from run/worker-wait-split · from stocktake

**Context:** The brief asked for `queries.md` to be committed alone under "docs(work): ki.prj.ways-of-working split WORKER-WAIT". Before this run committed, another session's host-sync review commit `76beec53` swept the uncommitted `queries.md` into its own commit and pushed it. The content on origin is exactly this run's split; only the commit subject is misleading for that file.

**Query:** Is the split accepted as published under that commit, or should a marker be added?

**Options:**

a) (recommended, confidence high - the content is identical and on origin, and the only correction possible without rewriting history is a note) Accept it as published; the coordinator records in the decisions log, at its next receive, that `76beec53` carries the WORKER-WAIT split.

b) Add an empty commit with the brief's subject that names `76beec53` as carrying the split.

### CLOSE-BLOCKED - The two stale runs cannot close

since 2026-10-31 · from run/wow-tidy · from stocktake; blind review needed · may have been overtaken by later closes; check before answering

**Context:** `ki agent close` refuses both runs for two reasons. First, the package folder has untracked files, which are the reports kept above and newly finished run reports. Second, decisions in `decisions.md` have no recorded home: 13 named for `ways-of-working-reg` (DIAGRAM-AGREED, MOVE-PROMPT-SHAPE, STOP-FOR-MOVE-WOW, ORCA-FIT, LANDSCAPE, ORCA-SUBAGENTS, AWAY-31-OCT and the dated receive entries) and 72 for `ways-sol-resume-20261029`. Homing each decision through `ki agent reconcile` is a judgement on live decisions, outside a tidy. `--reconciled` would waive the check, but nothing authorises a waiver. A side effect remains: three sol reports now sit untracked in the package root as their only copies.

**Query:** How should the two stale runs be closed?

**Options:**

a) (recommended, confidence medium - the decision homes need the steward's judgement, and committing the three sol reports keeps them safe in Git) Have the coordinator receive the new reports and commit the three returned sol reports into `reports/`. Then run one bounded reconcile pass that records each decision's home or class with `ki agent reconcile`, and retry both closes.

b) Close both with `--reconciled` under an explicit owner waiver. The close note records the waiver, and the decision-home check is left to the next mark.

### AGENT-HOME-IDEA - Who writes the Techné dispatch `Idea:` line

since 2026-10-31 · from run/landscape-rollout · from stocktake; blind review needed

**Context:** AGENT-HOME a) also says "Record Techné dispatch agent an `Idea:` line on Techne theme page". The Techne theme page lives in `Streams/Themes/techne.md`, and no work package's routing description claims it. Root `AGENTS.md` sends work that no package owns to State of play's `messages.md`.

**Query:** Should the `Idea:` line go to ki.sop.main as a message, or should this package write it itself?

**Options:**

a) (recommended, confidence medium - AGENTS.md routes unowned work to State of play, but this package may already own theme-page edits for its decisions) Send one line to ki.sop.main's `messages.md`.

b) This package's coordinator adds the line itself in a bounded run.

### ORCA-REACH-VEGA - Tell ki.prj.agent-host about the `vega` launcher choice

since 2026-10-31 · from run/landscape-rollout · from stocktake; blind review needed

**Context:** ORCA-REACH a) keeps `ki agent` as the only launcher on `vega`, by choice. ki.prj.agent-host builds and runs `vega`. The line went only to ki.prj.orca-evaluation, which owns Orca use.

**Query:** Should ki.prj.agent-host also get a line about ORCA-REACH?

**Options:**

a) (recommended, confidence medium - the decision constrains vega's launcher, but the brief named only the Orca owner) Send one ORCA-REACH line to ki.prj.agent-host's `messages.md`.

b) Leave it with ki.prj.orca-evaluation only.

### WIP-PACKAGE - How many units may a package have in flight?

since 2026-10-31 · from run/ideas-board · from stocktake

**Context:** Overnight this package ran up to three units at once, as the current "keep about three agents running" rule allows. You asked for one at a time where possible, finished quickly. A unit's independent review is a separate run, but it works on the same change.

**Query:** How many units may one work package have in flight at a time?

**Options:**

a) (recommended, confidence high - it is your WIP-LIMIT answer written down, and allowing the review keeps reviews independent without a second piece of work) One unit at a time, plus at most one independent review of that same unit.

b) One unit at a time with nothing alongside it, reviews included.

c) Up to two units at a time where they touch different repositories.

### WIP-TERRITORY - How many packages may be active across the territory?

since 2026-10-31 · from run/ideas-board · from stocktake; blind review needed

**Context:** The current cap is "three or four" Project packages, not counting State of play; today five packages are neither on hold nor finished, one being worked and four waiting on you. A package waiting on you would count as active under this proposal, so that answering frees a slot.

**Query:** How many work packages may be active at once across the Knowledge Islands territory?

**Options:**

a) (recommended, confidence medium - it tightens the existing cap to its lower bound without stopping you working on more than one thing a day, though "minimal parallelisation" could mean one) At most three Project or regular packages, plus State of play, with packages waiting on you counting as active.

b) One package at a time, plus State of play: strictly serial.

c) Keep "three or four", with packages waiting on you not counted.

### ROADMAP-UPCOMING - Should the roadmap hold only upcoming work?

since 2026-10-31 · from run/ideas-board · from stocktake; blind review needed

**Context:** Records can sit on the roadmap with horizon `soon`, `future` or `hold`, and done records stay until pruned. Today 19 of 22 records are finished, held, in triage or tied to work that is not moving. Making the roadmap hold only `now` and `next` would turn the other horizons into ideas, which needs the roadmap standard and its checker changing in the harness and tools-ki.

**Query:** Should a roadmap hold only records that are coming up next, with everything else moved back to ideas?

**Options:**

a) (recommended, confidence medium - it is what EMPTY-BOARD asks for, but it changes a standard and a checker that other territories also use) Yes: only `now` and `next` stay, capped at three per repository and ten across the territory; `soon` and `future` records go back to ideas, and held records go back to ideas unless their release is in sight within a fortnight.

b) Keep the horizons as they are, but count only `now` and `next` as upcoming, and cap those.

### GATES - Are the two gates right?

since 2026-10-31 · from run/ideas-board · from stocktake; blind review needed

**Context:** Section 3 proposes Gate 1 (idea to upcoming: you say yes, it has a home, the next step is known, it is small, and there is room) and Gate 2 (upcoming to active: it is Ready, nothing it needs is missing, and the package and the territory have a free slot). Most of these already exist in `ki-next` and `ki-plan`; the new parts are the size rule and the room checks.

**Query:** Should the two gates in section 3 be adopted as written?

**Options:**

a) (recommended, confidence medium - most of each gate restates existing rules, and the new size and room checks are easily relaxed later) Adopt both gates as written.

b) Adopt them without the size rule, so larger work can be adopted and split later.

### PARKED-TO-IDEAS - What happens to parked queries?

since 2026-10-31 · from run/ideas-board · from stocktake; blind review needed

**Context:** 120 parked queries sit in nine packages with no age limit; several point at records that no longer exist, and eight here are duplicated. A parked query is a decision nobody is currently making, which is what an idea is. Moving one keeps its recommendation, so nothing is lost.

**Query:** Should parked queries move to the ideas list?

**Options:**

a) (recommended, confidence medium - it empties the Parked sections and stops stale decisions piling up, but some parked queries are close to answerable and might be better brought back) Yes: at each package's next mark, each parked query moves to the ideas list with its recommendation, and the Parked section goes.

b) Keep Parked sections, but offer any parked query older than 30 days for dropping at your next review.

### HOLD-CLOSE - What happens to packages on hold?

since 2026-10-31 · from run/ideas-board · from stocktake; blind review needed

**Context:** Nine packages are on hold, six of them since 18 to 20 October. While held they still receive messages they cannot act on, such as the ORCA-ENV-LEAK security fix waiting in tools-burndown. Closing a held package would home its decisions, move its messages and parked queries to the ideas list and remove its folder, leaving the Project `paused`; reopening means creating a fresh package.

**Query:** Should a package on hold for more than 14 days be closed out?

**Options:**

a) (recommended, confidence low - it clears the board fastest, but closing a package is hard to undo cleanly and several held packages, such as tools-burndown, hold live handoffs) Yes, after you have seen what each would close, one package at a time.

b) No: keep held packages, but route new messages for a held package to State of play instead, so nothing waits behind a hold.

c) Keep held packages as they are.

### QUICK-FIXES - Fix the easily undone contradictions now?

since 2026-10-31 · from run/ideas-board · from stocktake; blind review needed

**Context:** Three contradictions can be fixed in Knowledge Islands Principal alone, each easily undone: nine Project pages whose `lifecycle` disagrees with their package (seven `active` but on hold, two `active` with no package); the finished Knowledge acquisition folder, which the standard says should already be gone and whose history Git keeps; and the eight duplicated parked entries in this package.

**Query:** Should one small run make these three fixes now, as a bounded change you approve?

**Options:**

a) (recommended, confidence medium - each fix is small, within this island and recoverable from Git, though the lifecycle wording for held Projects needs a choice between `paused` and keeping `active`) Yes: set the seven held Projects to `paused` and the two packageless ones to `planned`, remove the Knowledge acquisition folder, and remove the duplicate entries.

b) Fold them into the wider rollout instead, after the standards change.

### DONE-PRUNE - Prune the seven finished records?

since 2026-10-31 · from run/ideas-board · from stocktake; blind review needed

**Context:** Seven records are done and accepted but still on their roadmaps: [KI-OBSERVA-BRG-004](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md), [KI-HARNESS-GOV-232](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-232-any-package-coordination.md), [KI-HARNESS-GOV-233](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-233-typed-work-naming-readers.md), [KI-HARNESS-GOV-234](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-234-footer-markdown-writers.md), [KI-TOOL-KI-CLI-173](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-173-regular-coordination-readers.md), [KI-TOOL-KI-CLI-174](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-174-typed-work-naming-readers.md) and [KI-TOOL-KI-CLI-175](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-175-footer-markdown-writers.md). Pruning is yours to approve; it removes the file from the roadmap and Git keeps it.

**Query:** Should the seven done records be pruned now?

**Options:**

a) (recommended, confidence medium - they are closed and pruning is recoverable from Git, but this run has not rechecked each one's closure evidence) Yes, through `ki-accept`'s prune, each repository in turn, after a check that each closure is complete.

b) Leave them until each owning work's next mark.

### PRINCIPAL-READOPT - Whether the 22 records that left adoption are re-adopted

since before 25 October 2026 · from run/fields-personal-principal · from stocktake; blind review needed

**Context:** The rule turned `horizon: triage` into `status: triage` for 22 drafts. In this Capital, that draft-on-triage combination already meant captured intake, so the meaning holds, but leaving triage now needs your approval. Five are date-bound and now fall outside selection: the half-term break ([KB-PRINCIPAL-018 (pruned)](https://github.com/krisb/personal-principal/blob/acd6e5c73c58b88a486c7c23805949fdb2515e1b/Streams/Roadmap/KB-PRINCIPAL-018-plan-half-term-break-with-lauren.md)), Halloween ([KB-PRINCIPAL-019 (pruned)](https://github.com/krisb/personal-principal/blob/b10b24dff565565536dffaa9d6b6d3e343df7983/Streams/Roadmap/KB-PRINCIPAL-019-plan-halloween-activity.md)), Lauren's birthday ([KB-PRINCIPAL-024 (pruned)](https://github.com/krisb/personal-principal/blob/b10b24dff565565536dffaa9d6b6d3e343df7983/Streams/Roadmap/KB-PRINCIPAL-024-plan-laurens-birthday.md)), the railway tickets before expiry ([KB-PRINCIPAL-025 (pruned)](https://github.com/krisb/personal-principal/blob/acd6e5c73c58b88a486c7c23805949fdb2515e1b/Streams/Roadmap/KB-PRINCIPAL-025-use-north-york-moors-railway-tickets.md)) and your daughter's birthday on 27 October ([KB-PRINCIPAL-027 (pruned)](https://github.com/krisb/personal-principal/blob/acd6e5c73c58b88a486c7c23805949fdb2515e1b/Streams/Roadmap/KB-PRINCIPAL-027-mark-daughters-october-birthday.md)).

**Query:** Should the five date-bound records be adopted now while the other 17 stay in triage?

**Options:**

a) (recommended, confidence medium - the mechanical result matches the old meaning, but the dated items fall before their next likely review) Adopt the five date-bound records now through `ki-next`, as `draft` at Now or Next with the proposed kind and size, and leave the other 17 in triage for ordinary intake review.

b) Leave all 22 in triage until the next personal triage review.

c) Adopt all 22 again at once through `ki-next`, each with a horizon chosen afresh.

### PRINCIPAL-KIND-SIZE - Confirming the proposed kind and size

since before 25 October 2026 · from run/fields-personal-principal · from stocktake; blind review needed

**Context:** The table above proposes a kind for the 6 adopted records that lack one, a kind for each of the 26 triage records to set at adoption, and a size for 33 records. [GDR-KI-PRINCIPAL-016](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-016-priority-and-size-on-work-records.md) makes these the owner's judgement. Until the `ki` release that accepts the fields, a writer leaves out any field the installed `ki` rejects. The harness already accepts `size`, as [KB-PRINCIPAL-045 (pruned)](https://github.com/krisb/personal-principal/blob/8f33dbb7cb00afda9b4abd186de15721bf02c37a/Streams/Roadmap/KB-PRINCIPAL-045-redraw-mermaid-diagrams-in-archify.md) shows.

**Query:** Do you confirm the proposals, with any changes, so that a follow-up run can write them?

**Options:**

a) (recommended, confidence medium - the sizes are provisional judgements from each record's Goal and Boundary, and are revisited before Ready anyway) Confirm them as listed. A short follow-up run then writes the 33 sizes and the 6 adopted kinds now, and the triage kinds are set at adoption.

b) Confirm them with the changes you name, for example `xl` on [KB-PRINCIPAL-004 (pruned)](https://github.com/krisb/personal-principal/blob/b10b24dff565565536dffaa9d6b6d3e343df7983/Streams/Roadmap/KB-PRINCIPAL-004-develop-intentional-life-thesis.md).

c) Hold all kind and size writes until the `ki` release, and write them together with the other repositories.

### STREAMS-CHECKER-GAP - The Streams checker cannot see the migrated fields

since before 25 October 2026 · from run/fields-personal-principal · from stocktake · may have been overtaken; check before answering

**Context:** The Streams checker, both installed and in the workspace at `88cce3e5`, does not warn on a retired horizon, on `initiative` or on a theme beside a Project. It lists `initiative` as a known field. The standard's migration window says the checkers warn on all three, and the window closes on "a complete scan of that inventory showing no gaps", so a scan of Streams Capitals would wrongly report no gaps. This matches VALIDATOR-PARITY, which ki.tools-burndown holds.

**Query:** Should the coordinator route this gap to the harness owner before the remaining Streams migrations?

**Options:**

a) (recommended, confidence high - verified directly: the before and after audits gave the same 34 warnings, and the workspace `streams.ts` has no rule for these shapes) Route it now as a Messages line to the harness work that owns the checkers, and have each remaining field run prove its result with a front-matter scan, as here.

b) Fold it into the next harness release run, and carry on with the front-matter scans meanwhile.

### Z-FILES - Keep the two Z files uncommitted

since 2026-11-01 · from run/wow-cleanup

**Context:** The brief asked for every never-committed report, including those in `reports/`, to be committed first. Only two such files are in `reports/`: `hold-request-20261030-z.md` and `z-session-retirement-20261030.md`, about retiring the Z session. The stock-take said to keep them out of any commit until PUBLIC-REPORT-AUDIENCE and PUBLIC-REPORT-RECOVERY are settled. Both questions were answered "a" on 1 November and are waiting for Kris to name the permitted audience and a private destination. Committing them and pushing would publish them to GitHub. I left them untracked and unchanged, so they are still the only copies.

**Query:** Should the two Z files stay uncommitted until the public-report questions are settled?

**Options:**

a) (recommended, confidence high - pushing them would publish material whose audience Kris has not yet named, and leaving them as they are changes nothing) Keep them uncommitted until PUBLIC-REPORT-AUDIENCE and PUBLIC-REPORT-RECOVERY are settled, then dispose of them as that decision says.

b) Commit them into `reports/` now, so Git keeps a copy, and accept that they become public.

### SWEEP-NOTE-LINKS - Tell two roadmap records where `roadmap-sweep` went

since 2026-11-01 · from run/wow-cleanup

**Context:** Two records outside this package link to `design/roadmap-sweep.md`, which was deleted as superseded: [KI-OBSERVA-BRG-004](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md) (line 89) and [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) (line 90). Both links were already broken before the deletion, because they use the old `~/workspaces/.../ki.ways-of-working/` path. The stock-take did not list them, so this run left them alone. The note's last version is in Git at `f8c70a30`. KI-OBSERVA-BRG-004 is also proposed for pruning under DONE-PRUNE.

**Query:** Should the owning works be told the note's pinned link?

**Options:**

a) (recommended, confidence medium - it costs one message line each and lets the owners decide, but the links were already broken and one record may be pruned soon) Send one line to the `messages.md` of the Observatory work and of the work that owns Rig, giving the pinned link `https://github.com/knowledgeislands/ki-principal/blob/f8c70a3000cdd7a531811ffe363884489eda0e50/+/_WORK/ki.prj.ways-of-working/design/roadmap-sweep.md`.

b) Leave them, since both links were already broken and the records are finished.

### ORCA-ADAPTER-WHEN - When to create the Orca adapter

since 2026-11-01 · from run/rename-paperclip

**Context:** Kris chose the delegation family on 1 November: `ki-delegation` as the shared contract, with an Orca adapter and a Paperclip adapter. The Paperclip adapter now exists under its new name. The Orca adapter doesn't exist yet. Writing it means describing how Orca carries out the shared contract (launch, queue, status, recovery, cleanup). That contract is still being slimmed, and the [Orca evaluation](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/state.md) hasn't yet tested a remote run.

**Query:** Should `ki-delegation-orca` be written now, or after the slimmed `ki-delegation` contract and the Orca evaluation's trial have landed?

**Options:**

a) (recommended, confidence medium - the adapter would otherwise describe a contract that is still changing and Orca behaviour nobody has tested) Wait: commission it as one harness run once the slimmed `ki-delegation` contract has landed and the Orca evaluation has reported, and write it from that evidence.

b) Write a minimal skeleton now: a skill that names its boundary, points to `ki-delegation` and records the open questions, then fill it in after the trial.

## Answered

- TOP-LEVEL-NOW - a; TOP-LEVEL-SWEEP-DELETE - a; TOP-LEVEL-SWEEP-MOVE - a, SWEEP-SCOPE all 17; DISCUSSIONS - b; SYNC-SNAPSHOT-ADOPT - a; WORKER-WAIT-MEANING, -QUEUED, -GATED, -DELIVERY - a; HOST-CADENCE, -COVERAGE, -SECONDARY-PUBLISH, -READBACK superseded; INBOX-ARMED, -CADENCE closed, INBOX-VERB, CODEX-WAKE, SENDER-NUDGE - a; ACQ-TEXT-RECHECK, HOLDING-SCOPE-INTERIM, IDEAS-ROADMAP-HOME, ACQUISITION-PROCESS-NOTE, CAPTURE-MODEL-SETTLED - a; UNLOGGED-QUERIES, DESIGN-GRADUATION, BROKEN-LINKS-LIVE - a under LAYOUT-TOPIC; RENAME-NAME - a ; HOOK-STASH - a; FINISHED-TIDY-KICK - a; ORCH-NAME-DISPATCH - a; PUBLIC-REPORT-AUDIENCE, -RECOVERY - a, awaiting audience and destination; WAKE-HOST - c, sync threads suffice; HOLDING-SCOPE-CARDS - cards mature in Acquire, no rush, move once home decided; IDEAS-ROADMAP-PRINCIPLE folded into IDEAS-REVISIT; BROKEN-LINKS-HISTORY - a (all 1 November 2026; see decisions.md).
- TOP-LEVEL-SWEEP-DELETE - a (1 November 2026): only stewards delete old reports.
- TOP-LEVEL-NOW - a (1 November 2026): reports into `reports/` now.
- ORCA-REACH - answered a) on 30 October 2026, follow-up due 6 November 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- AGENT-HOME - answered a) on 30 October 2026, follow-up due 2 November 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- WAKE-SESSION - answered a) on 30 October 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- WAKE-DURABLE - answered a) on 30 October 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- WORKTREE-OPTOUT - answered a) on 30 October 2026; see [Owner answers](decisions.md#owner-answers-30-october-2026-0615-gmt).
- HOST-REVIEW - supply the missing common-brief review packet. Answered a) on 30 October 2026, "proceed with the recommendation, then refine additional HOST-* based on that review"; see [Owner answers, 30 October 2026, 06:15 GMT](decisions.md#owner-answers-30-october-2026-0615-gmt). Delivered as the [merged host-sync report](design/host-sync/report.md).
- ORCA-ENV-LEAK - acted on 30 October 2026 under Kris's ORCA-SUBAGENTS words: sent to ki.prj.tools-burndown; see [ORCA-SUBAGENTS](decisions.md#orca-subagents---ki-agent-runs-appear-as-orca-sub-agents-30-october-2026-1610-gmt).
- WORKER-WAIT-MIDTURN - An orchestrator turn moves nothing. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- AMEND-RACE - Guard amends in a shared checkout. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCH-NAME-THREAD - answered b) by Kris on 31 October 2026, keep `ki-coordination` and `ki-coordinator`; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- LAYOUT-PILOT-ORDER - When the pilot moves files. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- REVIEW-CHALLENGE - Let reviews challenge earlier decisions, visibly. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- REVIEW-LIFT - Precedent earns no confidence. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- READ-FEEDBACK-NOW - Feedback packages before the Observatory can write them. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCA-CLOSE-OUT - Make worker release part of KI coordinator close-out. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCA-SUBAGENT-PILOT - Prove the Orca worker path before changing tools-ki. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCA-PLACEMENT - Which Orca route Part B takes. Taken a) under ACCEPT-BY-CRITERIA on 31 October 2026; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).
- ORCA-QUEUE - answered a) by Kris on 31 October 2026, Orca first while the parent chat is live, detached otherwise; see [Owner answers during AWAY-31-OCT](decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026).

## Parked

- HOMES - Existing packages default to the territory Capital, with approved regular/ad hoc exceptions. Local keys and canonical repository identities differ. Explicit metadata must not create a new home or permission. Recommended: a) (confidence high - portable identity and existing authority remain distinct) Use the HOMES model above: optional matching `territory`, omitted `canonical_home` derives Capital, explicit null stays unresolved, supplied identities must resolve uniquely and exceptions retain their approval requirements.
- EXECUTION - The owner means where work is meant to be running and illustrates the chezmoi repository footprint. Both earlier reviews prefer plural execution hints; neither establishes support in current readers. One declared default can supply a verified launch working directory without replacing canonical package home, explicit unit targets or authority. Recommended: a) (confidence medium - meets the owner's execution intent with lean semantics; launch compatibility remains unproved) Keep singular `execution_home`, unspecified when absent/null, as one default repository/context that can supply a verified launch working directory after explicit work selection, host requirements and unit authority checks. Preserve explicit unit targets and overrides; resolving the directory grants no write authority. Current readers need separately authorised compatibility work; no binding or directory change happens here.
- HOST - Device constraints already resolve through inventory, while live placement stays out of packages. Most constraints belong to units. The current naming ban needs clarification for the owner's illustrative machine-related subject id. Recommended: a) (confidence high - explicit constraints do not imply placement or authority) Adopt the optional typed `host_requirement` design, normally using unit constraints instead; unresolved required identities block device-dependent execution. Permit owner-chosen machine-related subjects such as illustrative `rig-sol`, with no inferred binding and no live-seat encoding.
- DISPLAY - Readers currently require title, but ordinary names are derivable and the owner wants a smaller definition. Custom labels and report headings must keep their meaning. Recommended: a) (confidence medium - feasible from naming rules, but compatibility needs fixture proof) Remove mandatory stored `title` after dual-reading readers can derive names, preserve custom display in optional `label`, expose compatible display projections and fall back visibly to id when metadata is unresolved.
- THEME - Regular is a work level; theme is optional thematic grouping. Requiring `theme: regular` would replace meaningful grouping or require an invented theme. Recommended: a) (confidence high - preserves both meanings without extra metadata) Keep optional/null `theme`, validate supplied theme slugs, and derive regular grouping from `level`; impose no regular-theme invariant.
- ROUTING - Description already includes exclusions at register depth. A separate `not_for` could improve authoring clarity but has no demonstrated routing gain and risks hidden or conflicting boundaries. Recommended: a) (confidence high - simplest design matching the actual reveal boundary) Retain purpose, Takes and Not for in `description`, the combined soft 500-character budget and Scope collision handling; add no anti field in this design.
- SIGNAL - No reviewed source proves universal telemetry. Package timestamps cannot supply session age. Useful partial evidence can coexist with explicitly unknown signals. Recommended: a) (confidence high - useful without fabricating counters or adding package state) Append evidenced elapsed wall-clock age and user/assistant message volume after `🧵 <id>` on the same final thread line, with coverage, provenance and observation time; preserve stable identity, epoch/reset rules, unknown/stale labels and no new persistent telemetry store. Keep the current footer unchanged until adoption and compatible reader migration.
- RESTART - The owner requested threshold-triggered advice. The masked review independently supports the same reversible four-hour/100-message convention with medium confidence in workflow fit and low confidence in the particular values. No evidence validates degradation prediction or numerical superiority. Existing pick-up defines safe continuation. Recommended: a) (confidence medium - reviewed workflow fit; numerical values unvalidated; fulfils the requested reminder through an explicitly unvalidated, reversible convention) Use four elapsed hours or 100 evidenced user/assistant messages, with a qualifying usable observation making one reminder pending per current session for the next existing safe resumable boundary. Unknown/stale evidence cannot establish a crossing; label partial coverage. The owner may continue and may request safe continuation earlier. No automatic restart, repeat or escalation; no implementation, pilot or study authority follows.
- STATE-MACHINE-DECISIONS - Open choices remain in [work-state-machine.md](design/work-state-machine.md). Recommended: settle them with the rollout.
- FOLDER-MIGRATE - This package has been tidied and its root reports moved losslessly into reports/; the wider migration remains open. Recommended: a) tidy, then git mv per package.

Terra portability questions below are deferred pending the owner's forthcoming movement/handover update. No option is selected and no Terra drain completion is claimed.

### TERRA-LOCAL-REPORTS - Dispose of the two run-only reports safely

**Context:** Terra retains drain-form.report.md and wow-sync-terra.report.md without exact blobs on origin/main. The sync outcome is logged in the package; the older report's complete outcome/query home is unproved here. PUBLIC-REPORT-AUDIENCE still applies.

**Query:** What private review and exact disposition should these copies receive before terra is called drained?

**Options:**

a) (recommended, confidence high - proves complete homes before disposal) Review both privately, record each outcome/query home, then select its disposition; retain both meanwhile.

b) Retain both on terra and leave the drain incomplete.

### TERRA-PR-CHECK - Supply the provider's open PR inventory

**Context:** Pruned origin refs and the absence of local work branches cannot establish open PR state. This run's provider-call ban prevented that check.

**Query:** Who will supply the current Ways of working open PR inventory?

**Options:**

a) (recommended, confidence high - obtains the missing fact within separate authority) Have an authorised attended session supply the inventory and resolve any named PR leftovers under its own grant.

b) Keep PR state unknown and leave the drain incomplete.

### TERRA-RECOVERY - Confirm the private recovery location

**Context:** The publication retention ref/archive and private-proof runtime named in decisions.md are absent on terra. No other machine or repository was inspected; nothing was deleted or published from those locations.

**Query:** Where is each retained item now held, with what size and private recovery home?

**Options:**

a) (recommended, confidence high - preserves retention without disclosure) Have the holding session confirm exact locations, sizes and private recovery arrangements, leaving every item intact and unpublished.

b) Leave recovery location/durability unknown and the drain incomplete.

- PACKAGE-FORWARDING - PKG-POINTER original request preserved at bcb3c1a3:+/_WORK/ki.ways-of-working/messages.md and the Principal enactment report. Owner approved one authoritative package and a Capital discovery reference; principal-only message forwarding remains separate design before any relay or second queue is built.
- PERM-PROMPTS-SETTINGS - whether to change the chezmoi-managed permission settings; Kris, 25 October: "can we come back to it later?". Recommended: not now, revisit if Kris leaves bypass mode.
- STEWARD-FIELD - where a package records who looks after it; reviews disagree, the harness carries the model with a marked placeholder and the Valle Armonia pilot runs on `worker` as it is. Recommended: a new dedicated field taking `work/<id>` values only. Parked under the 27 October bulk reading; comes back if the pilot needs it.
- LEGACY-PREFIX - whether a `repo_code` rename stays a one-sweep change; renames are rare and Personal's runs as one sweep, while an allowance costs two checkers and tools-ki. Recommended: write the one-sweep rename into `ki-work-roadmap`. Parked under the 27 October bulk reading; comes back at the next rename.
- PARTIAL-REPOS - how a repository with only Pillars and Resources fits the model; Kris's own words defer it and HNR's tracked-notes workaround holds. Recommended: record the idea on the Ways of working Project note and open a `ki-work-design` brief when Kris takes it up. Parked under the 27 October bulk reading; comes back when Kris opens it.
- UNATTENDED-FIELD - recording unattended eligibility on records; a new record field with reviews disagreeing while the roadmap is cut to next to nothing. Recommended: adopt the optional `unattended` mapping and criteria. Parked under the 27 October bulk reading; comes back if a window plan needs it.
- UNATTENDED-AND-DUE-DATES - adopting the eight criteria as the unattended assessment; the due-date half is done and the criteria stay Personal's prototype. Recommended: adopt the criteria in `ki-delegation`, leaving UNATTENDED-FIELD to decide where the verdict is recorded. Parked under the 27 October bulk reading; comes back with UNATTENDED-FIELD.
- CLI-PREVIEW - whether public state-changing commands write by default and preview with `--dry-run`; a fleet-wide tool convention while tools are not ready and releases are deprioritised. Recommended: write by default, `--dry-run` and `-n` preview, both standards reconciled first and each tool changed through its own work. Parked under the 27 October bulk reading; comes back when a repair command is next touched.
- MGIT-CACHE-SCOPE - what to build first for the mgit cache; Kris asked for the concept in plain language first, and the design note keeps the six routes. Recommended: `--repos-from` with `--to-cache` and `--from-cache` in one record, `sync --push-only` and `--pull-only` in a second. Parked under the 27 October bulk reading; comes back when Kris wants the cache built.
- MGIT-CACHE-FAILED - whether a checkout the sweep failed on goes into the cached set; same feature as MGIT-CACHE-SCOPE. Recommended: exclude them, keep their names and count as diagnostics, and warn on every `--from-cache` that the selection is incomplete. Parked under the 27 October bulk reading; comes back with MGIT-CACHE-SCOPE.
- RECORD-2 - work-package schema failures in thirteen folders; forty judgement fixes across live packages with reviews disagreeing on who makes them, and the full audit now runs only in CI. Recommended: one run per territory sweep, read-back of every changed field. Parked under the 27 October bulk reading; comes back when the work-package standard settles or a package is next tidied.
- FOLDER-1 - extras in two work folders; a rename of nine old reports and a script's home, with the review finding the counts wrong. Recommended: rename the nine to `<name>.report.md`, move `adobe-remove.sh` beside its design note and `spec-sched.brief.md` to `briefs/`. Parked under the 27 October bulk reading; comes back when those packages are next tidied.
- COORD-7-REST - fifty-one identifiers in reports with no local target; a known floor in old run reports that marks will prune, and fixing it needs a fetch and a rewrite run. Recommended: authorise the fetch of the two personal checkouts, write pruned links and rewrite the 25 tag-like identifiers. Parked under the 27 October bulk reading; comes back if the reports survive pruning.
- LINT-WHERE - where generated Markdown gets linted; the check-only staged hook of 26 October stops a bad report at commit with CI the backstop, and a generator check is extra machinery. Recommended: check-only in the generator, after FORM-VS-RUMDL. Parked under the 27 October bulk reading; comes back if bad reports still reach `+/_WORK`.
- MISSING-TOOLS - installing the missing hook tools in three package repositories; the recommendation is itself to wait, and installing would add new software. Recommended: leave them until the second convergence and bring any needed tool to Kris as its own decision. Parked under the 27 October bulk reading; comes back at that convergence.
- REL-X64-TIMEOUT - local timeout-only repair delivered and verified; release and pin work stays deferred until Kris explicitly reopens releases, under the current local-tools/no-release instruction.
- MIRROR-TOKEN - the Notion integration token and 1Password item behind the retired mirror; taken under the 27 October bulk reading, but the action is Kris's own and needs Notion and a credential change, both outside the window's limits. Recommended: revoke the integration in Notion and delete the 1Password item after `chezmoi apply` removes the last reference, finishing any HNR Notion page removal first. Parked for Kris to do at the machine.

### RIG-ATTENDED - Existing Rig attended prerequisites

since 2026-10-27 · from run/wow-rig-remainder; parked until Kris is available for the existing attended checks.

**Context:** These are existing prerequisites, not a request for another item-by-item approval. No live evidence was obtained in this run.

**Query:** Coordinator to route the existing attended checks and CORE-068 planning questions when Kris is available; keep both records in draft meanwhile.

**Options:**

a) (recommended, confidence high - preserves the plans' explicit gates) Arrange the existing attended checks and record the existing owner answers before another bounded delivery run.

b) Leave both drafts parked until those prerequisites are available.

### ANSWER-VECTOR - whether the first slice writes the answer line itself or waits for a `ki work answer` command

**Parked:** Parked with ki.observatory, which owns the feature and redesign. Release when its steward or the owner returns a route decision; neither option is selected here.

**Context:** The proposal's first slice has the Observatory compose the `messages.md` line and commit it through its own declared file effect, the path `feedback-send` already implements and tests, so the slice needs no tools-ki change. The Observatory's contract prefers consuming stable `ki` commands over duplicating work semantics, and a `ki work answer <id> <TAG> --option a --note "..."` command would make the line's shape one tool's and give the Observatory an argument vector instead. Waiting for it adds a tools-ki unit and a pin before anything can be answered in the Observatory; building the file effect first means a later swap to the command.

The review also found that the `ki-work-package` entry points let the owner, through the Observatory, commit a feedback package with its linking message, but grant no standalone answer-line write, so either option needs that authority written into the standard; sending stays off (`FEEDBACK_SENDING` false, KI-OBSERVA-BRG-004 delivered and Awaiting review pending its audit).

**Query:** Should the first slice write the line through the Observatory's own file effect, with the `ki work answer` command as a later record, rather than wait for the command?

**Options:**

a) (recommended, confidence medium - the file effect and its gate exist and are tested, and the swap later is one operation's vector, but the Observatory's own contract leans the other way) Build the first slice on the existing file effect; capture `ki work answer` and `ki work queries` for tools-ki as a later message and the Observatory's KI-OBSERVA-INT-005.

b) (blind review's pick, confidence medium - putting answer validation, the line's shape and the repository effect in one tools-ki command avoids a temporary second implementation; the feedback effect proves the mechanism, not an answer contract) Wait for tools-ki to provide `ki work answer`, and have the Observatory's first slice declare it as its vector from the start.

### AREA-COLUMN - publish the existing area reading aid?

**Irreducible hold:** `standards-compatible-harness.md` under `skills/repo-structure/ki-repo-harness/references/` explicitly calls areas a diagram reading aid rather than a published skill fact. Its marker-bounded README catalogue derives from frontmatter; `capability-publication.ts` has no area projection. The original blind review recommended extending this boundary, but that recommendation was never accepted. Existing area values avoid a new taxonomy/schema design; publishing them as a stable consumer contract still needs the choice below. A release is not the blocker.

**Delivered partial:** The immutable-ref local catalogue adapter is committed in website `2c15168`; Primary baseline received and final facts (27 October 07:03 GMT) records its integration, focused replacement evidence and the closed factual catalogue correction. The earlier dispatch and verification instructions are complete. They do not authorise the README publication extension below.

**Parked:** README publication remains outside the two independently qualified local website units; release when Kris decides the consumer contract.

**Context:** The current contract deliberately keeps areas outside published skill facts. The parked recommendation would make the harness README a stable consumer boundary. Local sync alone does not authorise that change; the two direct units and local-input partial can proceed independently.

**Query:** May the harness publish the existing area membership as a generated README reading aid and have the website consume it, without changing applicability or dependency semantics?

**Options:**

a) (recommended, confidence high - reuses the existing model and removes generator-code coupling, with the contract change explicit) Approve that bounded publication extension, then qualify exact harness generator/contract/test paths and the website parser/provenance companion paths. Use local immutable commits and local sync; no release cycle.

b) Retain the diagram-only publication boundary and the current finder/parser coupling; deliver only the independently qualified units above.

### HOST-SYNC - Settle the two-host synchronisation design

since 2026-10-28; parked until owner design discussion, source HOST-SYNC and HOST-SYNC-REPLY.

**Context:** Full received owner words, stopped-sync context, unresolved primary/secondary publication sequence and both Rig reply destinations are in [the live unadopted design](design/host-sync-and-reply-trades.md). Existing seat policy does not select concurrency, timing or a scheduler.

**Query:** Which primary/secondary publication sequence and offset should the equivalent Rig work use, including how primary hosts consume secondary updates?

**Options:**

a) (recommended, confidence medium - preserves the full request without inventing concurrency or scheduling authority) Discuss and settle the existing design choices, then send one bounded rollout line to each Rig queue; Rig and chezmoi own execution.

b) Keep the design parked and leave existing host operations to their owners; no new scheduler or host action is authorised here.

### STREAM9-SHA - Define the bare SHA-256 boundary

since 2026-10-28; parked pending owner boundary, source STREAM9-SHA and the masked source review.

**Context:** A bare hexadecimal SHA-256 can collide with an otherwise valid work identifier. The source review did not establish a high-confidence grammar-wide exemption. Filename and source-linked work references must retain precedence. No classifier change was delivered and no HNR source was inspected.

**Query:** What context should distinguish a bare checksum from a work identifier without suppressing a genuine identifier?

**Options:**

a) (recommended, confidence high - retains the existing hard boundary until the ambiguous case is defined) Keep the classifier change held; qualify a context-specific rule and negative examples before implementation.

b) Bring the exact bare-identifier ambiguity to an owner design decision before qualifying a patch; no general hexadecimal exemption is selected.

### GATE-BASELINE-COMPARATOR - Define inherited-finding equivalence

since 2026-10-28; parked until a source-grounded comparison can be reviewed, source GATE-BASELINE-PREFLIGHT.

**Context:** The routed approval asks that inherited origin/main findings be distinguished from regressions. The current preflight hard stops still apply; an exact baseline comparator, its identity/provenance and refusal cases have not been settled. A prose clarification cannot silently waive all existing WARN/FAIL findings. The sibling-worktree half already belongs to Tools under GATE-BASELINE-SIBLING.

**Query:** What exact evidence establishes that a finding is unchanged from the declared baseline, while preserving hard stops for new, changed or uncomparable findings?

**Options:**

a) (recommended, confidence high - preserves the approved goal without weakening an undefined guard) Retain current hard stops until the narrow comparator and refusal evidence are qualified; keep this a held method need.

b) Revisit the approved approach with the owner before defining comparator semantics. No baseline-wide exemption is adopted.

### THREAD-DEFAULTS - Select a session and its default work home

since 2026-10-28; parked until session/default selection is decided, sources THREAD-HOME and HOOK-SHORTCUT.

**Context:** Typed readers and member-launched coordination support are delivered. The new unknown-session hook partial emits a short conditional pointer and avoids checkout-wide scans; it does not discover the selected session. Default selection for member-local status, a Capital package and multiple candidates remains undecided. No session marker, schema or automatic work opening is authorised.

**Query:** How should a session explicitly select its one work and determine the default status/home context without assuming the launch checkout is the package home?

**Options:**

a) (recommended, confidence high - keeps delivered launch support usable while retaining explicit selection) Preserve explicit work selection and the quiet-hook partial; design the remaining default/session boundary separately.

b) Have the owner choose the intended default-selection contract before qualifying another implementation unit.

### LINK-EXTERNAL - Decide the external linked-target boundary

since 2026-10-28; parked until owner boundary decision, source THREAD-HOME/LINK-CHECKER.

**Context:** Shared LINK-1 now follows contained linked directories and contained absolute filesystem paths, with outside-byte/refusal checks. Targets outside the selected root are still excluded. This does not clear the reported HNR sibling-tree findings; no HNR source was inspected or changed.

**Query:** Should a future resolver follow a separately declared external target, and under what explicit source-access and containment contract?

**Options:**

a) (recommended, confidence high - preserves the tested containment boundary and confidential-source guard) Keep external targets held and the contained partial unchanged until the access contract is decided.

b) Ask the owner to define a bounded external-target model before any source discovery, traversal or implementation.

### PUSH-RETRY - Decide whether any bounded retry is wanted

since 2026-10-28; parked pending method choice, source Personal Rig terra PUSH-RETRY.

**Context:** The sender proposes up to five retries for a queue append losing a push race. Current coordination/delegation/Git rules distinguish an uncontested remote append from actual divergence, peer-owned history, contested staging or content conflict. No blind replay or retry policy has been adopted. The existing private qualification preserves the two routes and their source sections.

**Query:** Should the method retain the current bounded conflict-run route or design a narrowly qualified retry for uncontested append races?

**Options:**

a) (recommended, confidence high - uses the existing supported route and preserves every ownership/refusal guard) Retain the current stop-and-bounded-conflict-run method; make no retry policy change now.

b) Qualify a bounded own-content-only retry for disjoint append races before adoption; the sender's five-attempt count remains a proposal and cannot override divergence, privacy or narrower push rules.

- PROTECTED-PUBLICATION - the current unpublished Principal stack has two protected report blob versions in the existing private safe-sync inventory. Owning Observatory has an IMPORTANT disposition request before any push; preserve peer work/history and infer no publication certification. This remains separate from the earlier remotely exposed report-history audience query.
- MD-STANDARD-REMAINDER - local writer/exclusion and staged-gate evidence is independently accepted Done in CLI-175; the HNR hook-bypass cause, global historical cleanliness and other-host/provider freshness are still unproved. HNR source/access remains excluded; no estate audit is commissioned. Revisit only under the owning source/access authority.
- ENACTMENT-ADMIN - the 20 October tiered/Admin-only gate-narrowing choice remains unmade; retain the current gate. Full original decision is retained in decisions.md.
- PROXY-SHAPER - Kris deferred this on 25 October; no proxy or chezmoi change. Full original owner words remain in decisions.md; revisit only when taken up.

### HOMES - Repository identity and defaults

**Context:** Existing packages default to the territory Capital, with approved regular/ad hoc exceptions. Local keys and canonical repository identities differ. Explicit metadata must not create a new home or permission.

**Query:** Use canonical repository identities, a derived Capital default and optional checked `territory`?

**Options:**

a) (recommended, confidence high - portable identity and existing authority remain distinct) Use the HOMES model above: optional matching `territory`, omitted `canonical_home` derives Capital, explicit null stays unresolved, supplied identities must resolve uniquely and exceptions retain their approval requirements.

b) Keep home declarations only in current Scope and omit both new fields; retain the current resolution contract.

### EXECUTION - One default execution context

**Context:** The owner means where work is meant to be running and illustrates the chezmoi repository footprint. Both earlier reviews prefer plural execution hints; neither establishes support in current readers. One declared default can supply a verified launch working directory without replacing canonical package home, explicit unit targets or authority.

**Query:** Use one optional execution repository/context as a checked launch default, with explicit unit targets and overrides?

**Options:**

a) (recommended, confidence medium - meets the owner's execution intent with lean semantics; launch compatibility remains unproved) Keep singular `execution_home`, unspecified when absent/null, as one default repository/context that can supply a verified launch working directory after explicit work selection, host requirements and unit authority checks. Preserve explicit unit targets and overrides; resolving the directory grants no write authority. Current readers need separately authorised compatibility work; no binding or directory change happens here.

b) Defer an execution field and retain explicit per-unit working-directory and target declarations under current readers, leaving the requested package-level launch default undelivered.

### HOST - Required machine versus session seat

**Context:** Device constraints already resolve through inventory, while live placement stays out of packages. Most constraints belong to units. The current naming ban needs clarification for the owner's illustrative machine-related subject id.

**Query:** Add an optional whole-package host/category requirement and distinguish subject naming from live placement?

**Options:**

a) (recommended, confidence high - explicit constraints do not imply placement or authority) Adopt the optional typed `host_requirement` design, normally using unit constraints instead; unresolved required identities block device-dependent execution. Permit owner-chosen machine-related subjects such as illustrative `rig-sol`, with no inferred binding and no live-seat encoding.

b) Retain all constraints in existing labels/Scope/unit prose and retain the current host-in-id prohibition; choose a different subject id before any adoption.

### DISPLAY - Remove mandatory stored title compatibly

**Context:** Readers currently require title, but ordinary names are derivable and the owner wants a smaller definition. Custom labels and report headings must keep their meaning.

**Query:** Approve title removal as the destination, after compatible readers and preserved display overrides?

**Options:**

a) (recommended, confidence medium - feasible from naming rules, but compatibility needs fixture proof) Remove mandatory stored `title` after dual-reading readers can derive names, preserve custom display in optional `label`, expose compatible display projections and fall back visibly to id when metadata is unresolved.

b) Retain required stored `title` as the permanent authoring contract, updating it from display metadata as today.

### THEME - Independent grouping

**Context:** Regular is a work level; theme is optional thematic grouping. Requiring `theme: regular` would replace meaningful grouping or require an invented theme.

**Query:** Keep theme independent and derive a Regular work display group from level?

**Options:**

a) (recommended, confidence high - preserves both meanings without extra metadata) Keep optional/null `theme`, validate supplied theme slugs, and derive regular grouping from `level`; impose no regular-theme invariant.

b) Make regular level imply `theme: regular`, deliberately replacing independent grouping for those packages and requiring a separately authorised real theme definition.

### ROUTING - One exclusion source

**Context:** Description already includes exclusions at register depth. A separate `not_for` could improve authoring clarity but has no demonstrated routing gain and risks hidden or conflicting boundaries.

**Query:** Keep the combined description as the proposed routing contract?

**Options:**

a) (recommended, confidence high - simplest design matching the actual reveal boundary) Retain purpose, Takes and Not for in `description`, the combined soft 500-character budget and Scope collision handling; add no anti field in this design.

b) Introduce optional text `not_for` as the sole exclusion source when present, with positive-only authored description, a combined legacy projection and the same total soft budget; migrate all register readers before conversion.

### SIGNAL - Truthful session indicator

**Context:** No reviewed source proves universal telemetry. Package timestamps cannot supply session age. Useful partial evidence can coexist with explicitly unknown signals.

**Query:** Display separately evidenced age and volume with volatile runtime observations and explicit unknowns?

**Options:**

a) (recommended, confidence high - useful without fabricating counters or adding package state) Append evidenced elapsed wall-clock age and user/assistant message volume after `🧵 <id>` on the same final thread line, with coverage, provenance and observation time; preserve stable identity, epoch/reset rules, unknown/stale labels and no new persistent telemetry store. Keep the current footer unchanged until adoption and compatible reader migration.

b) Show only a qualitative resumability reminder until one client can evidence both full-session age and volume; keep numerical freshness display deferred.

### RESTART - Advisory policy and safe continuation

**Context:** The owner requested threshold-triggered advice. The masked review independently supports the same reversible four-hour/100-message convention with medium confidence in workflow fit and low confidence in the particular values. No evidence validates degradation prediction or numerical superiority. Existing pick-up defines safe continuation.

**Query:** For the design only, use four elapsed hours or 100 evidenced user/assistant messages as the provisional reminder cutoff?

**Options:**

a) (recommended, confidence medium - reviewed workflow fit; numerical values unvalidated; fulfils the requested reminder through an explicitly unvalidated, reversible convention) Use four elapsed hours or 100 evidenced user/assistant messages, with a qualifying usable observation making one reminder pending per current session for the next existing safe resumable boundary. Unknown/stale evidence cannot establish a crossing; label partial coverage. The owner may continue and may request safe continuation earlier. No automatic restart, repeat or escalation; no implementation, pilot or study authority follows.

b) Retain truthful signals and user-requested safe continuation without numerical reminders, explicitly deferring the requested threshold-triggered element.

c) Choose different provisional numerical values as an owner workflow preference, with the same advisory and evidence constraints and no degradation claim.
