# ki.ways-of-working queries

## Open

### FOOTER-PROVISIONALS - Confirm KI-TOOL-KI-CLI-134's three warning choices

**Context:** [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) (`--allow` launch grants) is awaiting review. Overnight its mistyped baseline was repaired (burn2-tools-ki, pushed), and accept4-tools-ki then passed it on technical and immutable-evidence review. It is held back from acceptance only because its Outstanding concerns reserve three choices for Kris: the marker and report-path fixes were delivered before the grants; a bare `<name>.report.md` gives no warning; and each differing report path is named once. All three are implemented and independently tested. burn-tools-ki also flagged the grant names `fetch` and `machine`, the `--allow` spelling and the grant order. These match the harness grant files and are no longer listed as concerns. GRANT-INTERIM waits on this acceptance.

**Query:** Do the three warning choices stand as implemented?

**Options:**

a) (recommended, confidence high - implemented and independently tested twice) Confirm all three; the record is then accepted under `ki-accept`, with a link preflight before pruning.

b) Say which choice changes; the record stays awaiting review until it is reworked.

**Review:** not needed; high confidence and not destructive.

### GRANT-INTERIM - Release `--allow` so the interim grant sentence can go

**Context:** Kris answered GRANT-INTERIM a) earlier: the interim sentence in `ki-delegation`'s Grants subsection ([background-run standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md), "until the launcher offers that option") is removed once a `ki` release carrying `--allow` is installed. The `ki` on `sol` runs the tools-ki source checkout directly, so it already offers `--allow`. No tagged release contains it, though: the latest is `v0.12.0`. A release is publication, so it is Kris's to authorise. It also follows FOOTER-PROVISIONALS and the acceptance of [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md). ki.tools-burndown already plans a patch release with KI-TOOL-KI-CLI-155 and the harness pin.

**Query:** Will Kris authorise a tools-ki release carrying `--allow` once KI-TOOL-KI-CLI-134 is accepted, so that the interim sentence can go?

**Options:**

a) (recommended, confidence medium - closes the interim cleanly, but the release also ships whatever else is on tools-ki `main`) Yes: fold it into ki.tools-burndown's planned patch release; once it is installed, a run removes the sentence.

b) Remove the sentence now, since `sol`'s `ki` already offers `--allow`, and release later.

c) Hold the release; the sentence stays.

**Review:** still needs a blind review (medium).

### OBS-ACT-VISUAL - Kris's own check of KI-OBSERVA-BRG-005

**Context:** [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) (the Act board's missing parts) is awaiting review. Its review packet reserves a live check for Kris at <http://127.0.0.1:1675/>: the repository-fetch and Rig-apply plan rows, meaning their scope, inputs and withheld-checkout rows, at 1,440 and 760 px. The overnight grant excludes acceptance wherever Kris's own eyes are needed. accept2-observatory accepted KI-OBSERVA-OPS-003 and KI-OBSERVA-VIS-027 alongside it.

**Query:** When does Kris make the live check of KI-OBSERVA-BRG-005?

**Options:**

a) (recommended, confidence high - the packet reserves the check for Kris) Kris checks this morning and reports the result to ki.observatory; the record stays awaiting review until then.

b) Return it to in progress if the check finds a defect.

**Review:** not needed; high confidence and not destructive.

### SITE-SOURCE - KI-WEBSITE-SITE-044's ki-design citation and visual checks

**Context:** [KI-WEBSITE-SITE-044](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) (adopt ki-design v1) passes every local gate (build, routes, provenance offline, 72 tests, audits) and is awaiting review. The Field Guide cites the `ki-design` repository as its symbol source. That repository is private, so readers cannot open the citation, and the [page-provenance guide](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/guides/developer/page-provenance.md) forbids inaccessible published citations. The visual checks of the home page, an inner page and the Field Guide at 1440 and 390 px, in both colour schemes, were not repeated after the last update. The two runs disagree. burn-website recommended accepting the citation as it stands and making ki-design public later (medium confidence). accept-website recommended keeping the record awaiting review until reader access is resolved (high confidence). The website has three unpushed commits from other sessions.

**Query:** Which remedy should KI-WEBSITE-SITE-044's ki-design citation take before acceptance?

**Options:**

