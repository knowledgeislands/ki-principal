# [Knowledge Islands](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/Themes.md) › State of play › review-hold

**🤖 → 👤 Handoff to supervisor · Run report at 19:02 BST · last mark 18:58 BST**

---

## Done

- I assessed all six held folders against the REVIEW-SURFACE rule, the `ki-work-package` rule for work awaiting review, both `README.md` index notes, the current `+/_WORK/` folders, the Project notes and the records they cite. Read-only: I wrote nothing except this report and committed nothing.
- Result: three folders are live and should come back as on-hold packages, and three are dead. On-hold work does not count against the cap (COORD-3). Two of the dead folders hold a few lines that must be moved elsewhere before deletion (see the tables).
- Limitation: I checked "pushed" against the local `origin/main` ref without fetching. Several parked items in [ki.estate-factorisation](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK_REVIEW/ki.estate-factorisation/work.md) rest on that drained run's own claims, which I did not re-verify.

### ki-principal `+/_WORK_REVIEW/`

| Item | Repository | Live or dead | Reason | Confidence | Evidence path |
| --- | --- | --- | --- | --- | --- |
| ki.agent-host | ki-principal | Live, on hold | The [Agent host](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/agent-host.md) Project is `lifecycle: active` under the Techne theme. The Project note links [workstation-bundle-walkthrough](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK_REVIEW/ki.agent-host/design/workstation-bundle-walkthrough.md) in this folder's `design/`, so deleting the folder would break that link. Open items: [KI-TOOL-TECHNE-CLI-009](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-009-tailscale-oauth-binding-field.md) is Draft / Next, [KI-TECHNE-OPS-018](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) is on Hold, the vega host-name hold is still in force, and the parked "personal harness instructions" idea has no other home. CLI-133-DELIVER is moot: [KI-TOOL-KI-CLI-133 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/683abf5f/docs/roadmap/KI-TOOL-KI-CLI-133-retired-reports-come-back.md) was accepted and pruned in tools-ki `06caa2ab`. Owner: the Techne theme, Agent host Project, with release when the Techne Programme Hold lifts. On return, drop the CLI-133 and STORE-REPAIR lines and keep `design/`. | high (live is not destructive; the Project's status and the design link were checked directly) | `Streams/Projects/agent-host.md` lines 1-36; `+/_WORK_REVIEW/ki.agent-host/work.md` Parked |
| ki.baseline-rollout | ki-principal | Dead | This is the old drained checkpoint from 15 October. A new package, [ki.baseline-rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/work.md), was created on 19 October (`7d463f09`, `1bb3b13b`) with its own scope, decisions, the WAVE-1 query and Handoff to supervisor. The PIN idea is carried in the [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) Project note at line 39. Two parked lines exist only here and should move first: CHECKLIST (adopt the stock Repository review Activity estate-wide only if Kris approves it for the Capital first), and the `update-ki-pin.yml` payload-field mismatch (`source_repository` against `repository`). Its decisions are thread-operational and superseded. | medium (deleting is safe only after those two lines are moved) | `+/_WORK_REVIEW/ki.baseline-rollout/work.md` Parked; `+/_WORK/ki.baseline-rollout/state.md`; `Streams/Projects/baseline-rollout.md` line 39 |
| ki.estate-factorisation | ki-principal | Live, on hold | The [Estate factorisation](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/estate-factorisation.md) Project is `lifecycle: active`. No `+/_WORK/` package or roadmap record carries it: only the new baseline-rollout package names it, and only as out of scope. PROJECT-CLOSE (phases and close-out gates still open) and the unverified OBS-ACTIVATION, GOVERNANCE and ALIAS-OWNERS items exist only here. On return, cut it to those open items under the Foundations theme. The rest are pointers to receivers (DEPS-HOLD, STORE-REPAIR, HOST-*, KI-RELEASE, TRIAGE-OWNERS, DOCK, RIG-REFS, RECEIVER-ROLLOUT), and some link to stale `_WORK_REVIEW` paths. | medium (the closing gates come from the drained run's own claims, not re-verified) | `+/_WORK_REVIEW/ki.estate-factorisation/work.md` Parked; `Streams/Projects/estate-factorisation.md` front matter |
| ki.paperclip-capture-and-rebuild | ki-principal | Live, on hold | The [Paperclip capture and rebuild](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/paperclip-capture-and-rebuild.md) Project is `lifecycle: active`. Its note relies on [[paperclip-rebuild-structure]] at lines 37 and 61, and that file lives only in this folder's `design/`. The [ki](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/state.md) next steps still schedule "the Paperclip rebuild once the work model settles". Owner: the Techne theme, Paperclip capture and rebuild Project, with release when the Techne Programme Hold lifts. | high (live is not destructive; the link dependency was checked directly) | `Streams/Projects/paperclip-capture-and-rebuild.md` lines 37 and 61; `+/_WORK_REVIEW/ki.paperclip-capture-and-rebuild/design/` |
| ki.regular.command-centre | ki-principal | Dead | Its subject was folded into the [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) Project under OBS-OWNER on 18 October, as the note records at lines 20 and 51. The only substantive decision, CC-HANDOFFS, is carried in [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) at line 32. The other decisions are generic token and commit reminders. Nothing is parked. | high (both homes were read directly) | `Streams/Projects/observatory.md` lines 20 and 51; `Streams/Projects/ways-of-working.md` line 32 |

### ki-agentic-harness `+/_WORK_REVIEW/`

| Item | Repository | Live or dead | Reason | Confidence | Evidence path |
| --- | --- | --- | --- | --- | --- |
| ki.regular.skill-reviews | ki-agentic-harness | Dead | The work is finished. [KI-HARNESS-GOV-193 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/c0924316/docs/roadmap/KI-HARNESS-GOV-193-area-diagrams-with-html.md) was accepted in `c0924316` and pruned in `b7f35cdf`. Both commits the push queries asked about (`a830b6ed`, `58d41ccc`) are ancestors of the local `origin/main` ref. The SRC-BADGE follow-up lives in [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) (triage). The decisions log was already folded in `b868812e`. Its briefs and scratch scripts are throwaway now that the generator change has landed. | medium (`origin/main` was not fetched, and I did not check the KI-PREFIX and PULSE notes against the diagrams one by one) | `+/_WORK_REVIEW/ki.regular.skill-reviews/*.report.md`; `docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md` |

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Whoever revives ki.agent-host and ki.estate-factorisation should repoint their links from `+/_WORK_REVIEW/...` to `+/_WORK/...` and drop the parked items that have since been resolved, as listed in the tables.

## Queries

### REVIEW-HOLD - live or dead for six held work folders

**Context:** Six folders are held for review. ki.agent-host and ki.paperclip-capture-and-rebuild belong to active Techne Projects whose Project notes link design papers in these folders. ki.estate-factorisation is the only home of its active Project's close-out. ki.baseline-rollout is the old copy of a package rebuilt in `+/_WORK/` today, and two of its parked lines are not carried anywhere else. ki.regular.command-centre is fully carried by the Observatory and Ways of working Project notes. ki.regular.skill-reviews is finished: its record was accepted and pruned, and its commits are pushed. On-hold packages do not count against the cap.

**Query:** Do you agree that the three Project folders return to `+/_WORK/` on hold and the other three are deleted, after the two baseline-rollout parked lines are moved into the live package?

**Options:**

a) (recommended, confidence medium - every live call and both deletion homes were checked directly; the estate-factorisation gates and the unfetched `origin/main` were not) Move ki.agent-host, ki.estate-factorisation and ki.paperclip-capture-and-rebuild to `+/_WORK/` with `git mv`, in package shape at `state: on-hold`. Copy CHECKLIST and the `update-ki-pin.yml` payload mismatch into `+/_WORK/ki.baseline-rollout/queries.md` under Parked. Then delete `+/_WORK_REVIEW/ki.baseline-rollout/`, `+/_WORK_REVIEW/ki.regular.command-centre/` and the harness's `+/_WORK_REVIEW/ki.regular.skill-reviews/`, removing each index line in the same commit.

b) Same as a), except ki.estate-factorisation is deleted too: send its PROJECT-CLOSE, OBS-ACTIVATION, GOVERNANCE and ALIAS-OWNERS items to State of play's `messages.md` first, and leave the Project to be reconciled from there.

c) Keep all six held until the Techne Programme Hold lifts, and delete only ki.regular.command-centre and ki.regular.skill-reviews now.
