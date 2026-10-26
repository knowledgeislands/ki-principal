# wow-review-checks-q - blind review of three queries on commit hooks, CI and Markdown linting

You are an independent reviewer. For each query, verify the Context's claims directly where you can: hook assets under /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/*/assets/githooks/, installed `.githooks`/`.husky`/lint-staged config and `.github/workflows` in repositories under /Users/krisbrown/workspaces, `.rumdl.toml` files, and tools-ki's `ki repo` source at /Users/krisbrown/workspaces/knowledge-islands/tools-ki. Kris's own view, on 26 October 2026: "some of them are running things like repo audit and conforms as part of a pre-commit. And I don't see why we'd ever want to be doing that". Pick the option you would recommend, confidence high, medium or low, one-line reason, and note any claim you found false. Do not read any queries.md, decisions.md or *.report.md file. Read-only: change nothing, commit nothing, run no conform, repair or fix, call no GitHub API.

Report under ## Done one ### section per tag: pick, confidence, reason, verified or refuted claims. Then ## In Progress (Nothing) and ## Queries (None).

## COMMIT-VS-CI - what should run at commit time and what in CI

**Context:** The canonical pre-commit hook runs lint-staged (which rewrites staged files), syncpack, shape-specific lints and one `ki repo audit --staged --skill <shape>`. It costs one to two seconds on an ordinary commit but 13 to 19 s on an empty-index path in two repositories, and its audit never includes ki-authoring, so Markdown outside the staged set is never checked locally. CI runs the full audit over every declared skill, but only 23 of 51 repositories have the workflow, and CI also runs `ki repo repair` in its checkout, so a CI pass does not prove the committed tree conforms. The owner of the hook composition and HOOK-1 to HOOK-5 is `ki-repo` in ki-agentic-harness ([standards-repository.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md)); the hook writer is `ki repo conform` in tools-ki; the CI workflow is also `ki-repo`'s.

**Query:** Should commit time keep only fast, check-only, staged lints and leave every audit to CI, or keep the staged audit in the hook?

**Options (unranked):**

- Keep everything as it is and fix only the CI gap by adding `ci.yml` to the 28 repositories without it.
- Keep the current hook, but make lint-staged check-only and keep the staged audit, accepting the audit outliers; CI unchanged.
- Commit time runs check-only staged lints only: `rumdl check` (no `--fix`), `biome check` (no `--write`), syncpack check, shellcheck and mandoc where relevant, and commitlint; the staged `ki repo audit` moves to CI, which drops `ki repo repair` and runs `ki repo audit --repo .` on the tree as committed. Change: `ki-repo` standards-repository.md hook composition and HOOK-4 assets, `ki-engineering` SCR-11 lint-staged commands, `ki-authoring` MD-hook, and the `ci.yml` asset, all in ki-agentic-harness, with the writer in tools-ki `conform` following.

### LINT-WHERE - where generated Markdown gets linted

**Context:** 85 of the 94 failing files in ki-principal and 15 of the 57 in hnr-principal and legal-principal are run reports and package files written by background agents and the coordinator, not by hand. Nothing in that path lints: the agent writes the report to the state folder, `ki agent` copies it into `+/_WORK` ([runs.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts)), and the coordinator commits it. The commit hook fixes staged Markdown silently where it can, and the whole-tree check lives only in `ki-authoring`'s MD-mech criterion, which runs only in CI's full audit. Owners: `ki-delegation` (report rule and run packet) and `ki agent` in tools-ki for the generator path; `ki-authoring` for MD-hook and MD-mech; `ki-coordination` and `ki-work-package` for what the coordinator may write into the work folder.

**Query:** Where should generated Markdown be linted: in the generator, in the hook, or in CI?

**Options (unranked):**

- In CI only: add `ci.yml` to every repository and accept that reports fail later and are fixed by a follow-up run.
- In the hook only: make every hook, legacy and canonical, run check-only staged rumdl, so the coordinator sees the failure at commit and sends it back to the run; no change to the generator.
- In the generator, check-only: `ki agent` runs `rumdl check` with the receiving repository's `.rumdl.toml` on the report before copying it into `+/_WORK` and marks the run's status line with the failure, never `--fix`, because a fix pass would merge the lettered options of the query form into one line; the `ki-delegation` report rule tells the agent to write lint-clean Markdown; the hook keeps a check-only staged rumdl so a bad report cannot be committed; CI's MD-mech stays the whole-tree backstop. This depends on FORM-VS-RUMDL, since today every well-formed report fails. Change: tools-ki `ki agent` (runs.ts copy step) and the `ki-delegation` brief and report rules in ki-agentic-harness.

### BASELINE-COMMITS - what a baseline commit may sweep in

**Context:** 15 local `chore: baseline` commits in ki-principal, and one or more in 39 other repositories, were made during the `ki.baseline-roll` work from 2026-09-26 to 2026-10-25. The ki-principal one of 24 October added 81 run reports that fail rumdl; the hook's lint-staged `--fix` accepted them. The Claude session logs do not record the command, so whether this is `ki-implement`'s immutable-baseline step, `ki-batch` or a hand `git add -A` is not established. Owners: `ki-git` for commit shape and explicit staging, `ki-implement` for the baseline step, both in ki-agentic-harness.

**Query:** Should a baseline commit be allowed to sweep in uncommitted work-folder reports, or should it stage by explicit path like every other commit under `ki-git`?

**Options (unranked):**

- Allow the sweep but run check-only rumdl over the whole tree before the baseline commit so it cannot carry failing Markdown.
- Require explicit-path staging for baseline commits too and have the `ki-implement` baseline step list its paths; a separate run identifies which tool produced the commits before the rule is written.
