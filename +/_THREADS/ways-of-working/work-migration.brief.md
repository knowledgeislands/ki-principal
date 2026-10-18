# SHAPE-AGREE migration brief - the work model

Draft for the `ways-of-working` thread, written by `settle-model` on 18 October 2026. Not launched. The thread launches it, run by run, once the queries at the end are answered.

## Authority

- **SHAPE-AGREE** (Kris, 17 October 22:50 BST): "Agree the nested Project shape, SHORT-NAMES, DESIGN-TIDY, DECISIONS-HOME, THREAD-IDS-AGREE, IDS-MIGRATE and NAMING-REST as one migration after the restart: harness checker first, then folders, decisions logs and thread ids together."
- **The work-model answers** (Kris, 18 October 01:38 BST), recorded in the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/ways-of-working/decisions.md): WORK-MODEL, WORK-WORDS, WORK-THEME, WORK-REGULAR as amended, DECISIONS-STRIKE, WORK-BANNER and WORK-SETTLE, with WORK-HOME and WORK-HISTORY settled in the walkthrough. WORK-SETTLE a) folds the work model and the work-model report's sections 7 and 10 into this one migration.
- **REPLY-BLOCK and BANNER-GLYPH** (Kris, 18 October 01:55 BST), recorded in the same log: owner reports drop the copyable reply block, Kris answering in speech; a settled state shows its holder's glyph alone and an arrow appears only in a handoff state. Both are written into GDR-KI-PRINCIPAL-009 and the Work Process note.
- **What the work model changes in SHAPE-AGREE.** Nesting Project notes is replaced by flat notes with a `theme:` key; Initiatives become themes; THREAD-IDS-AGREE's three-part ids become two-part ids with no theme segment, and `.sop` becomes `ki`; DECISIONS-HOME's `decisions.md` beside the Project note is reversed, decisions staying in the work folder; DESIGN-TIDY's `+/_DESIGN/<subject>/` becomes `+/_WORK/<id>/design/`. SHORT-NAMES, IDS-MIGRATE's per-thread order and NAMING-REST stand, read through the work model.
- **The canonical description** is [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) and the [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note. Every run reads both first and cites the note rather than restating it. Harness and tools-ki text cites it by its canonical GitHub URL.
- Kris's answers stand in for an Enactment record for every Admin and Pillars change below that the model requires; any other canonical change needs its own record.

## Order and gates

Each phase is one or more background runs, chained where they touch the same files, under the `ki-delegation` background-run standard. A phase starts only when the one before it has landed and been pushed.

| Phase | Repository | Gate to the next phase |
| --- | --- | --- |
| 1. Harness | ki-agentic-harness | standards, skills and checkers accept both shapes, pushed, records at Awaiting review |
| 2. tools-ki and a release | tools-ki, then ki-principal's `.github/ki-version` | `ki` released with the new readers and `ki work status`, and installed on both hosts |
| 3. The Capital | ki-principal | folders, notes, work files and ids moved; audits clean with the released `ki` |
| 4. The other territories | each territory's Capital, under its own authority | each territory reports its move done |
| 5. Close the tolerance window | ki-agentic-harness, tools-ki | legacy readers removed and released |

## The moves

From the work-model report's section 7, with section 10's folder moves:

| Today | After |
| --- | --- |
| `+/_CHECKPOINTS/<initiative>.<project>.md`, `_state-of-play.md` | `+/_WORK/<id>/work.md`, front matter carrying the Work Process observatory fields |
| `+/_THREADS/<run>/decisions.md` and reports | `+/_WORK/<id>/decisions.md` and open reports; settled reports pruned |
| briefs in `~/.local/state/ki/agents/<run>/` | `+/_WORK/<id>/briefs/<run>.md` while the handoff is open |
| `ki-checkpoint` | the work-file standard; its new name is a query below |
| pick-up block, moves list | work file front matter; Git as the logbook |
| REST, BUSY, HOLD and DONE frames; resume line | the rich-text glyph banner, holder's glyph alone when settled and an arrow only in handoff; the send line |
| the copyable stacked reply block | none; Kris answers in speech, each answer read back as taken in the decisions log, one line asked where unclear |
| `hold` as a receive word; the ki-pmo hold | On hold, paused or more expected; `pause`, `done for now`, `resume`, `finish` |
| ids `ki.sop`, `ki.<initiative>.<project>` | `ki`, `ki.regular`, `ki.<project>`, `ki.regular.<slug>`; run slugs hyphenated |
| `Streams/Initiatives/` and Initiative notes | `Streams/Themes/<theme>.md`, one page per theme holding no work |
| `initiative:` on Projects, records and Activity notes | an optional `theme:` |
| Project folders holding only their note | flat `Streams/Projects/<slug>.md` |
| `Streams/**/design/` folders | `+/_WORK/ki.<project>/design/`; the territory-selection papers deleted |
| `Streams/Projects/mac-studio-setup/` script, logs and SVG | `+/_WORK/ki.mac-studio-setup/` |
| recurring work's home in an Initiative (ACT-HOME) | regular work, defined in the Capital, self-coordinating; a Project's own checks stay with it |
| "staging area" | "working area", already dispatched as `working-areas` |

## Phase 1 - harness

```text
Task, in ki-agentic-harness: write the work model into the harness standards, skills and checkers, citing the Work Process note by its canonical GitHub URL and restating none of it. Read GDR-KI-PRINCIPAL-009 and the Work Process note in ki-principal first, then this brief.

1. ki-pmo: replace thread types with the work levels and forms; the seven states, On hold with its two reasons and the drain; the receive words; the glyph banner and send line in place of the frames and resume line, a settled state showing its holder's glyph alone and an arrow only in a handoff state, the hold report keeping its Done, Parked and Left over sections; REPLY-BLOCK: drop the copyable stacked reply block from the owner report, run report and reply forms, queries keeping Context, Query and Options with confidence, the owner answering in speech and the thread reading each answer back as taken in the decisions log and asking one line where an answer is unclear; the work file in place of the pick-up block and Messages block placement; the heartbeat only while work lies with a worker; the decisions life cycle (struck, pointer or kept at each mark, no numbering); THREAD-TIDY as pruning the work folder; the Thread naming section rewritten for two-part ids with no theme segment, `ki` for territory work and `ki.regular` for regular work; design notes in `+/_WORK/<id>/design/`. Regenerate with `ki dev skill generate ki-pmo --write`.
2. ki-delegation: briefs in `+/_WORK/<id>/briefs/<run>.md`, deleted once the report is received; the run report's banner; the run report with no reply block; the decisions log in the work folder.
3. ki-checkpoint: rewrite as the work-file standard (front matter fields, next steps, Messages, parked tags; no moves list), under the name Kris chose in WORK-FILE-NAME; keep reading old checkpoints for the tolerance window.
4. ki-work's project registry standard, ki-repo-kb-streams and ki-work-roadmap: `Streams/Themes/`, flat `Streams/Projects/<slug>.md` with `theme:`, no `design/` folder anywhere under `Streams/` (the Streams checker fails one), upkeep records naming an optional `theme`; accept `initiative:` and `Streams/Initiatives/` with a warning for the tolerance window.
5. ki-repo-kb-activities and ki-work-recurring: an Activity's home is the territory's regular work or a Project; `initiative:` becomes an optional `theme:`; regular work is self-coordinating and state of play may discuss it but does not necessarily dispatch it. Amend KI-HARNESS-GOV-206 to match.
6. ki-pmo-design: the artefact home is `+/_WORK/<id>/design/`.
7. The checker contexts: `project-registry.ts`, `pmo.ts` (work files and their Project or theme), `stream.ts`; both shapes accepted with a warning on the old.
8. Records: capture one KI-HARNESS-GOV record for the write-in and its tolerance window, under project ways-of-working; amend KI-HARNESS-GOV-199, KI-HARNESS-GOV-200 and KI-HARNESS-GOV-189 where the work folder replaces the thread folder and checkpoint. Deliver to Awaiting review; do not accept.
9. Leave the `ki-coordinator` output style alone: it is chezmoi-managed. Write a ready-to-send handoff for Rig > chezmoi in the report.

Run the repository's tests, typecheck and `ki repo audit` for every touched skill; commit by explicit path, pull with rebase, push fast-forward.
```

## Phase 2 - tools-ki and a release

tools-ki belongs to the tools burndown thread's session. Send this to that thread as a handoff under KI-TOOL-KI-CLI-127; do not launch it from `ways-of-working`.

```text
Task, in tools-ki, under KI-TOOL-KI-CLI-127: add `ki work status --format json` to the ki/work-status/v1 contract in the settle-model report; teach the registry reader `Streams/Themes/` and flat `Streams/Projects/<slug>.md` with `theme:`, reading `Streams/Initiatives/` and `initiative:` with a warning for the tolerance window; have the `thread.status` parser and `ki agent`'s thread home read `+/_WORK/<id>/work.md` and the work folder, with old checkpoints and thread folders still read; show the five views (with you, stuck, blocked, moving, on hold) in `ki work status`'s text form. Tests through `run(args, context)` and `sandbox()`, `man/ki.1`, README and CHANGELOG. Then cut a release, install it on both hosts, and bump ki-principal's `.github/ki-version` by explicit path.
```

## Phase 3 - the Capital

```text
Task, in ki-principal, after the released ki is installed: move the Capital to the work model. Read GDR-KI-PRINCIPAL-009, the Work Process note and this brief first. Kris's answers stand in for the Enactment record for the Admin and Pillars edits listed.

1. Design out of Streams, first: delete Streams/Initiatives/knowledge-islands-model/design/ (its outcome is ADR-KI-PRINCIPAL-002); move each Project's design/ to +/_WORK/ki.<project>/design/ (agent-host, paperclip-capture-and-rebuild, ways-of-working, mac-studio-setup); move mac-studio-setup's adobe-remove.sh, its three run logs and favicons-headroom.svg to +/_WORK/ki.mac-studio-setup/; merge mac-studio-setup's hosts.md into Hosts, Roles and Layers and fold decisions-in-force.md into the mac-studio-setup Notes, as DESIGN-TIDY set; turn the extra H2 sections in paperclip-capture-and-rebuild and mac-studio-setup into ### subsections under Notes.
2. Themes: git mv Streams/Initiatives/ to Streams/Themes/ with Themes.md as its index; each theme a flat page under the slug WORK-THEME-SLUGS settled, saying why it is a theme, what matters, its general direction and common guidance, and holding no work, Project pointers or design pointers; the Model theme's recurring-upkeep paragraph moves to the Activity notes it describes, where they do not already carry it.
3. Projects: each Project folder that now holds only its note becomes Streams/Projects/<slug>.md; initiative: becomes theme: in all 21 notes; Projects.md and Streams.md updated; drop the "It sits under" lines.
4. Activities: initiative: becomes an optional theme: in Briefings, Tending and the Schedule; each names the territory's regular work as its home.
5. Work folders: create +/_WORK/ with its index note; convert _state-of-play.md to +/_WORK/ki/ and the ways-of-working checkpoint and thread folder to +/_WORK/ki.ways-of-working/, writing work.md with the observatory front matter and moving decisions.md and open reports; create +/_WORK/ki.regular/; move registry-removal as ki.regular.registry-removal after asking its thread; for every other checkpoint and thread folder, write one line into the state-of-play Messages block asking its thread to move itself at its next mark, as IDS-MIGRATE set. Do not touch a file another session has in flight; name it.
6. Rewrite live citations of +/_CHECKPOINTS/, +/_THREADS/, Streams/Initiatives/ and the old ids in AGENTS.md, Admin, Pillars, open roadmap records and checkpoints; leave settled reports and pinned pruned-record links as history.
7. Update the ignore block if it names the old folders.

Run ki repo audit for ki-repo-kb, ki-repo-kb-streams, ki-decision-records and ki-pmo; commit in small explicit-path commits (design tidy, themes, projects, activities, work folders, citations), pull with rebase, push fast-forward.
```

The `ways-of-working` thread strikes its decisions log to its live entries at the first mark after this phase, as DECISIONS-STRIKE set.

## Phase 4 - the other territories

The Capital has no write authority in another territory. For each, send one handoff through that territory's state of play, carrying this brief's Phase 3 steps adapted to what it holds:

- **hnr-principal**: 2 Initiatives, 7 flat Project notes and 10 checkpoints; three folders under `Streams/Projects/` (`Developer experience and build pipelines/`, `Fourth paper figures/` and `Fourth paper guidance/`) hold design papers and evidence that move to their Projects' work folders.
- **personal-principal**: 6 Initiatives and 5 Projects, 12 checkpoints; carries the ACT-WORK handoff on activity levels and the Knowledge acquisition retitle to Acquire, with Acquire intake as the PILOT-LABEL pilot under NAMING-REST.
- **legal-principal**: 6 Initiatives, 1 Project and 1 checkpoint; its Initiatives look like former roadmap themes and are for its own state of play to judge.
- **er-principal, tmx-principal, va-principal and the remaining Capitals**: a state-of-play checkpoint each, converted to `+/_WORK/<alias>/`.

## Phase 5 - close the tolerance window

When every territory reports its move done: remove the legacy readers from the harness checkers and tools-ki, release `ki`, and bump each Capital's `.github/ki-version`.

## Afterwards

- Capture an Observatory work instrument and Beacon contributor in apps-observatory.local, which is outside this Capital's choreography list, once `ki work status` is released: Kris to have it captured there.
- The `ki-coordinator` output style changes through Rig > chezmoi, from phase 1's handoff.

## Queries to settle before launch

- **WORK-THEME-SLUGS.** SHORT-NAMES renamed `knowledge-islands-model` to `model` and `platform-foundations` to `foundations`; the work-model report's folder tree, which Kris called correct, drew them with today's slugs. A flat `Streams/Themes/model.md` shares its basename with `Pillars/Philosophy/Model/Model.md`. Recommended: apply SHORT-NAMES, with path-form wikilinks such as `[[Themes/model|Model]]`.
- **WORK-FILE-NAME.** `ki-checkpoint` becomes the work-file standard. Recommended: rename it `ki-work-file` in the same harness run, keeping a pointer from the old name for the tolerance window.
