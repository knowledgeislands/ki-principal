---
id: ki.prj.agora
parent: ki.sop.main
level: project
title: 'KI > Techne > Agora'
project: agora
theme: techne
description: >-
  Builds and runs Agora: Beacon, the always-on menu-bar app where territories meet; Atlas, the desktop viewer;
  Lantern on the phone; and the Agora MCP and store in knowledgeislands/mcp-agora. Takes Agora features,
  records, the KIV and identity design. Not for the vega recipe (ki.prj.agent-host), the Observatory's own
  repository (ki.prj.observatory), or the coordination method (ki.prj.ways-of-working and personal.reg.inbox-sol).
worker: agent
supervisor: owner
role: warden
created_at: 2026-11-03T22:50:53Z
---

# ki.prj.agora

## Goals

- Deliver the [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/agora.md) Project's outcome.
- Give Agora its own coordinating thread, so it carries on without holding personal.reg.inbox-sol's attention.
- Role: **warden** ⚒️, the Project package's primary role (ROLE-FIX, 6 November 2026, under Kris's approval of ROLES-TIDY); the footer, messages and Atlas's who-holds-what table use it. Atlas's navigation run confirmed the Warden role, distinct from Beacon's own glyph.

## Scope

- In: `knowledgeislands/apps-agora.local` and its eight existing records (KI-AGORA-APP-001, KI-AGORA-LVL-001, KI-AGORA-NET-001, KI-AGORA-TRY-001 and KI-AGORA-WRK-001 to KI-AGORA-WRK-004), plus the fifteen non-MCP records adopted under PACKAGE-PLAN; the KIV, owned by Agora since 6 November (KIV-TO-AGORA), its views in Atlas now and its code moved in later; waking Orca threads; Agora Lantern and its read-only phone endpoint; reading the jobs register household-sol keeps (AGORA-JOBS), once it exists; Agora's identity design and the two design doers in `identity/` (the illustrator in ChatGPT Codex and the information architect in Claude Design) until the MCP pilot replaces their mailboxes.
- In: the Agora MCP and store in `knowledgeislands/mcp-agora` under AGORA-STORE and APPLY-SCOPE: `messages/<territory>/<recipient>/<ISO-8601 UTC ms Z>-<uuid>.md`, one file per message, processed by filename order with UUID ties; and `roster/<territory>/<work-id>.md`. Beacon binds to one store, through a local clone with immediate commit and push or a direct remote writer. Handled messages leave the tree but stay in Git history; truncation requires Kris's word. MCP work belongs to that repository's own roadmap once it exists.
- Out: the vega recipe and Techne products (ki.prj.agent-host); the Observatory's own repository and product (ki.prj.observatory); the coordination method and message words (personal.reg.inbox-sol under TOPIC-HOMES, with the standard's text owned by ki.sop.main); Rig's scheduled-jobs engine (tools-rig, sent to ki.prj.mac-studio-setup as RIG-AGORA-ENGINE); keeping the Personal territory's beacon repository, which remains its watchman's; Orca's own chat-send work, watched only; installing and updating each rig, which the households own except for the specific NIGHT-INSTALL grant to the coordinator and the approved UPDATE-PATH click in the product. This application run installs nothing.

## Focus

1. `atlas` ⭐ - Agora Atlas: Known Lands, who holds what, Roadmap, Jobs, Guilds, Accounts, Settings, Updates and the Observatory's and KIV's tabs, built against Claude Design's pack.
2. `mcp` - the Agora MCP and store in knowledgeislands/mcp-agora: specification decisions, the pilot with the two doers, then migration.
3. `beacon` - Agora Beacon and Agora Lantern: presence and health, Agora's call and the end of `doorbell/`, broadcasts and marks, keeping level, releases to both Macs.
4. `jobs` - running the rig's scheduled jobs, switching Claude accounts, keeping the host awake and checking host settings: captured, each waiting on its decisions.
5. `identity` - Agora's look and its two design doers: badges, glyphs, icons and the design pack.
6. `kiv` - the KIV: its views in Atlas now, the approved deliberate-click defer write without committing (KIV-WRITE a), then its code move.
7. `_emerging` - what has not yet been named: the voice bard path, with no work or record since 3 November.
