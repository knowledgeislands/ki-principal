# plan069 - plan KI-TOOL-RIG-CORE-069 to Ready

Work: ki.prj.mac-studio-setup (KI > Rig > Mac Studio setup). Dispatched through Orca Run `run_0de85069bc1d` under ORCA-HOST (Kris, 29 October 2026). Authority: GO-PLAN a) (Kris, 30 October 2026, 00:2x GMT).

**Target:** `/Users/krisbrown/workspaces/knowledge-islands/tools-rig`, record `docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md` (draft, horizon now, size s), and the code, specification and tests it names, read only for planning. Related: KI-TOOL-RIG-CORE-070 (awaiting review, handler read-back), which you may read but not change.

**Change:** plan KI-TOOL-RIG-CORE-069 under the `ki-plan` skill until it is Ready, or as far as planning can go without touching the live machine. On 20 October planning stopped at RIG-069-PROBE, an attended handler change at sol's screen (rungs `legacy`, `modern`, `workspace`, with `observe` after each). The record was touched again on 23 October; first establish from its history (`git -C <tools-rig> log -- <record>`) whether that probe or later evidence has since settled the native setter. If Ready needs the live probe, leave the record at draft with the plan otherwise complete, and raise a query instead of probing.

**Constraints:**

- No sudo, no `rig apply`, no handler change, no `duti`/LaunchServices write, no live probe and no other system change. Read-only commands on sol are allowed.
- No implementation (`ki-implement`), no acceptance (`ki-accept`), no new records (BURN-DOWN, CAPTURE-GATE).
- Never stash, rebase, reset, force-push or use `--no-verify`.
- Leave other sessions' uncommitted files alone; name any you meet in the report.

**Ownership:** you may edit only the KI-TOOL-RIG-CORE-069 record (and the tools-rig roadmap index if `ki-plan` requires it), and write your report. Commit each by explicit path. In tools-rig, commit locally then `git pull --ff-only` and `git push` fast-forward only; stop and report on divergence. In ki-principal, commit only your report the same way.

**Report:** write `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/plan069.report.md`: the record's resulting status, what changed and why, evidence (commit ids, the record history you relied on), anything left over, and every query in full as `### <TAG> - <title>` with **Context**, **Query** and **Options**, the recommended option first as `a) (recommended, confidence <level> - <reason>)`. Also note, in a short `## Orca` section, anything about heartbeats, ask/reply or `worker_done` that was awkward or unclear. Use British English and ASCII hyphens.

**Observable acceptance:** the record is at `ready` with an implementation plan `ki-plan` accepts, or at `draft` with a query naming exactly what blocks Ready; both commits pushed; the report exists in ki-principal at the path above; `worker_done` sent with `--report-path` set to that path.
