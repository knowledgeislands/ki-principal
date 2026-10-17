# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working/ways-of-working.md) › work-model-shape

**Run report at 00:54 BST · last mark 22:34 BST**

---

## Done

- Revised the [work-model report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/work-model.report.md) to Kris's REGULAR-WORK, THEMES-PAGE and FOLDER-TREE ideas of 18 October 00:46 BST in the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/decisions.md): regular work replaces regular activities throughout, as one of two forms of work beside Project work under territory work, defined in the Capital and creating work items in any repository; a Project's own recurring checks stay with it; the theme is a label with its own page in `Streams/Themes/`. Committed `a12fbf1` through the commit gate (pass) and pushed fast-forward; no other session's commit was beneath it.
- Redrew the [diagram](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/work-model.svg) in the same style: territory work at the top, regular work and Project work side by side, Kris to the side, execution at the bottom, the theme as a label node. Archify's gates passed, the `ki-diagrams` exporter exported it, a fresh one-off script flattened it to static light SVG, and `rsvg-convert` showed it reads cleanly by eye.
- Added section 10, the folder tree: an inventory of `Streams/` today, `tree`-style blocks for today, the proposed flat shape and the nested alternative, and which folder WORK-THEME is about (the Project note's place in `Streams/`, not the flat `+/_WORK/<id>/` folder settled in WORK-HOME).
- The inventory found more design material in `Streams/` than the Model Initiative's: three Project `design/` folders (16 papers) and, under Mac Studio setup, a script, three run logs and an SVG. All go to `+/_WORK/ki.<project>/`. The territory-selection papers under the Model Initiative are already consolidated into [ADR-KI-PRINCIPAL-002](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-002-territory-derived-repository-selection.md), so the report counsels deleting them rather than moving them.
- Rewrote WORK-THEME as the choice of nested or flat Project notes, with pros and cons, and WORK-REGULAR as regular work beside Project work. Every recommended option now carries a confidence in [KI-HARNESS-GOV-207](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-207-recommendation-confidence.md)'s form. WORK-HOME and WORK-HISTORY, answered a) in the walkthrough, were taken out of the queries and reply block.
- Counsel only: no standard, skill, record, checkpoint, Admin, Pillars or Resources was changed, and no files were moved. The temporary folder was deleted.

## In Progress

- Nothing is running.

### Outstanding - no action requested now

- I read `registry-removal`, which has no Project note, as ad hoc work, `ki.regular.registry-removal`. I did not check that with its thread.
- The flatten script was again one-off. [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md) would make it a supported export.
- The run report's heading time is a minute ahead of the clock, a slip left in place.
- `+/_THREADS/chezmoi/decisions.md` is dirty from another session and was left alone.

## Queries

WORK-THEME and WORK-REGULAR are given below in full. WORK-MODEL, WORK-WORDS, DECISIONS-STRIKE, WORK-BANNER and WORK-SETTLE are still in the work-model report, unchanged apart from their confidence and a line on the two forms of work. Their entries are in the reply block below.

### WORK-THEME - where Project notes sit under themes

**Context:** Kris set the shape on 18 October: `Streams/Initiatives/` becomes `Streams/Themes/`, each theme with its own page saying why it is a theme, what matters, its general direction and common guidance, and the theme holds no work; regular work, Project work and ad hoc work can all carry its label, and ids drop the theme segment (section 3). In the walkthrough Kris first answered "Theme, keep nesting", then asked for pros and cons. The folder in question is where a Project's note sits in `Streams/`, not the work folder in `+/_WORK/`, which is flat under WORK-HOME; section 10 draws both. Today the 21 Project notes are already flat in `Streams/Projects/` with an `initiative:` key, and SHAPE-AGREE agreed to nest them before the migration runs. Nesting under `Streams/Themes/<theme>/`: for, a theme's Projects sit together in the file tree, the theme page doubles as the folder's index note, and it keeps SHAPE-AGREE and Kris's first answer; against, re-theming a Project moves its note and changes every path link to it, a Project touching two themes must pick one, regular and ad hoc work cannot nest so themes would be carried two ways, and the migration moves 21 notes and teaches tools-ki's registry reader and `ki-repo-kb-streams` a two-level path. Flat with a `theme:` key: for, it is today's shape so the migration is a key rename, one mechanism serves all three forms of work, and re-theming is a one-line edit; against, the theme page lists its Projects by a query or a maintained list rather than by folder, and the file tree does not group them.

**Query:** Should Project notes stay flat in `Streams/Projects/` with a `theme:` key, rather than nest in their theme's folder?

**Options:**

a) (recommended, confidence medium - it is today's shape and one mechanism for all three forms of work, but nesting's browsing benefit is real and Kris first leant to it) Keep Project notes flat in `Streams/Projects/` with `initiative:` renamed `theme:`; rename `Streams/Initiatives/` to `Streams/Themes/` with one page per theme holding no work; drop the theme from ids; amend SHAPE-AGREE's nesting and THREAD-IDS-AGREE's three-part ids within the one migration.

b) Nest Project notes under `Streams/Themes/<theme>/`, the theme page as the folder's index note, keeping SHAPE-AGREE's nesting; ids still drop the theme segment.

c) Nest them and keep THREAD-IDS-AGREE's three-part ids as well.

### WORK-REGULAR - regular work beside Project work

