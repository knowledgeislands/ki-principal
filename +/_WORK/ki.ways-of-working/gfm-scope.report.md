# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › gfm-scope

**🤖 → 👤 Handoff to supervisor · Run report at 21:36 BST · last mark 21:25 BST**

---

## Done

- Read-only scoping for GFM-MIGRATION is finished. No repository was edited and nothing was committed. The inventory script and its JSON output are in the run's temporary folder only.
- Read the `ki-authoring` skill (SKILL, `standards-markdown`, `exemplars`, `sources`, rubric), the `ki-repo-kb` linking standard and LINK-1, ki-principal `AGENTS.md`, `.ki.toml`, `.rumdl.toml`, `.obsidian/` and the Structure note. Also traced the 2026-10-09 flavour idea to ki-principal commit `18d9d4d3`.
- Inventoried ki-principal and sampled er-principal, hnr-principal, personal-principal and va-principal. The findings and the feasibility table are below.
- Surveyed every link parser in tools-ki, the harness, the Observatory, mcp-ki-kb-fs and mcp-ki-kb-notion-mirror. The breakages are listed below.

### Where Obsidian syntax is required today

- **`ki-repo-kb`**, under "Linking within a base" and rubric LINK-1, _requires_ shortest-unique `[[wikilinks]]` in base note content. Its `## Contents` lists must use `[[Full/Path|Name]]`. This mandate is what must change. `ki-authoring` defers to it, and the Links section of its `standards-markdown` names KB notes as an exception.
- **ki-principal** names wikilinks as the convention in 18 canonical notes outside `+/`: `AGENTS.md`, the Charter, Structure, Format, Notes, the Obsidian tool note and its 21 templates, and the Tending activities. One of those activities, Wikilink Review, is built on Dataview.
- **ki-principal's own `.rumdl.toml`** already runs rumdl's _standard_ (GFM) flavour, and its comment says the repository "forbids wikilinks". The linter and the KB standard contradict each other today. One side effect: MD013 silently skips every paragraph containing an aliased wikilink, so those paragraphs are never reflowed.
- **`.obsidian/app.json`** sets `newLinkFormat: shortest` and leaves `useMarkdownLinks` off. Every link Obsidian creates is therefore a wikilink. The only community plugin that touches syntax is `callout-manager`, and Dataview is _not_ installed, so the two Dataview blocks already render as plain code.

### Inventory (tracked Markdown, code excluded)

| Construct | ki-principal | er | hnr | personal | va |
| --- | --- | --- | --- | --- | --- |
| Markdown files | 362 | 299 | 736 | 1,503 | 45 |
| Wikilinks, plain | 537 | 651 | 1,340 | 3,598 | 16 |
| Wikilinks, aliased | 488 † | 22 | 402 | 3,542 | 27 |
| Wikilinks, heading target | 10 | 1 | 13 | 21 | 0 |
| Wikilinks, block target | 0 | 0 | 0 | 0 | 0 |
| Embeds | 15 ‡ | 0 | 1 | 46 | 0 |
| Callouts, GFM-compatible / custom | 0 / 2 § | 0 / 0 | 17 / 6 | 1 / 14 | 0 / 0 |
| Highlights, comments, block IDs | 0 | 0 | 0 | 0 | 0 |
| Inline `#tags` | 0 | 0 | 322 ¶ | 26 | 0 |
| Dataview blocks / `.base` files | 2 / 0 | 0 / 0 | 5 / 0 | 5 / 1 | 0 / 0 |
| Wikilinks in front matter | 0 | 41 | 26 | 14 | 0 |
| Links to a path with spaces | 441 | 586 | 1,369 | 3,958 | 13 |
| Ambiguous / unresolved targets | 7 / 29 ‖ | 0 / 0 | 45 / 224 | 362 / 635 | 1 / 5 |
| Relative Markdown links already | 512 | 13 | 1,080 | 553 | 16 |

† Of these, 21 sit in table cells with an escaped `\|`. Conversion removes that table hazard.

‡ 12 PNG and 3 SVG image embeds, including `![[Release Cascade.svg]]`. There are no note transclusions.

§ Both are `[!todo]`, in Structure, used as definition headings for Port and Routes.

¶ A regex count and not reviewed. Some may be issue numbers or anchors. It is given for scale only.

‖ Ambiguous: 6 are `[[Themes]]`, which collides with a `+/_WORK/ki/design/themes` note, and 1 is `Diagrams/Diagrams`. Unresolved: almost all are in `+/_WORK` design notes, plus 1 placeholder in a template.

