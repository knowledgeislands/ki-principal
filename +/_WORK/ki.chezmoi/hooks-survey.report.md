# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › hooks-survey

**🤖 → 👤 Handoff to supervisor · Run report at 02:55 BST**

---

## Done

I surveyed the Git hooks in all 24 repositories without changing anything: no commits, no writes to Git config, no installs and no network calls. Spot-checking four repositories showed their working trees unchanged afterwards, and no `.git/*.lock` files were left anywhere. No commits were made.

Twenty-one repositories bind `core.hooksPath .githooks`. ki-design binds `.husky/_`. kw-website, paperclip and chezmoi set no `core.hooksPath` and have no hooks at all, not even in `.git/hooks`. No global or system `core.hooksPath` is set. Every committed `.githooks/*` file is tracked with mode `100755` and follows the `ki-repo` frame (`#!/bin/sh`, then refuse if a tool is missing).

| Repository | Mechanism | Hooks | What pre-commit runs | Rough cost |
| --- | --- | --- | --- | --- |
| apps-knowledgeislands.info | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| apps-observatory.local | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| ki-techne-harness | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| mcp-acquire-whatsapp | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| mcp-git-audit | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| mcp-gsuite | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| mcp-housekeeping-chatgpt | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| mcp-housekeeping-claude | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| mcp-ki-kb-fs | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| mcp-ki-kb-notion-mirror | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| mcp-m365 | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| tools-git-almanac | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| tools-ki | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ (Syncpack 0.1 s) |
| tools-techne | `.githooks` + lint-staged | pre-commit, commit-msg | common package gate † | ~1–3 s ‡ |
| ki-principal | `.githooks` + lint-staged | pre-commit, commit-msg | `lint-staged --quiet`, Syncpack, `ki repo audit --skill ki-repo-kb --staged`; also refuses without `ki` | ~3–5 s (audit 1.6 s) |
| ki-agentic-harness | `.githooks` + lint-staged | pre-commit, commit-msg | `lint-staged --quiet` and Syncpack; whole-project `tsc --noEmit` if any `.ts` is staged; a `ki-skills` audit over a full staged snapshot if skills are staged; a `bun` diagram-receipt check if diagrams are staged; also refuses without `ki` and `bun` | seconds, rising to tens of seconds when `.ts` or skills are staged (not timed: `tsc` can write build info) |
| ki-specifications | `.githooks`, no package | pre-commit | `ki repo audit --skill ki-repo-specifications --staged` | 0.2 s |
| homebrew-tap | `.githooks`, no package | pre-commit | two Ruby test files, then `ki repo audit --skill ki-repo-homebrew-tap --staged` | a few seconds (tests not run) |
| tools-mgit | `.githooks`, no package | pre-commit | shellcheck, `bash -n`, `mandoc -T lint`, **the whole bats suite (141 tests in 3 files)**, `ki repo audit --skill ki-repo-tools --staged` | shellcheck 3.5 s, mandoc 0.0 s, audit 0.2 s, plus the suite (not run; likely tens of seconds or more) |
| tools-rig | `.githooks`, no package | pre-commit | shellcheck over 6 paths plus `src/rig/*.bash`, `bash -n` on each, `assemble-rig --check`, mandoc, **the whole bats suite (602 tests in 37 files)**, the `ki-repo-tools` staged audit | the heaviest in the estate: likely minutes (not run) |
| ki-design | **Husky**: `core.hooksPath .husky/_`; `prepare: husky` | pre-commit, commit-msg (Husky) plus unbound `.githooks` stubs | `bunx lint-staged`, `bunx syncpack format --check`, with no refusal frame § | ~1–3 s |
| kw-website | none (no `.ki.toml`) | none | nothing | 0 |
| paperclip | none (no `.ki.toml`; a fork using pnpm) | none | nothing | 0 |
| chezmoi | none | none | nothing; AGENTS.md lists a manual gate (`ki repo audit`, `node --test`, `rumdl check .`) | 0 |

