# Commit-gate hooks standard

Design note for HOOKS-STANDARD, the [Tools burndown](../work.md) work, rewritten on 19 October 2026 for the shape Kris decided that evening: GIT-HOOKS a), COMMIT-MSG a), ROLLOUT-AUTHORITY a), HOOK-AUDIT and NON-KI a), all in the [decisions log](../decisions.md). It sets out the convention, the mechanical audit checks, the exact harness and tools-ki changes, and the rollout waves. It folds in the former `git-hooks.md` answer and its options note, both deleted here with Git holding them, and the caveats of the blind ghreview run. No standard, hook, binding or other repository changed with this note; the records it led to are listed in section 4.2.

Sources: the `ki-repo` [commit gate section](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md) and its `HOOK-1`, `HOOK-2` checker; [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md); the `ki-engineering` [standard](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/governance/ki-engineering/references/standards-engineering.md), "Common local Git hooks", with `PKG-5`, `PKG-6`, `SCR-5` and `SCR-11`; `ki-repo-kb` `GATE-1`, `ki-repo-dotfiles-chezmoi` `GIT-2` and `ki-repo-tools` `SHELL-HOOK`; `ki-git`'s standard, "Package-backed commit-message binding"; ki-principal's `.githooks/` and `.husky/`; tools-ki's `src/`, which has no hook handling; a local scan of 57 checkouts on 19 October; and the ghreview run's 23 scratch-repository assertions under Git 2.56.0 and Husky 9.1.7.

## Short answers

- **One home for hooks: a committed `.githooks/`, in every KI repository.** It holds `pre-commit` and `commit-msg`, each the whole hook: refusal when a tool is missing, `node_modules/.bin` on `PATH` where a package exists, then the content. `core.hooksPath .githooks` binds it in every clone.
- **Husky leaves.** Once a committed hook is bound, Husky does nothing a one-line `prepare` does not: `prepare` becomes `git config core.hooksPath .githooks`, with the boundary-install suffix kept where it exists. `husky` leaves every manifest and `PKG-5`, and `.husky/` leaves every repository.
- **The knowledge-base audit stays in `.githooks/pre-commit`,** where `GATE-1` already reads it. KB-AUDIT falls away, and so does the "effective gate" reading the first design needed.
- **Package-less repositories get `commit-msg` when `ki git check-message` ships** ([KI-TOOL-KI-CLI-161](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-161-git-check-message.md)); until then they run `pre-commit` only. Bun repositories keep Commitlint, now called from `.githooks/commit-msg`.
- **`ki repo audit` checks it mechanically** (section 3), at WARN through the rollout and FAIL after the last wave.
- **Rollout runs in waves, each under one owner grant,** committing by explicit path locally; Kris pushes. Only repositories with `.ki.toml` take part.

## 1. Why outside `.git`, and why not Husky

Git runs hooks from `.git/hooks/` by default, but that directory is never tracked, so nothing there is reviewed or versioned, `git clone` does not copy it, and every clone on both machines would need installing and keeping in step. A tracked `.githooks/` puts the hook in the repository: it is reviewed with the code, every clone and worktree runs the hook at the revision it has checked out, and a change reaches the other machine with an ordinary pull. The one per-clone step left is the binding.

Husky 9.1.7 is about 30 lines. Its one real service is setting the binding automatically on `bun install`. Its runtime is the untracked, install-generated `.husky/_`, so an uninstalled clone or worktree commits unchecked, and its lifecycle wants a `package.json`, which about 21 KI repositories lack. ki-principal and ki-agentic-harness already bypass Husky's runner by calling `sh .husky/pre-commit` from a committed stub, and their `prepare` overrides Husky's binding immediately after setting it. Dropping Husky removes a second hook directory, generated files and a binding that installation overwrites.

## 2. The convention

### 2.1 Binding

`core.hooksPath` is the relative `.githooks` in every clone of every KI repository. A relative value resolves from the root of the working tree that is committing, so one setting serves the clone and all its linked worktrees.

- **Bun repositories:** `prepare` is `git config core.hooksPath .githooks`, followed by `&& bun install --frozen-lockfile --cwd tooling/boundaries` where that install root exists. `bun install` then binds a fresh clone.
- **Package-less repositories:** `ki repo conform` sets the binding, and the estate sweep sets it in every registered clone (section 5).

### 2.2 Hook files

`.githooks/pre-commit` and `.githooks/commit-msg` are tracked regular files with mode `100755`; Git ignores a non-executable hook. Each follows one template:

1. `#!/bin/sh`, then `root="$(git rev-parse --show-toplevel)" || exit 1`.
2. Refuse unless every required tool is present: `node_modules/.bin/<tool>` in a Bun repository, `command -v <tool>` otherwise. The refusal names the missing tools and the install step, and ends with ki-principal's line: "do not bypass with --no-verify; a gate that cannot run is unknown, not a pass."
3. In a Bun repository, put `$root/node_modules/.bin` on `PATH`.
4. The content, each command ending `|| exit 1` so failure propagates, with `"$@"` forwarded where a hook takes arguments.

