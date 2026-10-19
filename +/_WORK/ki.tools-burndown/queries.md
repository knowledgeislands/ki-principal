# ki.tools-burndown queries

## Open

### GIT-HOOKS - Where hooks live, and whether Husky keeps a role

**Context:** You asked whether we need Husky, what it brings, and whether hooks can live inside `.git`. Hooks in `.git/hooks` work, worktrees included, but are untracked and never cloned, so each clone on each machine must be installed by hand and drifts unreviewed. A committed `.githooks` folder reaches every clone and worktree at its revision and needs one binding per clone (`core.hooksPath`); ADR-KI-HARNESS-SKILLS-017 already requires it. Husky only sets that binding on `bun install` and runs files under `.husky`; ki-principal's and the harness's stubs already call that content directly, bypassing Husky's runner. Dropping Husky means amending ki-engineering SCR-5, SCR-11 and PKG-5 and editing the Husky repositories' `prepare` scripts, which the rollout touches anyway. KB-AUDIT then falls away and HOOKS-CONVENTION is answered by this. The blind review checked Git's behaviour in 23 scratch tests and agreed; it adds that a fresh clone still needs the binding under any option, a worktree without `.githooks` commits unchecked, and the rollout must keep both pre-commit and commit-msg and each repository's own checks.

**Query:** Should the estate keep hooks in a committed `.githooks` folder and drop Husky?

**Options:**

a) (recommended, confidence high - reviewed, Git already does what Husky adds once the stub is bound, and one hook home removes KB-AUDIT) Committed `.githooks` everywhere holding all hook content, bound by `core.hooksPath`; `prepare` becomes `git config core.hooksPath .githooks`, and `husky` and `.husky` leave every repository.

b) Committed `.githooks` stubs everywhere, with Husky kept in Bun repositories as the content behind them (HOOKS-CONVENTION a).

c) Husky alone everywhere, adding a package to each repository without one.

d) Hooks inside `.git/hooks`, installed into every clone by `ki repo conform`, with nothing tracked.

### HOOKS-CONVENTION - Which convention "standardise on Husky" means

since 2026-10-19 · from hooksstd.report.md in the run state folder · [design note](design/hooks-standard.md)

**Context:** The harness standard and [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md) already require a committed `.githooks/pre-commit` bound by `core.hooksPath .githooks` in every repository, with Husky as the content layer where a Bun package exists. 25 KI repositories bind Husky's untracked `.husky/_` instead. Husky alone cannot gate the 21 package-less repositories without adding a package to each, and lets a fresh linked worktree with no install commit unchecked.

**Query:** Should the estate converge on Husky for content behind committed `.githooks` stubs, or on Husky alone?

**Options:**

a) (recommended, confidence high - reviewed, the only shape that gates package-less repositories and fresh worktrees, and it keeps the current decision, but it reads "Husky" more narrowly than you may have meant) Husky holds the content wherever a Bun package exists; every repository commits `.githooks` stubs and binds `.githooks`.

b) Husky alone: bind `.husky/_` everywhere and add a `package.json` and `husky` to every package-less repository; unbuilt worktrees commit unchecked and the decision is superseded.

c) Commit `.husky/` and bind it directly, dropping Husky's runtime and dependency across the estate.

### KB-AUDIT - Where the knowledge-base audit lives

since 2026-10-19 · from hooksstd.report.md in the run state folder

**Context:** ki-principal runs the KB audit from its `.githooks/pre-commit` stub, and the rubric criteria read only that file. Moving it into `.husky/pre-commit` makes every Bun stub a generated wrapper, and `GATE-1`, `GIT-2` and `SHELL-HOOK` would read the stub and the Husky hook together.

**Query:** Should the KB audit move into `.husky/pre-commit` where a package exists?

**Options:**

a) (recommended, confidence high - reviewed, one content home per repository and uniform stubs, at the cost of a small change to three checkers) Move it into `.husky/pre-commit` where a package exists, keep it in the stub where none does, and have the three criteria read the effective gate.

b) Keep the KB audit in the stub everywhere.

### COMMIT-MSG - Message checks in package-less repositories

since 2026-10-19 · from hooksstd.report.md in the run state folder

**Context:** Commitlint needs Node and an install, so the 21 package-less repositories have no message check. A shell pattern in each stub would copy the `ki-git` vocabulary 21 times and drift.

**Query:** How should package-less repositories check commit messages?

**Options:**

a) (recommended, confidence high - reviewed, one source for the vocabulary and no Node dependency, though it adds a tools-ki command) Add `ki git check-message` for `.githooks/commit-msg` to call; until it ships, those repositories have `pre-commit` only.

b) A shell pattern in `.githooks/commit-msg`, generated from the `ki-git` vocabulary by conform.

c) No message check outside Bun repositories.

### ROLLOUT-AUTHORITY - Who writes the stubs in other repositories

since 2026-10-19 · from hooksstd.report.md in the run state folder

**Context:** The current decision makes adding a stub "that repository's change, raised as a receiver-owned trade", and the Charter gives territory selection no cross-repository write authority. Rolling out through `ki repo` and the estate repair means runs writing stubs in about 47 repositories. The blind review prefers b): ADR-KI-HARNESS-SKILLS-017 explicitly requires receiver-owned trades and the Charter denies inferred cross-repository authority, though an explicit bounded wave grant could authorise a different arrangement.

**Query:** Should one owner grant per wave cover `ki repo conform` writing and committing the stubs in every listed KI repository?

**Options:**

a) (recommended, confidence medium - review disagrees, it matches "through `ki repo`" and the change is mechanical, but each wave writes to repositories this work does not own) One grant per wave; a run commits the stubs and the `prepare` change by explicit path in each listed repository, local only, and you push.

b) Receiver-owned trades: this work ships the standard and the tool, and each repository's owning work runs `ki repo conform` itself.

### ROUTING-VIEW - Routing view for State of play in `ki work status`

**Context:** The wpreader run delivered KI-TOOL-KI-CLI-158, which reads work packages and emits each work's id, state, pending-message count and description in JSON, but explicitly leaves out the human routing view State of play would read. The run recommended capturing that view only when State of play asks for it. The blind review (qreview3, 21:32 BST) prefers b): the finalised work-package design in ki.ways-of-working, point 35, already asks for exactly this register, and the JSON now carries its data. Capture does not delay the v0.11.5 release; tools-ki keeps its priority.

**Query:** Shall I capture a tools-ki triage record for the routing view now?

**Options:**

a) (recommended, confidence medium - review prefers it and I now agree, the agreed design already asks for it, the reader's own pick was to wait) Capture it now, planned straight after KI-TOOL-KI-CLI-158.

b) Capture it only when State of play asks for the view.

c) Leave it out.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
