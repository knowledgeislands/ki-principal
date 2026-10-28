# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-checks-survey

**🤖 → 👤 Handoff to supervisor · Run report at 22:14 GMT**

---

## Done

Read-only survey of all 51 registry repositories under `/Users/krisbrown/workspaces/`. Nothing was changed, installed, committed or pushed; no `ki repo conform` or `repair` ran. Timings came from throwaway local clones of three repositories.

### Summary in two minutes

Commit time is cheap and CI is where the real check happens. The canonical pre-commit hook costs about one to two seconds on a one-file commit: lint-staged 0.2 to 0.5 s, staged audit 0.2 to 1.4 s. The staged audit has a bad edge, though: on an empty or odd index it costs 12.9 s in personal-principal and 18.5 s in mcp-m365, because `ki repo audit --staged` still evaluates the whole shape skill. A CI-shaped full audit takes 10 to 22 s. All hooks come from one source: the harness assets under `ki-agentic-harness/skills/repo-structure/<shape>/assets/githooks/`, composed by `ki-repo` and written by `ki repo conform` from tools-ki. Chezmoi writes no hooks. 31 repositories carry the current canonical text, 17 carry an older conform-written "legacy gate", and 3 (chezmoi, si-agentic-harness, si-principal) have no hook at all. Every package hook writes files: lint-staged runs `rumdl check --fix` and `biome check --write` on staged files, so a commit may differ from what was staged. CI exists in only 23 repositories and it also writes, running `ki repo repair --repo .` in the checkout before `ki repo audit --repo .`.

Markdown fails rumdl in 6 of 51 repositories, for four reasons. First, in ki-principal, 85 of the 94 failing files are run reports under `+/_WORK/` that background agents wrote and `ki agent` copied in unlinted; 85 were committed wholesale by one local `chore: baseline` commit on 24 October, and the hook let them through because every finding was auto-fixable and the hook only fails when the fix cannot apply, and 8 more are the still-uncommitted reports of this run and its siblings. Second, hnr-principal, legal-principal, er-principal and personal-principal use legacy or no-package hooks with no rumdl at all and have no CI, so hand and coordinator edits went in unchecked. Third, apps-yorkphotosoc.org has no `.rumdl.toml`, a 2023 eslint/prettier hook and no CI, so its 116 failures are historic content against rumdl's defaults. Fourth, one Pillars file in ki-principal breaks only because a pruned `+/_WORK` target no longer exists. The MD013 findings in the run reports are not sloppy writing: they fall on the report form itself, where `**Context:**`, `**Query:**` and `**Options:**` sit on consecutive lines and the lettered options follow with no blank line, and the principal `.rumdl.toml` sets `reflow-mode = "normalize"`, which wants those lines joined into one paragraph. Auto-fixing them would merge the options into one line and destroy the form, so the fix belongs in the form or the rumdl configuration, not in a `--fix` pass. The only check that lints the whole tree is `ki-authoring`'s MD-mech criterion inside the CI full audit, and the hook's `--skill <shape>` audit never selects ki-authoring, so nothing at commit time looks at unstaged or generated Markdown. The baseline-commit tool search in the Claude session logs timed out and found nothing; the Codex logs tie the commits to the `ki.baseline-roll` work on 20 October.

### Part 1 - commit-time checks

Pre-commit hooks bind through `core.hooksPath=.githooks` in every repository that has one. "Canonical" means the committed text matches the harness asset byte for byte, as rule HOOK-4 in [standards-repository.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md) requires; three Project-shape repositories (apps-observatory.local, ki-design, ki-techne-harness) are one asset revision behind, missing the `ki` presence check and the offline `--skill ki-repo` audit. "Legacy gate" is an older conform-written text that predates the asset. The audit column shows the shape skill the hook audits with `ki repo audit --repo "$root" --staged --concise ... --skill <shape>`, which excludes `ki-authoring`.

