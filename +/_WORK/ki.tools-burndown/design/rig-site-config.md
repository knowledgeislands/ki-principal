# Rig site configuration and package managers

Design note for RIG-SITE-CONFIG (19 October 2026), the [Tools burndown](../work.md) work. It assesses the rig.midnight.ninja handoff (Ask A per-host configuration, optional Ask B acquisition kind), proposes the data shape Rig should own, and answers Kris's question on package managers. It is investigation only: no code, record or release has changed.

Sources read: tools-rig at `22d4ed9` (specifications, `src/rig/`), the chezmoi Rig configuration (`dot_config/rig/conf.d/`), the site's `apps/site-rig/pipeline/pull.ts`, `data/hosts.json` and `data/host-tools.json`, and [KB-MIDNIGHT-RIG-SITE-001](/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja/docs/roadmap/KB-MIDNIGHT-RIG-SITE-001-show-hosts-per-tool.md).

## Short answers

- **Ask A is the right question, built on two wrong premises.** Settings already link to tools: every service, scheduled job, setting, Dock layout and firewall may carry `requires`, default applications carry `tool`, and Dock items carry `tool`. But `requires` means "prerequisite", not "this resource configures that tool", so it cannot be reused as is. More importantly, Kris's declared data would show **no difference between terra and sol on any tool** today. Every resource that names a tool is either in `core` (same on both Macs) or concerns a tool that is itself laptop-only.
- **Rig should own a subject link and the derivation.** It should add an optional `tool = "ID"` on settings, services, scheduled jobs and firewalls, with the meaning default applications already give it. Rig derives "configured" while it resolves a profile, and `rig show --format json` carries it per tool as a list of qualified resource identities, which the site reduces to a boolean. The public export stays unchanged.
- **Package managers are half-modelled.** mas, mise, node, npm, uv and bun are ordinary catalogue tools, published on the site, with hand-written `requires` links. Homebrew, the manager behind 128 of the catalogue's 170 installation-bearing tools, sits outside the catalogue entirely. It must already be installed, `rig doctor` mentions it only as an informational line, and it is invisible in `rig show`, the export and the site. The apply-time prerequisite matrix is hard-coded and misses uv installed through mise. Doctor's manager list is also hard-coded and misses mas.

## 1. The handoff against Rig as it stands

### What holds

- The boundary is right: a per-profile flag for each tool, declared intent only, no keys, values or counts, and `rig export --profile public` left as narrow as it is ([RIG-PUB-002](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/publishing.md)).
- Rig, not the site, should decide what "configures" means. Today the site would otherwise have to reverse-engineer it from resource fields.
- A profile stands in for a host: chezmoi renders each Mac's `default-profile` from `rigProfile` (`dot_config/rig/private_rig.toml.tmpl`), and `hosts.json` maps terra to `laptop` and sol to `studio`.

### What the handoff gets wrong or misses

1. **There is already a tool link, but it means "prerequisite".** [RIG-CONF-016](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/configuration.md), RIG-CONF-017, RIG-CONF-018 and RIG-CONF-030 allow a `requires` array of tool identities on services, scheduled jobs, settings, Dock layouts and firewalls. [RIG-ORCH-020](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/orchestration.md) makes each entry select that tool and its requirements. `[default-application.ID]` has `tool`, parsed into the same `requires` field (`src/rig/10-configuration.bash:457`). `[dock-item.ID]` has `tool` as a filter only, which keeps the item when the tool is selected and never selects it. `[port.ID]` has `owner = "tool:ID"`. The handoff's proposed `tool =` field would duplicate `requires` unless it carries a different meaning, and it should, because the live data shows why `requires` alone misleads. `dock.workstation` has `requires = ["dockutil", "spark-desktop"]`: dockutil is the instrument, not the thing configured.
2. **The declared data has no per-host configuration divergence to show.** The live chezmoi configuration has 55 settings, all on macOS system domains (global, Finder, Dock, screencapture, desktop services, Time Machine, disk images, AirDrop), none linked to a catalogue tool. Its 12 services and scheduled jobs carry no `requires` at all. The only resource-to-tool links are `default-application.svg` to `google-chrome` (core) and `port.headroom` to `headroom` (core). Laptop-only items are 2 tools (`rendapp`, `the-tower`), `dock.workstation`, `service.paperclip`, `port.paperclip` and 3 scheduled jobs. Studio adds one tool. Even with every sensible subject link authored, every flag would match on both Macs. Core resources give the same answer on terra and sol, `service.paperclip` concerns `paperclip`, a tool already laptop-only, and the laptop's Dock layout and scheduled jobs configure macOS or Kris's own scripts rather than a catalogue tool. Nor does chezmoi branch any tool's configuration by host: only `rigProfile` and one SSH script are host-conditional. Kit's expectation that "terra and sol diverge mainly through configuration" is not borne out by what is declared. The "own config" cell would mostly light up identically in both columns.
3. **Ask A's privacy boundary is enforced by the site, not Rig.** `rig show --format json` (`rig_show_json`, `src/rig/30-commands.bash:1699`) already emits every selected resource with its provider and, for settings, its value; default applications with bundle ID; ports with number, scope and owner. `pull.ts` reads it and writes only tool IDs. A boolean adds no privacy. Its value is that Rig owns the meaning.
4. **The site depends on an unspecified contract.** [RIG-QUERY-001](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/queries.md) specifies the `rig show` text form only. The JSON carries `schema: 1` in its envelope, but no clause lists `tools[]` fields. Whatever lands should specify the JSON, including the existing `tools[].id` the site already relies on.

