---
title: Agora tray menu
status: proposed
updated: 2026-11-06
owner: ki.prj.agora
author: Claude Design (identity doer)
---

# Agora tray menu

A calmer tray, as Kris asked on 6 November about 04:00 GMT (TRAY-CALM): "there's obviously too much information in there". The menu answers "is everything all right?" in two lines, shows only what is wrong below them, and keeps everything else one level down.

![The tray menu in its three states, light and dark](tray-menu.png)

The [mockup](tray-menu.html) is drawn from [build.py](build.py). It shows the native macOS menu Agora uses, with the shipped meeting ring in the menu bar.

## The shape

```text
10 agents on 2 Macs                    line 1: who is here
All well                               line 2: the verdict
◆ hnr-principal on terra is diverged ▸ only while something is wrong, at most 3
─────────────
Broadcast…
Away…  ▸   (or I'm back, "Away until 08:00", while away)
Ping
Mark all ▸
─────────────
Agents ▸
Macs and checkouts ▸
Runs ▸
Broadcasts ▸
News ▸   (News · 2 new, while unread)
─────────────
Sync now
Open log
─────────────
About Agora
Quit Agora   (sol leaves the Agora)
```

Four blocks: the answer, speaking to everyone, the detail, and looking after Agora itself. The top block grows only when something is wrong.

## Line 1: who is here

The count is of agents that have joined (are in a watch list) on the Macs heard from.

| Situation | Line 1 |
| --- | --- |
| Both Macs present | `10 agents on 2 Macs` |
| One Mac not heard from | `4 agents on 1 Mac`, plus an exception row for the missing Mac |
| The other Mac has left (said goodbye, or gone past 10 minutes) | `4 agents on 1 Mac` and no exception row, because leaving is not a fault |
| One Mac only, by design | `4 agents on sol` |
| This Agora is not in the square | `Not in the Agora: not listening` |
| Not configured | `Not in the Agora: not configured`, then the reason and the path Agora reads |

## Line 2: the verdict

| Situation | Line 2 |
| --- | --- |
| Everyone heard, everything level | `All well` |
| Before the first review after starting | `Looking…` |
| One thing wrong | `1 needs a look` |
| Several | `3 need a look` |

Lines 1 and 2 are set in bold. They are enabled, not greyed, so they read at full strength. Clicking line 1 opens Who's doing what.

## Exceptions: the only detail at the top

Each thing that is wrong gets one row under line 2, with its mark and a submenu. The submenu says what Agora sees, what it did, and at most two actions. At most three rows are shown, most serious first; a fourth becomes `and 2 more ▸`, which opens Agents or Macs and checkouts.

| Exception | Mark | Row | Submenu |
| --- | --- | --- | --- |
| A Mac not heard from | hollow stone | `terra not heard from since 03:41` | `Last heard at 03:41` · `Its 6 agents are not counted until it is back` · `1 broadcast waits for it` · `Nothing it holds is taken over` · **Ask after terra now** |
| A checkout stuck | diamond | `hnr-principal on terra is diverged` (or `is dirty`, `is detached`, `has no upstream`) | `Ahead 1, behind 2 of origin/main` · `Agora has left it as it is` · `Called hnr.sop.main at 04:12 to settle it` · **Call hnr.sop.main again** · **Show in Finder** |
| Two Macs disagree | diamond | `ki-design: sol and terra disagree` | The disagreement as the review found it |
| An agent silent | slashed stone | `hnr.prj.site-robots silent since 02:10` | `Last answered at 02:10` · `Listens by Agora's call` · `2 calls unanswered` · **Ping it again** |
| A wake waiting on Orca | slashed stone | `hnr.sop.main cannot be woken` | `It is an Orca chat, which Orca cannot send into yet` · `Kris was told at 04:12` |

Not exceptions, so they stay one level down:

- A checkout only ahead for under a minute.
- Unread news. The ring's centre point and `News · 2 new` carry it.
- A queued broadcast, unless its Mac is missing.
- A Mac that left on purpose.

## Speaking to everyone

| Item | Does |
| --- | --- |
| `Broadcast…` | Opens the small window to type a message to every agent on every Mac |
| `Away…` ▸ | `2 hours`, `4 hours`, `8 hours`, `Until a time…`. While an Away window is open, this item becomes `I'm back`, with `Away until 08:00` beneath it |
| `Ping` | Asks every agent to answer. `Ping threads` becomes `Ping`, since every agent, not only threads, answers it |
| `Mark all` ▸ | `Mark and summarise`, `Mark only`, a `No art` tick |

Away and I'm back become one item that changes, so the menu never offers both at once.

## Detail, one level down

| Submenu | Holds |
| --- | --- |
| `Agents` | Each agent by Mac, this Mac first: a stone (solid listening, slashed silent), its work id and its primary focus (`★ send`). Then `Who's doing what…`, which opens the window |
| `Macs and checkouts` | Each Mac with its presence and where it listens; then the checkouts: `64 level`, and each one not level with its condition; then `Territories` |
| `Runs` | Running first, then the rest, each with its package |
| `Broadcasts` | Recent broadcasts, each with `3 answered, 1 silent` and who; then those received from the other Mac |
| `News` | Recent news, newest first, `HH:MM  package, from terra`; `Mark news as read` while any is unread |

The labels carry no counts, so they do not change as Agora works; only `News · 2 new` does, while news is unread. `Review now` goes: Sync now ends with a review, and a review runs every five minutes anyway. `Check for news now` and `Ask after the others now` move inside their submenus.

## The menu bar

The meeting ring alone, with no text beside it. Its marks already say who is missing, whether something needs a look and whether news waits (KI-AGORA-TRY-001); the count moves into line 1, as AGORA-COUNT-PLACE a) proposed. The tooltip and VoiceOver read lines 1 and 2: `Agora. 10 agents on 2 Macs. All well.`

| State | Ring |
| --- | --- |
| All well | Three solid stones |
| Something needs a look | The diamond, top right |
| A Mac not heard from | One hollow stone |
| News waiting | The centre point |
| This Agora not in the square | Every stone hollow |

The ChatGPT illustrator's icons (`identity/chatgpt/`) explore six stones and a diamond inside the ring. The mockup uses the shipped ring; the menu works with whichever is chosen.

## Words

- **Agents and Macs**, as the specification now says (C13): not threads, sessions, computers or rigs. `this Mac` marks the Mac the menu is on.
- **Not heard from**, not "quiet", which is a Knowledge Islands condition word (sound but little visited).
- **Silent** for an agent that has not answered, as the Broadcasts menu already says.
- **Times** are `HH:MM`, 24-hour, local, within the day; a date is added when it is not today.
- No exclamation marks, no emoji. The star `★` is a text mark, not an emoji.

## What changes in the code

`src/wording.ts` gains the line 1 and line 2 forms and the exception rows; `src/main.ts` builds the four blocks. Today's `Computers`, `Checkouts`, `Disagreements`, `Territories` and `Watching` submenus fold into `Agents` and `Macs and checkouts`. The title text beside the ring goes.
