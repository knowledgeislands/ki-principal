# plan062 brief

Run for the work `ki.mac-studio-setup` in Knowledge Islands Principal.

## Task

Take [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) to Ready with `ki-plan`. Plan only: do not implement. Account for what KI-TOOL-RIG-CORE-063 has just changed in the tests.

## Authority

- Owner decision, Kris, 2026-10-19 19:55 BST, on RIG-ORDER: "All three are high confidence to do them", taking option a): plan and deliver KI-TOOL-RIG-CORE-063 in the background now, then plan KI-TOOL-RIG-CORE-062 and KI-TOOL-RIG-CLI-027.
- Work only in `/Users/krisbrown/workspaces/knowledge-islands/tools-rig`. Before you start, run `git -C /Users/krisbrown/workspaces/knowledge-islands/tools-rig status`; if another session has uncommitted changes there, do not touch them, and stop and report if they overlap the files you need.
- Commit only your own completed, verified unit, staged by explicit path under `ki-git`, with Conventional Commit subjects ending in the attribution line `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Never use `--no-verify`.
- Do not push, release, tag, accept, prune or touch any other repository. No remote operations beyond `git fetch`. Do not change sol's or terra's live configuration: no `chezmoi apply`, `rig apply`, `sudo`, launchd loads or firewall changes.
- If the work needs a decision from Kris, stop at a safe point and raise it as a query.

## Report

Write `/Users/krisbrown/.local/state/ki/agents/mac-studio-setup/plan062.report.md` in the `ki-coordination` owner-report shape for a run report: Done, In Progress and Queries, each query with Context, Query and lettered Options, the recommended one first with confidence and reason. Cite every record by its full identifier, linked to its local file by absolute path. Name every commit you made, and the record's resulting status. Use British English and ASCII hyphens only.
