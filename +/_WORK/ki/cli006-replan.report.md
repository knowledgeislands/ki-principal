# [Techne](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/techne.md) › [Agent host](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/agent-host.md) › cli006-replan

**🤖 → 👤 Handoff to supervisor · Run report at 00:49 BST · last mark 15:59 BST, 15 October**

---

## Done

- Re-checked the [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) plan against tools-techne `e7dc018` and ki-techne-harness `9366496`, and updated it in place. It stays `deliver / draft / next`, and nothing is implemented. Goal and boundary are unchanged.
- What the re-check found and the plan now covers:
  - The host-patching work already parses the recipe's `[status]` table and validates `updates`. The plan builds on that and folds its separate updates read into the one structured read, keeping `workspace.updates` in v3.
  - The shipped `techne host status` reports an at-risk or unknown host as failed, with exit 1, because the Harness text route exits 3 or 4.
  - The CLI lays the administrator `AWS_PROFILE` over the recipe's per-script profiles, so stop would run under the wrong role. There is now a step to fix it, with tests.
  - `destroy.sh` refuses unless `CONFIRM_DESTROY_AGENT_HOST` equals the stack name. The manifest doesn't declare this variable, and the 12 October plan missed it. The plan now passes it through from your environment and never sets it.
  - The test fixture has no `[operations]` table.
  - The CLI-008 sequencing note is replaced: CLI-008 has landed. A note on [KI-TOOL-TECHNE-CLI-009](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-009-tailscale-oauth-binding-field.md) says the two records' writers should run one after the other.
- Added `size: l` and a Replan note, and moved `updated_at` forward. `created_at` is unchanged.
- Commit `31c7b7d` in tools-techne, local, not pushed.
- Checks:
  - ki-work audit: passed.
  - ki-work-roadmap audit: no warning left on CLI-006. One warning remains on CLI-009, which has no `size`.
  - ki-authoring audit: one existing warning, `.rumdl.toml` drift, which I didn't touch.
  - rumdl: clean.
  - `git diff --check`: clean.
  - Commit hooks: passed.
- Added the outcome line to `ki-principal/+/_WORK/ki.agent-host/decisions.md` with `ki agent decide`, under the CLI006-PLAN entry. I did not commit it.

## In Progress

- In ki-principal, `+/_WORK/ki.agent-host/decisions.md`, `queries.md` and `state.md` already had another session's uncommitted changes. I added only the one decisions line and left all three files uncommitted for that session.
- Follow-ups, with no records created under CAPTURE-GATE:
  - A non-blocking request to the Harness to declare the destroy confirmation in the manifest's `[operations]` table, if you choose b) below.
  - A `size` for CLI-009.
  - The `.rumdl.toml` drift from the house template. Conforming it needs care because of HOOKS-MIGRATION.
  - If CLI-006 is held back, a small separate fix so `host status` stops reporting exit 3 and 4 as failures.

## Queries

### CLI006-CONFIRM

**Context:** `destroy.sh` will only run if `CONFIRM_DESTROY_AGENT_HOST` is set to the stack name. The recipe manifest doesn't declare this variable, and under ADR-KI-PRINCIPAL-006 the manifest is the only contract between the CLI and the Harness. So the CLI can't name the variable without hard-coding something from the Harness. The plan now passes your own environment through, and the CLI never sets the variable.

**Query:** How should `techne host rebuild` and `withdraw` meet this confirmation?

**Options:**
a) (recommended, confidence medium - it works today with no Harness change and leaves the guard with the script, but you must export the variable for each run) Pass it through from your environment, with the CLI docs pointing to the Harness operator guide.
b) Ask the Harness to declare the confirmation in its `[operations]` table so the CLI can prompt for it. Rebuild and withdraw would wait for that change.
c) Have the CLI prompt for the stack name and set the variable itself. This hard-codes an undeclared Harness variable.

### CLI006-READY

**Context:** The replanned [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) is ready for your review. It makes structured status authoritative under v3 and list v2, and keeps `workspace.updates`. Stop goes through its script under the operator profile. Rebuild and withdraw go through `destroy.sh` under the administrator profile, and teardown becomes a diagnostic that only exits 2. All checks use injected runners, with no live operation. Setting it to Ready also accepts CLI006-CONFIRM's answer and the choice to keep `workspace.updates`.

**Query:** Should KI-TOOL-TECHNE-CLI-006 be set to Ready?

**Options:**
a) (recommended, confidence medium - the plan is grounded in today's sources and passes its audits, but the confirmation route is still open) Review it, and once CLI006-CONFIRM is answered, have a ki-plan run set it to Ready.
b) Set it to Ready now, taking CLI006-CONFIRM a).
c) Keep it as draft at `next` for now.
