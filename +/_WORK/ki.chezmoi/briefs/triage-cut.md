# Brief: triage-cut

Work: KI > Rig > chezmoi (`+/_WORK/ki.chezmoi/` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`); queries and options in that folder's `queries.md`. Authority: Kris, 19 October 19:47 BST, "It can do anything that's high confidence", taking option a) of every open query. This is TRIAGE-CUT a), in `/Users/krisbrown/.local/share/chezmoi` under `ki-next` and `ki-work-roadmap`:

1. Merge KB-DOTFILES-UE-095 into KB-DOTFILES-UE-090: carry its gap into UE-090 and close UE-095 as merged, with a one-line reason.
2. Adopt KB-DOTFILES-UE-096 as a draft on Hold, release condition "KI-HARNESS-GOV-199 Phase 3 starts".
3. Leave KB-DOTFILES-UE-098 as it is.
4. Gate: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`. Report the open count after.

Commit by explicit path with a Conventional Commit subject; never push, never `chezmoi apply` beyond what this brief names. Stop and report on any unexpected gate failure. Report under the owner report with the work's report heading and `› <run name>`.
