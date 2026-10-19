# Commit-gate hooks standard

Design note for HOOKS-STANDARD (19 October 2026), the [Tools burndown](../work.md) work, routed from ki.ways-of-working on Kris's direction of 19 October: "add an urgent message to it to standardise". It sets out one commit-gate convention for the estate, the harness standard and rubric changes it needs, the `ki repo` and estate-repair changes in tools-ki, the rollout order and the gate each package-less repository should run. It is investigation only: no record, standard, hook or binding has changed.

Sources read at 18:20 to 18:50 BST on 19 October: the `ki-repo` [commit gate section](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md) and its `HOOK-1` and `HOOK-2` checker (`keystone/ki-repo/scripts/rubric/contexts/hooks.ts`); [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md); the `ki-engineering` [standard](/Users/krisbrown/.local/share/ki/harnesses/knowledgeislands/ki-agentic-harness/skills/governance/ki-engineering/references/standards-engineering.md) (`SCR-5`, `SCR-11` and the hook-stub paragraph) and `git-hooks.ts`; `ki-repo-kb` `GATE-1`, `ki-repo-dotfiles-chezmoi` `GIT-2` and `ki-repo-tools` `SHELL-HOOK`; `ki-git`'s standard; the `.githooks` and `.husky` files of ki-principal, ki-agentic-harness and ki-design; tools-ki's `src/core/repository/operations/conform.ts`, `src/core/estate/` and `src/core/manage/repair.ts`; and a local scan of the 57 Git checkouts under `~/workspaces` plus the chezmoi source.

## Short answers

- **The harness already has one convention, and it is not "Husky only".** [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md), from [KI-HARNESS-GOV-109 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/6387e0d29ff3d75cb20bcae042342df1c1752f77/docs/roadmap/KI-HARNESS-GOV-109-fail-when-commit-gates-absent.md), requires every repository to commit `.githooks/pre-commit` and bind `core.hooksPath` to `.githooks` (`HOOK-1`, `HOOK-2`, both at WARN). Husky is the `ki-engineering` content layer for Bun repositories (`SCR-11`), and `.githooks` stubs wrapping Husky are optional there. The estate drifted the other way: 25 KI repositories bind `.husky/_` and fail `HOOK-2` quietly.
- **Recommended convention: Husky for content, `.githooks` for the binding, everywhere.** Every KI repository commits `.githooks/pre-commit` (and `.githooks/commit-msg` where a message check exists) and binds `.githooks`. In a Bun repository the stub refuses when the tooling is missing, then hands over to `.husky/<hook>`, which holds all the content. In a package-less repository the stub holds the content itself. This is the ki-principal and ki-agentic-harness shape, made uniform. It is the only shape that gates a package-less repository and a linked worktree that has never run `bun install`.
- **The worktree refusal cannot move into Husky.** Husky's runtime is the untracked `.husky/_`, which `bun install` generates. A linked worktree without an install has no `.husky/_`, so a repository bound to it commits unchecked and nothing runs that could refuse. The refusal must live in a committed, bound file.
- **The knowledge-base audit moves into `.husky/pre-commit` where a package exists.** The stubs then become generated, content-free wrappers, identical across the estate apart from the tool list. `GATE-1`, `GIT-2` and `SHELL-HOOK` read the effective gate: the stub plus the Husky hook it hands to.
- **tools-ki needs three changes:** hook-file composition and writing in `ki repo conform`, the clone-local binding in `ki repo conform`, and a binding sweep across every registered clone on a machine for the estate repair. It has no hook handling today.

## 1. The estate as it stands

The scan read each checkout's `core.hooksPath`, tracked `.husky` and `.githooks` files, `package.json`, Bun lockfile and `.ki.toml` shape skills. Of 57 checkouts, 51 declare `.ki.toml`.

