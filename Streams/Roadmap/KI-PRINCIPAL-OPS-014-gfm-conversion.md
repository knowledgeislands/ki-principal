---
note_type: stream-roadmap
id: KI-PRINCIPAL-OPS-014
area: OPS
title: Convert ki-principal to GitHub-flavoured Markdown
kind: deliver
project: ways-of-working
component: model
priority: medium
size: l
status: done
tags:
  - topic/knowledge-islands
blocks: []
blocked_by: []
baseline_ref: 442c3501f53ee95fa8eb0ae9e7c6d493d3d31df1
created_at: 2026-10-19T21:04:00Z
updated_at: 2026-10-27T01:22:25Z
---

# Convert ki-principal to GitHub-flavoured Markdown

## Goal

Knowledge Islands Principal's authored Markdown is GitHub-flavoured (GFM): internal links are document-relative Markdown links, image embeds are Markdown images, and no convention note in the island prescribes wikilinks. Every converted link resolves to the same target as before, in exact case, and the island's link audit passes.

## Context

On 2026-10-19 Kris set the direction that Knowledge Islands prefers GFM, keeps other flavours supported, converts a file when it is touched, and may rewrite batches of files whole. At 22:00 BST the same day Kris answered the scoping and review queries with "Do all recommended": GFM-ORDER a) convert ki-principal outright in staged batches, each failing closed; FLAVOUR-FIELD a) no per-note flavour field; GFM-LINK-FORM a) document-relative paths in angle brackets, `%20` normalised, the audit failing dangling or wrong-case links; and GFM-ENACT a) one `Streams/Roadmap/` record for the whole ki-principal conversion. This is that record.

The decided plan, the review's prerequisites, the converter requirements and the batch order are in the [GFM migration design note](<../../+/_WORK/ki.ways-of-working/design/gfm-migration.md>) of the [Ways of working](<../Projects/ways-of-working.md>) Project. The scoping run counted 1,025 wikilinks, 10 heading links and 15 embeds in ki-principal, including `+/`; those counts are re-inventoried at the pilot and are not authority.

## Boundary

- ki-principal only. Each other island plans its own conversion when its owner chooses.
- Syntax conversion and the convention rewrites it requires; no other content change is mixed into a batch, and formatter changes land in a separate following commit.
- `+/` working areas convert on touch only; `+/_Voice Notes/` is never touched. The machine-local `/Users/` links in `+/_WORK` are a separate coordination question.
- No construct without a GFM equivalent is dropped silently; each is decided before its batch writes.

## Scope

- **Batches**, in order, each previewed through the converter's dry run, approved, applied against unchanged bytes with a rollback manifest, and committed alone:
  1. Pilot: Resources, Calendar, root and the `-` area, with a render check of an alert and a heading link on GitHub, in Obsidian, in Zed and in the Observatory.
  2. Obsidian configuration: `useMarkdownLinks: true` and `newLinkFormat: relative` in `.obsidian/app.json`.
  3. Streams.
  4. Admin.
  5. Pillars.
- **Exceptions**, decided per batch before it writes:
  - the four image embeds sized to width 800 (two in `Influences Along the Way`, one in `What is Knowledge Islands`, one in `What is Knowledge`), and the three SVG embeds;
  - the 10 heading links, whose fragments the Observatory drops and whose GitHub slugs differ from Obsidian heading text;
  - the two custom `[!todo]` callouts in the Structure note, whose definition text must survive;
  - the Obsidian templates under `Pillars/Philosophy/Model/Tools/Obsidian/Templates/` and their dynamic destinations;
  - ambiguous and unresolved destinations found at the pilot's re-inventory.
- **Convention notes** that prescribe wikilinks, rewritten to the GFM preference: root `AGENTS.md`, the Charter, Structure, Format, Notes, the Obsidian tool note and the Tending activities.
- **Wikilink Review Activity** (`Pillars/Philosophy/Model/Activities/Tending/Wikilink Review.md`, renamed Link Review on 2026-10-20) and its two inert Dataview blocks: rewritten as a link review over both forms, or retired, as decided in the judgement pass.

## Acceptance tests

1. Every converted link's target identity, fragment, label and image asset match its pre-image, by per-link comparison, not totals.
2. Every internal link in the converted paths resolves in exact case under the harness link audit, and `ki repo audit` is clean apart from recorded pre-existing findings.
3. Front matter, code, template expressions, tables and prose are byte-identical outside the converted link spans; a second converter run changes nothing.
4. The pilot's GitHub, Obsidian, Zed and Observatory checks pass, or each failure has a recorded decision.
5. No convention note outside `+/` prescribes wikilinks.