Content by shape, each owned by the criterion named:

| Shape | `pre-commit` content | `commit-msg` content | Owner |
| --- | --- | --- | --- |
| Bun (`ki-engineering`) | `lint-staged` (or `lint-staged --quiet`), then `syncpack format --check`, then any repository-specific fast checks | `commitlint --edit "$1"`; may switch to `ki git check-message "$1"` once [KI-TOOL-KI-CLI-161](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-161-git-check-message.md) ships | `SCR-11` |
| Knowledge Base (`ki-repo-kb`) | adds `ki repo audit --repo "$root" --skill ki-repo-kb --staged`, concise then full on failure, as ki-principal runs it today | as its package shape, or `ki git check-message "$1"` | `GATE-1` |
| Harness (`ki-repo-harness`) | adds `ki repo audit --repo "$root" --skill ki-repo-harness --staged`, concise then full | as above | new criterion, section 4 |
| Bash tool (`ki-repo-tools`) | `shellcheck` over staged shell files, then `bats` | `ki git check-message "$1"` | `SHELL-HOOK` |
| chezmoi source | `ki repo audit --skill ki-repo-dotfiles-chezmoi --staged`, concise then full | as above | `GIT-2` |
| Others with `.ki.toml` (homebrew-tap, ki-specifications, apps without a package) | `ki repo audit --repo "$root" --staged` over the declared skills | as above | `HOOK-1` only |

A repository with both a package and a KB, such as ki-principal, keeps the Bun lines first and the KB audit after them, in the one file. Every command is check-only: no `ki repo conform`, `--fix` or `--write`.

### 2.3 Caveats carried from the ghreview run

- A fresh clone has no binding under any option: the binding is clone-local configuration, which `git clone` does not copy. `prepare`, conform and the sweep exist for this.
- A worktree checked out at a revision without `.githooks/` commits unchecked despite the inherited binding. This shrinks as the rollout lands and is not otherwise fixable locally.
- `extensions.worktreeConfig` lets a worktree override `core.hooksPath`, so linked worktrees share the binding only by default. `HOOK-2` must read the effective value from the working tree it audits.
- Working-tree-root resolution holds for ordinary commit hooks in non-bare repositories; bare repositories and receive-side hooks are out of scope.
- Husky's installer runs without a manifest when called directly; "needs a `package.json`" is a property of its package lifecycle, not of Git. This does not change the decision.
- Migration must keep each repository's own checks after the common prefix, argument forwarding, the tool refusal and failure propagation, and the boundary-install suffix in `prepare`.
- Local hooks are bypassable with `--no-verify`; CI and the repository audit remain the authoritative gate. Hosted checks and branch protection were not inspected, so mandatory CI enforcement is unverified.
- Counts differ by machine: ghreview's directory saw 21 checkouts with `.ki.toml` (13 bound to `.husky/_`, two to `.githooks`, six unset) against this note's 51 of 57. Each wave recounts on the machine it runs on.

## 3. Mechanical audit checks (HOOK-AUDIT)

What `ki repo audit` verifies once the standard lands. All start at WARN and move to FAIL after the last wave. Checks that read clone-local state are not applicable in CI, as `HOOK-2` is today.

| Check | Verifies | Criterion | Local only |
| --- | --- | --- | --- |
| Committed `pre-commit` | `.githooks/pre-commit` tracked, regular file, mode `100755` | `HOOK-1` (exists) | no |
| Committed `commit-msg` | `.githooks/commit-msg` tracked, regular file, mode `100755`; required now in a package-backed repository, and in a package-less one once `ki git check-message` ships, until then not applicable there | `HOOK-3` (new, `ki-repo`) | no |
| Bound to `.githooks` | the effective `core.hooksPath`, read with `git config --get core.hooksPath` from the audited working tree so a worktree override shows, equals `.githooks`; the message names `.husky/_` as the common wrong value and gives the exact command | `HOOK-2` (exists, message sharpened) | yes |
| Refusal before content | each hook starts `#!/bin/sh` and refuses on a missing tool before its first content command; it never suggests `--no-verify` | `HOOK-4` (new, `ki-repo`) | no |
| No Husky | no tracked `.husky/` path; no `husky` in `dependencies` or `devDependencies`; `prepare` does not call `husky`; no hook references `.husky/`; locally, no leftover untracked `.husky/_` | `HOOK-5` (new, `ki-repo`), with `PKG-5` and `SCR-5` | the `.husky/_` part only |
| Bun content | `.githooks/pre-commit` runs `lint-staged` then `syncpack format --check`; `.githooks/commit-msg` runs `commitlint --edit "$1"` or `ki git check-message "$1"` | `SCR-11` (moved from `.husky/`) | no |
| KB audit in `pre-commit` | where `ki-repo-kb` is declared, `.githooks/pre-commit` runs the check-only `ki repo audit --skill ki-repo-kb --staged` | `GATE-1` (exists, unchanged) | no |
| Shape content | `GIT-2`, `SHELL-HOOK` and the new harness criterion each find their check-only command in `.githooks/pre-commit` | existing, plus one new | no |

