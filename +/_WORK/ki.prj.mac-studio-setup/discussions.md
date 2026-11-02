# ki.prj.mac-studio-setup discussions

## Open

### TOOLS-RIG-LANE - Who carries the Rig tooling work once Mac Studio setup closes

since 2026-11-02 · from handover.report.md · blind review pending

**Context:** On 17 October Kris gave this work the tools-rig lane (RIG-OWNER). The household works taking over Mac Studio setup exclude Rig tooling changes, and no other work names tools-rig. Left without an owner: KI-TOOL-RIG-CORE-047, 068, 069 and 070, the newer triage records KI-TOOL-RIG-CORE-075 and 076, the RIG-INTAKE and RIG-ASKS captures, and spec-sched from ki.prj.observatory. On 1 November Kris said Knowledge Islands' method work goes to State of play (ki.sop.main) when a work closes (PS-METHOD-HOME).

**Query:** Which work should carry the tools-rig lane after Mac Studio setup closes?

**Options:**

a) (recommended, confidence medium - follows Kris's PS-METHOD-HOME pattern and keeps Rig tooling apart from the household works, but Kris has not said so for tools-rig) State of play holds the lane, receives the retained Rig lines at close-out, and dispatches tools-rig work until Kris opens a dedicated Rig work.

b) ki.prj.tools-burndown takes tools-rig alongside tools-ki and tools-mgit.

c) personal.reg.household-sol takes Rig tooling too, widening its scope.

### MGIT-PRESEED - The unfinished mgit repair change may be lost

since 2026-11-02 · from handover.report.md (supersedes the 14 October parked query) · blind review pending

**Context:** sol's old tools-mgit held an uncommitted 31 July change letting `mgit repair` clone into a folder holding only its mgit config file, the case that once blocked hnr-principal on sol. The saved patch is no longer at its cited path, no tools-mgit record cites it, and every checkout was rebuilt in the move to `~/kis` on 31 October to 1 November with no such failure seen.

**Query:** Should the idea be carried forward without the patch, or dropped?

**Options:**

a) (recommended, confidence medium - the patch is gone and no failure has been seen since the rebuild) Drop it, and raise it again only if `mgit repair` fails that way.

b) Have ki.prj.tools-burndown capture a tools-mgit triage record from the description above.

### RIG-069-PROBE - Native setter evidence for KI-TOOL-RIG-CORE-069

focus: setup · since 2026-10-30 · from plan069.report.md

**Context:** KI-TOOL-RIG-CORE-069 is planned but stays draft: terra proved the legacy setter can assign the dynamic TOML type, but sol's recorded -50 failure happens before the confirmation helper runs, and read-only inspection cannot choose between legacy success with consent, a different identifier, or the NSWorkspace setter. Only an attended probe at sol's screen settles it.

**Query:** Will Kris attend the bounded sol probe (rungs `legacy`, `modern`, `workspace`, with `observe` after each, restoring Warp if needed) so the route can be settled and the plan approved to Ready?

**Options:**

a) (recommended, confidence high - attended sol evidence is the one missing fact) Keep KI-TOOL-RIG-CORE-069 draft and arrange the probe with Kris at sol's screen, then approve Ready on its results.

b) Defer the probe; the record stays draft and sol's TOML hold remains.

### RIG-ASKS - Two new Rig asks from terra

focus: setup · since 2026-10-31 · from personal.reg.rig-terra messages GUIDE-FIELD and RIG-RETIRE-ONE

**Context:** Two more Rig requests arrived on 31 October, both sent at Kris's own request. GUIDE-FIELD: Kris wants each tool's guide "managed in Rig as well"; Rig has no guide field and rejects unknown fields, so the proposal is an optional `guide` link on a tool, shown in Rig's tool description and kept off the public site unless separately agreed, first used for the chezmoi modern-tools guide (eza, fd, bat). RIG-RETIRE-ONE: retiring one switched-off service (Paperclip's leftover launch file on terra) today means reconciling all eight live services at once; the ask is a way to retire one stale resource on its own. The 19 October capture rule admits items Kris asked for, the same ground RIG-INTAKE's recommended option uses.

