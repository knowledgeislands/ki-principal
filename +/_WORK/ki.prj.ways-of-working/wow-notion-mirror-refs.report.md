# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-notion-mirror-refs

**🤖 → 👤 Handoff to supervisor · Run report at 22:16 GMT · last mark 01:07 GMT**

---

## Done

- Read-only search finished across ~/workspaces (hidden files included), the chezmoi source, the local KI registry, mcporter, Claude Code, Claude Desktop and Codex settings, launchd agents, mgit manifests and `~/.local/state/ki`; Git history, `+/_WORK` reports and Calendar notes were ignored as briefed. No commit, no change, no network call, Notion untouched.
- The local checkout at `~/workspaces/knowledge-islands/mcp-ki-kb-notion-mirror` is gone, yet eight `node` processes are still running the server from that path: two spawned by Claude Desktop and the rest by the mcporter daemon, which is still advertising the `hnr-mcp-ki-kb-notion-mirror` tools to this very session. They survive only because the binary was loaded before the deletion; every respawn will fail with a missing entry point.
- Limitation: my first scan of `~/.mcporter` printed the Notion integration token into this run's tool output, so it sits in the run's Claude transcript; every later read masked it, and nothing was written anywhere. The token is also in plain text in two rendered targets (mcporter and Claude Desktop), which chezmoi renders from the 1Password item referenced in `mcp-servers.yaml`.
- No references found in: tools-ki, homebrew-tap, ki-specifications, tools-rig, tools-mgit, paperclip, hnr-agentic-harness, `~/Library/LaunchAgents`, any `.mgit.toml`, `~/.config` (ki config, mgit, codex), `~/.claude.json`, or the Codex `mcp_servers` section. apps-observatory.local uses `notion-mirror` only as a test-fixture name in three test files, which is not a reference to the repository.
- Useful context: HNR's State of play (`hnr.sop.sites`) decided on 25 October 2026 that the Notion Mirror MCP's purpose is now met by publishing through pt.humansnotrobots.be, and authorised Notion removal leaf to root; the HNR mirror is therefore already retired in intent, which makes the hnr-principal owner's fix a tidy-up rather than a decision.

### Workstation runtime state (ordinary files, not chezmoi-managed)

| File | Line | What the reference does |
| --- | --- | --- |
| `~/.local/state/ki/registry.toml` | 159-161 | Inventory: `[repositories."mcp-ki-kb-notion-mirror"]` with GitHub URL and the deleted path. `ki` estate selection will resolve to a missing checkout. |
| `~/.local/state/ki/chezmoi/claude-desktop-trust-revoked-2026-10-20.txt` | 24, 49 | Historical: old `kis/` and `kit/` paths in a revocation log. Leave. |
| `~/.local/state/ki/audit-health/*.json` (two files) | - | Cache of past audits naming the path. Leave; regenerates. |
| `~/.local/state/ki/worktrees/ki-principal-integrate/...` and `.../ki-agentic-harness/wow-checker-title/...` | - | Worktree copies of the repository content listed below. Follow their repositories. |
| `~/.claude/settings.json.bak-2026-10-14` | - | Historical backup. Leave. |
| Running processes (pids 2070, 2208, 6500, 13958, 15225, 55439, 99124, 99313) | - | Live: stale server instances under Claude Desktop and the mcporter daemon. They stop at the next restart and will not come back. |

Proposed change: remove the registry entry (`ki registry` has no visible remove subcommand in `--help`, so this is an edit of the TOML or whichever `ki` command owns it), then restart the mcporter daemon and Claude Desktop after the chezmoi apply below. Ordinary state file, no `chezmoi diff` needed for the registry.

### chezmoi source `~/.local/share/chezmoi` (needs an independent `chezmoi diff` review)