| Group | Count | Repositories |
| --- | --- | --- |
| Bound to `.githooks`, stubs wrapping Husky | 2 | ki-principal (stub adds the KB audit and a `ki` presence check), ki-agentic-harness (stub wraps Husky only; no KB audit) |
| Husky bound to `.husky/_`, KI | 25 | 5g-emerge-apex, 5g-emerge-demos, 5g-emerge-phase2, 5g-emerge-phase3, 5g-emerge-testbed, hnr-agentic-harness, infoschematics, apps-observatory.local, ki-techne-harness, mcp-acquire-whatsapp, mcp-git-audit, mcp-gsuite, mcp-housekeeping-chatgpt, mcp-housekeeping-claude, mcp-ki-kb-fs, mcp-ki-kb-notion-mirror, mcp-m365, tools-git-almanac, tools-ki, tools-techne, apps-midnight.ninja, apps-rig.midnight.ninja, apps-tower.midnight.ninja, apps-markhowarth.com, apps-vallearmonia.com |
| Hooks committed, unbound | 3 | ki-design (`.githooks` and `.husky`, `prepare` is plain `husky` and the binding is unset), apps-knowledgeislands.info (`.husky`, Bun), apps-yorkphotosoc.org (`.husky/pre-commit` only, npm, no Bun lockfile) |
| No gate, KI | 21 | Knowledge Bases: er-principal, hnr-principal, legal-principal, personal-principal, si-principal, tmx-principal, va-principal. Harnesses: er-, legal-, personal-, si-, tmx- and va-agentic-harness. Bash tools: tools-mgit, tools-rig. Others: the chezmoi source, homebrew-tap, ki-specifications, apps-dafacts.org, apps-kris.me.uk, personal/acquire |
| Not KI (no `.ki.toml`) | 6 | hnr-backend and hnr-frontend (npm Husky with `pre-push` and `require-tools.sh`, bound to `.husky/_`), hnr-benchmarks, hnr-shared, kw-website, paperclip (no gate) |

Two corrections to the 18:01 BST survey. Only ki-principal's stub runs the knowledge-base audit; ki-agentic-harness's stub wraps Husky and nothing else. The Husky-bound count here is 27 including the two non-KI HNR repositories, against 30 in the survey; the difference is probably checkouts on the other machine, and the rollout sweep should recount on each.

hnr-principal and legal-principal carry a `package.json` without a lockfile or `ki-engineering`, so they count as package-less.

## 2. The convention

### 2.1 Layers

1. **Binding (`ki-repo`).** `core.hooksPath` is `.githooks` in every clone of every KI repository. `HOOK-2` already checks this. In a Bun repository, `prepare` sets it: `husky && git config core.hooksPath .githooks`, which `SCR-5` already allows. This becomes the only form `SCR-5` accepts. Husky's own `prepare` step still generates `.husky/_`, but nothing binds it.
2. **Entry (`ki-repo`).** `.githooks/pre-commit`, and `.githooks/commit-msg` where the repository checks messages, are tracked, executable regular files. The template has four parts: find the root, refuse unless every required tool is present, put `node_modules/.bin` on `PATH` where a package exists, and run the content. The refusal text is the ki-principal text ("a gate that cannot run is unknown, not a pass"), with the install command a parameter (`bun install`, `npm install`, or the tool to install).
3. **Content (shape skills).** In a Bun repository the content lives only in `.husky/pre-commit` and `.husky/commit-msg`, and the stub ends `exec sh "$root/.husky/<hook>" "$@"`. In a package-less repository the content lives in the stub after the refusal. Each shape skill keeps the commands it owns: `SCR-11` for Husky, `GATE-1` for the KB audit, `GIT-2` for chezmoi, `SHELL-HOOK` for Bash tools.

### 2.2 The knowledge-base audit

ki-principal's KB audit moves from `.githooks/pre-commit` to the end of `.husky/pre-commit`, and `ki` joins the stub's required tools. Its stub then matches every other Bun repository's stub except for the tool list. A package-less Knowledge Base, which is every principal except ki-principal, keeps the audit in its stub, because it has no Husky.

`GATE-1`, `GIT-2` and `SHELL-HOOK` currently read only `.githooks/pre-commit`. They change to read the effective gate: the stub, and `.husky/pre-commit` where the stub hands over to it. The check-only rule (no `ki repo conform`, no `--fix` or `--write`) applies to both files. Without this change, moving the audit into Husky would turn `GATE-1` from PASS to FAIL in ki-principal.

### 2.3 Not chosen

