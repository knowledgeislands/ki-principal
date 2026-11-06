---
work: ki.prj.agora
session: interactive
written_at: 2026-11-06T06:20:00Z
---

# Agora: what we agreed and what is being built (6 November 2026, 06:20 GMT)

## The picture

- **Islands** are repositories, the home of everything durable; each has its own roadmap. A **territory** is a group of islands with a principal island, whose council is State of play main.
- **Rigs** (sol, terra) are planes of existence over the same islands: neither sees what the other is doing at the moment it happens, but each sees the effects of what the other has done.
- **Work packages** pull work through. Regular ones sit one-to-one on an island; Projects sit in the principal island because they bring several islands together. When swamped, a package pushes back up into roadmap items and ideas.
- **Roles:** leaders, enablers, doers. Per rig, the housekeeper (household) and the assistant (inbox) run the rig.

## How they talk

- **Two layers.** Durable (work and knowledge in Git: `messages.md` Inbound and Outbound, `MSG-` ids, ACKs) and conversational (through Agora, no Git).
- **Hierarchy, not everyone to everyone.** Each island has a meeting point; work packages talk up to their territory's State of play main; the mains talk across territories; the great portal joins the rigs.
- **Routing by focus:** an idea goes to the agent whose focus covers it; new features are announced to every agent that has joined.
- **Announce, then make durable:** new and noteworthy is announced; the assistant on the rig where it started writes it into the record.
- **Presence:** roll call and keep-alive are one mechanism; pings at 50% and 75% of an agent's listening period, then every 5% until lost.
- **Mark:** a line in the sand across the Agora; later updates run from it.
- **Where Agora cannot push into a session, the session polls.**

## The two apps

- **Agora Portal** (the tray): communication only. Status line, Open Agora, Broadcast, Away, Ping, Mark all, Sync now, Quit. It is the rig's portal (Tailscale between rigs) and the local entrance agents use to join, speak, acknowledge and answer a roll call. It keeps checkouts level and never writes knowledge.
- **The Agora** (rich Electron app): one viewport-sized map of the civilisation: territories, islands, work packages, agents by role and rig, focus, messages as golden light, outputs building up, warnings and questions drawing attention; click an island to go in. Tabs host pages; first the Observatory's repository and activity views, then the KIV's views until the KIV retires. Later: art gallery, feedback written back to islands as change requests, islands' live artifacts and MCPs.

## Built tonight (apps-agora.local, tested and pushed)

- Agora's call (renamed from doorbell), small fixes, Mark all, the roster and focus address book, the settle call for cooperation between rigs, a calmer tray; installed on both Macs.
- Plain-English specification, RFC-style protocol draft, wake map, six architecture diagrams with a one-page explainer.
- Design doers: the information architect's Agora app design pack; the illustrator's concept art, icons and slides, each indexed.

## Building now, in order

1. Install fix (the stale build and missing relaunch).
2. **The Agora app**, first version: the civilisation map on live data, message events, Observatory tabs.
3. Portal slimmed to communication only.

## Rules we work by

- Skills are the home of reusable knowledge; specifications are RFC-style like the Agent Host Protocol.
- Work package holds work in progress only; a healthy roadmap behind it.
- Lint before push; nothing posted outside Kris's repositories; nothing starts an agent on its own; legacy only for hours, not weeks.

## Waiting on Kris

- The large art's home (Git, Git LFS or the OneDrive store).
- Protocol open questions; whether work packages may talk across territories directly.
- AGORA-START, AGORA-COUNT-PLACE, CONFIG-OWNER, ORCA-WATCH, MARK-WORDS and the scheduled-jobs design points.
