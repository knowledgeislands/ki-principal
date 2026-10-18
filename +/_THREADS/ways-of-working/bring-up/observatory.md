# Observatory - bring-up

Drafted on 18 October 2026 by the `bring-up` run of `ways-of-working`, under Kris's RESTART-PROMPTS and RUN-SHAPE answers of 18 October in the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/decisions.md). Nothing here is filed: the draft records below go to `apps-observatory.local` through `ki-next` when the thread restarts. Items marked **after phase 2** need the `tools-ki` release with `ki work status`; items marked **after phase 3** need the Capital's move into `+/_WORK/` and `Streams/Themes/`.

## 1. The work after the migration

| | Before | After |
| --- | --- | --- |
| Id | `knowledge-islands-model.observatory` | `ki.observatory` |
| Title | `KI > Knowledge Islands model > Observatory` | `KI > Model > Observatory` |
| Level | coordination thread | Project work, `level: project` |
| Theme | Initiative `knowledge-islands-model` | theme `model`, page `Streams/Themes/model.md` (after phase 3) |
| Project note | [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) | unchanged path, `initiative:` becomes `theme: model` |
| Home | [checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_CHECKPOINTS/knowledge-islands-model.observatory.md) and [thread folder](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/observatory/) | `+/_WORK/ki.observatory/`: `work.md`, `decisions.md`, open reports, `briefs/<run>.md` |
| State at migration | hold, drained 18 October 02:27 BST | `on-hold`, reason `paused`, release "after the work migration lands" |
| Worker, supervisor | - | `agent`, `owner` |
| Run name | `observatory` | `observatory` (run slugs stay hyphenated) |

The inherited Command centre log, `+/_THREADS/command-centre/`, goes to `+/_WORK_REVIEW/ki.regular.command-centre/` for Kris's review and is not part of this work (classification of 18 October).

## 2. Bring-up items, in priority order

The product reads today's instruments directly: `packages/evidence/src/sessions.ts` reads `Streams/Initiatives/`, `Streams/Projects/` and `+/_CHECKPOINTS/` and parses `<initiative>.<project>` thread ids; `packages/evidence/src/review.ts` reads `+/_THREADS/<thread>/*.report.md` and `+/_THREADS/*/decisions.md`. The work model replaces each of these. Under [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) the Observatory reads work state only through `ki work status --format json`, schema `ki/work-status/v1`, and work items through its existing roadmap read.

The two delivered units both use the old readers: [KI-OBSERVA-VIS-023](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-023-sessions-and-threads.md) Sessions and threads and [KI-OBSERVA-VIS-024](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-024-review-queue.md) Review queue, both Awaiting review. Item 1 hands off to the migration's phase 2 under [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md).

VIS reserves through `024`, BCN through `006`; numbers are taken from the ledger at filing, so the ids below are placeholders.

| Priority | Draft | Depends on |
| --- | --- | --- |
| 1 | Work instrument on `ki work status` | after phase 2; real data after phase 3 |
| 2 | Review queue reads work folders | fixtures now; real data after phase 3 |
| 3 | Beacon raises stuck, blocked and old holds | item 1 |
| 4 | Themes and flat Projects in the Streams read | after phase 3; tolerance read can land first |

Then the thread's own carried work: unit 3, Capture feedback, and the serving and live-reload triage record.

### Item 1 - Work instrument on `ki work status`

```markdown
---
id: KI-OBSERVA-VIS-<next>
area: VIS
title: Work instrument on ki work status
kind: deliver
purpose: capability
project: observatory
theme: model
component: visualisation
horizon: next
status: triage
blocks: []
blocked_by: []
created_at: <filing time>
updated_at: <filing time>
---

# Work instrument on ki work status

## Goal

Show the selected territory's work under the work model: one row per work file from `ki work status --format json`, schema `ki/work-status/v1`, with its id, title, theme, state in role words and glyphs, holder and since, and its items beneath it; and the five views derived from the contract, with you, stuck, blocked, moving and on hold, with with you listed oldest first.

## Context

GDR-KI-PRINCIPAL-009 decides that work state is read through one `ki` command, and its Consequences say an Observatory work instrument reads the `ki work status` contract once `tools-ki` provides it. The Work Process note's Observatory fields section in Knowledge Islands Principal defines the entry fields and the rules for the five views. KI-OBSERVA-VIS-023 Sessions and threads reads checkpoints, Streams notes and the run packet directly; this record replaces that read for work state.

## Boundary

- In scope: a port and adapter that runs `ki work status --format json` for the selected territory and validates `schema: ki/work-status/v1`; the five views by the Work Process note's stated rules (stuck: a worker-held item whose later of `since` and `beat` is over 10 minutes old; on hold: `state: on-hold`, a paused hold flagged after 31 days); the banner glyphs, a settled state showing its holder's glyph alone and an arrow only in a handoff state; runs shown as items with holder `run/<name>` rather than through the run packet; `+/_WORK_REVIEW/` work shown as a count, outside the views; retiring the checkpoint and run-packet readers from the Sessions Instrument; the operator guide `read-the-instruments.md` and CHANGELOG.
- Out of scope: writing any work file or sending any move; the Beacon contributor (its own record); work items, which stay on the roadmap read; other territories beyond what `ki work status` selects.

## Dependencies / blocks

- `ki work status` released by `tools-ki` (migration phase 2, under KI-TOOL-KI-CLI-127's handoff) and installed on the host.
- Supersedes the readers of KI-OBSERVA-VIS-023.
```

