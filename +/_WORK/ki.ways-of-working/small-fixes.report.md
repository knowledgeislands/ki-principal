# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › small-fixes

**🤖 → 👤 Handoff to supervisor · Run report at 19:33 BST · last mark 19:08 BST**

---

## Done

- **ACQUIRE-CHECKPOINTS:** acquire `2a36d3c`, pushed. The old checkpoint is now the work file [kb.regular.acquire-intake](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/work.md).
  - The id is ad hoc work in the Personal territory (`kb`), with the stem `acquire-intake` as its slug, following Work naming.
  - The work file is `on-hold`, paused until Kris resumes the conversation. It keeps `created_at` and treats the 10:17 UTC checkpoint as its mark.
  - `+/_CHECKPOINTS/` and its README are removed.
  - The work-folder audit no longer fails on `+/_CHECKPOINTS/`. It now fails on the tracked `+/_THREADS/acquire-intake/` (39 files), which the audit says must not sit beside `+/_WORK/`. See ACQUIRE-THREADS.
- **`ki repair`:** the dry run proposes no repairs. It fails only on `ki-pmo` and `ki-pmo-design` in the live user configuration, which is USER-SKILL-STALE, so there was nothing to apply.
- **DEPS-HOLDS, vallearmonia:** apps-vallearmonia.com `f790d34`, pushed. New record [VA-WEBSITE-OPS-004](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-OPS-004-adopt-happy-dom-21.md), "Adopt happy-dom 21", is a Next draft, and the OPS ledger moves to 004.
  - Checks: the record passes rumdl and the gate.
  - Its only roadmap-audit finding is the identifier-format failure every record in that repository already has. That repository's roadmap carries 40 failures that predate this run.
- **DEPS-HOLDS, observatory:** a Messages line to `ki.observatory` asks it to refresh the notices for Mermaid 12.2.0 and lift the hold. The Vitest and `@types/node` holds stay as they are.
- **CLI-DEPARTURES:** a Messages line to `ki.tools-burndown` lists the departures by tool for mgit, Rig and ki. `-f, --filter` is left out because it is open as CLI-F-FILTER. The line links the report pinned at `06acbc1`, so the link survives the prune.
- **USER-SKILL-STALE:** a Messages line to `ki.chezmoi` asks it to check `ki-coordination` and `ki-work-design` in `chezmoi diff` and include them in Kris's next reviewed apply.
- **Commits in ki-principal:** `1451ba1`, `70d82c7` and `444b9b0` add the three Messages lines. `62b9791`, `a8349dc` and `1790ba0` correct the times on those lines, which I had first stamped 19:46 BST by mistake. All six are pushed, each through the gate with the audit passing. No other session's commits were stacked with them.
- **Net records:** apps-vallearmonia.com +1, acquire 0, ki-principal 0.
- **Report path:** this report is at the state path only, because the progress protocol makes that the only report path, overriding the `$D` path in the common rules. The launcher homes it.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Another session's untracked file, `+/_WORK/ki.chezmoi/mark-tidy-current.report.md` in ki-principal, was left alone. `+/_WORK/ki.chezmoi/decisions.md` is no longer dirty.
- The `ki.chezmoi` Messages list is out of order: its FIRST-STEP line is not first. I only added my line at the end, as the previous sender did.

## Queries

### ACQUIRE-THREADS - acquire's retired threads folder now fails the audit

**Context:** With `+/_WORK/` now in acquire, the work-folder audit fails STRUCTURE-1 on the tracked `+/_THREADS/acquire-intake/`.

- The folder holds 31 run reports and `decisions.md`, which fit the work folder's closed list.
- It also holds `local-working.md` and `ways-of-working-wrap-up.md`, which the new work file links as its working record. Neither is on the closed list.
- It also holds `binary-probe/`, a README and four Python scripts with tests. Scripts never belong in a work folder.

The brief authorised only the checkpoint move, so I left the folder alone.

**Query:** Should one acquire run move this folder into `kb.regular.acquire-intake` and remove `+/_THREADS/` there?

**Options:**

a) (recommended, confidence medium - it finishes the migration ACQUIRE-CHECKPOINTS started and clears the audit, but placing the working record and probe needs judgement) Authorise one acquire run to do four things, then commit and push:

- Move `decisions.md` and every report with an open query into the work folder, and delete the reports that are answered and homed.
- Fold `local-working.md` and the wrap-up into the work file or a `design/` note.
- Move `binary-probe/` to acquire's tooling home if it is still used, or delete it with Git holding it.
- Remove `+/_THREADS/`.

b) Leave it for acquire's own session to migrate when Kris resumes it, through a FIRST-STEP line in its work file, accepting that the audit fails until then.

### 🤖 → 👤 Handoff to supervisor · since 19:33 BST

👤 1 with you

- [with you] ACQUIRE-THREADS · owner · since 19:33
- [committed] acquire, apps-vallearmonia.com and ki-principal, pushed
