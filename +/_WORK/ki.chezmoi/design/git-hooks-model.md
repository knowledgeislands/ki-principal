# Git hooks model

Design note for Kris to sanity-check before anything is implemented. First written on 20 October 2026 at 03:19 BST from his direction at 03:14 BST: hooks are uniform and set once per kind of repository, their details maintained through audit and conformance; they do basic linting, formatting and commit-message checks; they never run test suites; and each repository shape defines its hooks consistently. Revised at 03:55 BST to his decisions at 03:47 BST, with a new section on mechanical conform. Nothing has changed in any repository, standard or configuration with this note, and it creates no work records.

Evidence: the [hooks survey](/Users/krisbrown/.local/state/ki/agents/chezmoi/hooks-survey.report.md) of 24 repositories, with its three corrections; the `ki-repo` [Commit gate](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md#commit-gate) and [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md); `ki-engineering` [Common local Git hooks](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-engineering/references/standards-engineering.md#common-local-git-hooks) and its repair code in `scripts/rubric/contexts/git-hooks.ts`; the tools-ki hook converter, `src/core/repository/hooks.ts`; the records [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) and [KI-TOOL-KI-CLI-165 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/fde00e97/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md); the earlier [hooks-standard design](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/design/hooks-standard.md); the committed hooks themselves; and the `primary_shape` each Knowledge Islands repository declares in `.ki.toml`.

## Decisions taken

Kris's answers at 03:47 BST, as the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/decisions.md) records them:

- **AUDIT-LINT a).** Exactly one focused `--staged` shape audit per hook, never the full audit.
- **EMPTY-EXIT a).** The empty-index exit sits before the missing-tool refusal, and `HOOK-4` is amended to accept it.
- **HARNESS-LINES a).** The harness's `tsc --noEmit`, staged-snapshot `ki-skills` audit and diagram-receipt check leave the hook for the manual gate and CI.
- **Dotfiles shape: no hook.** "It should be nothing for a dot files repo." The chezmoi source gets no `.githooks/`, `ki-repo-dotfiles-chezmoi` `GIT-2` changes to require none, and the manual gate in its AGENTS.md stays. This also settles the former CHEZMOI-TESTS query: `node --test` stays in that manual gate.
- **Standing rule.** A repository without `.ki.toml` is outside the standards, always. `ki-repo` already says so ("a repository without `.ki.toml` is out of scope"); nothing here reaches such a repository.
- **STRICTNESS a), provisionally.** The audit requires each recipe's required lines and forbids a list. Kris's concern: "that doesn't really help us then with the conform aspect, right? Mechanical conform." He floated extension points inside the hook. Section 5 answers it and the closing query asks him to settle it.

Still open: **MSG-UNIFY.** Until Kris decides otherwise, package-backed repositories keep `commitlint --edit "$1"` and every other repository uses `ki git check-message "$1"`. This note writes the package-backed `commit-msg` line as "the package message line", so either answer drops in without changing anything else.

## Short answers

- **Binding is settled:** `.githooks/` with a relative `core.hooksPath`.
- **One frame for every hook,** opening with an exit when nothing is staged, so an estate-wide `mgit ci` costs nothing in a clean repository even without `bun install`.
- **One content rule:** a hook runs lint, format and commit-message checks over what is staged, quietly, offline and within a few seconds. Test suites, whole-project type checks, full audits and network fetches go to the manual gate and CI.
- **The hook is set by the repository's declared `primary_shape`** and whether it has a `package.json`. The dotfiles shape sets no hook at all.
- **Mechanical conform needs a canonical hook, not a checklist.** Required lines plus a forbidden list can be audited but not conformed: conform can add a missing line but cannot place it reliably, cannot remove a forbidden one safely, and leaves two repositories of one shape different. A canonical hook per shape, written byte-exact by conform and audited exact, with one declared extension file for the rare repository-specific check, is mechanical and idempotent. The closing query recommends it.

## 1. Binding

**Boundary.** How Git finds the hook in each clone and worktree; not what it runs.

