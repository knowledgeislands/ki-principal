# ki.sop.main discussions

## Open

### KNOWLEDGE-PLAN - Start the knowledge folder as planned

focus: _emerging

**Context:** Covers ATTACH-HOW, ATTACH-SET, RENAME-WHEN and PACE, from the [knowledge folder design note](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/knowledge.design.md); RESOURCES-IN, where views differ, is asked separately below. The plan gives Knowledge Islands Principal a top-level `knowledge/` graph that replaces `Pillars/` over time: phase 0 adopts the standard under one governance decision and one Enactment record, phase 1 pulls the Inbox's 41 staged cards, phase 2 upgrades Pillars one subtree at a time behind pointers, phase 3 retires `Pillars/`. You asked for it "quickly". Waiting on this: ATER-014 (the Inbox's cards are ready to pull, with its PREDICATES and WORK-FOLDER questions left to the node standard), ATER-025 and its 6 November reminder (three records, now PERSONAL-INBOX-KNW-004, KNW-005 and KNW-010, are State of play's and are being pruned from krisb/inbox, so their content must be captured from their last revisions), and ATER-011 STOA-NAMES (how icon cards name icons, taken with the iconography pull). Your SKILLS-OVER-GRAPH words of 6 November, "separate out things that are versus things that can inform", mean the graph method itself becomes a skill (see SKILLS-OVER-GRAPH below), while the graph holds what is.

**Query:** Should phases 0 and 1 go ahead this week with the four choices as recommended?

**Options:**

a) (recommended, confidence high - ATTACH-HOW and ATTACH-SET reviewed: an independent reviewer chose the same, adding a stable never-reused id and path retired by a kept pointer; RENAME-WHEN and PACE high because renaming earlier would move links twice and this is the fastest route that keeps the Enactment gate) Attachment points are a front matter flag `attachment: true`, listed on `knowledge/_index.md` and promising a stable id and path retired by pointer, with shadow nodes recording `shadows:` and `checked:`; the first ones are the capture funnel, the knowledge graph and the work process once pulled; the older areas are lower-cased after Pillars is retired, one record per repository; phases 0 and 1 go under one approval this week, the harness carrying the standard in parallel; the phase 0 run also captures the three pruned records' content and ACKs ATER-014, ATER-025 and ATER-011.

b) The standard first, and the Knowledge Islands Principal bootstrap after it.

c) Declare no attachment points until the first slice has settled; otherwise as a).

### CHAIN-START-FIRST - A first step that runs and fails

focus: chain

**Context:** Split from the former CHAIN-START under the rule that a query still below high after review is split. As built, a repository whose first step ran and failed counts as "failed to start", alongside a checkout that could not be entered; "stopped" is a repository where a later step failed after at least one completed. The record's Discussion section and the tests follow the build's reading. This gates [KI-TOOL-MGIT-CLI-032](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-032-chain-command.md)'s acceptance under ACCEPTANCE.

**Query:** Should a first step that runs and fails count as "stopped" rather than "failed to start"?

**Options:**

a) (recommended, confidence medium - reviewed, views differ: the blind reviewer chose it at high because a Git step that ran has started and may already have changed things; the build run preferred b)) Yes: count it as "stopped", and change the record's Discussion and the tests to match.

b) Keep it as built: count it as "failed to start", because a failing first step is the common case worth singling out.

### OLD-ORPHANS - Where the old orphaned repositories live

focus: _emerging

**Context:** A query parked in [ki.prj.mac-studio-setup](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/work.md) concerns old orphaned repositories that were to be kept through the Mac Studio move. The census found no checkout of them under `~/workspaces` and no bundle in OneDrive. If they lived only on a retired disk or host, the last copies may be gone. Nothing is dropped while this is unknown; you kept this open when you agreed TIDY-UPS a) on 7 November.

**Query:** Where do the old orphaned repositories live now, or are they gone?

**Options:**

a) (recommended, confidence high - reviewed: only you can say whether another copy exists) You name the location or confirm they are gone, and ki.prj.mac-studio-setup records the answer before its query closes.

b) Treat them as lost and close the query.

### KA-CLOSE-GATE - Let the Knowledge acquisition close pass two superseded runs

focus: _emerging

**Context:** Under TIDY-UPS a) (7 November) the tidy-ups run tried to close the finished [ki.prj.knowledge-acquisition](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.knowledge-acquisition/work.md). Every package check holds (finished, decisions homed, no open query, no worktree, nothing queued), but `ki agent close` refused: two of its runs, `gov209-link` and `title-fix`, stopped without finishing on 17 to 18 October. Each was re-run as `gov209-link-2` and `title-fix-2`, and both of those finished. The only line in its `messages.md`, household-terra's HK-006 notice, asks for exactly this close-out. Nothing was deleted or archived. Not blind reviewed: this run could not launch a reviewer.

