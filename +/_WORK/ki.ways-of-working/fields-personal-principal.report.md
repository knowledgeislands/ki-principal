# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › fields-personal-principal

**🤖 → 👤 Handoff to supervisor · Run report at 14:13 BST · last mark 13:37 BST**

---

## Done

The field migration in personal-principal is finished and pushed. 26 of the 35 records changed. Nothing remains on a retired horizon, `initiative` is gone, and no record names a theme beside its Project. Kind and size are proposed below and not written.

- Commit `98c2472e`, `chore(roadmap): migrate record fields to the work-record model`. I staged the 26 record files by explicit path. The repository has no pre-commit gate. It was the only commit stacked on `origin/main`, so after `pull --rebase` I pushed it fast-forward, and the branch is level.
- Horizon pass. I checked that `ki repo roadmap migrate` (ki 0.11.4) reads `Streams/Roadmap/`. Before applying, I listed each record's status beside its retired horizon: all 22 were `status: draft` on `horizon: triage`. None was ready or in progress, so I left nothing untouched. None was on Waiting for or Parked, so no REVIEW placeholder arose. The dry run matched the standard's rule, and `--apply` moved all 22 to `status: triage` with no horizon and advanced `updated_at`.
- Classification pass. This was a separate script, kept outside the repository, run as a dry run first and then applied. The applied diff was the same as the dry run apart from the timestamps. It dropped the theme beside a Project in 12 records and renamed `initiative` to `theme` in 3. Its dry-run diff, without the `updated_at` lines:

```diff
KB-PRINCIPAL-004  -theme: intentional-living
KB-PRINCIPAL-014  -theme: personal-finance
KB-PRINCIPAL-015  -theme: personal-finance
KB-PRINCIPAL-016  -theme: email-management
KB-PRINCIPAL-017  -theme: email-management
KB-PRINCIPAL-018  -theme: relationships
KB-PRINCIPAL-019  -theme: relationships
KB-PRINCIPAL-020  -theme: relationships
KB-PRINCIPAL-024  -theme: relationships
KB-PRINCIPAL-025  -theme: relationships
KB-PRINCIPAL-026  -theme: relationships
KB-PRINCIPAL-027  -theme: relationships
KB-PRINCIPAL-038  -initiative: life-admin             +theme: life-admin
KB-PRINCIPAL-042  -initiative: knowledge-acquisition  +theme: knowledge-acquisition
KB-PRINCIPAL-043  -initiative: life-admin             +theme: life-admin
```

- Counts. Retired horizons went from 22 to 0, `initiative` from 3 to 0, and a theme beside a Project from 12 to 0. There were no `waiting_on_trades` before or after. Every triage record now has no horizon, and every draft has one. The net record count is 0 (35 before and after: 34 open and 1 cancelled).
- Before audit, with `ki repo audit --skill ki-repo-kb-streams`: passed with 0 failures and 34 warnings. 33 are a missing `size`; one is the legacy `Streams/Initiatives/` folder. `--skill ki-work` passed.
- After audit, run the same way: the same 34 warnings, line for line, and 0 failures. `--skill ki-work` passed. The checker cannot see the fields this run fixed (see STREAMS-CHECKER-GAP), so I confirmed the fix with my own scan of the record front matter.
- The full `ki repo audit` failed both before and after, on the same tool error, before it evaluated anything: ki-coordination's rubric item COORD-1 uses a level the tool does not declare. This was already there, and I left it alone.

Per record, with the before and after state of each changed record (all records are in `/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/`):