**Query:** Should both be captured as unadopted tools-rig triage records alongside the RIG-INTAKE captures?

**Options:**

a) (recommended, confidence high - both are Kris's explicit asks, which the capture rule admits, and capture adopts nothing) Capture both as unadopted tools-rig triage records in the same run as the RIG-INTAKE captures, keeping each message's wording and provenance.

b) Hold both as `_IDEAS.md` bullets in tools-rig until the roadmap burn-down allows new records.

### RIG-INTAKE - What happens to the nine retained Rig capability lines

focus: setup · since 2026-10-30 · from rig-intake.report.md (per-line table there) · blind review intake-review agreed (high)

**Context:** Nine lines (eleven bullets) have waited in this package since 29 October. On 14 October Kris set BURN-DOWN ("burn the roadmap down; no new feature records"). CAPTURE-GATE refined it on 19 October: capture only blockers, defects seen failing, or items Kris asked for, and put ideas in `_IDEAS.md`. Four lines carry Kris's own explicit asks: RIG-TUI, RIG-SSH-CHECK, RIG-COMMENT-KIND and the IMPORTANT RIG-APP-FOOTPRINT with its RIG-NOTIFICATIONS and RIG-MACHINE-MANAGEMENT companions. RIG-CLI-CONSISTENCY reports defects seen failing on sol. The footprint group's natural owner, KI-TOOL-RIG-CORE-072, was moved to ideas on 27 October, after those asks, when Kris bulk-approved the sweep's "defer to Later" bucket and asked for fewer things in the queue. The sweep did not have the footprint lines in front of it. WAKE-SUBSTRATE needs nothing new from Rig, since `scheduled-job` already makes the launchd job. chezmoi already covers RIG-REMINDER-DOCTOR.

**Query:** Should the lines be dispositioned as the table proposes: four triage captures, the footprint group held in the KI-TOOL-RIG-CORE-072 idea, and two returns?

**Options:**

a) (recommended, confidence high - reviewed: the blind review independently chose this course, since CAPTURE-GATE admits Kris's explicit asks and defects seen failing, and the 27 October deferral of KI-TOOL-RIG-CORE-072 stands until Kris brings it back) Capture four unadopted tools-rig triage records: RIG-TUI (a separate viewer over `rig status --json`, with this package's RIG-FULLSCREEN idea noted as the alternative shape, no in-core interface implied), RIG-SSH-CHECK, RIG-COMMENT-KIND, and one bounded RIG-CLI-CONSISTENCY record that keeps the ten-point evidence and separates real failures from intended contracts such as preview-by-default `rig remove`. Hold RIG-APP-FOOTPRINT, both RIG-NOTIFICATIONS lines and RIG-MACHINE-MANAGEMENT with the KI-TOOL-RIG-CORE-072 idea, their wording and provenance kept there and their fuller scope put to Kris whenever 072 is reconsidered. Return WAKE-SUBSTRATE to State of play (Rig's launchd calendar job already exists; the checker, its authority and deployment stay with the sender) and RIG-REMINDER-DOCTOR to its originating work with the evidence (chezmoi configures the hook and link) and the still-open question of who audits their health, not as "already satisfied".

b) Strict BURN-DOWN: capture only the two records Kris named as idea records, RIG-TUI and RIG-SSH-CHECK. Hold RIG-COMMENT-KIND and RIG-CLI-CONSISTENCY as `_IDEAS.md` bullets, and the footprint group in the KI-TOOL-RIG-CORE-072 idea. The returns stay as in a).

c) Honour the IMPORTANT footprint ask now: bring KI-TOOL-RIG-CORE-072 back from ideas as a triage record carrying the whole footprint group, split at planning, plus everything else in a).

## Parked

Parked at the 2026-10-20 hold (take stock on ways of working; put back one at a time when Kris says resume):

