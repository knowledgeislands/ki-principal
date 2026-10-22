# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › cli150-deliver

**🤖 → 👤 Handoff to supervisor · Run report at 07:59 BST · last mark 20:20 BST**

---

## Done

- [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) is at Awaiting review, with its review packet. It was delivered from baseline `b263ca45` under HARNESS-DIRECT a). Nothing was released or accepted. Net records: 0 in every repository.
- Step 1, the harness wording: ki-agentic-harness `1fe52516`, pushed fast-forward with only my commit on top. The run prompt's report line now says "in the run's state folder and nowhere else", and the prompt shape says the launcher homes the report. The harness gate and skill audit passed, and the generated surfaces are in sync.
- Step 2, the common rules: in `~/.local/state/ki/agents/ways-of-working/`, the report lines of `_common-1018b.md`, the older `_common-1018.md` and `_common-1016.md`, `roadmap-next.queued.md` and `migrate-apply.queued.md` now name the state-folder path. They tell the agent not to commit the report into `$D`. `work-folder-design.queued.md` named no report path. No other coordinator keeps common rules, and the other queued briefs already used state-folder paths, so I sent no Messages lines. Verify 6 (no live brief names its own report in a work folder) passed.
- Step 3, the tools-ki change: tools-ki `949ff512`, pushed fast-forward with only my commit on top. `ki agent new` now fills in the state-folder report path. `launch` and `queue` now refuse with exit 1, writing nothing, a brief that sends the agent's own report into a work folder. That covers relaunches, and the dispatcher logs the refusal as `failed` and moves on. Tests, manual, command inventory, guide and changelog are updated.
- Checks: the commit gate passed. The full test suite with coverage passed (1,350 tests, thresholds met). Type-check, knip, the manual lint, rumdl and `ki repo audit` passed (no failures, 3 warnings). Repo-wide `biome check .` fails, but only on files this change does not touch (query BIOME-DRIFT).
- One deviation, recorded in the record: the refusal checks the brief before the run's home is first recorded. Without that, a refused first launch would still have written `thread.json`.

## In Progress

- The plan says step 2 is noted in the ways-of-working work file before the release. I did not write the work file, because it belongs to the coordinator.
- The run's temporary folder still holds the before-copies of the six state files and a commit log. My clean-up was declined, so `ki agent close` will refuse until it is emptied. The before-copies are the restore path for step 2.
- The refusal waits for the next `ki` release, which should run the Verify 6 check again first.

## Queries

### BIOME-DRIFT - Repo-wide Biome check fails at baseline

**Context:** `biome.json` in tools-ki still names the 2.5.12 schema, while the declared and installed Biome is 2.5.15. Lint findings also stand in files this change did not touch, such as `src/core/kb/contract.ts` and `src/commands/acquire/index.ts`. CI does not run `biome check .`, and the commit gate checks only staged files, so it has gone unnoticed. The record's Verify 7 lists it as clean.

**Query:** How should the existing repo-wide Biome failure be handled?

**Options:** a) (recommended, confidence medium - the failure is outside this record's scope and is a small, mechanical fix) Capture a tools-ki chore record through `ki-next` to move the schema to 2.5.15 and clear the findings, and review KI-TOOL-KI-CLI-150 as it stands. b) Fold the fix into KI-TOOL-KI-CLI-150 before acceptance. c) Leave it, and drop repo-wide Biome from future Verify lists.
