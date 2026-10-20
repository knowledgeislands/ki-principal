# gfm-review - blind review of the conversion's open questions

Blind review. Do not read any `+/_WORK/` file or run report. Read-only: ki-principal (now GitHub-flavoured Markdown), its Format convention note and `ki markdown gfm`. No edits, commits, launches or network calls. For each query pick an option (or another), with confidence, one-line reason and conditions.

## SIZED-EMBEDS - Images sized to width 800

**Context:** Four Pillars images use Obsidian's sized embed `![[image.png|800]]`. Two are in Influences Along the Way, one in What is Knowledge Islands and one in What is Knowledge. The Format note still prescribes that form, so acceptance test 5 is only partly met. GFM has no size syntax. GitHub and Obsidian both already shrink a wide image to fit the column. An HTML `<img width="800">` renders on GitHub, but Obsidian may not resolve a relative path inside raw HTML.

**Query:** How should the four images, and the Format note's image rule, be written?

**Options:** (unranked)

- Plain GFM images `![alt](<image.png>)`, and Format drops the width-800 rule.
- Keep the four as recorded Obsidian-only exceptions, and keep Format's sized-embed rule for images.
- HTML `<img src="image.png" width="800" alt="...">`, after a check that Obsidian renders it.

### TEMPLATE-LINKS - Placeholder links in two templates

**Context:** The yearly Calendar template has 12 month placeholders, such as `[[YYYY-01 January]]`. The location template has `[[Landmark 1]]` and `[[Landmark 2]]`. No file matches them, so the converter left them alone and they are the only wikilinks left in the templates. New notes made from these templates will start with wikilinks. Under the Calendar layout a month note sits at `YYYY-MM Month/YYYY-MM Month.md` beside the year note.

**Query:** Should the template placeholders be rewritten by hand as GFM links?

**Options:** (unranked)

- Rewrite them: months as `[YYYY-01 January](<YYYY-01 January/YYYY-01 January.md>)` and landmarks as `[Landmark 1](<Landmark 1.md>)`.
- Leave them as wikilinks, and let the touch rule convert each new note when it is first edited.

### LINK-REVIEW-NAME - Name of the Wikilink Review Activity

**Context:** The Wikilink Review Activity now reviews Markdown links and wikilinks alike, through the LINK-1 audit. Its name, its file and its trigger, "ki wikilink review", are unchanged. The Charter, What Keeps an Island Alive, Tending, Agents and the Knowledge Islands index all name it. Renaming means moving the file and changing the trigger in every note that names it.

**Query:** Should the Activity be renamed Link Review, with the trigger "ki link review"?

**Options:** (unranked)

- Rename it to Link Review, and update the trigger and every note that names it.
- Keep the Wikilink Review name and trigger.
- Retire the Activity, because `ki repo audit` already checks links.

### RENDER-CHECK - Client render checks before acceptance

**Context:** Acceptance test 4 asks for the pilot's alert and heading link to be checked on GitHub, in Obsidian, in Zed and in the Observatory, or for each failure to have a recorded decision. This run could not open any of the four. Heading links now carry GitHub slugs: an example is the Library link in AGENTS.md (`Structure.md#library`). The Observatory drops fragments, so there the link opens the note without jumping to the heading.

**Query:** Will you run the four client checks before accepting KI-PRINCIPAL-OPS-014?

**Options:** (unranked)

- Before accepting, open AGENTS.md's Library link and an alert note in each client. Record any failure in the record.
- Accept without the client checks, and record the Observatory's fragment loss as known.

## Report

Owner report: Done (per query pick, confidence, reason, conditions), In Progress, Queries.
