---
note_type: stream-roadmap
id: KI-PRINCIPAL-ECO-015
area: ECO
title: Tool toolchains brought level
priority: medium
size: l
status: draft
horizon: next
kind: deliver
purpose: upkeep
component: engineering-practice
assignee: work/ki.tools
blocks: []
blocked_by: []
baseline_ref: null
created_at: 2026-11-26T02:55:00Z
updated_at: 2026-11-26T02:55:00Z
---

# Tool Toolchains Brought Level

## Goal

Every Knowledge Islands tool and MCP server repository runs the current development toolchain, Bun 1.4.4 with the Biome, knip and rumdl versions tools-ki already runs, taken one repository at a time, each landing only on Kris's yes with a diff summary.

## Context

DEPS-HOLD held four development-tool updates from October 2026 (ki.guilds' [Skills refresh proposals (20)](https://github.com/krisb/ki-cairn-store/blob/c786846e80656d8e83ac4352df0b9e1458aa58b7/work/ki/ki.guilds/20-skills-refresh-proposals.change.md), its consequence 1). Biome, knip and rumdl are now past the 14-day window. Kris set the order on 24 November 2026, 11:16 GMT, via Kitteth: the `ki` tools come back on in stages, the store-reading step first, then the held tool updates one repository at a time, then Bun 1.4.4, each landing only on his yes with a diff summary ([ki.tools at 177742d5](https://github.com/krisb/ki-cairn-store/blob/177742d5205ec4bcedd2ce58378beb7a5831c447/work/ki/ki.tools/_index.md)).

Checked locally on 26 November 2026: tools-ki, packages-stoa, packages-tessera, ki-principal, ki-agent-backpack, ki-techne-harness and the sites already pin Bun 1.4.4 and Biome 2.6.6 or later. Nine still pin Bun 1.4.3, Biome 2.6.3, knip ^6.43.0 and rumdl ^0.3.0: tools-git-almanac, tools-techne, mcp-acquire-whatsapp, mcp-git-audit, mcp-gsuite, mcp-housekeeping-chatgpt, mcp-housekeeping-claude, mcp-ki-kb-fs and mcp-m365. tools-mgit and tools-rig carry no Bun toolchain.

Captured at `next` from the ki.tools reset map ([4.1 and 4.4](https://github.com/krisb/ki-cairn-store/blob/d28c5faeca6ddcf069354dea49e8a645a37d7efb/work/ki/ki.tools/13-reset-map.change.md#41-kisoptools-legacy-10), N13), as cross-estate coordination: ki.tools owns the participating set, the order and the roll-up, and each repository its own update, release and acceptance.

## Boundary

- **In:** the participating set above, each repository's update to the shared versions as one housekeeping change, its checks rerun, and the roll-up here.
- **Out:** releasing any tool, which waits on Kris; a toolchain version not yet past its 14-day window; the shared versions themselves, which `ki-engineering` sets.

## Discussion

Each repository's change goes to Kris with a diff summary before it lands, under the switch. Whether a repository's update needs its own record there is settled when its turn comes; none does yet.
