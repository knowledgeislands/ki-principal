# Capture model: brief

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal, work `ki.prj.ways-of-working` · **Date:** 2026-10-31

Stage one of the `ki-work-design` loop for CAPTURE-MODEL, strands 1 and 2, with the succinct-capture rule strand 3 needs. Written by run `w-U12` in the unattended window AWAY-31-OCT under CAPTURE-MODEL, relayed at Kris's request on 30 October: "Kris wants Ways of working to take over improving the capture model now". Acquire was read in place and nothing in it was changed. Revising Acquire's `CAPTURE.md` is strand 3: it is Personal's repository, so it follows this design for Kris's go. Every choice below is left for Kris; the recommendations have not yet had a blind review. Two independent reviews, a merged report and Kris's decisions come next.

## Problem

Acquire preserves what arrives well, but it does not say what Kris means to do with it, it has nowhere to keep that intention open, and it keeps far more than a small capture needs.

1. **Purpose is not recorded as data.** Purpose appears only as prose, in two of the eight intake captures: "consider mode" for the French cleat shelving and "Buy" for the wheel arch clips. Nothing tracks the item afterwards. The clips README says "Purpose: buy; held here in Acquire", but no buy list exists, and dispatch removes a capture from Acquire on delivery with "nothing in Acquire" remembering it. A buy or consider item either sits in Acquire with nobody watching it or leaves with nobody owning the follow-up.
2. **Ideas have no single route.** Ideas arrive as Acquire captures and also gather inside work packages: design notes, parked queries and held packages. The empty-board survey on 31 October found 244 ideas in at least seven kinds of place. Kris has said ideas stay out of the roadmap, but not where a captured idea goes or how it moves on.
3. **Captures are too heavy.** The French cleat capture is a dictated note of 156 words and one photograph, held as `original.txt`, a 207-word `README.md` that largely restates the note, `SHA256SUMS` and the attachment. `CAPTURE.md` requires `original.txt` and a `README.md` for every supplied text and a `SHA256SUMS` entry for every kept original, whatever the size.

## Owner's proposal

The CAPTURE-MODEL line, relayed from `personal.reg.acquire-intake` on 30 October and received in this package's `messages.md` in `45a138b4`, verbatim:

> 2026-10-30 · CAPTURE-MODEL · Personal > Acquire intake (personal.reg.acquire-intake) > Ways of working (ki.prj.ways-of-working): relayed at Kris's request. Kris wants Ways of working to take over improving the capture model now; `ki.prj.knowledge-acquisition` is finished and not needed, and should be cleaned up (see FINISHED-TIDY-KICK). Three strands. (1) Purpose at capture: Acquire is to hold every captured point tagged with a purpose (so far buy, consider and a design digest), with something that manages open items properly; the OneDrive `sources-acquire/+/` intent folders (`act`, `buy`, `explore`, `know`, `read`, `watch`) are one way to supply the purpose, not the mechanism. Source digest: acquire `captures/knowledge-islands/intake/2026-10-30-intent-based-onedrive-acquisition/`. (2) Ideas: ideas stay out of the roadmap; today they sit in work-package folders and also arrive as Acquire captures, so decide where an idea lives and how it moves on. (3) Succinct captures: captures hold far too much detail. For example acquire `captures/personal/intake/2026-10-30-french-cleat-shelving-bedroom/` has `original.txt`, `README.md`, `SHA256SUMS` and an attachment, where a short note beside the photo would do; `original.txt` is not needed in a case like that. Revise `CAPTURE.md` accordingly.

Kris's correction to the OneDrive digest, sent while it was being captured, verbatim as its README records it:

> doesn't have one drive, we capturing should associate metadata "purpose", and one such way put things into onedrive location too

## Established facts

