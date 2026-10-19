# ready-rest

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol.

Authority: READY-REST a), Kris on 19 October, 23:43 BST: "go ahead". Split held gap 1 (the Headroom deployment, waiting on KB-DOTFILES-UE-087) out of KB-DOTFILES-UE-090, then move the rest of UE-090 to Ready. KB-DOTFILES-UE-076 stays draft ([bringup-fold](/Users/krisbrown/.local/state/ki/agents/chezmoi/bringup-fold.report.md)).

Retry authority: READY-PREFLIGHT a), Kris on 19 October, 23:47 BST: "yes you can retry". A one-run exception to the `ki-plan` and `ki-next` stop-on-warning preflight, for exactly the 20 existing roadmap migration warnings the first attempt found (16 missing sizes, four retired `initiative` fields, all in other records) ([first attempt](/Users/krisbrown/.local/state/ki/agents/chezmoi/ready-rest-1.report.md)). Record that baseline before writing; stop on any warning or failure outside it. Do not fix the 20 warnings.

Third-attempt authority: READY-GATE a) and READY-DETAIL a), taken under Kris's standing authority for high-confidence work ([second attempt](/Users/krisbrown/.local/state/ki/agents/chezmoi/ready-rest-2.report.md)). The exception also covers the three existing full-audit warnings: `.rumdl.toml` drift from the house template, the ADR-KB-DOTFILES-003 amendment heading, and the absent `.githooks/pre-commit`. Leave all 23 unchanged; reuse `ready-rest-2.baseline.json`, extended by those three, and stop on anything else. After the split, shape under `ki-plan` the gap-5 per-target fallback for `audit-chezmoi-health` (Step, touched files, verification) and the size-l item's bounded delivery and review rounds per the roadmap's Delegation contract. Mark UE-090 Ready only if the complete readiness assessment then passes; otherwise commit the split and shaping and report what is missing.

Task:

1. Use the repository's roadmap tooling (`ki repo roadmap`, under `ki-plan` and the roadmap standard) to reserve and capture a new record for gap 1, carrying its text, its hold on KB-DOTFILES-UE-087 and a link back to UE-090. Link it from UE-090 and UE-087.
2. Remove gap 1 from UE-090's delivery scope, leaving a pointer to the new record.
3. Move UE-090 to Ready under `ki-plan`, only if its readiness checks pass. If they do not, stop and report what is missing as a query.
4. Run the gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`. Commit by explicit path.

Constraints:

- `bin/chezmoi/json` may carry a change that is not yours: leave it alone and do not stage it.
- Do not push, apply or fetch. Never run `ki repo conform` without `--dry-run` (HOOK-GUARD). Leave no `.git/*.lock`.

Report: the run report form, heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › ready-rest`, linking every record by its full identifier.
