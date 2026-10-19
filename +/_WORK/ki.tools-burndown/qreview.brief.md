# qreview - blind review of open queries

Blind query review under the ki-coordination standard's Query review section. Below are 10 open queries from the ki.tools-burndown work package. Each gives Context, Query and Options only; option letters carry no ranking and no recommendation is shown. For each query, check what you can directly in the repositories under /Users/krisbrown/workspaces/knowledge-islands (read-only: the tools-ki, tools-mgit, tools-rig, ki-agentic-harness, ki-principal and chezmoi checkouts, and `~/.local/state/ki/agents/tools-burndown/` reports), then give your own recommended option letter, a confidence (high, medium or low) and a one-line reason, plus one line on anything you verified or found wrong in the Context. Change nothing in any repository.

Write the result to /Users/krisbrown/.local/state/ki/agents/tools-burndown/qreview.report.md: one `### <TAG>` section per query with `**Pick:** <letter>`, `**Confidence:** <level>`, `**Reason:** <one line>`, `**Checked:** <one line>`. Then stop.

## TRIAGE-PROPOSAL - Keep all eight triage records

**Context:** The goal was to cancel or merge at least half. I found no honest case for any of them. Each one is either a live dependency, part of a run writing now, or something you asked for in the last two days: KI-TOOL-KI-CLI-145 (thread bindings, `ki thread`): keep, because KI-HARNESS-GOV-199 Phase 3 and KB-DOTFILES-UE-096 wait on it; its text still speaks of checkpoints and `role`, and planning should reread it for the work model's work id and `level`. KI-TOOL-KI-CLI-149 (work status views contract): keep, because a live run is writing it and the brief rules it out. KI-TOOL-KI-CLI-151 (CLI convention departures): keep, because CLI-DEPARTURES a) made it the single carrier, and none of the four departures is fixed yet. KI-TOOL-KI-CLI-152 (work folder housekeeping commands): keep, because a live run is writing it and the brief rules it out; its goal still names `ki-work-folder`, which has become `ki-work-package`. KI-TOOL-KI-CLI-154 (territory tolerates unregistered members): keep, because the defect is real (the territories spec line 29 requires the hard fail) and your TERRITORY-REGISTER c) handed it here today. KI-TOOL-KI-CLI-156 (CI runs the local gate): keep, because your open BIOME-CI-STANDARD answer decides its shape, not its existence. KI-TOOL-MGIT-CLI-027 (fatal Bats assertions): keep, because all 8 bare assertions are still present in `tests/territory-producer.bats` and `tests/territory-protocol.bats`. KI-MCP-GIT-FND-006 (ground roots in `~/workspaces`): keep, because `DEFAULT_SAFE_ROOTS` is still `~` and your EXT-ROOTS answer asked for it today. I also checked for overlap with KI-TOOL-KI-CLI-125, -134, -140 and -149, and with KI-TOOL-MGIT-CLI-026: none.

**Query:** Do you confirm keeping all eight, which leaves the "at least half" goal unmet?

**Options:**

a) Accept all: keep all eight. KI-TOOL-KI-CLI-145 and -152 get rewritten for the work model when they are planned.

b) Accept with named exceptions: name any record to cancel anyway, with its resolution (obsolete, rejected, duplicate, merged or superseded), and I'll carry it out under `ki-accept`.

c) Decline: send it back for a second pass with a firmer cut, for example cancelling KI-TOOL-KI-CLI-151 and fixing each departure without a record.

### BIOME-CI-STANDARD - The record conflicts with the Minimal CI rule

**Context:** The ki-engineering Minimal CI rule says CI must not repeat checks that the audit runs. In tools-ki, `ki repo audit` already runs Biome (BIO-1, at FAIL), TypeScript and `bun run test:coverage`, and rubric item CI-2 warns when `ci.yml` repeats the test run. CI already runs that audit, so the premise that "CI does not run Biome" looks wrong. The real gap is that CI's audit did not stop the drift. The cause might be the pinned `KI_VERSION` v0.11.3, the harness that CI resolves, or a red CI that nobody was watching. I could not check, because this run was not allowed to call GitHub. The record's Discussion sets this out for planning.

**Query:** Should KI-TOOL-KI-CLI-156 keep your explicit-steps goal, or start by finding out why CI's audit missed the drift?

**Options:**

a) Keep the record as captured, and have planning check the latest CI runs first. If the audit gate turns out to be broken, fix it rather than repeat its checks.

b) Keep the explicit steps whatever planning finds, and hand ki-agentic-harness a Minimal CI exception.

c) Reframe the record now as "make CI's audit gate effective" and drop the explicit steps.

### MGIT-LEARN-UNATTENDED - Scripts can no longer learn unattended

**Context:** Because every template now needs a yes on a terminal, a script or pipe that used to learn when all repositories agreed now saves nothing and exits 1. This is what the refinement asked for, and the record lists it under Outstanding concerns.

**Query:** Should unattended learning stay impossible, or should a later record add an explicit flag that accepts without asking?

**Options:**

a) keep it impossible for now and capture a flag only if a need comes up;

b) capture a record now for a `--yes` style flag, which the current boundary leaves out.

### SITE-CONFIG-SHAPE - Capture the per-profile configuration record in tools-rig