| File | Line | What the reference does |
| --- | --- | --- |
| `.chezmoidata/mcp-servers.yaml` | 109-118 | Live config that will fail: server `hnr-mcp-ki-kb-notion-mirror` for clients `claude-desktop` and `mcporter`, entry point under the deleted checkout, token from a 1Password item, KB root `hnr-shared`, access `destructive`. |
| `.chezmoidata/mcp-servers.yaml` | 51-52 | Documentation: comment distinguishing the hosted `notion` server from the mirror. |
| `.chezmoidata/trusted-folders.yaml` | 150-151 | Inventory: trusted path for `chatgpt-codex`, `claude-code`, `claude-desktop`. Harmless but stale. |
| `workspaces/vscode/kis-mcp-ki-kb-notion-mirror.code-workspace` | 4 | Live config: VS Code workspace whose only folder is the deleted path. |
| `docs/guides/tools/mcporter.md` | 43 | Documentation: lists the server among mcporter's knowledge servers. |

Rendered targets that carry the same references and change only through `chezmoi apply`:

| Rendered target | Line | Rendered from |
| --- | --- | --- |
| `~/.mcporter/mcporter.json` | 10-20 | `mcp-servers.yaml` via `dot_mcporter/private_mcporter.json.tmpl`; live, fails on respawn. |
| `~/Library/Application Support/Claude/claude_desktop_config.json` | `mcpServers.hnr-mcp-ki-kb-notion-mirror`, 140 | `mcp-servers.yaml` and `trusted-folders.yaml` via the Claude Desktop modify template; live, fails on respawn. |
| `~/.claude/settings.json` | 31 | `trusted-folders.yaml` via `dot_claude/modify_private_settings.json.tmpl` (`permissions.additionalDirectories`); harmless. |
| `~/.codex/config.toml` | 190 | `trusted-folders.yaml` via `dot_codex/modify_private_config.toml.tmpl` (project trust); harmless. |
| `~/bin/rig-bringup-check` | 75 | `mcp-servers.yaml` via `bin/executable_rig-bringup-check.tmpl` lines 74-78; reports the entry point as missing on every bring-up check. |
| `~/workspaces/vscode/kis-mcp-ki-kb-notion-mirror.code-workspace` | 4 | The workspace file above. |

Proposed change: delete the server block, the trusted-folder entry and the workspace file; reword the comment and the guide line; run `chezmoi diff` for independent review, then `chezmoi apply`, `bin/launchd/mcporter_restart` and a Claude Desktop restart. The 1Password item the token points to and the Notion integration itself are outside this brief and left to Kris (query MIRROR-TOKEN).

### ki-principal (ordinary repository content; `Admin` and `Pillars` changes go through the Enactment Process or an explicit owner instruction)

| File | Line | What the reference does |
| --- | --- | --- |
| `.ki.toml` | 49 | Inventory: GitHub URL in the territory repository list read by `ki` tooling. |
| `Admin/Governance/Known Lands.md` | 42, 128 | Inventory: table row and link reference. Known Lands already records retired islands in prose at lines 52 and 54 (ki-plugins, mcp-housekeeping-codex). |
| `Pillars/Philosophy/Model/Tools/Notion Mirror/Notion Mirror.md` | whole note | Documentation: the tool's chapter note, status "current - October 2026". |
| `Pillars/Philosophy/Model/Tools/Tools.md` | 56-58 | Documentation: the Notion Mirror section of the Tools index. |
| `Pillars/Philosophy/Model/Tools/How Tools Connect.md` | 47-49 | Documentation: narrative section. |
| `Pillars/Philosophy/Knowledge Islands.md` | 117 | Documentation: link in the list of connected tools. |

Proposed change: drop the `.ki.toml` entry; replace the Known Lands row with a retirement line in the pattern of lines 52 and 54, citing the 26 October deletion; remove the Notion Mirror folder and its three inbound mentions, or keep the note marked historical (query MIRROR-NOTE). One Enactment record, or Kris's bounded instruction in the thread, covers the batch.

### ki-agentic-harness (ordinary repository content)