- Acquire holds 398 capture packages: 350 Granola meetings, 35 ChatGPT conversations, 4 Codex sessions, 8 intake captures and 1 voice-notes group - `/Users/krisbrown/workspaces/personal/acquire/captures/`, at `7b6ab6b`.
- `CAPTURE.md` asks for supplied text "unchanged as `original.txt`", a short `README.md` saying "what arrived, when, from which tool, its scope and what is missing", and each kept original copied into `attachments/` and recorded in `SHA256SUMS` - [CAPTURE.md](/Users/krisbrown/workspaces/personal/acquire/CAPTURE.md), Supplied material and Original files.
- `CAPTURE.md` has no purpose field and no open-item step; its goals end at preservation and say "Capture is separate from evaluation, dispatch and source retirement" - [CAPTURE.md](/Users/krisbrown/workspaces/personal/acquire/CAPTURE.md), Goals.
- Dispatch delivers a capture whole into the territory principal's `+/_ACQUIRED/`, "delivery is acceptance", the capture then leaves Acquire, and "Nothing in Acquire needs to remember the delivery"; there is "no manifest, dispatch ID or ledger" - [dispatch](/Users/krisbrown/workspaces/personal/acquire/docs/guides/operator/dispatch.md).
- Purpose already appears in prose: French cleat "consider mode ... Nothing is decided or requested"; wheel arch clips "Buy: Kris asked for the clips to go on the buy list ... held here in Acquire" - the two capture READMEs under `/Users/krisbrown/workspaces/personal/acquire/captures/personal/intake/`.
- The wheel arch capture already shows the lean shape: `README.md` and `original.txt` only, the photographs "seen and deliberately not kept, at Kris's direction" - `/Users/krisbrown/workspaces/personal/acquire/captures/personal/intake/2026-10-30-wheel-arch-moulding-clips/`.
- The OneDrive digest proposes six intent folders and separates source, intent and territory as three dimensions; it says "intent not workflow status", that processing must retain "user intent, resulting artefacts and processing status" and avoid processing an item twice, and that "precise ownership and routing rules remain design decisions" - [original](/Users/krisbrown/workspaces/personal/acquire/captures/knowledge-islands/intake/2026-10-30-intent-based-onedrive-acquisition/original.txt).
- The six folders exist under `OneDrive-Personal/sources-acquire/+/` and were empty at capture; Acquire's tracked configuration declares no OneDrive source store - [README](/Users/krisbrown/workspaces/personal/acquire/captures/knowledge-islands/intake/2026-10-30-intent-based-onedrive-acquisition/README.md).
- The Acquire intake package still names `ki.prj.knowledge-acquisition` as owner of "accepted acquisition method and rationale"; Kris has since said that Project is finished, and its tidy is FINISHED-TIDY-KICK, unit U8 - [work](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/personal.reg.acquire-intake/work.md) and its decisions, PURPOSE-METADATA.
- The roadmap standard says "An idea has no identifier, horizon, or status, and never owns state", places a concept in its Capital's Emerging Concepts note and other ideas outside the record queue - [Ideas and graduation](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-repository-roadmaps.md#ideas-and-graduation).
- The empty-board design, drafted on 31 October for Kris's review, counts ideas in seven kinds of place, proposes Ideas, Upcoming and Active columns with gates, and asks IDEAS-HOME, where every idea in the Knowledge Islands territory should live, and PARKED-TO-IDEAS; both are open - [empty board](../empty-board/design.md).

## Reflection

1. Purpose is one metadata field on the capture, set at capture time, not a location. The OneDrive folders, a word in Kris's note and a question from the capturer are all just ways of supplying it, as Kris's correction says.
2. The field belongs in the capture's own `README.md` front matter, so it travels whole at dispatch and needs no ledger, with `purpose`, `territory` and `captured` as its keys.
3. The purpose words should be the ones Kris actually says at capture, since capture is conversational: `consider` rather than the digest's `explore`, and `design` for material meant as input to a design, beside `act`, `buy`, `know`, `read` and `watch`. That is seven words, a closed list, extended only by Kris.
4. Purpose is required for every new intake capture. Where Kris gives none, the capturer asks once; meeting, conversation and session routes default to `know`. The 398 existing captures are not backfilled.
5. Purpose is intent, not status. Status lives in one open-items list in Acquire, not in the capture, so the capture's bytes never change after it is committed.
6. Every purpose except `know` opens an item: `act`, `buy`, `consider`, `design`, `read` and `watch` each add one line to the open-items list, holding purpose, title, territory, date, link and state (`open`, `done` or `dropped`). A `know` capture opens nothing and dispatches as today.
7. An open item's capture stays in Acquire until the item is closed, which changes the dispatch rule: dispatch skips open items, and a closed item either dispatches as today or, on Kris's word, is removed.
8. Kris closes items, and Kris reviews the list on a regular beat, perhaps weekly; an item untouched for 90 days is offered for dropping, matching the ageing the empty-board design proposes.
9. A captured idea is an open `consider` item and nothing more; Acquire is its intake queue, not its home. At review Kris turns it into work in its owning package, moves it to its territory's ideas home, or drops it. Never the roadmap.
10. Where an idea lives is IDEAS-HOME's question, already open; this design depends on it and does not answer it. Whatever IDEAS-HOME settles for Knowledge Islands should take the same shape in each other territory's principal, because many captured ideas are personal, like the bedroom shelves.
11. Ideas inside work packages, in design notes, parked queries and held packages, leave the package for the same ideas home at its next mark, the route PARKED-TO-IDEAS proposes for parked queries.
12. A capture should be as small as its knowledge allows. A short note in Kris's own words goes verbatim into `README.md` beneath the front matter, with no `original.txt`; `original.txt` stays for long or structured text, or text another tool or author produced, where its exact form matters: digests, transcripts and exports.
13. The README holds no restatement of the note or the photograph, only a one-line source, the note, and one line per attachment; it describes a photograph in words only when the photograph is not kept.
14. `SHA256SUMS` adds nothing Git does not already prove for a single intake attachment, since Git hashes every committed byte and dispatch already checks tree identifiers. It can go for intake captures; route guides that rely on it keep it.
15. The OneDrive intent folders wait until purpose and the open-items list work from conversational intake. Adopting them needs a declared source store and a rule for moving files out of the folders, which is source retirement, a separate authority.
16. Method ownership for capture moves from the finished `ki.prj.knowledge-acquisition` to Ways of working; the Acquire intake package's Out line should be updated to say so when FINISHED-TIDY-KICK runs.