### Item 2 - Review queue reads work folders

```markdown
---
id: KI-OBSERVA-VIS-<next>
area: VIS
title: Review queue reads work folders
kind: deliver
purpose: capability
project: observatory
theme: model
component: visualisation
horizon: next
status: triage
blocks: []
blocked_by: []
created_at: <filing time>
updated_at: <filing time>
---

# Review queue reads work folders

## Goal

Keep the Review queue right after the move: open reports and decisions logs are read from `+/_WORK/<id>/`, work handed to the owner comes from the with you view, and migrated work in `+/_WORK_REVIEW/<id>/` appears as its own row group for the owner's review.

## Context

KI-OBSERVA-VIS-024 reads `+/_THREADS/<thread>/*.report.md` for unanswered queries and `+/_THREADS/*/decisions.md` for answered tags. Under GDR-KI-PRINCIPAL-009 the work folder holds `decisions.md` and open reports only, settled reports are pruned at each mark, and an owner report carries no reply block: each query keeps its Context, Query and lettered Options, and Kris answers in speech. Decisions logs carry no running numbers.

## Boundary

- In scope: report and decisions paths under `+/_WORK/<id>/`, with `+/_THREADS/` still read and flagged legacy until the tolerance window closes (migration phase 5); query parsing that needs no reply block and no numbered decisions; a `+/_WORK_REVIEW/` row group; work in `handoff-to-supervisor` with holder `owner` taken from item 1's adapter once it lands; fixtures for both shapes.
- Out of scope: answering a query, editing a decisions log, opening a `+/` item for writing (OBS-REVIEW-OPEN keeps the staging refusal).

## Dependencies / blocks

- Can be built and tested on fixtures now; meets real data after the Capital's phase 3 move.
- The with you rows depend on item 1.
```

### Item 3 - Beacon raises stuck, blocked and old holds

```markdown
---
id: KI-OBSERVA-BCN-<next>
area: BCN
title: Beacon raises stuck work
kind: deliver
purpose: capability
project: observatory
theme: model
component: beacon
horizon: next
status: triage
blocks: []
blocked_by: [KI-OBSERVA-VIS-<item 1>]
created_at: <filing time>
updated_at: <filing time>
---

# Beacon raises stuck work

## Goal

The Beacon raises, from the work instrument's views: a stuck worker item (no move and no heartbeat for 10 minutes), a blocked handoff (`blocking: true` or the roadmap's own blocked signal), and a paused hold older than 31 days; and shows the count of work with the owner.

## Context

The Work Process note sets the heartbeat (an update on change, at least every 5 minutes and always by 10), stuck, blocked and the 31-day flag. KI-OBSERVA-VIS-023's Beacon raises quiet, waiting or unfinished runs from the run packet; this contributor raises the same conditions from the contract instead. Work with the supervisor is never stuck, only older, so the Beacon never raises it.

## Boundary

- In scope: one Beacon contributor reading item 1's adapter; the run-packet contributor retired once this lands.
- Out of scope: notifications beyond the Beacon; any change to the heartbeat itself.

## Dependencies / blocks

- Blocked by item 1.
```

The brief's Afterwards section names this pair, "the Observatory work instrument and Beacon contributor", for capture once `ki work status` is released.

### Item 4 - Themes and flat Projects in the Streams read