## Current state

Before the conversion the island held about 1,050 wikilinks, heading links and embeds outside `+/_Voice Notes/`, and the convention notes prescribed wikilinks. `ki` v0.12.0 carries the converter (`ki markdown gfm`) and the LINK-1 audit that resolves both forms in exact case, with fragments.

## Steps

- [x] Pin `.github/ki-version` to v0.12.0.
- [x] Pilot: Resources, Calendar, root and the `-` area, previewed, applied with a rollback manifest and committed alone.
- [x] Obsidian configuration: `useMarkdownLinks: true` and `newLinkFormat: relative`.
- [x] Streams, Admin and Pillars, each previewed, decided, applied and committed alone.
- [x] Judgement pass: the listed items decided or kept for the owner; the Wikilink Review Activity rewritten over both forms.
- [x] Convention notes rewritten to the GFM preference.
- [x] Tracked, unmodified `+/_WORK/` files, last, in one batch.
- [x] Owner answers applied (2026-10-20): the four sized embeds as plain images, the template placeholders as links, the Activity renamed Link Review.
- [x] Client render checks on GitHub, Obsidian, Zed and the Observatory, by Kris before acceptance: closed by his acceptance of 27 October 2026, with no outcome recorded per client.

## Files touched

`.github/ki-version`, `.obsidian/app.json`, this record, and the Markdown files the batch commits name: 8 in the pilot, 34 in Streams, 51 in Admin, 91 in Pillars, 17 convention notes and 12 in `+/_WORK/`.

## Verify

Per batch: `ki markdown gfm --dry-run` with the batch's decisions shows 0 undecided; the apply matches the preview; a second dry run changes nothing; every relative Markdown link in the changed files resolves in exact case; `ki repo audit` shows no new finding against the baseline taken before the pilot; the pre-commit gate passes on the staged paths.

## Dependencies / blocks

- **Harness rules** (ki-agentic-harness): the `ki-authoring` GFM preference clause, the `ki-repo-kb` linking standard rewritten so GFM is preferred and wikilinks tolerated, the link audit replaced by exact-case resolution of both forms with fragments, and the Decision Record and Activities parser fixes. Blocking: until they land, the standard still mandates wikilinks and a converted island has no link check.
- **Converter** (tools-ki): the path-scoped, fail-closed converter with dry run, unchanged-bytes guard, per-link verification and rollback manifest that the design note specifies. Blocking: the batches are not hand-converted.
- Nothing in this repository blocks the record; `blocked_by` is empty because both blockers are in other repositories.

## Documentation impact

### Decision Records

None: the direction and link form were decided on 2026-10-19 (GFM-ORDER, GFM-LINK-FORM, TOUCH-SCOPE) and are carried by the `ki-authoring` and `ki-repo-kb` standards.

### Specifications

None: no behaviour-level contract changes in this repository.

### Guides

The Format note now prescribes document-relative Markdown links; the Enactment Process footer template, AGENTS.md, Notes, Structure, Calendar, the Obsidian notes and the Tending activities stop prescribing wikilinks.

### Roadmap

None: no follow-on record is created (CAPTURE-GATE); the open exceptions below go to the owner as queries.

## Review

### Delivered

The whole of ki-principal outside `+/_Voice Notes/` and other sessions' uncommitted files, from baseline `442c3501f53ee95fa8eb0ae9e7c6d493d3d31df1`: 23 links in the pilot, 234 in Streams, 199 and one SVG embed in Admin, 534 in Pillars and 54 in `+/_WORK/`, with Obsidian set to create relative Markdown links and the convention notes rewritten.

### Change Summary

- Commits: `17d96936` pin and adoption; `25007312` pilot; `df620255` Obsidian; `e21e7346` Streams; `dbbfabcf` two pruned report links pinned to their last revision; `64c046c2` Admin; `554bcd8e` Pillars; `d64f0abc` convention notes; `f65c4fac` `+/_WORK/`, which also pins the pruned KI-PRINCIPAL-ECO-012 link.
- Heading links take GitHub slugs (`heading_fragments = "github"`).
- Dead links whose target was clear were decided to their current home: the ambiguous `Themes` links to `Streams/Themes/Themes.md`; `command-centre` to the Observatory Project it became; Initiatives `rig`, `techne` and `knowledge-islands-model` to their theme pages; `Techne Programme Hold` and the old GDR-KI-PRINCIPAL-004 name to their renamed files; old checkpoints to their work packages.
- Kept for the owner: the four width-800 image embeds, the Wikilink Review orphan Dataview block, the two custom `[!todo]` callouts in Structure (unchanged, text intact) and the 14 placeholders in the yearly and location templates.
- The Wikilink Review Activity's broken-link view now points to the LINK-1 audit instead of a wikilink-only Dataview query.
- Owner answers of 2026-10-20, applied in one following commit: SIZED-EMBEDS a) the four width-800 embeds are plain Markdown images with descriptive alt text and note-relative destinations, and the Format note no longer mandates a width; TEMPLATE-LINKS a) the 14 placeholders in the yearly and location templates are GFM links to the month folders' notes and sibling landmark notes, deliberately unresolved until a note is instantiated; LINK-REVIEW-NAME a) the Activity is now [Link Review](<../../Pillars/Philosophy/Model/Activities/Tending/Link Review.md>), trigger _"ki link review"_, with the Charter, Tending, What Keeps an Island Alive, Knowledge Islands and Agents notes updated together; no local consumer of the old trigger was found in the harness, `tools-ki`, the Observatory, KI Specifications or chezmoi, and external consumers were not checked.

