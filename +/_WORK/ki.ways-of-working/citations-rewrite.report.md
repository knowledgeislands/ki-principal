# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › citations-rewrite

**🤖 → 👤 Handoff to supervisor · Run report at 18:18 BST · last mark 18:12 BST**

---

## Done

- **Scope.** I re-scanned all 51 registered repositories. Citations of retired `+/_THREADS/` and `+/_CHECKPOINTS/` paths were rewritten outside the work areas, which is the scope CITATIONS-DANGLE asked about. Successors were mapped from each repository's Git history, using renames, the conversions from checkpoint to package in the migration commits, and the last revision of each pruned file. Nothing was invented; every pruned revision was checked to hold its file and to be on origin. Unresolved citations: none.
- **Authority.** Kris, 19 October at 17:57 BST, "CITATIONS-DANGLE - fix them now please" (option b). Every commit body cites it as standing in for an Enactment record. Every commit has the subject `docs: rewrite retired work-folder citations`. Net records: 0 in every repository.
- **What was rewritten.** Only references meant to be followed were rewritten. Left as written: generic convention mentions; code, tests, rubric logic, man pages and generated diagrams that handle the legacy folders; provenance sentences; evidence and retention manifests that pin old paths; links already pinned to a GitHub revision; and owner quotations in decisions logs. `+/_Voice Notes/` and Git history were untouched. No repository had another session's dirty file in a touched path.
- **Bare-name wikilinks.** A second sweep found three wikilinks that give only a note's name (`[[_state-of-play]]` and `[[life-admin.personal-administration]]`), which the path search had missed. I fixed them in legal-principal `68b24574` and personal-principal `aa127e5d`, both pushed.
- **Audits.** Each repository's `ki repo audit` gave no new FAIL in the changed files. Whole-repository totals were unchanged from baseline wherever there was a baseline; apps-tower's audit ran only after editing, with 0 FAIL. Every commit gate and Markdown lint passed.
- **Pushes.** Every push was fast-forward with only my own commit stacked, after `pull --rebase`. No foreign commits were stacked anywhere. The apps-observatory.local push hit two GitHub server errors and landed on retry.
- **Helpers.** The five helpers ran as in-session subagents in parallel. The Agent tool ran them asynchronously inside this session; none was a detached `ki agent` run.

In the table, "rewritten" counts every changed citation, including the pruned links. "Found" counts every matching occurrence, including those left by design.

| Repository | Found | Rewritten | Pruned links | Unresolved | Commit | Pushed |
| --- | --- | --- | --- | --- | --- | --- |
| hnr-principal | 204 in 48 files | 110 | 3 | 0 | `a7667d8` | yes |
| 5g-emerge-phase2 | 9 in 4 files | 1 | 0 | 0 | `1719fac` | yes |
| acquire | 39 in 11 files | 22 | 7 | 0 | `2a70d45` | no, see ACQUIRE-PUSH |
| personal-principal | 24 in 8 files | 22 | 7 | 0 | `03749b16`, `aa127e5d` | yes |
| apps-tower.midnight.ninja | 342 in 11 files | 16 | 13 | 0 | `1112a83` | no, site deploys on push, see TOWER-PUSH |
| legal-principal | 5 in 5 files | 5 | 1 | 0 | `8d1c7321`, `68b24574` | yes |
| tmx-principal | 2 in 2 files | 1 | 0 | 0 | `5e1282c` | yes |
| er-principal | 1 in 1 file | 1 | 0 | 0 | `08c73f3` | yes |
| va-principal | 1 in 1 file | 1 | 0 | 0 | `cf08bec` | yes |
| mcp-gsuite | 3 in 2 files | 3 | 0 | 0 | `d69b955` | yes |
| mcp-m365 | 5 in 3 files | 5 | 0 | 0 | `52d6dbd` | yes |
| tools-rig | 1 in 1 file | 1 | 1 | 0 | `f9409b7` | yes |
| chezmoi source | 6 in 3 files | 6 | 4 | 0 | `5bfcc4f` | yes, no `chezmoi apply` |
| apps-observatory.local | 82 in 27 files | 2 | 0 | 0 | `4763352` | yes, on retry |
| tools-ki | 70 in 15 files, 6 specific | 3 | 1 | 0 | `bfe91f00` | yes |
| ki-agentic-harness | 92 in 35 files, 6 specific | 0 | 0 | 0 | none, all already pinned, generic or provenance | n/a |
| ki-principal | 19 in 5 files | 0 | 0 | 0 | none: 14 links already pinned and resolving, 5 generic or test evidence in `KI-PRINCIPAL-ECO-013` | n/a |
| apps-knowledgeislands.info | 3 generic mentions in CLI data | 0 | 0 | 0 | none, out of bounds for these runs and generic anyway | n/a |