## Worked example

The French cleat capture under rules 2, 12, 13 and 14, as one `README.md` beside the photograph:

```markdown
---
purpose: consider
territory: personal
captured: 2026-10-30
---

# French cleat shelving for the bedroom

Dictated in Acquire intake, Orca on terra.

> This is something that I saw in the Cycle Cafe at the Cycle Heaven on Hospital Fields Road ... the idea here is just for me to put into a sort of consider mode about ideas for my bedroom.

- [01-3.jpg](attachments/01-3.jpg): the cafe's cleats and locking block. A wider view was dropped at Kris's direction.
```

The note is quoted in full in practice; it is shortened here only to fit the example. The capture opens one line in Acquire's open-items list: `consider · French cleat shelving for the bedroom · personal · 2026-10-30 · open`.

## Proposed succinct-capture rule

Draft wording for strand 3's revision of `CAPTURE.md`, Supplied material, for Kris's go:

> Keep a capture as small as its knowledge allows. Give every intake capture a `README.md` whose front matter carries `purpose`, `territory` and `captured`. A short note in Kris's own words goes verbatim into the README beneath a one-line source; keep it separately as `original.txt` only when it is long or structured, or when another tool or author produced it and its exact form matters. List each kept attachment in one line and do not restate what the note or the attachment already says. Describe a photograph in words only when it is not kept.

## Rollout sketch

Not decided; shown so the reviews can test the order.

1. Strand 3, Acquire: revise `CAPTURE.md` with purpose front matter and the succinct-capture rule, and add the open-items list seeded with the two 30 October items. Acquire's change, on Kris's go.
2. Dispatch, Acquire: skip open items.
3. Ideas: once IDEAS-HOME is answered, the review route from `consider` to the ideas home, and the same shape in each other territory's principal.
4. OneDrive intent folders: later, as a declared source store with its own retirement rule.

## Choices for Kris

None of these has had a blind review yet.

### PURPOSE-WORDS - Which words name a capture's purpose?

**Context:** Kris has used "buy", "consider" and "a design digest" so far. The OneDrive digest proposes `act`, `buy`, `explore`, `know`, `read` and `watch`, and the empty folders already carry those names. Capture is conversational, so the words Kris says are the ones a capturer will hear. A closed list keeps the open-items list sortable; a free word does not.

**Query:** Which closed list of purpose words should a capture use?

**Options:**

a) (recommended, confidence medium - it uses the words Kris has actually said, but it is tested on only three captures) Seven words: `act`, `buy`, `consider`, `design`, `know`, `read` and `watch`, with `consider` replacing the digest's `explore` and `design` added for material meant as input to a design; Kris alone extends the list.

b) The digest's six words unchanged, with Kris's "consider" read as `explore` and "design digest" read as `know`.

c) A free purpose word, with no closed list.

### PURPOSE-WHEN - Must every capture carry a purpose?

**Context:** Kris asked for "every captured point tagged with a purpose". Intake captures are conversational, so the capturer can ask. Granola meetings, ChatGPT conversations and Codex sessions arrive in bulk, where asking each time would be friction. There are 398 existing captures with no purpose field.

**Query:** When is a purpose required, and what happens to captures already held?

