# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › gfm-convert

**🤖 → 👤 Handoff to supervisor · Run report at 03:51 BST · last mark 03:08 BST**

---

## Done

- `.github/ki-version` pinned to v0.12.0, and [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) adopted into Now (`17d96936`).
- Pilot: Resources, Calendar, the root files and the `-` area, 23 links, with the one heading link given its GitHub slug (`25007312`). Checks: re-run made no changes, 0 unresolved links in exact case, no new audit findings, LINK-1 clean for these paths.
- Obsidian now creates relative Markdown links (`useMarkdownLinks`, `newLinkFormat: relative`) (`df620255`).
- Streams: 234 links in 34 files (`e21e7346`). Nine ambiguous or dead links had clear targets: `Themes` now points to the Themes index, `command-centre` to the Observatory Project it became, and the pilot's design folder to its work-package home. Two older dead report links now point to their last revision on GitHub (`dbbfabcf`). Checks: re-run made no changes, 0 new unresolved links, no new audit findings.
- Admin: 199 links and one SVG embed in 51 files (`64c046c2`). Checks: re-run made no changes, 0 unresolved, no new audit findings.
- Pillars: 534 links and embeds in 91 files (`554bcd8e`). Checks: re-run made no changes, 0 unresolved, no new audit findings. Four kinds of item are kept for you to decide (Queries). The two custom `[!todo]` callouts in Structure are unchanged and their text is intact: GitHub shows them as plain quotes.
- Convention notes (`d64f0abc`). Format now prescribes links relative to the note, in angle brackets when the path has a space, and says wikilinks are still read. AGENTS.md, Notes, Structure, Calendar, the Obsidian notes, the Tending activities and the Enactment Process footer template no longer prescribe wikilinks. The Wikilink Review Activity now covers both link forms through the LINK-1 audit and keeps its orphan view. Check: the commit gate and rumdl passed.
- `+/_WORK/` last, in one batch: 54 links in 12 tracked files that no other session had changed (`f65c4fac`). Twelve dead links were followed through their renames to their current homes. The pruned KI-PRINCIPAL-ECO-012 link now points to its last revision. Checks: re-run made no changes, 0 unresolved, no new audit findings.
- KI-PRINCIPAL-OPS-014 moved to awaiting review, with its review packet (`30cb3da0`). Pushed fast-forward. main is level with origin.
- Limitation: the four clients' render checks (acceptance test 4) were not run, because this run cannot open GitHub, Obsidian, Zed or the Observatory.
- Correction: from `f65c4fac` on, the commit gate ran with the released Homebrew `ki` 0.12.0. The local `ki` runs from the tools-ki source, which another session is part-way through editing (Acquire Granola). Each time, that build crashed the gate.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Earlier problems the audit still reports, none caused by this run:
  - LINK-1 lists the absolute `/Users/` links, which the record treats as a separate coordination question.
  - LINK-1 lists one link to a file in the harness repository.
  - `MD-mech` and `ki-decision-records` BODY-11 failures.
  - Failures in other work packages.
- The front-matter wikilinks the Properties and Structural Audit notes prescribe (`creator: "[[Author Name]]"`) are Obsidian properties, which the converter does not handle. They are left as they are.
- Other sessions' uncommitted files are left untouched: `+/_WORK/ki.chezmoi/` decisions and queries, `+/_WORK/ki.ways-of-working/` decisions, queries and briefs, and the untracked reports.
- tools-ki has uncommitted Acquire edits that break the local `ki` source runner until they land.

## Queries

### SIZED-EMBEDS - Images sized to width 800

**Context:** Four Pillars images use Obsidian's sized embed `![[image.png|800]]`. Two are in Influences Along the Way, one in What is Knowledge Islands and one in What is Knowledge. The Format note still prescribes that form, so acceptance test 5 is only partly met. GFM has no size syntax. GitHub and Obsidian both already shrink a wide image to fit the column. An HTML `<img width="800">` renders on GitHub, but Obsidian may not resolve a relative path inside raw HTML.

**Query:** How should the four images, and the Format note's image rule, be written?

**Options:** a) (recommended, confidence medium - both main readers already fit images to the column, so the width adds little) Plain GFM images `![alt](<image.png>)`, and Format drops the width-800 rule. b) Keep the four as recorded Obsidian-only exceptions, and keep Format's sized-embed rule for images. c) HTML `<img src="image.png" width="800" alt="...">`, after a check that Obsidian renders it.

### TEMPLATE-LINKS - Placeholder links in two templates

**Context:** The yearly Calendar template has 12 month placeholders, such as `[[YYYY-01 January]]`. The location template has `[[Landmark 1]]` and `[[Landmark 2]]`. No file matches them, so the converter left them alone and they are the only wikilinks left in the templates. New notes made from these templates will start with wikilinks. Under the Calendar layout a month note sits at `YYYY-MM Month/YYYY-MM Month.md` beside the year note.

**Query:** Should the template placeholders be rewritten by hand as GFM links?

**Options:** a) (recommended, confidence medium - the Calendar layout makes the month path certain, but landmark notes have no fixed home) Rewrite them: months as `[YYYY-01 January](<YYYY-01 January/YYYY-01 January.md>)` and landmarks as `[Landmark 1](<Landmark 1.md>)`. b) Leave them as wikilinks, and let the touch rule convert each new note when it is first edited.

### LINK-REVIEW-NAME - Name of the Wikilink Review Activity

**Context:** The Wikilink Review Activity now reviews Markdown links and wikilinks alike, through the LINK-1 audit. Its name, its file and its trigger, "ki wikilink review", are unchanged. The Charter, What Keeps an Island Alive, Tending, Agents and the Knowledge Islands index all name it. Renaming means moving the file and changing the trigger in every note that names it.

**Query:** Should the Activity be renamed Link Review, with the trigger "ki link review"?

**Options:** a) (recommended, confidence medium - the name now undersells what it does, and the rename is reversible) Rename it to Link Review, and update the trigger and every note that names it. b) Keep the Wikilink Review name and trigger. c) Retire the Activity, because `ki repo audit` already checks links.

### RENDER-CHECK - Client render checks before acceptance

**Context:** Acceptance test 4 asks for the pilot's alert and heading link to be checked on GitHub, in Obsidian, in Zed and in the Observatory, or for each failure to have a recorded decision. This run could not open any of the four. Heading links now carry GitHub slugs: an example is the Library link in AGENTS.md (`Structure.md#library`). The Observatory drops fragments, so there the link opens the note without jumping to the heading.

**Query:** Will you run the four client checks before accepting KI-PRINCIPAL-OPS-014?

**Options:** a) (recommended, confidence high - this is the only acceptance test no tool could run) Before accepting, open AGENTS.md's Library link and an alert note in each client. Record any failure in the record. b) Accept without the client checks, and record the Observatory's fragment loss as known.
