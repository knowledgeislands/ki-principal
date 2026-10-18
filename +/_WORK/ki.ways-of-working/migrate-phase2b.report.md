# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › migrate-phase2b

**🤖 → 🧑 Handoff to supervisor · Run report at 04:50 BST · last mark 22:34 BST**

---

## Done

- Phase 2 has landed in tools-ki and is pushed fast-forward. The registry reads `Streams/Themes` and `+/_WORK`, including `_WORK_REVIEW`, and still reads the legacy shapes.
- `ki work status [--repo <dir>] [--format json]` ships as `ki/work-status/v1`. It shows the five views with their glyphs, gives review as a count, and warns on bad work files. It has tests, help, the man page, the README and spec [REPO-OPS-028](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/specs/repository-operations.md). [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md) is widened to cover the work-model readers and is back at Awaiting review.
- `ki agent` keeps its name. A new run is homed in the `+/_WORK/<id>/` folder whose slug equals the run name, and falls back to `+/_THREADS/<run>/`. If two work folders share the slug, the launch refuses and names them. `ki agent home <run>` prints a run's home, and `--work <id>` re-homes it to an existing work folder without moving any file.
- Five choices were made under [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md):
  - `identity` is the repository identity, not `<alias>:<id>`;
  - role is null when the holder is a third party;
  - moving is everything not in another view;
  - a legacy checkpoint's alias comes from the first work file, then `territory_aliases`, `territory_prefix` and the folder name;
  - re-homing moves no file.
- `ki work status` now reads the work file directly, replacing the `thread.status` parser, as ki-pmo foresaw.
- tools-ki v0.11.0 is released and installed on this host through the documented process:
  - the harness pin carrying the work model, then release preparation;
  - full checks passed: 1291 tests at 100% coverage, types, lint, unused-code, man-page and repository audits, CI, and a build and install trial;
  - the tag and the release workflow, giving an immutable release with five assets;
  - the Homebrew tap's automatic PR merged, and `brew upgrade` delivered 0.11.0.
- Against ki-principal as phase 3 left it at 04:47, `ki work status` reads nine work files, all `ki.*`: one stuck (this Project), eight on hold and five awaiting review. Read-only, no warnings.
- Mechanical steps:
  - scripted renames and replacements;
  - regenerating the command inventory;
  - the harness pin and version bump;
  - tag, release workflow, tap merge and `brew upgrade`;
  - every gate.
- By hand:
  - the design of `ki work status` and of the thread home;
  - the tests;
  - man page, README, guide and spec prose;
  - the widening of [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md);
  - this report.

## In Progress

- The ki-principal pin bump to v0.11.0 is committed locally by the phase 3 session `migrate-apply` but not yet pushed, so I left it alone rather than add a second commit. That session is also working through ki-principal's audit failures. Those predate this release: link debt in older reports, a hook layout and checkpoint scaffolds.
- The other host still has ki 0.10.5; nothing here can reach it. Its next session should run `brew update` and `brew upgrade knowledgeislands/tap/ki`.
- On this host `~/.local/bin/ki`, a local runner over the tools-ki checkout, comes before Homebrew's `ki` on PATH. Both report 0.11.0.
- `apps-knowledgeislands.info/apps/site/src/_data/cliCommands.json5` still names `ki repo roadmap --by initiative`, which the theme change removed. It needs a site update; I did not touch it.
- The question of who owns ki-repo, raised in phase 1, is still open.

## Queries

### REHOME - the ways-of-working run still points at the removed `_THREADS` folder

**Context:** Phase 3 moved this Project into `+/_WORK/ki.ways-of-working/`, but this run's recorded home is still `+/_THREADS/ways-of-working/`, which no longer exists. The work folder's slug is `ki-ways-of-working`, so it does not match the run name `ways-of-working`. Launches into this run will write to the old path until it is re-homed. I did not re-home it, because this coordinator is live and phase 3 is still moving folders.

**Query:** Should the coordinator re-home this run to its work folder now?

**Options:**

a) (recommended, confidence high - one recorded pointer, no files move) The coordinator runs `ki agent home ways-of-working --work ki.ways-of-working` once `migrate-apply` reports DONE, then checks that `ki agent home ways-of-working` prints the work folder.

b) Fold the re-home into a phase 4 run, along with any other runs whose names differ from their work slugs.

c) Rename future runs to the work slug, such as `ki-ways-of-working`, so that homing is automatic, and let this run's old pointer lapse.

### 🤖 → 🧑 Handoff to supervisor · since 04:50 BST

🧑 1 with you · 🤖 1 moving

- [with you] REHOME · owner · since 04:50
- [moving] ki-principal pin bump and audit · migrate-apply · since 04:43
- [committed] tools-ki v0.11.0, released and installed on this host
- [committed] this report