By zone, ki-principal's wikilinks are: Pillars 539 plus 13 embeds; Streams 218; Admin 195 plus 1 embed; `+` 60; root 12; `-` 4; Resources 4; Calendar 3. Separately, `+/_WORK` holds 337 machine-local absolute links (`/Users/...`). These come from the coordination conventions, not from Obsidian, and they do not resolve on GitHub either.

### Feasibility

| Construct | GFM equivalent | Conversion | What breaks or changes |
| --- | --- | --- | --- |
| Plain wikilink | `[Note](<rel/path/Note.md>)` | Mechanical with resolver † | Path text changes when a linking file moves outside Obsidian ‡ |
| Aliased wikilink | `[Alias](<rel/path/Note.md>)` | Mechanical | Nothing; table `\|` escaping goes away |
| Heading wikilink | `[Note › Heading](<path.md#gfm-slug>)` | Mechanical but lossy | Obsidian may not follow a GitHub slug § |
| Block wikilink, block ID | No GFM equivalent | Judgement | None present anywhere sampled |
| Image embed | `![alt](<image.png>)` | Mechanical; alt text is judgement | Obsidian embed sizing (`\|300`) is lost; none found |
| Note transclusion | Link, or inline the text | Judgement | None in ki-principal; check personal before converting it |
| GFM-type callout | `> [!NOTE]` and the other four | Already GFM | Text on the marker line becomes an Obsidian title ¶ |
| Custom callout | GFM alert, heading or prose | Judgement | `callout-manager` styling |
| Highlight, comment | `<mark>`, `<!-- -->` | Mechanical | None present |
| Inline tag | Front-matter `tags` | Judgement | Obsidian tag pane; hnr only |
| Dataview, `.base` | Static list, generated note or removal | Judgement | Wikilink Review Activity already inert |
| Front-matter wikilink | Path string | Judgement | Obsidian link-typed property loses its link; none in ki-principal |

† The resolver must follow Obsidian's order (beside the note, then full path, then a unique leaf name, case-insensitive) and emit the exact on-disk case. GitHub is case-sensitive and macOS is not.

‡ Obsidian rewrites Markdown links on rename (`alwaysUpdateLinks` is on). A `git mv` does not, so a link-existence check must replace LINK-1.

§ GitHub anchors are slugs (`#my-heading`), while Obsidian Markdown links use the heading text. There are only 10 such links in ki-principal, so behaviour should be confirmed in the pilot.

¶ The house example `> [!NOTE] Message` deserves a GitHub render check in the pilot. On GitHub I believe the marker must stand alone on its line. That is not verified, because this run made no network calls.

### What breaks in tools and surfaces

- **`ki repo audit` (harness `ki-repo-kb`, LINK-1, `kb.ts`)** checks only that wikilinks are unambiguous. A converted island passes vacuously but has no link check at all. LINK-1 needs replacing with "every internal link resolves, in exact case". House `.rumdl.toml` also disables MD057 (relative-link existence), so nothing else catches dangling links.
- **Harness `ki-decision-records` rubric (`decision-records.ts`, `bodyLinks`)** parses `[x](<a b.md>)` as `a`, because its pattern stops at the first space. This is a real defect for angle-bracket links, which is the form the house standard prescribes.
- **Harness `ki-repo-kb-activities` rubric** already parses both forms, angle brackets included. No change is needed.
- **The Observatory (`packages/evidence/src/knowledge-bases.ts`)** already resolves wikilinks, embeds and relative Markdown links through `marked` with GFM and `decodeURI`. No change is needed, apart from checking that the graph edge count is the same before and after conversion.
- **mcp-ki-kb-notion-mirror** builds backlinks and @mentions from wikilinks only (`wikilinks.ts`, `backlinks/graph.ts`). A converted island that is mirrored to Notion would lose its edges. No island's `.ki.toml` declares a mirror, and I did not check the mirror's own root configuration.
- **tools-ki and mcp-ki-kb-fs** parse no wikilinks. `ki-repo-kb`'s source-mirror script strips wikilinks and should also strip Markdown links, though this is minor.
- **Obsidian** keeps working: it renders, links, shows backlinks and graphs relative Markdown links. To stop it re-introducing wikilinks, set `useMarkdownLinks: true` and `newLinkFormat: relative`. Obsidian writes `%20` rather than angle brackets, which the converter or `ki repo conform` should normalise.
- **Generated surfaces**: the 21 Obsidian templates and the `ki-repo-kb` asset templates emit wikilinks. The latter hold none today. Harness evals for `ki-authoring`, `ki-skills` and `ki-subagents` test the old KB exception and need rewording.

### Draft `ki-authoring` clause

