# GIT-HOOKS options

Options note for GIT-HOOKS (19 October 2026), the [Tools burndown](../work.md) work. It sets out the choices only; the answer and recommendation are in [git-hooks.md](git-hooks.md). It feeds HOOKS-CONVENTION, KB-AUDIT, COMMIT-MSG and ROLLOUT-AUTHORITY in [hooks-standard.md](hooks-standard.md).

## Context

Kris asked at 21:34 BST: "Do we need to use Husky? What advantage does that bring? Can we just put the git hooks inside the .git folder? Or is it better to have it outside of the .git folder?"

How Git finds a hook, checked against Git and a scratch repository on 19 October:

- Without configuration, Git runs hooks from `.git/hooks/`. That directory is never tracked, so nothing there is reviewed, versioned or shared. `git clone` does not copy it: a fresh clone has only Git's `.sample` files, so every clone on every machine must be installed separately, and a hook edited in one clone drifts from the rest.
- Linked worktrees share the main clone's common directory, so one `.git/hooks/` (or one `core.hooksPath` setting) serves the clone and all its worktrees.
- `core.hooksPath` points Git at another directory. A relative value resolves from the root of whichever working tree is committing, so `.githooks` means the tracked `.githooks/` at the revision checked out there. The setting itself is clone-local configuration: it is not cloned either, so something must set it once per clone. A worktree checked out at a revision without `.githooks/` commits unchecked.
- Husky 9.1.7, the version in the estate, is about 30 lines. Its `prepare` step, run by `bun install`, does three things: sets `core.hooksPath` to `.husky/_`, writes the untracked `.husky/_/` with one two-line shim per hook and a git-ignore of `*`, and copies its runner `h`. At commit time the shim calls `h`, which runs the tracked `.husky/<hook>` with `sh -e` after putting `node_modules/.bin` on `PATH`, honours `HUSKY=0` to skip, and exits quietly if that hook file is absent.

What that means in practice: Husky's one real service is setting the binding automatically when someone installs, which matters for repositories outside contributors clone. Its runtime lives in an untracked, install-generated directory, so a clone or linked worktree that has not run `bun install` has no hook and commits unchecked. It needs a `package.json`, which 21 of the estate's KI repositories do not have.

The estate today (scan in [hooks-standard.md](hooks-standard.md), section 1): 25 KI repositories bind `.husky/_`; ki-principal and ki-agentic-harness bind a committed `.githooks/` whose stub refuses when tooling is missing and then runs `sh .husky/pre-commit` directly, bypassing Husky's runtime; 3 commit hooks but bind nothing; 21 have no gate. No repository installs into `.git/hooks/`. [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md) requires a tracked `.githooks/pre-commit` bound by `core.hooksPath .githooks` in every repository (`HOOK-1`, `HOOK-2`), and `ki-engineering` `SCR-11` and `PKG-5` require Husky, its `devDependency` and `.husky/` hook content in every Bun repository. All the options below are local hooks, bypassable with `--no-verify`; CI remains the authoritative gate in each.

## Query

Where should the estate's commit hooks live, and does Husky keep a role?

## Options

a) Hooks tracked outside `.git`, with Husky kept for content: every KI repository commits `.githooks/` and binds `core.hooksPath .githooks`; in a Bun repository the stub refuses when tooling is missing and hands over to `.husky/<hook>`, and `prepare` is `husky && git config core.hooksPath .githooks`. This is the current decision and HOOKS-CONVENTION a); `SCR-11`, `PKG-5` and the `husky` dependency stay.

b) Hooks tracked outside `.git`, without Husky: every KI repository commits `.githooks/` holding the whole hook (refusal, `node_modules/.bin` on `PATH`, content) and binds `core.hooksPath .githooks`; in a Bun repository `prepare` becomes `git config core.hooksPath .githooks`, and `husky` and `.husky/` leave every repository. `SCR-11` moves its content checks to `.githooks/`, `PKG-5` drops `husky`, the current decision is refined rather than reversed, and KB-AUDIT falls away because content has one home everywhere.

c) Husky alone: bind `.husky/_` everywhere, add a `package.json` and `husky` to each of the 21 package-less repositories, accept that an uninstalled clone or worktree commits unchecked, and supersede the current decision. This is HOOKS-CONVENTION b).

d) Hooks inside `.git`: `ki repo conform` and the estate sweep write each repository's hooks into `.git/hooks/` of every clone on every machine, with nothing tracked and `core.hooksPath` unset. The hook text lives in the harness or tools-ki rather than the repository, and `HOOK-1`, `HOOK-2` and the current decision are replaced.