**Query:** May a State of play run close it, telling `ki agent close` to accept those two stopped runs as superseded?

**Options:**

a) (recommended, confidence medium - each stopped run has a finished re-run, and Git keeps the folder) Yes: close with `--accept-exited gov209-link --accept-exited title-fix` (never `--reconciled`), then delete the folder in one commit, `docs(work): ki.prj.knowledge-acquisition close-out`.

b) Leave the folder until you open that work's thread.

### OTHER-TERRITORIES - Send the cross-territory asks

focus: themes

**Context:** Covers ACCESS-ADMINS-ROUTE, BASELINE, HARNESS-LINK, LEGAL-GUIDANCE, HNR-GUIDANCE and THEME-REGISTRY; SANCTUARY-STAGE5 and GRANOLA, where views differ, are asked separately below. On 28 October you asked, for "all sites I run", for a per-site admins Access group and a `/admin` application admitting only it, and to "send the equivalent to ki-principal for all sites I run"; HNR has done its nine sites and the Knowledge Islands ones went to ki.prj.website and ki.prj.observatory, leaving Equal Remedy, Personal, TechMedix and Valle Armonia. The [skills assessment](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/_emerging/skills-assessment.report.md) found the eight Capitals differ: it recommends one common baseline recorded in `ki-repo-kb-principal` through ki.prj.ways-of-working, each Capital listing its own territory harness, legal's runtime-neutral mandates moving from `CLAUDE.md` into `AGENTS.md` (Codex does not read `CLAUDE.md`), hnr rewriting its out-of-shape `AGENTS.md`, and Equal Remedy capturing a theme registry. Each goes as one message to the territory's State of play, whose own gates decide. On 12 October you kept territories other than Personal and Valle Armonia parked until Knowledge Islands is bottomed out.

**Query:** Should State of play send these asks to the other territories now?

**Options:**

a) (recommended, confidence high - each reviewed or resting on your own words, and a message only queues work for each owner's own gates) Send them now: the Access admins line to Equal Remedy, Personal, TechMedix and Valle Armonia quoting you and linking HNR's note; adopt the Capital baseline through ki.prj.ways-of-working and message each State of play to conform; add each territory harness to its Capital; ask Legal to move its mandates into `AGENTS.md` and raise a record for harness skills; ask HNR to rewrite its `AGENTS.md`; ask Equal Remedy to capture a theme registry.

b) Send to Personal and Valle Armonia only, the territories running now, and keep the rest parked under your 12 October words.

c) Keep them all parked until Knowledge Islands is bottomed out.

### SANCTUARY-STAGE5 - Take the Sanctuary package at stage 5

focus: themes

**Context:** Carried over unchanged in substance. Under [ADR-VA-WEBSITE-009](/Users/krisbrown/kis/valle-armonia/apps-vallearmonia.com/docs/decisions/ADR-VA-WEBSITE-009-the-sanctuary-becomes-a-shared-editorial-library.md), Valle Armonia builds the Sanctuary editor through stages 2 to 4 and asks Knowledge Islands to own stage 5: a separate vendored package repository, with packages-portal-commons the nearest precedent. Valle Armonia hands over verified code, fixtures and adapter contracts at stage 4 and asks for agreement before VA-WEBSITE-SANC-008 is readied.

**Query:** Should Knowledge Islands agree now to take stage 5?

**Options:**

a) (recommended, confidence medium, review disagrees - Knowledge Islands decides Project and repository when there is something to receive) Agree now, and set its Project and repository at the stage 4 handover.

b) Agree in principle, with Knowledge Islands reviewing the adapter contracts and fixture shape before stage 4 starts; the blind reviewer prefers this at medium, to check the portability boundary before extraction hardens it.

c) Decline for now; Valle Armonia keeps the Sanctuary.

### GRANOLA - Declare Granola acquisition where it runs

focus: themes

**Context:** Carried over unchanged in substance. `ki-acquire-granola` is linked in six Capitals without being declared. hnr keeps a local `granola-sync` command; the blind review found legal's command and activity already retire direct import in favour of central acquisition. Since 5 November the acquisition skills point to the Inbox's `ki-muninn` rather than `ki acquire`.

**Query:** How should Capitals that acquire from Granola carry the skill?

**Options:**

a) (recommended, confidence medium, review partly disagrees - one consistent declaration) Declare `ki-acquire-granola` in ki, hnr, er, legal, personal and va, and retire the local commands once their routing is in the skill's configuration.

