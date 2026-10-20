# ki.ways-of-working queries

## Open

### FOOTER-PROVISIONALS - Confirm KI-TOOL-KI-CLI-134's three warning choices

**Context:** [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) (`--allow` launch grants) is awaiting review. Overnight its mistyped baseline was repaired (burn2-tools-ki, pushed), and accept4-tools-ki then passed it on technical and immutable-evidence review. It is held back from acceptance only because its Outstanding concerns reserve three choices for Kris: the marker and report-path fixes were delivered before the grants; a bare `<name>.report.md` gives no warning; and each differing report path is named once. All three are implemented and independently tested. burn-tools-ki also flagged the grant names `fetch` and `machine`, the `--allow` spelling and the grant order. These match the harness grant files and are no longer listed as concerns. GRANT-INTERIM waits on this acceptance.

**Query:** Do the three warning choices stand as implemented?

**Options:**

a) (recommended, confidence high - implemented and independently tested twice) Confirm all three; the record is then accepted under `ki-accept`, with a link preflight before pruning.

b) Say which choice changes; the record stays awaiting review until it is reworked.

### GRANT-INTERIM - Release `--allow` so the interim grant sentence can go

**Context:** Kris answered GRANT-INTERIM a) earlier: the interim sentence in `ki-delegation`'s Grants subsection ([background-run standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md), "until the launcher offers that option") is removed once a `ki` release carrying `--allow` is installed. The `ki` on `sol` runs the tools-ki source checkout directly, so it already offers `--allow`. No tagged release contains it, though: the latest is `v0.12.0`. A release is publication, so it is Kris's to authorise. It also follows FOOTER-PROVISIONALS and the acceptance of [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md). ki.tools-burndown already plans a patch release with KI-TOOL-KI-CLI-155 and the harness pin.

**Query:** Will Kris authorise a tools-ki release carrying `--allow` once KI-TOOL-KI-CLI-134 is accepted, so that the interim sentence can go?

**Options:**

a) (recommended, confidence high - reviewed: the standard makes removal conditional on launcher support, and the agreed installed-release boundary is met by the planned release after acceptance; its complete release range still needs verification) Yes: fold it into ki.tools-burndown's planned patch release; once it is installed, a run removes the sentence.

b) Remove the sentence now, since `sol`'s `ki` already offers `--allow`, and release later.

c) Hold the release; the sentence stays.

### OBS-ACT-VISUAL - Kris's own check of KI-OBSERVA-BRG-005

**Context:** [KI-OBSERVA-BRG-005](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) (the Act board's missing parts) is awaiting review. Its review packet reserves a live check for Kris at <http://127.0.0.1:1675/>: the repository-fetch and Rig-apply plan rows, meaning their scope, inputs and withheld-checkout rows, at 1,440 and 760 px. The overnight grant excludes acceptance wherever Kris's own eyes are needed. accept2-observatory accepted KI-OBSERVA-OPS-003 and KI-OBSERVA-VIS-027 alongside it.

**Query:** When does Kris make the live check of KI-OBSERVA-BRG-005?

**Options:**

a) (recommended, confidence high - the packet reserves the check for Kris) Kris checks this morning and reports the result to ki.observatory; the record stays awaiting review until then.

b) Return it to in progress if the check finds a defect.

### SITE-SOURCE - KI-WEBSITE-SITE-044's ki-design citation and visual checks

**Context:** [KI-WEBSITE-SITE-044](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) (adopt ki-design v1) passes every local gate (build, routes, provenance offline, 72 tests, audits) and is awaiting review. The Field Guide cites the `ki-design` repository as its symbol source. That repository is private, so readers cannot open the citation, and the [page-provenance guide](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/guides/developer/page-provenance.md) forbids inaccessible published citations. The visual checks of the home page, an inner page and the Field Guide at 1440 and 390 px, in both colour schemes, were not repeated after the last update. The two runs disagree. burn-website recommended accepting the citation as it stands and making ki-design public later (medium confidence). accept-website recommended keeping the record awaiting review until reader access is resolved (high confidence). The website has three unpushed commits from other sessions. A conflicting source, [KI-DESIGN-ART-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md), says ki-design went public on 18 October. This local-only review cannot resolve anonymous access to the exact cited revision.

