---
note_type: streams/design
status: draft
work: ki.ways-of-working
run: ways-of-working
agent: wow-obs-review-design
written_at: 2026-10-26T22:50:00Z
---

# A review view in the Observatory

**Owner:** Kris Brown - **Work:** `ki.ways-of-working` (KI > Model > Ways of working) - **Date:** 26 October 2026 - **Status:** proposal, nothing built

Kris, 26 October 2026: "I'm just wondering how we can make all this a lot easier on ourselves. Is there a way that we can make use of the observatory a bit better?" and "Yes, I'm happy with the observatory as the place to do it, please." Today the open queries across the work packages are read as long Markdown in each package's `queries.md`, or in a hand-written review pack, and answered in chat for the coordinator to read back into `decisions.md`. This note proposes one place in the Observatory to read every open query and answer it, keeping each coordinator the one writer of its `queries.md` and `decisions.md`.

## What exists to reuse

Most of the view is already there. The Observatory's **Review queue** instrument reads every work package's `queries.md` across the selected scope, takes the tags under `## Open` with one sentence and a `since` day each, leaves parked tags out, checks the decisions logs beside them so an answered tag is not listed, and links each row to its work in the Work instrument; it answers nothing. The **Work** instrument reads `ki work status`, shows each work's description, holder and state, and opens a report in a reader "to comment on" (`packages/evidence/src/review.ts`, `packages/contracts/src/review.ts`, `docs/guides/operator/read-the-instruments.md`).

The answer path exists too. [PDR-KI-OBSERVA-007](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-007-feedback-returns-to-the-producing-work.md) returns the owner's feedback on a document as one package in the producing work's folder plus one `messages.md` line, through the Bridge's `feedback-send` operation: a `mutate` tier, its two files declared on the plan, the plan bound to a digest of the draft, the commit holding exactly those paths with hooks run, both files restored if the commit fails, nothing pushed, and a receipt kept. Drafts live in the Observatory's own XDG state, never the browser. Sending is switched off by `FEEDBACK_SENDING` under [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md), which waits for the harness to admit a `feedback/` kind and name the owner as a sender. The `ki-work-package` standard now lists the feedback package in the closed list and names "the owner, through the Observatory" in its sender table, so that hold condition appears to be met; releasing it is the Observatory coordinator's call, not this note's.

What `queries.md` carries is exactly what the review pack showed Kris found readable: a tag and title, **Context** written to be read cold, **Query** in one sentence, and lettered **Options** with the recommendation first and its confidence and reason. The pack added two things the files do not hold: an "idea in brief" per theme and a worked example. The view cannot invent those; what it can do is lead each group with the work's own description from `work.md`, which `ki work status` already reports, so a group reads cold without a new field.

## The view

Extend the Review queue rather than add an instrument. Its query rows gain a **query reader**, as the Work instrument's report reader, that shows the whole query: tag, title, Context, Query and Options, the recommended option set apart with its confidence and reason in plain words, and a `since` day. Grouping follows the instrument's existing dimensions: by work by default, each group headed by the work's label and description; also by confidence, so the "all recommended" answers Kris gave tonight can be read as one block, and by repository. Parked queries are counted on the group's line and not opened. A query crosses to the browser as a work report does today, through the same typed prose tree, since Context already carries links and quotations.

Beneath the reader sits the answer: the lettered options as buttons, a note field, and **send…**. A letter alone, a note alone, or both.

## The answer path and its authority

An answer is one line in that work's `messages.md`, the one write the sender table allows other parties, in the standard's line shape: `- <date> · <TAG> · Kris, through the Observatory (owner): a) <the option's first words>; <the note>`. The coordinator reads it at its next pick-up, records it as taken in `decisions.md` in Kris's words, asks one line where it is unclear, removes the line, and moves the query out of `## Open`. Nothing else changes hands: the Observatory never writes `queries.md` or `decisions.md`, and the coordinator stays the one writer of both. A note longer than the 60-word line limit takes the existing feedback package shape, linked by the line. If a tag is still open at the next observation, the row says `answer queued` rather than listing it again.

The operation, `query-answer`, is declared like `feedback-send`: `mutate` tier, one file effect, a plan bound to a digest of the query text as read, one confirm per answer, a commit of `messages.md` alone with the subject `docs(work): <id> message from owner`, hooks run, no push, the file restored on failure, a receipt kept. It is refused when the tag is no longer under `## Open`, when `messages.md` carries an uncommitted change, when the query changed since the plan, or when the same tag already has an unacted owner line; the standard lets a sender replace its own line, so a changed answer replaces rather than repeats. Pushing stays the Repositories instrument's governed push, so an answer reaches a coordinator on another machine only when Kris pushes, as feedback does today. Batching several answers under one confirm is out until the gate has batch operations, which BRG-005 left for later.

## Privacy

The Observatory binds the loopback address and keeps its state under the user's XDG directory; the public website carries no work-package content and nothing here changes that. The only other way in planned is the tailnet read-only appearance under [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md), where `query-answer` must be refused like every other operation. Query bodies name local files, as reports do; they cross as reports cross and no answer or plan carries a path in its receipt.

## What would change outside the Observatory

- **ki-agentic-harness, `ki-work-package`:** add the owner's query answer to the sender table beside the feedback package: one `messages.md` line carrying an open tag, with or without a linked package, committed alone. **`ki-coordination`, Answers:** say the owner may answer in speech or by a messages line from the Observatory, read back the same way; the coordinator's wake already acts on `messages.md` in queue order, so an answer given during an unattended window is read within the five-minute wake.
- **tools-ki:** nothing for the first slice; the Observatory already parses `queries.md`. Later, a `ki work queries --format json` contract would let the Observatory consume one reading rather than keep its own parser, and a `ki work answer <id> <TAG> --option a --note "..."` command would make the line's composition one tool's and give the Observatory an argument vector instead of its own file effect, as its contract prefers.

## Smallest first slice

Read the whole query and answer it with a letter or a short note, one at a time, nothing pushed: the query reader on the Review queue's query rows, `query-answer` declared and gated as above, and `answer queued` on an answered tag. It presumes the hold on KI-OBSERVA-BRG-004 is judged met so that the Observatory may write a work folder at all. Out of the slice: theme grouping, batch confirm, the long-note package, the `ki work` contracts, and the tailnet way in.

## Roadmap records it would become

Named here, not created, with serials from today's listing and assigned at capture: `KI-OBSERVA-VIS-046`, the query reader on the Review queue; `KI-OBSERVA-BRG-007`, answering a query as a messages line, built on the released [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md); and later `KI-OBSERVA-INT-005`, consuming the `ki work queries` and `ki work answer` contracts once tools-ki provides them. The harness changes go to the Ways of working work as its own units, and the tools-ki ones as a message to its work, never as records in another repository's roadmap.