| File | Line | What the reference does |
| --- | --- | --- |
| `skills/repo-structure/ki-repo-mcp/SKILL.md` | 17 | Documentation: sibling list, under the old name `mcp-ki-repo-kb-notion-mirror`. |
| `skills/repo-structure/ki-repo-mcp/SKILL.md` | 53 | Documentation: `notion_mirror` in the fixed `<app>` prefix list. |
| `skills/repo-structure/ki-repo-mcp/references/standards-mcp-servers.md` | 75, 97 | Documentation: prefix table row and the access-level divergence note. |
| `skills/repo-structure/ki-repo-mcp/references/standards-mcp-shared-code.md` | 37 | Documentation: shared-code comparison row. |
| `skills/repo-structure/ki-repo-mcp/references/mode-audit.md` | 15 | Documentation: drift example citing the mirror's `CLAUDE.md`. |
| `skills/repo-structure/ki-repo-mcp/references/sources.md` | 61, 88, 93, 109, 131 | Historical: dated audit evidence. |
| `skills/keystone/ki-repo/references/standards-repository.md` | 319-320 | Documentation: `all=` and `public=` arrays in the `gh` reference plan, old name. |

Proposed change: remove the mirror from the sibling list, prefix list, tables and the `gh` arrays; keep `sources.md` as dated evidence with a one-line note that the repository was deleted on 26 October 2026.

### ki-techne-harness (ordinary repository content)

| File | Line | What the reference does |
| --- | --- | --- |
| `operations/aws/agent-host/host/repositories.txt` | 16 | Live config that will fail: clone list read by `converge.sh`, which logs `fail clone` for the line and continues. |

Proposed change: delete the line. Any clone already on the agent host is a separate, remote clean-up outside this brief.

### apps-knowledgeislands.info, the public website (ordinary repository content)

| File | Line | What the reference does |
| --- | --- | --- |
| `apps/site/src/_data/projects.json5` | 365-392 | Live content: a full project card linking to the deleted GitHub repository, which now 404s. |
| `apps/site/src/_data/arcadiaArchipelago.json5` | 34 | Live content: island list for the archipelago map. |
| `apps/site/src/_data/arcadiaSnapshot.json5` | 94-97 | Live content: snapshot entry with the GitHub URL. |
| `apps/site/src/_includes/ki-design/arcadia-archipelago.svg` | 478-479 | Generated from ki-design: island link to the deleted repository. |
| `apps/site/src/_includes/ki-design/arcadia-archipelago-tall.svg` | 481-482 | Generated from ki-design: same. |

Proposed change: remove the card and the two data entries, regenerate the two SVGs from ki-design after its examples are updated, and rebuild. Whether the card stays as a retired entry is query MIRROR-SITE.

### ki-design (ordinary repository content)

| File | Line | What the reference does |
| --- | --- | --- |
| `packages/hexmap/examples/arcadia-territory.archipelago.json` | 79-81 | Example data with the GitHub URL. |
| `packages/hexmap/examples/arcadia-territory.svg` | 524-525 | Rendered example. |
| `packages/hexmap/examples/arcadia-territory-night.svg` | 524-525 | Rendered example. |
| `docs/design-review/explorations/KnownLands.dc.html` | 357 | Exploration: island list. |

Proposed change: drop the island from the example data and re-render the two SVGs; leave the exploration as historical or update it with the rest, at the ki-design owner's choice.

### hnr-principal and hnr-shared (HNR owns; handoff as a message to `hnr.sop.sites`)

