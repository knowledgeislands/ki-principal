# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › work-package-standard

**🤖 → 👤 Handoff to supervisor · Run report at 14:40 BST · last mark 13:37 BST**

---

## Done

- ki-principal `fba56feb`: [the work-package design note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/work-package.md) is finalised to the decided model.
- ki-agentic-harness `9e174750`: renamed `ki-work-folder` to [`ki-work-package`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/SKILL.md) and kept a thin deprecated [`ki-work-folder` alias](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-folder/SKILL.md). Its audit warns and names the replacement declaration.
- In the same commit: the standard, rubric, checks and templates now define the five-file package. Readers and checks accept both shapes, and the single-file shape gets a warning.
- In the same commit: the [ki-coordination standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md) now covers:
  - the `messages.md` queue with the important flag;
  - route receipt;
  - the inbox check at each wake;
  - refresh through `method_read`;
  - pick-up reads;
  - the turn budget;
  - state history;
  - State of play's stewardship;
  - a warning when more than eight queries are open.
- In the same commit: the generated output style and hook, the catalogue, the README and every live pointer follow the new name. Historical text keeps the old name.
- ki-agentic-harness `4434afaf`: the skill-map and coordination-area diagrams are rebuilt against `9e174750`.
- `bun run test`: pass, 1287 tests.
- `bunx tsc --noEmit`: pass.
- The pre-commit hook passed on both commits.
- Audits `ki-skills`, `ki-work-package`, `ki-coordination` and `ki-delegation`: pass.
- `ki repo audit --skill ki-repo`: fails, but not because of this change. FILES-10 reports that `[skills.ki-acquire]` follows `[skills.ki-trades]` in `.ki.toml`, and that ordering came in with another session's `8bc9d49d`.
- `ki repo audit --skill ki-diagrams`: 10 DIAG-4 warnings, on the nine other area diagrams and `thread-model`. Regenerating them changes only their revision pin, so I left them for their owner.
- `ki-recap` and `ki-work-folder` audits: unknown, because neither skill is declared in the harness. The alias's unit tests cover its check.
- Push: not pushed. `origin/main..main` also holds `8bc9d49d` and `88cce3e5`, both from another session.
- Net records: ki-principal 0, ki-agentic-harness 0.

## In Progress

Nothing is running.

Outstanding - no action requested now

**tools-ki changes needed so readers accept both shapes:**

- `src/core/work/status.ts` (`ki work status`):
  - read the state from `state.md` where it exists, over `work.md`'s front matter, keeping `id` from `work.md`;
  - keep the `ki/work-status/v1` schema, and give `path` as `state.md` for a package;
  - add the fields `description`, `method_read` and the count of pending lines in `messages.md`;
  - add a routing view with the age of the oldest unread line.
- `src/core/agent/thread.ts`: it still keys on `work.md`, which a package keeps, so it works as it is. It should also write route receipt into `messages.md`.
- `src/core/configuration/resolution.ts`: a native alias resolving `ki-work-folder` to `ki-work-package`.
- `man/ki.1`, `man/ki.commands.json` and the help text: rename the skill.
- [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) and [KI-TOOL-KI-CLI-152](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-152-work-folder-housekeeping-commands.md): their links to `ki-work-folder/references/standards-work-folder.md` now break, and should point to `ki-work-package/references/standards-work-package.md`.

**Observatory changes needed:**

- `packages/evidence/src/work.ts`: follow the new `ki work status` output.
- `review.ts`: date a package by the modification time of its `state.md`.
- The with-you link: follow the `path` field.
- `packages/evidence/src/feedback.ts`: its comment names the work-folder standard; rename it.

**What the reinstall must check:**

- Only the alias payload is installed for `ki-work-folder`, with no stale full copy.
- `ki repair` is clean.
- `chezmoi diff` has been reviewed.
- The regenerated `ki-coordinator` output style and `coordinator-reminder.sh` hook are installed.
- ki-principal and the eight principals resolve under `ki repo audit`.
- A scratch check of the readers passes on both a single-file folder and a five-file package.

**Other sessions' uncommitted work.** ki-principal has 20 uncommitted paths from other sessions, which I did not touch. Among them are `+/_WORK/ki.ways-of-working/decisions.md` and the untracked `+/_WORK/ki.ways-of-working/design/spec-areas.md`.

## Queries

### ALIAS-LIMIT - The old declaration gets no package checks

**Context:** A repository that still declares `[skills.ki-work-folder]` resolves through the alias but runs only its deprecation warning. The `ki-work-package` checks run only where `[skills.ki-work-package]` is declared, because the host resolves each skill by its own name.

**Query:** Should the enact run switch every declaration now, or should tools-ki map the alias onto the full checks?

**Options:**
a) (recommended, confidence high - a one-line `.ki.toml` change per repository, already made in the harness) Switch the declarations in ki-principal and the eight principals during the enact run, and remove the alias once none is left.
b) Add a native alias in tools-ki that runs the `ki-work-package` checks under the old name, and switch the declarations later.

### HARNESS-PUSH - Another session's commits sit under this run's commits

**Context:** Local `main` in ki-agentic-harness is four commits ahead of `origin/main`. Two are this run's, `9e174750` and `4434afaf`. Two come from another session: `8bc9d49d` (shared acquisition contract) and `88cce3e5` (acquire diagrams). Under the push rule I did not push. Tests and typecheck pass on the combined result; the only failing check is FILES-10, which `8bc9d49d` introduced.

**Query:** Will you push all four commits, or hold until the acquire session pushes its own?

**Options:**
a) (recommended, confidence medium - the combined tree tests clean, but I have not reviewed the acquire commits themselves) Push all four after a look at the acquire commits, and ask the acquire session to fix the FILES-10 table order.
b) Hold until the acquire session pushes its commits, then push this run's two.

### 🤖 → 👤 Handoff to supervisor · since 14:40 BST

👤 2 with you · 🤖 0 running

- [with you] ALIAS-LIMIT · owner · since 14:40
- [with you] HARNESS-PUSH · owner · since 14:40
- [committed] ki-principal `fba56feb`; ki-agentic-harness `9e174750`, `4434afaf`
- [unpushed] ki-agentic-harness, four commits
