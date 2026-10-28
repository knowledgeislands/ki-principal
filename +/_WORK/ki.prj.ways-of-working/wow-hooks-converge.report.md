# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-hooks-converge

**🤖 → 👤 Handoff to supervisor · Run report at 23:07 GMT · last mark 01:07 GMT**

---

## Done

HOOK-DRIFT a) first pass. "The five 5g-emerge site apps" read as the five registry-tracked checkouts `5g-emerge-apex`, `-demos`, `-phase2`, `-phase3`, `-testbed`; the five `apps-*.5g-emerge.io` checkouts are unregistered duplicates at the same commits and were left alone. The bounded command was `ki repo conform --repo <path> --skill ki-repo`, dry run first, then applied; hooks staged by explicit path; commit `chore(hooks): converge on the canonical pre-commit hook`; fast-forward push. Every converged hook was re-checked byte-exact against the harness assets at 23:06 GMT (harness checkout at the 23:05 GMT commit), and every target checkout is clean and level. One line per repository:

- er-agentic-harness: converged and pushed, 37cb873, HOOK-4 clean.
- apps-dafacts.org: converged and pushed, 9ebe4a2, HOOK-4 clean.
- er-principal: converged and pushed, 5a1afcc, HOOK-4 clean.
- legal-agentic-harness: converged and pushed, cb3a939, HOOK-4 clean.
- tmx-agentic-harness: converged and pushed, 28b4780, HOOK-4 clean.
- tmx-principal: converged and pushed, d868aff, HOOK-4 clean.
- 5g-emerge-testbed: converged and pushed, db646f9, HOOK-4 clean.
- infoschematics: converged and pushed, eecc689, HOOK-4 clean.
- hnr-agentic-harness: converged and pushed, 7b3dab4, HOOK-4 clean.
- apps-observatory.local: already canonical, nothing to commit; its hook matches the harness asset that landed at 22:51 GMT, and conform wrote no hook.
- ki-techne-harness: already canonical, nothing to commit, same reason.
- ki-design: already canonical, nothing to commit; conform withheld all writes behind GitHub live-state failures (description, merge policy, toggles, topics, Dependabot, secret scanning), but the hook needs no change.
- 5g-emerge-apex: skipped; ki refuses to run because `.ki.toml` still declares the pre-rename repository `apps-5g-emerge.io`, which clashes with the registry key; fixing `.ki.toml` is beyond the hook set.
- 5g-emerge-demos: skipped, same reason (`apps-demo.5g-emerge.io`).
- 5g-emerge-phase2: skipped, same reason (`apps-phase2.5g-emerge.io`).
- 5g-emerge-phase3: skipped, same reason (`apps-phase3.5g-emerge.io`).
- acquire: skipped; conform withheld every write behind GitHub live-state failures (merge policy, Projects toggle, Dependabot), so no hook was written.
- apps-yorkphotosoc.org: skipped; the canonical package hook needs syncpack, biome and rumdl in `node_modules/.bin` and they are not installed; GitHub live-state failures would also withhold the write.
- hnr-principal: skipped; the canonical package hook needs lint-staged, syncpack, biome, rumdl and commitlint in `node_modules/.bin` and none is installed; another session also moved it ten commits during the run.
- legal-principal: skipped; the canonical package hook needs lint-staged, biome and commitlint in `node_modules/.bin` and they are not installed.

Hookless chezmoi, si-agentic-harness and si-principal untouched. Nothing was installed; no `--no-verify`, no force push.

REPORT-LINT-NOW a). The Pillars file is `Pillars/Engineering Practice/Foundations/Principles.md`: its adoption link pointed at the `2026-10-21 14:35 BST` entry of `+/_WORK/ki.ways-of-working/decisions.md`, pruned in 7c5ce0d1. Repointed to the pinned GitHub revision d09a6756 (the last holding the entry) with the same anchor; rumdl clean on the file; committed that path alone as 652606a7 and pushed, after rebasing my one commit over one commit another session had pushed meanwhile. Under rumdl 0.3.0 `rumdl check Pillars` reports nothing, so the file was found by checking every Pillars link into `+/`.

Two departures from the brief's letter, both reversible and raised below: the bounded conform also rewrote `.rumdl.toml` in every repository it converged and ran `rumdl check --fix` over er-principal (two Resources notes changed); I reverted those writes of mine and committed the hooks alone rather than skipping the repositories. Conform's audits read GitHub live state as part of the tool; nothing was written to GitHub.

## In Progress

Nothing. The second convergence waits for the canonical text to ship in a ki release; the harness checkout was still being edited by another session at the end of this run.

## Queries

### EXTRA-WRITES - commit the `.rumdl.toml` refresh the conform proposed?

**Context:** in every converged repository the bounded conform also rewrote `.rumdl.toml` (re-enabling MD005 and MD075 for rumdl 0.3.0) and in er-principal ran `rumdl check --fix`; the brief said to skip a repository that would change files beyond the hook set, which would have skipped nearly all of them, so I committed the hooks alone and reverted my other writes.

**Query:** was committing hooks alone the right call, and should the `.rumdl.toml` refresh be committed by a follow-up run?

**Options:** a) (recommended, confidence high - the hook commits are self-contained and the config refresh is a separate, auditable change) yes, accept the hook commits as made and queue one bounded run to commit the `.rumdl.toml` refresh per repository; b) accept the hook commits and leave `.rumdl.toml` to the second convergence; c) revert the nine hook commits and redo them with `.rumdl.toml` included.

### RENAMED-5G - repoint `.ki.toml` in the four renamed 5g-emerge repositories?

**Context:** apex, demos, phase2 and phase3 still declare their pre-rename `apps-*.5g-emerge.io` repository URL in `.ki.toml`, so ki refuses every operation on them.

**Query:** may a bounded run update the four `.ki.toml` repository fields and then converge their hooks?

**Options:** a) (recommended, confidence high - a one-line fix that unblocks all ki tooling there) yes, one run, four one-line commits plus the hook commits; b) leave until the second convergence.

### MISSING-TOOLS - authorise installs in the three package repositories without hook tools?

**Context:** hnr-principal, legal-principal and apps-yorkphotosoc.org lack some or all of lint-staged, syncpack, biome, rumdl and commitlint in `node_modules/.bin`, so their canonical package hook would refuse every commit; the brief forbade installs.

**Query:** may a follow-up run do `bun install --frozen-lockfile` in those three and then converge their hooks (acquire and apps-yorkphotosoc.org additionally need their GitHub settings conformed before conform will write anything)?

**Options:** a) (recommended, confidence medium - installs are routine but hnr-principal was actively changing under another session) yes, after hnr-principal's active session ends; b) leave until the second convergence.

🧵 Coordination thread · Ways of working (ki.ways-of-working)