b) Declare it only where capture actually runs, keep central capture with local reconciliation, and retire a local importer only after its routing is verified; the blind reviewer proposes this at high.

c) Unlink it where no acquisition happens and keep the local commands.

### RESOURCES-IN - Resources in other territories' graphs

focus: _emerging

**Context:** Split from the knowledge plan, where views differ. In Knowledge Islands Principal, Resources stays outside `knowledge/`, because the island strictly enforces the split between its own knowledge and outside reference. Nothing in phases 0 and 1 waits on this.

**Query:** May another territory bring its Resources into its graph?

**Options:**

a) (recommended, confidence medium - reviewed, views differ: no territory has shown the need yet; the independent reviewer chose b) at high, letting each territory choose with its own provenance and access rules) No for now. Revisit when a territory asks.

b) Yes, as each territory chooses.

### RESUME-SPECS - Resume Portable specifications

focus: _emerging

**Context:** Carried over unchanged in substance. [ki.prj.portable-specifications](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.portable-specifications/state.md) has been paused since 20 October, released only when you say resume. Its draft 0.8 specifications passed six blind reviews, the last finding nothing, and its two parked queries, SPEC-TEXT and HOMING-EDITS, are both recommended at high. Resuming means planning KI-HARNESS-GOV-229 and KI-HARNESS-GOV-230 to Ready in the harness; the summary-model and emerging-only harness chain they waited on has finished. SKILLS-OVER-GRAPH's ask to rethink `ki-specs` touches the same ground. Timelines and Baseline rollout are paused the same way.

**Query:** Should Portable specifications resume now, with the other two paused works left as they are?

**Options:**

a) (recommended, confidence high - reviewed: an independent reviewer chose the same; owner review can resume now) Resume Portable specifications only: put SPEC-TEXT and HOMING-EDITS to you, then plan its harness records.

b) Keep all three paused until the open method queries are settled.

### STOA-NAMES - How icon cards name icons

focus: _emerging

**Context:** From the Inbox (ATER-011, 5 November, parked since 3 November), for the graph standard's icon cards, taken with the pull of the iconography cards. Stoa's icon mapping gives icons meaning-based names (`refresh-cw` for Phosphor's `arrows-clockwise`), while the staged icon-identities card says every icon reference names its source library, with no aliases across libraries. The two rules disagree for any card that names a Stoa icon.

**Query:** Which name should an icon card use for an icon?

**Options:**

a) (recommended, confidence medium - reviewed: an independent reviewer chose the same, since the icon identity card already separates product defaults from configured choices) Meaning-based names stay Stoa's product defaults, each resolving to one source-qualified identity, and the card says so.

b) Cards use only the source-qualified name, and Stoa's meaning-based names stay inside Stoa.

### PREDICATES - Keep the default related-links the tidy added

focus: _emerging

**Context:** From the Inbox (ATER-014, 5 November): its tidy of the 41 Knowledge Islands cards staged for the knowledge folder's phase 1 added a default `skos:related` link entry (a generic "is related to" link) wherever a card had no more specific link. Kris left keeping or pruning them to the node standard. The knowledge design note expects `skos:related` for links into Resources.

**Query:** Should the pull keep the default related-links or prune them?

**Options:**

a) (recommended, confidence medium - reviewed: an independent reviewer chose the same, since the staged Semantic Markdown card says an unannotated link must not acquire an invented predicate) Prune the defaults at pull, keeping only links the card's text supports.

b) Keep them all and let tending prune them later.

### WORK-FOLDER - Where the six work-related cards go

focus: _emerging

**Context:** From the Inbox (ATER-014, 5 November): six of the staged cards are about work rather than knowledge (workers, glyphs, refining decisions, the change-log graph, value-chain attribution, pioneering through practice). Kris left their place to the folder layout, asking whether they go to `knowledge/work/`. The Work Process note in Pillars already owns the model of work.

**Query:** Where should the six work-related cards land at pull?

**Options:**

a) (recommended, confidence medium - reviewed: an independent reviewer chose the same, as separate cards keep unaccepted proposals out of the canonical Work Process note) Pull them into `knowledge/work/`, each linking to the Work Process note.

b) Fold their content into the Work Process note through an Enactment record instead of pulling them as cards.

## Parked

- ALIAS-OWNERS (from ki.prj.estate-factorisation, under ESTATE-CLOSE a), 7 November): territory alias ownership is a governance residual; State of play keeps it parked until a Harness or Principal record owns it. Recommended: keep parked.
- GOVERNANCE (from ki.prj.estate-factorisation, under ESTATE-CLOSE a), 7 November): repository governance and projection follow-ups are State of play residuals, kept only where still real. Recommended: keep parked and check at the next stock-take.
