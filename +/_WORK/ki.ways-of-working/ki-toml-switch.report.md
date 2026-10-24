# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › ki-toml-switch

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 14:18 BST**

---

## Done

- Renamed `[skills.ki-work-folder]` to `[skills.ki-work-package]` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/.ki.toml` (line 136, an empty table with no keys and no sub-tables).
- `ki repo audit`: failed, on one error only: "declared skill ki-coordination requires declared dependency ki-work-folder". The installed harness ships `ki-work-package`, but its `ki-coordination` SKILL.md still names `ki-work-folder` as a dependency.
- Commit: not made. The pre-commit gate's formatter passed, but the gate runs the same audit and refused on that same dependency error. Nothing was bypassed and nothing was pushed.

## In Progress

Nothing is running. `.ki.toml` is left modified and uncommitted in ki-principal, holding only the rename.

Outstanding - no action requested now: `+/_WORK/ki.ways-of-working/decisions.md` was already dirty from another session when this run started, and was not touched.

## Queries

### KITOML-GATE - ki-coordination still requires ki-work-folder

**Context:** You allowed fallout in other places, but the failure blocks the commit itself. The `ki-coordination` skill in ki-agentic-harness still lists `ki-work-folder` as a dependency, so any audit of ki-principal with the renamed table fails. While `.ki.toml` stays renamed in the working tree, every other session's commit in ki-principal will probably fail the same gate.

**Query:** Should the harness's ki-coordination dependency be changed to ki-work-package before this rename is committed, or should the rename be reverted until that change lands?

**Options:**
a) (recommended, confidence medium - this fixes the cause and keeps one source of truth; the dependency line was read directly but not traced through the CLI resolver) Launch a run in ki-agentic-harness that changes ki-coordination's dependency, and any other references to ki-work-folder, to ki-work-package and installs the harness; then commit this `.ki.toml` change as briefed.
b) Revert the one-line rename in ki-principal now so other sessions' gates pass, and reapply it after the harness change.
c) Also declare an empty `[skills.ki-work-folder]` alongside `ki-work-package` as a temporary bridge so the gate passes now.
