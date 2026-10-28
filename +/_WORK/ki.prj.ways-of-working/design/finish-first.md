---
note_type: streams/design
updated: 2026-10-20T03:30:00Z
author: Written with Claude
---

# Finish first

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-20

Design note for FINISH-FIRST. Kris asked at 02:38 BST on 20 October: "how do we make it so that we get work finished before we start creating more work in the roadmap items? You know we need to see roadmaps going down, not going up like they are." The read-back taken in the [decisions log](../decisions.md) asks for a burn-down rule set, designed and reviewed before it reaches Kris: counts per repository tracked at each mark and shown by State of play, no new records beyond CAPTURE-GATE's exceptions, a work adopts new Now work only while its Now and awaiting-review counts are under a cap (with OWNER-QUEUE), and done records pruned promptly.

This note measures the last fourteen days from Git, names the causes of growth, and proposes eight rules, each with its owner and its check. It applies nothing and creates no record. It graduates when Kris has answered its queries and each accepted rule is written into its owning standard by wow-standards or a successor run; it is then deleted in the same change.

## Contents

- [Findings in brief](#findings-in-brief)
- [Method](#method)
- [Measurements](#measurements)
- [Where new records come from](#where-new-records-come-from)
- [The current rules](#the-current-rules)
- [Causes of growth](#causes-of-growth)
- [Rule set](#rule-set)
- [Queries for Kris](#queries-for-kris)

## Findings in brief

1. Open records across the estate rose from 198 on 13 October to 330 on 20 October, up 67% in a week. The week before, under the earlier burn-down focus, they fell from 202 on 6 October to 175 on 12 October.
2. Closing is not slow: 180 records were accepted and 32 cancelled in the week from 13 October, and 419 terminal records were pruned in the fortnight. Creation outran it: 370 new records in the same week, against 168 the week before.
3. Two queues hold the growth. Triage rose from 30 to 106 records and awaiting-review from 13 to 55. Awaiting-review is Kris's acceptance queue; it is the bottleneck in the delivery chain.
4. Most new records do not come from a run noticing a defect. They come from fan-out: one design, decision or sweep becomes records in several repositories (102 records), bulk imports (56 records in five commits), records opened for work as it was done (97), and query answers whose recommended option was "capture a record" (85 cite a Kris decision).
5. CAPTURE-GATE, set on 19 October, lives only in briefs and decisions logs. No harness skill carries it, and `ki-next` still tells every session to capture triage "without prior approval". Twenty-seven records were created after the gate, 21 of them by the ki.baseline-rollout sweep under a blanket approval and by Kris answers that the captures cite.
6. The old backlog does not move: 39 Future drafts have a median of 51 days since update, 21 of them in er-agentic-harness, untouched in the window.

## Method

Read-only, local checkouts at `HEAD`, no fetch. Every repository under `/Users/krisbrown/workspaces` with `docs/roadmap/` or `Streams/Roadmap/` and its own `.git` directory: 50 repositories, 36 holding records in the window. Worktrees such as `ki-agentic-harness-ci-green` are excluded; `personal/dotfiles` is a symlink to the chezmoi source and is counted once.

- **Daily counts:** for each day from 6 to 20 October, the last first-parent commit before 23:59:59 local time, its roadmap tree listed with `git ls-tree` and each record's `status` and `horizon` read from front matter. Index files (`_ISSUES.md`, `_IDEAS.md`, `Roadmap.md`) are excluded.
- **Events:** `git log --no-merges --no-renames --name-status` over each roadmap directory since 6 October. An added record is _created_; a deleted one is _pruned_, with its last status read from the parent commit; a status change to `done` or `cancelled` is _closed_. A deletion of an open record paired with an addition in the same commit is a _re-key_ (identity adoption, renumbering or retitling); 141 such pairs are excluded from the new-record count. Two unpaired open deletions remain.
- **Sources:** each new record is classed by its creating commit subject and its `## Context` text: created already at `ready` or later is _opened for delivery_; a split, fold or merge is _split_; a handoff, routing, trade, sweep or estate-wide wording is _handoff or sweep_; a retro, finding, follow-up or "seen failing" wording is _run finding_; a Context citing Kris is _cites Kris_; the rest is _other capture_. The classes are heuristic. A sample of 16 read by hand showed _cites Kris_ includes many records whose capture Kris approved as an agent's recommended option rather than asked for, and _other capture_ includes some owner goals. Read the split as indicative, within about ten records per class.

The scripts and their JSON output were kept in the run's temporary folder and are not homed; every figure below can be recomputed from Git history.

## Measurements

### Estate, by day

Open is every record not `done` or `cancelled`. Retained is `done` or `cancelled` not yet pruned. New excludes re-keys.

| Date | Open | Triage | Draft and ready | In progress | Awaiting review | Retained | New | Done | Cancelled | Pruned |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 06 Oct | 202 | 0 | 188 | 13 | 1 | 2 | 13 | 35 | 0 | 35 |
| 07 Oct | 179 | 9 | 150 | 13 | 7 | 2 | 47 | 36 | 37 | 73 |
| 08 Oct | 183 | 31 | 137 | 12 | 3 | 7 | 36 | 31 | 0 | 26 |
| 09 Oct | 171 | 21 | 137 | 12 | 1 | 1 | 17 | 16 | 13 | 35 |
| 10 Oct | 184 | 27 | 135 | 12 | 10 | 3 | 17 | 3 | 1 | 2 |
| 11 Oct | 175 | 33 | 120 | 12 | 10 | 10 | 24 | 19 | 14 | 26 |
| 12 Oct | 175 | 18 | 136 | 12 | 9 | 10 | 14 | 8 | 4 | 14 |
| 13 Oct | 198 | 30 | 143 | 12 | 13 | 17 | 30 | 7 | 0 | 0 |
| 14 Oct | 202 | 30 | 145 | 15 | 12 | 12 | 42 | 22 | 14 | 41 |
| 15 Oct | 222 | 34 | 147 | 15 | 26 | 7 | 23 | 2 | 2 | 9 |
| 16 Oct | 239 | 38 | 150 | 15 | 36 | 6 | 49 | 28 | 0 | 29 |
| 17 Oct | 264 | 48 | 156 | 15 | 45 | 7 | 33 | 8 | 0 | 7 |
| 18 Oct | 301 | 64 | 182 | 16 | 39 | 15 | 95 | 59 | 2 | 54 |
| 19 Oct | 319 | 108 | 165 | 17 | 29 | 18 | 77 | 44 | 14 | 56 |
| 20 Oct | 330 | 106 | 151 | 18 | 55 | 16 | 21 | 10 | 0 | 12 |

Week from 6 to 12 October: 168 new, 217 closed (148 done, 69 cancelled). Week from 13 to 20 October: 370 new, 212 closed (180 done, 32 cancelled). The 18 October spike follows the work-model launch, when many works began running at once.

### Repositories that grew, 13 to 20 October

| Repository | Open 06 Oct | Open 13 Oct | Open 20 Oct | Change since 13 Oct | New in 14 days | Done | Cancelled | Triage now | Awaiting review now |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| apps-observatory.local | 0 | 1 | 22 | +21 | 45 | 13 | 9 | 0 | 9 |
| ki-agentic-harness | 30 | 9 | 25 | +16 | 96 | 86 | 27 | 11 | 2 |
| dotfiles (chezmoi) | 10 | 9 | 21 | +12 | 34 | 15 | 10 | 1 | 4 |
| ki-design | 0 | 0 | 10 | +10 | 25 | 15 | 0 | 0 | 6 |
| mcp-m365 | 0 | 0 | 10 | +10 | 13 | 3 | 0 | 0 | 0 |
| tools-ki | 1 | 4 | 14 | +10 | 64 | 47 | 3 | 0 | 0 |
| tools-rig | 0 | 5 | 15 | +10 | 35 | 18 | 2 | 2 | 5 |
| hnr-principal | 13 | 16 | 24 | +8 | 12 | 0 | 1 | 14 | 5 |
| apps-tower.midnight.ninja | 0 | 4 | 10 | +6 | 24 | 14 | 0 | 1 | 8 |
| 5g-emerge-phase2 | 5 | 5 | 10 | +5 | 5 | 1 | 0 | 2 | 4 |
| legal-principal | 19 | 25 | 30 | +5 | 11 | 0 | 0 | 8 | 5 |
| personal-principal | 29 | 31 | 36 | +5 | 13 | 4 | 1 | 28 | 0 |
| apps-vallearmonia.com | 8 | 14 | 17 | +3 | 10 | 0 | 1 | 3 | 2 |

Nine more repositories grew by one or two. Two fell: ki-principal (5 to 4) and ki-techne-harness (5 to 2). er-agentic-harness holds 22 open drafts, unchanged and untouched in the window. apps-tower.midnight.ninja retains 13 `done` records not yet pruned.

### The open queues now

| Status and horizon | Records | Median days since `updated_at` | Largest holders |
| --- | ---: | ---: | --- |
| triage | 106 | 0 | personal-principal 28, hnr-principal 14, ki-agentic-harness 11 |
| awaiting-review | 55 | 0 | apps-observatory.local 9, apps-tower.midnight.ninja 8, ki-design 6 |
| draft, hold | 42 | 0 | apps-observatory.local 10, mcp-m365 10, apps-vallearmonia.com 5 |
| draft, future | 39 | 51 | er-agentic-harness 21, er-principal 5, personal-principal 5 |
| draft, next | 32 | 0 | dotfiles 7, legal-principal 5 |
| draft, now | 19 | 0 | ki-agentic-harness 6 |
| in-progress | 18 | 8 | legal-principal 6, tools-ki 3 |
| draft, soon | 17 | 0 | tools-ki 8, legal-principal 3 |
| ready | 2 | 8 | |

Median zero means most records in the queue were touched today, chiefly by the TRIAGE-ALL and burn passes, not that they are new.

## Where new records come from

Of 370 new records from 13 to 20 October, created at `triage` 197, `draft` 76, `ready` 43, `in-progress` 19, `awaiting-review` 31 and `done` 4.

| Source (heuristic) | Records | Examples, by repository and creating commit |
| --- | ---: | --- |
| Handoff or sweep | 102 | ki-design `2ada5be` (15 Observatory hand-off drafts); apps-observatory.local `87fab2c` (18, "plan the ki-design handoff in four steps"); Archify redraw of Mermaid in seven repositories (er-principal `12f3fc5`, hnr-principal `bd6a334`, personal-principal `3cb2402e`, legal-principal `ebabe3ed`, ki-specifications `e39fab5`, apps-vallearmonia.com `64ee877`, apps-tower.midnight.ninja `9e396bd`); fatal Bats assertions in three (ki-agentic-harness `1d7c2895`, tools-rig `9752f68`, tools-mgit `c76b4d5`); portable-specification homings ki-agentic-harness `871e98ea` (3) |
| Opened for delivery | 97 | tools-ki `1311057d` ("capture and plan KI-TOOL-KI-CLI-153 to Ready"); apps-tower.midnight.ninja `7a1d9df` (3 at `ready`); ki-agentic-harness `8061c13e` (opened at `in-progress`) |
| Cites Kris | 85 | GIT-HOOKS answer: ki-agentic-harness `8c5b5575`, tools-ki `5158a927` (2); ki.baseline-rollout under "Anything high confidence can be done": er-principal `497c7d9`, hnr-principal `3d162b1` (2), legal-principal `7bec4bcc`, personal-principal `64387631`, tmx-principal `2de973a` (2), va-principal `0c54498` (2) |
| Other capture | 55 | ki-design `fdecadc` (10 drafts with the design-system import); mcp-m365 `e401aa3` (8 email-routing triage) and `1b597b4` (5) |
| Run finding | 22 | apps-observatory.local `5209851` (browser smoke check seen failing on `main`); tools-rig `1506d47` (doctor findings from sol) |
| Split or merge | 9 | dotfiles `e939158`; tools-rig `1eac12d` |

Five commits with five or more records each created 56 records. Twenty-seven records were created after CAPTURE-GATE at 23:45 BST on 19 October. Twelve are ki.baseline-rollout conformance-warning records in nine repositories (including 5g-emerge-apex `e5cb5f4`, 5g-emerge-demos `816559b` and 5g-emerge-testbed `4a0a16a`), captured under Kris's blanket "Anything high confidence can be done" (its [decisions log](../../ki.baseline-rollout/decisions.md), 23:59 BST), though CAPTURE-GATE says small audit fixes need no record. Nine cite a Kris decision (GIT-HOOKS three, BANNER-GLYPHS, STORAGE-OWNER, KNIP-HUSKY, TECHNE-FOCUS, and two Acquire intake decisions). Three are ki.portable-specifications plan homings, one (`5209851`) is a defect seen failing, one is a split and one a Sanctuary style-token guard.

## The current rules

- **CAPTURE-GATE a)** (Kris, 19 October, [ki decisions](../../ki/decisions.md)): runs never create records; the owning work's coordinator captures only a blocker, a defect seen failing or a Kris request; ideas go to Project notes; small audit fixes need no record. It is carried in briefs only. A search of `ki-agentic-harness/skills` finds it in no skill; the queued HOMELESS-STANDING run is to write it into `ki-next` and `ki-delegation`.
- **ROADMAP-CAP** (Kris, 19 October, same log): "apart from the roadmap cap, I don't think we need one, I just think we need to focus on what we're doing now, which is to get through it." No cap and no weekly cap measure.
- **BURN-WAVE-1 a)** (Kris, 19 October): each lane runs one `ki-accept` pass and brings Kris its cancel, merge and idea list as one query. It is one pass, not a cadence.
- **TRIAGE-ALL** (Kris, 19 October): every lane triages all its triage records; high-confidence adoptions go to Now and are delivered; the rest come to Kris. It moves triage into Now and so into awaiting-review.
- **OWNER-QUEUE a)** (Kris, 20 October 02:36 BST, [this work's decisions](../decisions.md)): the `ki-coordination` audit counts each work's records awaiting acceptance and open queries and warns over about eight; the banner shows the count; acceptance fixes and backlog-clearing work stay allowed over the cap. It goes into wow-standards and is not yet written.
- **`ki-next`** ([next-work standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-next/references/standards-next-work.md), section 3): capture a substantive outcome once it passes the graduation test, "Do not require prior approval", as `status: triage`; adoption needs explicit human approval; cancellation routes to `ki-accept`; it may recommend pruning but never deletes.
- **`ki-work-roadmap`** ([repository roadmap standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-repository-roadmaps.md)): triage may be captured without prior approval; the graduation test admits a record when it is actionable, a decision, or "must survive the session: it is deferred, delegated, multi-step, or reviewed by someone else"; ideas that do not graduate go to Project or theme `## Notes`, otherwise `_IDEAS.md`; "Views may report the Now count as a signal; there is no cap." The record threshold opens a record only for a product or standard change needing acceptance.
- **`ki-accept`** ([acceptance standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-accept/references/standards-acceptance.md)): closure needs explicit human approval; "a standing human grant counts only when quoted with its source and it covers the exact record"; pruning selected terminal records is sanctioned and needs no second confirmation.
- **Tools:** `ki` 0.12.0 has `ki repo roadmap summary` (current counts by repository, Project, theme or area), `stats` (age and inactivity) and `prune` (non-KB sweep). It has no history command; the 14 October [roadmap sizing and burn-down note](roadmap-sizing-and-burn-down.md) designed one, not yet built.

## Causes of growth

1. **Capture is on by default in the standard.** `ki-next` and the roadmap standard tell every session to capture without approval, and the graduation test's third limb, "must survive the session", admits almost anything a run notices. CAPTURE-GATE reverses this only where a brief repeats it.
2. **Fan-out turns one idea into many records.** An estate sweep or a design handoff writes a record in every repository it touches: seven Archify records, three Bats records, twelve baseline-rollout records, 33 records across ki-design and the Observatory for one handoff. ki-principal's AGENTS.md lets seven repositories add a concrete handoff item to one another's roadmap, and five of them (ki-principal, ki-specifications, apps-knowledgeislands.info, ki-techne-harness, tools-techne) carry a cross-repository choreography section saying so.
3. **Query options default to "capture a record".** Coordinators offer a captured record as the recommended outcome, and a blanket answer such as "Anything high confidence can be done" then authorises many records at once. CAPTURE-GATE's "Kris request" exception lets these through.
4. **Parallel works multiply intake.** Fourteen work packages sit under `+/_WORK/ki.*` in ki-principal, and each lane triages and adopts for itself. TRIAGE-ALL sends high-confidence triage to Now, so delivery fills awaiting-review faster than Kris can accept.
5. **Acceptance is the bottleneck.** Every closure waits for Kris. Awaiting-review rose from 1 to 55 in fourteen days while delivery kept running.
6. **Records opened for operational work.** 97 records were created already at `ready` or later. Some are product or standard changes that rightly need acceptance; others are operational work that the record threshold says needs no record, and each adds to the acceptance queue.
7. **Old backlog is never re-decided.** Future drafts sit for weeks with no prompt to cancel, so the count has no floor that falls by itself.

Pruning is not a cause: terminal records are pruned within a day or two except in apps-tower.midnight.ninja.

## Rule set

Eight rules. The first four stop growth; the next three make counts fall; the last makes the trend visible. Each names its owner and its check.

### R1 - Capture gate in the standard

Only a coordinator captures, and only a blocker, a defect seen failing, or a record Kris names in his own words. A run's finding goes into its report's Outstanding concerns; at receive the coordinator homes it as an `Idea:` bullet in the Project note, a line in the work's `queries.md`, or, under SMALL-FIXES, a direct fix with no record. The graduation test's "must survive the session" limb stops admitting capture by itself. Every record captured after the change carries `origin: blocker | defect | owner` and an `origin_ref` link to the report, failing check or decision line that justifies it.

- **Owner:** `ki-work-roadmap` (graduation test, `origin` fields in the work-item format), `ki-next` (capture procedure), `ki-delegation` (the brief footer line), `tools-ki` (the work-item model reads the fields).
- **Check:** the `ki-work-roadmap` rubric warns on a `triage` record created after the effective date with no `origin` or an unresolved `origin_ref`; State of play's count line shows new records by origin each mark.

### R2 - One record per sweep, messages for handoffs

An estate sweep opens one record, in the repository that owns the change, listing the repositories it will touch; one run delivers it. A cross-repository handoff lands as a line in the receiving work's `messages.md`, not as a record; the receiver's coordinator captures only under R1. A design handoff between two products, such as ki-design to the Observatory, lands as one record per product, its steps inside the record.

- **Owner:** `ki-work-roadmap` (handoff section), `ki-coordination` (messages between work), the cross-repository choreography sections in the AGENTS.md of ki-principal, ki-specifications, apps-knowledgeislands.info, ki-techne-harness and tools-techne, `ki-trades` where a trade route exists.
- **Check:** R1's rubric warning catches a handoff record, because `handoff` is not an allowed origin; the `ki-coordination` rubric flags a commit that adds records in more than one repository for the same sweep.

### R3 - Query options do not create records by default

A query's recommended option prefers, in order: do it now (under SMALL-FIXES, no record), add to an existing record, an `Idea:` bullet, and only then a new record, named by its title. A blanket answer ("all as recommended", "anything high confidence") never authorises a new record; it authorises only options that create none.

- **Owner:** `ki-coordination` (query and read-back rules).
- **Check:** at read-back the coordinator lists each record an answer would create and asks one line where the answer did not name it; R1's `origin_ref` must point at a decision line that names the record.

### R4 - Finish before adopting

A work adopts or starts new Now work only while its in-flight count is under the cap. The in-flight count is the work's records at Now (`draft`, `ready` or `in-progress`), plus its `awaiting-review` records, plus its open queries. Over the cap, the work may only accept, cancel, merge, prune, deliver work already in progress and fix its own blockers. This joins FINISH-FIRST's read-back to OWNER-QUEUE so that the threshold and the count are the same. A record belongs to a work through its `project` field matching the work's Project.

- **Owner:** `ki-coordination` (the rule, the banner count, the audit), `ki-next` (adoption to Now refuses over the cap), `ki-work-roadmap` (amend "there is no cap" to defer to the coordinating standard's per-work cap), `tools-ki` (`ki work status` shows the count).
- **Check:** the `ki-coordination` audit counts per work and fails over the cap where an adoption to Now landed after the cap was reached; the banner counts line shows it every report.

### R5 - Acceptance in one answer per work

At each handoff to Kris, a work brings every `awaiting-review` record in one ACCEPT query, oldest first, each line naming the record, its outcome and any concern; Kris answers once ("accept all", "all but X"). The decisions log quotes the answer with its source and lists the exact records, which is the standing grant `ki-accept` already recognises. Then one `ki-accept` run closes them and prunes in the next prune-only commit.

- **Owner:** `ki-coordination` (query form), `ki-accept` (closure from a quoted grant listing exact records).
- **Check:** the `ki-coordination` audit warns on an `awaiting-review` record older than three days whose work has sent to Kris since without an ACCEPT query listing it.

### R6 - Prune at each mark

At each mark, the coordinator prunes its work's `done` and `cancelled` records in a prune-only commit, after the reference preflight. Nothing waits for a weekly sweep.

- **Owner:** `ki-accept` (procedure), `ki-coordination` (mark checklist), `ki repo roadmap prune` for non-KB repositories.
- **Check:** the `ki-work-roadmap` rubric warns on a terminal record whose terminal commit is more than seven days old.

### R7 - Re-decide old backlog

Once a week, State of play puts to Kris one CANCEL-OR-KEEP query per repository listing every `draft` at Future, Soon or Hold not updated for 30 days. The recommended option is cancel as `obsolete`, with the record's idea kept as an `Idea:` bullet in its Project note; keep moves it, with a fresh `updated_at`. Today this would list 39 Future drafts, 21 of them in er-agentic-harness.

- **Owner:** `ki-work-roadmap` (staleness rule), `ki-coordination` (State of play weekly form), `ki repo roadmap stats` (already reports inactivity).
- **Check:** `ki repo roadmap stats` lists records past 30 days; the State of play audit warns when a week passes without the query for a repository that has them.

### R8 - Counts at every mark

At each mark, State of play records one line per repository in its `state.md`: open, triage, awaiting-review, new since the last mark, closed since the last mark, read from `ki repo roadmap summary`, and shows the change since the last mark and since a week ago in its Summary. Git keeps the history; the tracked daily snapshot and the Observatory chart in the [14 October note](roadmap-sizing-and-burn-down.md) remain the later step. A repository whose open count rose over the week gets one burn query from its owning work: its cancel, merge and idea list, as BURN-WAVE-1 did once.

- **Owner:** `ki-coordination` (State of play report), `tools-ki` (`ki repo roadmap summary`, later a history read built on `readWorkItemsAtCommit`).
- **Check:** the `ki-coordination` rubric flags a State of play mark without the counts line; the trend is visible to Kris in every State of play Summary.

### Where ideas go

Ideas never become records by default. In order: an `Idea:` bullet in the owning Project note's `## Notes`; the theme page's `## Notes` when no Project fits; `_IDEAS.md` otherwise. A run's ideas reach those homes only through the coordinator at receive. This is the existing `ki-work-roadmap` rule; R1 and R3 make it the default path rather than the fallback.

## Queries for Kris

Each query here is medium confidence and, under BLIND-REVIEW, goes to one blind review before it reaches Kris.

### NET-DOWN - A weekly direction target, not a cap

**Context:** ROADMAP-CAP (19 October) set no roadmap cap and no weekly cap measure. On 20 October Kris asked to "see roadmaps going down". A weekly target asks each repository's open count to fall week on week; it is a direction measure, not a limit on size, but it reopens part of ROADMAP-CAP.

**Query:** Should each repository's open count be expected to fall week on week, with a burn query when it does not?

**Options:** a) (recommended, confidence medium - it answers "going down" without a size cap, but it narrows ROADMAP-CAP's "no weekly measure") Show the week-on-week change per repository at every State of play mark (R8); a repository that grew over the week gets one burn query from its owning work; no adoption block. b) Show the counts only, with no target or burn query. c) A hard rule: no adoption to Now in a repository whose open count grew over the past week.

### WIP-CAP - The per-work cap and what it counts

**Context:** FINISH-FIRST's read-back caps a work's Now and awaiting-review counts; OWNER-QUEUE warns over about eight awaiting acceptance and open queries per work. The roadmap standard says of Now, "there is no cap", so R4 amends it. Today apps-observatory.local alone holds 9 awaiting-review records and 11 at Now or awaiting review.

**Query:** What should the per-work cap count, and at what number?

**Options:** a) (recommended, confidence medium - one number is easier to see and check, and eight matches OWNER-QUEUE) One count per work, records at Now plus awaiting-review plus open queries, capped at eight; over it the work only accepts, cancels, merges, prunes, finishes in-progress work and fixes blockers (R4). b) Two caps: at most three records in progress per work, and OWNER-QUEUE's eight for awaiting-review and open queries. c) No cap; the banner shows the count only.

### CAPTURE-ORIGIN - Home CAPTURE-GATE with an origin field

**Context:** CAPTURE-GATE is in briefs only; `ki-next` still captures "without prior approval", and 27 records were created after the gate. R1 writes the gate into `ki-next`, `ki-work-roadmap` and `ki-delegation`, drops the "must survive the session" limb for capture, and adds `origin` and `origin_ref` so the rubric can check it. The field changes the work-item format and the `tools-ki` model.

**Query:** Should CAPTURE-GATE become a standard rule with a checked `origin` field?

**Options:** a) (recommended, confidence medium - a field makes the gate checkable, but it is a format change across `ki-work-roadmap` and `tools-ki`) Write R1 into the standards with `origin: blocker | defect | owner` and `origin_ref`, the rubric warning on new triage without them. b) Write the rule as prose in `ki-next` and `ki-delegation` only, with no field and no rubric check.

### HANDOFF-AS-MESSAGE - Handoffs and sweeps stop creating records in each repository

**Context:** 102 of the week's new records came from handoffs and sweeps, such as one Archify redraw in seven repositories and one design handoff as 33 records across two. R2 makes a sweep one record in its owning repository and a handoff a `messages.md` line. The cross-repository choreography sections in five repositories' AGENTS.md, which let seven repositories add handoff items to one another's roadmaps, would change.

**Query:** Should a sweep be one record in its owning repository, and a handoff a message rather than a record?

**Options:** a) (recommended, confidence medium - it removes the largest source of growth, but five choreography sections change and the receiver loses a record it can see in its own roadmap) Adopt R2: one record per sweep in the owning repository, handoffs as `messages.md` lines, one record per product for a design handoff. b) Keep handoff records, but at most one per receiving repository per sweep, its steps inside it.

### STALE-SWEEP - Re-decide drafts untouched for 30 days

**Context:** 39 Future drafts have a median of 51 days since update; er-agentic-harness holds 21 of them, untouched in the fortnight. R7 brings one cancel-or-keep query per repository each week, recommending cancel as `obsolete` with the idea kept as a Project note bullet.

**Query:** Should drafts at Future, Soon or Hold untouched for 30 days come to Kris weekly as one cancel-or-keep query per repository?

**Options:** a) (recommended, confidence medium - it gives the count a floor that falls, though the first round is large) Yes, at 30 days, recommending cancel with the idea kept. b) Yes, at 60 days. c) No sweep; records stay until a lane chooses to review them.

### ACCEPT-BUNDLE - One acceptance answer per work

**Context:** 55 records await Kris's acceptance, up from 1 on 6 October. `ki-accept` already counts "a standing human grant ... quoted with its source" that "covers the exact record". R5 brings every awaiting-review record of a work in one ACCEPT query that Kris answers once.

**Query:** May each work bring its awaiting-review records as one ACCEPT query, answered in one word, as the approval for the exact records listed?

**Options:** a) (recommended, confidence medium - it fits `ki-accept`'s standing-grant rule and clears the largest queue, but Kris reviews a list rather than each packet) Yes, one ACCEPT query per work at each handoff, oldest first, each line with outcome and concern, the answer quoted with the record list in the decisions log. b) Keep one acceptance per record.