† The common package gate refuses unless `node_modules/.bin` holds `lint-staged` and `syncpack`, then runs `lint-staged`, which applies `bunx @biomejs/biome check --write` to staged code and `bunx rumdl check --fix` to staged Markdown, then `syncpack format --check`. All 14 copies are byte-identical, and so are their `commit-msg` hooks (Commitlint behind the same refusal frame). Every package-backed repository has its tools installed. ‡ Estimated; it scales with the staged files and is close to nothing when nothing is staged. § The `.githooks/pre-commit` and `.githooks/commit-msg` stubs refuse correctly but are not bound, and they `exec` the `.husky/` scripts.

**Governance:** the `ki-repo` "Commit gate" section, under HOOK-1 to HOOK-5 and ADR-KI-HARNESS-SKILLS-017, decides whether a hook exists, how it is bound and its frame. Repositories without `.ki.toml` are out of scope. What a hook runs belongs to each repository's shape skill: `ki-engineering` SCR-11 for package-backed repositories, `ki-repo-kb` GATE-1, `ki-repo-harness` GATE-1, `ki-repo-tools` SHELL-HOOK and `ki-repo-dotfiles-chezmoi` GIT-2. All hook criteria are WARN for now.

**Drift from that governance:**

- **ki-design** fails HOOK-2 and HOOK-5. It binds `.husky/_`, declares `husky`, uses `prepare: husky`, tracks `.husky/`, and its stubs delegate to `.husky/`. In a linked worktree, the untracked `.husky/_` means commits go through unchecked.
- **ki-agentic-harness** has `primary_shape = ki-repo-harness`, but its hook lacks the GATE-1 line `ki repo audit --skill ki-repo-harness --staged`.
- **homebrew-tap and ki-specifications** run shape audits, but their shape skills declare no hook content criterion, which `ki-repo` says every shape skill should. The gap is in the standard, not the repositories.
- **tools-mgit and tools-rig** are not drifting: SHELL-HOOK requires `bats` in the hook and does not limit its scope, so the standard itself requires the whole-suite cost.
- **The 14 common hooks** use plain `lint-staged` rather than the accepted `--quiet` form; both are allowed. Their lint-staged configs call `bunx` even though the standard says hooks call tools without `bunx`.

**Comparison:**

- **Groups:**
  - The common package gate: 14 repositories.
  - Package gate plus repository audit: ki-principal and ki-agentic-harness.
  - Package-less audit-only: ki-specifications.
  - Package-less with tests plus audit: homebrew-tap, tools-mgit, tools-rig.
  - Husky: ki-design.
  - No hook: chezmoi, kw-website, paperclip.
- **Whole test suites on every commit:**
  - tools-mgit runs 141 bats tests and tools-rig runs 602.
  - homebrew-tap runs its two Ruby test files, which is cheap.
  - No other repository runs `bun test`, `vitest` or `turbo test` in a hook.
- **Repositories with no hook:**
  - chezmoi is in scope, with WARN on HOOK-1. The `KI-HARNESS-GOV-117` record that its AGENTS.md cites is not in the local harness checkout; only that AGENTS.md reference turned up.
  - kw-website and paperclip have no `.ki.toml`, so they are out of scope.
- **Husky versus `.githooks`:** only ki-design still uses Husky, and its replacement stubs are already committed.
- **Behaviour under `mgit ci` and other non-interactive runs:**
  - `mgit ci` is the Git alias `ci = commit` fanned out over 8 jobs, with stdin from `/dev/null` and `GIT_EDITOR=false`. Each job's output is buffered, and progress moves only as the _oldest_ job finishes.
  - I confirmed in a scratch repository that pre-commit runs even with nothing staged. So every estate-wide `mgit ci` runs both bats suites, and progress stalls behind them, which is the "looks hung" symptom.
  - Without `-m`, the hooks run in full and then the commit aborts on the editor, so all of the cost buys no commit.
  - ki-design's `bunx` lines, and `bunx` inside every lint-staged config, would try to download from the registry if a tool were missing locally, a network call that could hang offline. ki-design has no refusal frame to stop that first.
  - A fresh clone without `bun install` refuses loudly. That is correct, but it makes `mgit ci` fail there.
  - The bats runs already redirect stdin and clear `GIT_*`, and the audits are local and quick (0.2–1.6 s). Nothing I found prompts for input.