The hook files live in the tracked `.githooks/`, and each clone runs `git config core.hooksPath .githooks` once: package-backed repositories in their `prepare` script, so `bun install` binds a fresh clone, and package-less repositories through `ki repo conform` ([KI-TOOL-KI-CLI-163 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/958c5d84fc5fdfabd63fdbd02f88a39ca9b61b05/docs/roadmap/KI-TOOL-KI-CLI-163-githooks-conversion.md)). Kris settled this at 03:16 BST; the note no longer weighs Husky. The two known gaps stay small: a fresh package-less clone needs `ki repo conform` once, and a worktree checked out at a revision older than its `.githooks/` commits unchecked.

## 2. The frame every hook shares

**Boundary.** The lines before and around the content, identical in every hook in every repository. `ki-repo` owns it (`HOOK-1` to `HOOK-5`, plus `HOOK-6` below) and never names a content command.

1. `#!/bin/sh`, then `root="$(git rev-parse --show-toplevel)" || exit 1`.
2. **Pre-commit only, decided under EMPTY-EXIT a):** `git diff --cached --quiet && exit 0`, before the refusal. Nothing staged means nothing to check, and Git then reports "nothing to commit" itself. `git commit -a` and `git commit <paths>` still work, because Git points `GIT_INDEX_FILE` at the temporary index before calling the hook. An `--amend` with nothing newly staged skips the gate; its tree already passed when first committed.
3. Refuse unless every tool the content calls is present: `node_modules/.bin/<tool>` in a package-backed repository, `command -v <tool>` otherwise. The refusal names the missing tools and the install step and ends "do not bypass with --no-verify; a gate that cannot run is unknown, not a pass." It covers every tool the content reaches, so `biome` and `rumdl` join `lint-staged` and `syncpack` in package-backed repositories.
4. In a package-backed repository, put `$root/node_modules/.bin` on `PATH`.
5. Where a shape audit runs, one quiet-audit helper: a shell function that runs `ki repo audit --repo "$root" --staged` concisely and, on failure, runs it again in full and returns 1. Today's hooks end with an inline `&& exit 0`, rerun, `exit 1` sequence, which breaks the standard's own rule that every command ends `|| exit 1` and makes any line after it unreachable. As a function, the audit becomes one more line ending `|| exit 1`.
6. The content, each command ending `|| exit 1`, with `"$@"` forwarded where a hook takes arguments.

Rules every hook's content follows, whatever its shape:

- **Lint, format and message only.** No test runner (`bats`, `bun test`, `bun run test`, `vitest`, `node --test`, `ruby test/...`), no whole-project type check (`tsc --noEmit`), no full multi-skill `ki repo audit`, no build.
- **Check-only,** with one exception kept from `SCR-11`: `lint-staged` may apply staged formatters (`biome check --write`, `rumdl check --fix`), because it restores partially staged files safely. Without `lint-staged`, a hook checks and never rewrites.
- **Staged scope.** A check runs over staged files of its type, or only when such a file is staged. CI keeps the whole-tree verdict.
- **Quiet on success.** One line or nothing when it passes; full output only on failure.
- **Offline and non-interactive.** Tools are called by bare name after the refusal, never through `bunx`, `npx` or `pnpm dlx`. Nothing reads standard input.
- **Budget.** A typical pre-commit finishes in under five seconds, and commit-msg in under one.

## 3. Hook content by repository shape

**Boundary.** What each kind of repository runs after the frame. The shape is the `primary_shape` that `ki-repo` already requires in every `.ki.toml`, so no new declaration is needed to tell a repository's shape; the only other input is whether the repository has a `package.json`. Under the provisional STRICTNESS a), each row lists a shape's required lines and the forbidden list applies everywhere; section 5 compares that with writing each row as the whole hook.

