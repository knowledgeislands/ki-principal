---
note_type: pillars/index
tags:
  - card/note
  - topic/mcp
  - topic/notion
  - topic/knowledge-management
source: claude
status: archive - October 2026
---

# Notion Mirror

## Retirement

Kris retired this server on 26 October 2026 and deleted its repository on GitHub and on sol and terra; see [Known Lands](<../../../../../Admin/Governance/Known Lands.md#retired-lands>). No active binding or checkout should refer to the deleted package. The ordinary hosted Notion connector used to read and trash pages is separate and remains available.

The tool catalogue and safeguards below are historical reference only.

## Historical purpose

MCP server that mirrors Knowledge Base notes into Notion and records the resulting page URL in each note's frontmatter. Source: `mcp-ki-kb-notion-mirror`. The former tool catalogue lived in the deleted repository; Git history retains the integration rationale.

## Tools

**Notes** - `kb_notion_mirror_note_*` tools act on one `kb_path` per call: preflight, status, diff, get, touch, update, move and delete under a caller-supplied Notion parent.

**Trees** - `kb_notion_mirror_tree_*` tools act on a caller-supplied folder subtree: preflight, status, touch, update, prune and delete.

**Roots** - `kb_notion_mirror_roots_list` lists configured mirror roots.

## Notes

One-directional: the KB is the source of truth and Notion is a derivative read surface for people who do not work in the KB. There is no fixed root folder or wiki database; every mutation names its KB path and Notion parent. Destructive operations default to `dry_run`. Do not edit mirrored content in Notion directly - the next mirror run overwrites it.