**Context:** Ask A needs a resource-to-tool link that means "configures", not "requires". The live Dock layout requires dockutil and spark-desktop but configures neither. The site already reads the private `rig show` JSON, so a boolean adds no privacy. What it adds is that Rig owns the meaning. The `rig show` JSON format has no specification today, even though the site already depends on it.

**Query:** Shall I capture a tools-rig record at triage, "Resource subject links and per-profile configured tools", with the shape in section 2 of the design note?

**Options:**

a) Capture it with an explicit `tool` subject link, `configured_by` in the `rig show` JSON, and a new specification clause covering that JSON.

b) Capture it with the handoff's plain `configured: true|false` instead of the list.

c) Derive the flag from the existing `requires` field, with no new field; this marks the wrong tools, as the Dock layout shows.

d) Capture nothing until Kris declares configuration that actually differs between the hosts.

### SITE-CONFIG-DATA - Follow-up chezmoi record for subject links and service paths

**Context:** Once Rig accepts `tool`, the resources that really concern a catalogue tool need the link added: the claude-swap, mcporter and paperclip services and the rig-update job. Separately, the observatory and paperclip services hard-code mise install paths, including node 24.15.0, and declare no `requires`. A node upgrade would silently break paperclip (G5).

**Query:** Shall I capture a krisb/dotfiles record for both pieces of data work, blocked by the SITE-CONFIG-SHAPE record?

**Options:**

a) Capture one record covering both.

b) Capture only the path fix now and add the links when the Rig record lands.

c) Neither.

### MANAGERS-AS-TOOLS - Package managers in Rig's model

**Context:** Homebrew is outside the catalogue (G1). Doctor's list of package managers is fixed in the code, leaves out mas and always says no action is needed (G2). The apply step's list of prerequisites it can install first is also fixed in the code and leaves out uv installed through mise. By my reading of the code, a first apply on a new Mac fails on claude-swap and headroom; I have not reproduced this (G3). Links from tools to the manager that installs them are written by hand and nothing checks them (G4).

**Query:** How should these gaps be captured in tools-rig?

**Options:**

a) Two records at triage: "Doctor reports the selected plan's managers, and uv installs before its tools" (G2, G3), and "Package managers as catalogue tools", a `provides` field that lets Rig derive manager links, prerequisites and findings from data (G1, G4).

b) One combined record.

c) No Rig change: declare `[tool.homebrew]` as a catalogue-only public tool in chezmoi and add the `requires` links by hand.

### HOOKS-CONVENTION - Which convention "standardise on Husky" means

**Context:** The harness standard and [ADR-KI-HARNESS-SKILLS-017](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-017-commit-gate-existence-and-content-are-owned-separately.md) already require a committed `.githooks/pre-commit` bound by `core.hooksPath .githooks` in every repository, with Husky as the content layer where a Bun package exists. 25 KI repositories bind Husky's untracked `.husky/_` instead. Husky alone cannot gate the 21 package-less repositories without adding a package to each, and lets a fresh linked worktree with no install commit unchecked.

**Query:** Should the estate converge on Husky for content behind committed `.githooks` stubs, or on Husky alone?

**Options:**

a) Husky holds the content wherever a Bun package exists; every repository commits `.githooks` stubs and binds `.githooks`.

b) Husky alone: bind `.husky/_` everywhere and add a `package.json` and `husky` to every package-less repository; unbuilt worktrees commit unchecked and the decision is superseded.

c) Commit `.husky/` and bind it directly, dropping Husky's runtime and dependency across the estate.

### KB-AUDIT - Where the knowledge-base audit lives

**Context:** ki-principal runs the KB audit from its `.githooks/pre-commit` stub, and the rubric criteria read only that file. Moving it into `.husky/pre-commit` makes every Bun stub a generated wrapper, and `GATE-1`, `GIT-2` and `SHELL-HOOK` would read the stub and the Husky hook together.

**Query:** Should the KB audit move into `.husky/pre-commit` where a package exists?

**Options:**

a) Move it into `.husky/pre-commit` where a package exists, keep it in the stub where none does, and have the three criteria read the effective gate.

b) Keep the KB audit in the stub everywhere.

### COMMIT-MSG - Message checks in package-less repositories

**Context:** Commitlint needs Node and an install, so the 21 package-less repositories have no message check. A shell pattern in each stub would copy the `ki-git` vocabulary 21 times and drift.

**Query:** How should package-less repositories check commit messages?

**Options:**

a) Add `ki git check-message` for `.githooks/commit-msg` to call; until it ships, those repositories have `pre-commit` only.

b) A shell pattern in `.githooks/commit-msg`, generated from the `ki-git` vocabulary by conform.

c) No message check outside Bun repositories.

### ROLLOUT-AUTHORITY - Who writes the stubs in other repositories

**Context:** The current decision makes adding a stub "that repository's change, raised as a receiver-owned trade", and the Charter gives territory selection no cross-repository write authority. Rolling out through `ki repo` and the estate repair means runs writing stubs in about 47 repositories.

**Query:** Should one owner grant per wave cover `ki repo conform` writing and committing the stubs in every listed KI repository?

**Options:**

a) One grant per wave; a run commits the stubs and the `prepare` change by explicit path in each listed repository, local only, and you push.

b) Receiver-owned trades: this work ships the standard and the tool, and each repository's owning work runs `ki repo conform` itself.