```markdown
---
id: KI-OBSERVA-VIS-<next>
area: VIS
title: Themes in the Streams read
kind: deliver
purpose: capability
project: observatory
theme: model
component: visualisation
horizon: next
status: triage
blocks: []
blocked_by: []
created_at: <filing time>
updated_at: <filing time>
---

# Themes in the Streams read

## Goal

Group work and Projects by theme: read theme pages from `Streams/Themes/<slug>.md` and flat Project notes `Streams/Projects/<slug>.md` with a `theme:` key, and say "theme" and "work" where the interface says "Initiative" and "thread".

## Context

GDR-KI-PRINCIPAL-009 makes Initiatives themes, a label that holds no work, with Project notes flat in `Streams/Projects/`. `sessions.ts` reads `Streams/Initiatives/` and derives a Project from a `<initiative>.<project>` thread id; work ids are now `ki.<project>` with no theme segment, and the theme comes from the work file's or Project note's `theme`.

## Boundary

- In scope: the new paths and `theme:` key, with `Streams/Initiatives/` and `initiative:` read with a legacy flag until phase 5; dropping the thread-id parse; interface and guide wording.
- Out of scope: reading theme page bodies beyond title and slug.

## Dependencies / blocks

- Real data after phase 3. If `tools-ki`'s registry reader exposes themes and Projects in a machine form by then, read that instead and say so at planning.
```

## 3. Restart prompt

Paste this into a new session in the ki-principal checkout once the migration has reached the Capital. It assumes phase 2 and phase 3 have landed; its first step checks.

```text
Resume KI > Model > Observatory, work id ki.observatory, from its work file under current ki-pmo and ki-delegation.

How this work runs now (GDR-KI-PRINCIPAL-009 and the Work Process note in ki-principal, Pillars/Philosophy/Model/Processes/Work Process/Work Process.md; read both first):
- The unit is work, not this session. Your work file is +/_WORK/ki.observatory/work.md: front matter holds the current state only (id, level project, title, project observatory, theme model, worker agent, supervisor owner, state, since, received, beat, mark); the body holds Next steps, Messages and Parked. Decisions live in +/_WORK/ki.observatory/decisions.md, in Kris's words, unnumbered. Open reports sit beside them; briefs in briefs/<run>.md while their handoff is open. Git history of the folder is the logbook: each send and receive is a commit whose subject carries the move, such as "docs(work): ki.observatory send to owner".
- You are worker to Kris and supervisor to your runs. The work is in one of seven states: With worker, With supervisor, Handoff to supervisor, Handoff to worker, Handoff to <target>, On hold (paused or more expected), Finished. Only the holder moves it: send puts it into handoff, receive takes it out.
- Kris receives with "with me", "ack", "got it" or "seen"; agrees a hold with "pause" or "done for now"; moves it with "resume" and "finish". "Hold" means only On hold; drain is the way into it.
- Reports are owner reports with the ki-pmo heading and form line, Done, In Progress, Queries (Context, one-sentence Query, lettered Options with a) recommended and its confidence first), then the glyph banner: holder's glyph alone when settled (🤖 With worker, 🧑 With supervisor), an arrow only in handoff (🤖 → 🧑 Handoff to supervisor), the send line only when the work is with Kris. No reply block: Kris answers in speech, by tag or bare letter; read each answer back as taken in decisions.md in the turn it arrives and ask one line where unclear.
- Coordinate only: delegate every unit through ki agent in run observatory, at most five tool calls a turn, heartbeat only while work lies with a worker.

First steps:
1. Check +/_WORK/ki.observatory/work.md exists and `ki work status --format json` runs. If either is missing, the migration has not reached this work: say so in one line and stop.
2. Re-read the work file, decisions.md and the Messages section; act on each Messages line, FIRST-STEP first. Mark, take stock (ki agent status; apps-observatory.local roadmap and git status), and give a fresh Summary carrying the parked queries forward.
3. Bring-up items first, from +/_THREADS/ways-of-working/bring-up/observatory.md (or the work folder copy if the ways-of-working work moved it): capture the four draft records in apps-observatory.local through ki-next, in priority order (work instrument on ki work status, Review queue reads work folders, Beacon raises stuck work, themes in the Streams read), reserving each number in the ledger first; then plan and deliver them as runs, item 1 first.
4. Put back the parked queries OBS-SESSIONS-ACCEPT and OBS-REVIEW-ACCEPT for KI-OBSERVA-VIS-023 and KI-OBSERVA-VIS-024 (recommended: accept as delivered, since items 1 and 2 replace their readers), OBS-REVIEW-OPEN and OBS-OVERDUE-TITLE.
5. Then the carried work: capture the serving and live-reload idea as triage, and unit 3, Capture feedback, behind KI-OBSERVA-VIS-024. Unit 4 still waits on Host network.
6. Each delivery needs the service restarted on the host in an interactive session; ask Kris.
Then banner.
```

## Open points for the restart

- The theme slug `model` follows WORK-THEME-SLUGS; the harness's example work file still shows `knowledge-islands-model`. Phase 3 settles which slug the work file carries.
- The parked queries' detail lives in `+/_THREADS/observatory/obs-land.report.md`; phase 3 decides whether it survives as an open report in the work folder or as Parked lines only.
