---
note_type: streams/design
updated: 2026-10-24T12:31:00Z
author: Written with Claude
---

# Tending

**Status:** a nascent area of Ways of working, being pioneered on the Valle Armonia territory. Other territory threads, personal-principal first, are invited to run it on their own territory and add their findings under [Other territories](#other-territories). Nothing here is a standard yet; the shape is expected to change as runs report back.

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-24 · **Pioneered by:** [VA > SoP](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/work.md), whose [decisions log](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/decisions.md) holds Kris's words from 07:39 to 08:02 BST on 24 October

Tending is the continual tending of a territory's knowledge: a repeated pass over a repository or a territory that takes stock and burns down what it finds. What matters is the process and the alignment it keeps, not the report it leaves.

## The process

Tending runs in two tracks, which look at the same estate from two sides:

- The **structural track** asks whether each repository, and the territory as a whole, is in the shape its standards and purpose expect. It has four levels, from everyday mechanical checks to a master territory checklist.
- The **PMO track** asks whether the work is in the right place: what is in flight, what is recorded, and whether the Projects and themes that classify it still fit. It has five levels and is worked bottom up, from work packages to the territory overall.

Both tracks are judgemental above their first level. Level 1 of the structural track uses the rubrics and tooling that already exist; every other level is a person or an agent reading and deciding, with no rubric and no new tooling.

### How the levels pick up each other's captures

The structural track runs before the PMO track in each repository, so the PMO track judges records and packages that already pass their checks. In the pioneer run, one run per repository took structural levels 1 to 3 and PMO levels 1 and 2 together, in parallel across repositories; then State of play took structural level 4 and PMO levels 3 to 5 for the whole territory.

Captures move upwards:

1. A structural level captures in the best place it knows: the repository it is reviewing and the Project or theme the work seems to belong to.
2. PMO level 1 picks up anything a package holds that is really a record, an idea or done.
3. PMO level 2 re-reads every captured record and moves it if another repository delivers it or another Project owns it.
4. PMO level 3 checks the captures against each Project's outcome and turns gaps into candidates.
5. PMO level 4 checks captures that name a theme directly and those that strain a theme's direction.
6. PMO level 5 reads everything above and brings structural change to Kris.

## Structural track

### Level 1: everyday mechanical audit and conform

- **Purpose.** Keep each repository passing its own mechanical checks, so the judgement levels start from a clean baseline.
- **Inputs.** The repository's `.ki.toml`, its declared skills and their rubrics, and the existing audit and conform tooling.
- **Typical questions.** What fails or warns? Which failures are this repository's to fix, and which belong elsewhere? Is each checkout's position against its upstream known?
- **Produces.** Mechanical fixes committed in the repository, and any remaining failure named with its owner.

### Level 2: ad hoc judgement audit and conform

- **Purpose.** Apply the judgement criteria of the declared skills where the mechanical checks cannot decide, when someone asks or when a baseline shifts.
- **Inputs.** Level 1's baseline, the judgement items of each declared skill, and the repository's own conventions.
- **Typical questions.** Does the repository meet the judgement items, not only the mechanical ones? Is each maturity, opt-in and orientation claim true? What is safe to conform now?
- **Produces.** Judgement fixes committed, and findings that need more than a fix, each given a disposition under the focus rule rather than parked.

### Level 3: master repository checklist

- **Purpose.** A deeper, always judgemental review of whether the repository meets its needs and fulfils its place in the wider estate. It runs on no rubric.
- **Inputs.** The `ki-repo` [REVIEW procedure](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/mode-review.md) and its lenses: purpose and stability, governance, naming and identity, documentation and knowledge, necessity, structure, contracts, human use, security and data, dependencies, performance and release, duplication, tests, scripts and operations, and language.
- **Typical questions.** Is the baseline recorded rather than held in memory? Does every work record exist and does its status match reality? Is the roadmap cleared down: every triage record dispositioned, adopted, merged, cancelled or held, with none left without a decision; every record awaiting review brought to acceptance; done and cancelled records pruned once nothing live depends on them; `ki repo roadmap summary` free of diagnostics, such as an issuing area `.ki.toml` does not declare; and each held record past its `hold.review` date raised with the owner? Have renames reached every reference? Does every cross-reference resolve, with each reference to a merged, cancelled or pruned record repointed to the surviving record's section or to the record's last revision? Does the declared skill set cover every capability used? Have the working areas been cleaned up: is the `+/` inbox triaged, with no hand-in left stale, and is every `+/_WORK/<id>/` work package, not only the coordinator's own, tidied under the `ki-work-package` [tidying rules](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#tidying-the-work-folder), with handled message lines removed in a commit naming each disposition, answered queries removed, the [decisions life cycle](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#decisions-life-cycle) worked, and report and brief copies whose outcome is homed pruned?
- **Produces.** Fixes made now, record candidates for bigger work, ideas, and close candidates for Kris. Lenses that do not apply are skipped without comment; the procedure's full output shape is not required.

### Level 4: master territory checklist

- **Purpose.** The same deep, judgemental review at territory level: what no single repository can see. It is State of play's own work, on top of each repository's levels 1 to 3.
- **Inputs.** Each repository's level 1 to 3 results, the Capital's Charter, Known Lands and registry, and every work package in the territory.
- **Typical questions.** Does every member's record name a Project or theme that resolves in the Capital's registry? Does each record sit in the repository that delivers its outcome? Do the Charter and Known Lands agree on the territory's members? Is the same fix waiting in more than one package? Are the territory's repositories on one baseline, such as maturity, hooks and toolchain versions? Has each repository's roadmap been cleared down at level 3, with no triage record left without a decision and no overdue hold left unraised? Have the working areas been cleaned up across every repository in the territory, each `+/` inbox triaged and every work package, not only State of play's own, tidied under the same [tidying rules](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#tidying-the-work-folder), with each untidy folder named in a line in its own `messages.md`?
- **Produces.** Territory-wide findings, each with a disposition, and messages to the packages that own them. It reads levels 1 to 3; it does not repeat them.

## PMO track

The PMO track is worked bottom up, so that what is in flight is settled before the structure that classifies it is judged.

### Level 1: work packages

- **Purpose.** Check work in flight or dispatched. Every active Project has one work package, on hold included, and a planned Project has none: its planning, and any message meant for it, goes through State of play. Nothing in a package should be really deferred work.
- **Inputs.** Every package's five files under `+/_WORK/`, and the registry's Project lifecycles.
- **Typical questions.** Does each active Project have exactly one package, does each package's Project exist, and does any planned Project have a package it should not? Does `state.md` match the package's own latest open or release line? Is any line deferred work, a duplicate of a record or of another package's line, already done, or waiting for a package that does not exist?
- **Produces.** Trims, each made by the package's own owner, and items that leave a package as records or ideas. Churn lives here, under the work, so that Streams stays stable.

### Level 2: roadmap records

- **Purpose.** Check that each record is still live and still in the right place.
- **Inputs.** Every open record's front matter and body in every member repository.
- **Typical questions.** Does the record's status match reality, or is it done but open, or stale? Does it sit in the repository that delivers it, under the right Project or theme? Does it carry the fields its standard requires, such as `size`? Does it duplicate or overlap another record?
- **Produces.** Field fixes made now, close and cancel candidates for Kris, and moves of captured records to a better place.

### Level 3: Projects

- **Purpose.** Check that each Project is a finite outcome whose records cover it.
- **Inputs.** The Project notes and the records that name each Project.
- **Typical questions.** Is every known part of the Project's outcome represented by a record or by work in flight? Is the description clear and distinct from its neighbours? Is the Project near its outcome, so that a close-out assessment is due? Has a planned Project become active, so that it now needs a package?
- **Produces.** Record candidates for gaps in an outcome, ideas in the Project's Notes, and description fixes.

### Level 4: themes

- **Purpose.** Check that each theme is used, distinct, and still the right direction for the work that names it.
- **Inputs.** The theme pages, the Projects that name them, and the records that name a theme directly.
- **Typical questions.** Is each theme used? Does any record or Project strain against its theme's direction? Does work that names a theme directly really never finish?
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

A level's report is as light as its outcome allows. "Fixed X" is a complete report; so is "nothing to tend". It names what was fixed, the dispositions it gave and any query for Kris, and nothing else is required: no counts, no per-lens sections and no narrative.

## Where it could later become mechanical

The pioneer run found checks that were judged by hand but have a clear yes or no answer. They are listed so later runs can confirm them; no tooling is proposed here.

- A member repository's record names a Project or theme that does not resolve in the Capital's registry. The Capital's own audit cannot see members' records.
- A package line names a package that does not exist.
- A package's `state.md` disagrees with its own latest open or release line.
- An active Project has no package, a planned Project has one, or a package's Project is not in the registry.
- A record is done but open, because its subject no longer exists or its acceptance sits only in a package line.
- A link to a pruned record could be pinned to its last revision.
- A repository's previous names still appear in its tracked files.
- A removed opt-in is still another declared skill's dependency.
- A root orientation section is missing from AGENTS.md.
- A specification claims `conforming` with no Evidence line.

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

## Where it came from

Kris, 24 October 2026, 07:57 BST: "there's four levels in a structural track ... I'm not looking to put any tooling in place for those ... make sure that we preserve this track concept when we hand it off". And of the PMO track: "the focus on all these is not to create more work". At 08:18 BST Kris named it: "The key thing is the process and the alignment and the continual kind of I guess it's like gardening of the knowledge, right? Tending of the knowledge." At 08:42 BST Kris set the package rule: "maybe we only need to do work packages for every active project", with a planned Project's planning done "through the state of play", because "we don't get too much churn under streams and ... any churn is really under the work".

This note supersedes the earlier [territory-review draft](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/design/territory-review.md) in va-principal. Kris's 07:57 "no tooling" replaces that draft's proposed `ki territory` audit and its `ki-work-package` rubric item; the draft's AUDIT and CONFORM framing survives as the territory level of the structural track.

## Other territories

Later runs add a `### <Territory> run, <date>` section here, a few short lines per level on what was useful, what was noise and what was missing, noting where their territory's shape differed.