| Repository | Pre-commit hook | Runs at commit time | Writes staged files | commit-msg | GitHub Actions | Hook origin |
| --- | --- | --- | --- | --- | --- | --- |
| 5g-emerge-apex | legacy gate | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | older conform text (differs from harness asset) |
| 5g-emerge-demos | legacy gate | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | older conform text (differs from harness asset) |
| 5g-emerge-phase2 | legacy gate | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | older conform text (differs from harness asset) |
| 5g-emerge-phase3 | legacy gate | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | older conform text (differs from harness asset) |
| 5g-emerge-testbed | legacy gate | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | older conform text (differs from harness asset) |
| acquire | legacy gate | audit --staged --skill ki-repo | no | none | none | older conform text (differs from harness asset) |
| apps-dafacts.org | legacy gate | audit --staged --skill ki-repo | no | none | none | older conform text (differs from harness asset) |
| apps-knowledgeislands.info | canonical ki-repo-website (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| apps-kris.me.uk | canonical ki-repo-website (package) | lint-staged (rumdl --fix --preflight, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | harness asset via conform |
| apps-markhowarth.com | canonical ki-repo-website (package) | lint-staged (rumdl --fix --preflight, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | harness asset via conform |
| apps-midnight.ninja | canonical ki-repo-website (package) | lint-staged (rumdl --fix --preflight, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | harness asset via conform |
| apps-observatory.local | canonical ki-repo-project (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| apps-rig.midnight.ninja | canonical ki-repo-website (package) | lint-staged (rumdl --fix --preflight, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | harness asset via conform |
| apps-tower.midnight.ninja | canonical ki-repo-website (package) | lint-staged (rumdl --fix --preflight, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | harness asset via conform |
| apps-vallearmonia.com | canonical ki-repo-website (package) | lint-staged (rumdl --fix --preflight, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | none | harness asset via conform |
| apps-yorkphotosoc.org | legacy gate | lint-staged (eslint --fix, prettier --write) · no audit | yes: lint-staged rewrites staged files | none | none | older conform text (differs from harness asset) |
| chezmoi | none | nothing | no | no | none | no `.githooks/` |
| er-agentic-harness | legacy gate | audit --staged --skill ki-repo-harness | no | none | none | older conform text (differs from harness asset) |
| er-principal | legacy gate | audit --staged --skill ki-repo-kb | no | none | none | older conform text (differs from harness asset) |
| hnr-agentic-harness | legacy gate | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | older conform text (differs from harness asset) |
| hnr-principal | legacy gate | audit --staged --skill ki-repo-kb | no | none | none | older conform text (differs from harness asset) |
| homebrew-tap | canonical ki-repo-homebrew-tap (no package) | rumdl check (staged, check-only) · ruby · audit --staged --skill ki-repo-homebrew-tap | no | none | ci.yml: repair, audit, rumdl, tests | harness asset via conform |
| infoschematics | legacy gate | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | older conform text (differs from harness asset) |
| ki-agentic-harness | canonical ki-repo-harness (package) | lint-staged (rumdl --fix --preflight, biome --write) · syncpack --check · audit --staged --skill ki-repo-harness | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| ki-design | canonical ki-repo-project (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| ki-principal | canonical ki-repo-kb (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · audit --staged --skill ki-repo-kb | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| ki-specifications | canonical ki-repo-specifications (no package) | rumdl check (staged, check-only) · audit --staged --skill ki-repo-specifications | no | none | ci.yml: repair, audit, diag, tests | harness asset via conform |
| ki-techne-harness | canonical ki-repo-project (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| legal-agentic-harness | legacy gate | audit --staged --skill ki-repo-harness | no | none | none | older conform text (differs from harness asset) |
| legal-principal | legacy gate | audit --staged --skill ki-repo-kb | no | none | none | older conform text (differs from harness asset) |
| mcp-acquire-whatsapp | canonical ki-repo-mcp (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| mcp-git-audit | canonical ki-repo-mcp (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| mcp-gsuite | canonical ki-repo-mcp (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| mcp-housekeeping-chatgpt | canonical ki-repo-mcp (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| mcp-housekeeping-claude | canonical ki-repo-mcp (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| mcp-ki-kb-fs | canonical ki-repo-mcp (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| mcp-ki-kb-notion-mirror | canonical ki-repo-mcp (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml (no `.ki.toml`): repair, audit, diag, tests | harness asset via conform |
| mcp-m365 | canonical ki-repo-mcp (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · no audit | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| personal-agentic-harness | canonical ki-repo-harness (no package) | rumdl check (staged, check-only) · audit --staged --skill ki-repo-harness | no | none | none | harness asset via conform |
| personal-principal | canonical ki-repo-kb (no package) | rumdl check (staged, check-only) · audit --staged --skill ki-repo-kb | no | none | none | harness asset via conform |
| si-agentic-harness | none | nothing | no | no | none | no `.githooks/` |
| si-principal | none | nothing | no | no | none | no `.githooks/` |
| tmx-agentic-harness | legacy gate | audit --staged --skill ki-repo-harness | no | none | none | older conform text (differs from harness asset) |
| tmx-principal | legacy gate | audit --staged --skill ki-repo-kb | no | none | none | older conform text (differs from harness asset) |
| tools-git-almanac | canonical ki-repo-tools (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · shellcheck, bash -n, mandoc · audit --staged --skill ki-repo-tools | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| tools-ki | canonical ki-repo-tools (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · shellcheck, bash -n, mandoc · audit --staged --skill ki-repo-tools | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| tools-mgit | canonical ki-repo-tools (no package) | rumdl check (staged, check-only) · shellcheck, bash -n, mandoc · audit --staged --skill ki-repo-tools | no | none | ci.yml: repair, audit, rumdl, tests | harness asset via conform |
| tools-rig | canonical ki-repo-tools (no package) | rumdl check (staged, check-only) · shellcheck, bash -n, mandoc · audit --staged --skill ki-repo-tools | no | none | ci.yml: repair, audit, rumdl, tests | harness asset via conform |
| tools-techne | canonical ki-repo-tools (package) | lint-staged (rumdl --fix, biome --write) · syncpack --check · shellcheck, bash -n, mandoc · audit --staged --skill ki-repo-tools | yes: lint-staged rewrites staged files | commitlint | ci.yml: repair, audit, diag, tests | harness asset via conform |
| va-agentic-harness | canonical ki-repo-harness (no package) | rumdl check (staged, check-only) · audit --staged --skill ki-repo-harness | no | none | none | harness asset via conform |
| va-principal | canonical ki-repo-kb (no package) | rumdl check (staged, check-only) · audit --staged --skill ki-repo-kb | no | none | none | harness asset via conform |

Timings, one-file commit in a local clone, warm cache:

| Repository | Whole pre-commit hook | Staged audit alone | lint-staged alone | CI-shaped full audit | Staged audit, empty index |
| --- | --- | --- | --- | --- | --- |
| ki-principal | 1.0 s | 0.3 s | 0.2 s | not timed (fails: 3 skills) | 0.4 s |
| tools-ki | 0.7 s | 0.2 s | 0.3 s | 11.9 s | 0.2 s |
| ki-agentic-harness | 2.2 s | 1.4 s | 0.5 s | 10.6 s | 1.4 s |
| mcp-m365 | not timed | not timed | not timed | 21.9 s | 18.5 s |
| personal-principal | not timed | not timed | not timed | not timed | 12.9 s |
| er-principal | not timed | not timed | not timed | not timed | 0.5 s |

Whole-tree `rumdl check .` in ki-principal takes 0.2 s and `syncpack format --check` is instant, so neither is a cost reason for keeping rumdl out of the hook.

Where each check comes from: hook text is composed by `ki-repo` from the harness assets and written by `ki repo conform` ([hooks.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/repository/hooks.ts), [conform.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/repository/operations/conform.ts)); lint-staged configuration lives in each `package.json` under `ki-engineering` SCR-11; the staged check-only rumdl line in package-less hooks is `ki-authoring` MD-hook; CI workflows are the `ki-repo` owned `.github/workflows/ci.yml`, which installs the pinned `ki`, runs `ki bootstrap`, `ki registry add`, `ki repo repair --repo .`, `ki repo audit --repo .` over every declared skill, `ki diag` and the repository's tests. No husky, lefthook or `.git/hooks/` hook is in use anywhere; chezmoi manages no hooks.

### Part 2 - Markdown failing rumdl

Each repository was checked with its own `.rumdl.toml` and rumdl 0.3.0. 45 repositories pass. In the principal configuration MD013 is `line-length = 100000` with `reflow = true`, so an MD013 finding means hard-wrapped prose that rumdl would rejoin, not an over-long line; it is auto-fixable, which is why lint-staged's `--fix` silently accepts the same text that a check-only run rejects.

| Repository | Failing files (issues) | Rules | Writer, from git log | Why no check caught it |
| --- | --- | --- | --- | --- |
| ki-principal | 94 (265) | MD013 in 79 files; MD032, MD034, MD012, MD022, MD051, MD064 in the rest | 85 files are `+/_WORK/*/*.report.md` written by background agents and copied in by `ki agent` ([runs.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts)); 81 committed by the local `chore: baseline` commit of 2026-10-24 (author Kris Brown, no body, part of the `ki.baseline-roll` work), 4 of those since modified, 8 uncommitted reports of the current runs; 1 Pillars file (MD051) committed 2026-10-21 by `docs(pillars): adopt candidate principles` | The hook's lint-staged ran `rumdl check --fix` on the staged reports and rewrote them, but the baseline commit staged files in one sweep whose fixes applied cleanly, so it passed; the hook audit is `--skill ki-repo-kb` and never runs ki-authoring; CI's ki-authoring MD-mech does fail today (confirmed: `ki repo audit --skill ki-authoring` FAIL on these files) but CI only runs on push and the commits are local. The MD013 hits are on the `**Options:**` and `**Context:**` lines of the query form, which `reflow-mode = "normalize"` wants merged. The MD051 file points at a `+/_WORK` fragment that pruning removed, so the file was valid when committed. |
| hnr-principal | 11 (23) | MD034, MD032, MD012, MD025, MD013 | `+/_WORK/hnr.sop.sites/briefs/*.md`, `queries.md`, `decisions.md`: coordinator `docs(work)` commits 2026-10-25 and 2026-10-26 (author kris) | Legacy gate with audit `--skill ki-repo-kb` only, no lint-staged and no rumdl line; no CI workflow. |
| legal-principal | 46 (63) | MD013 in 38 files; MD034, MD032, MD012, MD049, MD056, MD057, MD064 | 24 Pillars/Evidence files from `chore(metadata): migrate legal note types` (2026-08-16) and `chore(kb): migrate legacy note metadata` (2026-08-18); 9 Command Centre and Calendar files from hand and agent `docs(command-centre)` commits 2026-10-12 to 2026-10-25; 4 `+/_WORK/lgl` files from coordinator `docs(work)` commits 2026-10-19 to 2026-10-25 | Legacy gate with audit `--skill ki-repo-kb` only, no rumdl; no CI workflow; the August migration predates the repository's rumdl configuration. |
| er-principal | 2 (3) | MD013 | Two Resources files from `feat(research)` commits of 2026-08-22 and 2026-09-02 (Kris Brown) | Legacy gate with audit only, no rumdl; no CI workflow. |
| personal-principal | 1 (1) | MD075 | One Pillars file from `chore(kb): classify note types` 2026-08-18 (author Kit) | At that date the hook was the legacy gate; the current no-package canonical hook has staged check-only rumdl, but the file has not been touched since; no CI workflow. |
| apps-yorkphotosoc.org | 116 (551) | MD013 in 99 files; MD071, MD047, MD064, MD041, MD001, MD012, MD033 | Site content and MDX under `apps/yps-website/src/content/` from 2023-05 to 2024-09 | No `.rumdl.toml`, so rumdl's 80-column default applies; the hook is a 2023 eslint/prettier lint-staged gate with no Markdown rule; no CI workflow; the repository declares ki-authoring in `.ki.toml` but has never been conformed. |

Classes of writer and the gap for each:

| Writer class | Files | Gap |
| --- | --- | --- |
| Background run reports, copied by `ki agent` into `+/_WORK` | 85 in ki-principal, 4 in legal-principal | No lint in the agent, the launcher copy or the coordinator's receive; the commit hook fixes only what is staged and only when the fix applies |
| Coordinator package writes (briefs, queries, decisions) | 11 in hnr-principal, 4 in legal-principal | Legacy gates have no rumdl at all and these repositories have no CI |
| Metadata migrations and hand edits, August to October | 25 legal, 2 er, 1 personal, 9 legal Command Centre | Same legacy gates, no CI; some predate the repository's rumdl config |
| Website generator or sync | none found | No website sync wrote any failing file; the ki website repositories all pass |
| Environment drift | 1 Pillars file in ki-principal | A cross-file fragment target was pruned after the commit |

Scratch material, kept for inspection under `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/ways-of-working/wow-checks-survey/`: `hooks.tsv`, `ci.txt`, `timing.txt`, `timing-staged.txt`, `rumdl/<repo>.txt`, `failing-files.tsv`, `baseline-fail.txt`, `legal-summary.txt`, and three local clones under `clones/` used for timing. The brief forbids removing the directory with `rm`; it is left in place.

## In Progress

Nothing is running. One search was stopped: the grep of Claude session logs for the command behind the `chore: baseline` commits hit its time limit twice and returned nothing, so the originating tool for those 15 ki-principal commits is attributed from the Codex logs to the `ki.baseline-roll` work rather than to a named command.

## Queries

### COMMIT-VS-CI - what should run at commit time and what in CI

**Context:** The canonical pre-commit hook runs lint-staged (which rewrites staged files), syncpack, shape-specific lints and one `ki repo audit --staged --skill <shape>`. It costs one to two seconds on an ordinary commit but 13 to 19 s on an empty-index path in two repositories, and its audit never includes ki-authoring, so Markdown outside the staged set is never checked locally. CI runs the full audit over every declared skill, but only 23 of 51 repositories have the workflow, and CI also runs `ki repo repair` in its checkout, so a CI pass does not prove the committed tree conforms. The owner of the hook composition and HOOK-1 to HOOK-5 is `ki-repo` in ki-agentic-harness ([standards-repository.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md)); the hook writer is `ki repo conform` in tools-ki; the CI workflow is also `ki-repo`'s.

**Query:** Should commit time keep only fast, check-only, staged lints and leave every audit to CI, or keep the staged audit in the hook?

**Options:**

a) (recommended, confidence medium - the measured cost is low on the normal path but the empty-index outliers and the write-in-hook behaviour both break the "commit what I staged" expectation, and CI already runs the full audit) Commit time runs check-only staged lints only: `rumdl check` (no `--fix`), `biome check` (no `--write`), syncpack check, shellcheck and mandoc where relevant, and commitlint; the staged `ki repo audit` moves to CI, which drops `ki repo repair` and runs `ki repo audit --repo .` on the tree as committed. Change: `ki-repo` standards-repository.md hook composition and HOOK-4 assets, `ki-engineering` SCR-11 lint-staged commands, `ki-authoring` MD-hook, and the `ci.yml` asset, all in ki-agentic-harness, with the writer in tools-ki `conform` following.

b) Keep the current hook, but make lint-staged check-only and keep the staged audit, accepting the audit outliers; CI unchanged.

c) Keep everything as it is and fix only the CI gap by adding `ci.yml` to the 28 repositories without it.

### LINT-WHERE - where generated Markdown gets linted

**Context:** 85 of the 94 failing files in ki-principal and 15 of the 57 in hnr-principal and legal-principal are run reports and package files written by background agents and the coordinator, not by hand. Nothing in that path lints: the agent writes the report to the state folder, `ki agent` copies it into `+/_WORK` ([runs.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/runs.ts)), and the coordinator commits it. The commit hook fixes staged Markdown silently where it can, and the whole-tree check lives only in `ki-authoring`'s MD-mech criterion, which runs only in CI's full audit. Owners: `ki-delegation` (report rule and run packet) and `ki agent` in tools-ki for the generator path; `ki-authoring` for MD-hook and MD-mech; `ki-coordination` and `ki-work-package` for what the coordinator may write into the work folder.

**Query:** Where should generated Markdown be linted: in the generator, in the hook, or in CI?

**Options:**

a) (recommended, confidence medium - the generator is the only place that sees every report, including ones never committed, and a check there is cheap at 0.2 s; the hook and CI stay as the backstop) In the generator, check-only: `ki agent` runs `rumdl check` with the receiving repository's `.rumdl.toml` on the report before copying it into `+/_WORK` and marks the run's status line with the failure, never `--fix`, because a fix pass would merge the lettered options of the query form into one line; the `ki-delegation` report rule tells the agent to write lint-clean Markdown; the hook keeps a check-only staged rumdl so a bad report cannot be committed; CI's MD-mech stays the whole-tree backstop. This depends on FORM-VS-RUMDL, since today every well-formed report fails. Change: tools-ki `ki agent` (runs.ts copy step) and the `ki-delegation` brief and report rules in ki-agentic-harness.

b) In the hook only: make every hook, legacy and canonical, run check-only staged rumdl, so the coordinator sees the failure at commit and sends it back to the run; no change to the generator.

c) In CI only: add `ci.yml` to every repository and accept that reports fail later and are fixed by a follow-up run.

### HOOK-DRIFT - converging the 17 legacy gates and the 3 stale Project hooks

**Context:** 17 repositories (the five 5g-emerge sites, acquire, apps-dafacts.org, apps-yorkphotosoc.org, er-agentic-harness, er-principal, hnr-agentic-harness, hnr-principal, infoschematics, legal-agentic-harness, legal-principal, tmx-agentic-harness, tmx-principal) carry an older conform-written hook; the knowledge-base ones among them run an audit with no rumdl, and the website ones run lint-staged with no audit. apps-observatory.local, ki-design and ki-techne-harness carry the Project hook one asset revision behind HOOK-4. Three repositories have no hook. HOOK-4 is WARN until the last wave, so audits do not fail on this. The owner is `ki-repo` in ki-agentic-harness; the mechanism is `ki repo conform` in tools-ki, run per repository.

**Query:** Should the legacy gates be converged to the canonical hooks now by a conform run per repository, before or after COMMIT-VS-CI changes the canonical text?

**Options:**

a) (recommended, confidence high - conforming twice is cheap and the legacy knowledge-base gates are the ones letting Markdown through today) Converge now with one bounded `ki repo conform` run per repository, staged by explicit path to `.githooks/` and `package.json` only, then converge again when COMMIT-VS-CI lands; the three hookless repositories are left to their owners.

b) Wait for COMMIT-VS-CI to settle the canonical text, then converge once.

### BASELINE-COMMITS - what a baseline commit may sweep in

**Context:** 15 local `chore: baseline` commits in ki-principal, and one or more in 39 other repositories, were made during the `ki.baseline-roll` work from 2026-09-26 to 2026-10-25. The ki-principal one of 24 October added 81 run reports that fail rumdl; the hook's lint-staged `--fix` accepted them. The Claude session logs do not record the command, so whether this is `ki-implement`'s immutable-baseline step, `ki-batch` or a hand `git add -A` is not established. Owners: `ki-git` for commit shape and explicit staging, `ki-implement` for the baseline step, both in ki-agentic-harness.

**Query:** Should a baseline commit be allowed to sweep in uncommitted work-folder reports, or should it stage by explicit path like every other commit under `ki-git`?

**Options:**

a) (recommended, confidence medium - the commits are local and provably swept the work folder in, but the tool behind them was not identified) Require explicit-path staging for baseline commits too and have the `ki-implement` baseline step list its paths; a separate run identifies which tool produced the commits before the rule is written.

b) Allow the sweep but run check-only rumdl over the whole tree before the baseline commit so it cannot carry failing Markdown.

### FORM-VS-RUMDL - the query form and the rumdl reflow setting disagree

**Context:** Every run report and coordinator query written to the required form fails MD013 in a principal repository, because `**Context:**`, `**Query:**` and `**Options:**` sit on consecutive lines and `a)`, `b)`, `c)` follow with no blank line, while the principal `.rumdl.toml` (written from `RUMDL_DEFAULT` in `ki-authoring`, [authoring.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-authoring/scripts/rubric/contexts/authoring.ts)) sets `[MD013] line-length = 100000`, `reflow = true`, `reflow-mode = "normalize"`, which asks for each paragraph to be one line. lint-staged's `rumdl check --fix` therefore rewrites a staged report by joining the options into one line, and a check-only run rejects it. This report had to add blank lines after `**Options:**` to pass. Owners: `ki-coordination` and `ki-delegation` in ki-agentic-harness for the form; `ki-authoring` for `RUMDL_DEFAULT`.

**Query:** Should the form change to put a blank line between the Context, Query and Options paragraphs and between the lettered options, or should the rumdl default stop normalising paragraphs?

**Options:**

a) (recommended, confidence high - a blank line between the lettered options keeps "no bullets" and is already what this report does; it leaves the rumdl default, which protects every other document, untouched) Change the form in `ki-coordination` and `ki-delegation`: a blank line after each of `**Context:**`, `**Query:**` and `**Options:**` paragraphs and between lettered options; update the harness output style and the brief template to match.

b) Set `reflow = false` or `reflow-mode = "sequential"` in `RUMDL_DEFAULT` in `ki-authoring` and reconform every repository's `.rumdl.toml`, accepting that hard-wrapped prose elsewhere is no longer flagged.

c) Disable MD013 for `+/_WORK/**` through a rumdl per-path override, leaving the form and the default as they are.

### REPORT-LINT-NOW - clearing the 94 failing ki-principal files

**Context:** 81 committed and 8 uncommitted run reports in `+/_WORK` fail MD013 and a few other auto-fixable rules; one Pillars file fails MD051 on a pruned target. `ki repo conform --skill ki-authoring` would fix all but the MD051 file in one pass, but it rewrites files, and 8 of them belong to runs still being received. Owner: ki-principal through its `ki.ways-of-working` package.

**Query:** Should the committed reports be fixed in one conform run now, or left until LINT-WHERE lands and they are pruned at the next mark?

**Options:**

a) (recommended, confidence high - most of these reports will be pruned at the next mark once their queries are copied, so fixing them is wasted work; the Pillars link is a one-line fix) Leave the committed reports to pruning, fix the one Pillars MD051 link by hand, and let LINT-WHERE stop new ones.

b) Run `ki repo conform --skill ki-authoring` once in ki-principal, staged by explicit path, and commit the fixes.
