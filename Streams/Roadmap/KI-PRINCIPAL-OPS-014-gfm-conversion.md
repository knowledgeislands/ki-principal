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
status: triage
tags:
  - topic/knowledge-islands
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-10-19T21:04:00Z
updated_at: 2026-10-19T21:04:00Z
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
- **Wikilink Review Activity** (`Pillars/Philosophy/Model/Activities/Tending/Wikilink Review.md`) and its two inert Dataview blocks: rewritten as a link review over both forms, or retired, as decided in the judgement pass.

## Acceptance tests

1. Every converted link's target identity, fragment, label and image asset match its pre-image, by per-link comparison, not totals.
2. Every internal link in the converted paths resolves in exact case under the harness link audit, and `ki repo audit` is clean apart from recorded pre-existing findings.
3. Front matter, code, template expressions, tables and prose are byte-identical outside the converted link spans; a second converter run changes nothing.
4. The pilot's GitHub, Obsidian, Zed and Observatory checks pass, or each failure has a recorded decision.
5. No convention note outside `+/` prescribes wikilinks.

## Dependencies / blocks

- **Harness rules** (ki-agentic-harness): the `ki-authoring` GFM preference clause, the `ki-repo-kb` linking standard rewritten so GFM is preferred and wikilinks tolerated, the link audit replaced by exact-case resolution of both forms with fragments, and the Decision Record and Activities parser fixes. Blocking: until they land, the standard still mandates wikilinks and a converted island has no link check.
- **Converter** (tools-ki): the path-scoped, fail-closed converter with dry run, unchanged-bytes guard, per-link verification and rollback manifest that the design note specifies. Blocking: the batches are not hand-converted.
- Nothing in this repository blocks the record; `blocked_by` is empty because both blockers are in other repositories.

## Discussion

- TOUCH-SCOPE is open: whether touching a file converts the whole file. Converting ki-principal in full narrows it to `+/` and to other islands, but does not remove it.
- The Enactment Process's preview checkpoint is each batch's dry-run output, reviewed by Kris before it is applied and kept as the intended-versus-executed artefact for the post-change review.
- Size is provisional and revisited before the record becomes Ready; the batches may be split into their own records if a batch grows beyond one reviewable change.

## Governance

This roadmap record adheres to the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>). Move content to `Admin/`, `Pillars/`, or `Resources/` only on user approval of a `ready` record.
