# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › settle-model

**Run report at 01:51 BST · last mark 22:34 BST**

---

## Done

- Wrote [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md), The work model, and indexed it in [Decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/Decisions.md) under a new Work decisions section, since reveal order puts it after GDR-KI-PRINCIPAL-008. It covers WORK-MODEL, WORK-WORDS, WORK-THEME, WORK-REGULAR as amended (regular work is self-coordinating, needs no coordination thread, and state of play may discuss it but does not necessarily dispatch it), WORK-HOME, WORK-HISTORY, DECISIONS-STRIKE, WORK-BANNER and WORK-SETTLE, and quotes Kris throughout.
- One judgment call on "list what it supersedes": the decision-records standard forbids a supersession chain and links to notes, so the record names the replaced choices in one present-tense Consequences line ("These earlier choices no longer govern: ...") and names the Work Process note without linking it.
- Amended [GDR-KI-PRINCIPAL-005](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-005-the-roadmap-model.md) in place, as WORK-SETTLE a) allows. It said checkpoints, Initiatives and an Initiative home for recurring work; it now says themes in `Streams/Themes/`, flat Projects with `theme`, regular work in the Capital, and working state outside `Streams/`. It does not point forward to GDR-KI-PRINCIPAL-009.
- Wrote the [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note, with a light static `work-model.svg` beside it (checked visually, no animation), and made [Processes](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Processes.md) four processes.
- Drafted the [work-migration brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/work-migration.brief.md). It is not launched. Its five phases are the harness, then tools-ki and a release, then the Capital, then the other territories, then closing the tolerance window. It folds in the work model and the work-model report's sections 7 and 10, and its counts for the other territories were checked against their checkouts.
- Checks: rumdl was clean on all six files. The ki-decision-records audit has no failures (three INDEX-8 warnings on ADR-KI-PRINCIPAL-004, 005 and 006, already there). The ki-repo-kb audit has no failures (four ki-repo-kb-streams warnings, already there). The commit gate passed.
- Committed and pushed fast-forward to ki-principal `main`: `docs(model): add the Work Process note` and `docs(threads): draft the work-migration brief`. No other session's commits were stacked under them.
- The commit split went wrong. The gate refused my first commit, `docs(decisions): add GDR-KI-PRINCIPAL-009 the work model`, without showing why (commitlint accepts the message). Its staged files were swept into the next commit, so `docs(model): add the Work Process note` also carries GDR-KI-PRINCIPAL-009, GDR-KI-PRINCIPAL-005 and Decisions. It is pushed and I left it as it is, because rewriting shared history is not allowed.
- `git pull --rebase --no-autostash` refused because another session has `+/_THREADS/chezmoi/decisions.md` uncommitted. Origin had not moved, so the push went through fast-forward. I did not touch that file or the untracked knowledge-acquisition reports.
- I left the tools-ki checkout alone. The work-status contract for [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md) is below, ready to paste.

### Handoff for KI-TOOL-KI-CLI-127 - the work-status contract

```text
To: tools-ki, under KI-TOOL-KI-CLI-127. From: ki-principal, ways-of-working, under GDR-KI-PRINCIPAL-009 (canonical description: the Work Process note, Pillars/Philosophy/Model/Processes/Work Process/ in ki-principal). Blocking: no; the Observatory work instrument waits on it.

Add `ki work status [--repo <path>] [--format text|json]`. It is read-only: it reads every `+/_WORK/<id>/work.md` in the repository and, for the tolerance window, every `+/_CHECKPOINTS/*.md`. It writes nothing.

JSON: { "schema": "ki/work-status/v1", "repository": "<name>", "generatedAt": "<UTC ISO>", "work": [ <entry> ] }, one entry per work file.

Entry fields:
- identity: "<territory alias>:<id>", unique across territories
- id: "ki" | "ki.regular" | "ki.<project>" | "ki.regular.<slug>"
- level: "territory" | "regular" | "project"
- title: string
- theme: string | null
- worker, supervisor: party names for the current handoff
- state: "with-worker" | "handoff-to-supervisor" | "with-supervisor" | "handoff-to-worker" | "handoff" | "on-hold" | "finished"
- hold: { "reason": "paused" | "more-expected", "release": string | null } | null
- holder: the party the work lies with now, derived from state, worker and supervisor
- role: "worker" | "supervisor" | "target", the holder's role
- target: the named party, for state "handoff" only, else null
- blocking: boolean, true when the handoff carries a blocking query
- since: UTC ISO, when the work entered its current state
- received: UTC ISO | null, the supervisor's last receive
- beat: UTC ISO | null, the worker's last heartbeat or move
- path: repository-relative path to work.md
- items: [ { id, kind ("record" | "run" | "person"), holder, role, state, target, blocking, since } ], one per open work item

Set versus derived: only `received` (the supervisor's receive) and `hold` are set in work.md front matter. `state` is derived from where the items lie: any item with the worker means with-worker; else any item in handoff to the supervisor means handoff-to-supervisor; and so on, per the Work Process note. For a record item, map the roadmap status: in-progress = with-worker, awaiting-review = handoff-to-supervisor, triage or unapproved draft = with-supervisor, ready = handoff-to-worker, a blocker or waiting-for hold = handoff to its target, a parked hold = on-hold, done or cancelled = finished.

The five views, derived and never stored:
- with you: holder is the named party
- stuck: holder's role is worker, state is with-worker, and now - max(beat, since) > 10 minutes; never for with-supervisor or on-hold
- blocked: blocking is true, or state is handoff to a target that has not received
- moving: with-worker and not stuck
- on hold: state is on-hold; flag a paused hold whose since is older than 31 days

Text form: the five views, one line per entry: glyph, id, holder, since.

Legacy: a checkpoint maps to an entry with level from its thread type, state from its pick-up status (rest = with-supervisor, busy = with-worker, hold = on-hold paused), and path to the checkpoint.

Tests through run(args, context) and sandbox(); man/ki.1, README and CHANGELOG; then a release.
```

## In Progress

Nothing is running.

### Outstanding - no action requested now

- The work-migration brief waits on MIGRATION-LAUNCH below. Phase 2 goes to the tools burndown thread as a handoff, not as a launch from ways-of-working.
- The ways-of-working decisions log is struck at the first mark after the Capital's phase, as DECISIONS-STRIKE set.
- At the next mark, the thread prunes the thread-lifecycle, thread-states and work-cascade reports, as the checkpoint's next steps already say.
- [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md), [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md), [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) and [KI-HARNESS-GOV-206](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-206-activity-homes-and-coordination.md) are amended by the brief's phase 1. Nothing was changed in the harness now.
- The six records SHAPE-AGREE's registry-shape report proposed do not appear to have been captured. Phase 1 captures one harness record in their place.
- The Observatory work instrument belongs to apps-observatory.local, outside this Capital's choreography list, so it is captured there once `ki work status` ships.

## Queries

### WORK-THEME-SLUGS - Which slugs the theme pages take

**Context:** SHORT-NAMES renamed `knowledge-islands-model` to `model` and `platform-foundations` to `foundations`. The work-model report's folder tree, which you called correct, drew `Streams/Themes/` with today's slugs. A flat `Streams/Themes/model.md` shares its basename with `Pillars/Philosophy/Model/Model.md`, so bare wikilinks would be ambiguous.

**Query:** Should the theme pages take the SHORT-NAMES slugs or keep today's?

**Options:**

a) (recommended, confidence medium - SHORT-NAMES is a standing answer and the tree read as illustrative) Apply SHORT-NAMES: `Streams/Themes/model.md` and `Streams/Themes/foundations.md`, with path-form wikilinks such as `[[Themes/model|Model]]`.

b) Keep today's slugs, `Streams/Themes/knowledge-islands-model.md` and `Streams/Themes/platform-foundations.md`, and drop that part of SHORT-NAMES.

### WORK-FILE-NAME - What the checkpoint skill becomes

**Context:** Under the work model, `ki-checkpoint` stops describing a checkpoint and becomes the standard for `+/_WORK/<id>/work.md`. The brief's phase 1 rewrites it, and the skill's name decides every citation the harness and tools-ki write.

**Query:** Should the harness run rename `ki-checkpoint`?

**Options:**

a) (recommended, confidence medium - the name then matches the file it governs) Rename it `ki-work-file` in the phase 1 harness run, keeping a pointer under the old name until the tolerance window closes.

b) Keep the name `ki-checkpoint` and rewrite its content only.

### MIGRATION-LAUNCH - Launch the work migration

**Context:** The [work-migration brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/work-migration.brief.md) is a draft under SHAPE-AGREE and WORK-SETTLE. It runs in five phases: the harness, tools-ki and a release through the tools burndown thread, the Capital, the other territories through handoffs, and then closing the tolerance window. Each phase starts only when the one before it has landed and been pushed.

**Query:** Should ways-of-working launch phase 1 now?

**Options:**

a) (recommended, confidence high - the order and gates are the ones you agreed, and each phase is gated) Once WORK-THEME-SLUGS and WORK-FILE-NAME are answered, launch phase 1 in ki-agentic-harness and send phase 2 to the tools burndown thread with the KI-TOOL-KI-CLI-127 handoff, then the Capital after the release.

b) Hold the brief until the restart, and launch nothing yet.

```text
WORK-THEME-SLUGS

Apply SHORT-NAMES to the theme pages: Streams/Themes/model.md and Streams/Themes/foundations.md, with path-form wikilinks such as [[Themes/model|Model]]; read the work-model report's tree as illustrative.

---

WORK-FILE-NAME

Rename ki-checkpoint to ki-work-file in the phase 1 harness run of the work-migration brief, keeping a pointer under the old name until the tolerance window closes.

---

MIGRATION-LAUNCH

Launch phase 1 of +/_THREADS/ways-of-working/work-migration.brief.md in ki-agentic-harness now, and send phase 2 to the tools burndown thread with the KI-TOOL-KI-CLI-127 handoff from the settle-model report; the Capital's phase follows the release.
```

```text
╭─ run report · 2026-10-18T00:51:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · nothing queued          │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] nothing running or queued
- [waiting] WORK-THEME-SLUGS
- [waiting] WORK-FILE-NAME
- [waiting] MIGRATION-LAUNCH
- [committed] decision record, Work Process note and migration brief, pushed
- [blocked] pull by another session's uncommitted `+/_THREADS/chezmoi/decisions.md`; push went through fast-forward
