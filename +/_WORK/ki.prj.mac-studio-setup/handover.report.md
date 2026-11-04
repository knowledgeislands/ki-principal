# [Rig](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › handover

**🤖 → 👤 Handoff to supervisor · Run report at 15:33 GMT · last mark 02:10 BST (20 October)**

---

## Done

- Took stock of every item in [ki.prj.mac-studio-setup](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/work.md), read-only, against tools-rig, chezmoi, State of play, the household works and sol's live state (`rig doctor`, `ki doctor`, OneDrive folders, installed apps, SSH). No machine changes were made.
- Wrote the [handover note](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/setup/handover.md): every query, state line, retained Rig line and `setup/` file, each with a verdict and, where not settled, who takes it. Committed in ki-principal as `3ba594a3`; `rumdl` clean.
- Handed over by message line, committed in the chezmoi source as `bf21b31a`:
  - [personal.reg.household-sol](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-sol/messages.md), the main receiver under PS-STUDIO, gets everything at sol: the rest of [PERSONAL-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-086-finish-software-alignment.md) (C4, C7a, C7b, C7d to C7h, C8, C9), ADOBE-DATA, UTM-SOL, sol's firewall re-apply under [KI-TOOL-RIG-CORE-047](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md), the attended RIG-069-PROBE, SOL-WHATSAPP, ZED-MD, the leftover `~/.ssh/config.pre-ue088`, the Headroom favicon drawing, and two new sol findings.
  - [personal.reg.household-terra](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-terra/messages.md) gets terra's items: confirming HOSTKEY-APPLY and key-only SSH on terra, the FW-LIVE check after a restart, the NordVPN check when Kris asks, and word that its GUIDE-FIELD and RIG-RETIRE-ONE asks are still with Kris as RIG-ASKS.
- One departure from the brief: personal.reg.rig-terra no longer exists in personal-principal. Under HOUSEHOLD-NAMES it became personal.reg.household-terra, and household-sol moved with it, so both lines went to their packages in the chezmoi source. Nothing was written in personal-principal. chezmoi's gate: `node --test` and `rumdl` pass; `ki repo audit` fails only on the three older `TAKEN` lines already in household-sol's `messages.md`, not on the new lines.
- Settled and can be closed: RIG-TRIAGE (every record done, cancelled or moved to ideas), FW-LIVE, SOL-SOURCES (all source folders on sol), SOL-HNR-HARNESS (installed), SOL-KI-CONFIG-DRIFT, C56-TICK and C8-WORDING (both already in UE-086), OBS-RESTART (the Observatory is running), key-only SSH on sol (drop-in installed) with KEYONLY-SKIP-EXIT, terra's firewall re-apply, FW-LINUX-LIVE ([KI-TOOL-RIG-CORE-051 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/06da52aec5de300f03386efbdb637af1873c18d0/docs/roadmap/KI-TOOL-RIG-CORE-051-linux-tailnet-only-firewall.md) done), RIG-REMINDER-DOCTOR, REPORTS-MOVED; WAKE-SUBSTRATE is superseded by household-sol's host loop.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The package's own `state.md`, `discussions.md`, `messages.md` and `decisions.md` are untouched, as the brief required. The coordinator puts the work on hold and, at close-out, forwards the retained Rig lines to whoever takes the tools-rig lane.
- Still with Kris in their existing homes, unchanged by this run: RIG-INTAKE, RIG-ASKS, RIG-069-PROBE and PLAN068-VERIFY-GRANT, PLAN068-UNPRIV and PLAN068-READY in this package's [discussions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/discussions.md); OLD-ORPHANS and ADOBE-SCRIPT-HOME in [ki.sop.main discussions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/discussions.md); spec-sched needs a new go (it never ran); UE-089-SHAPE goes to ki.prj.chezmoi; [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) awaits Kris's acceptance.
- household-sol's queue says Kris is making assistant-terra his liaison so terra can be shut down. If terra goes, household-terra's handed items fall away with it.

## Queries

### TOOLS-RIG-LANE - Who carries the Rig tooling work once Mac Studio setup closes

**Context:** On 17 October Kris gave this work the tools-rig lane (RIG-OWNER). The household works that take over Mac Studio setup exclude Rig tooling changes, and no other work names tools-rig. Left over without an owner: four open records ([KI-TOOL-RIG-CORE-047](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md), [KI-TOOL-RIG-CORE-068](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md), [KI-TOOL-RIG-CORE-069](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md), [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md)), two newer triage records ([KI-TOOL-RIG-CORE-075](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-075-restart-services-after-upgrade.md), [KI-TOOL-RIG-CORE-076](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-076-host-defaults-and-power.md)), the RIG-INTAKE and RIG-ASKS captures, and the spec-sched request from ki.prj.observatory. On 1 November Kris said Knowledge Islands' method work goes to State of play ([ki.sop.main](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/state.md)) when a work closes (PS-METHOD-HOME). This query has not been blind reviewed, because this run cannot launch a reviewer.

**Query:** Which work should carry the tools-rig lane after Mac Studio setup closes?

**Options:**

a) (recommended, confidence medium - it follows Kris's PS-METHOD-HOME pattern for closing KI work and keeps Rig tooling apart from the household works, but Kris has not said so for tools-rig) State of play (ki.sop.main) holds the lane, receives the retained Rig lines at close-out, and dispatches tools-rig work until Kris opens a dedicated Rig work.

b) ki.prj.tools-burndown takes tools-rig alongside tools-ki and tools-mgit.

c) personal.reg.household-sol takes Rig tooling too, widening its scope.

### MGIT-PRESEED - The unfinished `mgit repair` change may be lost

**Context:** Parked since 14 October: sol's old `tools-mgit` held an uncommitted 31 July change that lets `mgit repair` clone into a folder holding only its `mgit` config file, the case that once blocked `hnr-principal` on sol. The saved patch is no longer at its cited path (`~/.local/state/ki/agents/mac-studio-bootstrap/`), and no tools-mgit record cites it. Since then every checkout was rebuilt in the move to `~/kis` (31 October to 1 November). This query has not been blind reviewed.

**Query:** Should the idea be carried forward without the patch, or dropped?

**Options:**

a) (recommended, confidence medium - the patch is gone and no failure has been seen since the rebuild, so a record would rest on memory alone) Drop MGIT-PRESEED, and raise it again only if `mgit repair` fails that way.

b) Have ki.prj.tools-burndown capture a tools-mgit triage record from the description above.

### 🤖 → 👤 Handoff to supervisor · since 15:33 GMT

👤 2 with you

- [with you] TOOLS-RIG-LANE · owner · since 15:33
- [with you] MGIT-PRESEED · owner · since 15:33

🧵 ki.prj.mac-studio-setup
