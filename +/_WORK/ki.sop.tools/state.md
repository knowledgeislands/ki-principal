---
id: ki.sop.tools
state: with-worker
hold: null
since: 2026-11-08T20:48:00Z
received: 2026-11-08T20:48:00Z
beat: null
mark: null
host: sol
workers: []
listening_enabled: true
listening_status: off
syncing_enabled: false
syncing_status: off
---

# ki.sop.tools state

## Now

- Reset on 8 November (RESET-PARK): everything before is parked; acting only on Kris and the six reset sessions, with personal.reg.inbox coordinating. Messaging is through the Agora store via the Agora MCP.
- Listening stopped at 22:49 GMT for the package's move into the Agora store (PACKAGE-TO-AGORA); no new work starts and no Agora message goes out until Kris says.
- Running: std-base in tools-ki (run packet `~/.local/state/ki/agents/ki-sop-tools/std-base.*`, brief `std-base/check.brief.md`), launched 22:20 GMT, at 22:48 GMT running the full test suite. On its report, reply to ki.reg.guilds (brief 01a1bcff) with the commit.
- Done: tools-rig and the coordinator-footer hook need no `_index.md` change; tools-ki's `_index.md` read landed by ki.reg.guilds in b537df2e; mcp-agora is the warden's; OBSERVATORY-READERS was withdrawn and its run stopped, its edits kept at `~/.local/state/ki/agents/ki-sop-tools/obs-index.withdrawn.patch`.

## Queue

- INDEX-ENTRY tools-ki: ki.reg.guilds's tools-index landed b537df2e at 22:19 GMT; waiting on its account of what it covered, then take over what's left, including a reinstall check (any release goes to Kris).
- STD-BASE check: run std-base running in tools-ki since 22:20 GMT; reply to ki.reg.guilds with the commit.

## Next steps

1. When Kris resumes: re-arm the Agora watch (fetch and compare origin/main only, WATCH-FETCH) at the package's new home.
2. Receive std-base; reply to ki.reg.guilds with its commit.
3. INDEX-ENTRY tools-ki: wait for ki.reg.guilds's account of what tools-index covered and whether the installed ki needs a reinstall; finish what's left; then reply to personal.reg.inbox (brief 01a1bcf0) with what landed and where. Any release goes to Kris.

## Held

- Parked under RESET-PARK until Kris says otherwise: the seven Inbound lines in `messages.md` (RIG-RETIRE, RIG-INTAKE, MAIL-GAPS, MAIL-IDEAS, RIG-ATTENDED, SCHEDULING, RIG-OWNS-CONFIG) and the earlier next step to take them on release.