## In Progress

Nothing.

## Queries

**Context:** tools-mgit and tools-rig run their whole bats suites (141 and 602 tests) on every commit, because `ki-repo-tools` SHELL-HOOK requires `bats` in the hook without limiting it. **Query:** How should SHELL-HOOK scope bats? **Options:** a) (recommended, confidence high - this keeps fast feedback and leaves CI as the authority, as the standard already intends) Amend SHELL-HOOK so the hook requires shellcheck, `bash -n` and mandoc, plus either a named fast bats subset or bats only when the staged paths touch `bin/`, `src/` or `tests/`; the full suite stays in CI. b) Move the full suite to a committed `pre-push` hook, which needs a frame rule for `pre-push` in `ki-repo`. c) Keep the whole suite in pre-commit and accept the cost.

**Context:** Git runs pre-commit even when nothing is staged, so an estate-wide `mgit ci` pays every repository's gate. **Query:** Should the `ki-repo` hook frame exit early when nothing is staged? **Options:** a) (recommended, confidence medium - it is cheap and estate-wide, but it needs a check that `--amend` and merge commits still get checked) Add `git diff --cached --quiet && exit 0` after the tool-refusal step of the frame. b) Fix only the expensive hooks, through the first query. c) Leave the frame as it is.

**Context:** chezmoi has no hook, and its AGENTS.md describes a manual gate. Under `ki-repo-dotfiles-chezmoi` GIT-2 a hook must run `ki repo audit` check-only. chezmoi has no package, so it gets pre-commit only until `KI-TOOL-KI-CLI-161`. **Query:** Should chezmoi get a committed `.githooks/pre-commit`? **Options:** a) (recommended, confidence medium - the `KI-HARNESS-GOV-117` record is not in the local harness checkout, so its outcome is unconfirmed) Yes: a package-less hook in the frame that refuses without `ki`, `rumdl` or `node`, then runs `ki repo audit --repo "$root" --staged` (concise form), `rumdl check` on staged Markdown and `node --test tests/*.test.mjs`, with `core.hooksPath` set in each clone. b) Audit and rumdl only, leaving `node --test` to manual and CI runs. c) Keep no hook until `KI-HARNESS-GOV-117` decides.

**Context:** ki-design is the last Husky repository (HOOK-2 and HOOK-5). Correct `.githooks` stubs are already committed but delegate to `.husky/`. **Query:** Should ki-design be migrated now or left for the tools-ki composition sweep? **Options:** a) (recommended, confidence high - this is small and closes the unchecked-worktree gap) Migrate now: inline the `.husky/` content into the stubs without `bunx`, switch `prepare` to `git config core.hooksPath .githooks`, and remove `husky` and `.husky/`. b) Wait for the tools-ki hook-composition and binding sweep.

**Context:** ki-agentic-harness lacks the `ki-repo-harness` GATE-1 line, and the homebrew-tap and specifications shape skills declare no hook content criterion although their repositories already run audits. **Query:** Should these governance gaps be closed? **Options:** a) (recommended, confidence medium - the hooks already do the right thing, so this aligns the standard with practice) Add the GATE-1 audit line to the harness hook, and add one check-only content criterion each to `ki-repo-homebrew-tap` and `ki-repo-specifications`. b) Leave them at WARN until the hooks rollout's final wave.

**Context:** kw-website (knowledge-wayfinder) and paperclip (a pnpm fork) sit in the workspace without `.ki.toml`, so the commit-gate standard does not cover them. **Query:** Should they stay outside the gate? **Options:** a) (recommended, confidence medium - paperclip follows upstream conventions and kw-website belongs to another organisation) Leave both out of scope and leave `mgit` selection as it is. b) Adopt `.ki.toml` and the common package gate in kw-website only. c) Adopt both.
