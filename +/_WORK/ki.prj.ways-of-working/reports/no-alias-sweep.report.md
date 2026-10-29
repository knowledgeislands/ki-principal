# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › no-alias-sweep

**🤖 → 👤 Handoff to supervisor · Run report at 14:48 BST · last mark 13:37 BST**

---

## Done

- ki-agentic-harness `3d50e252`: the `ki-work-folder` alias is gone, under NO-ALIAS. This removed:
  - the alias skill;
  - `ki-repo`'s reading of the old declaration and the old `coverage-work-folder` key, with its test;
  - the tolerance-window wording in the [work-package standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md), the [ki-work-package skill](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/SKILL.md) and the `ki-repo` configuration standard;
  - the old name from the harness skill-area grouping and from a checkpoint template string.
- In the same commit:
  - `ki-work-package` is a required dependency of [ki-coordination](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/SKILL.md) again, as `ki-work-folder` was before the rename.
  - A NO-ALIAS entry is added to the ki-work-package sources.
  - The capability catalogue, the README counts and the diagram sources are republished.
  - The test's remediation-inventory counts drop by the alias's two criteria.
  - The open records [KI-HARNESS-GOV-219 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-219-feedback-work-folder-kind.md) and [KI-HARNESS-GOV-200 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) now name `ki-work-package`, and GOV-219's broken standard link is fixed.
  - Historical text keeps the old name: the changelog, the ADR, sources provenance, and the completed items and evidence in [KI-HARNESS-GOV-199 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md).
- ki-agentic-harness `9c9ae922`: the skill-map and coordination-area diagrams are rebuilt without `ki-work-folder`, and their last check is pinned at `3d50e252`.
- `ki dev skill generate ki-coordination`: in sync, with no changes.
- `bun run test`: pass, 1284 tests.
- `bunx tsc --noEmit`: pass.
- The pre-commit hook passed on both commits.
- Audits `ki-skills`, `ki-work-package`, `ki-coordination`, `ki-repo-harness` and `ki-work-roadmap`: pass, with warnings only.
- `ki repo audit --skill ki-repo`: fails, but not because of this change. FILES-10 reports the `.ki.toml` table order that `8bc9d49d` introduced.
- `ki repo audit --skill ki-diagrams`: the same 10 DIAG-4 warnings as before, on the nine other area diagrams and `thread-model`. I left them for their owner.
- The `.ki.toml` sweep found nothing to switch. No Knowledge Islands repository under `knowledge-islands/` declares `[skills.ki-work-folder]` or a `coverage-work-folder` key. The only declarations are ki-principal's and the harness's, and both already name `ki-work-package`.
- Not pushed. Of the six commits in `origin/main..main`, only two are mine; see HARNESS-PUSH below.
- Net records: 0 in ki-agentic-harness, 0 in every other repository.

## In Progress

Nothing is running.

Outstanding - no action requested now

**Accepted fallout under NO-ALIAS, recorded rather than worked around:**

- Seven principals in other territories still declare `[skills.ki-work-folder]` and not `[skills.ki-work-package]`: er-principal, hnr-principal, legal-principal, personal-principal, si-principal, tmx-principal and va-principal. They are territories-package's to switch.
- Once the harness is reinstalled, two things fail in each of those seven until it switches:
  - the `ki-work-folder` declaration resolves to no skill;
  - its `ki-coordination` declaration fails its now-required `ki-work-package` dependency.
- The installed harness payload carries the alias until the next reinstall. That reinstall should leave no `ki-work-folder` payload behind.

**Live `ki-work-folder` references in tools-ki, for ki.tools-burndown (not edited):**

- `man/ki.1:1995`: `.B ki-work-folder`, in the `ki work` description ("under the ki-work-folder work-folder standard").
- `man/ki.commands.json:548`: the `ki work` purpose string, "under the ki-work-folder work-folder standard". No source file in `src/` holds the old name, so the fix is in the generated man page and its command data, or in whatever produces them.
- `docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md:21`: "the `ki-work-folder` standard" in the record's scope. Line 25 is a historical decision quote, and line 30 is a link pinned to an old revision; both can stay.
- `docs/roadmap/KI-TOOL-KI-CLI-152-work-folder-housekeeping-commands.md:17`: "the `ki-work-folder` standard" in the record's scope.
- `docs/roadmap/KI-TOOL-KI-CLI-152-work-folder-housekeeping-commands.md:23`: a broken local link to `ki-work-folder/references/standards-work-folder.md`. It should point to `ki-work-package/references/standards-work-package.md`.
- `CHANGELOG.md:187` and `:195` are historical and keep the old name.
- No test in tools-ki names `ki-work-folder`.

**Chezmoi source:** no references, tracked or untracked.

**Other sessions' work:** the stacked commits are named under HARNESS-PUSH. I touched no other session's dirty files; ki-agentic-harness has none.

## Queries

### HARNESS-PUSH - Four of the six unpushed harness commits are not this run's

**Context:** In ki-agentic-harness, local `main` is six commits ahead of `origin/main`. Two are this run's: `3d50e252` (alias removal) and `9c9ae922` (diagrams). Two are work-package-standard's: `9e174750` (rename) and `4434afaf` (diagrams). The other two come from the acquire session: `8bc9d49d` (shared acquisition contract) and `88cce3e5` (acquire diagrams). The brief allows a push only where my own commits alone are stacked, so I did not push. Tests and typecheck pass on the combined tree, and its only failing check is FILES-10, from `8bc9d49d`. This repeats work-package-standard's open HARNESS-PUSH with two more commits.

**Query:** Will you push all six commits now, or hold until the acquire session pushes its own?

**Options:**

a) (recommended, confidence medium - the combined tree tests clean and the four ways-of-working commits form one reviewed chain, but I have not reviewed the acquire commits) Push all six after a look at `8bc9d49d` and `88cce3e5`, and ask the acquire session to fix the FILES-10 table order.

b) Hold until the acquire session pushes its two commits, then push the four ways-of-working commits.

### 🤖 → 👤 Handoff to supervisor · since 14:48 BST

👤 1 with you · 🤖 0 running

- [with you] HARNESS-PUSH · owner · since 14:48
- [committed] ki-agentic-harness `3d50e252`, `9c9ae922`
- [unpushed] ki-agentic-harness, six commits
