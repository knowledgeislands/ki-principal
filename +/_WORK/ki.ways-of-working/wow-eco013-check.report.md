# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-eco013-check

**🤖 → 👤 Handoff to supervisor · Run report at 22:06 BST · last mark 09:27 BST**

---

## Done

- [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md) cannot go back to acceptance yet: its review requires the governing audits to pass, and two of them still fail, though no failure is in this work's package.
- `ki-authoring` audit: passes, with one warning (OWN-1, `.rumdl.toml` drifted from the house template). The two MD-mech failures the review found in this work folder are gone.
- `ki-work-package` audit: fails, 39 failures and 48 warnings. Failures by work: `ki` (State of play) RECORD-2 ×5; `ki.agent-host` RECORD-2 ×1; `ki.baseline-rollout` FOLDER-1 ×1, RECORD-2 ×3; `ki.chezmoi` RECORD-2 ×1 (its `messages.md` is now empty and must say at least "None"); `ki.mac-studio-setup` FOLDER-1 ×1, RECORD-2 ×2; `ki.observatory` RECORD-2 ×12; `ki.portable-specifications` RECORD-2 ×5; `ki.regular` RECORD-2 ×1; `ki.timelines` RECORD-2 ×2; `ki.tools-burndown` FOLDER-1 ×1, RECORD-2 ×3; STRUCTURE-1 ×1 on the stray `+/_WORK/ki.specifications` folder.
- `ki-coordination` audit: fails. It repeats every work-package failure above and adds COORD-7 (unlinked record identifiers in reports): `ki.baseline-rollout` ×12 and `ki.mac-studio-setup` ×18.
- `ki.ways-of-working`: no failures, so I had nothing to fix. It has three warnings: the Now section of `state.md` runs past 5 lines, its body runs past 400 words, and `queries.md` holds 19 open queries, over the limit of eight.
- Lines sent for step 1: none. Every failing work was already told today: commit `862751d2` routed the findings to each work, the COORD-7 findings are already in the `messages.md` of `ki.baseline-rollout` and `ki.mac-studio-setup`, and the `ki.specifications` folder was routed to State of play.
- Step 2: sent State of play the MOD-LEDGER line in commit `3d3f4b5d`, and the pre-commit audit passed. One correction: the ledger lives in `Streams/Roadmap/_ISSUES.md` (`MOD: 9`, reserving through `009`), not in `Admin/Governance/Decisions/`. The fact checks out: [KI-PRINCIPAL-MOD-010 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/6bd48a41/Streams/Roadmap/KI-PRINCIPAL-MOD-010-work-model-terminology-sweep.md) was issued, accepted and pruned. The line asks for the ledger to go to 10.
- Step 3: not run. `gh run list` calls the GitHub API, which the brief's no-remote rule forbids, and only a push rule can override that rule. See CI-CHECK.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The other works need to clear their findings before KI-PRINCIPAL-ECO-013 can have a fresh review packet. All of them have been told.
- `ki.chezmoi`'s single RECORD-2 failure came from its own clean-up today (commits `7e650b93` and `d9ca50ee` left its `messages.md` with no body). It is a one-line fix in its own folder, and I did not send it a second line, as the brief's once-a-day rule requires.
- State of play's `state.md` already listed the MOD ledger gap among the items carried for ways of working, so the new line repeats a known item.

## Queries

### CI-CHECK - Reading the harness CI result from GitHub

**Context:** Step 3 asks for the latest harness CI `build` result on `main` through `gh run list`. The same brief also forbids every remote call, the GitHub API included, and lets only a push rule override that, so I did not run it. Nothing local records the result: State of play still lists the harness CI `build` on `979e075a`, `9c17df3c` and `2d28656f` to `1b8ab57b` as waiting to be confirmed.

**Query:** Should a later run be allowed one read-only `gh run list` call against the harness?

**Options:**

a) (recommended, confidence high - it reads only and changes nothing) Allow one read-only `gh run list --branch main --workflow build` in the next run's brief, written as an explicit exception to the no-remote rule.

b) Leave it for Kris or the coordinator to check by hand on GitHub.

### 🤖 → 👤 Handoff to supervisor · since 22:06 BST

👤 1 with you

- [with you] CI-CHECK · owner · since 22:06
- [committed] `3d3f4b5d` State of play MOD-LEDGER line, unpushed
- [unpushed] ki-principal `main`
