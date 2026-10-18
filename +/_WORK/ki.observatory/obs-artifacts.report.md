# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-artifacts

**🤖 → 👤 Handoff to supervisor · Run report at 19:10 BST · last mark 19:08 BST**

---

## Done

- Swept every repository under `~/workspaces/*/*` across all eight territories. Found 15 live-artifact sources: in `hnr-principal`, `legal-principal` and `personal-principal`, and in none of the other territories. Also found two rendered dashboard sites, `apps-rig.midnight.ninja` and `apps-tower.midnight.ninja`. Product dashboards, benchmark reports, slides and diagrams were looked at and left out.
- Only two pairs show in the Observatory today: HNR Council and Legal Activity Status. Legal Hearing Dashboard and Command Centre are each missing only a manifest. Command Centre's Session Threads tab reads `+/`, which the host refuses.
- Seven artifacts read Linear, Slack, Microsoft 365, a calendar, `mcp-git-audit` or `mcp-housekeeping-claude`. The portable interface answers only `mcp-ki-kb-fs` reads, so none of these seven can be shown through it.
- No scheduled task, launch agent or generator refreshes any artifact; each pair reads its data live when opened. The local Cowork artifact and scheduled folders are empty, so the `artifact_path` targets in the legal recipes are gone from this machine. I opened no private Claude content.
- Wrote [live-artifacts.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/design/live-artifacts.md). It has the inventory, a proposal in four waves plus retire and leave lists, and an embedded Mermaid diagram.
- Committed it as `4c338f0` by explicit path. Fetch passed, the pre-commit lint and repository audit passed, and I pushed fast-forward because it was the only commit stacked on `origin/main`.
- Limitation: no Mermaid renderer is installed locally, so I checked the diagram's syntax by eye only.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Any approved step lands in the repository that owns the artifact: manifests in `legal-principal` and `hnr-principal`, and the Estate and Housekeeping Instruments in `apps-observatory.local`. No records were captured.
- The run left alone two untracked files from other sessions in `ki-principal`: `+/_WORK/ki.chezmoi/mark-tidy-current.report.md` and `+/_WORK/ki.tools-burndown/briefs/mark-tidy.md`.

## Queries

### OBS-ARTIFACTS-ORDER - Approve the order for bringing live artifacts into the Observatory

**Context:** There are four waves.

- **Wave 1 needs no product work.** Keep HNR Council and Legal Activity Status as they are. Add manifests to Legal Hearing Dashboard and Command Centre, dropping Command Centre's threads tab because Sessions covers threads. Retire Kit Git Repo Audit, which Repositories duplicates and which still scans the old workspace roots, and the Tower recipe, which is already archived.
- **Wave 2** absorbs Estate Map and Estate Targets as the first new Instrument, following on from ESTATE-MAP-OBSERVATORY on 16 October.
- **Wave 3** folds HNR Streams Tracker into Sessions and Roadmap.
- **Wave 4** absorbs Kit Claude Housekeeping as a this-machine Instrument.

The five Cowork artifacts that need a provider connector or an LLM stay in Cowork: Email Pulse, Architecture Tracker, Linear Open Issues, Slack Digest and Week at a Glance. GitHub Organisation Management stays where it is, and so do the rig and tower sites.

**Query:** Do you approve this order, so each owning repository can be handed its first step?

**Options:** a) (recommended, confidence medium - Wave 1 rests on directly checked manifests and tool calls, but the Estate read-back and the HNR Streams pipeline mapping are still undesigned) Approve all four waves as proposed. Send Wave 1 as handoffs to `legal-principal`, `personal-principal` and `hnr-principal`, and the Estate Instrument to `apps-observatory.local` as the Project's next unit. b) Approve Wave 1 only, and decide Waves 2 to 4 once the Sessions token work has landed. c) Keep Command Centre's Session Threads tab: first extend the host to allow governed `+/_WORK` reads, then add the manifest.