| `primary_shape` (repositories) | `pre-commit` after the frame | `commit-msg` | Moves to the manual gate and CI |
| --- | --- | --- | --- |
| Package-backed, no shape lines: `ki-repo-project`, `ki-repo-mcp`, `ki-repo-website`, and package-backed `ki-repo-tools` (in Knowledge Islands, 12 repositories plus tools-ki, tools-git-almanac and tools-techne) | `lint-staged --quiet`: Biome over staged code, rumdl over staged Markdown; then `syncpack format --check` | the package message line | type check, Knip, tests and coverage, which `ki repo audit` and CI already run |
| `ki-repo-kb`, package-backed (ki-principal) | the package lines, then the quiet audit `--skill ki-repo-kb` | the package message line | nothing new |
| `ki-repo-kb`, package-less (va-principal and the other principals) | `rumdl check` over staged Markdown, then the quiet audit `--skill ki-repo-kb` | `ki git check-message "$1"` | nothing new |
| `ki-repo-harness` (ki-agentic-harness; package-less harnesses take the package-less KB pattern with `--skill ki-repo-harness`) | the package lines, then the quiet audit `--skill ki-repo-harness` | the package message line | `tsc --noEmit`, the staged-snapshot `ki-skills` audit and the diagram-receipt check, decided under HARNESS-LINES a) |
| `ki-repo-tools`, package-less (tools-mgit, tools-rig) | when shell files are staged, `shellcheck` and `bash -n` over them; `mandoc -T lint` when a manual page is staged; `rumdl check` over staged Markdown; the quiet audit `--skill ki-repo-tools` | `ki git check-message "$1"` | the whole bats suite, which CI already runs (`SHELL-TEST`) |
| `ki-repo-specifications` (ki-specifications) | `rumdl check` over staged Markdown, then the quiet audit `--skill ki-repo-specifications` | `ki git check-message "$1"` | nothing new |
| `ki-repo-homebrew-tap` (homebrew-tap) | `ruby -wc` over staged `.rb` files, `rumdl check` over staged Markdown, then the quiet audit `--skill ki-repo-homebrew-tap` | `ki git check-message "$1"` | the two Ruby test files, which CI already runs |
| `ki-repo-dotfiles-chezmoi` (the chezmoi source) | **no hook**: no `.githooks/` and no `core.hooksPath` | **no hook** | `node --test tests/*.test.mjs` and the focused audit stay in AGENTS.md's manual gate; the source has no CI |

ki-techne-harness declares `ki-repo-project`, so it takes the first row, not the harness row.

Verdicts on the contested lines:

- **Shape audits stay, one per hook, decided under AUDIT-LINT a):** always the one focused shape skill and always `--staged`, never the full audit over every declared skill. Package-backed repositories with no shape lines get no audit line, because their shape audit is the heavy engineering one.
- **Type checking goes,** with the harness's other two heavy lines, decided under HARNESS-LINES a).
- **Syncpack stays, unconditional.** It takes 0.1 s, and the empty-index exit removes the nothing-staged case.
- **Every test suite goes:** bats in tools-mgit (141 tests) and tools-rig (602), the Ruby tests in homebrew-tap. Each repository's CI already names them.
- **`scripts/assemble-rig --check` in tools-rig** is the one repository-specific check that is fast, check-only and not a test. It stays, run only when `src/rig/` or `bin/rig` is staged; where it lives depends on the closing query (section 5.3).
- **Markdown formatting is uniform.** Every hooked repository checks staged Markdown with rumdl: through `lint-staged` where a package exists, and as a plain `rumdl check` over staged files where none does.

## 4. Where each rule lives

**Boundary.** Which standard and rubric criterion owns each line, so that `ki repo audit` reports drift and `ki repo conform` repairs it. The table is written for the provisional STRICTNESS a); the paragraph after it says what changes under the closing query's recommendation.

