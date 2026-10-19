# ki.mac-studio-setup queries

## Open

### SOL-FW-TEST - What this parked tag meant

since 2026-10-19 · reviewed by query-review, 19:48 BST, which disagrees with the coordinator

**Context:** First seen in `4352cecc` among parked tags in the old checkpoint, with no definition; its text is lost. The same checkpoint separately calls for a sol firewall test with a NordVPN check, which the archived firewall-deliver report specifies under KI-TOOL-RIG-CORE-047 (awaiting review). The sol firewall test stays held for sol's screen either way.

**Query:** Is SOL-FW-TEST only the held sol firewall test, NordVPN check included, or something else still open?

**Options:**

a) (recommended by the reviewer, confidence high - the wording is lost, and keeping the tag avoids silently dropping a separate requirement; the coordinator recommended b at low) Kris restates or confirms it; keep the entry until then.

b) Treat it as the held sol firewall test with its NordVPN check, and delete the separate entry.

### BOOTOUT-GUARD - Guard every bootout site against an empty label

since 2026-10-19 · rig-capture run report, 23:31 BST · reviewed by bootout-review, 23:34 BST, which agrees

**Context:** An empty-label `launchctl bootout system/` shut terra down at 21:07 on 19 October during a hand-run rehearsal. Rig has three bootout sites, `rig_firewall_apply`, `rig_firewall_retire` and `rig_launchd_unload`; none checks its label itself, each relying on validation earlier in the call chain, and native firewall retirement does not enforce its own preflight. The normal commands are safe today, and no test bypasses the earlier checks. KI-TOOL-RIG-CORE-047 is awaiting review, and the launchd site lies outside its firewall scope.

**Query:** Capture a separate tools-rig record that refuses an empty or invalid label at all three bootout sites?

**Options:**

a) (recommended, confidence high - reviewed; all three missing local checks verified directly, and a Triage record is reversible) Capture a Triage record for a local refusal at each site, before any other side effect, with a fixture test each that bypasses earlier validation and proves refusal with no native change.

b) Capture nothing; accept reliance on the earlier checks.

c) Fold the guards into KI-TOOL-RIG-CORE-047 when it is next planned.

## Parked

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