| Record | Before | After |
| --- | --- | --- |
| [KB-PRINCIPAL-004](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-004-develop-intentional-life-thesis.md) | draft · next · theme intentional-living + project intentional-life | draft · next · project intentional-life |
| [KB-PRINCIPAL-009](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-009-track-repository-intelligence-tools.md), [011](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-011-reconcile-kb-guidance.md), [013](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-013-complete-source-mirrors.md), [021](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-021-process-granola-self-messages.md), [022](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-022-acquire-phone-voice-memos.md), [023](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-023-review-personal-priorities.md), [030](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-030-acquire-granola-personal-meetings.md), [031](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-031-decide-voicenotes-sync-target.md), [032](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-032-ship-chatgpt-capture.md), [033](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-033-import-historical-chatgpt.md), [034](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-034-manage-codex-sessions.md) (11, projectless) | draft · horizon triage · theme kept | triage · no horizon · theme unchanged |
| [KB-PRINCIPAL-014](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-014-verify-improv-mx-cancellation.md), [015](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-015-review-personal-spending.md), [016](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-016-tidy-older-to-file-emails.md), [017](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-017-assess-email-storage.md) (project household-and-finance) | draft · horizon triage · theme + project | triage · no horizon · project only |
| [KB-PRINCIPAL-018](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-018-plan-half-term-break-with-lauren.md), [019](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-019-plan-halloween-activity.md), [020](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-020-reconnect-with-friends.md), [024](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-024-plan-laurens-birthday.md), [025](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-025-use-north-york-moors-railway-tickets.md), [026](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-026-contact-helen-about-writing-to-children.md), [027](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-027-mark-daughters-october-birthday.md) (project family-and-friends) | draft · horizon triage · theme relationships + project | triage · no horizon · project only |
| [KB-PRINCIPAL-038](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-038-complete-personal-email-triage.md) | triage · initiative life-admin | triage · theme life-admin |
| [KB-PRINCIPAL-042](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-042-create-personal-activities-collection.md) | cancelled · initiative knowledge-acquisition | cancelled · theme knowledge-acquisition |
| [KB-PRINCIPAL-043](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-043-write-personal-gmail-rules.md) | draft · soon · initiative life-admin | draft · soon · theme life-admin |

These records were left unchanged: [KB-PRINCIPAL-002](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-002-costa-rica-flight-planning.md), [003](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-003-hermes-skill-stack-review.md), [005](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-005-enterprise-agent-economics.md), [006](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-006-tech-medics-microtools.md) and [007](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-007-software-discovery-and-evaluation.md) (draft · future), [037](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-037-review-repository-naming.md), [044](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-044-reground-git-audit-artifact.md) and [045](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-045-redraw-mermaid-diagrams-in-archify.md) (triage), and [041](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-041-initial-personal-health-stocktake.md) (draft · now).

### Kind and size proposals (not written)

These cover the 34 open records; the cancelled [KB-PRINCIPAL-042](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-042-create-personal-activities-collection.md) is exempt. `kind` is required only once a record is adopted, so on a triage record the proposed kind is the one to set at adoption. Size uses GDR-KI-PRINCIPAL-016's delivery shapes: `s` is one run and one commit, `m` one run with several commits and a plan, and `l` several chained runs or repositories.