| Line or rule | Owning standard | Criterion | Severity now, proposed |
| --- | --- | --- | --- |
| Hook exists, tracked, executable | `ki-repo` Commit gate | `HOOK-1` (pre-commit), `HOOK-3` (commit-msg, now required wherever a hook is), both not applicable where the shape declares no hook | WARN, FAIL after the last wave |
| Bound to `.githooks`, or unbound where the shape declares no hook | `ki-repo` | `HOOK-2` | WARN, then FAIL |
| Frame, with the empty-index exit before the refusal and the quiet-audit helper | `ki-repo` | `HOOK-4`, amended (EMPTY-EXIT a)) | WARN, then FAIL |
| Husky gone, in every repository including the no-hook shape | `ki-repo` | `HOOK-5` | WARN, then FAIL |
| No test runner, whole-project type check, full audit or `bunx`/`npx` in a hook | `ki-repo` | `HOOK-6`, new | WARN, then FAIL |
| Stated gate matches the hook | `ki-repo` | `HOOK-J1` | judgement |
| `lint-staged --quiet`, `syncpack format --check`, the package message line | `ki-engineering` Common local Git hooks | `SCR-11` | FAIL, unchanged |
| `lint-staged` block calls Biome and rumdl without `bunx` | `ki-engineering` | `PKG-6` | as `PKG-6` |
| `rumdl check` over staged Markdown where no package exists | `ki-authoring` | new content criterion | WARN, then FAIL |
| `ki git check-message` where no package exists | `ki-git` Commit-message binding | named by `HOOK-3`; vocabulary stays with `ki-git` | as `HOOK-3` |
| KB focused audit | `ki-repo-kb` Commit gate | `GATE-1`, tightened to `--skill ki-repo-kb --staged` | FAIL, unchanged |
| Harness focused audit; `tsc`, `ki-skills` audit and receipt check named as manual-gate and CI work | `ki-repo-harness` Commit gate | `GATE-1` | WARN, then FAIL |
| `shellcheck`, `bash -n`, `mandoc -T lint`, tools focused audit | `ki-repo-tools` capability conditionals | `SHELL-HOOK`, reworded: bats leaves, the three linters and the audit come in | FAIL, unchanged |
| Specifications focused audit | `ki-repo-specifications` | `GATE-1`, new | WARN, then FAIL |
| `ruby -wc`, tap focused audit | `ki-repo-homebrew-tap` | `GATE-1`, new | WARN, then FAIL |
| Dotfiles shape declares no hook: no `.githooks/`, no `core.hooksPath` | `ki-repo-dotfiles-chezmoi` | `GIT-2`, changed to require none | FAIL, unchanged |

`HOOK-1` to `HOOK-4` must read the dotfiles shape's "no hook" declaration, or `HOOK-1` would report the chezmoi source for lacking the hook its shape forbids. The chezmoi source declares `.ki.toml`, so it stays inside the standards; the standing rule does not exempt it.

Under the closing query's recommendation, each content criterion keeps owning its block's text, but the audit of a hook collapses into one exact comparison: `HOOK-4` checks that each hook equals the hook composed for the repository's shape, and `HOOK-6`'s forbidden list applies only to the extension file. `SCR-11`, `GATE-1`, `SHELL-HOOK` and the new content criteria stop pattern-matching hook lines and instead check that their block, as declared, is what the composer emits.

## 5. Mechanical conform

**Boundary.** How `ki repo conform` writes a repository's hook where none exists and repairs one that has drifted, without judgement, and with a second run changing nothing. It does not decide what a shape runs (section 3) or who owns a line (section 4).

### 5.1 What conform does today

Two writers touch hooks, and neither composes one from a shape.

