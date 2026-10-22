# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › ci-green

**🤖 → 👤 Handoff to supervisor · Run report at 02:48 BST · last mark 02:01 BST**

---

## Done

- Diagnosis of the 9 FAILs: they are 8 RUNTIMES-2 and 1 REPO-REG-1 findings. Both appear only when the audit runs against a worktree that has not been registered or had its skill links set up. The primary checkout showed neither, and CI's own `ki registry add` and `ki repo repair` steps prevent both. No source fix was needed. The fix for the class is an audit recipe: point `KI_DATA_HOME` and `KI_STATE_HOME` at an isolated temp home, then run `ki repo repair --repo .` before `ki repo audit --repo .`. The only real FAILs left were 7 ITEM-3 findings, one for each unplanned draft, and they are cleared below.
- Limitation: I did not read CI's own log, because the brief allows no GitHub API call. The claim that CI was red for these reasons alone is inferred. CI also pins `ki` v0.11.3, and I verified against local 0.12.0.
- `165deda0` docs(roadmap): planned seven records. Each has Current state, Steps, Files touched, Verify, Dependencies / blocks and Documentation impact, and all are still draft:
  - [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md)
  - [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md)
  - [KI-HARNESS-GOV-214](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md)
  - [KI-HARNESS-GOV-215](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-215-pmo-12-to-fail.md)
  - [KI-HARNESS-GOV-220](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-220-coord-1-undeclared-warn-level.md)
  - [KI-HARNESS-GOV-221](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-221-ki-diagrams-mermaid-fence-warning.md)
  - [KI-HARNESS-GOV-223](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-223-island-maturity-declaration.md)
- `b852835a` fix(hooks): `.githooks/pre-commit` now refuses the commit when `bun` is not on PATH, before any content check, as the refuse-before-content rule requires for [KI-HARNESS-GOV-224](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-224-diagram-viewer-receipts.md)'s receipt step. A new test in `hooks/git-hook-stub.test.ts` fails without the fix and passes with it.
- `ki repo audit --repo .` (isolated `KI_DATA_HOME` pointing at the worktree): 0 FAIL, 83 WARN findings, exit 0.
- `bun run test`: passes with 1,326 tests and 0 failures.
- `bunx tsc --noEmit`: passes.
- The pre-commit hook passed on both commits.
- Pushed fast-forward to `origin/main` at `b852835a`, with only my two commits stacked. The primary checkout is fast-forwarded to `b852835a` and its tree is clean.
- Material: when I pushed, GitHub reported that it bypassed two `main` rules: "Changes must be made through a pull request" and the required status check "build". The account has bypass rights, so the push went through. This repository's `AGENTS.md` describes a direct-to-`main` workflow with no PR gate, so the remote ruleset and the local policy disagree.
- Clean-up: I removed the worktree, deleted the `ci-green` branch and emptied the temp directory.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Each planned record has decisions to settle under Dependencies / blocks before it can go Ready. The PLANNED-READY query below covers these.
- [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) still links [KI-TOOL-KI-CLI-150 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/4f8d97d2/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) by a local path that no longer exists. I left it alone; it should be fixed when that record is next edited.
- [KI-HARNESS-GOV-220](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-220-coord-1-undeclared-warn-level.md) is latent: no Capital still holds `+/_CHECKPOINTS/_state-of-play.md`, so no live audit aborts today.
- The `main` rule bypass and the CI `ki` version pin (v0.11.3 against local 0.12.0) are for the next CI-health pass.

## Queries

### WORKTREE-AUDIT - Write down the worktree audit recipe

**Context:** All nine "pre-existing" CI FAILs came from running `ki repo audit --repo .` in a worktree that was neither registered nor set up with skill links. Any run working in a fresh worktree will hit the same false RUNTIMES-2 and REPO-REG-1 FAILs. The recipe that avoids this, without touching the real registry, is: an isolated `KI_DATA_HOME` and `KI_STATE_HOME`, then `ki repo repair --repo .`, then the audit. Right now only this report records it.

**Query:** Should the recipe be written into this repository's `AGENTS.md` Verification line and the `ki-delegation` worktree guidance?

**Options:**

a) (recommended, confidence medium - one run proved the recipe and CI follows the same order, but I have not checked it under `ki` v0.11.3) Capture a harness record that adds the recipe to `AGENTS.md` Verification and to `ki-delegation`'s worktree guidance.

b) Have `ki repo audit` itself report an unregistered or unlinked worktree as one setup finding instead of separate FAILs, through a tools-ki handoff.

c) Leave it unwritten.

### HOOK-4-CLASS - Check every tool a hook calls

**Context:** HOOK-4 in `ki-repo` checks only that some tool test followed by `exit 1` comes before the hook's content. That is why the pre-commit hook passed while calling `bun` without testing for it. I fixed this one hook, but the class is still open. CAPTURE-GATE stopped me from capturing a record.

**Query:** Should HOOK-4 require every external tool a hook calls to be tested in its refusal frame?

**Options:**

a) (recommended, confidence medium - the gap is proven here, but how many hooks across the fleet would newly fail is unmeasured) Capture a harness record to tighten HOOK-4. It would start at WARN, after a fleet census.

b) Keep HOOK-4 as it is and rely on review.

### PLANNED-READY - Settle the planned records' decisions

**Context:** The seven planned records each list their open decisions under Dependencies / blocks, with a recommendation for each:

- [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md): which temp home stands, and whether to FAIL now or WARN until the census is clean.
- [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md):
  - token source (vendored copy with a drift test)
  - default form (`dual` stays)
  - an optional `svg_form` manifest field
- [KI-HARNESS-GOV-214](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md): the time field (`written_at`), and dropping `rebuilt_from`.
- [KI-HARNESS-GOV-221](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-221-ki-diagrams-mermaid-fence-warning.md):
  - reach (declared repositories only)
  - tracked Markdown only
  - a keep-marker comment
- [KI-HARNESS-GOV-223](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-223-island-maturity-declaration.md):
  - the key in `[skills.ki-repo]`
  - no level for retired islands
  - the decline and ruin mapping

[KI-HARNESS-GOV-215](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-215-pmo-12-to-fail.md) and [KI-HARNESS-GOV-220](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-220-coord-1-undeclared-warn-level.md) have no open decision.

**Query:** Should the recommended answers be taken and the seven records approved to Ready?

**Options:**

a) (recommended, confidence medium - each recommendation rests on the checked current state, but the GOV-200 temp home and the GOV-205 token source affect other repositories) Take every recommendation and mark all seven Ready in one planning commit. Split GOV-205's KI-theme form out at Ready if its `l` size warrants it.

b) Mark only GOV-215 and GOV-220 Ready now, since they have no open decisions, and take the others record by record.

### 🤖 → 👤 Handoff to supervisor · since 02:48 BST

👤 3 with you

- [with you] WORKTREE-AUDIT · owner · since 02:48
- [with you] HOOK-4-CLASS · owner · since 02:48
- [with you] PLANNED-READY · owner · since 02:48
- [committed] ki-agentic-harness `main` at `b852835a`, pushed
