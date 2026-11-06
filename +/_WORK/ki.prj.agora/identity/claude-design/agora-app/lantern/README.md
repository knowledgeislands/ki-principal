---
title: Agora Lantern design
status: proposed
updated: 2026-11-06
author: Claude Design (information architect)
---

# Agora Lantern: Who is listening

The iPhone companion to the Agora app, with one screen. Open [index.html](index.html) for the annotated board. It only shows; it grants no authority and writes nothing to Git.

## Artboards

Each is 393 by 852 points, in night (the reference) and light.

| Artboard | What | Region codes |
| --- | --- | --- |
| a ★ | Grouped by Mac | L1 to L9 |
| b | Grouped by territory | L1 to L9, L12 |
| c | Listening first | L1 to L9, L12 |
| a-detail | a, with hnr.sop.main opened | L1, L2, L3, L10 |
| a-empty | a, no Mac reachable | L1, L2, L3, L9, L11 |

Codes: L1 summary and key, L2 group header, L3 agent rows, L4 package id, L5 territory, L6 focus areas, L7 listening state, L8 waiting on you, L9 ping bar, L10 agent detail, L11 no-Mac message, L12 Mac.

## Files

- `build.py` writes `mocks/<artboard>-<night|light>.html` and, once `shots/regions.json` exists, `index.html`.
- `shoot.js` takes `shots/*.png` (2x, each under 500 KB), measures the regions and warns of clipped text.
- Run: `python3 build.py && node shoot.js && python3 build.py`.

## Choices

- **Preferred a, grouped by Mac.** Presence belongs to a Mac, so a Mac that drops takes its agents with it and the header says so once. Within a Mac, silent rows come first, then on open, then listening. A Mac header folds to one line.
- **Glyph, word and colour together.** Solid dot "listening", hollow ring "on open", slashed ring "silent", dashed ring "unknown". These reuse the pack's stone, hollow and slashed marks. Colour only repeats them.
- **Gold is attention.** Silent rows and waiting counts use gold text and a gold edge. The one brass fill is the ping action in the thumb zone; in the empty state it becomes "Try again". The detail's own ping is outlined, not brass.
- **A row is two lines.** Package id and state; then territory, the primary focus starred plus one more with a count, and the waiting count. The full focus list is in the detail. Rows are 62 points tall, above the 44-point minimum for a tap.
- **Listening means answered Agora's call, or polling.** That gives 9 of 12 (the pack's `call` and `poll`). On open is the 10th, silent the 11th and 12th.
- **Unknown, never gone.** With no Mac reachable the Macs read unknown and the agents are hidden, not shown stale. The screen says an unknown Mac may still be running work, as AGENTS.md asks.
- **Lists, not cards.** System font, tokens copied from `../build/app.css`, no pure black or white. The Dynamic Island is a near-black, as the hardware is.
- The roster is a snapshot of `../build/data.py`, held in `build.py` so this folder stays stable while the main pack changes. The detail's two query titles (SITE-DOMAIN, P2MS3-DATES) are invented; the pack gives only their ids.

## Open questions

1. Is "Ping everyone" the right one action? It sends the same ping as the app. Or should the phone offer Away (a broadcast) there instead?
2. Should a tap on "waiting" go anywhere? Lantern has no inbox; the pack's 4.1 Waits on you lives in the Mac app.
3. Should a silent agent show how long it has been silent, rather than a time of day? "2h 10m" reads faster, but needs the phone's clock to agree with the Macs.
4. How does the phone reach the tailnet when Tailscale is off? Lantern can only say so; Agora accepts requests only from configured peers of the same Tailscale user.
5. Does the phone need a notification when an agent goes silent? It is the main reason to glance, but it would make Lantern more than a viewer.
6. Is `poll` (household-sol, polling every 2 minutes) a listening agent, as drawn, or a fourth state?