## 2. The shape Rig should own

### 2.1 How a resource links to its tool

**Recommended: one optional `tool = "ID"` subject link** on `[setting.*]`, `[service.*]`, `[scheduled-job.*]` and `[firewall.*]`, with exactly the meaning `[default-application.*]` already gives `tool`. The named tool is the resource's subject, and it also enters the profile's prerequisite closure, as a `requires` entry does. One field name, one meaning, across every resource kind that can configure a tool. `requires` keeps its narrower meaning of "needs this tool to exist". A resource may have both, as `dock.workstation` would (no subject, `requires` dockutil).

Alternatives considered:

- **Derive from `requires`** (no new field). Cheapest, but wrong on the only live example. It would mark dockutil and spark-desktop "configured", and any service that `requires` its runtime (node, bun, uv) would mark that runtime configured.
- **Derive from preference domain** (a derived link rather than a field). A setting whose `domain` equals a tool's application bundle identifier links automatically. That is attractive for app settings and zero-authoring, but it needs a declared bundle ID per tool, since reading `Info.plist` is observation, not declared intent. It does not cover services or jobs, and none of today's settings would match. It could later be added as sugar on top of the explicit link.
- **Tool-side list** (`[tool.X] configures = [...]`). Wrong direction: the tool would list resources whose membership varies by profile, splitting one fact across two tables.
- **Dock-item filter meaning** (the resource applies only where its tool is selected). Useful later for "settings follow the app", but it would make configuration divergence a pure echo of tool divergence, the opposite of what Kit wants to show.

### 2.2 Where "configured" is derived

During `rig_resolve_profile`, after resource selection. A selected tool T is configured by profile P when P selects at least one setting, default application, service, scheduled job or firewall whose subject `tool` is T. Not counted:

- Dock items, which place an app rather than configure it.
- Ports, which declare a listener.
- `requires`-only links.
- Tool-owned artifacts and application CLIs, which belong to the tool and do not vary by profile.
- Skills.

The same derivation feeds the text forms: `rig show TOOL` gains a "Configured by" line listing qualified resources and their profiles, and the `rig show` tool table can mark configured tools. That way the site and the human views cannot disagree.

### 2.3 JSON contract

**Recommended:** in `rig show [--profile P] --format json`, every `tools[]` entry always carries `configured_by`, an array of qualified resource identities in bytewise order, empty when none:

```json
{"schema":1,"rig":"…","command":"show","profile":"laptop",
 "tools":[{"id":"google-chrome","name":"Google Chrome","category":"…","purpose":"…",
           "configured_by":["default-application:svg"]},
          {"id":"zed","name":"Zed","category":"…","purpose":"…","configured_by":[]}]}
```

The site writes `profiles.<P>.config` as the IDs whose `configured_by` is non-empty, and publishes only that boolean. It is a private command that already discloses these identities, so nothing new leaves Rig. The list makes the derivation auditable and testable, and the boolean is one line in `pull.ts`. A RIG-QUERY clause should specify the complete `rig show` JSON tool entry, including `id`, `name`, `category`, `purpose` and `configured_by`.

Alternatives:

