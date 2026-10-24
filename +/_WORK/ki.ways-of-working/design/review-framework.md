---
note_type: streams/design
updated: 2026-10-24T07:20:00Z
author: Written with Claude
---

# Review framework

**Status:** a nascent area of Ways of working, being pioneered on the Valle Armonia territory. Other territory threads, personal-principal first, are invited to run it on their own territory and add their findings under [Other territories](#other-territories). Nothing here is a standard yet; the shape is expected to change as runs report back.

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-24 · **Pioneered by:** [VA > SoP](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/work.md), whose [decisions log](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/decisions.md) holds Kris's words from 07:39 to 08:02 BST on 24 October

Kris, 24 October 2026, 07:57 BST: "there's four levels in a structural track ... I'm not looking to put any tooling in place for those ... make sure that we preserve this track concept when we hand it off". And of the PMO track: "the focus on all these is not to create more work".

This note supersedes the earlier [territory-review draft](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/design/territory-review.md) in va-principal. Kris's 07:57 "no tooling" replaces that draft's proposed `ki territory` audit and its `ki-work-package` rubric item; the draft's AUDIT and CONFORM framing survives as the territory level of the structural track.

## What it is

A review takes stock of a repository or a territory and burns down what it finds. It runs in two tracks, which look at the same estate from two sides:

- The **structural track** asks whether each repository, and the territory as a whole, is in the shape its standards and purpose expect. It has four levels, from everyday mechanical checks to a master territory checklist.
- The **PMO track** asks whether the work is in the right place: what is in flight, what is recorded, and whether the Projects and themes that classify it still fit. It has five levels and is worked bottom up, from work packages to the territory overall.

Both tracks are judgemental above their first level. Level 1 of the structural track uses the rubrics and tooling that already exist; every other level is a person or an agent reading and deciding, with no rubric and no new tooling.

## The focus rule

Do now what is needed now, and burn it down inside the review. A review does not create work for later: it does not load work packages with lines, and it does not turn every finding into a roadmap record.

Only bigger work, which needs more thought than the review can give it, becomes a roadmap record. It is captured during the review in the best place known at the time, meaning the owning repository and the Project or theme that seems right. Later levels of the PMO track re-read what was captured and move it if a better place shows.

Each finding gets exactly one disposition:

- **Fix now.** A small change in its owning repository, made by the review's own run under that repository's gates.
- **Record.** Bigger work, captured as a triage record in the owning repository, naming its Project or theme. The owning work's coordinator captures; a run proposes the record as a candidate and does not write it.
- **Idea.** A thought worth keeping that is not yet work, written as a dated `Idea:` line in the Notes of the Project or theme it belongs to. Registry notes name no work record, so an idea refers to records by subject, not by identifier.
- **Message.** A line to an existing work package that owns the item. A line never waits for a package that does not exist; such an item becomes a record or an idea instead.
- **Drop.** Recorded in the decisions log with its reason, such as already done or duplicated.
- **Query.** Only where Kris must choose, such as closing a record, closing a Project or changing canonical knowledge.

## Structural track

### Level 1: everyday mechanical audit and conform

- **Purpose.** Keep each repository passing its own mechanical checks, so the judgement levels start from a clean baseline.
- **Inputs.** The repository's `.ki.toml`, its declared skills and their rubrics, and the existing audit and conform tooling.
- **Typical questions.** What fails or warns? Which failures are this repository's to fix, and which belong elsewhere? Is each checkout's position against its upstream known?
- **Produces.** Mechanical fixes committed in the repository, and a baseline count before and after, with each remaining failure named with its owner.

### Level 2: ad hoc judgement audit and conform

- **Purpose.** Apply the judgement criteria of the declared skills where the mechanical checks cannot decide, when someone asks or when a baseline shifts.
- **Inputs.** Level 1's baseline, the judgement items of each declared skill, and the repository's own conventions.
- **Typical questions.** Does the repository meet the judgement items, not only the mechanical ones? Is each maturity, opt-in and orientation claim true? What is safe to conform now?
- **Produces.** Judgement fixes committed, and findings that need more than a fix, each given a disposition under the focus rule rather than parked.

### Level 3: master repository checklist

- **Purpose.** A deeper, always judgemental review of whether the repository meets its needs and fulfils its place in the wider estate. It runs on no rubric.
- **Inputs.** The `ki-repo` [REVIEW procedure](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/mode-review.md) and its lenses: purpose and stability, governance, naming and identity, documentation and knowledge, necessity, structure, contracts, human use, security and data, dependencies, performance and release, duplication, tests, scripts and operations, and language.
- **Typical questions.** Is the baseline recorded rather than held in memory? Does every work record exist and does its status match reality? Have renames reached every reference? Does every cross-reference resolve? Does the declared skill set cover every capability used?
- **Produces.** Fixes made now, record candidates for bigger work, ideas, and close candidates for Kris. Lenses that do not apply to a repository are named in one line and skipped.

### Level 4: master territory checklist

- **Purpose.** The same deep, judgemental review at territory level: what no single repository can see. It is State of play's own work, on top of each repository's levels 1 to 3.
- **Inputs.** Each repository's level 1 to 3 results, the Capital's Charter, Known Lands and registry, and every work package in the territory.
- **Typical questions.** Does every member's record name a Project or theme that resolves in the Capital's registry? Does each record sit in the repository that delivers its outcome? Do the Charter and Known Lands agree on the territory's members? Is the same fix waiting in more than one package? Are the territory's repositories on one baseline, such as maturity, hooks and toolchain versions?
- **Produces.** Territory-wide findings, each with a disposition, and messages to the packages that own them. It reads levels 1 to 3; it does not repeat them.

## PMO track

The PMO track is worked bottom up, so that what is in flight is settled before the structure that classifies it is judged.

### Level 1: work packages

- **Purpose.** Check work in flight or dispatched. A package is an active piece of work, so there should be one open package for every open Project, and nothing in a package that is really deferred work.
- **Inputs.** Every package's five files under `+/_WORK/`, and the registry's Project lifecycles.
- **Typical questions.** Does each open Project have exactly one package, and does each package's Project exist? Does `state.md` match the package's own latest open or release line? Is any line deferred work, a duplicate of a record or of another package's line, already done, or waiting for a package that does not exist?
- **Produces.** Trims, each made by the package's own owner, and items that leave a package as records or ideas.

### Level 2: roadmap records

- **Purpose.** Check that each record is still live and still in the right place.
- **Inputs.** Every open record's front matter and body in every member repository.
- **Typical questions.** Does the record's status match reality, or is it done but open, or stale? Does it sit in the repository that delivers it, under the right Project or theme? Does it carry the fields its standard requires, such as `size`? Does it duplicate or overlap another record?
- **Produces.** Field fixes made now, close and cancel candidates for Kris, and moves of captured records to a better place.

### Level 3: Projects

- **Purpose.** Check that each Project is a finite outcome whose records cover it.
- **Inputs.** The Project notes and the records that name each Project.
- **Typical questions.** Is every known part of the Project's outcome represented by a record or by work in flight? Is the description clear and distinct from its neighbours? Is the Project near its outcome, so that a close-out assessment is due?
- **Produces.** Record candidates for gaps in an outcome, ideas in the Project's Notes, and description fixes.

### Level 4: themes

- **Purpose.** Check that each theme is used, distinct, and still the right direction for the work that names it.
- **Inputs.** The theme pages, the Projects that name them, and the records that name a theme directly.
- **Typical questions.** Is each theme used? Does any record or Project strain against its theme's direction? Does work that names a theme directly really never finish?
- **Produces.** Ideas in theme Notes, and candidate changes to themes for level 5.

### Level 5: the territory overall

- **Purpose.** Judge the shape of the whole: whether the territory has the themes and Projects it needs.
- **Inputs.** Levels 1 to 4 of both tracks.
- **Typical questions.** Does the territory need more themes? Should any theme or Project close or merge? Does a planned Project need a package yet? Are the Project descriptions clear and distinct across the registry?
- **Produces.** Queries for Kris, each with a recommended option; nothing is opened, closed or renamed without Kris.

## How the levels pick up each other's captures

The structural track runs before the PMO track in each repository, so the PMO track judges records and packages that already pass their checks. In the pioneer run, one run per repository took structural levels 1 to 3 and PMO levels 1 and 2 together, in parallel across repositories; then State of play took structural level 4 and PMO levels 3 to 5 for the whole territory.

Captures move upwards:

1. A structural level captures in the best place it knows: the repository it is reviewing and the Project or theme the work seems to belong to.
2. PMO level 1 picks up anything a package holds that is really a record, an idea or done.
3. PMO level 2 re-reads every captured record and moves it if another repository delivers it or another Project owns it.
4. PMO level 3 checks the captures against each Project's outcome and turns gaps into candidates.
5. PMO level 4 checks captures that name a theme directly and those that strain a theme's direction.
6. PMO level 5 reads everything above and brings structural change to Kris.

## Where it could later become mechanical

The pioneer run found checks that were judged by hand but have a clear yes or no answer. They are listed so later runs can confirm them; no tooling is proposed here.

- A member repository's record names a Project or theme that does not resolve in the Capital's registry. The Capital's own audit cannot see members' records.
- A package line names a package that does not exist.
- A package's `state.md` disagrees with its own latest open or release line.
- An open Project has no package, or a package's Project is not in the registry.
- A record is done but open, because its subject no longer exists or its acceptance sits only in a package line.
- A link to a pruned record could be pinned to its last revision.
- A repository's previous names still appear in its tracked files.
- A removed opt-in is still another declared skill's dependency.
- A root orientation section is missing from AGENTS.md.
- A specification claims `conforming` with no Evidence line.

## Findings: Valle Armonia pioneer run, 2026-10-24

The run covered the Capital, va-principal, and three members: apps-vallearmonia.com, apps-markhowarth.com and va-agentic-harness. Structural levels 1 and 2 ran first, as the tidy and judgement audit-and-conform runs from 07:09 to 07:35 BST; the territory-review run took a first pass at structural level 4 from 07:39 to 07:50; four burn-down runs, one per repository, took structural levels 1 to 3 and PMO levels 1 and 2 from 07:49 to 08:10; and the framework run took PMO levels 3 to 5 and the package check for the territory from 08:05 to 08:18.

### Structural level 1: everyday mechanical audit and conform

- **Useful.** The baseline audit gave exact findings and a before-and-after count in every repository: the website went from FAIL 20, WARN 53 to FAIL 2, WARN 25 across the day, and va-principal from FAIL 8, WARN 29 to FAIL 1, WARN 16.
- **Noise.** Failures outside the repository, BIND-2 in chezmoi's MCP source, came back in all four repositories as the same finding.
- **Missing.** The audit does not see a member's records against the Capital's registry, so 12 website records with unregistered themes passed the Capital's audit. The size scale offered in briefs included `xs`, which neither the standard nor the audit accepts.
- **Should be mechanical.** Already is; the gaps above belong in it.
- **Time.** Not timed apart from level 2; the audit itself is quick, and most of the time went on reading the findings.

### Structural level 2: ad hoc judgement audit and conform

- **Useful.** It fixed most failures before any deeper review: hooks and `.rumdl.toml` in va-principal, seven commits of conform in the website, and the harness baseline. Its judgement items also found that the Charter and Known Lands disagree on the territory's members.
- **Noise.** Run under a holding-point instruction, it parked 23 findings rather than burning them down, and each later needed a disposition. Under the focus rule this level fixes what it can and dispositions the rest.
- **Missing.** A check that removing an opt-in does not break another declared skill's dependency; the harness run found it only because the audit stopped.
- **Should be mechanical.** Making the coverage check respect skill dependencies, and pruning stale runtime projections after an opt-in is removed.
- **Time.** About 6 minutes for va-agentic-harness and apps-markhowarth.com, 8 for va-principal and 26 for the website, most of the website's in its full test gate before each commit.

### Structural level 3: master repository checklist

- **Useful.** A few REVIEW items did most of the work. "The work record exists and its status matches reality" found three stale or done-but-open records in va-principal and one in the website. "Renames propagated to every reference" found stale names in va-principal and apps-markhowarth.com. "Every cross-reference resolves" found a stale setup guide and a hero-video recipe path in the website. "The declared skill set covers every capability used" found a dependency clash in the harness. Running a real validator on a disputed file settled a migration in one step.
- **Noise.** Most of the purpose lens for a single-site repository; pull-request items in repositories that commit on `main`; the knock-on items for Ready-plan pull requests and `package.json` in a knowledge base; and the full 13-section output for a small repository. Empty lenses should collapse to one line.
- **Missing.** A rule for a two-line repair under an already adopted record, which the website run had to judge; and a check that a specification's `conforming` claim has an Evidence line.
- **Should be mechanical.** Previous repository and Worker names lingering in tracked files; pinned last-revision links for pruned records; a missing root orientation section.
- **Time.** About 3 to 6 minutes per repository, mostly reading the standards' wording.

### Structural level 4: master territory checklist

- **Useful.** Only the territory view found that 17 website records name no registered Project or theme, that two Projects both claimed corrections to canonical governance while no rule placed harness work beyond its baseline, and that deferred items sat in the territory package and a Project package. It confirmed that no record sat in the wrong repository.
- **Noise.** Its first draft proposed tooling and a rubric item, which Kris's 07:57 instruction removed; and it called itself "not tidy, audit or conform" until reframed as territory audit and conform.
- **Missing.** A step that lists the package lines naming each repository, so a repository's run can see trims held in the Capital rather than in the repository under review.
- **Should be mechanical.** Registry resolution of member records, and package lines naming absent packages.
- **Time.** About 8 minutes for the first pass, and 3 more to reframe it.

### PMO level 1: work packages

- **Useful.** It found deferred work held as package lines (five website items that are really records, two lines waiting for packages that do not exist) and a duplicate of a record's awaiting-review state. The territory package check found every open Project has exactly one package, and that the rule needs "open" defined: the Community website Project is `active` while its package is on hold, and Territory alignment's package was opened by a message its `state.md` does not yet reflect.
- **Noise.** In a repository with no packages, such as the harness, the level is one line: "no packages; owner Project confirmed".
- **Missing.** A way for each repository's run to see the package lines that name it, since those live in the Capital; and a rule for whether a planned Project should have a package.
- **Should be mechanical.** Package lines naming absent packages; package lines a later line already reports done; `state.md` against the latest open line; open Projects without packages.
- **Time.** About 1 to 3 minutes per repository, and about 3 minutes for the territory check.

### PMO level 2: roadmap records

- **Useful.** It found done-but-open records (VA-PRINCIPAL-GOV-008, and VA-WEBSITE-GOV-004 whose sources directory no longer exists), an effectively done one (VA-PRINCIPAL-GOV-006), a stale one from an earlier era (VA-PRINCIPAL-GOV-003), and a sequencing overlap in the website. Provisional sizes went on every open record that lacked one.
- **Noise.** In a repository with no records, the level is one line.
- **Missing.** A check for records whose acceptance sits only in a package line, and a burn-down owner for each parked query.
- **Should be mechanical.** Done-but-open records whose subject no longer exists; missing `size`.
- **Time.** About 2 to 4 minutes per repository; the website's took longest, with 17 open records.

### PMO level 3: Projects

- **Useful.** Checking each record against its Project's outcome found what was missing: the Mark Howarth launch Project had no record for building its identity on the design system or for the launch itself. Reading the Project notes together found that Territory alignment is near its outcome, so its close-out assessment is the next exit, and that two Knowledge intake Notes lines say nearly the same thing.
- **Noise.** Re-reading Project notes that the registry run had confirmed the same morning; a short "unchanged since" line would do.
- **Missing.** A way to see how near a Project is to its outcome before its records finish; the close-out assessment only triggers when no record is open. Ideas given by subject collided with the rule that registry notes name no work record, so the framework now says ideas refer to records by subject.
- **Should be mechanical.** Project-outcome coverage, given a per-Project list of outcome clauses.
- **Time.** About 4 minutes for the territory.

### PMO level 4: themes

- **Useful.** Reading each theme's direction against the labels member records carry: the website's six unregistered labels all map onto Presence, Stewardship or a Project, and only the member-area record straddles directions.
- **Noise.** With three themes, all used, it largely confirmed what levels 2 and 3 had shown; it can collapse to one line when nothing strains.
- **Missing.** Nothing material.
- **Should be mechanical.** Theme resolution of member records, as at structural level 4.
- **Time.** About 2 minutes.

### PMO level 5: the territory overall

- **Useful.** It turned the levels' scattered observations into a short set of decisions for Kris: what "open" means for packages, whether planned Projects get packages, whether more themes are needed, and when Territory alignment closes.
- **Noise.** Merge questions between Projects that share a checkout but have distinct outcomes, such as the Community website and the Sanctuary library, were already settled and needed only one line.
- **Missing.** The standing rule for a planned Project's package, which this level had to propose rather than apply.
- **Should be mechanical.** Nothing; this level is judgement by nature.
- **Time.** About 3 minutes, after levels 1 to 4.

### Across the run

- Running the structural and PMO levels per repository in one run, in parallel, then the territory levels once, kept the whole pass to about 30 minutes of wall-clock time after the tidy runs.
- Most time went on reading standards and on full test gates before commits, not on judging.
- Runs that proposed record candidates rather than writing them kept capture with the owning coordinator, as CAPTURE-GATE requires, and the candidates came back in one place.

## Other territories

Later runs add a `### <Territory> run, <date>` section here, with the same per-level headings as the Valle Armonia findings, and note where their territory's shape differed.
