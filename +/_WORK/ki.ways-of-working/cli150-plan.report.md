# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › cli150-plan

**🤖 → 👤 Handoff to supervisor · Run report at 20:44 BST · last mark 20:20 BST**

---

## Done

- [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) is adopted as deliver / Now and is Ready, for the launch part only, under CLI-150-LAUNCH a). The plan runs in this order:
  1. The harness run-prompt wording: the report line says the report goes in the run's state folder and nowhere else.
  2. The coordinators move their common rules and queued briefs to the state-folder path.
  3. `ki agent new` fills in the state-folder path.
  4. `launch` and `queue` refuse a brief that sends the agent's own report into `+/_WORK/<id>/`. That covers relaunches, and the dispatcher logs it as `failed`.
  5. The refusal ships in the next `ki` release, and only after step 2.
- The record had to be split, because a Ready record is planned whole. The close-gate parse, unnumbered `decide`, `ki work message` and `ki work prune` moved unplanned to [KI-TOOL-KI-CLI-152](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-152-work-folder-housekeeping-commands.md), in triage. Net records: tools-ki +1, other repositories 0.
- Commits `c67fbcdf` (reserve CLI-152) and `27acf8ef` (plan and split) are on tools-ki `main`. The commit gate and the full `ki repo audit` passed. Pushed fast-forward; nobody else's commits were on top.
- For the coordinator: `roadmap-next.queued.md` in this run's state folder names its own report inside `+/_WORK/ki.ways-of-working/`. Once the refusal ships it will be refused, so plan step 2 rewrites it, along with the report line in `_common-1018b.md`. No other coordinator has a common-rules file.
- Report path: per the progress protocol, this report went to the state folder rather than `$D`, so I made no ki-principal commit.

## In Progress

Nothing. No implementation, no harness edit and no release were made.

## Queries

### HARNESS-DIRECT - How the harness wording lands

**Context:** Plan step 1 is a one-sentence change in ki-agentic-harness: the `run-report` source in the ki-coordination standard, the regenerated `run-prompt.md` and item 4 of the background-run standard's prompt shape. The plan has the run that delivers CLI-150 make it as a direct harness commit under CLI-150-LAUNCH a), with no harness record. The record notes this as provisional. [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) separately plans a different `run-prompt.md` line and does not conflict.

**Query:** Should the harness wording land as a direct commit from the CLI-150 delivery run?

**Options:** a) (recommended, confidence medium - your answer named "the harness wording" as part of this plan, and one sentence does not need a record of its own) Yes, a direct harness commit cited from KI-TOOL-KI-CLI-150. b) Fold it into KI-HARNESS-GOV-200, which is still in triage, so the launch part waits on that record's planning. c) Open a new harness record for it.

### 🤖 → 👤 Handoff to supervisor

1 run · 1 handoff

- [handoff to supervisor] cli150-plan: KI-TOOL-KI-CLI-150 launch part Ready, KI-TOOL-KI-CLI-152 split out · 👤 · 20:44 BST
