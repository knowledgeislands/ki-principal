# GFM migration: plan

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-19

Design note under `ki-work-design` for GFM-MIGRATION: Knowledge Islands prefers GitHub-flavoured Markdown (GFM), keeps other flavours supported, converts a file when it is touched, and may rewrite batches of files whole. It records the decided plan after Kris's answers at 22:00 BST on 19 October ("Do all recommended"), the prerequisites the blind review added, what the converter must do and the order of the ki-principal batches. The scoping and review reports are run reports under `~/.local/state/ki/agents/ways-of-working/` (`gfm-scope.report.md`, `gfm-review.report.md`); their outcome is carried here and in the decisions log. This note graduates when the harness rules land, the converter is released and the conversion record [KI-PRINCIPAL-OPS-014](<../../../../Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md>) carries the batch plan through delivery; it is then deleted in the same change.

## Contents

- [Decisions](#decisions)
- [Open](#open)
- [Owners and order](#owners-and-order)
- [Prerequisites](#prerequisites)
- [Converter requirements](#converter-requirements)
- [Batch order](#batch-order)
- [Other islands](#other-islands)

## Decisions

Kris, 2026-10-19 22:00 BST: "Do all recommended". The decisions log in this work package holds the read-back.

- **GFM-ORDER a.** Convert ki-principal outright in staged batches once the harness rules, the converter, the consumer fixes and a pilot are verified. Each batch fails closed: its exceptions are decided before it writes, not after all batches.
- **FLAVOUR-FIELD a.** No per-note flavour field. A file's flavour is observable from its syntax; a declared field would only describe intent and drift. A repository-level setting is added only if an island chooses to stay Obsidian-flavoured, through an explicitly defined configuration contract, not a speculative key now.
- **GFM-LINK-FORM a.** Internal links are document-relative paths, in angle brackets when the path contains a space: `[Note](<../Folder/Note.md>)`. `ki repo conform` normalises Obsidian's `%20` spelling structurally, keeping URI escapes that are needed. The link audit fails any dangling or wrong-case link and checks fragments.
- **GFM-ENACT a.** One `Streams/Roadmap/` record in ki-principal carries the whole conversion through the Enactment Process: the batches, the exceptions, the convention notes and the Wikilink Review Activity. That record is [KI-PRINCIPAL-OPS-014](<../../../../Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md>).

## Open

- **TOUCH-SCOPE** is open. Kris asked whether a full conversion makes it unnecessary. It narrows the question rather than removing it: once ki-principal is converted, a touched file has nothing left to convert there, but `+/` working areas convert on touch only and every other island stays mixed until its owner converts it. The recommendation stands at medium confidence: convert the whole authored file on touch, through the converter's preflight, escalating an unsafe file or recording an approved exception; define protected and generated-file handling before the rule is enabled. A whole-file touch rule is never an implicit estate-wide write grant.

## Owners and order

1. **Harness rules** - ki-agentic-harness (gfm-harness run). The `ki-authoring` "Markdown flavour" clause; the `ki-repo-kb` linking standard rewritten so GFM is preferred and wikilinks tolerated; LINK-1 replaced by exact-case resolution of every internal link in both forms, with fragments; the consumer parser fixes below; the three evals and the source-mirror stripper. This lands first: until it does, the standard still mandates wikilinks.
2. **Converter** - tools-ki, under its `ki-self` boundaries, as an operation hosted by `ki repo conform --skill ki-authoring` or its own `ki` command. Handed to `ki.tools-burndown` with the [requirements below](#converter-requirements).
3. **ki-principal conversion** - ki-principal, under [KI-PRINCIPAL-OPS-014](<../../../../Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md>), blocked by 1 and 2.
4. **Other islands** - each island's owner, when they choose ([Other islands](#other-islands)).

## Prerequisites

The review accepted the staged plan with these additions. None of them is optional.

- **Consumer fixes before any conversion.** The `ki-decision-records` rubric's body-link parser fails open on angle-bracket destinations containing spaces and truncates reference-definition destinations. The `ki-repo-kb-activities` parser reads both syntax families but does not decode percent-encoded spaces, so encoded links fail filename coverage. Both need fixtures for angle-bracket and encoded destinations, reference definitions and escaped table aliases. A global percent-decoding rewrite is unsafe for reserved characters and literal percent signs.
- **Per-batch exception decisions.** Before a batch writes, its owner decides each construct the converter cannot carry without loss:
  - the four image embeds sized to width 800 (two in `Influences Along the Way`, one in `What is Knowledge Islands`, one in `What is Knowledge`), which the Format note's image-width convention requires; choose a supported replacement or an approved exception, never sizing turned into alt text, and check the three SVG embeds against each reader's restrictions;
  - the 10 heading links: the Observatory discards the fragment, and GitHub slugs differ from Obsidian heading text; test self-links, cross-note headings, duplicate headings and Unicode anchors in each real client;
  - the two custom `[!todo]` callouts in the Structure note, used as definition headings for Port and Routes, whose definition text must survive;
  - the two Dataview blocks in the Wikilink Review Activity, which are already inert because Dataview is not installed;
  - the Obsidian templates (20 tracked Markdown files under `Pillars/Philosophy/Model/Tools/Obsidian/Templates/`, including the index; the scoping report's 21 is to be reconciled) and their dynamic link destinations.
- **Per-link verification, not totals.** For each link, compare old and new target identity, fragment, label, image asset and display properties. Equal link counts, rendered text or graph-edge totals can hide a wrong destination.
- **Reviewed paths against unchanged bytes.** Apply only the reviewed paths, against the same input bytes the preview was made from; abort on a concurrent edit or a newly ambiguous destination.
- **Rollback manifest.** Each batch records the exact paths and pre-images it changed, so it can be reversed exactly; commits are by explicit path.
- **Enactment preview checkpoint.** The Enactment Process requires a concrete preview for a complex or destructive rollout: each batch's dry-run output is the preview Kris reviews before it is applied, and the intended-versus-executed artefact for the post-change review.
- **Resolver universe re-inventoried at the pilot.** The scoping counts are not authority. The resolver's candidate universe and precedence are defined first, actual destinations snapshotted, and the inventory re-run at the pilot. The review reproduced 29 unresolved candidates (11 in `+/`, 14 dynamic template destinations, 4 in Streams) and found five, not seven, multi-candidate occurrences once exact and source-relative matches take precedence.

## Converter requirements

What tools-ki is asked to build. The acceptance is tools-ki's; these are the needs.

1. **Resolver in Obsidian's order** - beside the note, then full path, then a unique leaf name, case-insensitive - emitting the exact on-disk case, because GitHub is case-sensitive and macOS is not. Its candidate universe and precedence are declared and testable.
2. **Output form** - document-relative destinations, in angle brackets when the path holds a space; GFM image syntax for embeds; heading fragments as decided per batch; Obsidian's `%20` spelling normalised structurally, with needed URI escapes kept.
3. **Mechanical constructs only** - plain and aliased wikilinks (including those escaped with `\|` in table cells) and unsized image embeds. Everything else - sized embeds, heading links unless the batch decided their form, custom callouts, Dataview, block references, transclusions, front-matter links, dynamic template destinations, ambiguous or unresolved targets - is left untouched and listed.
4. **Dry run** - `--dry-run` gives a per-file diff and a report of ambiguous, unresolved and judgement items; that output is the Enactment preview.
5. **Path scope** - takes explicit paths, so it converts one batch or a single touched file; never the whole repository by default.
6. **Fail-closed preflight** - refuses a file containing an undecided judgement item, protected or generated material, or a destination that became ambiguous since the preview, rather than converting part of it silently.
7. **Unchanged-bytes guard** - applies only when each input file's bytes match the reviewed preview; aborts the whole batch otherwise.
8. **Per-link verification** - for every converted link, old and new target identity, fragment, label and image asset match; links resolve in exact case.
9. **Preservation** - YAML front matter, fenced and inline code, template expressions, list and table structure and authored prose are byte-identical outside the converted link spans.
10. **Idempotence and containment** - a second run changes nothing; no write lands outside the given paths.
11. **Rollback manifest** - writes the list of changed paths with their pre-images.
12. **No formatter mixed in** - syntax conversion only; rumdl conform runs as a separate following commit, because removing the `|` lets MD013 reflow paragraphs it has always skipped.
13. **Fixture tests** on the ki-principal shapes: aliases in tables, headings, embeds with and without size, spaces, case mismatches, templates, code examples and reference definitions.

## Batch order

All batches run under [KI-PRINCIPAL-OPS-014](<../../../../Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md>), each previewed, approved, applied and committed alone, then a separate formatter commit where needed.

1. **Pilot** - Resources, Calendar, root and the `-` area (about 23 links), including a GitHub render check of an alert with text on its marker line and of a heading link, and a check in Obsidian, Zed and the Observatory.
2. **Obsidian configuration** - `useMarkdownLinks: true` and `newLinkFormat: relative` in `.obsidian/app.json`, so Obsidian stops creating wikilinks.
3. **Streams** (about 218 links).
4. **Admin** (about 195 links and 1 embed).
5. **Pillars** (about 552 links and embeds), after the width-800 embed, heading-link and template decisions.
6. **Judgement pass** - the two `[!todo]` callouts, the Wikilink Review Activity and its Dataview blocks, the heading links, the ambiguous links and the templates, as far as earlier batches did not settle them.
7. **Convention notes** that prescribe wikilinks: root `AGENTS.md`, the Charter, Structure, Format, Notes, the Obsidian tool note and the Tending activities, rewritten to the GFM preference.

`+/` working areas convert on touch only, and `+/_Voice Notes/` is never touched. The 337 machine-local absolute `/Users/` links in `+/_WORK` are a separate coordination question, not part of this conversion. Counts are from the scoping run and are re-inventoried at the pilot.

## Other islands

Each island owns its own conversion and plans it when its owner chooses, with the tools-ki converter once it is released. The scoping run suggests smallest first: va-principal, er-principal (41 front-matter links), hnr-principal (callouts, inline tags, Dataview), personal-principal last (about 7,200 links, 635 unresolved, 362 ambiguous, 46 embeds). An island mirrored to Notion waits until mcp-ki-kb-notion-mirror reads Markdown-link edges; whether any island is mirrored was checked only against `.ki.toml`. State of play in each other capital has been told.

TOUCH-SCOPE decided 2026-10-19 22:32 BST, Kris: "agreed" - option a): once the converter exists, editing a file converts the whole file in the same change; a file the converter refuses is flagged or given a recorded exception. The `ki-authoring` clause already says so.
