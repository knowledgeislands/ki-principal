# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › work-package-enact

**🤖 → 👤 Handoff to supervisor · Run report at 14:12 BST · last mark 13:37 BST**

---

## Done

- Committed `f5781619` in ki-principal, `docs(model): bring the work model to the work package`, local only; the commit gate's scoped audit passed with no findings on the three paths.
- [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) brought to the decided model: the work package and its work folder; five files created together, with what each holds and when it is read; nothing in the package is a log; the inbox as a priority queue, with similar items grouped and important lines at the top taken first; a new Routing and stewardship section (State of play as the single dispatch coordinator, already-owned units going direct, routed work that cannot be rejected and is returned at most once before going to Kris, held work keeping its hold, continual improvement coordinated by State of play, a significant change reviving Ways of working or a targeted Project under the Model theme, Ways of working's direct refresh while the method is being defined, and targeted refresh using the recorded method revision); the Words table, the Homes tree, On hold parking in the queries and state files, and the Observatory reading both shapes.
- [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) refined in place, `updated` set to 19 October: Kris's 19 October words added to Context; the Unit, Territory work, On hold, Homes and observatory points rewritten; new Inbox, Routing and Stewardship points; two consequences, one naming `ki-work-package` as owner of the exact form and one setting readers first, then one pass. It links no other note and cites no later record.
- The [Processes](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Processes.md) index entry for Work Process now names the work package, routing, the priority queue and stewardship. The [Decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/Decisions.md) index entry needed no change.
- No other Admin or Pillars text names `ki-work-folder`: the only live reference is `.ki.toml`. The work-model diagram shows no files, so it needs no change.
- Full repository audit: run before and after; unchanged at 15 failures and 26 warnings, all already present in other works' reports, folders and Decision Records, none in the files this run touched.
- No records: net change 0 in ki-principal. Kris's instruction stood in for an Enactment record.
- Not pushed: 13 other commits sit unpushed beneath mine. Ten belong to `ki.ways-of-working`'s coordinator: `53c11a0f`, `872a4172`, `0c67f927`, `51d681ca`, `3d12ecc5`, `e10889b0`, `3fd3e041`, `1fc93b73`, `db12ad33` and `a9b75552`. Two belong to `ki.knowledge-acquisition`: `9011db12` and `585a7d1d`. One is `82db4e67`, "reconcile completed coverage and remaining handoffs", whose owner is unknown.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- `.ki.toml` still declares `[skills.ki-work-folder]`. With `[skills.ki-work-package]` declared, `ki repo audit` refuses to run at all, because no installed harness provides that skill yet; the harness checkout has no `ki-work-package` either. I reverted the line, and it is the subject of the query below.
- The Work Process note and GDR-KI-PRINCIPAL-009 describe `ki work status` reading `state.md` or `work.md`. That reader is the handoff to `ki.tools-burndown` and is not yet released. The text describes the decided model, not what is installed today.
- The note says "marked important" and leaves the exact syntax of the flag to `ki-work-package`, which work-package-standard is writing.
- `+/_WORK/ki.ways-of-working/design/work-package.md` is uncommitted and belongs to work-package-standard. I did not touch it.
- [Chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) in `Streams/Projects/` still says "checkpoint" and `ki-checkpoint`. That is outside this run's Admin and Pillars scope, and its own work or the migration pass should pick it up.

## Queries

### KI-TOML-PACKAGE - When to switch the skill declaration to ki-work-package

**Context:** The brief asks for `.ki.toml` to declare `[skills.ki-work-package]`. The installed `knowledgeislands/ki-agentic-harness` does not provide that skill yet, so with the new declaration the whole repository audit stops with "declared skill ki-work-package is provided by no declared harness". The commit gate would fail too. The harness rename, with the deprecated `ki-work-folder` alias, is work-package-standard's to land, and it must then be installed. Until then, the old declaration is the only one that works.

**Query:** Should the declaration switch in a short follow-up once the renamed harness is installed, rather than now?

**Options:**

a) (recommended, confidence high - verified directly: the audit refuses the new name today, and the alias makes the old name safe meanwhile) Keep `[skills.ki-work-folder]` for now, and add a one-line step to the migration pass's gate: switch to `[skills.ki-work-package]` and run the audit once `ki inventory` shows the renamed harness installed.

b) Switch it now and accept that the audit and commit gate fail in ki-principal until the harness is installed.

### 🤖 → 👤 Handoff to supervisor · since 14:12 BST

👤 1 with you

- [with you] KI-TOML-PACKAGE · owner · since 14:12
- [committed] Work Process note, GDR-KI-PRINCIPAL-009 and Processes index, `f5781619`
- [unpushed] ki-principal, 13 other commits stacked beneath