| File | Line | What the reference does |
| --- | --- | --- |
| `Admin/Knowledge Management/KB Specifics/Integrations.md` | 35 | Live binding documentation: names the `hnr-mcp-ki-kb-notion-mirror` server and its tool prefix. |
| `Admin/Knowledge Management/Regular Activities/Mirror/Mirror Sync.md` | 10-19, 50-55 | Activity that calls the MCP; now unrunnable. |
| `Admin/Knowledge Management/Regular Activities/Mirror/Mirror.md` | 18 | Index of that activity. |
| `Admin/Knowledge Management/Regular Activities/Regular Activities.md` | 79 | Index line for the activity. |
| `Admin/Tools/Notion.md` | 25, 38 | Documentation: publish CLI under the older name `mcp-kb-notion-mirror`, the wiki database and the exclusion rule. |
| `.meta/tools/mirror/package.json` | 15-26, 29 | Live config already broken before the deletion: twelve scripts call `mcp-kb-notion-mirror-publish` and the `file:` dependency points at `~/workspaces/knowledgeislands/mcp-kb-notion-mirror`, a path that does not exist. `bun.lock` carries the same. |
| `.meta/tools/mirror/README.md` | 3, 7, 19 | Documentation of the publish workflow and its env names. |
| `.meta/tools/mirror/sync-adr-linear.ts`, `assign-icons.ts` | 15, 235-257; 7, 398-402 | Code reading `kb_notion_mirror_url` frontmatter; still works on the frontmatter alone. |
| `Admin/Knowledge Management/Conventions/Frontmatter Conventions.md` | 36-39 | Documentation of the four `kb_notion_mirror_*` keys. |
| `Admin/Knowledge Management/Integrations/Claude/Live Artifacts/HNR Architecture Tracker Artifact.md` | 37, 54, 78-85 | Artifact spec computing mirror freshness from frontmatter. |
| `Admin/Knowledge Management/Integrations/Claude/Live Artifacts/HNR Streams Tracker Artifact.md` | 47, 88 | Documentation: "no Notion mirror". |
| `Admin/Governance/Outward Sharing.md` | 16, 43 | Governance prose naming the mirror as a sharing route. |
| `Admin/Governance/ADR Consolidation/ADR Consolidation Plan 09 - Wrap-Up.md` | 9, 25, 34 | Plan step to re-run the mirror sync. |
| `AGENTS.md` 25; `Pillars/Pillars.md` 41; `Pillars/Competitors/Competitors.md` 11, 20; `Pillars/Commercial/Commercial.md` 11, 20; `Admin/Knowledge Management/Conventions/Knowledge Base Structure.md` 76; `Admin/Knowledge Management/Enriching the Canonical Knowledge Base/Enriching the Canonical Knowledge Base.md` 40; `Admin/Operations/Activities/Competitor Watch.md` 62 | - | Documentation: "never reaches the Notion mirror" statements and `kb_notion_mirror_exclude: true` flags on the private Pillars. |
| `Streams/Roadmap/HNR-PRINCIPAL-PRD-009`, `PRD-010`, `KM-028`, `KM-032`, `ENG-010` | 32-109; 38, 94; 81; 29; 24, 60 | Historical: work records describing the mirror as a sharing path. Leave. |
| hnr-principal notes with `kb_notion_mirror_*` frontmatter | 13 files | Metadata written by the mirror. |
| hnr-shared notes with `kb_notion_mirror_*` frontmatter (hash, published_at, url, root, exclude) | 272 files | Metadata written by the mirror; the `root` flags are the allowlist the deleted server read. |

Proposed change: a message line to `hnr.sop.sites` saying the server and its repository are gone, so HNR retires the Mirror Sync activity and the Integrations row, marks `Admin/Tools/Notion.md` and the `.meta/tools/mirror` publish scripts historical, and decides whether to strip the frontmatter across 285 notes or keep it as a record of what was published (query MIRROR-FRONTMATTER). The two private-Pillar exclusion flags can go with the rest.

### HNR sites (HNR owns; follow the hnr-principal decision)

| File | Line | What the reference does |
| --- | --- | --- |
| `apps-pt.humansnotrobots.be/docs/kb-mirror.md` and `apps-product.humansnotrobots.be/docs/kb-mirror.md` | 5-15, 154, 160 | Documentation: the "why not the Notion mirror" rationale for the site mirror. Still true, now moot. |
| both sites, `apps/site/src/kb/engineering/bioweave/adrs/index.md` | 88 | Mirrored KB content naming the `kb_notion_mirror_note_status` tool. |
| `apps-sales.humansnotrobots.be` and `apps-sm.humansnotrobots.be`, `AGENTS.md` 17 and `docs/guides/developer/content.md` 63 | - | Documentation: "never reaches the Notion mirror". |

Proposed change: reword at next touch; nothing fails.

### personal-principal (ordinary repository content)

