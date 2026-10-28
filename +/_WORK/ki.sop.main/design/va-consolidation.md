# VA consolidation - messages from VA > SoP, grouped by theme

Draft for Kris, written by run va-consolidate under VA-CONSOLIDATE (Kris, 24 October 2026 16:46 BST, in [decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/decisions.md)): "Consolidate messages from VA > SoP (va) in your messages.md into one clear, coherent set ... Keep Kris's quoted words in each; source." Read-only analysis: no `messages.md` line, standard, skill, Work Process note or record has been changed or created. The queries this note raises are in the run report.

Sources read:

- [ki messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/messages.md) and [ki.prj.ways-of-working messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/messages.md), the va lines in each, cited by tag.
- [va decisions.md](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/decisions.md), current, with the pruned HTTPS-OTHERS and SANCTUARY-RELATION answers at its [pinned revision `d41e504`](https://github.com/vallearmonia/va-principal/blob/d41e504/+/_WORK/va/decisions.md).
- The coordination standard, [standards-coordination.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md), and [ki-coordination SKILL.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/SKILL.md), at harness `main` `57226cdea`.
- The work package standard, [standards-work-package.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md).
- The [Work Process note](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>).

Kris's seven-point model, as VA-CONSOLIDATE states it, is the yardstick:

1. Work packages and threads are different things.
2. One State of play thread can run the territory, cascading into each Project's work package unless the Project has its own live coordination thread.
3. Work flows from roadmap records into the work package of the record's Project.
4. Each thread and package records what it relates to: territory, Project, parent State of play.
5. A Summary's Done covers only what happened since the last mark; In Progress lists only what is running in this work; Outstanding lists only what this work carries, with no push state, hand-offs or roadmap-held items.
6. An explicit `ki-coordination` command for each move: at least hold, drain and mark, plus resume, send and receive.
7. Tending checks that working areas are cleaned up at master-repository and territory-wide levels.

## Method lines

### A. Reports and the mark (model point 5)

**Consolidated line.** Every report windows on the mark: after a mark, Done says nothing has happened since it, In Progress says nothing is running, Queries says none are outstanding, and Outstanding carries only what this work itself holds. Push state, hand-offs to other work and items waiting in a roadmap are updates, not Outstanding.

Kris's words:

- SUMMARY-SINCE-MARK (ki.prj.ways-of-working): "It looks like we're getting items under done which I thought was completely done. So if I do a mark again and then a summary from that, I should have nothing that's done right. And there should be nothing in progress." And: "after this mark, what I'm expecting is done to say nothing since the last mark, and in progress to say nothing is running, in queries to say no outstanding queries ... and it says on hold at the end."
- SUMMARY-OUTSTANDING (ki.prj.ways-of-working): "all of this can be fed back to the ways of working to make sure that these summaries get clearer and better".
- va decisions, 24 October 12:50 BST: "You don't need to tell me about anything to push ... That's a different thing entirely"; items waiting on others are "just something that you give me as an update. It's not outstanding for this thread"; roadmap items waiting are "nothing to do with the work package".

Replaces: SUMMARY-SINCE-MARK, SUMMARY-OUTSTANDING (its reporting part).

**Already done.** The working-area part of SUMMARY-OUTSTANDING is in Tending: harness `fdb407ebd` and ki-principal `3a575852` (level 3 working-area and package-tidy questions in [tending.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/tending.md)). Push state is already kept out of owner reports and banners by the Banner section of the coordination standard.

**Conflicts with the standards.**

- Coordination standard, Report forms: the Summary's window is "since your last message"; only the recap interacts with the mark. Kris expects the Summary itself to be empty after a mark.
- Coordination standard, Recap since the mark: Outstanding is "open work records in the work's scope", which "carries forward across marks". Kris excludes roadmap-held items.
- Coordination standard, Owner report, In Progress: "A handoff to other work stays outstanding until the owner expressly says it is done". Kris calls hand-offs an update, "not outstanding for this thread". This is a conflict between two owner positions; the later one (24 October) is the narrower.
- Coordination standard, Full summary: In Progress includes dated upcoming deadlines. Compatible if kept to the full summary only.
- Work Process note: no conflict; the note leaves the report windows to the standard.

**Conflicts with the model.** None: the lines are the source of point 5.

**Proposed change.** Standard edits to `ki-coordination`:

- Report forms: the Summary windows Done on the mark, not the last message, so that a Summary straight after a mark has an empty Done; the recap stays as the longer look back.
- Owner report, In Progress and Outstanding: list only runs in this work and items this work holds (its own parked queries, its own uncommitted files); a hand-off is reported once in Done when it is sent and no longer carried; records waiting in a roadmap are left to the roadmap.
- Recap since the mark: Outstanding loses the carried-forward open records, or keeps them only in the full summary.

No record (CAPTURE-GATE: a standard change on Kris's request goes as an edit by the work that owns the standard, not as a record).

**Carrier.** ki.prj.ways-of-working, which owns the coordination method.

### B. A command for each move (model point 6)

**Consolidated line.** Each move in the work model has an explicit `/ki-coordination` command, so that Kris can say the move rather than describe it: at least `hold`, `drain` and `mark`, with `resume`, `send` and `receive` beside them.

Kris's words, COORD-COMMANDS (ki.prj.ways-of-working): "I think there needs to be a number of commands as well that can be passed into the KI coordinate scale. So things, for example, putting something on whole or giving it a mark, you should be able to make that express or explicit by saying KI-coordination mark or KI-coordination hold or KI-coordination drain."

Replaces: COORD-COMMANDS.

**Already done.** `mark` exists: SKILL.md Operating modes lists `FULL-SUMMARY · MARK · RECAP · SUMMARY` beside `AUDIT · CONFORM · EDUCATE · REFRESH`.

**Conflicts with the standards.**

- SKILL.md Operating modes and coordination standard Report forms: the only commands are `summary`, `recap`, `full-summary` and `mark`.
- Coordination standard, Putting work on hold: the receive words are `pause` and `done for now`, with `resume` and `finish`; hold is spoken, not a command.
- Work Process note: drain is an activity inside the move to On hold, not a state of its own. A `drain` command that does not end in On hold would need the note to say what state the work is in while it drains (With worker, launching nothing).

**Conflicts with the model.** None.

**Proposed change.** Standard edit to `ki-coordination`: add `HOLD`, `DRAIN`, `RESUME`, `SEND` and `RECEIVE` to SKILL.md Operating modes and the Report forms paragraph, each naming the procedure it runs (Putting work on hold, Picking work up, States and moves). `hold` runs the drain and the move to On hold; `drain` stops new launches and lets running work finish while the work stays With worker, ending in a report; the spoken words stay as synonyms. If `drain` is to be a state, the Work Process note changes through the Enactment Process.

**Carrier.** ki.prj.ways-of-working.

### C. One State of play thread, packages against threads, metadata and host (model points 1 to 4)

**Consolidated line.** A thread is a session working on a package; it is not the package. A territory's State of play thread can run the whole territory alone: it takes work from roadmap records, creates or uses the work package of the record's Project, and does the work in that package, unless the Project has its own live coordination thread, which it must be able to find. To find it, each thread and package records what it relates to (territory, Project, parent State of play). Coordinating threads know which host they run on, so that work aimed at a machine or class of machine can be applied there.

Kris's words:

- SINGLE-THREAD (ki.prj.ways-of-working): "looking into how we can effectively do everything through a state of play thread alone. So sometimes it might not have anything to coordinate with, in which case it can delegate down the structure and it can deal with things. It should always still deal with things in the right work package, regardless of whether which thread is dealing with it, right? So there's a difference between work packages and threads, which are things working on the work packages. And basically, I think the idea is that we're taking stuff from effectively the road maps, we're creating then stuff within a work package related to the project that the roadmap item is in, for example. I know it probably is something that we need to get mapped out in terms of a lot of this and there's a lot of documentation to do really. ... I think the basic idea is that for something like Valley Armonia, we really only need to direct it through one single thread, which is focus at the state of play level, and it can then cascade down and deal with all of the work across the work packages that are within all of that."
- SOP-PROJECT-CARE (ki.prj.ways-of-working): "when you've got a state of play which is running, it also looks after any of the project work packages that are part of that and keeps those sorted out, unless, of course, I've got their own coordination thread, which it should know about somehow. I think one of the key things is that we need to add to the metadata of the threads, what it's related to, so that when we're using the coordination skill we know that and we can find it and look it up. But also it should probably be able to sort of keep a good eye on what it is anyway."
- va decisions, 24 October 10:41 BST, on State of play handing items into a repository's inbound area: "There's a difference, isn't there, when you're a state of player, because as a state of player you can push things into a repository to accept, to get on with it."
- va decisions, 24 October 16:41 BST, on SINGLE-THREAD: "Yeah, make the changes that you need to, please..." (given to va's coordinator for va's own work, not as approval of KI standard changes).
- COORDINATOR-HOST (ki.prj.ways-of-working), **from Rig > chezmoi > SoP, not from va**: "coordination teams should use a hostname to understand who they're running on. Presumably, they do that already, but if that's not explicit in the skill usage of it, so that you can apply if there's things targeted to particular machines or categories of machines, then we should deal with that."

Replaces: SINGLE-THREAD, SOP-PROJECT-CARE, COORDINATOR-HOST (grouped here as model point 4 metadata).

Related non-va lines in ki messages.md, for the same design: KI-SOP-PATTERN, SOP-SECONDARY and WORK-PROCESS-NOTE (HNR: secondary States of play are not in the Work Process note).

**Already done.** Secondary States of play carry `parent` and `covers` (coordination standard, Secondary States of play; work package standard, work file fields), merged in harness `41b391d61` (SOP-SECONDARY-MERGED). Nothing yet for Project work.

**Conflicts with the standards.**

- Work Process note, Levels and forms: territory work "executes nothing"; "Attention comes back up: each level reads the work packages beneath it and rolls up the five views". Kris wants State of play to do Project work in the Project's package.
- Work Process note, Overview: "A chat session is only the channel through which a party works on it". This already separates package from session, but the note has no thread concept, no live-thread binding and no secondary State of play.
- Work Process note, Homes: "Other work and State of play write into a package only by adding a line to its `messages.md`". A cascading State of play writes into a Project package directly.
- Coordination standard, Territory work: State of play owns messages to Project work and the Project-work queue, names flagged folders by a line, and "never prunes another work folder itself".
- Work package standard, work file fields: `parent` appears only on a secondary; a Project work file has `project` and `theme` but no parent State of play and no live-thread field; `beat` in `state.md` is a heartbeat only.
- Host: coordination standard, Picking work up: "Neither file names a host; where a territory is seated is host data, not work state"; Putting work on hold: a hold "never says which host the work comes back up on"; work package standard, prohibited payloads: "no host"; Work naming: the label carries a `(<host>)` suffix only for work limited to one machine.

**Conflicts with the model.** Points 2 and 4 conflict with the four standard passages above; point 3 has no home in the Work Process note, which says nothing about records flowing into a package; point 1 is consistent with the note's Overview but unnamed.

**Proposed change.** A shaping, not a direct edit: the cascade reverses a stated principle of the Work Process note, which is canonical content under the Enactment Process.

- Open a `ki-work-design` brief in ki.prj.ways-of-working covering: threads against packages; the State of play cascade and when a Project thread takes over; roadmap record to Project package; the relation fields (a `parent` on every Project work file naming its State of play, generalising the secondary's field); how a live thread is found without putting host or session into the package (for example a machine-local binding under the `ki agent` state); and whether a message line may target a host or host class.
- Its outcome edits the Work Process note (Enactment Process, record in `Streams/Roadmap/`), the coordination standard (Territory work, Picking work up) and the work package standard (work file fields, prohibited payloads).

No record from this run (CAPTURE-GATE); the shaping captures its own when Kris approves it.

**Carrier.** ki.prj.ways-of-working, with the Work Process note change through the Enactment Process.

### D. Tending (model point 7)

**Consolidated line.** Tending, the continual care of a territory's knowledge, runs as two tracks (a structural track of four levels, a PMO track of five worked bottom up), pioneered on Valle Armonia. Round 2 adds: skip empty PMO levels, collapse repeated findings under one disposition, confirm upstream fixes are in the installed payload, and seven candidate mechanical checks. Level 3 names agent memory and orientation files explicitly; level 4 asks whether guidance common to several repositories should be promoted into a skill. Tending checks working areas and roadmap clear-down at master-repository and territory-wide levels.

Kris's words:

- TENDING-GUIDANCE-OVERLAP (ki.prj.ways-of-working): "I also meant auditing things like agents.md and claude.md to make sure that we weren't overlapping with things that are already in skills and the promotion of things into skills where there's commonality in their approach across multiple repositories."
- TENDING-ROADMAP (ki.prj.ways-of-working): "We should probably add that into the list so that we do this for other tending activities."
- METHOD and TENDING-ROUND-2 carry va's description, not Kris's quoted words.

Replaces: METHOD, TENDING-ROUND-2, TENDING-GUIDANCE-OVERLAP, TENDING-ROADMAP, and the working-area part of SUMMARY-OUTSTANDING.

**Already done.**

- TENDING-ROADMAP: ki-principal `1f998140`, harness `57226cdea`.
- Working-area and package-tidy questions at level 3: harness `fdb407ebd`, ki-principal `3a575852`.

**Pending.**

- [tending-round2-notes.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/tending-round2-notes.md) is not yet folded into [tending.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/tending.md).
- Level 3 has no explicit AGENTS.md, CLAUDE.md and agent-memory overlap check.
- Level 4 has no cross-repository guidance-promotion question.

**Conflicts with the standards.** None found: Tending is a design note in ki.prj.ways-of-working, not yet a standard. The `ki-repo` REVIEW procedure may later want the AGENTS.md overlap question.

**Conflicts with the model.** None: point 7 is met for working areas; the guidance-overlap check extends it.

**Proposed change.** Design-note edits in ki.prj.ways-of-working: fold round 2, add the level-3 agent-memory check and the level-4 promotion question. No standard edit and no record now.

**Carrier.** ki.prj.ways-of-working.

### E. Size labels

**Consolidated line.** Show a record's size as a T-shirt label in capitals, 👕 S, 👕 M, 👕 L, 👕 XL, in reports and messages.

Kris's words, va decisions T-SHIRT-SIZES (24 October 08:42 BST): "I wonder if there's a way of showing a T-shirt with S, M, etc. next to it. And probably put it in a capital letter, almost like it's a label for a t-shirt." TENDING-SIZES (ki.prj.ways-of-working) asks KI to consider it for the sizing guidance.

Replaces: TENDING-SIZES.

**Already done.** va uses it.

**Conflicts with the standards.**

- `ki-work-roadmap` [standards-work-item-format.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md), Priority and size: `size` is `s`, `m`, `l` or `xl`, and `xl` must be split before Ready. There is no `xs`, yet BIND-2 was labelled 👕 XS.
- [roadmap-sizing-and-burn-down.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/roadmap-sizing-and-burn-down.md) (14 October) still describes Fibonacci points 1 to 13, superseded by the `size` field.

**Conflicts with the model.** None.

**Proposed change.** Standard edit to `ki-work-roadmap` Priority and size: a display convention, 👕 plus the capital letter, for reports and messages, with the field values unchanged and no XS. Mark the Fibonacci text in the sizing note superseded.

**Carrier.** ki.prj.ways-of-working.

## Product and defect lines

### F. Always Use HTTPS on Cloudflare sites with their own domain

**Line.** Kris (ki messages.md, from va, 23 October 20:30 BST): "I want the skill updating so that this is the default for cloudflare deployed sites with their own domains", meaning Always Use HTTPS on every Cloudflare-deployed zone with its own domain. The pruned va answer HTTPS-OTHERS at [`d41e504`](https://github.com/vallearmonia/va-principal/blob/d41e504/+/_WORK/va/decisions.md) reads "a, and I want skill updating so default cloudflare deployed sites with own domains".

**Already done.** Nothing in KI: [standards-cloudflare-hosting.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-website-cloudflare/references/standards-cloudflare-hosting.md) has no Always Use HTTPS rule, and no harness record exists.

**Conflicts.** None with the standards or the model.

**Proposed change.** A record in ki-agentic-harness under `ki-next` (CAPTURE-GATE allows it: a Kris request) for `ki-repo-website-cloudflare`: Always Use HTTPS on by default for zones with their own domain, with a rubric check.

**Carrier.** State of play routes it; the harness owns it. There is no harness work package, so the capture is a bounded run from State of play into the harness roadmap.

### G. `node_modules` ignore rule and symlinks

**Line.** ki messages.md, from va, 23 October 23:05 BST: the managed `node_modules/` rule does not match a symlink, and FILES-6 (`LEGACY_EQUIVALENTS` in [gitignore.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/scripts/rubric/contexts/gitignore.ts), lines 39 and 40) strips `/node_modules` as a legacy equivalent. A dangling `node_modules` symlink in apps-vallearmonia.com `ece7827` hung Workers Builds; that repository is fixed at the script level in `a13802c`. No Kris quote.

**Already done.** Only the va repository's own fix.

**Conflicts.** The `ki-repo` ignore contract, which treats a symlink-safe `node_modules` as legacy. None with the model.

**Proposed change.** A record in ki-agentic-harness under `ki-next` (CAPTURE-GATE allows it: a defect seen failing) for `ki-repo` FILES-6: make the managed rule symlink-safe or stop stripping `/node_modules`.

**Carrier.** State of play routes it; the harness owns it.

### H. Harness root orientation

**Line.** HARNESS-ORIENTATION (ki messages.md, VA > SoP, Project [baseline-rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md), 👕 S): the compatible-harness standard puts root orientation in `CLAUDE.md`, `ki-repo` makes `AGENTS.md` authoritative, the scaffold writes neither and no rubric item checks it; the Equal Remedy, Techmedix, Sacred Inquiry, Legal and Personal harnesses lack it. No Kris quote.

**Conflicts with the standards.** [standards-compatible-harness.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-harness/references/standards-compatible-harness.md), Root orientation ("The source-harness `CLAUDE.md` is its runtime-bound orientation") against [standards-repository.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md) lines 47 to 51 (root `AGENTS.md` authoritative for multi-runtime repositories). None with the model.

**Proposed change.** A standard edit to `ki-repo-harness` Root orientation, pointing at root `AGENTS.md` with `CLAUDE.md` importing it, plus a scaffold and rubric item. Whether a record may be captured is unclear under CAPTURE-GATE: it is a Tending finding of a standards conflict, not a defect seen failing, and not a Kris request.

**Carrier.** ki.prj.baseline-rollout, as a line in its `messages.md`.

### I. Sanctuary stage 5

**Line.** SANCTUARY-STAGE5 (ki messages.md, from va, 24 October 01:54 BST): Kris wants the Sanctuary to be "a package effectively that is available in the Knowledge Islands". Kris decided (SANCTUARY-RELATION a, "VA 2-4, KI 5", pruned at [`d41e504`](https://github.com/vallearmonia/va-principal/blob/d41e504/+/_WORK/va/decisions.md)) that Valle Armonia delivers stages 2 to 4 of [ADR-VA-WEBSITE-009](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/decisions/ADR-VA-WEBSITE-009-the-sanctuary-becomes-a-shared-editorial-library.md) under va Project `sanctuary-library`, and KI takes stage 5: a separate, vendored package repository. va asks KI to agree, or say what it needs, before [VA-WEBSITE-SANC-008](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SANC-008-package-the-sanctuary.md) is readied. At stage 4 va hands over code, fixtures and adapter contracts; KI then decides Project, repository, priority and acceptance. packages-portal-commons is the nearest precedent.

**Related.** SANC008-SPLIT (split stage 4 out of VA-WEBSITE-SANC-008) is parked in [ki.prj.baseline-rollout queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.baseline-rollout/queries.md).

**Conflicts.** None with the standards or the model. Needs a Kris decision: KI has no Project for it.

**Proposed change.** None until Kris answers. If KI agrees, State of play replies to va's State of play with a message line, and the record is captured later by the KI work that will own stage 5.

**Carrier.** State of play.

## Cleared lines

These need no further work; the ki coordinator may remove them with their disposition.

- BIND-2 (chezmoi, 👕 XS) and BIND-2-DONE: fixed in chezmoi `6a67f4d` and harness `e54ad7cb9`; BIND-2-DONE says "Both lines, and this one, can be removed at pick-up". The XS label is not a valid size (theme E).
- COV-1-SUBAGENTS and COV-1-NOT-LIVE: the fix `e54ad7cb9` is on harness `main`, and the installed harness now points at the primary checkout on `main`, so it is live.
- SOP-SECONDARY-MERGED: merged in harness `41b391d61`. The divergence it notes between local and remote `main` over the OAuth marker is push state and is not carried.