**Query:** Which remedy should KI-WEBSITE-SITE-044's ki-design citation take before acceptance?

**Options:**

a) (recommended, confidence medium - keeps the provenance guide whole, but whether ki-design goes public is Kris's publication call; blind review disagrees and prefers d), because access is disputed and a publication promise does not make the citation readable) The record stays awaiting review. Kris makes ki-design readable, or confirms it is to be, then makes the 1440 and 390 px checks in both schemes, and an acceptance review follows.

b) Return it to in progress for a site-local remedy that keeps attribution accurate without the private link, then a fresh review packet and Kris's visual checks.

c) Accept the citation as it stands and make ki-design public later; it breaks the provenance guide until then.

d) Blind review: first verify anonymous access to the exact cited source revision. If accessible, retain the accurate citation; otherwise return the record to in progress for an accessible site-local source that preserves attribution and immutable provenance. Complete the required visual checks and independent acceptance review afterwards. Reason: the records conflict about public access, and neither a future publication promise nor making the whole repository public is needed to establish a readable citation.

### OPS-014-RENDER - Kris's four client render checks for the GFM conversion

**Context:** [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) converted ki-principal to GitHub-flavoured Markdown and is awaiting review. Kris answered RENDER-CHECK a) at 05:20 ("Vendor check fine"), and gfm-answers applied the other three answers. Acceptance test 4 is still unticked and reserved for Kris. In each of GitHub, Obsidian, Zed and the Observatory, open the Library heading link and a representative alert. Check that the four plain images read well at natural size. Record each outcome in the record and decide each failure. The Observatory drops the heading fragment; that is to be recorded either as a navigation failure or as an accepted fallback.

**Query:** When does Kris run the four client render checks, and is the Observatory's dropped fragment a failure or an accepted fallback?

**Options:**

a) (recommended, confidence high - the packet reserves acceptance test 4 for Kris) Kris runs the four checks this morning, records the outcomes, accepts the Observatory's dropped fragment as a fallback, and the record then goes to acceptance.

b) Kris runs the checks and records the dropped fragment as a navigation failure, routed to ki.observatory before acceptance.

### SPEC-SKETCH - Correct the KIP lifecycle text sketch

**Context:** In [specification-process.md](/Users/krisbrown/workspaces/knowledge-islands/ki-specifications/docs/specification-process.md), the plain-text sketch below the lifecycle list reads `Draft -> Review -> Accepted -> Implemented -> Superseded`. Lifecycle step 8, `GOVERNANCE.md`, the old Mermaid diagram and the new Archify diagrams all say `Superseded` comes from `Accepted`, and `Implemented` is terminal. [KI-SPEC-RGV-004 (pruned)](https://github.com/knowledgeislands/ki-specifications/blob/8c3c2189971323697626b191db6c7e75d995b385/docs/roadmap/KI-SPEC-RGV-004-archify-status-flow-diagrams.md) was accepted overnight (local, unpushed) without touching the text, which was out of its scope. accept2-specifications notes that both text sketches remain unchanged. It also notes a separate, unsettled inconsistency in the text: whether a KIP is Implemented at Draft publication or after implementation experience.

**Query:** Should the sketch be corrected to `Accepted -> Superseded`?

**Options:**

a) (recommended, confidence high - reviewed: accept-specifications agreed independently, and accept2-specifications concurred) Correct the text sketches to `Accepted -> Superseded` as an editorial patch fix.

b) Leave it as it is.

c) Allow `Implemented -> Superseded` too, and change the governance text through a KIP.

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

### RIG-053-SHAPE - Observe-only shape of the macOS menu bar resource