This would sit in `standards-markdown.md` under "Markdown flavour", with the KB exception removed from "Links" and "Linking within a base" in `ki-repo-kb` rewritten to match:

> **Markdown flavour.** Knowledge Islands prefers GitHub-flavoured Markdown (GFM): it renders the same on GitHub, in editors such as Zed, in the Observatory and in Obsidian. Other flavours, chiefly Obsidian's wikilinks, embeds and custom callouts, remain supported: a reader, audit or tool must not fail on them, and no one need convert a file just to read or cite it. A file you touch is converted: when you edit a Markdown file for any reason, convert its whole body to GFM in the same change, using relative links in angle brackets (`[Note](<../Folder/Note.md>)`) and GFM alerts, and keep the conversion visible in the change. From time to time a repository may rewrite a batch of files, or the whole repository, to GFM in one dedicated change, through the converter's dry run and its verification, with no other edits mixed in. Where a construct has no GFM equivalent (a block reference, a transclusion, a plugin query), the author decides the replacement; it is never dropped silently.

**The 2026-10-09 front-matter flavour field** is no longer needed. Kris's touch-to-convert rule, together with batch rewrites, replaces gradual per-note declaration. A file's flavour can be detected mechanically from the presence of `[[`, `![[` or a custom callout, so a declared field would only duplicate that and drift from it. If any island must stay on Obsidian flavour long term, a repository-level `.ki.toml` key is enough. See FLAVOUR-FIELD below.

### Recommended plan

1. **Harness rules** (owner: ki-agentic-harness). Add the clause to `ki-authoring`. Rewrite the `ki-repo-kb` linking standard so GFM is preferred and wikilinks are tolerated. Replace LINK-1 with internal-link resolution in exact case, covering both forms. Fix the `ki-decision-records` `bodyLinks` space defect. Update the three evals and the source-mirror stripper. This must land first, because otherwise the standard still mandates wikilinks.
2. **Converter** (owner: tools-ki, under its `ki-self` boundaries, as an operation hosted by `ki repo conform --skill ki-authoring` or as its own `ki` command). It should provide:
   - an Obsidian-order resolver;
   - `--dry-run`, giving a per-file diff plus a report of ambiguous, unresolved and judgement items;
   - paths to scope a batch or a single touched file;
   - mechanical constructs only, leaving judgement items untouched and listed. It needs fixture tests on the ki-principal shapes: aliases in tables, headings, embeds, spaces, case and templates.
3. **Verification**, built into the converter and run in each batch:
   - the link count is the same per file before and after;
   - the visible rendered text is identical once link markup is stripped;
   - every link resolves in exact case;
   - `ki repo audit` is clean;
   - the Observatory edge count is the same;
   - an Obsidian spot-check of backlinks and the graph. rumdl conform runs as a separate following commit, because removing the `|` will let MD013 reflow paragraphs it has always skipped.
4. **ki-principal batches** (owner: ki-principal):
   - a pilot on Resources, Calendar, root and the `-` area (23 links), including a GitHub render check of an alert and a heading link;
   - Obsidian configuration (`useMarkdownLinks`, `newLinkFormat: relative`);
   - Streams (218);
   - Admin (196);
   - Pillars (552);
   - the judgement pass: the 2 `[!todo]` callouts, the Wikilink Review Activity and its Dataview blocks, the 10 heading links, the 7 ambiguous links and the 21 templates;
   - the convention notes that prescribe wikilinks (`AGENTS.md`, the Charter, Structure, Format, Notes, Obsidian, Tending).

   `+/` working areas convert on touch only. `+/_Voice Notes/` is never touched. The 337 absolute `/Users/` links in `+/_WORK` are a separate coordination question.
5. **Enactment** (ki-principal): a single `Streams/Roadmap/` record should cover everything. The mechanical batches change no meaning but are not trivial in scale. The convention-note and Activity rewrites are substantive changes to Pillars and Admin and need the record regardless.
6. **Other islands** (each island owns its own conversion). They follow the same converter when their owner chooses, smallest first: va-principal, er-principal (41 front-matter links), hnr-principal (callouts, tags, Dataview), and personal-principal last (about 7,200 links, 635 unresolved, 362 ambiguous, 46 embeds). Before converting any island mirrored to Notion, mcp-ki-kb-notion-mirror must learn Markdown-link edges.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The confidences below are my own. Under DESIGN-REVIEW practice, the coordinator's blind review has not yet run on them.
- Whether any island is mirrored to Notion was not checked beyond `.ki.toml`.
- The GitHub alert render and the Obsidian heading-slug behaviour are unverified, because no network calls were made. The pilot settles both.
- The hnr-principal inline-tag count is unreviewed.

