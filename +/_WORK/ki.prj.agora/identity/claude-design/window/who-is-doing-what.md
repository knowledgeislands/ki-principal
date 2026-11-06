---
title: Who's doing what, first sketch
status: proposed
updated: 2026-11-06
owner: ki.prj.agora
author: Claude Design (identity doer)
---

# Who's doing what, first sketch

The richer view behind the tray's `Agents` submenu (goal 3 in the specification): every live agent on both Macs, what each looks after, whether it listens, and what waits on Kris. It is also the address book for routing by focus.

| Night (the reference rendering) | Light |
| --- | --- |
| ![Night](who-is-doing-what-night.png) | ![Light](who-is-doing-what-light.png) |

[The sketch](who-is-doing-what.html) is one HTML page in the Instrument dialect of `ki-design`. It uses system type, tokens only and a table, and follows the OS theme; add `?theme=light` to see light. The data is illustrative. The rows for ki.prj.agora and ki.sop.main come from their work packages on 6 November 2026; the others' focus areas, times and queries are placeholders.

## What it shows

- **The summary**, one line, in the same words as the tray: `10 agents on 2 Macs · 7 listening · 1 on open · 2 silent · 34 queries wait on you`.
- **One row per agent**, grouped by Mac with this Mac first, each Mac's row saying whether it is present.
  - **Agent:** the work id and its title.
  - **Territory.**
  - **Focus areas,** the primary first, starred and in bold.
  - **Listening:** how it listens (Agora's call, polling and its interval, on open, or off) and when it last answered.
  - **Waits on you:** how many queries, with the first ids.
- **Who looks after…** is the address book. Typing `identity` keeps only the agents whose focus covers it, with the matching focus picked out. It is the same lookup an agent makes through Agora before sending an idea.
- **The selected agent**, below the table:
  - its focus areas with their one-line descriptions;
  - how and when it last listened, and when its listener is next checked;
  - its run and doers;
  - what waits on Kris, with the one brass action, `Open its queries`, and the quieter `Ping it` and `Open its folder`.

## Choices

- **A table, not cards.** It is dense and stays in place: rows are sorted by Mac, then territory, then work id, never by recent activity, so an agent stays where Kris learnt it was (continuity over disruption). At a narrow width the territory column drops first.
- **Listening is shown from answers,** not from the agent's own `listening_status`: a ping or call answered sets `answered 04:12`; two calls unanswered make it `Silent`. This is how the hnr.sop.main message that lay unread from 4 to 6 November would have shown up.
- **Shape and word, never colour alone.** A solid stone means listening, a hollow stone means it reads on open, and a slashed stone with the word `Silent` (rust) means it has not answered.
- **The star is ink, not gold.** In `ki-design` gold means attention, so the only gold in the window is the one action that needs Kris.
- **One brass action per view,** on the selected agent: open its queries, since those are what wait on Kris.
- **No agents dashboard feel.** The work id and its title lead each row, so the window reads as work packages with their workers, as `ki-design` asks ("who is working is a column").

## What it needs from Agora

The live roster (goal 3, in the overnight runs) supplies most of this:

- each agent's focus areas and primary, read from its `work.md`;
- its listening method from the register (`agora-call`, `poll`, `on-open`, `off`);
- its last answer from Agora's acknowledgements;
- the count and ids of its open queries, from its `discussions.md` headings.

The read endpoint (`/v1/state`) could carry the same, so the Observatory or the KIV can show it too.

## Open

- **A window at all?** The specification's C12 keeps Agora to small windows only. This one is small (about 1080 by 700 points) and opens only on request, from line 1 of the tray or `Who's doing what…`. If it should live in the KIV or the Observatory instead, the same table moves there unchanged.
- **Where the queries come from.** Counting `###` headings in `discussions.md` is a guess at the source; personal.reg.inbox-sol's method may name the true one.
- **Doers.** Doers such as this Claude Design session are shown under the package that brought them in, not as agents of their own. Should they count among the agents?