- **tools-ki, `src/core/repository/hooks.ts` ([KI-TOOL-KI-CLI-163 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/958c5d84fc5fdfabd63fdbd02f88a39ca9b61b05/docs/roadmap/KI-TOOL-KI-CLI-163-githooks-conversion.md)).** It converts a Husky repository: it reads `.husky/<hook>`, strips Husky's boilerplate, rewrites `bunx <tool>` to the bare tool, infers the refusal's tool list from what the content calls, prepends the frame and writes the file at mode `0755`. It refuses, writing nothing, whenever it meets a frame line it does not recognise. A committed hook that no longer delegates to `.husky/` is left untouched: there is nothing it knows to do.
- **ki-agentic-harness, `ki-engineering` `SCR-11`.** Its repair (`git-hooks.ts`) splits an existing hook at the frame's `export PATH`, removes any earlier copy of the required lines, writes `lint-staged --quiet || exit 1` and `syncpack format --check || exit 1` first, and keeps every other line after them. A rubric write cannot set the executable mode, so it never creates a hook; it leaves that to "hook composition", which is KI-HARNESS-GOV-225 (claims declared by skills) and KI-TOOL-KI-CLI-165 (the host composer). KI-TOOL-KI-CLI-165 plans to compose the frame and every declared skill's claimed lines in declared skill order and to refuse a hook with lines it cannot attribute; how a repository keeps its own lines is its open question, HOOK-LOCAL.

So today's repair is already the required-lines model, for one shape, and the other shapes' criteria (`GATE-1`, `SHELL-HOOK`, `GIT-2`) audit and never repair.

### 5.2 Three ways to make it mechanical

**(a) Required lines plus a forbidden list; conform adds missing lines.** The provisional STRICTNESS a), extending `SCR-11`'s repair to every shape.

- **Adding a line is not mechanical.** Where it goes depends on the hook around it. Today's audit idiom ends the hook with `exit 1`, so an appended line never runs; inserting before it means recognising shell control flow. Across shapes, the order of lines from two skills (package lines, then rumdl, then shape lint, then the audit) has to be encoded somewhere anyway.
- **Removing a forbidden line is not safe.** tools-rig's bats call is a three-line subshell with an environment reset; tools-mgit's is different. Conform can only refuse and leave the removal to a person, which is exactly the hand repair the shell tools needed.
- **The refusal list cannot be kept right.** The frame must name every tool the content calls. With arbitrary permitted lines, conform has to infer tools by parsing shell, as the Husky converter does with `bunx` and `ki` today, and it cannot see what a called script needs.
- **The forbidden list is open-ended.** It catches `bats` and `bun test`; it cannot catch `scripts/check.sh` running bats, or `make test`.
- **Two repositories of one shape stay different** in comments, order and extra lines, so "set once per shape" is never visible as a fact.
- **Idempotent:** yes, once the recognisers are exact. **Mechanical:** only for the lines it requires. **Cost:** lowest; it is today's `SCR-11` code generalised, plus `HOOK-6`.

A variant the model-blind review named, an ordered allowlist with nothing else permitted, is (b) without an extension point; it is option d) in the query.

**(b) A canonical hook per shape, written byte-exact by conform and audited exact, with one declared extension point.**