| Record | State | Kind | Size |
| --- | --- | --- | --- |
| [KB-PRINCIPAL-002](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-002-costa-rica-flight-planning.md) Costa Rica flights | draft · future | investigate | m |
| [KB-PRINCIPAL-003](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-003-hermes-skill-stack-review.md) Hermes skill review | draft · future | investigate | m |
| [KB-PRINCIPAL-004](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-004-develop-intentional-life-thesis.md) Intentional life thesis | draft · next | deliver | l † |
| [KB-PRINCIPAL-005](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-005-enterprise-agent-economics.md) Agent economics | draft · future | investigate | m |
| [KB-PRINCIPAL-006](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-006-tech-medics-microtools.md) Microtools | draft · future | investigate | l |
| [KB-PRINCIPAL-007](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-007-software-discovery-and-evaluation.md) Software discovery | draft · future | decide | m |
| [KB-PRINCIPAL-009](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-009-track-repository-intelligence-tools.md) Repository intelligence watch | triage | investigate | s |
| [KB-PRINCIPAL-011](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-011-reconcile-kb-guidance.md) Reconcile KB guidance | triage | deliver | m |
| [KB-PRINCIPAL-013](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-013-complete-source-mirrors.md) Source mirrors | triage | deliver | l |
| [KB-PRINCIPAL-014](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-014-verify-improv-mx-cancellation.md) Improv MX cancellation | triage | investigate | s |
| [KB-PRINCIPAL-015](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-015-review-personal-spending.md) Personal spending | triage | audit | m |
| [KB-PRINCIPAL-016](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-016-tidy-older-to-file-emails.md) `_to file` emails | triage | deliver | m |
| [KB-PRINCIPAL-017](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-017-assess-email-storage.md) Email storage | triage | investigate | s |
| [KB-PRINCIPAL-018](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-018-plan-half-term-break-with-lauren.md) Half-term break ‡ | triage | deliver | s |
| [KB-PRINCIPAL-019](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-019-plan-halloween-activity.md) Halloween activity ‡ | triage | deliver | s |
| [KB-PRINCIPAL-020](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-020-reconnect-with-friends.md) Reconnect with friends | triage | deliver | m |
| [KB-PRINCIPAL-021](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-021-process-granola-self-messages.md) Granola self-messages | triage | deliver | s |
| [KB-PRINCIPAL-022](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-022-acquire-phone-voice-memos.md) Phone voice memos | triage | deliver | m |
| [KB-PRINCIPAL-023](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-023-review-personal-priorities.md) Personal priorities | triage | decide | s |
| [KB-PRINCIPAL-024](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-024-plan-laurens-birthday.md) Lauren's birthday ‡ | triage | deliver | s |
| [KB-PRINCIPAL-025](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-025-use-north-york-moors-railway-tickets.md) Railway tickets ‡ | triage | decide | s |
| [KB-PRINCIPAL-026](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-026-contact-helen-about-writing-to-children.md) Contact Helen | triage | deliver | s |
| [KB-PRINCIPAL-027](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-027-mark-daughters-october-birthday.md) Daughter's birthday ‡ | triage | deliver | s |
| [KB-PRINCIPAL-030](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-030-acquire-granola-personal-meetings.md) Granola personal meetings | triage | deliver | m |
| [KB-PRINCIPAL-031](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-031-decide-voicenotes-sync-target.md) Voicenotes sync target | triage | decide | s |
| [KB-PRINCIPAL-032](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-032-ship-chatgpt-capture.md) ChatGPT capture | triage | deliver | l |
| [KB-PRINCIPAL-033](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-033-import-historical-chatgpt.md) Historical ChatGPT import | triage | deliver | m |
| [KB-PRINCIPAL-034](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-034-manage-codex-sessions.md) Codex sessions | triage | deliver | m |
| [KB-PRINCIPAL-037](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-037-review-repository-naming.md) Repository naming | triage | decide | s |
| [KB-PRINCIPAL-038](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-038-complete-personal-email-triage.md) Personal email triage | triage | deliver | l |
| [KB-PRINCIPAL-041](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-041-initial-personal-health-stocktake.md) Health stocktake | draft · now | investigate (already set) | m |
| [KB-PRINCIPAL-043](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-043-write-personal-gmail-rules.md) Gmail rules | draft · soon | deliver (already set) | m |
| [KB-PRINCIPAL-044](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-044-reground-git-audit-artifact.md) Git audit artifact | triage | deliver | s |
| [KB-PRINCIPAL-045](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-045-redraw-mermaid-diagrams-in-archify.md) Archify redraw | triage | deliver | s (already set) |

† The thesis may prove `xl` once it is shaped, because it develops a philosophy and then proposes enactments in several territories. If so, it should be split before Ready. ‡ This record is tied to a date in late October and lost adoption in this run (see PRINCIPAL-READOPT).

In short, I propose 6 kinds for the adopted records that lack one, 26 kinds for triage records to set at adoption, and 33 new sizes. The 33 missing sizes are the whole of the 33 size warnings.

### Lessons for hnr-principal, 5g-emerge-phase2 and legal-principal

- Count the records yourself. The pilot's figures for this repository were swapped: there were 12 themes beside a Project and 3 `initiative` fields, not the other way round.
- `ki repo roadmap migrate` does read `Streams/Roadmap/`. Its dry run is reliable, and it changes only the horizon, status and `updated_at`.
- Neither the installed Streams checker nor the workspace one flags the retired horizons, `initiative` or a theme beside a Project. The audit shows the same warnings before and after, so prove the migration with a front-matter scan: retired horizons, `initiative`, theme with Project, triage with a horizon, and draft without one.
- In a Capital with `ki-coordination` declared, the full `ki repo audit` stops on the COORD-1 error. Audit with `--skill ki-repo-kb-streams` and `--skill ki-work`.
- In the old Capital model, `draft` on `horizon: triage` meant captured intake, so the mechanical result keeps the meaning. Still, read each record for a date, because date-bound personal or client items silently leave selection.
- Here, a theme beside a Project was the old free-text grouping, such as `relationships` or `personal-finance`. It differed from the Project's own theme, so dropping it loses a finer grouping that nothing in the model reads. Say so in the report.
- The Project notes still carry `initiative:`, and `Streams/Initiatives/` still exists. That is the registry migration, a separate pass, so leave it alone.
- A classification script must advance `updated_at` as `migrate` does. Make sure it leaves a closed record's status alone. Mine renamed `initiative` on the cancelled record and touched nothing else.
- In zsh, a path list held in a variable does not split into words. Stage with `git diff --name-only -z -- <dir> | xargs -0 git add --`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Projectless [KB-PRINCIPAL-011](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-011-reconcile-kb-guidance.md) names `theme: repository-governance`, which no Personal theme or Initiative defines. The record was already like this, and the checker did not flag it.
- The Personal registry is still in the thread-model shape: `Streams/Initiatives/`, and `initiative:` on the five Project notes. That belongs to the work-model registry migration, not to this run.
- The COORD-1 tool error stops the full `ki repo audit` in this repository and in any repository that declares `ki-coordination`.