- **Husky only (`core.hooksPath .husky/_` everywhere).** Every package-less repository, 21 of them, would need a `package.json`, `husky` and an install just to run `ki repo audit` or `shellcheck`. A fresh linked worktree would commit unchecked, the gap [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md) records under Consequences and the stubs were written to close. It would also reverse a current decision for no gain beyond the directory name.
- **Commit `.husky/` and bind it directly, dropping Husky's runtime.** This gives one directory name, but `bun install` would rebind `.husky/_` through `prepare`, so `husky` would have to leave every manifest and `PKG-5`. It would also put a directory called `.husky` in repositories that have no Husky.

## 3. Harness standard and rubric changes

All of these sit in ki-agentic-harness, inside ki.tools-burndown's hooks-standard scope.

| Skill | Change |
| --- | --- |
| Decision record | Refine [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md) in place: the stub template and the Husky hand-over become part of the decision, and "Adding a stub is a receiver-owned trade" gives way to the rollout authority Kris chooses (ROLLOUT-AUTHORITY). |
| `ki-repo` | The standard states the stub template and that a Bun repository's stub hands over to Husky. "`ki-repo` never writes hook" becomes: conform writes the stub from the template and sets the binding, and never writes content. `HOOK-1` adds the template's shape (refusal before content) as a check. `HOOK-2` names `.husky/_` as the common wrong value in its message (the test already covers it). Both move from WARN to FAIL at the end of the rollout. `HOOK-J1` is unchanged. |
| `ki-engineering` | `.githooks` stubs move from MAY to MUST for package-backed repositories. `SCR-5` accepts only `husky && git config core.hooksPath .githooks`, keeping the existing `tooling/boundaries` suffix. `SCR-11` keeps the Husky content and adds "content lives only in `.husky/`". The stub tool list is derived from the Husky hooks (`lint-staged`, `syncpack`, `tsc` where used, `commitlint`). |
| `ki-repo-kb` | `GATE-1` reads the effective gate; the standard names `.husky/pre-commit` as the KB audit's home where a package exists. `contributes` gains `.husky/pre-commit`. |
| `ki-repo-dotfiles-chezmoi`, `ki-repo-tools` | `GIT-2` and `SHELL-HOOK` read the effective gate. No content change. |
| `ki-repo-harness` | No content criterion exists for a harness's hook. Add one: `ki repo audit --staged` check-only, matching `GATE-1`. |
| `ki-git` | One line in the standard: a commit gate that cannot run refuses, and the remedy is the install the refusal names, never `--no-verify`. It also cites `ki-repo` for the binding. `ki-git` still installs nothing. If COMMIT-MSG a) is chosen, `ki-git` owns the vocabulary a non-Bun `commit-msg` checks. |

## 4. tools-ki changes

tools-ki has no hook handling today. `ki repo conform` runs each declared skill's conform operation and composes only `package.json` scripts through claims. `ki estate converge` moves, clones, re-remotes and relinks checkouts. `ki repair` repairs user skill links.

1. **Hook composition in `ki repo conform`.** A claims mechanism for `.githooks/pre-commit` and `.githooks/commit-msg`, on the model of the package-script claims: `ki-repo` supplies the template and each shape skill claims its content lines (package-less) or the Husky hand-over (Bun). Conform writes the file deterministically, mode `100755`, and refuses a file that has hand-written lines it cannot attribute rather than overwriting them. ki-principal's and ki-agentic-harness's current stubs should re-render byte-identical apart from the moved KB audit, which makes them the fixtures.
2. **Binding in `ki repo conform`.** Where a tracked `.githooks/pre-commit` exists and `core.hooksPath` is unset or `.husky/_`, conform sets it to `.githooks`. This is clone-local Git configuration, not a tracked change, and reverses with `git config --unset core.hooksPath`. It never overrides any other value; it reports it.
3. **Estate binding sweep.** The binding belongs to each clone, so every machine needs it after every pull that adds a stub. Add it to the estate repair: `ki estate converge` plans a `hooks-path` action for every registered clone whose tracked stub is unbound, and apply sets it, with the same preview, apply and roll-back as other converge actions. Converge already repairs worktrees, so it is the natural home; `ki repair` is about the user runtime and is not. Linked worktrees share the clone's configuration, so one action per clone is enough.
4. **Optional, under COMMIT-MSG a): `ki git check-message <file>`.** This checks a message against the `ki-git` Conventional Commit vocabulary with no Node dependency, so a package-less repository's `.githooks/commit-msg` can call it.

