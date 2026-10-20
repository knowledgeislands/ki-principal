---
note_type: pillars/note
tags:
  - card/note
  - topic/knowledge-islands
  - topic/knowledge-management
status: draft - April 2026
author: Written with Claude
---

# Format

## Overview

Every note follows a consistent physical structure. The rules here govern what sections a note contains, how those sections are organised, how content within them is formatted, and how notes reference each other and embed external material. Type-specific extensions are in [Notes](Notes.md) (Types section); the properties and tags that live in frontmatter are in [Notes](Notes.md) (Frontmatter section).

---

## Full Note Structure

1. **Frontmatter** - YAML block with `tags`, `status`, `author` (and optionally `creator`)
2. **Title** - H1 heading matching the filename (see H1 and Filenames below)
3. **Overview** - `## Overview` section; high-level introduction
4. **Body** - H2 sections on the topic; one topic per section

Each section is separated by a `---` horizontal rule. Type-specific notes may extend this structure with additional footer sections.

**Single-section exception:** If a note has only one H2 section (its Overview), omit the `## Overview` heading - the content follows the H1 title directly. A heading that labels the only section adds no structure and no navigation value.

---

## H1 and Filenames

The H1 heading should use the canonical title of the note. Filenames must avoid characters that are invalid on most filesystems - use `-` as a substitute for `:` and `-` where needed. This means the H1 and filename may differ in punctuation; this is expected and not an error.

---

## Tables

Target a total table width of 200 characters. Pad columns with spaces so that column borders align vertically, making them readable in a plain text editor. The separator row should match the width of the widest cell in each column.

If the content is too wide to fit within 200 characters, collapse all padding so each cell contains only its value with single spaces either side of the `|` - no alignment padding.

### Fits within 200 characters - pad to align

````text
| Field     | Format / Values                     |
| --------- | ----------------------------------- |
| `status`  | `draft - Month YYYY`                |
```text

### Too wide - collapse whitespace

```text
| Field | Format / Values |
| --- | --- |
| `status` | `draft - Month YYYY`, `current - Month YYYY`, `archive - Month YYYY`, `outdated - Month YYYY` |
```text

---

## Markdown Conventions

Consistent formatting ensures notes render correctly and remain readable in plain text.

### Sub-section headings

Use H3 (`###`) for sub-section headings within a body section - not bold text. Bold is for inline emphasis only, not structural headings.

### Lists

Always include a blank line between a paragraph or heading and a following list (ordered or unordered). Without it, some renderers will not
parse the list correctly:

```markdown
Some introductory sentence.

- First item
- Second item
```text

### Trailing newlines

Every file must end with a single trailing newline - the last content line is followed by exactly one `\n`, with no blank line after it. Do
not end files mid-line or with multiple trailing newlines (`\n\n` or more).

---

## Links and Images

Internal links are GitHub-flavoured Markdown (GFM) links, and linking is preferred over repeating content - link rather than duplicate. When a concept, decision, or piece of reference material has its own note, link to it rather than restating it.

### Body link format - document-relative path

A body link's destination is the target's path relative to the note holding the link, in the target's exact on-disk case and with its extension:

1. Write the path from the linking note to the target - `[Concept](../Concept/Concept.md)`
2. Put a destination that holds a space or a parenthesis in angle brackets rather than percent-encoding it - `[Enactment Process](<../Processes/Enactment Process.md>)`
3. Link to a heading with its GitHub heading slug - `[Library](../Structure/Structure.md#library)`

The link text is the reader-facing name of the target, usually its leaf name or title. Wikilinks (`[[Note Name]]`) are still read and resolved, but a new or edited note uses Markdown links: editing a file converts its wikilinks in the same change, with `ki markdown gfm`, and the link audit checks every internal link of either form in exact case.

Images and diagrams used by a single note must be saved in the same folder as that note. Images shared across multiple notes may sit in a
folder common to all the notes that use them.

Embed an image as a plain Markdown image, with descriptive alt text and a path relative to the note:

```markdown
![Diagram of the capture, connect and reflect cycle](diagram.png)
```text

The alt text says what the image shows, so the note still reads without it. Do not add a size constraint; a demonstrated sizing need is decided as an explicit exception.

Bare URLs must be wrapped in angle brackets so they render as clickable links in all contexts:

```text
<https://example.com>
```text

Where a note references several external sources, use Markdown reference-style links - define the URL at the foot of the file and use a
short label inline. This keeps the body text readable and groups all external references in one place.
````
