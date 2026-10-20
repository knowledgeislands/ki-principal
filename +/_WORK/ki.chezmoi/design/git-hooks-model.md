# Git hooks model

Design note for Kris to sanity-check before anything is implemented, written on 20 October 2026 at 03:19 BST from his direction at 03:14 BST: hooks are uniform and set once per kind of repository, their details maintained through audit and conformance; they do basic linting, formatting and commit-message checks; they never run test suites; and each repository shape defines its hooks consistently. Nothing has changed in any repository, standard or configuration with this note, and it creates no work records.

Evidence: the [hooks survey](/Users/krisbrown/.local/state/ki/agents/chezmoi/hooks-survey.report.md) of 24 repositories, with three corrections (20 repositories bind `.githooks`, not 21; `ki-repo-tools` `SHELL-HOOK` and `ki-repo-dotfiles-chezmoi` `GIT-2` are FAIL-severity, and `ki-repo-kb` `GATE-1` and `ki-engineering` `SCR-11` are FAIL too, while `ki-repo-harness` `GATE-1` and `HOOK-1` to `HOOK-5` are WARN; Syncpack runs even when nothing is staged); the `ki-repo` [Commit gate](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md#commit-gate) and [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md); the shape standards named in section 4; the earlier [hooks-standard design](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/design/hooks-standard.md); the committed hooks themselves; and three facts checked for this note: `ki git check-message` ships in `ki` 0.12.0 and takes 0.1 s, the installed harness collection is a symlink to the primary harness checkout, and the chezmoi source has no CI workflow.

## Short answers

- **Keep `.githooks` with `core.hooksPath`. Moving off Husky was right.** The slowness and the test suites came from what the hooks run, not from how they are bound; Husky would have run the same bats suites.
- **One frame for every hook, with one addition:** a commit with nothing staged exits at once, so an estate-wide `mgit ci` costs nothing in a clean repository.
- **One content rule for every shape:** a hook runs lint, format and commit-message checks over what is staged, quietly, offline and within a few seconds. Test suites, whole-project type checks, full audits and anything that fetches from the network go to the repository's manual gate and CI.
- **Per shape, the hook is fixed by the shape skill** and the audit enforces both halves: what must be there (each shape's content criterion) and what must not (a new `ki-repo` `HOOK-6`).
- **Commit-message checks reach every repository now,** because `ki git check-message` has shipped.

## 1. Binding: `.githooks` versus Husky

**Boundary.** How Git finds and runs the hook in each clone and worktree. It does not decide what the hook runs.

**How it works now.** The hook files live in the tracked `.githooks/` directory, and each clone runs `git config core.hooksPath .githooks` once. Package-backed repositories do that in their `prepare` script, so `bun install` binds a fresh clone; package-less repositories get it from `ki repo conform` (KI-TOOL-KI-CLI-163). Twenty repositories are bound this way, and ki-design converted locally shortly before this note (commit `7cb9f1d`, not yet pushed).

**Why not Husky.** Husky 9 does one useful thing: it sets the binding on `bun install`. Everything else counts against it:

- **Linked worktrees.** Husky binds to `.husky/_`, an untracked directory that `bun install` generates. A linked worktree that has never run `bun install` has no `.husky/_`, so Git finds no hook and the commit goes through unchecked, silently. Agents work in linked worktrees all the time (the harness's GREEN-MAIN rule requires it). A tracked `.githooks/` is present in every worktree at the revision it has checked out.
- **Package-less repositories.** Husky installs through the package lifecycle. Roughly half the estate has no `package.json`: the shell tools, the tap, the specifications, the chezmoi source and most principals and harnesses outside Knowledge Islands. Husky cannot serve them, so it would leave two mechanisms side by side.
- **`node_modules` dependence.** Husky's runtime sits in `node_modules`, so a clone without an install is ungated. With `.githooks`, the hook itself is always present, and it refuses loudly when a tool is missing rather than letting the commit pass.

**What Husky would not have fixed.** The tools-mgit and tools-rig hooks run 141 and 602 bats tests because `SHELL-HOOK` requires bats in the hook, and every repository's hook runs even when nothing is staged because Git calls pre-commit regardless. Both are content and frame problems; section 2 and section 3 fix them.

**Alternatives looked at.** Lefthook and the pre-commit framework each add a runtime and a per-clone install step, the same binding gap Husky has, for parallelism and file filtering that a two-line shell hook does not need.

**Recommendation.** Keep `.githooks` and `core.hooksPath`; finish the Husky exit with ki-design's push. The remaining gaps are known and small: a fresh package-less clone needs `ki repo conform` once, and a worktree checked out at a revision older than its `.githooks/` commits unchecked.

## 2. The frame every hook shares

**Boundary.** The lines before and around the content, identical in every hook in every repository. `ki-repo` owns it (`HOOK-1` to `HOOK-5`, plus `HOOK-6` below) and never names a content command.

1. `#!/bin/sh`, then `root="$(git rev-parse --show-toplevel)" || exit 1`.
2. **New, pre-commit only:** `git diff --cached --quiet && exit 0`. Nothing staged means nothing to check, and Git then reports "nothing to commit" itself. `git commit -a` and `git commit <paths>` still work, because Git points `GIT_INDEX_FILE` at the temporary index before calling the hook. An `--amend` with nothing newly staged skips the gate; its tree already passed when first committed. Placement is the second query.
3. Refuse unless every tool the content calls is present: `node_modules/.bin/<tool>` in a package-backed repository, `command -v <tool>` otherwise. The refusal names the missing tools and the install step, and ends "do not bypass with --no-verify; a gate that cannot run is unknown, not a pass." The list now includes every tool the content reaches indirectly, so `biome` and `rumdl` join `lint-staged` and `syncpack` in package-backed repositories.
4. In a package-backed repository, put `$root/node_modules/.bin` on `PATH`.
5. The content, each command ending `|| exit 1`, with `"$@"` forwarded where a hook takes arguments.

Rules every hook's content follows, whatever its shape:

- **Lint, format and message only.** No test runner (`bats`, `bun test`, `bun run test`, `vitest`, `node --test`, `ruby test/...`), no whole-project type check (`tsc --noEmit`), no full multi-skill `ki repo audit`, no build.
- **Check-only,** with one exception kept from `SCR-11`: `lint-staged` may apply staged formatters (`biome check --write`, `rumdl check --fix`), because it restores partially staged files safely. Without `lint-staged`, a hook checks and never rewrites.
- **Staged scope.** A check runs over staged files of its type, or runs only when such a file is staged. CI keeps the whole-tree verdict.
- **Quiet on success.** One line or nothing when it passes; full output only on failure (`lint-staged --quiet`; the audit runs concise, then in full on failure).
- **Offline and non-interactive.** Tools are called by bare name after the refusal, never through `bunx`, `npx` or `pnpm dlx`, which would try the registry when a tool is missing. Nothing reads standard input.
- **Budget.** A typical pre-commit finishes in under five seconds, and commit-msg in under one.

## 3. Hook content by repository shape

**Boundary.** What each kind of repository runs after the frame. Each row is the whole hook for that shape; a repository adds nothing that its shape skill does not list, apart from the generated-file check in tools-rig noted below.

| Shape (repositories) | `pre-commit` after the frame | `commit-msg` | Moves to the manual gate and CI |
| --- | --- | --- | --- |
| Package-backed engineering (the 14 common copies, tools-ki, ki-design) | `lint-staged --quiet`: Biome over staged code, rumdl over staged Markdown; then `syncpack format --check` | `commitlint --edit "$1"`, or `ki git check-message "$1"` (fourth query) | type check, Knip, tests and coverage, which `ki repo audit` and CI already run |
| Knowledge base, package-backed (ki-principal) | the engineering lines, then `ki repo audit --skill ki-repo-kb --staged` | as engineering | nothing new |
| Knowledge base, package-less (va-principal and the other principals) | `rumdl check` over staged Markdown, then `ki repo audit --skill ki-repo-kb --staged` | `ki git check-message "$1"` | nothing new |
| Harness (ki-agentic-harness; package-less harnesses take the package-less lines) | the engineering lines, then `ki repo audit --skill ki-repo-harness --staged` | as engineering | `tsc --noEmit`, the staged-snapshot `ki-skills` audit and the diagram-receipt check (third query) |
| Package-less shell tool (tools-mgit, tools-rig) | when a shell file is staged, `shellcheck` and `bash -n` over the declared shell files; `mandoc -T lint` when the manual page is staged; `rumdl check` over staged Markdown; `ki repo audit --skill ki-repo-tools --staged` | `ki git check-message "$1"` | the whole bats suite, which CI already runs (`SHELL-TEST`) |
| Specifications (ki-specifications) | `rumdl check` over staged Markdown, then `ki repo audit --skill ki-repo-specifications --staged` | `ki git check-message "$1"` | nothing new |
| Homebrew tap (homebrew-tap) | `ruby -wc` over staged `.rb` files, `rumdl check` over staged Markdown, then `ki repo audit --skill ki-repo-homebrew-tap --staged` | `ki git check-message "$1"` | the two Ruby test files, which CI already runs |
| chezmoi dotfiles (the chezmoi source) | `rumdl check` over staged Markdown, then `ki repo audit --skill ki-repo-dotfiles-chezmoi --staged` | `ki git check-message "$1"` | `node --test tests/*.test.mjs`, which stays in AGENTS.md's manual gate because the source has no CI (sixth query) |
| Design (ki-design) | as package-backed engineering: it declares `ki-engineering` and `ki-repo-project`, and no design shape skill exists | as engineering | as engineering |

Verdicts on the contested lines:

- **Shape audits stay** (`ki repo audit --skill <shape> --staged`). They are structural lint of the repository's own shape, they are the only lint the package-less shapes have, and they take 0.2 to 1.6 s. Two limits keep them lint: always the one focused shape skill, never the full audit over every declared skill (which, in a package-backed repository, runs the engineering type check, Knip and coverage); and always `--staged`. Generic package-backed repositories get no audit line, because their shape audit is the heavy engineering one. First query.
- **Type checking goes.** `tsc --noEmit` is whole-project, can take tens of seconds and can write build information. Biome already lints staged code, and the engineering audit and CI type-check every change. Third query, with the harness's other two heavy lines.
- **Syncpack stays, unconditional.** It takes 0.1 s, and the new empty-index exit removes the nothing-staged case that the survey's correction raised.
- **Every test suite goes:** bats in tools-mgit (141 tests) and tools-rig (602), the Ruby tests in homebrew-tap, `node --test` in chezmoi. Each repository's CI or manual gate already names them.
- **Generated-file checks stay where they are fast and check-only.** `scripts/assemble-rig --check` in tools-rig is a format check of the assembled `bin/rig`, so it stays, run only when `src/rig/` or `bin/rig` is staged, subject to a timing check during implementation.
- **Markdown formatting is uniform.** Every repository checks staged Markdown with rumdl: through `lint-staged` where a package exists, and as a plain `rumdl check` over staged files where none does.

## 4. Where each rule lives

**Boundary.** Which standard and rubric criterion owns each line, so that `ki repo audit` reports drift and, once hook composition lands, `ki repo conform` repairs it. Today the content criteria only check that a required line is present; nothing stops a repository adding a test suite, which is how the shell tools drifted. `HOOK-6` closes that.

| Line or rule | Owning standard | Criterion | Severity now, proposed |
| --- | --- | --- | --- |
| Hook exists, tracked, executable | `ki-repo` Commit gate | `HOOK-1` (pre-commit), `HOOK-3` (commit-msg, now required in every repository) | WARN, FAIL after the last wave |
| Bound to `.githooks` | `ki-repo` | `HOOK-2` | WARN, then FAIL |
| Frame, including the empty-index exit | `ki-repo` | `HOOK-4` (amended to accept the exit line) | WARN, then FAIL |
| Husky gone | `ki-repo` | `HOOK-5` | WARN, then FAIL |
| No test runner, whole-project type check, full audit or `bunx`/`npx` in a hook | `ki-repo` | `HOOK-6`, new | WARN, then FAIL |
| Stated gate matches the hook | `ki-repo` | `HOOK-J1` | judgement |
| `lint-staged --quiet`, `syncpack format --check`, `commitlint` or `check-message` | `ki-engineering` Common local Git hooks | `SCR-11` | FAIL, unchanged |
| `lint-staged` block calls Biome and rumdl without `bunx` | `ki-engineering` | `PKG-6` | as `PKG-6` |
| `rumdl check` over staged Markdown where no package exists | `ki-authoring` | new content criterion | WARN, then FAIL |
| `ki git check-message` where no package exists | `ki-git` Commit-message binding | named by `HOOK-3`; vocabulary stays with `ki-git` | as `HOOK-3` |
| KB focused audit | `ki-repo-kb` Commit gate | `GATE-1`, tightened to `--skill ki-repo-kb --staged` | FAIL, unchanged |
| Harness focused audit | `ki-repo-harness` Commit gate | `GATE-1` | WARN, then FAIL |
| `shellcheck`, `bash -n`, `mandoc -T lint`, tools focused audit | `ki-repo-tools` capability conditionals | `SHELL-HOOK`, reworded: bats leaves, the three linters and the audit come in | FAIL, unchanged |
| Specifications focused audit | `ki-repo-specifications` | `GATE-1`, new | WARN, then FAIL |
| `ruby -wc`, tap focused audit | `ki-repo-homebrew-tap` | `GATE-1`, new | WARN, then FAIL |
| chezmoi focused audit | `ki-repo-dotfiles-chezmoi` | `GIT-2`, tightened to `--skill ki-repo-dotfiles-chezmoi --staged` | FAIL, unchanged |

Writing the hooks from these declarations, so that conform keeps every copy byte-identical to its shape, stays with the existing records [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) and [KI-TOOL-KI-CLI-165](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md). Until then each shape standard carries its hook text as a worked example, the hooks are written by hand from it, and the audit holds them to it. Fifth query.

## 5. Change list, in dependency order

Two ordering facts drive this. The installed harness collection is a symlink to the primary harness checkout, so standards take effect on this machine the moment harness `main` moves, and on the other machine after its pull. And each shell tool's hook runs its own `ki-repo-tools` audit over the staged hook, where `SHELL-HOOK` is FAIL and today requires bats: a commit that removes bats is refused by its own gate until the reworded `SHELL-HOOK` is live. So the harness lands first and every repository follows.

### 5.1 ki-agentic-harness standards, one unit

Under GREEN-MAIN: in a linked worktree off the shared primary checkout, never in it, fast-forwarded into `main` only when `bun run test`, `bunx tsc --noEmit` and the focused audit of every touched skill pass. Local commits only; Kris pushes.

1. **ADR-KI-HARNESS-SKILLS-017**, refined in place: hook content is limited to lint, format and message checks; test suites and whole-project checks belong to the manual gate and CI; `HOOK-6` enforces it; `commit-msg` is required everywhere now that `ki git check-message` ships.
2. **`ki-repo`** Commit gate text (frame step 2, the content rules of section 2, `HOOK-3` everywhere); `HOOK-4` accepts the empty-index line; new `HOOK-6`; rubric items, contexts and tests in `scripts/rubric/{items,contexts}/hooks.ts`; regenerated `references/rubric.md`.
3. **`ki-engineering`** Common local Git hooks: refusal covers `biome` and `rumdl`; type checking is named as not hook content; `PKG-6` rejects `bunx` in the `lint-staged` block; `SCR-11` follows the fourth query's answer; items and tests.
4. **`ki-authoring`**: the new staged-Markdown criterion for package-less hooks.
5. **`ki-git`** Commit-message binding: `ki git check-message "$1"` is the package-less line now, not a future one.
6. **`ki-repo-kb` `GATE-1`** and **`ki-repo-dotfiles-chezmoi` `GIT-2`**: tighten to the focused `--staged` form; items and tests.
7. **`ki-repo-tools` `SHELL-HOOK`**: reword (bats out, `bash -n` and `mandoc` in, focused audit in); the standard's capability-conditionals row and its commit-msg sentence; `shell.ts` and tests.
8. **`ki-repo-specifications`** and **`ki-repo-homebrew-tap`**: one new `GATE-1` each, standard text, items and tests.
9. **`ki-repo-harness`**: the standard names `tsc`, the `ki-skills` audit and the receipt check as manual-gate and CI work, subject to the third query.
10. **The harness's own hook**, a separate commit in the same worktree: empty-index exit, `GATE-1` audit line added, the three heavy lines removed (or kept, per the third query), `biome` and `rumdl` in the refusal; the AGENTS.md sentence describing the hook rewritten for `HOOK-J1`. Then fast-forward `main`.

### 5.2 Repository hooks, each its own local commit by explicit path

After 5.1 is on harness `main`. Each repository: edit `.githooks/pre-commit`, add or edit `.githooks/commit-msg` at mode `100755`, make one test commit in a scratch linked worktree, then commit; Kris pushes.

1. **tools-mgit**: remove bats; scope shellcheck, `bash -n` and mandoc as in section 3; add `rumdl`; add `commit-msg`.
2. **tools-rig**: the same, keeping `assemble-rig --check` behind its staged-path condition.
3. **homebrew-tap**: remove the two Ruby test files; add `ruby -wc` over staged `.rb`, `rumdl` and `commit-msg`.
4. **ki-specifications**: add the empty-index exit, `rumdl` and `commit-msg`.
5. **ki-principal**: the common package delta below, keeping its KB audit line.
6. **The 14 common copies**, byte-identical today: one scripted delta applied per repository (empty-index exit; `biome` and `rumdl` in the refusal; `lint-staged --quiet`; `bunx` out of the `package.json` `lint-staged` block; `commit-msg` per the fourth query), one commit each.
7. **ki-design**: being migrated separately now (its Husky exit is committed locally as `7cb9f1d`); it takes the common package delta after that lands.
8. **The chezmoi source**: new `.githooks/pre-commit` and `.githooks/commit-msg` per section 3; the AGENTS.md "no Git hook" paragraph rewritten for `HOOK-J1`; and the binding `git config core.hooksPath .githooks`, a configuration write that needs Kris's approval. chezmoi ignores source entries that begin with a dot, so `.githooks/` deploys nothing to `$HOME`.
9. **Other territories' repositories** follow by shape under their own grants, as the earlier design's waves 3 and 4 set out.
10. **Severity step**: after the last repository, raise `HOOK-1` to `HOOK-6` and the new `GATE-1` criteria to FAIL, as already planned.

## Open decisions

1. **SHAPE-AUDIT.** Are focused shape audits lint? a) Yes: keep exactly one focused `--staged` shape audit per hook, never the full audit (recommended). b) No: move every audit to CI, leaving package-less shapes with only rumdl and their language linters.
2. **EMPTY-EXIT.** Where does the empty-index exit sit? a) Before the tool refusal, so a clean `mgit ci` passes even in a clone without `bun install`, with `HOOK-4` amended to accept this one line (recommended). b) After the refusal, leaving `HOOK-4` unchanged. c) No exit.
3. **HARNESS-HEAVY.** What happens to the harness's type check, staged-snapshot `ki-skills` audit and diagram-receipt check? a) All three move to the manual gate and CI (recommended). b) Keep the `ki-skills` audit when skills are staged, move the other two. c) Keep all three.
4. **MSG-UNIFY.** One commit-message gate everywhere? a) `ki git check-message "$1"` in every repository, retiring Commitlint and its configuration from package-backed repositories (recommended). b) Commitlint where a package exists, `check-message` elsewhere.
5. **STRICT-SHAPE.** How strictly does the audit hold each hook to its shape before composition lands? a) Required lines plus `HOOK-6`'s forbidden list (recommended). b) Exact match to the shape's worked example, nothing else allowed.
6. **CHEZMOI-TESTS.** With `node --test` out of the hook and no CI, where do chezmoi's tests run? a) Stay in AGENTS.md's manual gate, which agents already run before committing (recommended). b) Add a CI workflow to the chezmoi source as well.