No other registered repository, si-principal included, has a citation outside its work areas.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Some sentences were left as written because the new path would make them untrue. [KI-OBSERVA-BCN-007](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BCN-007-beacon-raises-stuck-work.md) line 114 and [KI-OBSERVA-VIS-025](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-025-work-instrument.md) line 37 describe the old `ways-of-working` thread folder as it stood. [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md) line 209 is test evidence. [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) line 44 and [KI-TOOL-KI-CLI-150](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-150-work-folder-entry-points.md) line 34 record the 18 October regression. Line 83 of [HNR-PRINCIPAL-FIN-001](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-FIN-001-resolve-bridge-funding-consent.md) is a provenance line.
- Two notes now cite the right folder, but their sibling file names have moved within it. In [HNR-PRINCIPAL-5GE-007](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Streams/Roadmap/HNR-PRINCIPAL-5GE-007-review-fourth-outline.md) line 44, `decisions.md` now sits at the package root, not under `design/`. In [5GE-P2-OPS-007](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase2/docs/roadmap/5GE-P2-OPS-007-preview-fourth-outline.md), `site-placement.proposal.md` is now under `design/`. Each record's owner can tidy these at the next touch.
- These old-path citations were left on purpose and are expected to remain: 92 in hnr-principal's build-pipeline delivery JSON, 326 in apps-tower's retention manifest, and 6 in 5g-emerge-phase2's projection manifest. All are evidence pinned to revisions.

## Queries

### ACQUIRE-PUSH - Push the acquire citation commit

**Context:** acquire's `AGENTS.md` line 29 says never to push without explicit authority, so the helper committed `2a70d45` on `main` on this machine and did not push. It is the only commit stacked and changes documentation links only: 15 rewritten, 7 pruned links.

**Query:** Should the acquire commit be pushed now?

**Options:**

a) (recommended, confidence high - one docs-only commit of this run's own, nothing else stacked) Push `2a70d45` fast-forward now, as a follow-up run or by hand.

b) Leave it for acquire's own session to push with its next work.

### TOWER-PUSH - Push the apps-tower citation commit, which redeploys the site

**Context:** apps-tower.midnight.ninja deploys on push through Workers Builds, so `1112a83` is committed and not pushed. It changes links in 10 Markdown files under `docs/` only: 3 rewritten and 13 pruned links. The site's built content is not affected, but a push would still trigger a redeploy.

**Query:** Should the apps-tower commit be pushed now, accepting a redeploy?

**Options:**

a) (recommended, confidence medium - the change is docs-only, but a push redeploys, which you have accepted before) Push `1112a83` now and accept the redeploy.

b) Leave it to go out with the site's next intended deploy.

### WORK-AREA-CITATIONS - Old-path citations inside work packages

**Context:** This run did not touch citations inside `+/_WORK/` and `+/_WORK_REVIEW/`, as the CITATIONS-DANGLE query framed it ("outside the work areas"), and other works' files take only a Messages line. Files there that still cite old paths: hnr-principal 88, ki-principal 45, personal-principal 13, ki-agentic-harness 8, legal-principal 8, acquire 2. Most are moved run reports and design files, where the old path is historical text, about 74 in legal's `hold-park.report.md` alone. A few are live package files.

**Query:** Should the citations inside work packages be rewritten too?

**Options:**

a) (recommended, confidence medium - reports are history that each mark prunes, while live package files belong to each work's worker) Leave reports as they are, and add one line to each affected work's `messages.md` asking its worker to rewrite old paths in its live package files at its next mark.

b) Launch one more mechanical run that rewrites the live package files (`work.md`, `state.md`, `queries.md`, `messages.md`) across the estate with the same successor map, leaving reports and decisions logs alone.

c) Leave everything in the work areas as it is.

### 🤖 → 👤 Handoff to supervisor · since 18:18 BST

👤 3 with you · ⬆️ 2 unpushed

- [with you] ACQUIRE-PUSH · owner · since 18:18
- [with you] TOWER-PUSH · owner · since 18:18
- [with you] WORK-AREA-CITATIONS · owner · since 18:18
- [committed] 17 commits across 15 repositories
- [unpushed] acquire `2a70d45`, apps-tower.midnight.ninja `1112a83`