- **Conform writes the whole file.** It composes the hook for the repository's `primary_shape` and package presence, writes it at mode `0755` when it differs, and does nothing when it matches. Repair is overwrite; a second run is a no-op by construction. The refusal list is part of the canonical text, so it is always right for the lines the hook carries.
- **The audit is a byte comparison.** No pattern matching, no denylist over the main hook: anything not canonical is drift, including a test suite added by hand. Two repositories of one shape carry identical files, which `mgit` or a hash can show across the estate.
- **First adoption is the only judgement point, and conform keeps it narrow.** For a hook that is not yet canonical, conform subtracts the lines the canonical hook already carries and the lines on the forbidden list. If nothing is left, it overwrites and reports the forbidden lines it dropped. If anything is left, it refuses, writing nothing, and names those lines with the remedy "move them to the extension file or delete them". A one-line managed marker in the canonical header lets later runs overwrite without that step, the way the composed `.gitignore` blocks already fail closed on malformed markers.
- **One extension point, `.githooks/pre-commit.local`.** The canonical pre-commit always carries the same line, after the shape's lint lines and before the shape audit: run the file with `sh` if it exists, `|| exit 1`. It runs as a child, never sourced, so an `exit 0` inside it cannot skip the shape audit and it cannot change the hook's variables. The file follows the `HOOK-4` frame itself (its own refusal for the tools it calls) and `HOOK-6`'s forbidden list, and `HOOK-J1` judges it. Conform never writes or edits it; the audit reports its presence. There is no `commit-msg` extension: message checks are wholly governed.
- **Why one file and not `.githooks/pre-commit.d/`.** After the decided removals, the estate has exactly one repository-specific check, tools-rig's `assemble-rig --check`. ki-principal keeps nothing local, and the harness's local lines all leave under HARNESS-LINES a), its quiet-audit function becoming the frame's helper. A directory adds ordering, naming and mode rules for a need of one line.
- **An extension block inside the hook** is the variant Kris floated: a marked region of `.githooks/pre-commit` that conform preserves verbatim, as the `.gitignore` composition keeps its unmanaged tail. It is equally idempotent, but conform must then parse markers and fail closed on malformed ones, the audit compares the file minus the block rather than the whole file, and a hook of one shape is no longer byte-identical across repositories. It is option b) in the query.
- **Per-repository inputs move to run time.** tools-rig and tools-mgit each list their shell files by hand today. The canonical tools hook instead takes the staged paths ending `.sh` or `.bash`, plus staged files whose first line is a `sh` or `bash` shebang, and the staged `man/*` pages; that is also what the staged-scope rule asks. The detection is a few lines of the canonical text and needs a pilot timing and a pass over both shell repositories.
- **Cost.** The block text moves into declared data in the harness (each shape skill owns its block; `ki-repo` owns the frame), with each shape standard's worked example regenerated from it so the prose cannot drift. The composer in tools-ki is smaller than KI-TOOL-KI-CLI-165's attribution design, because exact comparison replaces line attribution everywhere except first adoption. Every change to a block churns every repository of that shape, one conform commit each; that is the point, but a block edit becomes an estate wave. Repositories lose freedom to add a line to the hook itself, and an extension file can grow; `HOOK-6`, `HOOK-J1` and the audit's report of its presence are the check on that.

**(c) The canonical hook generated from `.ki.toml` declarations.** Two readings.

- **(c1) From every declared skill's claims, in declared order.** This is KI-TOOL-KI-CLI-165 as written. It is as mechanical and idempotent as (b), since the output is deterministic, but the claims need conditions to compose: rumdl is `ki-authoring`'s line only where no `lint-staged` already runs it, the package lines appear only with a `package.json`, the tools lint only without one, and the dotfiles shape must suppress every other skill's claims. Reordering skills in `.ki.toml` would change the hook's bytes. Keyed instead on the one `primary_shape` plus package presence, with a fixed order (frame, empty exit, refusal, package lines or plain rumdl, shape lint, extension, shape audit), (c1) becomes (b) with its blocks declared as data, which is the recommended build.
- **(c2) Repository lines written into `.ki.toml`,** such as a `pre_commit_local` array. It answers HOOK-LOCAL without a second file, but puts shell into TOML strings with their quoting, splits the hook across two languages for review, and gains nothing over the extension file. Declaring inputs there, such as a shell file list, is harmless but unnecessary once detection runs on staged paths.

### 5.3 Which is mechanical, and how tools-rig fits

Only (b), and (c1) keyed on `primary_shape`, which is the same thing built from data, make conform mechanical and idempotent for the whole hook: every repository of a shape converges to one text, a repair needs no judgement after first adoption, and a second run changes nothing. (a) audits well and conforms partially. Its weaknesses are the shell tools' history: the hook drifted by additions the required-lines check could not see and conform could not undo.

How the existing repository-specific lines fit under (b):

- **tools-rig.** Its `.githooks/pre-commit` becomes the canonical package-less tools hook. `scripts/assemble-rig --check` moves to `.githooks/pre-commit.local`, a short file with its own `#!/bin/sh`, root and refusal for `bash`, that exits 0 unless `src/rig/` or `bin/rig` is staged and otherwise runs the check `|| exit 1`. Its hand-listed shell files give way to staged detection; bats leaves.
- **tools-mgit, homebrew-tap, ki-specifications, ki-principal, the package-backed repositories.** Nothing local; each hook becomes its shape's canonical text.
- **ki-agentic-harness.** Its `staged`, `matches_staged` and `quiet_audit` functions and the snapshot audit leave with HARNESS-LINES a); the quiet audit returns as the frame's helper. Nothing local.
- **The chezmoi source.** No hook. Conform writes nothing for the dotfiles shape and, finding a hook there, reports it under `GIT-2` rather than deleting it.

