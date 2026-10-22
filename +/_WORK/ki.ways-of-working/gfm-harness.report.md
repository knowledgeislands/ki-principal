# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › gfm-harness

**🤖 → 👤 Handoff to supervisor · Run report at 22:09 BST · last mark 21:25 BST**

---

## Done

- Step 1 — `2d28656f`: GFM preference, supported flavours, standalone whole-file touch paragraph, conversion exceptions, angle-bracket house links and structural `%20` normalisation; removed the KB linking exception and per-note flavour proposal; regenerated the authoring rubric.
- Step 2 — `012090a2`: KB linking policy and LINK-1 now resolve Markdown links, reference definitions, wikilinks and embeds in exact case; fixtures cover spaces, `%20`, table aliases, missing targets, ambiguity, dotfiles and wrong-case extensions. Working-area sources remain excluded; their targets can still make a link elsewhere ambiguous.
- Step 3 — `b5bb1a1e`: Decision Records retain complete angle-bracket and reference-definition destinations; Activities decode `%20` spaces within destinations while preserving other escapes and literal percent signs; regression fixtures pass.
- Step 4 — `624b39f1`: Reworded all three requested eval scenarios; extended the existing inline Markdown-link stripper to reference links and added source-mirror pointer fixtures.
- Step 5 — `af4cb478`: Retained the existing invalid-revision check, rejected non-string method_read values, added numeric and timestamp fixtures, and made the revision requirement explicit in the generated rubric.
- Step 6 — Generated rubric publications: authoring, KB and work-package generation and parity checks passed.
- `bun run test`: 1,292 passed, zero failed, across 170 files; includes the eval registry and new regression fixtures.
- `bunx tsc --noEmit`: passed.
- `ki-skills` audit on the harness: passed.
- `ki-authoring` audit on the harness: passed.
- `ki-decision-records` audit on the harness: passed.
- `ki-work-package` audit on the harness: passed.
- `ki-subagents` audit on the harness: passed.
- `ki-engineering` audit on the harness: passed.
- `ki-repo-kb` audit on a disposable declared KB fixture, including its three dependencies: passed with zero warnings or failures.
- `ki-repo-kb-activities` audit on that fixture: passed. These two skills are not declared by the harness itself, so its checkout is not an applicable audit target.
- All five hook-backed, explicit-path commits passed; actual committed paths were checked after every commit. No unrelated changes or work records were touched, accepted, pruned or deleted.
- Publication: fetched and pulled with rebase; only this run's five commits were stacked. Pushed non-force to `origin/main` at `af4cb478` from `sol.local`; local and remote-tracking tips matched and the checkout was clean when checked. GitHub reported bypass of its PR and required-build rules; no hosting rule was changed.

## In Progress

Nothing running.

Outstanding — no action requested now: the tools-ki converter, client heading-navigation pilot and ki-principal rollout remain receiver-owned work. TOUCH-SCOPE remains with Kris; its proposed whole-file sentence is isolated as requested. LINK-1 verifies file paths, not fragment navigation. The CLI audits do not assess judgment-only criteria, and model-driven eval runs and hosted build results were not checked under this run's remote-call limits. Temporary verification output has been removed; the committed fixtures preserve the executable evidence.

## Queries

### GFM-HOSTING-RULES — reconcile direct-to-main delivery with hosted rules

**Context:** The repository instructions explicitly select direct-to-main delivery without a PR gate. The authorised push succeeded, but GitHub reported that a PR requirement and required `build` status were bypassed. All local gates passed; this run changed no hosting rules and made no GitHub API calls.

**Query:** Should the repository's written delivery policy and hosted rules be reconciled in a separate follow-up?

**Options:**

a) (recommended, confidence high - the written workflow and observed hosting response disagree) Inspect the current hosted rules and reconcile them with the intended delivery policy in separately authorised work.

b) Keep the mismatch documented and defer that review.

### 🤖 → 👤 Handoff to supervisor · since 22:09 BST

👤 1 with you

- [with you] GFM-HOSTING-RULES · supervisor · since 22:09 BST
