---
id: ki.prj.agora
state: handoff-to-supervisor
since: 2026-11-07T04:53:34Z
received: null
beat: null
mark: 2026-11-07T04:53:34Z
listening_enabled: true
listening_status: off
method_read: d5ede6dd
workers:
  - role: warden
    tier: managers
    since: 2026-11-03T22:50:53Z
    status: active
    listening: off
---

# ki.prj.agora state

## Now

- Overnight delivery is landed and installed on sol, terra and the phone under NIGHT-INSTALL: Home's Island column and dashes for seats not created, the published role glyphs, the Atlas staying full across a Beacon restart, Lantern (bundle info.knowledgeislands.agora-lantern, icon, details card, Listening and Roadmap views), the revised Atlas designs, the Guilds skill table's layout and its tallies counted without their own choice. No run is going.
- The Agora MCP (knowledgeislands/mcp-agora) now supports one shared mount for every agent, each naming itself with `from`. Mounting for all agents (MCP-MOUNT) is stopped on MOUNT-1 and MOUNT-2: the store's Markdown check refuses every message. The store's README and Agora's MCP specification now describe what is built, with the rest marked Planned and cited to [the gap design](design/agora-gap.md).
- The roadmap sweep closed nothing and corrected five records. [KI-AGORA-NET-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-NET-001-observatory-read-endpoint.md) and [KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md) still need review packets.
- Terra cannot reach GitHub while its SSH agent is locked; installs reach it by pushing from sol.
- The thread listens on Agora's call, ~/.local/state/ki/agora/call/ki.prj.agora, and the old doorbell path. Health pings stay with the coordinator until [KI-AGORA-NET-002](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-NET-002-beacon-health-watches.md).

## Next steps

1. On MOUNT-1 and MOUNT-2, resume mcp-mount-all: store lint exclusion, live test, chezmoi `agora` entry for mcporter, apply on sol and terra.
2. Then the Beacon's binding to the store, the gap design's Phase 1, which waking depends on.
3. On MCP-READ and STORE-CODE, a small follow-up run for the specification and the store's code.
4. Prepare NET-001 and TRY-001 review packets for Kris.
5. Shape [KI-AGORA-NET-004](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-NET-004-retire-doorbell-path.md) once every watched thread's health ACK names call/.
6. Gap design notes: Atlas still looks up the island key `ki-portal`; chezmoi keeps an old mgit binding.
7. Retain the other open queries in [discussions](discussions.md). Nothing starts a fresh agent without Enactment under FOCUS-FIT.