**Context:** [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) is awaiting review (tools-rig `c55f2e9`, pushed; 611 tests pass). Rig can now declare a macOS menu bar layout and report unreadable, unplaced, visibility and order drift. Apply records the layout as skipped `observe-only` with a Command-drag reminder, never writes a preference and never fails. [ADR-KI-TOOL-RIG-006](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-006-declarative-operational-resources.md) gained a paragraph on observation-only layouts. The coordinator took PLAN053-MODEL and PLAN053-LOGIN at 06:53 under the overnight grant: drop the current-host scope, since macOS 27 keeps visibility and order in the user domain, and leave out login items, which need an Automation-consent prompt. It is Rig's first observe-only resource. Its acceptance also waits on SHELL-HOOK (RIG-PRECOMMIT-BATS).

**Query:** Is the observe-only shape right for Rig's first observe-only setup resource?

**Options:**

a) (recommended, confidence high - reviewed: the source explicitly skips observe-only apply with a Command-drag reminder, while status and doctor own drift reporting; fixtures cover no writes and no failure) Accept the shape as delivered: skipped, with a reminder and no failure.

b) Have apply report drift as a non-failing warning.

c) Return it for a different contract.

### PLAN067-READY - Design answers and Ready for KI-TOOL-RIG-CORE-067

**Context:** [KI-TOOL-RIG-CORE-067](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md) (package managers as catalogue tools; draft, Next; planned in `5908727`, pushed) has nine steps. It adds an optional `provides` field, manager edges derived from each binding, one finding per missing manager, a doctor managers block and an opt-in missing-provider check. Four design answers come before Ready. PLAN067-EDGES: derived edges sit beside hand-written ones (high). PLAN067-OPTIN: the missing-provider check runs only once a catalogue declares `provides` (high). PLAN067-MATRIX: keep the fixed deferral matrix as a fallback (medium, as it keeps two routes for a while). PLAN067-ADR: write ADR-KI-TOOL-RIG-011 (high). Every step is fixture-testable and touches no live manager, but the record is large and changes apply ordering.

**Query:** Should KI-TOOL-RIG-CORE-067's four recommended answers be taken and its plan approved to Ready?

**Options:**

a) (recommended, confidence high - reviewed: derived edges enter cycle detection, the opt-in and matrix fallback preserve existing configurations, and fixture gates cover ordering without installing a live manager) Take EDGES, OPTIN, MATRIX and ADR a), and approve Ready.

b) Take the four answers but keep the record in draft.

c) Remove the matrix now (PLAN067-MATRIX b)), so that every deferral needs `provides`, then approve Ready.

### TECHNE-006-REVIEW - Review the replanned guarded host commands

**Context:** [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) (draft, Next, null baseline) is the last open tools-techne record. Its 20 October replan replaces the teardown command with destructive rebuild and withdraw commands, guarded removal operations, a stop warning and `--now`, and status schemas and exits. The record says the plan stays draft until Kris reviews it. Delivery would be local and stubbed. The `destroy` parameter from KI-TOOL-TECHNE-CLI-009, accepted overnight, takes effect only when CLI-006 lands.

**Query:** Will Kris review CLI-006's Steps, Files touched and Verify so that a later run can deliver it?

**Options:**

a) (recommended, confidence high - only Kris's review unblocks it, and delivery is local and stubbed) Kris reviews the plan and releases it to Ready.

b) Leave it in Next until the agent-host work needs rebuild and withdraw.

### DESIGN-DISPOSITIONS - MAP-002 timing, stale records and sizes in ki-design

**Context:** burn-ki-design found ki-design's five open records unworkable without Kris, another repository or an attended check, and two of them stale. [KI-DESIGN-MAP-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-MAP-002-isometric-renderer.md) (draft, Next) asks for a Canvas 2D renderer drawing "from a tile set's atlas". No atlas format exists, and its Verify still renders Arcadia from the Modern set, though [GDR-KI-DESIGN-038](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-038-ancient-is-the-isometric-set.md) made Ancient the only isometric set. The open hex-terrain composition question in [OPEN.md](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/OPEN.md) may also replace the plinth model it would build on. [KI-DESIGN-TIL-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-TIL-002-ancient-tile-set.md) still names the closed KI-DESIGN-ART-001 as a blocker and leaves [KI-DESIGN-ART-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md) out of `blocked_by`. All five lack `size:`. The proposed sizes are ART-002 s, [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) m, ICO-001 s, MAP-002 l and TIL-002 xl.

