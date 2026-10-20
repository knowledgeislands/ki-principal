# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › ki-brew

**🤖 → 👤 Handoff to supervisor · Run report at 00:00 BST · last mark 00:00 BST**

---

## Done

- Homebrew: `brew update` refreshed the `knowledgeislands/tap` tap; the `ki` formula now offers 0.11.5, matching the latest local tools-ki release tag `v0.11.5` (tagged 2026-10-19 19:52 BST).
- Homebrew: `brew upgrade ki` took `ki` from 0.11.4 to 0.11.5; `/opt/homebrew/bin/ki --version` confirms 0.11.5. Nothing else was upgraded; no repository was written to and nothing was committed.
- Tonight's hooks-migration release is **not** in the formula yet. The Husky-to-`.githooks` work (`feat(repo): convert Husky commit gates to committed githooks in conform`, `chore(hooks): move the commit gate to committed githooks and retire husky`, `fix(bootstrap): pin the harness carrying the githooks standard`) comes after `v0.11.5` in [tools-ki](/Users/krisbrown/workspaces/knowledge-islands/tools-ki). It is staged in `chore(release): prepare v0.12.0` (23:51 BST), but there is no local `v0.12.0` tag and the formula still points at the v0.11.5 assets. I made no fetch to check the remote, so the worker should rerun this once v0.12.0 is tagged and the tap is bumped.

## In Progress

Nothing is running.

Outstanding - no action requested now: rerun KI-BREW once tools-ki v0.12.0 is published and the tap formula is updated.

## Queries

No outstanding queries