| File | Line | What the reference does |
| --- | --- | --- |
| `Admin/Operations/Live Artifacts/Estate Targets.json` | 679-690 | Inventory: the estate migration target, status done, with old and new paths. |
| `Admin/Operations/Live Artifacts/Estate Map.html` | 28, 34, 38 | Rendered inventory of the same. |
| `acquire/captures/...` (granola and ChatGPT captures) | - | Historical session captures. Leave. |

Proposed change: mark the estate entry removed on the next regeneration of the map, or drop it.

### mcp-gsuite (ordinary repository content)

| File | Line | What the reference does |
| --- | --- | --- |
| `src/tools/{attachments,threads,labels,drafts,messages}/index.ts` | 12, 21, 12, 40, 24 | Code comments: "matching the sibling mcp-ki-kb-notion-mirror convention". |

Proposed change: reword the five comments at next touch; nothing fails.

## In Progress

Nothing is running.

## Queries

### MIRROR-TOKEN - the Notion integration token and 1Password item

**Context:** `mcp-servers.yaml` draws the mirror's token from a 1Password item and chezmoi renders it in plain text into mcporter and Claude Desktop configuration. The server is gone, HNR has moved to publishing through pt.humansnotrobots.be, and this run's transcript saw the token once before masking. The brief forbids touching Notion and credentials, so this is yours.

**Query:** Should the Notion integration behind the mirror be revoked and its 1Password item deleted once the chezmoi change is applied?

**Options:**
a) (recommended, confidence medium - the mirror is retired in HNR's decisions and the token has no other consumer I could find, but I could not check Notion or 1Password) Revoke the integration in Notion and delete the 1Password item after `chezmoi apply` removes the last reference.
b) Keep the item and integration for now, in case the mirror is rebuilt from the deleted repository's history elsewhere.

### MIRROR-NOTE - what happens to the Notion Mirror chapter note in ki-principal

**Context:** `Pillars/Philosophy/Model/Tools/Notion Mirror/Notion Mirror.md` documents a tool that no longer exists, with three inbound links from the Tools index, How Tools Connect and Knowledge Islands. Known Lands records retired islands as a dated prose line rather than a row.

**Query:** Should the Notion Mirror note be deleted with its inbound mentions, or kept as a historical note?

**Options:**
a) (recommended, confidence medium - matches the retirement pattern Known Lands already uses, but Pillars changes are yours under the Enactment Process) Delete the folder and the three inbound mentions, and record the retirement as one dated line in Known Lands, all under one Enactment record.
b) Keep the note with `status: retired - October 2026` and a line saying the repository was deleted, so the model's tool chapter still shows what the mirror was.

### MIRROR-SITE - the public website's project card

**Context:** knowledgeislands.info carries a full project card and two archipelago map entries for the mirror, all linking to a GitHub repository that now returns 404.

**Query:** Should the card and map entries be removed, or should the card stay as a retired project without the repository link?

**Options:**
a) (recommended, confidence high - a public card linking to a 404 misleads readers and the site has no retired-project shape today) Remove the card and the two data entries, regenerate the SVGs from ki-design and rebuild.
b) Keep the card marked retired with the link removed, adding a retired state to the site's project schema.

### MIRROR-FRONTMATTER - the 285 notes carrying mirror frontmatter in HNR

**Context:** 272 hnr-shared notes and 13 hnr-principal notes carry `kb_notion_mirror_*` keys written by the server: hashes, publish timestamps, Notion URLs, root flags and two exclusion flags. HNR's Notion removal is trashing the mirrored pages leaf to root, so the URLs will soon point at trashed pages. The `.meta/tools/mirror` scripts and the Architecture Tracker artifact read `kb_notion_mirror_url`.

**Query:** Should the handoff to `hnr.sop.sites` ask HNR to strip the frontmatter keys, or leave them as a record of what was published?

**Options:**
a) (recommended, confidence medium - the keys will be dead once the Notion pages are trashed and the Frontmatter Conventions note would need rewriting either way, but HNR owns the choice and its removal work is mid-flight) Ask HNR to strip the five keys in one bounded run after the Notion removal finishes, updating Frontmatter Conventions and the two scripts that read them.
b) Leave the keys in place as published-history evidence and only retire the activity, the Integrations row and the publish scripts.