**Query:** Should ki-design's stale records and missing sizes take the burn run's dispositions?

**Options:**

a) (recommended, confidence high - reviewed: the open composition pilot precedes renderer commitments, GDR-KI-DESIGN-038 retains Modern as a fixture, and licensing remains the live Ancient blocker; the proposed sizes fit the recorded scope) Put MAP-002 on hold behind composition Pilot 0, then replan it with an atlas format, Modern as the fixture and Ancient as the target. Replan TIL-002 so that only ART-002 blocks it, and put it on hold until that lands. Add the sizes in one `docs(roadmap)` commit, leaving ICO-001 alone until it is accepted.

b) Plan MAP-002 now on the plinth model, with a recording-context test and no frame-rate claim, and make the TIL-002 and size tidy as in a).

c) Cancel MAP-002 until the Ancient set exists, and make the TIL-002 and size tidy as in a).

### DESIGN-ICONS - Kris's look at the KI-DESIGN-ICO-001 contact sheet

**Context:** [KI-DESIGN-ICO-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ICO-001-icon-seed-set.md) (icon seed set) is awaiting review. Its Verify ends "owner reviews drawings on contact sheet". There are five new glyphs, `realm`, `pillars`, `thriving`, `quiet` and `weathered`, bordered in brass on `/Users/krisbrown/workspaces/knowledge-islands/ki-design/packages/icons/contact-sheet.png`. The record's tests and lint pass.

**Query:** Do the five new glyphs on the contact sheet pass Kris's look?

**Options:**

a) (recommended, confidence high - the record's Verify reserves this look for Kris) Kris looks at the contact sheet; on a pass, an independent acceptance review accepts the record.

b) Kris names the glyphs to redraw, and the record goes back to in progress.

### TOOLS-KI-SHAPES - Homes for KI-TOOL-KI-CLI-140's checks and the work status views

**Context:** burn-tools-ki and burn2-tools-ki left tools-ki records that need Kris. [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) (Git-hygiene estate audit) has its dependencies landed. Its CLEAN-1 to CLEAN-7 criteria live in the harness `ki-git` catalogue as judgement items, and where the mechanical checks live is undecided. [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) (routing view) is promoted only once State of play confirms the form it reads. [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md) has open questions of its own: whether views carry full lines or keys, and whether `v1` is kept. KI-TOOL-KI-CLI-139 is parked in ki.tools-burndown as SRC-PLACEMENT. KI-TOOL-KI-CLI-157 is settled by VALIDATOR-HOME a). Both runs' recommendations below are medium.

**Query:** Should KI-TOOL-KI-CLI-140's checks live in the harness catalogue, and should KI-TOOL-KI-CLI-149 and -160 wait for State of play's form?

**Options:**

a) (recommended, confidence high - reviewed: the harness catalogue owns CLEAN criteria and already names their evidence, tools-ki composes mgit facts, and the view records leave their form and compatibility unresolved) Make the CLEAN checks mechanical in the harness `ki-git` catalogue, with tools-ki composing them with `mgit overview --json`. ki.tools-burndown asks State of play for the form, then plans KI-TOOL-KI-CLI-160 as `--view routing` beside the text views, with KI-TOOL-KI-CLI-149 waiting alongside it.

b) Implement the CLEAN checks natively in tools-ki, and plan KI-TOOL-KI-CLI-149 and -160 now on provisional choices.

### GOV209-OWNER - Which skill owns the acquired-area scaffold