tools-ki is itself a Bun repository bound to `.husky/_`, so it takes its own stubs in the pilot wave. [KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md) leaves the Husky hooks alone and does not conflict.

## 5. Rollout order

1. **Standard.** Refine the decision and change the five skills in section 3, with `HOOK-1` and `HOOK-2` still at WARN. Harness tests cover the effective-gate reading and the stub template.
2. **Tool.** Ship the tools-ki changes in section 4 (one record each for composition, binding and the estate sweep, plus `check-message` if chosen). Both machines run tools from their checkouts (LOCAL-MODE, 19 October), so a pull delivers them without a release.
3. **Pilot.** Run three repositories that between them exercise every path: ki-design (stubs already present: change `prepare`, bind), ki-principal (move the KB audit into Husky, re-render the stub) and one package-less Knowledge Base, va-principal. Then tools-ki itself. Check that a commit refuses in a fresh linked worktree with no install, and passes after it.
4. **Bun wave.** The 25 Husky-bound KI repositories plus apps-knowledgeislands.info: add stubs, change `prepare`, bind. Knowledge Islands repositories go first, then Humans Not Robots, personal and Valle Armonia. This is mechanical, one commit per repository.
5. **Package-less wave.** The 20 ungated KI repositories in section 6, then apps-yorkphotosoc.org. The chezmoi source goes to ki.chezmoi as a handoff, because Rig and dotfiles are outside this work.
6. **Machines and severity.** Run the estate sweep on Terra and on Sol, re-scan both, then raise `HOOK-1` and `HOOK-2` to FAIL.

## 6. Gate content for package-less repositories

Every package-less stub refuses first when a tool it needs is absent from `PATH`. The table gives what follows the refusal. All commands are check-only.

| Repositories | Required tools | `pre-commit` content | Owning criterion |
| --- | --- | --- | --- |
| er-principal, hnr-principal, legal-principal, personal-principal, si-principal, tmx-principal, va-principal | `ki` | `ki repo audit --repo "$root" --skill ki-repo-kb --staged --concise --progress never --reporter-levels FAIL`, rerun in full on failure (the ki-principal form) | `GATE-1` |
| er-, legal-, personal-, si-, tmx- and va-agentic-harness | `ki` | `ki repo audit --repo "$root" --skill ki-repo-harness --staged`, same concise-then-full form | new `ki-repo-harness` criterion |
| tools-mgit, tools-rig | `shellcheck`, `bats` | `shellcheck` over the staged shell files, then the `bats` suite | `SHELL-HOOK` |
| chezmoi source (handoff to ki.chezmoi) | `ki` | `ki repo audit --repo "$root" --skill ki-repo-dotfiles-chezmoi --staged`, concise-then-full | `GIT-2` |
| homebrew-tap | `ki` | `ki repo audit --repo "$root" --skill ki-repo-homebrew-tap --staged`, concise-then-full | none today; `HOOK-1` only |
| ki-specifications | `ki` | `ki repo audit --repo "$root" --skill ki-repo-specifications --staged`, concise-then-full | none today; `HOOK-1` only |
| apps-dafacts.org, apps-kris.me.uk, personal/acquire | `ki` | `ki repo audit --repo "$root" --staged`, concise-then-full, over the declared skills | none today; `HOOK-1` only |
| apps-yorkphotosoc.org (npm) | `node_modules/.bin` entries its `.husky/pre-commit` uses | stub hands over to the existing `.husky/pre-commit`; install command `npm install` | `HOOK-1` only, as it does not declare `ki-engineering` |

The `bats` timing in tools-rig and tools-mgit was not measured. If either suite is slow, the pilot should say so before the package-less wave fixes `SHELL-HOOK` on every commit. `--staged` was confirmed only with `--skill ki-repo-kb`. The pilot confirms it for the other skills.

