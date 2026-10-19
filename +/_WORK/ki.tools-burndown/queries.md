# ki.tools-burndown queries

## Open

### KI-RELEASE-GO - Cut the ki patch release once it is ready

since 2026-10-19 · from the KI-PATCH-RELEASE message

**Context:** Through ki.ways-of-working you asked for one `ki` patch release "soon", carrying KI-TOOL-KI-CLI-155 so `priority` and `size` stop dropping 18 records, and pinning a ki-agentic-harness that provides `ki-work-package`, so ki-principal CI stops failing at "Install released KI". Your standing rule is to ask before any `ki` release. The cli155 run is building the change now and stops before tagging, pushing or publishing.

**Query:** May I cut, push and publish the patch release as soon as KI-TOOL-KI-CLI-155 passes verification and the harness pin sits at or after the harness-link-fix commit?

**Options:**

a) (recommended, confidence high - it is the release you asked for, and it is gated on verification and the harness fix) Yes: cut it on those two conditions, then reply with the tag in ki.ways-of-working's `messages.md`.

b) No: bring the finished change back to you before the tag.

### BIOME-CI-STANDARD - The record conflicts with the Minimal CI rule

since 2026-10-19 · from biomeci.report.md in the run state folder

**Context:** The ki-engineering Minimal CI rule says CI must not repeat checks that the audit runs. In tools-ki, `ki repo audit` already runs Biome (BIO-1, at FAIL), TypeScript and `bun run test:coverage`, and rubric item CI-2 warns when `ci.yml` repeats the test run. CI already runs that audit, so the premise that "CI does not run Biome" looks wrong. The real gap is that CI's audit did not stop the drift. The cause might be the pinned `KI_VERSION` v0.11.3, the harness that CI resolves, or a red CI that nobody was watching. I could not check, because this run was not allowed to call GitHub. The record's Discussion sets this out for planning.

**Query:** Should KI-TOOL-KI-CLI-156 keep your explicit-steps goal, or start by finding out why CI's audit missed the drift?

**Options:**

a) (recommended, confidence medium - it keeps your choice and leaves the evidence to planning) Keep the record as captured, and have planning check the latest CI runs first. If the audit gate turns out to be broken, fix it rather than repeat its checks.

b) Keep the explicit steps whatever planning finds, and hand ki-agentic-harness a Minimal CI exception.

c) Reframe the record now as "make CI's audit gate effective" and drop the explicit steps.

### MGIT-LEARN-UNATTENDED - Scripts can no longer learn unattended

since 2026-10-19 · from mgitlearn2.report.md in the run state folder

**Context:** Because every template now needs a yes on a terminal, a script or pipe that used to learn when all repositories agreed now saves nothing and exits 1. This is what the refinement asked for, and the record lists it under Outstanding concerns.

**Query:** Should unattended learning stay impossible, or should a later record add an explicit flag that accepts without asking?

**Options:**

a) (recommended, confidence medium - you asked for a prompt "just in case", and nobody has asked for a scripted use yet) keep it impossible for now and capture a flag only if a need comes up;

b) capture a record now for a `--yes` style flag, which the current boundary leaves out.

### SITE-CONFIG-SHAPE - Capture the per-profile configuration record in tools-rig

since 2026-10-19 · from rigsite-config.report.md in the run state folder

**Context:** Ask A needs a resource-to-tool link that means "configures", not "requires". The live Dock layout requires dockutil and spark-desktop but configures neither. The site already reads the private `rig show` JSON, so a boolean adds no privacy. What it adds is that Rig owns the meaning. The `rig show` JSON format has no specification today, even though the site already depends on it.

**Query:** Shall I capture a tools-rig record at triage, "Resource subject links and per-profile configured tools", with the shape in section 2 of the design note?

**Options:**

a) (recommended, confidence medium - this matches how default applications already work, the reason for each flag can be checked, and the public export stays untouched) Capture it with an explicit `tool` subject link, `configured_by` in the `rig show` JSON, and a new specification clause covering that JSON.

b) Capture it with the handoff's plain `configured: true|false` instead of the list.

c) Derive the flag from the existing `requires` field, with no new field; this marks the wrong tools, as the Dock layout shows.

d) Capture nothing until Kris declares configuration that actually differs between the hosts.

### SITE-CONFIG-DATA - Follow-up chezmoi record for subject links and service paths

since 2026-10-19 · from rigsite-config.report.md in the run state folder

**Context:** Once Rig accepts `tool`, the resources that really concern a catalogue tool need the link added: the claude-swap, mcporter and paperclip services and the rig-update job. Separately, the observatory and paperclip services hard-code mise install paths, including node 24.15.0, and declare no `requires`. A node upgrade would silently break paperclip (G5).

**Query:** Shall I capture a krisb/dotfiles record for both pieces of data work, blocked by the SITE-CONFIG-SHAPE record?

**Options:**

a) (recommended, confidence medium - one data pass covers both, and the path fix is worth having on its own) Capture one record covering both.

b) Capture only the path fix now and add the links when the Rig record lands.

c) Neither.

### MANAGERS-AS-TOOLS - Package managers in Rig's model

since 2026-10-19 · from rigsite-config.report.md in the run state folder

**Context:** Homebrew is outside the catalogue (G1). Doctor's list of package managers is fixed in the code, leaves out mas and always says no action is needed (G2). The apply step's list of prerequisites it can install first is also fixed in the code and leaves out uv installed through mise. By my reading of the code, a first apply on a new Mac fails on claude-swap and headroom; I have not reproduced this (G3). Links from tools to the manager that installs them are written by hand and nothing checks them (G4).

**Query:** How should these gaps be captured in tools-rig?

**Options:**

a) (recommended, confidence medium - G2 and G3 are small, self-contained fixes, and the model change deserves its own design) Two records at triage: "Doctor reports the selected plan's managers, and uv installs before its tools" (G2, G3), and "Package managers as catalogue tools", a `provides` field that lets Rig derive manager links, prerequisites and findings from data (G1, G4).

b) One combined record.

c) No Rig change: declare `[tool.homebrew]` as a catalogue-only public tool in chezmoi and add the `requires` links by hand.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