**Context:** [KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md) (draft, Next, not yet planned) gives each territory principal a `+/_ACQUIRED/` folder with a scaffold README, where the acquire port delivers whole packets, and adds receiver triage guidance to `ki-repo-kb`: file the packet, turn it into work, or park it. The record does not say which skill owns the scaffold. The repository rule is that a capability which owns a working-area subarea must require its exact README while that capability is declared, and restores the README through its own conform. If `ki-repo-kb` owned it, every knowledge base would carry the folder, not only the principals. `ki-repo-kb-principal` writes no scaffold today. Eight principals declare the `ki-repo-kb-principal` overlay and none of them has the folder yet, so under either owner all eight would fail audit until each is conformed. Acquire's dispatch guide already creates the folder on first delivery, so the scaffold is not a precondition for dispatch. Kris dropped the return route on 20 October, so the receiver writes nothing back to the port.

**Query:** Which skill should own the `+/_ACQUIRED/` scaffold, and should it be required in every principal or checked only once the folder exists?

**Options:**

a) (recommended, confidence medium - reviewed: principal-only delivery matches the overlay, and the repository rule requires declared specialist areas to retain an exact scaffold restored by their owner) Give the scaffold to `ki-repo-kb-principal`, require it while the overlay is declared and add conform support; put the receiver triage guidance in `ki-repo-kb`.

b) Check the scaffold only once `+/_ACQUIRED/` exists, which means amending the `ki-repo` rule on specialist subareas.

c) Give the scaffold to `ki-repo-kb` for every knowledge base.

### GOV225-CLOSE - Close the hook content-claims record

**Context:** [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) (draft, Next, ki.tools-burndown) makes each shape skill declare the lines it requires in a repository's committed Git hooks, so that the `ki` host can compose them. Kris's STRICTNESS-CONFORM decision settled its design: one canonical hook pair per shape and package presence, held as data in `ki-repo` and audited by exact comparison. Five of its six steps are done: the frame, each shape's block and content criterion, the standard text and the regenerated rubrics. The last step is to agree with Kris whether the record now closes. Writing the canonical hooks into repositories was always out of its scope and belongs to tools-ki's KI-TOOL-KI-CLI-165, which can now proceed against the published hooks. The record is still marked draft, so closing it means moving it to awaiting review for an acceptance review.

**Query:** Should KI-HARNESS-GOV-225 close now, leaving composition in repositories to KI-TOOL-KI-CLI-165 in tools-ki?

**Options:**

a) (recommended, confidence high - reviewed: canonical hook data, exact comparison and generated shape assets are present; repository composition is a separate delivery, and acceptance still needs its own review) Move it to awaiting review, then accept it after an independent review.

b) Keep it open until KI-TOOL-KI-CLI-165 lands in tools-ki.

### GOV189-SCOPE - Narrow the thread-move record to its decided slice

**Context:** [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) (draft, Next, Mac Studio Setup) adds to `ki-coordination` a procedure for moving coordinating work from one Mac to another, plus a level check at resume and at every mark with a `[behind]` banner item. Kris decided the level check and `[behind]` under SYNC-GUARD on 18 October, so that part could be delivered now. Two questions remain open. The first is how agents that must run on one host are handled: kept queued on the old host, carried with a host constraint, or treated as blocking the move. The second is which closing form the session left on the old host uses, since Kris's 14 October decision named the retired DONE frame and the work model keeps `Finished` for work that has ended. Exporting and re-importing the agent queue belongs to tools-ki, and until a command exists the standard can name the manual route of re-queuing briefs from the work package's Next steps. The record does not block the Mac Studio setup.

**Query:** Should KI-HARNESS-GOV-189 be narrowed to the decided level check and `[behind]` item, or wait until Kris answers both open questions?

**Options:**

a) (recommended, confidence medium - reviewed: SYNC-GUARD already settles the level check and banner item; host-bound queue handling and the old session's closing form remain explicit open questions) Narrow it to the level check and the `[behind]` item, and keep the two open questions in its Discussion for a later record.

b) Kris answers both questions now, so that the whole record can be planned.

### GOV202-ADOPT - Adopt the skill-area stats badge