- **The handoff's boolean**, `"configured": true|false`, always present rather than absent. It is minimal and fine if Kris prefers no identities. It loses the "why" for review.
- **A per-profile top-level list**, `"configured_tools": [...]`. Mirrors what the site stores, but it duplicates tool membership and drifts from `tools[]`.
- **A comparison in the public export**, `rig export --profile public --compare laptop,studio`, emitting per-profile membership and configured flags already intersected with the view. This is the genuinely stronger boundary, because Rig rather than `pull.ts` would enforce "never name a private tool" and the site would stop reading private profiles at all. It changes the public export, which this brief rules out, so it is recorded here, not proposed.

### 2.4 Done when

`rig show` JSON for `laptop` and `studio` carries `configured_by`. Fixture tests cover a tool configured in one profile and not the other, the subject link selecting its tool, a `requires`-only resource not counting, and export byte-identity. The configuration guide documents `tool` on each resource kind, and the RIG-QUERY clause specifies the JSON.

A data step must follow in chezmoi before the site shows anything: add `tool` to the resources that do concern a catalogue tool (for example `service.claude-swap-auto` to `claude-swap`, `service.mcporter-daemon` and `service.mcporter-http-bridge` to `mcporter`, `service.paperclip` to `paperclip`, `scheduled-job.rig-update` to `rig`). Per section 1 item 2, that still yields identical columns until Kris declares genuinely host-specific configuration.

### 2.5 Ask B, option only (no go-ahead)

If Kit gives the go-ahead, add one coarse field per public tool, derived as follows:

- `application`: the tool declares an application artifact, or installs as a Homebrew cask or mas app.
- `command-line`: a formula, uv, mise or npm tool, or a direct-download executable.
- Absent for a catalogue-only tool.

Name it `kind` or `form`. The site's guard matches substrings (`install`, `provider`, `path`, `port`, `service`, `version`, `locator`, `hostname`), so `install_kind` and `provider_kind` fail. One complication: export is platform-independent ([RIG-PUB-001](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/publishing.md)) while installations vary by platform variant. Either the field becomes a per-platform map or it derives from the tool rather than the variant. The change would amend RIG-PUB-002 and the RIG-PUB-004 example. It is additive to format version 1, which consumers must tolerate.

## 3. Package managers

| Manager | Rig provider | In Kris's catalogue | Gets onto a fresh Mac by | Apply defers until installed | `rig doctor` | `rig show` / export / site |
| --- | --- | --- | --- | --- | --- | --- |
| Homebrew (128 tools) | built-in `homebrew` | no | hand, setup guide Stage 1 step 6 | no: "Homebrew itself MUST already be available" ([RIG-ORCH-018](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/orchestration.md)) | `brew: available/unavailable; action=none` informational line; Command Line Tools check ([RIG-STATE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/state.md)); each bound tool `unavailable` | invisible |
| mas (14 tools) | built-in `mas` | `tool.mas`, Homebrew formula, public | Rig | yes, mas from Homebrew; all 14 declare `requires = ["mas"]` | not in the manager line | tool and `requires` edges, public |
| mise (15 tools) | built-in `mise` | `tool.mise`, Homebrew formula, public | Rig | yes, mise from Homebrew | listed | tool and edges, public |
| node / npm (9 tools) | built-in `npm` | `tool.node` (mise), `tool.npm` (npm, requires node), public | Rig | yes, npm via mise node, transitive | `npm` listed | tool and edges, public |
| uv (2 tools) | built-in `uv` | `tool.uv`, **mise** tool, public | Rig | **no**: the matrix has no uv-from-mise case | listed | tool and edges, public |
| bun | none: not a Rig provider | `tool.bun`, mise tool, public | Rig | not applicable | not applicable | tool, public |
| chezmoi | built-in `chezmoi` (no tool uses it) | `tool.chezmoi`, Homebrew formula, public | Rig, though it applies Rig's own configuration | not applicable | listed | tool, public |
| paperclip | custom, `${RIG_DATA_HOME}/providers/paperclip` | provider shipped by chezmoi | chezmoi | not applicable | executable checked at preflight | invisible |
| Command Line Tools | environment | no | hand, Stage 1 step 4 | not applicable | `command-line-tools` finding | invisible |

### Gaps