**Options:**

a) (recommended, confidence medium - it meets Kris's "every captured point" without adding friction to bulk routes) Required for every new intake capture, with the capturer asking once when Kris gives none; meeting, conversation and session routes default to `know`; existing captures are not backfilled except the two 30 October items, which seed the open-items list.

b) Required on every route with no default, asked each time.

c) Optional everywhere, recorded only when Kris states one.

### OPEN-ITEMS - How are open purpose items managed?

**Context:** A buy or consider item needs following up, but today dispatch removes a capture from Acquire with nothing remembering it, and the "buy list" the clips README mentions does not exist. Kris said Acquire "is to hold every captured point tagged with a purpose, with something that manages open items properly".

**Query:** Where are open purpose items kept, and how do they close?

**Options:**

a) (recommended, confidence medium - it follows Kris's words that Acquire holds them, but it changes the dispatch rule that a delivered capture leaves at once) One open-items list in Acquire, one line per capture whose purpose is anything but `know`, with state `open`, `done` or `dropped`; the capture stays in Acquire while its item is open; Kris closes items at a regular review, perhaps weekly, and an item untouched for 90 days is offered for dropping; a closed item then dispatches as today or, on Kris's word, is removed.

b) Dispatch as today, carrying the purpose to the territory's principal, where each island keeps its own open lists such as a buy list.

c) The purpose field only, with no list, and Kris searching Acquire by purpose when wanted.

### IDEA-ROUTE - How does a captured idea move on?

**Context:** Ideas stay out of the roadmap. They arrive as Acquire captures and also gather in work packages as design notes, parked queries and held packages. Where an idea finally lives is IDEAS-HOME in the empty-board design, still open; this query is only about the route. Many captured ideas are personal, like the bedroom shelves, not Knowledge Islands work.

**Query:** How should a captured or package-held idea reach its home?

**Options:**

a) (recommended, confidence medium - it fits the empty-board direction and keeps ideas out of the roadmap, but its destination waits on IDEAS-HOME) A captured idea is an open `consider` item in Acquire until Kris's review turns it into work in its owning package, moves it to its territory's ideas home or drops it; ideas in a work package move to the same home at the package's next mark; each territory's principal keeps the same shape of ideas home that IDEAS-HOME settles for Knowledge Islands.

b) Acquire's open-items list is the single home for every idea in every territory, and work packages send their ideas there.

c) Ideas stay where they arise, with a consolidated list generated on demand.

### LEAN-CAPTURE - Adopt the succinct-capture rule?

**Context:** Kris said captures hold "far too much detail" and that for the French cleat capture "a short note beside the photo would do; `original.txt` is not needed in a case like that". The draft rule above puts a short note of Kris's own verbatim in the README, keeps `original.txt` only for long, structured or other-authored text, and stops the README restating the note or the photograph.

**Query:** Should strand 3 write the succinct-capture rule into `CAPTURE.md` as drafted?

**Options:**

a) (recommended, confidence high - it carries out Kris's own words on the example Kris gave) Yes, as drafted under Proposed succinct-capture rule.

b) Keep `original.txt` always, and only shorten the README.

### CHECKSUMS - Drop SHA256SUMS for intake captures?

**Context:** Kris listed `SHA256SUMS` among the excess in the French cleat capture. `CAPTURE.md` asks for one wherever an original is kept. Git already hashes every committed byte, and dispatch verifies a delivery by comparing Git tree identifiers. Other route guides may rely on the file and have not been checked.

**Query:** Should intake captures stop writing `SHA256SUMS`?

**Options:**

a) (recommended, confidence medium - Git already proves the bytes, but the other route guides' use of the file has not been checked) Yes for intake captures; each route guide keeps or drops it on its own terms.

b) Keep `SHA256SUMS` wherever an original is kept, as now.

### ONEDRIVE-LATER - When do the OneDrive intent folders come in?

**Context:** Kris's correction makes the folders "one such way" to supply purpose, not the mechanism. They are empty. Using them needs Acquire to declare a OneDrive source store in tracked configuration and a rule for moving files out once captured, which is source retirement, a separate authority.

**Query:** Should the OneDrive intent folders wait until purpose and the open-items list work from conversational intake?

**Options:**

a) (recommended, confidence medium - nothing is lost by waiting while the folders are empty, but it delays phone capture Kris may want soon) Yes: adopt them later as a declared source store with its own retirement rule, mapping each folder to a purpose word.

b) Adopt them now, alongside strand 3.