**Context:** [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) is still in triage with no horizon, priority or size. It replaces the uninformative SRC badge on the ten skill-area diagrams with stable stats about each skill, such as its rubric rule count, a code-size bucket and its reference count, which Kris asked for on 14 October under SRC-BADGE. It is small. Planning still has to decide whether the badge comes from the harness generator or needs a change to the vendored viewer, and which stats are stable enough not to churn the diagrams. Nobody has judged its value against other work.

**Query:** Should KI-HARNESS-GOV-202 be adopted?

**Options:**

a) (recommended, confidence low - it is small, but its value has not been judged; blind review disagrees and prefers c), because adoption should follow a value comparison and a feasible implementation route) Adopt it to Next for a later burndown.

b) Cancel it.

c) Blind review: retain it in triage until a short comparison establishes its value against other work and a feasible route within the record's boundary. Reason: capture approved the idea without adopting it, no size or effort estimate supports the smallness claim, and the generator-versus-viewer question is unresolved.

### GOV227-SCHEMA - Design the repository storage schema

**Context:** [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md) (draft, Next, Observatory) adds a `ki-repo`-owned `.ki.toml` table in which a repository declares what each tool, MCP server or app it ships stores in its XDG config, data, cache and state folders, and why. Kris decided the owner under STORAGE-OWNER a) on 20 October. Its first step is to design the schema with Kris: entries per item, each XDG category with its purpose and whether the content is disposable, recoverable or the owner's knowledge, and a way to declare shared namespaces with their owners. The record cannot be planned until the schema exists. It blocks only the tool-storage phase of the Observatory's machine instrument.

**Query:** When should Kris design the storage-declaration schema for KI-HARNESS-GOV-227?

**Options:**

a) (recommended, confidence high - reviewed: the schema still needs explicit recoverability and shared-namespace ownership, the record requires owner co-design, and one Observatory phase depends on it) Hold a short design session in its own work.

b) Defer the record to Future.

### OPS009-SPLIT - Split the AI session acquisition record

**Context:** [KI-HARNESS-OPS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md) (draft, Next, Model theme) carries the eight unfinished steps of AI-session acquisition from the closed Knowledge acquisition Project. They run from ChatGPT project enumeration and explicit handling of missing or changed sessions, through receiver triage and separating Claude and Codex acquisition from housekeeping, to a fail-closed, owner-approved deletion manifest. Kris chose on 17 October to capture all eight as one record, and the record expects them to split at planning. Several steps touch sibling repositories, which must plan and accept their own parts. The harness-burn run could not split it because CAPTURE-GATE barred that run from creating records.

**Query:** Should KI-HARNESS-OPS-009 be split into separate records?

**Options:**

a) (recommended, confidence high - reviewed: the record anticipates a planning split across acquisition, receiver triage and source retirement; sibling delivery remains receiver-owned) Split it in a run that is allowed to capture records, with each sibling repository capturing its own part.

b) Leave it whole at Next.

### OBS-BRG-006-VISUAL - Your running-site check of KI-OBSERVA-BRG-006

**Context:** [KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md) (feedback writes to the work's messages.md) passed an independent Codex review on 20 October at 22:26 BST: tests, typecheck, Biome, audits and the browser smoke at 1,440 and 720 px all pass. Its Verify reserves a running-site look for you at 1,440 and 760 px on <http://127.0.0.1:1675/>, the same session as OBS-ACT-VISUAL. The Observatory service also needs a restart to pick up the delivery.

**Query:** Will you make the check alongside OBS-ACT-VISUAL?

**Options:**

a) (recommended, confidence high - every mechanical check passes; only your look remains) Yes: restart the Observatory, check both records in one sitting, and a pass accepts it.

b) Name a defect; the record returns to in progress.

### CALENDAR-LIBRARY - [KI-PRINCIPAL-MOD-008] is Calendar part of the Library?

**Context:** Structure, The Home of Knowledge and the website put Calendar inside the Library. [SDR-KI-PRINCIPAL-002](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/SDR-KI-PRINCIPAL-002-the-home-of-knowledge.md>) defines the Library as Pillars plus Resources, with Calendar beside it. Calendar entries are exempt from the Enactment record, but Structure says "Nothing enters the Library except through the governance process".