a) (recommended, confidence medium - keeps the provenance guide whole, but whether ki-design goes public is Kris's publication call) The record stays awaiting review. Kris makes ki-design readable, or confirms it is to be, then makes the 1440 and 390 px checks in both schemes, and an acceptance review follows.

b) Return it to in progress for a site-local remedy that keeps attribution accurate without the private link, then a fresh review packet and Kris's visual checks.

c) Accept the citation as it stands and make ki-design public later; it breaks the provenance guide until then.

**Review:** still needs a blind review (medium; the runs disagree).

### OPS-014-RENDER - Kris's four client render checks for the GFM conversion

**Context:** [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) converted ki-principal to GitHub-flavoured Markdown and is awaiting review. Kris answered RENDER-CHECK a) at 05:20 ("Vendor check fine"), and gfm-answers applied the other three answers. Acceptance test 4 is still unticked and reserved for Kris. In each of GitHub, Obsidian, Zed and the Observatory, open the Library heading link and a representative alert. Check that the four plain images read well at natural size. Record each outcome in the record and decide each failure. The Observatory drops the heading fragment; that is to be recorded either as a navigation failure or as an accepted fallback.

**Query:** When does Kris run the four client render checks, and is the Observatory's dropped fragment a failure or an accepted fallback?

**Options:**

a) (recommended, confidence high - the packet reserves acceptance test 4 for Kris) Kris runs the four checks this morning, records the outcomes, accepts the Observatory's dropped fragment as a fallback, and the record then goes to acceptance.

b) Kris runs the checks and records the dropped fragment as a navigation failure, routed to ki.observatory before acceptance.

**Review:** not needed; high confidence and not destructive.

### SPEC-SKETCH - Correct the KIP lifecycle text sketch

**Context:** In [specification-process.md](/Users/krisbrown/workspaces/knowledge-islands/ki-specifications/docs/specification-process.md), the plain-text sketch below the lifecycle list reads `Draft -> Review -> Accepted -> Implemented -> Superseded`. Lifecycle step 8, `GOVERNANCE.md`, the old Mermaid diagram and the new Archify diagrams all say `Superseded` comes from `Accepted`, and `Implemented` is terminal. [KI-SPEC-RGV-004](/Users/krisbrown/workspaces/knowledge-islands/ki-specifications/docs/roadmap/KI-SPEC-RGV-004-archify-status-flow-diagrams.md) was accepted overnight (local, unpushed) without touching the text, which was out of its scope. accept2-specifications notes that both text sketches remain unchanged. It also notes a separate, unsettled inconsistency in the text: whether a KIP is Implemented at Draft publication or after implementation experience.

**Query:** Should the sketch be corrected to `Accepted -> Superseded`?

**Options:**

a) (recommended, confidence high - reviewed: accept-specifications agreed independently, and accept2-specifications concurred) Correct the text sketches to `Accepted -> Superseded` as an editorial patch fix.

b) Leave it as it is.

c) Allow `Implemented -> Superseded` too, and change the governance text through a KIP.

**Review:** already blind-reviewed by accept-specifications (Codex), which agreed with a).

### RIG-ATTENDED - Kris's attended Rig checks on sol and terra

**Context:** Four tools-rig records cannot move without Kris at the Macs:

- [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) (draft, Now). Its step 1 is Kris's native handler probe at `sol`'s screen: three rungs (`legacy`, `modern`, `workspace`) run in order, stopping at the first that makes Zed the TOML handler. It is a live change, and delivery is blocked on it.
- [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) (draft, Now; approved under TERRA-NORDVPN a) on 19 October). Its gate is the attended NordVPN check at `terra`'s console. The check writes pf and is connection-critical. The record carries a tested restore path, R, which is rehearsed at step 4 before NordVPN connects, and the trial stops if R fails.
- [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) (in progress). Both failed acceptance overnight. SHELL-HOOK fails because Bats runs in pre-commit, and that fix is with ki.tools-burndown as RIG-PRECOMMIT-BATS. They also need Kris's live apply on `terra` and then `sol`, the SSH-over-tailnet check, and the missing `terra` evidence, under [ADR-KI-TOOL-RIG-009](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-009-system-domain-resources-under-an-attended-grant.md)'s attended grant.

**Query:** When and in what order does Kris run the attended Rig checks?

**Options:**