## 6. Change list, in dependency order

Two ordering facts drive this. The installed harness collection is a symlink to the primary harness checkout, so standards take effect on this machine the moment harness `main` moves, and on the other machine after its pull. And each shell tool's hook runs its own `ki-repo-tools` audit over the staged hook, where `SHELL-HOOK` is FAIL and today requires bats: a commit that removes bats is refused by its own gate until the reworded `SHELL-HOOK` is live. So the harness lands first and every repository follows. The chezmoi source has dropped out of the rollout: it has no `.githooks/` and no `core.hooksPath` today, so the changed `GIT-2` finds it already conforming.

### 6.1 ki-agentic-harness standards, one unit

Under GREEN-MAIN: in a linked worktree off the shared primary checkout, never in it, fast-forwarded into `main` only when `bun run test`, `bunx tsc --noEmit` and the focused audit of every touched skill pass. Local commits only; Kris pushes.

1. **ADR-KI-HARNESS-SKILLS-017**, refined in place: hook content is limited to lint, format and message checks; test suites and whole-project checks belong to the manual gate and CI; a shape may declare no hook; `HOOK-6` enforces the limit; `commit-msg` is required wherever a hook is.
2. **`ki-repo`** Commit gate text (the frame of section 2, its content rules, `HOOK-3` wherever a hook is); `HOOK-4` accepts the empty-index line before the refusal and the quiet-audit helper; `HOOK-1` to `HOOK-4` honour a shape's "no hook"; new `HOOK-6`; rubric items, contexts and tests in `scripts/rubric/{items,contexts}/hooks.ts`; regenerated `references/rubric.md`.
3. **`ki-engineering`** Common local Git hooks: the refusal covers `biome` and `rumdl`; type checking is named as not hook content; `PKG-6` rejects `bunx` in the `lint-staged` block; `SCR-11`'s message line follows MSG-UNIFY; items and tests.
4. **`ki-authoring`**: the staged-Markdown criterion for package-less hooks.
5. **`ki-git`** Commit-message binding: `ki git check-message "$1"` is the package-less line now.
6. **`ki-repo-kb` `GATE-1`**: tightened to the focused `--staged` form. **`ki-repo-dotfiles-chezmoi` `GIT-2`**: changed to require no `.githooks/` and no `core.hooksPath`, with the standard naming the AGENTS.md manual gate as the dotfiles gate. Items and tests.
7. **`ki-repo-tools` `SHELL-HOOK`**: reworded (bats out; `shellcheck`, `bash -n` and `mandoc` over staged files in; focused audit in); the capability-conditionals row and its commit-msg sentence; `shell.ts` and tests.
8. **`ki-repo-specifications`** and **`ki-repo-homebrew-tap`**: one new `GATE-1` each, standard text, items and tests.
9. **`ki-repo-harness`**: the standard names `tsc --noEmit`, the `ki-skills` audit and the receipt check as manual-gate and CI work.
10. **The harness's own hook**, a separate commit in the same worktree: empty-index exit, the focused audit through the helper, the three heavy lines and their functions removed, `biome` and `rumdl` in the refusal; the AGENTS.md sentence describing the hook rewritten for `HOOK-J1`. Then fast-forward `main`.

If STRICTNESS-CONFORM a) is taken, items 2 to 8 also declare each block as data with its worked example generated from it, and `HOOK-4` becomes the exact comparison; that is the declaration half of KI-HARNESS-GOV-225, whose planning takes this note's composition order and extension point as input.

### 6.2 Repository hooks, each its own local commit by explicit path