## Queries

### GFM-ORDER - convert ki-principal outright or by touch only

**Context:** Every ki-principal construct except 2 callouts, 2 Dataview blocks, 10 heading links, 7 ambiguous links and the templates converts mechanically: 1,025 wikilinks and 15 embeds. Kris leans to "just do it". Doing it outright needs the harness rule change and a tools-ki converter first. Touch-only converts nothing until files are edited, which leaves the island mixed for months.

**Query:** Should ki-principal be converted outright, in zone batches, once the rule change and converter land?

**Options:**

a) (recommended, confidence medium - the inventory shows the work is mechanical, but the converter does not yet exist and the pilot has not run) Land the harness rules and the tools-ki converter, pilot on the 23 links in Resources, Calendar, root and `-`, then batch Streams, Admin and Pillars, followed by the judgement pass and the convention notes.

b) Adopt the clause now and convert on touch only, with no batches until a later decision.

c) Convert ki-principal by hand now in batches, without building a converter, and leave the other islands until one exists.

### FLAVOUR-FIELD - drop the 2026-10-09 front-matter flavour field

**Context:** On 2026-10-09 the idea was a per-note front-matter field declaring flavour, so the standard could change gradually. Touch-to-convert plus batch rewrites now does that job, and flavour is detectable mechanically. A long-term Obsidian-flavour island could instead declare it once in `.ki.toml`.

**Query:** Should the per-note flavour field be dropped?

**Options:**

a) (recommended, confidence high - detection is mechanical and a declared field would duplicate it and drift) Drop it. Add a repository-level `[skills.ki-authoring]` flavour key only if an island opts to stay Obsidian-flavoured.

b) Keep the per-note field as the marker of a converted note during the transition.

### GFM-LINK-FORM - relative angle-bracket paths as the house link form

**Context:** Only document-relative paths resolve the same on GitHub, Zed, the Observatory and Obsidian. Root-relative `/Admin/...` links work on GitHub but not in Obsidian, and Obsidian's "absolute in vault" form breaks on GitHub. The house standard already prescribes angle brackets for paths with spaces, and 441 ki-principal links point at such paths. Obsidian itself writes `%20`. Relative paths change when the linking file moves outside Obsidian, so a resolution audit becomes essential.

**Query:** Should the house link form for KB notes be document-relative paths in angle brackets?

**Options:**

a) (recommended, confidence medium - this is the only form all four readers resolve, but the cost when files move rests on a new audit) Use document-relative paths in angle brackets, have `ki repo conform` normalise Obsidian's `%20` form, and have the new LINK check fail on any dangling or wrong-case link.

b) Use document-relative paths with `%20` encoding, which matches what Obsidian writes, at the cost of less readable source.

### GFM-ENACT - one Enactment record for the ki-principal conversion

**Context:** The mechanical batches change link syntax across Admin and Pillars but not meaning. The convention notes (`AGENTS.md`, the Charter, Structure, Format, Notes, Obsidian, Tending) and the Wikilink Review Activity need substantive rewording. Under ki-principal's rules, related changes share one record, and Kris's explicit instruction can stand in only for a bounded change.

**Query:** Should a single Roadmap record carry the whole ki-principal conversion through the Enactment Process?

**Options:**

a) (recommended, confidence medium - the scale makes the formatting exemption a stretch, and the convention rewrites need a record in any case) Open one `Streams/Roadmap/` record covering the batches, the judgement pass and the convention notes.

b) Treat the mechanical batches as exempt formatting and open a record only for the convention notes and the Activity.

### TOUCH-SCOPE - what "touch" converts

**Context:** "If you touch a file, it changes" could mean converting the whole file whenever it is edited, or converting only the lines edited. Whole-file conversion keeps each file single-flavour and is mechanical through the converter. It does add link churn to unrelated diffs, which makes them noisier to review.

**Query:** Does touching a file convert the whole file?

**Options:**

a) (recommended, confidence high - single-flavour files are what make the audit and the Obsidian settings coherent) Convert the whole file, using the converter on that path, in the same change.

b) Convert only the edited lines and leave the rest for a batch.

### 🤖 → 👤 Handoff to supervisor · since 21:36 BST

👤 5 with you

- [with you] GFM-ORDER · owner · since 21:36
- [with you] FLAVOUR-FIELD · owner · since 21:36
- [with you] GFM-LINK-FORM · owner · since 21:36
- [with you] GFM-ENACT · owner · since 21:36
- [with you] TOUCH-SCOPE · owner · since 21:36
