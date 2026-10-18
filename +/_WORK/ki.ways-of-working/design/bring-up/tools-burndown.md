# Tools burndown - bring-up

Drafted on 18 October 2026 by the `bring-up` run of `ways-of-working`, under Kris's RESTART-PROMPTS and RUN-SHAPE answers of 18 October in the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/decisions.md). Nothing here is filed. Under RUN-SHAPE the `ways-of-working` work itself runs migration phase 2 in `tools-ki` (`ki work status`, the registry and work-file readers, one release); the items below are what remains for this Project's product work once that lands. Items marked **after phase 2** need that release; **after phase 3** needs the Capital's move into `+/_WORK/`.

## 1. The work after the migration

| | Before | After |
| --- | --- | --- |
| Id | `platform-foundations.tools-burndown` | `ki.tools-burndown` |
| Title | `Fnd: tools-burndown` | `KI > Foundations > Tools burndown` |
| Level | coordination thread | Project work, `level: project` |
| Theme | Initiative `platform-foundations` | theme `foundations`, page `Streams/Themes/foundations.md` (after phase 3) |
| Project note | [tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) | unchanged path, `initiative:` becomes `theme: foundations` |
| Home | [checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_CHECKPOINTS/platform-foundations.tools-burndown.md) and [thread folder](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/tools-burndown/) | `+/_WORK/ki.tools-burndown/`: `work.md`, `decisions.md`, open reports, `briefs/next-worker.md`, and `design/` for the five evidence and manifest files |
| State at migration | rest, wrapping up for the ways-of-working updates | `on-hold`, reason `paused`, release "after the work migration lands" |
| Worker, supervisor | - | `agent`, `owner` |
| Run name | `tools-burndown` | `tools-burndown` |

**Phase 3 holds this folder back.** The classification of 18 October moves `ki.tools-burndown` only once the session that has `+/_THREADS/tools-burndown/` in flight releases it; the work folder may therefore arrive after the rest of the Capital. Scope is unchanged: `tools-ki`, `tools-mgit`, `tools-git-almanac` and the CLI-shaped `ki-agentic-harness` records, excluding `tools-rig` and `tools-techne`.

## 2. Bring-up items, in priority order

On `origin/main`, `tools-ki` reads the old instruments in `src/core/agent/thread.ts` (`threadFolder` is `+/_THREADS/<run>`), the registry and roadmap readers (`src/core/work/registry.ts`, `roadmap-report.ts`, `src/commands/repo/roadmap.ts`, reading `initiative:`), and its guide, README and manual. `ki agent reconcile <run> <number> <home>` addresses decisions by running number. The [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md) delivery (decision classes, `send`, bare letters, the live listing) sits in the 31 local commits not yet on `origin/main`, behind the stuck rebase Kris is looking at. `tools-mgit` and `tools-git-almanac` read none of the old paths and need no bring-up item.

CLI reserves through `143` on `origin/main`, with `144` and `145` issued in the local commits; numbers come from the ledger at filing, so the ids below are placeholders. Phase 2 may already cover part of an item: each is captured only for what phase 2's delivery leaves.

| Priority | Draft | Depends on |
| --- | --- | --- |
| 1 | Decisions log in the work folder, unnumbered | after phase 2; the CLI-127 line pushed |
| 2 | Re-key thread session bindings to work ids (amend KI-TOOL-KI-CLI-145) | after phase 2 |
| 3 | Live listing and send speak the work model | after phase 2; the CLI-127 line pushed |
| 4 | Background-agents guide speaks the work model | items 1 to 3 |
| 5 | Record `theme:` accepted, `initiative:` warned | only if phase 2 did not ship it |

Then the thread's carried work, below the items.

### Item 1 - Decisions log in the work folder, unnumbered