`commit-msg` for these repositories waits on COMMIT-MSG.

## 7. Decisions for Kris

### HOOKS-CONVENTION - which convention "standardise on Husky" means

**Context:** The harness standard and its current decision record already require a committed `.githooks/pre-commit` bound by `core.hooksPath .githooks` in every repository, with Husky as the content layer only where a Bun package exists. 25 repositories bind Husky's untracked `.husky/_` instead. A Husky-only binding cannot gate the 21 package-less repositories without adding a package to each, and it lets a fresh linked worktree commit unchecked.

**Query:** Should the estate converge on Husky for content behind committed `.githooks` stubs, or on Husky alone?

**Options:**

a) (recommended, confidence medium - the only shape that gates package-less repositories and fresh worktrees and keeps the current decision, but it reads "Husky" more narrowly than Kris may have meant) Husky holds the content wherever a Bun package exists; every repository commits `.githooks` stubs and binds `.githooks`.

b) Husky alone: bind `.husky/_` everywhere, add a `package.json` and `husky` to every package-less repository, accept that unbuilt worktrees commit unchecked, and supersede the current decision.

c) Commit `.husky/` and bind it directly, dropping Husky's runtime and the `husky` dependency estate-wide.

### KB-AUDIT - where the knowledge-base audit lives

**Context:** ki-principal runs the KB audit from its `.githooks/pre-commit` stub; the rubric criteria read only that file. Moving the audit into `.husky/pre-commit` makes every Bun stub a generated wrapper, but the criteria must then read the stub and the Husky hook together.

**Query:** Should the KB audit move into `.husky/pre-commit` where a package exists?

**Options:**

a) (recommended, confidence medium - one content home per repository and uniform stubs, at the cost of a small change to three checkers) Move it into `.husky/pre-commit` where a package exists, keep it in the stub where none does, and make `GATE-1`, `GIT-2` and `SHELL-HOOK` read the effective gate.

b) Keep the KB audit in the stub everywhere, so a stub may carry content even beside Husky.

### COMMIT-MSG - message checks in package-less repositories

**Context:** Commitlint needs Node and an install, so the 21 package-less repositories have no message check. A shell pattern in each stub would copy the `ki-git` vocabulary 21 times and drift from it.

**Query:** How should package-less repositories check commit messages?

**Options:**

a) (recommended, confidence medium - one source of the vocabulary and no Node dependency, but it adds a tools-ki command) Add `ki git check-message`, which `.githooks/commit-msg` calls; until it ships, these repositories have `pre-commit` only.

b) A generated shell pattern in `.githooks/commit-msg`, rendered from the `ki-git` vocabulary by conform.

c) No message check outside Bun repositories.

### ROLLOUT-AUTHORITY - who writes the stubs in other repositories

**Context:** The current decision makes adding a stub "that repository's change, raised as a receiver-owned trade", and the Charter gives territory selection no cross-repository write authority. Kris asked for the rollout to run through `ki repo` and the estate repair, which means one run writing stubs in about 47 repositories.

**Query:** Should one owner grant cover `ki repo conform` writing and committing the stubs, wave by wave, in every KI repository?

**Options:**

a) (recommended, confidence medium - it matches Kris's "through `ki repo`" and the change is mechanical, but each wave writes to repositories ki.tools-burndown does not own) One grant per wave in section 5: a run commits the conformed stubs and `prepare` change by explicit path in each listed repository, local only, and the pushes are Kris's.

b) Receiver-owned trades: ki.tools-burndown ships the standard and tool, and each repository's owning work runs `ki repo conform` itself.

### NON-KI - repositories without `.ki.toml`

**Context:** hnr-backend and hnr-frontend run their own npm Husky gates with `pre-push`; hnr-benchmarks, hnr-shared, kw-website and paperclip have none. `ki repo` does not reach a repository without `.ki.toml`.

**Query:** Are the six non-KI repositories outside this rollout?

**Options:**

a) (recommended, confidence high - `ki repo` cannot reach them, and the HNR gates are deliberate and working) Leave them out. They join only if they adopt `.ki.toml`.

b) Bring them in by declaring `.ki.toml` first.
