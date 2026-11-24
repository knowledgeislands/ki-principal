---
note_type: pillars/note
updated: 2026-11-24T02:24:09Z
tags:
  - card/note
  - topic/knowledge-islands
status: current - November 2026
author: Written with Claude
---

# D12, the Dodecakrisis

D12, the Dodecakrisis, is the sorting engine for everything that comes in: twelve Ds that say what happens to each delivery, from arrival until it is kept or let go. It sits before the knowledge capture funnel: not everything enters the funnel, and the Dodecakrisis is where things are held back, worked or dropped. Kris made it a fundamental tenet on 5 November 2026.

Origin: Kris's working session on email triage and archiving in the assistant-terra thread, 5 November 2026.

![D12, the Dodecakrisis](<D12 Dodecakrisis.svg>)

## Why

Kris, 5 November 2026, starting from the HNR mailbox's triage and archive folders not matching: email "isn't fit for purpose" as a store. Folders make sense while sorting, but once something leaves the sorting it belongs in a store "which would benefit the most from being a single, probably date-centric structure … heavily tagged and indexed", with path-based tags. "Maybe archive is no longer in either of them."

The model is tested for everything that comes in, not just email: "we're testing this as a model for bringing everything into the system".

## The model

A coin sorter. Everything delivered drops into Do; the sorting rules drop it into a queue by what it looks like; each queue is worked to a conclusion; a concluded item drops back into the sorting rules, until the rules send it out to Deposit or Delete. Along the bottom runs the Docket lane, where action items come out of the sorter so nothing gets lost.

```text
 Deliveries ──► Do ─────────────────────────────────┬──► Deposit ─┐
               sorting rules + automator             │             │ retention ends
               ▼        ▼        ▼  …  ▼             │             ▼
               Determine · Decide · Discuss ·        └──► Delete ◄─┘
               Delegate · Defer · Dormant · Digest
               └── concluded: back to the rules ──┘
 ────────────────────────── Docket: action items ──────────────────────────
```

## Names

- **D12, the Dodecakrisis** (doh-DEK-uh-KREE-sis): the whole system, its twelve Ds and how they fit (Kris, 5 November 2026). Twelve letters, all Greek like dodecahedron: _dodeca_, twelve, and _krisis_ (κρίσις), "a separating, a sorting out, a judgement", from _krinō_, to separate, sort or decide, the root also of criterion and critic. Said with KREE, not KRY, so it is not heard as "crisis".
- **Do:** block 2, the engine itself. It keeps the plain D.
- **Set aside:** "the Dodecahedron", the first working name; and "Dodecafactor", which in software reads as "twelve-factor", after the Twelve-Factor App.

## The twelve Ds

Four blocks in a row, seven queues inside Do, and the Docket lane beneath.

| # | D | Where | What it is |
| --- | --- | --- | --- |
| 1 | **Deliveries** | block | Everything that comes in: email, meetings, chats, links and files, voice and photos, messages. |
| 2 | **Do** | block | The engine. The sorting rules and the automator sit at its top, acting automatically or by hand; its seven queues sit below. |
| 3 | **Determine** | queue | Where does it go? The rules can't place it, so a person does; each one teaches a rule. |
| 4 | **Decide** | queue | I need to do something about this (me). |
| 5 | **Discuss** | queue | We talk it through (us), at the next contact with the person. |
| 6 | **Delegate** | queue | Someone else does something about it (them): fire and forget, or send and wait. |
| 7 | **Defer** | queue | It doesn't need deciding now; it comes back into the rules on a date, when it may be decided or delegated. |
| 8 | **Dormant** | queue | Someday, maybe: no date; it waits until something makes it relevant. |
| 9 | **Digest** | queue | It sits for a time, to be absorbed. This is not the maturation in the knowledge store's funnel, which is a separate system. |
| 10 | **Deposit** | block | Kept for the longer term, with a retention period and an optional reminder. The handoff to the knowledge store. |
| 11 | **Delete** | block | Let go, with a reason: junk, no longer needed, retention ended. |
| 12 | **Docket** | lane | Action items made out of the sorter, so nothing gets lost. A docket item can point at an item in the sorter or in Deposit, and is used to pull it through. |

The queues read in threes: Decide, Discuss and Delegate are me, us and them; Defer, Dormant and Digest are when, if ever, and over time. Determine comes first, because it is where the rules ask for help.

## How deliveries come in

Each source has its own approach, for correctness and consistency across sources; the sources card lists them and says, for each, how it comes in and where its triage sits. Kris set these out on 3 November 2026. Each source comes in one of two ways:

- **Pull:** everything filed or available is brought in on a regular basis, as meetings are.
- **Push:** only what Kris explicitly sends comes in. Email is pushed, since there is far too much of it to pull, and so is anything Kris gives directly in a thread.

**Triage** is the judging of what is worth bringing in and going on. It is not a stage but a filter, and where it sits depends on the source, so each source's approach says where its filters sit. For meetings, it makes sense for Kris to triage before they are brought in, checking the notes and judging each meeting worth bringing in. For Slack or WhatsApp, pulling the information in may come first, with triage then deciding what goes on.

**Fire hoses** are sources that pour in far more than any person could read: X (formerly Twitter), Reddit and social media generally. They need much more diligence about what is let in and what is not, so their filters sit early and are strict.

## Rules

1. **The sorting rules are Do's top.** They place each delivery in a queue, or send it straight to Deposit or Delete. Sorting by hand is the same step done by a person.
2. **The cycle.** Concluded items come off the bottom of the queues and go back through the sorting rules, which place them again or send them out. The loop is the same whether a step was automatic or by hand.
3. **Only the rules send items out.** Deposit and Delete are reached from the sorting rules, never directly from a queue.
4. **Two exits.** Everything ends in Deposit or Delete; nothing stays in Do for good.
5. **Delete carries a reason, not a sub-state.** Junk is not a special case, only a reason, and "junk" is the reason that teaches the rules.
6. **Everything has a timeline.** Defer carries a wake-up time. Deposit carries a retention period; when it ends, the item is pruned to Delete. How long and how well a deposit is kept follows its fidelity, set out in evidential nodes: evidential material is kept word for word for as long as its owner requires, the rest only its gist for a period. A Deposit may carry a reminder without keeping the item in a queue.
7. **Determine teaches.** Every item placed by hand in Determine is a candidate for a new sorting rule, so Determine should shrink over time.
8. **The Docket keeps actions.** A queue's conclusion may make a docket item and, at the same time, send the item itself back through the rules, so the task outlives the email or note it came from.
9. **Deposit is a handoff.** What happens to a deposit next, its capture, curation and dispatch, belongs to the knowledge capture funnel, which starts at Deposit.
10. **The sorter comes before the funnel.** Not everything enters the funnel: the sorter is where things are held back or dropped.

## Prior art

The 4 Ds of email (Do, Delete, Delegate, Defer) are widely published, without a named originator; GTD's processing step, Inbox Zero and the Eisenhower matrix are close relatives. None found has Deposit as an exit to a knowledge store, the sorter-and-queues shape, or the Docket lane.

It is one of the processes of Making Knowledge Durable, on the intake side. Once material is acquired, the [Acquisition Process](<../Acquisition Process/Acquisition Process.md>) describes how it enters an island and is harvested.
