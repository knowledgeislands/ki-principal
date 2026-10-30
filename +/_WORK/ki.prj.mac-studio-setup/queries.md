# ki.prj.mac-studio-setup queries

## Open

### RIG-069-PROBE - Native setter evidence for KI-TOOL-RIG-CORE-069

since 2026-10-30 · from plan069.report.md

**Context:** KI-TOOL-RIG-CORE-069 is planned but stays draft: terra proved the legacy setter can assign the dynamic TOML type, but sol's recorded -50 failure happens before the confirmation helper runs, and read-only inspection cannot choose between legacy success with consent, a different identifier, or the NSWorkspace setter. Only an attended probe at sol's screen settles it.

**Query:** Will Kris attend the bounded sol probe (rungs `legacy`, `modern`, `workspace`, with `observe` after each, restoring Warp if needed) so the route can be settled and the plan approved to Ready?

**Options:**

a) (recommended, confidence high - attended sol evidence is the one missing fact) Keep KI-TOOL-RIG-CORE-069 draft and arrange the probe with Kris at sol's screen, then approve Ready on its results.

b) Defer the probe; the record stays draft and sol's TOML hold remains.

### RIG-INTAKE - What happens to the nine retained Rig capability lines

since 2026-10-30 · from rig-intake.report.md (per-line table there) · blind review intake-review agreed (high)

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
- **`RIG-TRIAGE`** - the rest of the Rig dispositions, kept in full below.

### RIG-TRIAGE - Where the remaining Rig records go

since 2026-10-20 · rig-triage and triage-review run reports, 00:24 BST, with CANCEL-MERGE from ki.tools-burndown's acceptrig folded in · the review disagreed with both proposals in places, so all three views are shown

**Context:** Eight tools-rig records are undecided: KI-TOOL-RIG-CORE-053 (report-only menu-bar declarations), KI-TOOL-RIG-CORE-056 (finding out how menu-bar order persists), KI-TOOL-RIG-CORE-057 (GitHub Desktop repository list), KI-TOOL-RIG-CORE-064 (scan for unmanaged configuration), KI-TOOL-RIG-CORE-067 (package managers as catalogue tools), KI-TOOL-RIG-CORE-068 (a replaced pf root ruleset can bypass the firewall), KI-TOOL-RIG-CORE-069 (dynamic-type handler fallback) and KI-TOOL-RIG-DIST-011 (stale Rig link on vega). The blind review found DIST-011 not repaired and its hold now lifted by the approved Techne Programme Focus, whose record KI-PRINCIPAL-GOV-035 still awaits review; it found 056's outcome deliberately separate from 053's.

**Query:** Which disposition package should tools-rig apply?

Taken overnight under OVERNIGHT, where rig-triage and the review agree: 053 and 067 to Next, 068 to Now for planning only, 069 to Now for diagnosis and planning, 056 left in Future. Still open: the 057 and 064 handoffs and DIST-011.

**Options:**

a) (recommended by triage-review, confidence medium - the technical boundaries are clear, but the two new owners have to acknowledge their handoffs) Next for 053 and 067; 056 stays in Future; 057 handed to tools-mgit and 064 to ki.chezmoi, keeping the requests; Now for planning 068 (implementation waits for the attended NordVPN check and a tested restore path) and for diagnosing and planning 069; DIST-011 kept and released to Next, with ki.agent-host running anything on the host once GOV-035's review is settled.

b) (rig-triage) Next for 053 and 067; 057 and 064 to Future in Rig; 068 to Next, plan only; 069 to Now after a live handler check at sol; 056 and DIST-011 unchanged.

c) (acceptrig) Cancel DIST-011 as obsolete, merge 056 into 053, and reject 057 and 064 from Rig.

Parked at the 2026-10-18 hold (Kris; put back one at a time, with a recommendation and reason):

- **`ADOBE-DATA`** - about 8 GB of leftover Adobe data on sol, including the Lightroom catalogue. Recommended: keep the catalogue and delete the rest at a sol screen session (it needs sudo). Not deleted on Kris's broad "get rid of everything".

Parked by Kris on 14 October; each block below is copied from its retired report, its Summary, Need from you and Recommendation given as Context, Query and option a), and any other option taken from its reply line.

### FW-LIVE - Confirm terra's pf anchor is loaded

since 2026-10-14 · from terra-read.report.md (FW-VERIFY) in the run state folder's `archive/` · (looks resolved: the decisions log records FW-VERIFY on 15 October, terra's rules proven loaded; the reboot check is held in `state.md`; the worker judges)

**Context:** Reading the live pf rules needs sudo, which this run did not have. Everything around the rules is in place: the daemon ran once with exit 0 and the anchor file holds the tailnet-only rules. FW-LIVE needs proof that the rules are actually loaded. The check below is read-only.

**Query:** Will Kris run the read-only check at terra's screen?

**Options:**

a) (recommended) At terra's screen, run `sudo pfctl -s info | head -3`, then `sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules`. Paste the output into the thread. Expect `Status: Enabled` and eight rules on port 5900.

b) Accept the indirect evidence and close FW-LIVE on it.

### UE-089-SHAPE - Sanity-check the channel model

since 2026-10-14 · from records.report.md in the run state folder's `archive/`

**Context:** the three open questions in the record: whether the channel needs its own `kiChannel` value or should just follow from `rigProfile`; whether the sync runs daily before `rig-update` or more often; and whether it should also pull the two Harness checkouts that local mode reads live.

**Query:** confirm the model or change it before anyone plans the record.

**Options:**

a) (recommended) keep `kiChannel` as its own value, run the sync daily before `rig-update`, and include the Harness checkouts.

b) change - <notes>

### OLD-ORPHANS - Four old repositories that exist only on sol now