- **G1, Homebrew sits outside the model.** It is the largest dependency and the only manager that is not a tool. It has no rationale, no public card, and no relation from the 128 tools that need it. A missing Homebrew surfaces as 128 separate `unavailable` tool findings, not one cause.
- **G2, doctor's manager line is hard-coded and inert.** `rig_doctor_native_availability` (`src/rig/22-observation.bash:1510`) checks `brew uv mise npm chezmoi`. It omits mas and custom providers, ignores what the profile selects, and always says `action=none`.
- **G3, uv's apply-time deferral is missing.** `rig_apply_provider_prerequisite` (`src/rig/21-provider-state.bash:1397`) hard-codes three cases: mise from Homebrew, mas from Homebrew, npm from mise node. Kris's uv comes from mise. By code reading, a first apply on a fresh Mac fails full-plan preflight on `claude-swap` and `headroom` ("provider 'uv' executable is unavailable") before any mutation, until uv exists. This is inferred, not reproduced.
- **G4, manager links are hand-authored and unchecked.** Today mas, mise, npm and uv tools all declare the right `requires`, but nothing validates it. A new App Store tool without `requires = ["mas"]` would fail a fresh-Mac apply with no warning.
- **G5, services hard-code mise install paths.** `service.observatory` runs `~/.local/share/mise/installs/bun/latest/bin/bun` and `service.paperclip` runs `…/node/24.15.0/bin/node`, with no `requires`. A node upgrade silently breaks paperclip until doctor's launch check ([RIG-STATE-046](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/state.md)) flags it. This is a chezmoi data issue that the subject link would partly surface.

### Proposed model: managers are catalogue tools

Rig should let a catalogue tool declare that it provides a built-in manager, for example `provides = "mas"` on `tool.mas`. Homebrew becomes a tool too (`provides = "homebrew"`), observation-only because it must pre-exist. Rig then:

- derives the manager edge for every bound tool, closing G4 and giving Homebrew its 128 relations;
- replaces the hard-coded deferral matrix with that data, closing G3 and any future case;
- attributes a missing manager to one finding on the manager tool rather than to every dependant, closing G1;
- derives doctor's manager list from the selected plan, closing G2.

Derived edges could enter the public relationships, so the site shows "installed with Homebrew" without any provider field, but that changes export content and so needs its own decision. A no-code interim is possible: declare `[tool.homebrew]` as a catalogue-only public tool in chezmoi and add `requires = ["homebrew"]` where wanted. That gives the site a Homebrew card and edges at once, at the cost of 128 hand edits that G4 would then have to police.

## 4. Awareness items

- **62 placeholder rationales.** These are Homebrew packages in `dot_config/rig/conf.d/private_16-homebrew.toml` in the chezmoi source (`krisb/dotfiles`) that still say "Retain the explicit package choice from the former managed Brewfile…". The fix is data in chezmoi, owned by [KB-DOTFILES-UE-027](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md) ("Honest Rig rationales"), on hold waiting for Kris's decisions in `-/rig-rationale-review.md`, review date 7 November 2026. The worksheet counts 121 unresolved rationales (86 tools, 35 settings), of which these 62 are the Brewfile subset. No Rig or site change is needed: `pull.ts` already counts them through its `^(Review needed|Retain explicit package choice)` match.
- **vega has no public view.** Its Rig configuration is the agent-host recipe, `recipes/agent-host/rig.toml` in ki-techne-harness. It declares 7 tools through a custom `agent-host-pins` provider, with no profile tables and so no `public` view. The fix would be in that recipe, adding a `[profile.public]` view and memberships, and naturally belongs with [KI-TECHNE-OPS-018](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) ("Converge tools through Rig", on hold). Even then the site's pull runs on a Mac against the Mac's configuration, so it would need a second export against the recipe (`RIG_CONFIG_HOME`), and vega must run a current Rig first. Until then the hand-written vega line in `hosts.json` stands, as [KB-MIDNIGHT-RIG-SITE-001](/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja/docs/roadmap/KB-MIDNIGHT-RIG-SITE-001-show-hosts-per-tool.md) intends.

## 5. Proposed next steps (each put to Kris as a query in the run report)

1. Capture a tools-rig record, "Resource subject links and per-profile configured tools", covering sections 2.1 to 2.4 including the RIG-QUERY JSON clause.
2. Capture a krisb/dotfiles record for the subject-link data step and the G5 paths, after record 1 lands.
3. Capture a tools-rig record, "Package managers as catalogue tools", covering G1 to G4. Optionally split out a small first record for G2 and G3.
4. Tell the site side now that per-host configuration columns would be identical with today's data, so Kit can decide whether the "own config" cell is worth shipping before Kris declares host-specific configuration.
5. Ask B stays parked until Kit's go-ahead.