**Query:** Should Calendar sit inside the Library?

**Options:**

a) (recommended, confidence high - SDR-KI-PRINCIPAL-002 explicitly separates them; SDR-004 exempts Calendar entries.) **Blind review:** Follow [SDR-KI-PRINCIPAL-002](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/SDR-KI-PRINCIPAL-002-the-home-of-knowledge.md>), and move Calendar out of the Library in Structure, The Home of Knowledge and the website. Keep Calendar outside the Library; reserve Library for Pillars and Resources, and retain the Calendar exemption.

b) **Delivery run:** (recommended, confidence low - two notes and the website agree, but SDR-002 is the decision of record) Keep Calendar in the Library, state that it is appended by note-type convention rather than by proposal, and amend [SDR-KI-PRINCIPAL-002](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/SDR-KI-PRINCIPAL-002-the-home-of-knowledge.md>)'s wording.

### ENACTMENT-ADMIN - [KI-PRINCIPAL-MOD-008] does the portable gate cover Admin?

**Context:** Five places in the portable model say nothing enters Pillars or Resources without enactment, and none of them names Admin: Governance, Jurisdiction, the Model Enactment Process, Processes and the Great Library. [SDR-KI-PRINCIPAL-002](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/SDR-KI-PRINCIPAL-002-the-home-of-knowledge.md>) and the island's own Enactment Process include `Admin/`.

Independent scope check: the Great Library is specifically the name for `Pillars/`, not a portable gate listing every canonical zone. Its growth section should remain Pillars-only; Admin belongs in the portable KB gate statements. The existing bounded owner-instruction and trivial-change exemptions still apply.

**Query:** Should the portable gate statements name `Admin/` as well?

**Options:**

a) (recommended, confidence medium - this matches the island's practice and SDR-002) **reviewed** (independent confidence high): Add `Admin/` to the portable gate statements.

b) Keep the portable model to Pillars and Resources and treat Admin gating as an island choice.

### CAPITAL-OF-CAPITALS - [KI-PRINCIPAL-MOD-008] KIP as "Knowledge Capital of Knowledge Capitals"

**Context:** Knowledge Islands.md lines 20 and 135 call Knowledge Islands Principal "the Knowledge Capital of Knowledge Capitals". Territories and Archipelagos says its authorship gives it "no jurisdiction over another territory", and the Great Library is "reference, not jurisdiction".

**Query:** Should the phrase be reworded so that it does not imply a role over other territories' Capitals?

**Options:**

a) (recommended, confidence medium - it removes a contradiction with SDR-KI-PRINCIPAL-005) **reviewed** (independent confidence high): Reword it as "the canonical home of the model, without jurisdiction over other territories", and keep the "legendary utopia" image.

b) Keep the phrase as rhetoric and add a qualifying sentence.

### TAGS - [KI-PRINCIPAL-MOD-008] keep subject tags beside note_type?

**Context:** Kris asked on 2026-10-12 whether subject tags are still needed. The `card/*` and `calendar/*` tags repeat what `note_type` already says, while the `topic/*` tags still help search across folders.

Independent scope check: retiring redundant kind tags is a model direction. Any later migration must check tag-dependent consumers and map existing kinds without losing information.

**Query:** Which tag families should the model keep?

**Options:**

a) (recommended, confidence low - retiring tags touches many notes and tools) **reviewed** (independent confidence high): Keep `topic/*`, `date/*` and `source/*`, and retire the `card/*` and `calendar/*` type tags in favour of `note_type`.

b) Keep the full taxonomy unchanged.

c) Retire all tags in favour of `note_type`, folders and links.

### EMERGING - [KI-PRINCIPAL-MOD-008] what to do with the Emerging Concepts

**Context:** Four notes sit in Emerging Concepts: Realm Model, Avatar Roles and Oversight, Known World and Fictional Lineage. [ADR-KI-PRINCIPAL-005](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-005-one-persona-across-explicit-working-contexts.md>) settles one persona with one name across working contexts. The Techne Programme Focus says that knowledge consolidation alone does not accept candidates.

