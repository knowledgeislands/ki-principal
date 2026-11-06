---
title: Claude Design's work for Agora
status: proposed
updated: 2026-11-06
owner: ki.prj.agora
author: Claude Design (identity doer)
---

# Claude Design's work for Agora

Information architecture for Agora, done for ki.prj.agora on 6 November 2026 from the [overnight brief](../../_emerging/overnight-brief.md). [index.md](index.md) lists every file.

| Piece | Read | Look at |
| --- | --- | --- |
| 1. How Agora fits together: one Mac, two Macs, the life of a message | [architecture.md](architecture.md) | [diagrams/](diagrams/) |
| 2. The calmer tray menu | [tray/tray-menu.md](tray/tray-menu.md) | [tray/tray-menu.png](tray/tray-menu.png) |
| 3. Who's doing what, first sketch | [window/who-is-doing-what.md](window/who-is-doing-what.md) | [night](window/who-is-doing-what-night.png), [light](window/who-is-doing-what-light.png) |

Everything here is **Proposed**, in the Knowledge Islands status words.

## Choices

- **Two layers in every picture.** Git is the durable layer and Agora the conversational one (TWO-LAYERS). The diagrams colour them apart (green and teal) and say so in words. Solid lines are what works today; dashed lines are the target or a gap, so the pictures do not promise what is not built.
- **Real names, plain verbs.** The diagrams use sol and terra, real work packages and the words Agora already uses (Agora's call, broadcast, ping, mark). The life of a message follows one idea from hnr.sop.main to ki.prj.agora and into the record.
- **Agents and Macs** on screen, as the specification now says (C13), replacing "computers" in KI-AGORA-TRY-001's menu. "Not heard from" for a Mac and "silent" for an agent. Never "quiet", which is a Knowledge Islands condition word.
- **The tray answers in two lines:** `10 agents on 2 Macs`, `All well`. Below them come only the exceptions, at most three, each with what Agora saw, what it did and at most two actions; then the actions; then detail one level down. Away and I'm back are one item that changes. The submenu labels carry no counts, so they stay still. The menu-bar title is the ring alone (AGORA-COUNT-PLACE a).
- **The window is a table, not cards,** sorted by Mac, territory and work id so rows stay put. Listening is shown from answers, not self-report. Gold is kept for the one action that needs Kris; the primary-focus star is ink.
- **Tokens and night.** The diagrams and the window use `ki-design` tokens only, with night as the reference rendering. The tray is drawn as the native macOS menu, which takes the system's colours.

## Open questions

For ki.prj.agora to take to Kris, or to personal.reg.inbox-sol where they are coordination rules.

1. **Who counts as an agent in line 1.** The proposal counts agents that have joined, on the Macs heard from; a silent one still counts and shows as an exception. Should a silent agent drop out of the count instead?
2. **A Mac that left on purpose.** The proposal treats it as no fault: line 1 says `4 agents on 1 Mac` with no exception row. Is that right, or should Kris always see that terra is away?
3. **"Where it started"** in "made durable by the assistant on the Mac where it started": the diagram reads it as where the news was announced (sol), not where the idea was first raised (terra). Which is meant?
4. **Acknowledging an ordinary message through Agora** (conversational, no commit) is drawn as the target. Today only pings and marks are acknowledged that way. Does every message get an Agora acknowledgement, or only those that ask for one?
5. **Two new tray actions:** `Call hnr.sop.main again` on a stuck checkout and `Ping it again` on a silent agent. Each rings one package's call, which Agora already does for `ahead, push it`. Are they within Agora's bounds?
6. **`Review now` goes.** Sync now ends with a review, and reviews run every five minutes. Does anyone rely on `Review now`?
7. **The window and C12.** The specification keeps Agora to small windows. The window is modest and opens only on request. Should it live in Agora, or in the KIV or the Observatory? DESIGN-PACK (MSG-9f90977f) now points to a richer Agora app, so this may be settled there.
8. **The icon.** The tray mockup uses the shipped three-stone ring. The ChatGPT studies use six stones and put the diamond inside the ring. They also name concepts after the Causeway, whose meaning is taken (translation), and the Harbour, which is retired; ki.prj.agora may want to rename those before they travel.
9. **Placeholders.** In the mockups, the focus areas, times and queries of agents other than ki.prj.agora and ki.sop.main are invented, apart from personal.reg.inbox-sol's `method` and `kiv` focus areas. The live roster will replace them.
