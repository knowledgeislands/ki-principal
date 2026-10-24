# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › banner-on-state

**🤖 → 👤 Handoff to supervisor · Run report at 22:43 BST · last mark 22:33 BST**

---

## Done

- Commit `6baab0b0` `feat(ki-coordination): end state-bearing replies with the banner`, made in a separate worktree and then fast-forwarded onto the main checkout's `main`. Other sessions' uncommitted files in the main checkout were not touched and did not overlap with this change.
- Where BANNER-ON-STATE landed:
  - [standards-coordination.md:222](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md): a new **When it appears.** paragraph in the Banner section.
  - [standards-coordination.md:197](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md): the "Heading and banner" coordinating practice.
  - [standards-coordination.md:405](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md): the Reply forms "Conversational reply" row, which now makes an exception to "no banner".
  - [standards-coordination.md:619](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md): the output-style source's Banner section. It is generated into [output-styles/ki-coordinator.md:34](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/output-styles/ki-coordinator.md).
- A thirtieth review entry was added to the ki-coordination [sources.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/sources.md). New assertions in `banner.test.ts` check that the rule appears in both the standard and the output style.
- Hook decision: the rule went into the hook line. It is one clause in hard rule 4 ([standards-coordination.md:562](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md), generated into [hooks/coordinator-reminder.sh:17](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/hooks/coordinator-reminder.sh)). The line grew from about 1,267 to about 1,375 characters, under the 1,500 ceiling, and every existing clause is unchanged. `hooks/coordinator-reminder.test.ts` repeats the line word for word, so it was updated to match.
- Generated surfaces: `ki dev skill generate --write` writes to the main checkout through the installed harness link, so I ran the skill's own generator against the worktree instead. The output style and hook line were regenerated; the run-report and footer surfaces did not change.
- Tests pass (1,295, none failing) after the hook test's pinned line was updated.
- The type check passes.
- The ki-skills and ki-authoring audits pass.
- The ki-coordination audit has no failures and one warning. The warning is COORD-3: one work folder is waiting under `+/_WORK_REVIEW/`. This was already in the repository and this change did not cause it.
- The generator check reports all 7 surfaces in sync on the main checkout after the fast-forward.
- Pushed fast-forward to origin/main. Only this commit was stacked, and the remote had no new commits after a fetch. The remote reported that its PR and status-check rules were bypassed for the push. That matches this repository's direct-to-`main` workflow.
- The worktree, its temporary branch and the temporary files have been removed.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The Work Process note's Banner section in Knowledge Islands Principal was not changed. The brief covered only the harness standard and its surfaces.

## Queries

### NOTE-BANNER - carry BANNER-ON-STATE into the Work Process note

**Context:** The harness standard now says that any coordinator reply that moves the mark, changes the state or answers where the work stands ends with the banner. The standard cites the Work Process note's Banner section in ki-principal for the banner itself. That note does not yet say when a non-report reply carries the banner.
**Query:** Should a ki-principal run add one sentence on BANNER-ON-STATE to the Work Process note's Banner section?
**Options:**
a) (recommended, confidence medium - I did not read the note, so whether it needs the sentence is not verified) queue a short ki-principal run to add the sentence, citing BANNER-ON-STATE
b) leave the note as it is and let the harness standard hold the rule

### 🤖 → 👤 Handoff to supervisor · since 22:43 BST

👤 1 with you

- [with you] NOTE-BANNER · owner · since 22:43
- [committed] ki-agentic-harness `6baab0b0`, pushed
