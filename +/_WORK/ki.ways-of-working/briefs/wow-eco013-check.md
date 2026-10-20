# wow-eco013-check

Goal: find out whether KI-PRINCIPAL-ECO-013 (/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md) can go back to acceptance, and clear small loose ends.

Authority: Kris, 20 October 2026, granting acceptance: "if you can quickly now accept ... accepting new things that are waiting with you and pruning those ... getting the roadmaps down to zero"; renewed 20 October 22:03 BST: "Is there anything more that you can do by yourself without me? ... roadmap down".

Steps:

1. Run ki-principal's authoring, coordination and work-package audits (`ki` audit commands for those skills; read-only). Report what still fails, grouped by owning work folder under +/_WORK/. Fix only findings in +/_WORK/ki.ways-of-working/; for each other work still failing, append one line to that work's messages.md naming its findings (skip any work already told today, per its messages.md or git log).
2. Append one line to State of play's messages.md (the territory work `ki` under +/_WORK/): the ki-principal MOD ledger in Admin/Governance/Decisions/ sits at 9 though KI-PRINCIPAL-MOD-010 was issued.
3. Read-only: report the latest harness CI `build` result on main (`gh run list` in /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness).

Constraints: British English, ASCII hyphens only, they/them. Commit by explicit path only. Never push commits that are not your own; never --no-verify or force-push. Harness and tools-ki edits only in a worktree, fast-forwarded into local main. No `ki repo conform` without --dry-run. Create no new roadmap records; route follow-ups as a line in the owning work's messages.md. Anything needing Kris (a visual or attended check, publication, a design choice) becomes a query in your report with Context, Query and lettered Options, recommendation first with a confidence.

Report: audits pass or fail with the remaining findings by work, lines sent, harness CI result.