a) (recommended, confidence high - follows each record's own gate and keeps the connection-critical step at a console with its rehearsed restore) Hold one attended session. Run KI-TOOL-RIG-CORE-069's probe on `sol` first. Next comes KI-TOOL-RIG-CORE-068's NordVPN check at `terra`'s console, with R rehearsed before it. Leave the live apply of KI-TOOL-RIG-CORE-047 and -062 until RIG-PRECOMMIT-BATS lands and both pass re-review.

b) Take them one at a time, whenever Kris is at each Mac.

c) Defer all four; they stay as they are.

**Review:** not needed; high confidence and not destructive (the scheduling follows the records' own gates).

### RIG-053-SHAPE - Observe-only shape of the macOS menu bar resource

**Context:** [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) is awaiting review (tools-rig `c55f2e9`, pushed; 611 tests pass). Rig can now declare a macOS menu bar layout and report unreadable, unplaced, visibility and order drift. Apply records the layout as skipped `observe-only` with a Command-drag reminder, never writes a preference and never fails. [ADR-KI-TOOL-RIG-006](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-006-declarative-operational-resources.md) gained a paragraph on observation-only layouts. The coordinator took PLAN053-MODEL and PLAN053-LOGIN at 06:53 under the overnight grant: drop the current-host scope, since macOS 27 keeps visibility and order in the user domain, and leave out login items, which need an Automation-consent prompt. It is Rig's first observe-only resource. Its acceptance also waits on SHELL-HOOK (RIG-PRECOMMIT-BATS).

**Query:** Is the observe-only shape right for Rig's first observe-only setup resource?

**Options:**

a) (recommended, confidence medium - apply never touches a preference macOS gives no safe way to write, but nothing like it exists yet) Accept the shape as delivered: skipped, with a reminder and no failure.

b) Have apply report drift as a non-failing warning.

c) Return it for a different contract.

**Review:** still needs a blind review (medium).

### PLAN067-READY - Design answers and Ready for KI-TOOL-RIG-CORE-067

**Context:** [KI-TOOL-RIG-CORE-067](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md) (package managers as catalogue tools; draft, Next; planned in `5908727`, pushed) has nine steps. It adds an optional `provides` field, manager edges derived from each binding, one finding per missing manager, a doctor managers block and an opt-in missing-provider check. Four design answers come before Ready. PLAN067-EDGES: derived edges sit beside hand-written ones (high). PLAN067-OPTIN: the missing-provider check runs only once a catalogue declares `provides` (high). PLAN067-MATRIX: keep the fixed deferral matrix as a fallback (medium, as it keeps two routes for a while). PLAN067-ADR: write ADR-KI-TOOL-RIG-011 (high). Every step is fixture-testable and touches no live manager, but the record is large and changes apply ordering.

**Query:** Should KI-TOOL-RIG-CORE-067's four recommended answers be taken and its plan approved to Ready?

**Options:**

a) (recommended, confidence medium - three answers are high, but MATRIX keeps two routes and the record changes apply ordering) Take EDGES, OPTIN, MATRIX and ADR a), and approve Ready.

b) Take the four answers but keep the record in draft.

c) Remove the matrix now (PLAN067-MATRIX b)), so that every deferral needs `provides`, then approve Ready.

**Review:** still needs a blind review (medium).

### TECHNE-006-REVIEW - Review the replanned guarded host commands

**Context:** [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) (draft, Next, null baseline) is the last open tools-techne record. Its 20 October replan replaces the teardown command with destructive rebuild and withdraw commands, guarded removal operations, a stop warning and `--now`, and status schemas and exits. The record says the plan stays draft until Kris reviews it. Delivery would be local and stubbed. The `destroy` parameter from KI-TOOL-TECHNE-CLI-009, accepted overnight, takes effect only when CLI-006 lands.

**Query:** Will Kris review CLI-006's Steps, Files touched and Verify so that a later run can deliver it?

**Options:**

a) (recommended, confidence high - only Kris's review unblocks it, and delivery is local and stubbed) Kris reviews the plan and releases it to Ready.

b) Leave it in Next until the agent-host work needs rebuild and withdraw.

**Review:** not needed; it asks for Kris's own review, and releasing to Ready follows that review.

### DESIGN-DISPOSITIONS - MAP-002 timing, stale records and sizes in ki-design

