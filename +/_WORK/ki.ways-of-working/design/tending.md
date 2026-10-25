---
note_type: streams/design
updated: 2026-10-25T00:45:00Z
author: Written with Claude
---

# Tending

**Status:** a nascent area of Ways of working, pioneered on the Valle Armonia territory. Valle Armonia and Personal both run it as interim policy, and their findings are folded in below and kept under [Other territories](#other-territories). Other territory threads are invited to run it on their own territory and add theirs. Nothing here is a standard yet; the shape is expected to change as runs report back.

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-24, folded 2026-10-25 · **Pioneered by:** [VA > SoP](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/work.md), whose [decisions log](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/decisions.md) holds Kris's words from 07:39 to 08:02 BST on 24 October

Tending is the continual tending of a territory's knowledge: a repeated pass over a repository or a territory that takes stock and burns down what it finds. What matters is the process and the alignment it keeps, not the report it leaves.

## The process

Tending runs in two tracks, which look at the same estate from two sides:

- The **structural track** asks whether each repository, and the territory as a whole, is in the shape its standards and purpose expect. It has four levels, from everyday mechanical checks to a master territory checklist.
- The **PMO track** asks whether the work is in the right place: what is in flight, what is recorded, and whether the Projects and themes that classify it still fit. It has five levels and is worked bottom up, from work packages to the territory overall.

Both tracks are judgemental above their first level. Level 1 of the structural track uses the rubrics and tooling that already exist; every other level is a person or an agent reading and deciding, with no rubric and no new tooling.

### How the levels pick up each other's captures

The structural track runs before the PMO track in each repository, so the PMO track judges records and packages that already pass their checks. In the pioneer run, one run per repository took structural levels 1 to 3 and PMO levels 1 and 2 together, in parallel across repositories; then State of play took structural level 4 and PMO levels 3 to 5 for the whole territory. A repository took about 6 to 12 minutes in Valle Armonia's second round.

Captures move upwards:

1. A structural level captures in the best place it knows: the repository it is reviewing and the Project or theme the work seems to belong to.
2. PMO level 1 picks up anything a package holds that is really a record, an idea or done.
3. PMO level 2 re-reads every captured record and moves it if another repository delivers it or another Project owns it.
4. PMO level 3 checks the captures against each Project's outcome and turns gaps into candidates.
5. PMO level 4 checks captures that name a theme directly and those that strain a theme's direction.
6. PMO level 5 reads everything above and brings structural change to Kris.

### Running a pass

- **Skip what is empty.** A level with nothing to read, such as PMO levels 1 and 2 in a repository with no packages or records, or most level 3 lenses on a one-skill harness, is skipped without a line.
- **Collapse repeats.** One disposition that applies to many items is given once, with the items listed, rather than once per item: nine branches one record covers are one finding.
- **Fresh results for the territory pass.** Structural level 4 reads the current round's level 1 to 3 results and does not repeat them. Where a repository has none from this round, the territory pass runs that repository's level 1 itself, since it is mechanical and quick, and names the repository as not reviewed at levels 2 and 3 rather than doing them.
- **Shared repositories.** Where several work packages share one repository, as four do in Personal's Capital, conform runs per skill, never whole-repository, because a whole-repository conform runs `rumdl --fix` over other packages' files. The run checks `git status` afterwards and commits only its own paths.
- **No-remote briefs.** Under a brief that bars remote calls, level 1 runs per skill with `ki repo audit --skill`, leaving out `ki-repo`'s GitHub checks and any `gh repo view` step, and names those checks as not run. No offline mode of the whole audit exists yet.
- **Where a run may not write.** In a repository the run may not change, such as a deploy repository whose pushes are Kris's or a package another coordinator runs, its fixes go as one collapsed message to the package that owns them, not as one query each.
- **Decided lines in another package.** A run may carry out a line held in another package when the line's decision is already logged and the fix lies in the repository the run is tending, as the Valle Armonia website run did under the RELABEL-MARK precedent. It reports the line as done, and the owning package removes it.

## Structural track

### Level 1: everyday mechanical audit and conform

- **Purpose.** Keep each repository passing its own mechanical checks, so the judgement levels start from a clean baseline.
- **Inputs.** The repository's `.ki.toml`, its declared skills and their rubrics, and the existing audit and conform tooling.
- **Typical questions.** What fails or warns? Which failures are this repository's to fix, and which belong elsewhere? Is each checkout's position against its upstream known? Does every cross-reference resolve, by a link resolver over every Markdown file, since dead links were the biggest site finding in Personal's run and the audit cannot see them? Is an upstream fix really in the installed payload: is the installed harness at its pinned or `main` revision, given that a symlinked harness follows whichever branch its checkout is on? Does the recorded baseline show passes and judgement items, not only the verdict the default output gives?
- **Produces.** Mechanical fixes committed in the repository, and any remaining failure named with its owner.

### Level 2: ad hoc judgement audit and conform

- **Purpose.** Apply the judgement criteria of the declared skills where the mechanical checks cannot decide, when someone asks or when a baseline shifts.
- **Inputs.** Level 1's baseline, the judgement items of each declared skill, and the repository's own conventions.
- **Typical questions.** Does the repository meet the judgement items, not only the mechanical ones? Is each maturity, opt-in and orientation claim true? Do the opt-ins and their dependencies agree both ways: no removed opt-in still a declared skill's dependency, and no opted-in skill left orphaned, as Personal's `ki-work-recurring` was? Is any opt-in's model retired, such as the Paperclip coordination skill after its record was cancelled? Does any documentation contradict an opt-out in `.ki.toml`, such as `auto_memory = "disabled"`? Does the repository read its standard's own sections, such as `ki-repo-harness` source layout and root orientation, where the audit does not reach? What is safe to conform now?
- **Produces.** Judgement fixes committed, and findings that need more than a fix, each given a disposition under the focus rule rather than parked.

### Level 3: master repository checklist

- **Purpose.** A deeper, always judgemental review of whether the repository meets its needs and fulfils its place in the wider estate. It runs on no rubric.
- **Inputs.** The `ki-repo` [REVIEW procedure](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/mode-review.md) and its lenses: purpose and stability, governance, naming and identity, documentation and knowledge, necessity, structure, contracts, human use, security and data, dependencies, performance and release, duplication, tests, scripts and operations, and language.
- **Typical questions.** Is the baseline recorded rather than held in memory? Does every work record exist and does its status match reality, checked against its Git history and against whether its subject still exists? Is the roadmap cleared down: every triage record dispositioned, adopted, merged, cancelled or held, with none left without a decision; every record awaiting review brought to acceptance; done and cancelled records pruned once nothing live depends on them; expired batch records closed; `ki repo roadmap summary` free of diagnostics, such as an issuing area `.ki.toml` does not declare; and each held record past its `hold.review` date raised with the owner? Does each record's body still agree with later decisions in its Project note? Have renames reached every reference, by a grep for the repository's previous names across the whole territory, with an allow-list for names kept on purpose, for history or for Workers? Does every cross-reference resolve, with each reference to a merged, cancelled or pruned record repointed to the surviving record's section or to the record's last revision? Does a guide's file tree name only paths that exist? Does the declared skill set cover every capability used? Does the agent guidance overlap the skills: do `AGENTS.md`, `CLAUDE.md` and any legacy or agent memory, such as `Admin/MEMORY.md` or Claude memory, restate or contradict what a declared skill already owns, with each overlap cut to a pointer to the skill? Have the working areas been cleaned up: is the `+/` inbox triaged, with no hand-in left stale, and is every `+/_WORK/<id>/` work package, not only the coordinator's own, tidied under the `ki-work-package` [tidying rules](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#tidying-the-work-folder), with handled message lines removed in a commit naming each disposition, answered queries removed, the [decisions life cycle](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#decisions-life-cycle) worked, and report and brief copies whose outcome is homed pruned?
- **Produces.** Fixes made now, record candidates for bigger work, ideas, and close candidates for Kris. Lenses that do not apply are skipped without comment; the procedure's full output shape is not required.

### Level 4: master territory checklist

- **Purpose.** The same deep, judgemental review at territory level: what no single repository can see. It is State of play's own work, on top of each repository's levels 1 to 3.
- **Inputs.** Each repository's level 1 to 3 results, the Capital's Charter, Known Lands and registry, every work package in the territory, and the machine-local state of the host the pass runs on.
- **Typical questions.** Does every member's record name a Project or theme, and does it resolve in the Capital's registry? Does each record sit in the repository that delivers its outcome? Do the Charter, Known Lands and `territory_members` agree on the territory's members? Is the same fix, or the same broken link, waiting in more than one package? Are the territory's repositories on one baseline, such as maturity, hooks and toolchain versions? Does each theme or Project index match its notes, such as the Themes index against each theme's `direction`? Is common guidance worth promoting into shared skills: comparing `AGENTS.md`, `CLAUDE.md` and memory across the members, does the same approach recur in several repositories, so that it belongs in a skill and each repository keeps only a pointer? Has each repository's roadmap been cleared down at level 3, with no triage record left without a decision and no overdue hold left unraised? Have the working areas been cleaned up across every repository in the territory, each `+/` inbox triaged, with no hand-in idle in a member's `+/` with no package line, and every work package, not only State of play's own, tidied under the same [tidying rules](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#tidying-the-work-folder), with each untidy folder named in a line in its own `messages.md`? Has the XDG state been reviewed: on the host the pass runs on, is the territory's machine-local state under `~/.local/state/ki/`, such as the `~/.local/state/ki/agents/<territory>/` run folders, their status files and reports, and the temporary run folders, closed and cleared once each run's report is homed, with no run left open, no report left unread and nothing kept that should be in Git?
- **Produces.** Territory-wide findings, each with a disposition, and messages to the packages that own them. It reads levels 1 to 3; it does not repeat them. Machine-local state is per host, so the pass names the host it reviewed.

## PMO track

The PMO track is worked bottom up, so that what is in flight is settled before the structure that classifies it is judged.

### Level 1: work packages

- **Purpose.** Check work in flight or dispatched. Every active Project has one work package, on hold included. A planned Project has none, except the on-hold package State of play may create solely to queue a first message for it, with `hold.release: when Kris opens this Project work`; its planning, and any other message meant for it, goes through State of play. Regular work, which no Project lifecycle governs, has its own package, which names its theme. Nothing in a package should be really deferred work.
- **Inputs.** Every package's five files under `+/_WORK/`, in the Capital and in each member, and the registry's Project lifecycles.
- **Typical questions.** Does each active Project have exactly one package, does each package's Project exist, and does any planned Project have a package other than an on-hold first-message one? Does each regular-work package name its theme, rather than `theme: null`? Does `state.md` match the package's own latest open or release line? Is any line deferred work, a duplicate of a record or of another package's line, already done, or waiting for a package that does not exist? Has a line's subject closed since it was written, or does it name a record now done, or ask for a field every named record already carries? Was every logged answer relayed where it was meant to go?
- **Produces.** Trims, each made by the package's own owner, and items that leave a package as records or ideas. Churn lives here, under the work, so that Streams stays stable.

A package is open in any state but Finished, On hold included.

### Level 2: roadmap records

- **Purpose.** Check that each record is still live and still in the right place.
- **Inputs.** Every open record's front matter and body in every member repository.
- **Typical questions.** Does the record's status match reality, or is it done but open, or stale? Does it sit in the repository that delivers it, under a named Project or theme? Does it carry the fields its standard requires, such as `size`? Does it duplicate or overlap another record? Is it a prune candidate? Is a build-order dependency on a record in the same repository, described in its prose, also in `blocked_by`, while work another repository must deliver stays in prose under `## Dependencies / blocks`, as the `ki-work-roadmap` work-item format sets?
- **Produces.** Field fixes made now, close and cancel candidates for Kris, and moves of captured records to a better place.

Sizes are shown in reports as a T-shirt label in capitals, 👕 S, 👕 M, 👕 L or 👕 XL, for the `ki-work-roadmap` `size` values `s`, `m`, `l` and `xl`, which are unchanged. There is no 👕 XS, because there is no `xs` value.

A "keep" in a staleness review says only that the record is still live; it does not decide a triage record, which still needs its triage decision at the level 3 clear-down.

### Level 3: Projects

- **Purpose.** Check that each Project is a finite outcome whose records cover it.
- **Inputs.** The Project notes and the records that name each Project.
- **Typical questions.** Is every known part of the Project's outcome represented by a record or by work in flight? Is the description clear and distinct from its neighbours? Is the Project near its outcome, so that a close-out assessment is due? Has a planned Project become active, so that it now needs a package?
- **Produces.** Record candidates for gaps in an outcome, ideas in the Project's Notes, and description fixes.

### Level 4: themes

- **Purpose.** Check that each theme is used, distinct, and still the right direction for the work that names it.
- **Inputs.** The theme pages, the Projects that name them, and the records that name a theme directly.
- **Typical questions.** Is each theme used? Does any record, Project or site sit outside every theme? Does any record or Project strain against its theme's direction? Does work that names a theme directly really never finish?
- **Produces.** Ideas in theme Notes, and candidate changes to themes for level 5.

### Level 5: the territory overall

- **Purpose.** Judge the shape of the whole: whether the territory has the themes and Projects it needs.
- **Inputs.** Levels 1 to 4 of both tracks.
- **Typical questions.** Does the territory need more themes? Should any theme or Project close or merge? Is State of play carrying the planning of each planned Project, with no messages left on a Project nobody is maintaining? Are the Project descriptions clear and distinct across the registry?
- **Produces.** Queries for Kris, each with a recommended option; nothing is opened, closed or renamed without Kris.

## The focus rule

Do now what is needed now, and burn it down inside the pass. Tending does not create work for later: it does not load work packages with lines, and it does not turn every finding into a roadmap record.

Only bigger work, which needs more thought than the pass can give it, becomes a roadmap record. It is captured during the pass in the best place known at the time, meaning the owning repository and the Project or theme that seems right. Later levels of the PMO track re-read what was captured and move it if a better place shows.

Each finding gets exactly one disposition:

- **Fix now.** A small change in its owning repository, made by the pass's own run under that repository's gates.
- **Record.** Bigger work, captured as a triage record in the owning repository, naming its Project or theme. The owning work's coordinator captures; a run proposes the record as a candidate and does not write it.
- **Idea.** A thought worth keeping that is not yet work, written as a dated `Idea:` line in the Notes of the Project or theme it belongs to. Registry notes name no work record, so an idea refers to records by subject, not by identifier.
- **Message.** A line to an existing work package that owns the item. A line never waits for a package that does not exist; such an item becomes a record or an idea instead.
- **Drop.** Recorded in the decisions log with its reason, such as already done or duplicated.
- **Query.** Only where Kris must choose, such as closing a record, closing a Project or changing canonical knowledge.

## Reports

A level's report is as light as its outcome allows. "Fixed X" is a complete report; so is "nothing to tend". It names what was fixed, the dispositions it gave and any query for Kris, and nothing else is required: no counts, no per-lens sections and no narrative. A dispositions table a brief asks for is part of Done, not a finding, because only an owner request makes a [finding](findings.md#what-counts-as-a-finding).

## Where it could later become mechanical

The pilot runs found checks that were judged by hand but have a clear yes or no answer. They are listed so later runs can confirm them; no tooling is proposed here.

- A member repository's record names no Project or theme, or names one that does not resolve in the Capital's registry. The Capital's own audit cannot see members' records, and VA-WEBSITE-SANC-011 names none while passing every audit.
- A package line names a package that does not exist.
- A package line names a record now done, or asks for a field every named record already carries.
- A package's `state.md` disagrees with its own latest open or release line.
- An active Project has no package, a planned Project has one other than an on-hold first-message package, or a package's Project is not in the registry.
- A regular-work package gives `theme: null`.
- A record is done but open, because its subject no longer exists or its acceptance sits only in a package line.
- A cross-reference does not resolve, or a link to a pruned record could be pinned to its last revision.
- A repository's previous names still appear in its own, other members' or the Capital's tracked files, with an allow-list for deliberate mentions.
- A guide's file tree names paths that do not exist.
- A removed opt-in is still another declared skill's dependency, or an opted-in skill has lost the skill that needed it.
- Documentation contradicts an opt-out in `.ki.toml`, such as `auto_memory = "disabled"`.
- The installed harness is not at its pinned or `main` revision.
- A harness orientation leaves out the audit and conform commands, or a shelf README contradicts the standard on MCP source.
- A root orientation section is missing from AGENTS.md.
- A specification claims `conforming` with no Evidence line.
- A theme or Project index disagrees with its notes.
- An audit baseline records only the verdict, because the default output hides passes and judgement items.

## Open questions

The pilots raised these, and no answer is settled yet:

- **Small repairs under an adopted record.** Whether a small repair that falls under an already adopted record is a fix now or part of that record's delivery.
- **Member packages from the Capital.** How State of play sees each member repository's packages and the package lines that name each repository, short of reading every member's `+/_WORK/` by hand.
- **Offline audit.** Whether `ki repo audit` gains a mode that skips every remote check, for briefs that bar remote calls; until then the per-skill route under [Running a pass](#running-a-pass) stands. If wanted, it is a tools-ki record candidate.
- **Near its outcome.** A sign that a Project is near its outcome before its records finish, and a maturity rule of thumb for a repository.
- **Noisy checks.** CLEAN-4 fires on the run's own local commits and counts other sessions' commits; whether it should count only what the run did not make.
- **Due dates.** Due dates held only in a record's body. This waits on the UNATTENDED-AND-DUE-DATES assessment in Ways of working, which may give records a `due` field.
- **Capital skill baseline.** The BASELINE question, which skills every Capital should declare, waits on State of play's blind review of its skills assessment, then comes here as a level 4 question.

## Findings: Valle Armonia pioneer run, 2026-10-24

The run covered the Capital, va-principal, and three members: apps-vallearmonia.com, apps-markhowarth.com and va-agentic-harness.

- **Structural 1.** Useful: exact findings and before-and-after counts. Noise: one out-of-repository failure repeated in every repository. Missing: member records against the Capital's registry.
- **Structural 2.** Useful: fixed most failures before any deeper review. Noise: a holding-point instruction parked 23 findings that each needed a disposition later. Missing: a check that removing an opt-in does not break a declared skill's dependency.
- **Structural 3.** Useful: a few REVIEW items did most of the work: record status, renames, cross-references and skill coverage. Noise: lenses and pull-request items that did not apply, and the full output shape for small repositories. Missing: a rule for a small repair under an already adopted record.
- **Structural 4.** Useful: only the territory view found member records naming unregistered Projects or themes, and deferred items held in packages. Noise: a first draft that proposed tooling. Missing: a list of the package lines that name each repository.
- **PMO 1.** Useful: found deferred work held as package lines, and lines waiting for absent packages. Noise: one line where a repository has no packages. Missing: a definition of "open" for packages, and a rule for a planned Project's package.
- **PMO 2.** Useful: found done-but-open and stale records, and missing sizes. Noise: one line where a repository has no records. Missing: records whose acceptance sits only in a package line.
- **PMO 3.** Useful: checking records against each Project's outcome found gaps. Noise: re-reading Project notes confirmed the same morning. Missing: a sign that a Project is near its outcome before its records finish.
- **PMO 4.** Useful: mapped unregistered labels onto existing themes. Noise: largely confirmed levels 2 and 3. Missing: nothing material.
- **PMO 5.** Useful: turned scattered observations into a short set of decisions for Kris. Noise: merge questions already settled. Missing: a standing rule for a planned Project's package.

The definition of "open" and the planned-Project rule are now under [PMO level 1](#level-1-work-packages).

## Where it came from

Kris, 24 October 2026, 07:57 BST: "there's four levels in a structural track ... I'm not looking to put any tooling in place for those ... make sure that we preserve this track concept when we hand it off". And of the PMO track: "the focus on all these is not to create more work". At 08:18 BST Kris named it: "The key thing is the process and the alignment and the continual kind of I guess it's like gardening of the knowledge, right? Tending of the knowledge." At 08:42 BST Kris set the package rule: "maybe we only need to do work packages for every active project", with a planned Project's planning done "through the state of play", because "we don't get too much churn under streams and ... any churn is really under the work".

Later the same day Kris widened the checklists. On the master checklists: "I also meant auditing things like agents.md and claude.md to make sure that we weren't overlapping with things that are already in skills and the promotion of things into skills where there's commonality in their approach across multiple repositories." At 17:16 BST, under TENDING-XDG-STATE: "Another thing for tending is that we need to make sure that things like the XDG state is also considered and reviewed." On va-principal's roadmap clear-down: "We should probably add that into the list so that we do this for other tending activities." Kris also asked for the working-area clean-up check, and liked showing sizes as a T-shirt label in capitals.

This note supersedes the earlier territory-review draft in va-principal, pruned there; its [last revision](https://github.com/vallearmonia/va-principal/blob/40dc02a3/+/_WORK/va/design/territory-review.md) points to the full drafts, the latest being [`feb280bd`](https://github.com/vallearmonia/va-principal/blob/feb280bd/+/_WORK/va/design/territory-review.md). Kris's 07:57 "no tooling" replaces that draft's proposed `ki territory` audit and its `ki-work-package` rubric item; the draft's AUDIT and CONFORM framing survives as the territory level of the structural track.

## Other territories

Later runs add a `### <Territory> run, <date>` section here, a few short lines per level on what was useful, what was noise and what was missing, noting where their territory's shape differed. What each section raised is folded into the levels above, and the short answers to its open points are given beneath it.

### Valle Armonia round two, 2026-10-24

Four repositories: apps-vallearmonia.com, va-agentic-harness, apps-markhowarth.com, and va-principal with the territory and PMO track. About 6 to 12 minutes each.

- **Useful.** Decided package lines turned twelve warnings into one mechanical commit. Checking lines and records against Git history found three done or held lines and one done-but-open record. A territory-wide grep for previous names found a stale guide tree and a Known Lands entry the repository's own audit cannot see. A link resolver found a link to a pruned record in another repository. Reading the standard's own sections found gaps the audit does not catch, and the installed harness's Git state explained a fixed warning still reported.
- **Noise.** PMO levels 1 and 2 with nothing to read; one disposition repeated many times, CLEAN-3 over nine branches and STREAM-14 fourteen times; CLEAN-4 on the run's own and other sessions' commits; the previous-names check on names kept on purpose.
- **Missing.** Whether a member's run may carry out a decided line in another package; a record body against later Project decisions; a package line whose subject has since closed; an opt-in whose model is retired; an installed-payload check; a rule on prose dependencies and `blocked_by`.
- **Answers.** Skipping and collapsing are under [Running a pass](#running-a-pass), as is carrying out a decided line. The new checks are at structural levels 1 to 3 and PMO level 1, and the seven candidate mechanical checks are in [the mechanical list](#where-it-could-later-become-mechanical). A build-order dependency on a record in the same repository goes in `blocked_by` as well as the prose, as the work-item format already sets, at PMO level 2. CLEAN-4's counting stays an [open question](#open-questions).

### Valle Armonia interim pass, 2026-10-24

One quick territory pass applying Tending, findings and repository metadata as interim policy.

- **Worked.** The structural 4 and PMO 1 to 2 questions found every item in minutes; the per-skill `ki repo audit --skill` let a no-remote pass skip `ki-repo`'s GitHub checks; the one mechanical failure, an empty `messages.md` not reading `None`, was a one-line fix.
- **Unclear, with short answers.**
  1. A territory pass whose repositories' level 1 to 3 results are not fresh runs those repositories' level 1 itself and names them as not reviewed at levels 2 and 3, under [Running a pass](#running-a-pass).
  2. A planned Project may hold the on-hold package State of play creates solely to queue its first message, as markhowarth-launch does; PMO level 1 now says so.
  3. A record naming no Project or theme, like VA-WEBSITE-SANC-011, is now caught at structural level 4 and in the mechanical list.
  4. Structural level 1 has no offline audit mode; a no-remote brief runs it per skill and names the remote checks as not run, and a true offline mode is an [open question](#open-questions).
  5. The territory-review link in [Where it came from](#where-it-came-from) is now pinned to its last revision.

### Personal run, 2026-10-24

Four runs: tend-principal, tend-sites, meta-survey and tend-territory. Four packages share the Capital, most live work is regular work (Rig, Tower, Acquire intake) with one active Project, and two of six sites are run by regular-work packages under standing autonomy.

- **Fitted.** The per-skill conform and scoped hook check at structural 1; the opt-in check with its dependency test at 2, which found an orphaned `ki-work-recurring`; the clear-down, cross-reference, rename and working-area items at 3, which did nearly all the work and alone found expired batch records; comparing packages with the registry at PMO 1, which found a planned Project holding a package and an answer logged but never relayed; sizes, unthemed records and prune candidates at PMO 2. Only the territory view at structural 4 found regular-work packages giving `theme: null`, a Valle Armonia hand-in idle in a member's `+/` with no package line, the same broken link in two packages, and the Themes index drifting from two themes' `direction`. PMO 3 showed four Projects fully covered and Family and friends near its outcome; PMO 4 found three records and three sites that no theme covers.
- **Did not fit.** A whole-repository conform runs `rumdl --fix` over other packages' files; the full audit queries live GitHub against briefs that bar remote calls; read-only deploy repositories turned every fix into a query; PMO 1 had nothing to read in six site repositories; PMO 3 gained little from planned Projects with no work in flight.
- **Missing.** A rule for regular-work packages, including that each names its theme; a level 1 cross-reference check; whether a "keep" in a staleness review decides a triage record; a way to see a member's packages from the Capital; due dates held only in a record's body; a check that a theme or Project index matches its notes; a maturity rule of thumb.
- **Differed.** Four packages in one Capital kept gates hitting files not the run's to fix; findings on autonomous sites went as messages; one site moved to Legal during the day and was already out of `territory_members` and Known Lands.
- **Answers.** Per-skill conform in a shared repository, the no-remote route and fixes where a run may not write are under [Running a pass](#running-a-pass). Regular-work packages name their theme, at PMO level 1. The cross-reference check is at structural level 1. A "keep" does not decide a triage record, at PMO level 2. The index check is at structural level 4. Seeing member packages, due dates and a maturity rule of thumb stay [open questions](#open-questions).