## Queries

### PRINCIPAL-READOPT - Whether the 22 records that left adoption are re-adopted

**Context:** The rule turned `horizon: triage` into `status: triage` for 22 drafts. In this Capital, that draft-on-triage combination already meant captured intake, so the meaning holds, but leaving triage now needs your approval. Five are date-bound and now fall outside selection: the half-term break ([KB-PRINCIPAL-018](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-018-plan-half-term-break-with-lauren.md)), Halloween ([KB-PRINCIPAL-019](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-019-plan-halloween-activity.md)), Lauren's birthday ([KB-PRINCIPAL-024](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-024-plan-laurens-birthday.md)), the railway tickets before expiry ([KB-PRINCIPAL-025](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-025-use-north-york-moors-railway-tickets.md)) and your daughter's birthday on 27 October ([KB-PRINCIPAL-027](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-027-mark-daughters-october-birthday.md)).

**Query:** Should the five date-bound records be adopted now while the other 17 stay in triage?

**Options:**

a) (recommended, confidence medium - the mechanical result matches the old meaning, but the dated items fall before their next likely review) Adopt the five date-bound records now through `ki-next`, as `draft` at Now or Next with the proposed kind and size, and leave the other 17 in triage for ordinary intake review.

b) Leave all 22 in triage until the next personal triage review.

c) Adopt all 22 again at once through `ki-next`, each with a horizon chosen afresh.

### PRINCIPAL-KIND-SIZE - Confirming the proposed kind and size

**Context:** The table above proposes a kind for the 6 adopted records that lack one, a kind for each of the 26 triage records to set at adoption, and a size for 33 records. GDR-KI-PRINCIPAL-016 makes these the owner's judgement. Until the `ki` release that accepts the fields, a writer leaves out any field the installed `ki` rejects. The harness already accepts `size`, as [KB-PRINCIPAL-045](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-045-redraw-mermaid-diagrams-in-archify.md) shows.

**Query:** Do you confirm the proposals, with any changes, so that a follow-up run can write them?

**Options:**

a) (recommended, confidence medium - the sizes are provisional judgements from each record's Goal and Boundary, and are revisited before Ready anyway) Confirm them as listed. A short follow-up run then writes the 33 sizes and the 6 adopted kinds now, and the triage kinds are set at adoption.

b) Confirm them with the changes you name, for example `xl` on [KB-PRINCIPAL-004](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-004-develop-intentional-life-thesis.md).

c) Hold all kind and size writes until the `ki` release, and write them together with the other repositories.

### STREAMS-CHECKER-GAP - The Streams checker cannot see the migrated fields

**Context:** The Streams checker, both installed and in the workspace at `88cce3e5`, does not warn on a retired horizon, on `initiative` or on a theme beside a Project. It lists `initiative` as a known field. The standard's migration window says the checkers warn on all three, and the window closes on "a complete scan of that inventory showing no gaps", so a scan of Streams Capitals would wrongly report no gaps. This matches VALIDATOR-PARITY, which ki.tools-burndown holds.

**Query:** Should the coordinator route this gap to the harness owner before the remaining Streams migrations?

**Options:**

a) (recommended, confidence high - verified directly: the before and after audits gave the same 34 warnings, and the workspace `streams.ts` has no rule for these shapes) Route it now as a Messages line to the harness work that owns the checkers, and have each remaining field run prove its result with a front-matter scan, as here.

b) Fold it into the next harness release run, and carry on with the front-matter scans meanwhile.