```markdown
---
id: KI-TOOL-KI-CLI-<next>
area: CLI
title: Unnumbered work decisions log
kind: deliver
purpose: capability
project: tools-burndown
theme: foundations
component: agent
horizon: next
status: triage
blocks: []
blocked_by: []
created_at: <filing time>
updated_at: <filing time>
---

# Unnumbered work decisions log

## Goal

`ki agent decide`, `reconcile` and the `close` gate work on the work folder's `decisions.md`, `+/_WORK/<id>/decisions.md`, whose entries carry no running numbers, and bare-letter resolution reads the work folder's open reports.

## Context

GDR-KI-PRINCIPAL-009 moves the decisions log into the work folder and drops running numbers: at each mark an entry is struck, reduced to a one-line pointer or kept. Today `reconcile` takes `<number>`, the `close` gate accepts a held entry's untracked home only under a `_CHECKPOINTS` path segment, and bare-letter resolution lists `*.report.md` under the thread folder. Owner reports no longer carry a reply block, but Kris may still answer with a bare letter, so the resolution stays.

## Boundary

- In scope: entries addressed by tag and time rather than number in `reconcile`; the held-home rule accepting `+/_WORK/<id>/work.md`; bare letters read from `+/_WORK/<id>/*.report.md`; old `+/_THREADS/` logs read with a warning until the tolerance window closes; tests through `run(args, context)` and `sandbox()`; README, `man/ki.1`, CHANGELOG.
- Out of scope: striking entries, which stays the coordinating work's duty at its mark; the run-to-work home mapping itself, which phase 2 delivers.

## Dependencies / blocks

- After migration phase 2 (work home in `thread.json`), and after the KI-TOOL-KI-CLI-127 commits reach `origin/main`.
```

### Item 2 - Re-key thread session bindings to work ids

[KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) is at triage and keys a binding as `<repository name>/<checkpoint stem>`, caching `label` and `role` from the checkpoint. This is an amendment to its Goal and Requirements, not a new record:

```markdown
## Amendment, work model (18 October 2026)

- The key becomes `<repository name>/<work id>`, such as `ki-principal/ki.observatory`, and the binding caches `title` and `level` from `+/_WORK/<id>/work.md`; `role_from` names the work file and its `since`.
- The role is derived from `level`: `territory` and `project` are coordinating, `regular` is not. The old `role` field is read from a checkpoint only during the tolerance window.
- `ki thread start|resume` opens with the work's send line, read from the work file's state, instead of the old resume line.
- Whether the command group stays `ki thread` or moves under `ki work` is an open question for planning; SKILL-NAMES keeps `ki agent` unchanged.
```

### Item 3 - Live listing and send speak the work model

```markdown
---
id: KI-TOOL-KI-CLI-<next>
area: CLI
title: Agent listing in banner form
kind: deliver
purpose: capability
project: tools-burndown
theme: foundations
component: agent
horizon: next
status: triage
blocks: []
blocked_by: []
created_at: <filing time>
updated_at: <filing time>
---

# Agent listing in banner form

## Goal

`ki agent status` with no run lists live runs under their work id and in the banner's item form, `- [<state>] <what> · run/<name> · since <time>`, marking a run stuck when neither its status line nor its process has moved for 10 minutes; and `ki agent send` addresses a work id.

## Context

KI-TOOL-KI-CLI-127 lists runs as `- [running] <agent> - <what>` under a `<run> (<thread home>)` line, the banner form of 14 October. The Work Process note's banner lists `- [state] what · holder · since`, holders are written `run/<name>`, and stuck is a worker's item with no move and no heartbeat for 10 minutes. Messages between work now live in the receiving work file's Messages section.

## Boundary

- In scope: the listing's heading by work id and its item form; the stuck mark; `send <work id> <line>` resolving the work's live run.
- Out of scope: writing into a work file's Messages section, which is a tracked edit the coordinating work makes; whether `send` should ever do so is an open question for planning. Per-run `status` output stays as it is.

## Dependencies / blocks

- After migration phase 2 and the KI-TOOL-KI-CLI-127 commits on `origin/main`.
```

### Item 4 - Background-agents guide speaks the work model

```markdown
---
id: KI-TOOL-KI-CLI-<next>
area: CLI
title: Agents guide work vocabulary
kind: deliver
purpose: debt
project: tools-burndown
theme: foundations
component: agent
horizon: next
status: triage
blocks: []
blocked_by: [KI-TOOL-KI-CLI-<item 1>, KI-TOOL-KI-CLI-<item 3>]
created_at: <filing time>
updated_at: <filing time>
---

# Agents guide work vocabulary

## Goal

`docs/guides/user/background-agents.md`, README and `man/ki.1` say work, work file, work folder, worker and supervisor where they say thread, checkpoint and thread folder; place briefs at `+/_WORK/<id>/briefs/<run>.md`; and drop the reply block from the bare-letter passage, citing the Work Process note by its canonical URL rather than restating it.

## Boundary

- In scope: wording and paths in the three surfaces and `man/ki.commands.json` where generated.
- Out of scope: behaviour, which items 1 to 3 and phase 2 change.
```

### Item 5 - Record `theme:` accepted, `initiative:` warned

Capture only if phase 2's release does not already do it: the roadmap readers accept an optional `theme:` on records and warn on `initiative:` for the tolerance window, as the harness's `ki-work-roadmap` standard now requires. The territory survey of 18 October lists `tools-rig` with 13 records to convert, so the reader must ship first.

## 3. Carried work, after the bring-up items

From the checkpoint's open queries and next steps, unchanged by the migration except where noted:

- **The tools-ki rebase.** Kris is looking at the stuck rebase (REBASE-LOOK, 18 October). PUSH-REBASE-CODE, which carries TMP-HOME and the state tooling into [KI-TOOL-KI-CLI-137](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-137-agent-run-tmp-home.md), depends on it.
- **TOOLS-RELEASE.** The v0.10.6 cut may be overtaken by the one release phase 2 cuts under RUN-SHAPE; put it back to Kris as superseded, recommending no separate cut.
- **One tools-ki writer at a time.** While phase 2 runs in `tools-ki`, this work launches nothing there.
- MGIT-PLAN, MGIT-REVIEW-LOWS, RIG-TARGET-SPEED-ACCEPT, RIG-TARGET-SPEED-LOAD, DESK-KIT-SOP and WRAP-NOW, as parked; [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) and [KI-TOOL-RIG-CORE-060](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md) awaiting Kris's acceptance.
- The thread-folder tidy under THREADS-CLEAR and PMO-7-BACKLOG is replaced by the work folder's prune at each mark.

## 4. Restart prompt

Paste this into a new session in the ki-principal checkout once the migration has reached this work. Its first step checks.

```text
Resume KI > Foundations > Tools burndown, work id ki.tools-burndown, from its work file under current ki-pmo and ki-delegation.

How this work runs now (GDR-KI-PRINCIPAL-009 and the Work Process note in ki-principal, Pillars/Philosophy/Model/Processes/Work Process/Work Process.md; read both first):
- The unit is work, not this session. Your work file is +/_WORK/ki.tools-burndown/work.md: front matter holds the current state only (id, level project, title, project tools-burndown, theme foundations, worker agent, supervisor owner, state, since, received, beat, mark); the body holds Next steps, Messages and Parked. Decisions live in +/_WORK/ki.tools-burndown/decisions.md, in Kris's words, unnumbered. Open reports sit beside them; briefs in briefs/<run>.md while their handoff is open; evidence in design/. Git history of the folder is the logbook: each send and receive is a commit whose subject carries the move, such as "docs(work): ki.tools-burndown send to owner".
- You are worker to Kris and supervisor to your runs. The work is in one of seven states: With worker, With supervisor, Handoff to supervisor, Handoff to worker, Handoff to <target>, On hold (paused or more expected), Finished. Only the holder moves it: send puts it into handoff, receive takes it out.
- Kris receives with "with me", "ack", "got it" or "seen"; agrees a hold with "pause" or "done for now"; moves it with "resume" and "finish". "Hold" means only On hold; drain is the way into it.
- Reports are owner reports with the ki-pmo heading and form line, Done, In Progress, Queries (Context, one-sentence Query, lettered Options with a) recommended and its confidence first), then the glyph banner: holder's glyph alone when settled (🤖 With worker, 🧑 With supervisor), an arrow only in handoff (🤖 → 🧑 Handoff to supervisor), the send line only when the work is with Kris. No reply block: Kris answers in speech, by tag or bare letter; read each answer back as taken in decisions.md in the turn it arrives and ask one line where unclear.
- Coordinate only: delegate every unit through ki agent in run tools-burndown, at most five tool calls a turn, heartbeat only while work lies with a worker. Ask Kris before any ki or mgit release and before any remote branch delete. One tools-ki writer at a time.

First steps:
1. Check +/_WORK/ki.tools-burndown/work.md exists, `ki work status --format json` runs, and the tools-ki checkout is on a clean main with the rebase finished. If any is missing, say which in one line and stop.
2. Re-read the work file, decisions.md and the Messages section; act on each Messages line, FIRST-STEP first. Mark, take stock (ki agent status; git status and roadmaps of tools-ki, tools-mgit and tools-git-almanac), and give a fresh Summary carrying the parked queries forward.
3. Bring-up items first, from +/_THREADS/ways-of-working/bring-up/tools-burndown.md (or the work folder copy if the ways-of-working work moved it): compare each against what phase 2 shipped, then capture what remains in tools-ki through ki-next, in priority order (unnumbered work decisions log; amend KI-TOOL-KI-CLI-145 to work ids; agent listing in banner form; agents guide work vocabulary; record theme only if phase 2 left it), reserving each number in the ledger first; then plan and deliver them as runs, one tools-ki writer at a time.
4. Put back the parked queries MGIT-PLAN, MGIT-REVIEW-LOWS, RIG-TARGET-SPEED-ACCEPT, RIG-TARGET-SPEED-LOAD, DESK-KIT-SOP and WRAP-NOW, and TOOLS-RELEASE marked as likely superseded by the phase 2 release.
5. Then the carried work: PUSH-REBASE-CODE into KI-TOOL-KI-CLI-137, the KI_QUIET triage record, and the tools-ki ki-accept group, as the work file's Next steps give them.
Then banner.
```

## Open points for the restart

- `project: tools-burndown` on the draft records follows RUN-SHAPE, which gives each Project its own bring-up items; KI-TOOL-KI-CLI-127 itself sits under `ways-of-working`. If Kris prefers the items under `ways-of-working`, only the `project:` key changes.
- The theme slug `foundations` follows WORK-THEME-SLUGS; phase 3 settles the slug the work file carries.