- **`PLAN068-VERIFY-GRANT`** - [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md): `apply --sudo` takes no grant and runs no root read when the firewall looks present, so a NordVPN-replaced root ruleset would never be checked. Recommended (high): count a selected `macos-pf` firewall as work for an explicit `--sudo`, and update RIG-ORCH-043, the ADR and the guide.
- **`PLAN068-UNPRIV`** - KI-TOOL-RIG-CORE-068: what doctor reports without privilege. Recommended (medium, blind review not yet run): keep `present` with `kernel-rules-unverified`, and say plainly that it never means the rules are evaluated.
- **`PLAN068-READY`** - KI-TOOL-RIG-CORE-068 is planned and still in draft. Recommended (medium, blind review not yet run): approve Ready, with `ki-implement` gated on Kris's attended NordVPN check (steps 2 to 4 matching, results pasted into the record).

Parked at the 2026-10-18 hold (Kris; put back one at a time, with a recommendation and reason):

- **`ADOBE-DATA`** - about 8 GB of leftover Adobe data on sol, including the Lightroom catalogue. Recommended: keep the catalogue and delete the rest at a sol screen session (it needs sudo). Not deleted on Kris's broad "get rid of everything".

Parked by Kris on 14 October; each block below is copied from its retired report, its Summary, Need from you and Recommendation given as Context, Query and option a), and any other option taken from its reply line.

### UE-089-SHAPE - Sanity-check the channel model

focus: setup · since 2026-10-14 · from records.report.md in the run state folder's `archive/`

**Context:** the three open questions in the record: whether the channel needs its own `kiChannel` value or should just follow from `rigProfile`; whether the sync runs daily before `rig-update` or more often; and whether it should also pull the two Harness checkouts that local mode reads live.

**Query:** confirm the model or change it before anyone plans the record.

**Options:**

a) (recommended) keep `kiChannel` as its own value, run the sync daily before `rig-update`, and include the Harness checkouts.

b) change - <notes>

### OLD-ORPHANS - Four old repositories that exist only on sol now

focus: setup · since 2026-10-14 · from old-trees.report.md in the run state folder's `archive/`

**Context:** GitHub no longer serves `5g-emerge/5g-emerge-resources`, `knowledgeislands/ki-techne-principal`, `knowledgeislands/ki-plugins` or `krisb/kit-openclaw-kitteth`, and the laptop has no copy of them. Files that exist nowhere else:

- 5g-emerge-resources: 4 decision records and about 10 KB of MS3 TVR alignment notes (hnr territory, last changed 29 May).
- ki-techne-principal: Architecture papers and a Techné v0.1 PDF. ki-principal records this repository as "archived read-only", but GitHub can't find it, and sol's copy predates revision `b25e9c9`, which ki-principal cites. That revision may now be lost.
- kit-openclaw-kitteth: a small OpenClaw agent workspace.
- ki-plugins: only older versions of files the harness has since replaced.

`kit-legal-old` is also gone from GitHub, but all of its files are in `legal-principal`, so it is under OLD-TREES.

**Query:** confirm that these deletions were intended, and choose where the last copies go.

**Options:**

a) (recommended) save each repository as a single Git bundle file in OneDrive: 5g-emerge-resources in `sources-humans-not-robots`, the other three in `sources-knowledge-islands`, each in an `_archive` folder. Then retire the checkouts. If `ki-techne-principal` should still be on GitHub as an archived repository, say so; restoring it there would be a separate push you would have to authorise.

b) restore <repo> on GitHub - <notes>

### SOL-WHATSAPP - The WhatsApp MCP server can't start on sol

focus: setup · since 2026-10-14 · from sol-build.report.md in the run state folder's `archive/`

**Context:** the server builds, but sol has no WhatsApp linked-device credentials or spool folder, so it closes on start. Pairing a linked device is a credential step done by a person.

**Query:** decide whether sol should acquire WhatsApp at all.

**Options:**

a) (recommended) keep WhatsApp acquisition on terra only, and remove `kb-mcp-acquire-whatsapp` from sol's mcporter config through the chezmoi MCP inventory. If you want it on sol too, pair a linked device there yourself.

b) I'll pair sol - <notes>