## 4. Exact changes

### 4.1 ki-agentic-harness

Not edited by this run: another session holds uncommitted changes there (`ki-repo-kb` link and KB context scripts). The changes do not overlap those files but should land in a separate unit once that session commits.

| Where | Change |
| --- | --- |
| [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md) | Refine in place: `.githooks/` holds all hook content, `pre-commit` and `commit-msg` both; Husky is retired; "adding a stub is a receiver-owned trade" gives way to ROLLOUT-AUTHORITY a), one owner grant per wave. Existence and binding stay with `ki-repo`, content with shape skills. |
| `ki-repo` standard, "Commit gate" | "should commit `.githooks/pre-commit`" becomes "commits `.githooks/pre-commit` and `.githooks/commit-msg`"; add the template of section 2.2; conform writes the template frame and the binding, and shape skills supply content. |
| `ki-repo` rubric and `scripts/rubric/{contexts,items}/hooks.ts` | `HOOK-2` reads the effective value per working tree and names `.husky/_`; add `HOOK-3` (commit-msg), `HOOK-4` (refusal before content), `HOOK-5` (no Husky); the WARN-to-FAIL step at rollout end. `HOOK-J1` unchanged. |
| `ki-engineering` standard, "Common local Git hooks" | Rewrite: hooks live in `.githooks/`; drop the MAY-stub paragraph, since the stub is now the hook; `.husky/pre-commit` and `.husky/commit-msg` prefixes become `.githooks/` prefixes called without `bunx`, with `node_modules/.bin` on `PATH`; remove `husky` from the toolchain list. |
| `PKG-5` | Drop `husky` from the required devDependencies; a declared `husky` fails, through `HOOK-5`. |
| `PKG-6` | Reword "the husky pre-commit fan-out" to "the pre-commit fan-out"; the check is unchanged. |
| `SCR-5` | Accept only `git config core.hooksPath .githooks`, plus the boundary-install suffix; reject any `husky` call. CONFORM rewrites the two current forms. |
| `SCR-11` | Read `.githooks/pre-commit` and `.githooks/commit-msg` instead of `.husky/`; accept `ki git check-message "$1"` beside `commitlint`. CONFORM repairs the prefixes in `.githooks/` and refuses a symlink or unsafe file, as now. |
| `ki-engineering` scripts | `contexts/git-hooks.ts`, `contexts/engineering.ts`, `contexts/audit-evidence.ts` (toolchain list and the `.husky` writer), `items/scripts.ts`, `items/package.ts` and their tests follow the four criteria above. The "Binding these hooks for the first time" paragraph drops Husky and keeps the Syncpack, install and Knip sequence. |
| `ki-engineering` `SKILL.md`, `exemplars.md` | Exemplar `"prepare": "husky"` becomes `"prepare": "git config core.hooksPath .githooks"`; `contributes` swaps `.husky/*` for `.githooks/*` where listed. |
| `ki-git` standard, "Package-backed commit-message binding", and `SKILL.md` | Rename to "Commit-message binding": every KI repository binds the deterministic rules through `.githooks/commit-msg`, by Commitlint where a package exists or `ki git check-message`; `ki-git` stays the sole owner of the vocabulary and the command reads it from there. Add one line: a gate that cannot run refuses, and the remedy is the install it names, never `--no-verify`. Drop "Husky can be bypassed" for "a local hook can be bypassed". |
| `ki-repo-kb` `GATE-1` | No change to the check. Standard text drops any Husky mention; `contributes` already names `.githooks/pre-commit`. |
| `ki-repo-dotfiles-chezmoi` `GIT-2`, `ki-repo-tools` `SHELL-HOOK` | No change to the checks; they already read `.githooks/pre-commit`. `SHELL-HOOK`'s standard gains the `commit-msg` line once KI-TOOL-KI-CLI-161 ships. |
| `ki-repo-harness` | Add a content criterion: `.githooks/pre-commit` runs `ki repo audit --skill ki-repo-harness --staged`, check-only, not applicable without a hook, matching `GATE-1`. |