**Context:** burn-ki-design found ki-design's five open records unworkable without Kris, another repository or an attended check, and two of them stale. [KI-DESIGN-MAP-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-MAP-002-isometric-renderer.md) (draft, Next) asks for a Canvas 2D renderer drawing "from a tile set's atlas". No atlas format exists, and its Verify still renders Arcadia from the Modern set, though [GDR-KI-DESIGN-038](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-038-ancient-is-the-isometric-set.md) made Ancient the only isometric set. The open hex-terrain composition question in [OPEN.md](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/OPEN.md) may also replace the plinth model it would build on. [KI-DESIGN-TIL-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-TIL-002-ancient-tile-set.md) still names the closed KI-DESIGN-ART-001 as a blocker and leaves [KI-DESIGN-ART-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md) out of `blocked_by`. All five lack `size:`. The proposed sizes are ART-002 s, [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) m, ICO-001 s, MAP-002 l and TIL-002 xl.

**Query:** Should ki-design's stale records and missing sizes take the burn run's dispositions?

**Options:**

a) (recommended, confidence medium - MAP-002 built now would probably be rebuilt after the pilot; the rest is tidying) Put MAP-002 on hold behind composition Pilot 0, then replan it with an atlas format, Modern as the fixture and Ancient as the target. Replan TIL-002 so that only ART-002 blocks it, and put it on hold until that lands. Add the sizes in one `docs(roadmap)` commit, leaving ICO-001 alone until it is accepted.

b) Plan MAP-002 now on the plinth model, with a recording-context test and no frame-rate claim, and make the TIL-002 and size tidy as in a).

c) Cancel MAP-002 until the Ancient set exists, and make the TIL-002 and size tidy as in a).

**Review:** still needs a blind review (medium).

### DESIGN-ICONS - Kris's look at the KI-DESIGN-ICO-001 contact sheet

**Context:** [KI-DESIGN-ICO-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ICO-001-icon-seed-set.md) (icon seed set) is awaiting review. Its Verify ends "owner reviews drawings on contact sheet". There are five new glyphs, `realm`, `pillars`, `thriving`, `quiet` and `weathered`, bordered in brass on `/Users/krisbrown/workspaces/knowledge-islands/ki-design/packages/icons/contact-sheet.png`. The record's tests and lint pass.

**Query:** Do the five new glyphs on the contact sheet pass Kris's look?

**Options:**

a) (recommended, confidence high - the record's Verify reserves this look for Kris) Kris looks at the contact sheet; on a pass, an independent acceptance review accepts the record.

b) Kris names the glyphs to redraw, and the record goes back to in progress.

**Review:** not needed; high confidence and not destructive.

### TOOLS-KI-SHAPES - Homes for KI-TOOL-KI-CLI-140's checks and the work status views

**Context:** burn-tools-ki and burn2-tools-ki left tools-ki records that need Kris. [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) (Git-hygiene estate audit) has its dependencies landed. Its CLEAN-1 to CLEAN-7 criteria live in the harness `ki-git` catalogue as judgement items, and where the mechanical checks live is undecided. [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) (routing view) is promoted only once State of play confirms the form it reads. [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md) has open questions of its own: whether views carry full lines or keys, and whether `v1` is kept. KI-TOOL-KI-CLI-139 is parked in ki.tools-burndown as SRC-PLACEMENT. KI-TOOL-KI-CLI-157 is settled by VALIDATOR-HOME a). Both runs' recommendations below are medium.

**Query:** Should KI-TOOL-KI-CLI-140's checks live in the harness catalogue, and should KI-TOOL-KI-CLI-149 and -160 wait for State of play's form?

**Options:**

a) (recommended, confidence medium - the rubric already owns the criteria, and building the views first would pre-empt State of play) Make the CLEAN checks mechanical in the harness `ki-git` catalogue, with tools-ki composing them with `mgit overview --json`. ki.tools-burndown asks State of play for the form, then plans KI-TOOL-KI-CLI-160 as `--view routing` beside the text views, with KI-TOOL-KI-CLI-149 waiting alongside it.

b) Implement the CLEAN checks natively in tools-ki, and plan KI-TOOL-KI-CLI-149 and -160 now on provisional choices.

**Review:** still needs a blind review (medium).

## Parked

- NO-GATE (with PKGLESS-GATE) - project shape commit gate; Kris will come back to it. a) `ki repo audit --skill ki-repo` staged, check-only; review prefers widening KI-HARNESS-GOV-225.