since 2026-10-14 · from old-trees.report.md in the run state folder's `archive/`

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

### MGIT-PRESEED - Rescue the unfinished mgit repair change

since 2026-10-14 · from old-trees.report.md in the run state folder's `archive/`

**Context:** sol's old `tools-mgit` has an uncommitted change from 31 July. It makes `mgit repair` clone into a folder that holds only its `mgit` config file, which is the case that blocked `hnr-principal` on sol. The current `tools-mgit` doesn't have it. The patch is saved at [old-trees.tools-mgit-preseeded.patch](/Users/krisbrown/.local/state/ki/agents/mac-studio-bootstrap/old-trees.tools-mgit-preseeded.patch). It was written against a version 203 commits older, so it won't apply cleanly.

**Query:** decide whether to carry it forward.

**Options:**

a) (recommended) have a run capture a triage record in `tools-mgit` on the laptop that cites the patch and the sol outage. Then plan and rework it on the current code through the normal roadmap, not by applying the old diff directly.

b) drop it

### SOL-SOURCES - OneDrive source stores are missing on sol

since 2026-10-14 · from old-trees.report.md in the run state folder's `archive/`

**Context:** the laptop has `~/Library/CloudStorage/OneDrive-Personal/sources-<group>` for all eight groups, which repositories use for material that doesn't belong in Git. sol is signed in to OneDrive-Personal but has none of these folders. They are probably not chosen for sync or not downloaded yet.

**Query:** turn on sync for those folders in OneDrive on sol, or say if sol shouldn't have them.

**Options:**

a) (recommended) in OneDrive on sol, make at least `sources-knowledge-islands` and `sources-humans-not-robots` available, plus the five kit-group stores (personal, legal, techmedix, valle-armonia, equal-remedy). A later `rig doctor` run can confirm the paths. Only you can do this in the app.

b) sol doesn't need them - <notes>

### SOL-HNR-HARNESS - The HNR Harness isn't installed on sol

since 2026-10-14 · from sol-build.report.md in the run state folder's `archive/`

**Context:** `ki dev local on humansnotrobots/hnr-agentic-harness` failed with "installed harness … must be a directory". The HNR Harness has never been installed on sol. The Homebrew `ki` 0.10.1 reported it missing in `ki doctor` before this run too. Installing it means a `ki bootstrap`, which downloads the verified archive, and that is outside this run's remote exception. ki has since also dropped it from sol's Harness list.

**Query:** decide whether sol should carry the HNR Harness.

**Options:**

a) (recommended) yes, to match terra. A short run, allowed the download, would run `ki bootstrap` for the HNR Harness and then `ki dev local on humansnotrobots/hnr-agentic-harness`. Do it after the chezmoi local-mode work, so the config file is settled once.

b) leave off sol - <notes>

### SOL-WHATSAPP - The WhatsApp MCP server can't start on sol

since 2026-10-14 · from sol-build.report.md in the run state folder's `archive/`

**Context:** the server builds, but sol has no WhatsApp linked-device credentials or spool folder, so it closes on start. Pairing a linked device is a credential step done by a person.

**Query:** decide whether sol should acquire WhatsApp at all.

**Options:**

a) (recommended) keep WhatsApp acquisition on terra only, and remove `kb-mcp-acquire-whatsapp` from sol's mcporter config through the chezmoi MCP inventory. If you want it on sol too, pair a linked device there yourself.

b) I'll pair sol - <notes>

### SOL-KI-CONFIG-DRIFT - ki rewrote a chezmoi-managed file on sol

since 2026-10-14 · from sol-build.report.md in the run state folder's `archive/` · (the `ki-pmo-design` part looks resolved by SKILLS-CONFIG on 14 October; the worker judges)

**Context:** after `ki dev local on`, sol's `~/.config/ki/config.toml` no longer lists the HNR Harness or `ki-design-loop`, so it differs from the chezmoi source. The `ki-design-loop` skill links on both Macs point at nothing since the Harness renamed it to `ki-pmo-design`.

**Query:** choose who brings the chezmoi source up to date.

**Options:**

a) (recommended) fold it into the "Local mode for KI tools on the Macs" chezmoi work (LOCAL-RECORD): update the source for the `ki-pmo-design` rename, and review `chezmoi diff` on sol before any apply.

b) separate fix - <notes>

### C56-TICK - Tick C5 and C6 in the record

since 2026-10-15 · from [ue086-walk](ue086-walk.report.md) · parked 2026-10-29 at the baseline finish; release: when Kris resumes the Mac Studio walk

**Context:** this run was asked to tick only the steps it walked. C5 (Google Drive through the `google-drive` cask) and C6 (Home Assistant from the App Store, 1099568401) are verified done on `sol`, with Rig reporting both present, but they are still unticked in [PERSONAL-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-086-finish-software-alignment.md).

**Query:** may an agent tick them?

**Options:** a) (recommended) an agent ticks C5 and C6 with today's evidence and commits only the record, locally; b) leave them until the full C9 check.

### C8-WORDING - C8 still expects Keynote, Numbers and Pages "present"

since 2026-10-15 · from [ue086-walk](ue086-walk.report.md) · parked 2026-10-29 at the baseline finish; release: when Kris resumes the Mac Studio walk

**Context:** step A8 deliberately left Keynote, Numbers and Pages catalogue-only, because `mas info` cannot resolve their App Store numbers. Rig therefore shows them as catalogue-only, never as present, so C8 as written can never pass. DaVinci Resolve is present through `mas`, with no route variant.

**Query:** should C8 be reworded to match A8?

**Options:** a) (recommended) an agent rewords C8 to expect Keynote, Numbers and Pages as catalogue-only and DaVinci Resolve as present, keeps the Adobe check that follows C7i, and commits only the record, locally; b) leave C8 as written and judge it by hand at C9.