**Context:** Kris on 18 October: regular activities "are defined at the territory level ... They're not on the individual repos ... they're in the principal thing, and then effectively they could create work item records", and "maybe rather than regular activities, we can call it regular work and project work. That's the two forms of work that happen". Section 1 and the diagram now draw regular work, `ki.regular`, beside Project work beneath territory work. It is defined at territory level in the Capital's Activity notes, never closes, has no coordinator session because state of play dispatches each occurrence as ACT-THREAD set, creates work item records in any repository, and may carry a theme label; ad hoc work with no Project lies there as `ki.regular.<slug>`. A Project's own recurring checks, which Kris allowed for in the walkthrough ("or even at the project level if there's a project exists ... once the project finishes, there'll be no need anymore for that activity"), stay with the Project and end with it. This amends ACT-HOME, "territory or Initiative level, never in a Project ... Initiative stays the default", and [KI-HARNESS-GOV-206](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-206-activity-homes-and-coordination.md), and moves the Model Initiative note's recurring-upkeep paragraph to regular work. Today the three active Activities name `initiative: knowledge-islands-model` as their home.

**Query:** Should regular work be the territory-level form of work beside Project work, with a Project's own recurring checks staying with the Project?

**Options:**

a) (recommended, confidence high - it is Kris's own framing of 18 October, and keeping a Project's checks with it follows [GDR-KI-PRINCIPAL-005](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-005-the-roadmap-model.md)'s rule that a Project is finite) Make regular work, `ki.regular`, the territory-level form of work beside Project work: defined in the Capital, dispatched by state of play, creating work items in any repository, carrying an optional theme label and holding ad hoc work as `ki.regular.<slug>`; a Project's own recurring checks stay with the Project and end with it; Activity notes' `initiative:` becomes an optional `theme:`; amend ACT-HOME and KI-HARNESS-GOV-206 to match.

b) As a), but all recurring work, a Project's own checks included, lives in regular work.

c) Make regular work a standing Project in each territory, amending GDR-KI-PRINCIPAL-005's rule that a Project is finite.

```text
WORK-MODEL

Agree section 1 of work-model.report.md as the one model of work: territory work at the top as the hub, regular work and Project work side by side beneath it as the two forms of work, each sending work items to any repository, and the work item as execution; a theme as a label either form can carry, not a level; work cascading to the lowest level that can do it, relative worker and supervisor roles per handoff, the four kinds of state (with someone, handed off, on hold, done) as seven role-word states with only the supervisor's receive and the hold set, On hold agreed from With supervisor and drained on the way in with the reasons paused (named release) and more expected (released by new work), the move into it a mark that commits, pushes and parks everything, resume or new work moving it to Handoff to worker and finish to Finished, the states mapped onto a record's status and horizon with ready as Handoff to worker, stuck as a worker's item quiet for 10 minutes and no heartbeat on hold; nothing written into standards until WORK-SETTLE's migration.

---

WORK-WORDS

Adopt section 2 of work-model.report.md as it stands: regular work and Project work as the two forms of work, work item (task in speech), work file work.md, worker and supervisor, the states With worker, Handoff to supervisor, With supervisor, Handoff to worker, Handoff to <target>, On hold (paused or more expected, with a release) and Finished, the lists with you, stuck, blocked, moving and on hold, the receive words with me, ack, got it and seen, and the supervisor's pause, done for now, resume and finish; hold means only the agreed On hold state, which the ki-pmo hold and the roadmap hold horizon already are, hold leaves the receive words, drain stays the activity and the hold report keeps its name.

---

WORK-THEME

Keep Project notes flat in Streams/Projects/ with initiative: renamed theme:; rename Streams/Initiatives/ to Streams/Themes/ with one page per theme (why it is a theme, what matters, general direction, common guidance) holding no work; drop the theme from ids (ki.ways-of-working); amend SHAPE-AGREE's nesting and THREAD-IDS-AGREE's three-part ids within the one migration.

---

WORK-REGULAR

Make regular work, ki.regular, the territory-level form of work beside Project work: defined in the Capital, dispatched by state of play, creating work items in any repository, carrying an optional theme label and holding ad hoc work as ki.regular.<slug>; a Project's own recurring checks stay with the Project and end with it; Activity notes' initiative: becomes an optional theme:; amend ACT-HOME and KI-HARNESS-GOV-206 to match.

---

DECISIONS-STRIKE

Agree section 4 of work-model.report.md: decisions.md kept apart from the Git logbook; at each mark each entry is struck, reduced to a pointer or kept after checking its durable home; moves are not decisions; no numbering; first applied to the ways-of-working log at the first mark after the migration.

---

WORK-BANNER

Adopt section 6 of work-model.report.md: one glyph-heading banner for every state in role words, counts and lists saying with you, the same prefix on the form line, the heartbeat only while work lies with a worker, and the frames retired when the model is written in.

---

WORK-SETTLE

Agree section 9 of work-model.report.md: write GDR-KI-PRINCIPAL-009 and the Work Process note under Pillars/Philosophy/Model/Processes/ first, then brief SHAPE-AGREE's one migration with sections 7 and 10 folded in, add the ki work status contract to KI-TOOL-KI-CLI-127, and have the Observatory Work instrument record captured once that read lands.
```

```text
╭─ run report · 2026-10-17T23:54:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · thread at rest          │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · nothing running         │
│  █  █ █▄▄▄ ▄▄▄█   █    · nothing queued          │
│                                                  │
╰──────────────────────────────────────────────────╯

- [at rest] nothing running or queued
- [waiting] WORK-MODEL
- [waiting] WORK-WORDS
- [waiting] WORK-THEME
- [waiting] WORK-REGULAR
- [waiting] DECISIONS-STRIKE
- [waiting] WORK-BANNER
- [waiting] WORK-SETTLE
- [committed] work-model report, diagram and this report, pushed
```

```text
Resume KI > Model > ways of working under current ki-pmo and ki-delegation since 22:34 BST: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.
```
