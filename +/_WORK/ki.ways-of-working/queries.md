# ki.ways-of-working queries

## Open

### GFM-ORDER - convert ki-principal outright, in verified batches

since 2026-10-19 21:36 BST · from gfm-scope · blind review (gfm-review, Codex) at 21:40 BST: agrees, adding prerequisites

**Context:** ki-principal holds about 1,000 Obsidian links and 15 image embeds; the review reproduced the counts and most convert by script. Some need a decision before their batch writes: four images fixed at width 800, which plain Markdown images cannot express; 10 links to headings, whose heading part the Observatory drops; 2 custom callouts; 2 Dataview blocks; the templates. Two harness checks misread the new link form, and the link audit checks wikilinks only, so those are fixed first. Plan: harness rules and audit fixes, a tools-ki converter with dry run and per-link verification, a 23-link pilot, then Streams, Admin and Pillars. Other islands convert when their owners choose.

**Query:** Should ki-principal be converted outright in zone batches, once the rules, converter, fixes and pilot are verified?

**Options:**

a) (recommended, confidence high - reviewed: the blind review reproduced the inventory and agrees, adding the fixes and per-batch exception decisions before any write) staged conversion as above, each batch failing closed on unresolved or unsafe links

b) adopt the GFM preference now and convert on touch only until the pilot proves batches

### FLAVOUR-FIELD - drop the per-note flavour field

since 2026-10-19 21:36 BST · from gfm-scope · blind review (gfm-review, Codex) at 21:40 BST: agrees

**Context:** On 2026-10-09 the idea was a front-matter field naming each note's flavour, so the change could be gradual. Converting on touch plus batch rewrites now does that job; a field would state intent without checking anything.

**Query:** Should the per-note flavour field be dropped?

**Options:**

a) (recommended, confidence high - reviewed: both runs agree a field adds upkeep and verifies nothing) drop it; define a repository-level setting only if an island chooses to stay Obsidian-flavoured

b) keep a per-note field as the marker of a converted note

### GFM-LINK-FORM - relative links in angle brackets

since 2026-10-19 21:36 BST · from gfm-scope · blind review (gfm-review, Codex) at 21:40 BST: agrees

**Context:** Only links relative to the note, such as `[Note](<../Folder/Note.md>)`, can work in GitHub, Zed, the Observatory and Obsidian alike. The authoring standard already uses angle brackets for paths with spaces; Obsidian itself writes `%20`, and the Observatory reads both. GitHub, Zed and Obsidian navigation are checked in the pilot.

**Query:** Should the house link form be note-relative paths in angle brackets?

**Options:**

a) (recommended, confidence high - reviewed: matches the existing authoring convention; the review confirmed Observatory and Obsidian parsing) note-relative paths in angle brackets, `ki repo conform` normalising Obsidian's `%20` form, and an audit failing any dangling or wrong-case link

b) note-relative paths with `%20`, as Obsidian writes them

### GFM-ENACT - one Enactment record for ki-principal

since 2026-10-19 21:36 BST · from gfm-scope · blind review (gfm-review, Codex) at 21:40 BST: agrees

**Context:** The batches change link syntax across Admin and Pillars without changing meaning, but the convention notes (`AGENTS.md`, the Charter, Structure, Format, Notes, Obsidian, Tending) and the Wikilink Review Activity need real rewording, so this is not trivial formatting.

**Query:** Should one Roadmap record carry the whole ki-principal conversion through the Enactment Process?

**Options:**

a) (recommended, confidence high - reviewed: related changes share one record under the existing rule) one `Streams/Roadmap/` record covering the batches, exceptions, convention notes and the Activity

b) your explicit bounded instruction in place of a record, with a record only for the convention rewrites

### TOUCH-SCOPE - what "touch" converts

since 2026-10-19 21:36 BST · from gfm-scope · blind review (gfm-review, Codex) at 21:40 BST: agrees on the whole file, at lower confidence

**Context:** "If you touch a file, it changes" could mean the whole file or only the edited lines. Scoping said whole file at high. The review agrees but at medium: a touched file may hold unresolved links, generated content or constructs with no GFM form, so the converter must stop and flag those rather than rewrite them, and generated or protected files need rules before the rule switches on.

**Query:** Does editing a file convert the whole file, once the safe converter exists?

**Options:**

a) (recommended, confidence medium - reviewed: the review backs whole-file conversion only once the converter refuses unsafe files; scoping had it high) whole file in the same change, via the converter; an unsafe file is flagged or given a recorded exception

b) edited lines only during the transition, the rest left for a batch

### METHOD-READ-RUBRIC - flag a non-revision `method_read`

since 2026-10-19 21:29 BST · from ki.tools-burndown (METHOD-READ-VALUES)

**Context:** Six works wrote a UTC time into `state.md` `method_read`, where the standard expects the short harness revision whose method they last read; nothing flagged it. Each has been told to fix it at its next refresh. ki.tools-burndown suggests the `ki-work-package` rubric flag any value that is not a revision.

**Query:** Should a small harness run add that rubric check?

**Options:**

a) (recommended, confidence high - one mechanical check that matches the standard's existing wording) add the check now in one harness run, pushed fast-forward only if alone

b) leave it to the next round

## Parked

Nothing parked.
