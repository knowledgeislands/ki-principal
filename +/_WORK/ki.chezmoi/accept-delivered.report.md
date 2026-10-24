# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › accept-delivered

**🤖 → 👤 Handoff to supervisor · Run report at 03:04 BST · last mark 02:41 BST**

---

## Done

- Closed [KB-DOTFILES-UE-082](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-082-tolerate-missing-template-tools.md), [KB-DOTFILES-UE-088](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-088-ssh-alias-for-sol.md) and [KB-DOTFILES-UE-092](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-092-restore-local-skill-projection.md) as `done` through `ki-accept`, on Kris's "accept them" (Decision 155), in local commit `7cb547a`. Nothing was pushed or pruned.
- All three records were still `draft`, delivered before Ready. Each one now has a `baseline_ref` taken from Git (the parent of its first delivery commit), every Step ticked, a six-part `## Review` built from its recorded delivery evidence plus fresh checks on sol, a `## Done` line, and a Discussion note "Acceptance before Ready".
- Recorded deviations: delivery commit `0091d88` for KB-DOTFILES-UE-092 also carried unrelated changes. The Documentation impact of KB-DOTFILES-UE-082 was never assessed, and its delivery changed no guide, Decision Record or Specification.
- `ki repo audit --repo .`: no failures, 12 warnings, all in the permitted baseline or `CLAUDEBIND-1`, identical before and after.
- `node --test tests/*.test.mjs`: 290 passed, 0 failed, 2 skipped.
- `rumdl check .`: clean.
- The working tree is clean and no `.git/*.lock` remains.

## In Progress

Nothing. Following the done-before-prune rule, the done state is committed first; pruning these records is left for a later, explicitly selected prune.

## Queries

**PRUNE-ACCEPTED**

**Context:** The three records are now committed as `done`. The brief permits no pruning, so they stay in `docs/roadmap/`.

**Query:** Should they be pruned now?

**Options:** a) (recommended, confidence high - their done state is committed, and the prune only needs the reference preflight and one prune-only commit) Queue a prune run for the three records by explicit path. b) Keep them until the next routine roadmap sweep.

**UE-082-FOLLOWUPS**

**Context:** Two planning questions on [KB-DOTFILES-UE-082](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-082-tolerate-missing-template-tools.md) were never taken up:

- Should `rig doctor` or `chezmoi status` also report a declared MCP server whose command is absent, after the first apply?
- Should bare commands resolve to a stable path?

The capture gate barred new records, so the Review lists them only as not pursued.

**Query:** Should either become work?

**Options:** a) (recommended, confidence medium - a warning shown only during apply is easy to miss once the first run has passed) Capture one triage record for a persistent absent-command finding, and drop the path-stability question. b) Drop both. c) Capture both.

### 🤖 → 👤 Handoff to supervisor · since 03:04 BST

👤 2 with you

- [with you] PRUNE-ACCEPTED · supervisor · since 03:04
- [with you] UE-082-FOLLOWUPS · supervisor · since 03:04
- [committed] three acceptances in chezmoi, local, unpushed