Independent scope check: Fictional Lineage can record attributed influences as Background while keeping speculative horizons explicitly speculative. This does not adopt Realm authority, Avatar powers, a registry or a deployment. The other three notes remain unadopted. [ADR-KI-PRINCIPAL-005](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-005-one-persona-across-explicit-working-contexts.md>) explicitly fixes one enduring persona and context-bound authority; it does not expressly forbid every display alias. Agreement keeps the present persona and name, and does not settle the broader alias question by inference.

**Query:** Which Emerging Concepts should move to the settled Philosophy?

**Options:**

a) (recommended, confidence medium - this respects the Focus and ADR-005) **reviewed** (independent confidence medium): Leave Realm Model, Avatar Roles and Oversight and Known World open, and keep one Avatar name under [ADR-KI-PRINCIPAL-005](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-005-one-persona-across-explicit-working-contexts.md>). Adopt Fictional Lineage into Background beside Influences Along the Way.

b) Leave all four open.

### CANDIDATE-PRINCIPLES - [KI-PRINCIPAL-MOD-008] adopt the two candidate engineering principles?

**Context:** Engineering Practice Principles holds two candidates: a neutrality extension to Provider-Neutral Execution, and FOSS-First and Inspectable. Both are consistent with the existing principles. The Techne Programme Focus says that consolidation alone does not accept candidates.

Independent scope check: the Focus prevents consolidation from silently accepting candidates. This query can supply the explicit owner decision. These qualified principles need no new product, service, provider change or implementation mandate.

**Query:** Should the two candidate principles be adopted?

**Options:**

a) (recommended, confidence medium-high - They fit the adopted replaceability and explicit-trade-off principles; the Focus requires an owner decision, not permanent deferral of principle decisions.) **Blind review:** Adopt both now. Adopt both as qualified engineering decision criteria: extend neutrality without lowest-common-denominator limits, and prefer FOSS/open standards where practical. This grants no implementation or product expansion.

b) **Delivery run:** (recommended, confidence medium - this follows the Focus as written) Leave both as candidates until the owner takes them up.

### STRUCTURE-TODOS - [KI-PRINCIPAL-MOD-008] settle the Port and Routes and Customs to-dos

**Context:** Structure's Port to-do is now largely settled by [GDR-KI-PRINCIPAL-010](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-010-the-port.md>) and the `+`/`-` rules. Routes and Customs is still open, though Territories and Archipelagos has a route paragraph and `ki-trades` governs exchange.

**Query:** Should the Port to-do become a settled section?

**Options:**

a) (recommended, confidence medium - the decision already exists) **reviewed** (independent confidence high): Make Port a settled section that cites [GDR-KI-PRINCIPAL-010](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-010-the-port.md>). Keep the Routes and Customs to-do, with pointers to the route paragraph and to `ki-trades`.

b) Leave both to-dos as they are.

### LAYER-PATHS - [KI-PRINCIPAL-MOD-008] content-layer paths that do not exist

**Context:** Authoring Guidelines lines 31, 32 and 84 give content-layer paths under `/Pillars/Knowledge Capital/Model/...` that do not exist. Configuration names the Charter and `Admin/Operations/Activities/` as the homes.

Independent scope check: use the declared homes without inventing a new layered directory tree or duplicating configuration. Portable definitions and runtime scripts retain their existing owners.

**Query:** Should the paths be rewritten to the declared homes?

**Options:**

a) (recommended, confidence medium - the current paths are unreachable) **reviewed** (independent confidence high): Rewrite them to the Charter and `Admin/Operations/Activities/`.

b) Remove the layered-path scheme and describe the layers in words.

## Parked

- NO-GATE (with PKGLESS-GATE) - project shape commit gate; Kris will come back to it. a) `ki repo audit --skill ki-repo` staged, check-only; review prefers widening KI-HARNESS-GOV-225.
