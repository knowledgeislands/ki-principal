# ki.ways-of-working queries

## Open

### GFM-ORDER - convert ki-principal outright or by touch only

since 2026-10-19 21:36 BST · from gfm-scope · in blind review (gfm-review)

**Context:** Every ki-principal construct except 2 callouts, 2 Dataview blocks, 10 heading links, 7 ambiguous links and the templates converts mechanically: 1,025 wikilinks and 15 embeds. Kris leans to "just do it". Doing it outright needs the harness rule change and a tools-ki converter first. Touch-only converts nothing until files are edited, which leaves the island mixed for months.

**Query:** Should ki-principal be converted outright, in zone batches, once the rule change and converter land?

**Options:**

a) (recommended, confidence medium - the inventory shows the work is mechanical, but the converter does not yet exist and the pilot has not run) Land the harness rules and the tools-ki converter, pilot on the 23 links in Resources, Calendar, root and `-`, then batch Streams, Admin and Pillars, followed by the judgement pass and the convention notes.

b) Adopt the clause now and convert on touch only, with no batches until a later decision.

c) Convert ki-principal by hand now in batches, without building a converter, and leave the other islands until one exists.

### FLAVOUR-FIELD - drop the 2026-10-09 front-matter flavour field

since 2026-10-19 21:36 BST · from gfm-scope · in blind review (gfm-review)

**Context:** On 2026-10-09 the idea was a per-note front-matter field declaring flavour, so the standard could change gradually. Touch-to-convert plus batch rewrites now does that job, and flavour is detectable mechanically. A long-term Obsidian-flavour island could instead declare it once in `.ki.toml`.

**Query:** Should the per-note flavour field be dropped?

**Options:**

a) (recommended, confidence high - detection is mechanical and a declared field would duplicate it and drift) Drop it. Add a repository-level `[skills.ki-authoring]` flavour key only if an island opts to stay Obsidian-flavoured.

b) Keep the per-note field as the marker of a converted note during the transition.

### GFM-LINK-FORM - relative angle-bracket paths as the house link form

since 2026-10-19 21:36 BST · from gfm-scope · in blind review (gfm-review)

**Context:** Only document-relative paths resolve the same on GitHub, Zed, the Observatory and Obsidian. Root-relative `/Admin/...` links work on GitHub but not in Obsidian, and Obsidian's "absolute in vault" form breaks on GitHub. The house standard already prescribes angle brackets for paths with spaces, and 441 ki-principal links point at such paths. Obsidian itself writes `%20`. Relative paths change when the linking file moves outside Obsidian, so a resolution audit becomes essential.

**Query:** Should the house link form for KB notes be document-relative paths in angle brackets?

**Options:**

a) (recommended, confidence medium - this is the only form all four readers resolve, but the cost when files move rests on a new audit) Use document-relative paths in angle brackets, have `ki repo conform` normalise Obsidian's `%20` form, and have the new LINK check fail on any dangling or wrong-case link.

b) Use document-relative paths with `%20` encoding, which matches what Obsidian writes, at the cost of less readable source.

### GFM-ENACT - one Enactment record for the ki-principal conversion

since 2026-10-19 21:36 BST · from gfm-scope · in blind review (gfm-review)

**Context:** The mechanical batches change link syntax across Admin and Pillars but not meaning. The convention notes (`AGENTS.md`, the Charter, Structure, Format, Notes, Obsidian, Tending) and the Wikilink Review Activity need substantive rewording. Under ki-principal's rules, related changes share one record, and Kris's explicit instruction can stand in only for a bounded change.

**Query:** Should a single Roadmap record carry the whole ki-principal conversion through the Enactment Process?

**Options:**

a) (recommended, confidence medium - the scale makes the formatting exemption a stretch, and the convention rewrites need a record in any case) Open one `Streams/Roadmap/` record covering the batches, the judgement pass and the convention notes.

b) Treat the mechanical batches as exempt formatting and open a record only for the convention notes and the Activity.

### TOUCH-SCOPE - what "touch" converts

since 2026-10-19 21:36 BST · from gfm-scope · in blind review (gfm-review)

**Context:** "If you touch a file, it changes" could mean converting the whole file whenever it is edited, or converting only the lines edited. Whole-file conversion keeps each file single-flavour and is mechanical through the converter. It does add link churn to unrelated diffs, which makes them noisier to review.

**Query:** Does touching a file convert the whole file?

**Options:**

a) (recommended, confidence high - single-flavour files are what make the audit and the Obsidian settings coherent) Convert the whole file, using the converter on that path, in the same change.

b) Convert only the edited lines and leave the rest for a batch.

### METHOD-READ-RUBRIC - flag a non-revision `method_read`

since 2026-10-19 21:29 BST · from ki.tools-burndown (METHOD-READ-VALUES)

**Context:** Six works wrote a UTC time into `state.md` `method_read`, where the standard expects the short harness revision whose method they last read; nothing flagged it. Each has been told to fix it at its next refresh. ki.tools-burndown suggests the `ki-work-package` rubric flag any value that is not a revision.

**Query:** Should a small harness run add that rubric check?

**Options:**

a) (recommended, confidence high - one mechanical check that matches the standard's existing wording) add the check now in one harness run, pushed fast-forward only if alone

b) leave it to the next round

## Parked

Nothing parked.