Refinement, SCR5-CONFORM a), 19 October: `SCR-5` CONFORM keeps Husky's `prepare` until both committed hooks exist, rather than rewriting it unconditionally as the `SCR-5` row says, so conform never points Git at a `.githooks/` with no gate in it. The audit warns on `SCR-5` throughout, so the gap stays visible. The shape-skill claim declarations behind the "shape skills supply content" line are captured as [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md).

### 4.2 tools-ki

| Change | Status |
| --- | --- |
| `ki git check-message <file>`: the deterministic `ki-git` rules with no Node dependency, for `.githooks/commit-msg` | Captured at triage, [KI-TOOL-KI-CLI-161](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-161-git-check-message.md) |
| Hook composition in `ki repo conform`: a claims mechanism for `.githooks/pre-commit` and `.githooks/commit-msg` on the model of the package-script claims; `ki-repo` supplies the frame, each shape skill claims its content lines; written deterministically at mode `100755`; refuses a file with lines it cannot attribute rather than overwrite them. ki-principal's hooks, with the Husky hand-over inlined, are the fixture | Captured at triage under HOOK-CAPTURE a), [KI-TOOL-KI-CLI-165](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md), with the claim declarations in [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) |
| Binding in `ki repo conform`: where a tracked `.githooks/pre-commit` exists and `core.hooksPath` is unset or `.husky/_`, set `.githooks` and remove a leftover untracked `.husky/_`; report any other value without changing it. Reversible with `git config --unset core.hooksPath` | Done in [KI-TOOL-KI-CLI-163](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-163-githooks-conversion.md) |
| Estate binding sweep: `ki estate converge` plans a `hooks-path` action for every registered clone whose tracked hook is unbound, with its usual preview, apply and roll-back; one action per clone covers its worktrees | Captured at triage under HOOK-CAPTURE a), [KI-TOOL-KI-CLI-164](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-164-estate-hook-binding-sweep.md) |
| Audit plumbing: `HOOK-2` and `HOOK-5` need the effective `core.hooksPath` and the untracked `.husky/_` state of the audited working tree; confirm the rubric context supplies both, or extend it | To check during planning |

tools-ki itself is a Bun repository bound to `.husky/_` and takes its own conversion in the first wave. [KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md) runs the local gate in CI; its plan should read the gate from `.githooks/` once that lands.

## 5. Rollout

Order, each step a unit of its own:

1. **Standard.** The harness changes in 4.1, with the new checks at WARN, once the other harness session's changes are committed.
2. **Tool.** The tools-ki composition, binding and sweep; `check-message` when ready. Both machines run tools from their checkouts, so a pull delivers them without a release.
3. **Waves.** Each wave is one owner grant naming its repositories. Per repository, one commit by explicit path, local only: write `.githooks/pre-commit` and `.githooks/commit-msg` (Husky content inlined, repository-specific lines kept), change `prepare`, remove `husky` from `package.json` and the lockfile, delete `.husky/`, rebind the clone, then prove a commit refuses in a fresh linked worktree with no install and passes after `bun install`. `prepare` and the `husky` removal go in the same commit as the hooks, or a later `bun install` rebinds to `.husky/_`. Kris pushes.
4. **Machines and severity.** After the last wave, run the estate sweep on Terra and on Sol, re-scan both, then raise the hook checks to FAIL.

Only repositories with `.ki.toml` take part (NON-KI a)); hnr-backend, hnr-frontend, hnr-benchmarks, hnr-shared, kw-website and paperclip stay out unless they adopt it. The chezmoi source goes to ki.chezmoi as a handoff rather than a wave entry.

### Proposed waves

| Wave | Repositories | Why together |
| --- | --- | --- |
| 1, pilot | ki-principal (Bun with KB audit), tools-ki (Bun tool, the hooks' own author), va-principal (package-less KB, `pre-commit` only) | Exercises every path once; ki-principal and tools-ki become the fixtures |
| 2, Knowledge Islands Bun | ki-agentic-harness, ki-design, ki-techne-harness, tools-techne, tools-git-almanac, apps-knowledgeislands.info, apps-observatory.local, the eight `mcp-*` repositories | The territory's own package-backed repositories |
| 3, other Bun | hnr-agentic-harness, infoschematics, the five `5g-emerge-*` repositories, apps-midnight.ninja, apps-rig.midnight.ninja, apps-tower.midnight.ninja, apps-markhowarth.com, apps-vallearmonia.com, apps-yorkphotosoc.org (npm) | Mechanical repeat of wave 2 in other groups |
| 4, package-less | the six other principals, the six other agentic harnesses, tools-mgit, tools-rig, homebrew-tap, ki-specifications, apps-dafacts.org, apps-kris.me.uk, personal/acquire | `pre-commit` only; `bats` timing in tools-mgit and tools-rig measured first |
| 5, messages | `commit-msg` in every wave-4 repository, then the sweep and FAIL step | Waits on KI-TOOL-KI-CLI-161 |