### Verification

- Each batch: 0 undecided at apply, apply matched its preview, a second dry run changed nothing.
- Exact-case resolution of every relative Markdown link in the changed files: 0 unresolved, apart from two pre-existing dead report links in Streams, since pinned.
- `ki repo audit`: no new finding against the pre-pilot baseline in any batch; LINK-1 now lists only pre-existing absolute `/Users/` links, one cross-repository harness link and the template placeholders.
- Pre-commit gate passed on every commit; the `+/_WORK/` commits ran it with the released `ki` 0.12.0 because the local `ki` source was mid-edit by another session.

### Outstanding concerns

- Acceptance test 4 is unchecked and is Kris's to run before acceptance (RENDER-CHECK a), 2026-10-20): open the Library heading link and a representative alert in each of GitHub, Obsidian, Zed and the Observatory, check the four plain images read well at natural size, record each outcome here, and decide each failure explicitly. The Observatory's dropped heading fragment is to be recorded as a navigation failure or expressly accepted as a fallback.
- Acceptance test 5 is met for links and images since the 2026-10-20 answers: the Format note prescribes plain Markdown images.
- The four width-800 embeds, the template placeholders and the Activity name were answered on 2026-10-20; the `[!todo]` callouts stay unchanged, text intact.
- Front-matter wikilinks (`creator: "[[Author Name]]"` in Properties and Structural Audit) are Obsidian properties, outside the converter's scope, and are left as they are.
- `MD-mech` and the `ki-decision-records` BODY-11 findings are pre-existing.

### Post-change review

The goal is met for every mechanical construct: internal links are document-relative Markdown links that resolve in exact case, and no convention note prescribes wikilinks for links. Regression risk is low: every write went through the converter's unchanged-bytes guard and per-link check, and each batch can be reversed from its manifest or its commit. Ready for acceptance once Kris has run the four client render checks and decided any failure.

### Mini recap

ki-principal is GitHub-flavoured in nine commits; checks clean against baseline; four exception groups and the client render checks are with Kris. Learning route: `ki` hooks that run from a live source checkout break when another session edits tools-ki; the released binary was the stable path.

## Done

Accepted 2026-10-27 by Kris Brown on the review packet above, under SWEEP-ACCEPT and his instruction of 27 October 2026 at 01:15 GMT, read back in the [ways-of-working decisions log](../../+/_WORK/ki.ways-of-working/decisions.md), entry "2026-10-27 01:15 GMT". Closed under `ki-accept` by the wow-accept-prune run.

## Discussion

- On 27 October 2026 Kris accepted the record under SWEEP-ACCEPT with the client render checks (acceptance test 4) still his own and unrecorded; his acceptance closes that step, and any render defect found later is new work.
- TOUCH-SCOPE was decided on 2026-10-19 at 22:32 BST, option a): editing a file converts the whole file in the same change. Before that it was open: whether touching a file converts the whole file. Converting ki-principal in full narrows it to `+/` and to other islands, but does not remove it.
- The Enactment Process's preview checkpoint is each batch's dry-run output, reviewed by Kris before it is applied and kept as the intended-versus-executed artefact for the post-change review.
- Size is provisional and revisited before the record becomes Ready; the batches may be split into their own records if a batch grows beyond one reviewable change.
- On 2026-10-20 Kris authorised the pilot and the remaining batches straight through while other threads were paused (PRINCIPAL-TRIAGE), so each batch's dry-run output was reviewed by this run rather than by Kris before apply; the previews are the intended-versus-executed artefact for the post-change review.

## Governance

This roadmap record adheres to the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>). Move content to `Admin/`, `Pillars/`, or `Resources/` only on user approval of a `ready` record.
