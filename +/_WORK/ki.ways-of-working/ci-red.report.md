# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › ci-red

**🤖 → 👤 Handoff to supervisor · Run report at 20:41 BST · last mark 20:20 BST**

---

## Done

- Ran the CI audit (`ki repo audit`, ki 0.11.3) on the working tree and again on a clean clone of HEAD, which is what CI sees. Both fail. COORD-7 flags reports in ki.ways-of-working, ki.chezmoi, ki.mac-studio-setup and ki.observatory, and RECORD-2 flags `+/_WORK/ki.observatory/work.md`. ki.tools-burndown has no findings, so it got no Messages line.
- ki.ways-of-working, `b4e46ed`: added links in `gov197-hook`, `ki-release`, `mgit-filter`, `prune-held`, `review-gov194-201` and `rig-release`, 44 identifiers in all. Each live record links to its absolute local path. The pruned ones are written `<ID> (pruned)` and link to their GitHub copy at the last revision: [KI-HARNESS-GOV-194 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f7982a61/docs/roadmap/KI-HARNESS-GOV-194-review-verification-effects.md), [KI-TOOL-MGIT-CLI-020 (pruned)](https://github.com/knowledgeislands/tools-mgit/blob/e91c0081/docs/roadmap/KI-TOOL-MGIT-CLI-020-safe-parallel-sync.md), [KI-TOOL-MGIT-CLI-021 (pruned)](https://github.com/knowledgeislands/tools-mgit/blob/e91c0081/docs/roadmap/KI-TOOL-MGIT-CLI-021-estate-overview.md), [KI-TOOL-KI-CLI-142 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/683abf5f/docs/roadmap/KI-TOOL-KI-CLI-142-preserve-harness-release-settings.md) and [KI-TOOL-KI-CLI-148 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/683abf5f/docs/roadmap/KI-TOOL-KI-CLI-148-coordination-rename-cli-side.md). The audit now finds nothing in this folder, and the commit gate passed. No files here were dirty from another session, so I skipped none.
- Two links go to GitHub rather than a local path, because the check reads them as record identifiers:
  - MGIT-WS-009 is a specification section, not a record. It links to [its section of `workspace-dispatch.md` at `781973e`](https://github.com/knowledgeislands/tools-mgit/blob/781973e/docs/specs/workspace-dispatch.md#mgit-ws-009--filter-composition). A local link would fail CI's file-name check.
  - The Needs tag PRUNE-GOV-201 also looks like a record identifier to the check. In its query heading and banner it links to the GitHub copy of [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) at `f7982a61`. That keeps the tag readable as a tag.
- Messages lines, one per work, tag PRINCIPAL-CI-RED, each naming the failing files and the fix:
  - ki.chezmoi `ce7b293`: `burn-a`, `burn-b`, `burn-order`, `coord-style`, `src-trio` and `ue086-a`. The line includes the pruned copy of KI-HARNESS-GOV-186 at `dd5761c6`.
  - ki.mac-studio-setup `8c16656`: `rig-lane.report.md`, whose KI-TOOL-RIG-CORE-058 link points at a pruned file. The brief did not list this work, but it has a finding. The line includes the copy at `6ac358fb`.
  - ki.observatory: the RECORD-2 fixes, plus the KI-OBSERVA-BRG-002 link and Markdown fix its still-untracked `obs-extensions` report needs before it is committed. That coordinator committed my uncommitted line inside its own `89535e2` before I could commit it.
- Push: the observatory session's commit `89535e2` sat under mine, so I held my push rather than push another session's commit. That session then pushed fast-forward, and its push took my three commits to origin as well. I did not push anything myself, and HEAD and origin/main now match.
- Net records: 0 in ki-principal.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- CI is not green after the push. I could not see the CI run because no GitHub calls were allowed. A clean-clone audit of the pushed HEAD still fails in two places:
  - COORD-7 on the six ki.chezmoi reports.
  - RECORD-2 on `+/_WORK/ki.observatory/work.md`: empty Parked and `hold: null`. My line fills its Messages section, but these two need that coordinator.
- `rig-lane.report.md` in ki.mac-studio-setup fails only locally. CI has no tools-rig checkout, so it checks only the link's file name, and that passes.
- When the untracked ki.observatory `obs-extensions.report.md` is committed, it will add a COORD-7 finding and a Markdown-format failure unless its coordinator fixes it first.
- Other sessions' dirty files I left alone: `+/_WORK/ki.chezmoi/briefs/finish-drift-prerequisites.md`, `+/_WORK/ki.chezmoi/finish-drift-prerequisites.report.md`, `+/_WORK/ki.observatory/obs-extensions.report.md` and `+/_WORK/ki.observatory/obs-mermaid.report.md`.

## Queries

### CI-RED-REST - ki-principal CI stays red until two other works act

**Context:** This work's reports are fixed and pushed. CI still fails on six ki.chezmoi reports, which have unlinked identifiers, and on the observatory work file's empty Parked and `hold: null`. Both works now have a PRINCIPAL-CI-RED Messages line with the exact fix. Both have sessions active right now, so editing their files directly would collide with them.

**Query:** Should CI wait for ki.chezmoi and ki.observatory to act on their Messages lines, or should one run fix their files directly?

**Options:**
a) (recommended, confidence medium - both works are active and their lines name the fixes, but how soon they act is up to them) Leave it to each work's next update, and check CI again at the next mark.
b) Authorise one run to fix the ki.chezmoi reports and the observatory work file directly once neither has dirty files from another session.

### 🤖 → 👤 Handoff to supervisor · since 20:41 BST

👤 1 with you

- [with you] CI-RED-REST · owner · since 20:41
- [committed] ki.ways-of-working report links, pushed (in another session's push)
- [committed] Messages lines to ki.chezmoi, ki.mac-studio-setup and ki.observatory, pushed