After 6.1 is on harness `main`. Each repository: write `.githooks/pre-commit`, add or edit `.githooks/commit-msg` at mode `100755`, make one test commit in a scratch linked worktree, then commit; Kris pushes. Under STRICTNESS-CONFORM a), each hook is copied byte-exact from its shape's generated worked example, so KI-TOOL-KI-CLI-165's composer later finds every hook already canonical and churns nothing; once the composer lands, the same step is `ki repo conform --dry-run`, then `ki repo conform`.

1. **tools-mgit**: bats out; shellcheck, `bash -n` and mandoc over staged files; `rumdl`; `commit-msg`.
2. **tools-rig**: the same; `assemble-rig --check` into `.githooks/pre-commit.local` under STRICTNESS-CONFORM a), or kept in the hook behind its staged-path condition otherwise.
3. **homebrew-tap**: the two Ruby test files out; `ruby -wc` over staged `.rb`, `rumdl` and `commit-msg`.
4. **ki-specifications**: the empty-index exit, `rumdl` and `commit-msg`.
5. **ki-principal**: the common package delta below, keeping its KB audit through the helper.
6. **The package-backed repositories without shape lines**, byte-identical today: one scripted delta per repository (empty-index exit; `biome` and `rumdl` in the refusal; `lint-staged --quiet`; `bunx` out of the `package.json` `lint-staged` block; the package message line), one commit each.
7. **ki-design**: takes the common package delta after its Husky exit (`7cb9f1d`) is pushed.
8. **Other territories' repositories** follow by shape under their own grants, as the earlier design's waves 3 and 4 set out; a repository without `.ki.toml` is left alone.
9. **Severity step**: after the last repository, raise `HOOK-1` to `HOOK-6` and the new `GATE-1` criteria to FAIL, as already planned.

## Open decision

### STRICTNESS-CONFORM - how conform keeps every hook to its shape

**Context:** Kris took STRICTNESS a) provisionally at 03:47 BST, required lines plus a forbidden list, and asked whether it helps mechanical conform. It does not, beyond adding lines: conform cannot place a missing line reliably (today's audit idiom ends the hook), cannot safely remove a forbidden multi-line block such as tools-rig's bats subshell, cannot keep the refusal list right for arbitrary lines, and leaves two repositories of one shape different. Writing each shape's hook as one canonical text, keyed on the `primary_shape` every `.ki.toml` already declares plus whether a `package.json` exists, lets conform overwrite and the audit compare bytes, with a second run changing nothing; the only judgement is at first adoption, where conform refuses and names any line that is neither canonical nor forbidden. The estate has one repository-specific check left after the decided removals, tools-rig's `assemble-rig --check`, so the extension point need hold one line. This reshapes KI-HARNESS-GOV-225's claims (one block per shape skill, fixed order) and answers KI-TOOL-KI-CLI-165's HOOK-LOCAL question; it creates no record. MSG-UNIFY drops in either way, as the package message line.

**Query:** Which strictness should the audit and conform hold every hook to?

**Options:**

a) (recommended, confidence medium - the mechanism follows the composed `.gitignore` and package-script claim precedents and fits all 22 Knowledge Islands checkouts and the chezmoi source, but the byte-exact templates and staged shell detection are not yet piloted) A canonical hook per `primary_shape` and package presence, composed from the `ki-repo` frame and the shape skill's declared block in a fixed order, written byte-exact by conform and audited exact, with one extension file, `.githooks/pre-commit.local`, run with `sh` before the shape audit and itself held to `HOOK-4` and `HOOK-6`; tools-rig's `assemble-rig --check` moves there.

b) The same canonical hook, with the extension as a marked block inside `.githooks/pre-commit` that conform preserves verbatim: one file per hook, but conform parses markers and the audit compares the hook minus its block.

c) Keep the provisional STRICTNESS a): required lines plus `HOOK-6`'s forbidden list, conform adding missing lines where it can place them and refusing forbidden ones for a person to remove.

d) A canonical hook with no extension point: tools-rig's `assemble-rig --check` leaves the hook for its manual gate and CI, and every hook of a shape is identical with no exception.
