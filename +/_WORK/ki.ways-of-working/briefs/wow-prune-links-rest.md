# wow-prune-links-rest

Goal: PRUNE-LINKS-REST. Kris has pushed the harness, apps-observatory.local and ki-specifications, and this work pushed its own commits on top (harness origin/main 2784c999). Prune these accepted records under ki-work-roadmap: KI-HARNESS-GOV-170, -199, -200, -205, -214, -215, -216, -219, -220, -221, -222, -223 and -226 (in /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/), KI-OBSERVA-OPS-003 and KI-OBSERVA-VIS-027 (apps-observatory.local), KI-SPEC-RGV-004 (ki-specifications) and KI-TOOL-KI-CLI-159 (tools-ki).

Authority: Kris, 20 October 2026, granting acceptance: "accepting new things that are waiting with you and pruning those"; renewed 22:03 BST: "Is there anything more that you can do by yourself without me? ... roadmap down".

Override: for these records only, this grant overrides any standing rule against pruning records.

Steps: for each record, confirm it is accepted (done) and that its last revision is on origin; skip and report any that is not. First repoint every live link to it across the KI repositories (ki-principal, harness, tools-ki, Observatory, specifications, website) to the pinned form [<ID> (pruned)](<https://github.com/><owner>/<repo>/blob/<last revision on origin>/<path>), never inventing a revision; then remove the record file and update any index. Harness and tools-ki edits in worktrees, fast-forwarded into local main. Commit by explicit path. Then push each repository fast-forward only, but only where every commit ahead of origin is your own or from ways-of-working runs this evening (subjects naming ways-of-working, KI-PRINCIPAL-MOD-008, knip, CI time limits, KI-OBSERVA-BRG-006 or GOV-219/224); never push a repository carrying another session's commit (ki-principal carries three ki.chezmoi commits, so leave it unpushed). Never --no-verify or force-push.

Constraints: British English, ASCII hyphens only. Create no new records. No ki repo conform without --dry-run.

Report: each record pruned with its pinned revision, links repointed per repository, commit SHAs, and which repositories were pushed or left unpushed and why.
