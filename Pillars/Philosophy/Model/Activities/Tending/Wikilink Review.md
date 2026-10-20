---
note_type: pillars/note
tags:
  - card/note
  - topic/productivity
  - topic/knowledge-management
  - source/claude
status: current - April 2026
author: Written with Claude
---

# Wikilink Review

## Overview

A focused review of link health across the repository, over Markdown links and wikilinks alike. Surfaces broken outlinks (internal links pointing to files that do not exist or differ in case) and orphan notes (files with no incoming links). Run before or after a Structural Audit, or whenever navigation across the repository feels incomplete.

---

## When

Adhoc - _"ki wikilink review"_. Typically paired with [Structural Audit](<Structural Audit.md>) or [Inbox Review](<Inbox Review.md>). Run any time new notes are created in bulk or a section of the repository has been significantly restructured.

---

## What It Does

1. Run `ki repo audit --skill ki-repo-kb` for broken outlinks - its LINK-1 check resolves every internal link of either form in exact case, with heading fragments; decide whether to create the missing note or correct the link
2. Query for orphan notes - files with no backlinks; decide whether to link them from an appropriate index or parent note, or whether they are genuinely standalone
3. Cross-reference both lists against [Inbox Review](<Inbox Review.md>) - new notes in `+/` that haven't been linked yet are the most common source of orphans

---

## Link Types

| Type | Description | Resolution |
| --- | --- | --- |
| Broken outlink | An internal link in a note with no matching file in exact case ‡ | Create the missing note, or fix/remove it |
| Orphan note | A file that no other note links to - unreachable by graph † | Link from a parent index note, or archive |
| Placeholder link | A link intentionally left unresolved pending a future note | Create the note when the topic is ready |

† It exists but is unreachable by graph.

‡ No matching file in the repository.

---

## Live View

### Broken Links

Internal links pointing to files that do not exist in the repository are listed by `ki repo audit --skill ki-repo-kb` under LINK-1, for Markdown links and wikilinks alike.

### Orphan Notes

Notes with no incoming links - unreachable by graph navigation. Calendar notes and inbox items are excluded.

```dataview
TABLE status, purpose
FROM ""
WHERE length(file.inlinks) = 0
AND !contains(file.path, "Calendar/")
AND !contains(file.path, "+/")
AND !contains(file.path, ".obsidian/")
SORT file.path ASC
```

---

## Notes

- The orphan view requires the [Dataview](https://github.com/blacksmithgu/obsidian-dataview) plugin to be installed and enabled; Dataview counts Markdown links and wikilinks alike as incoming links
- Not all orphan notes are problems - some reference notes are genuinely standalone; use judgement
- Do not remove a link without first checking whether the target note should exist
