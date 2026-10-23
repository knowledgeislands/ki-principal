# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › radar-design

**🤖 → 👤 Handoff to supervisor · Run report at 08:22 BST · last mark 23:56 BST (21 October)**

---

## Done

- I read the whole Rig catalogue: 190 tools, 2 skills, 3 retired applications, 5 services and 10 jobs. I also read the tools-rig specifications, ADR-KI-TOOL-RIG-008 and its roadmap, the Rig site's data pipeline, the `ki-self` lifecycle, the purpose worksheet, [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md), [KB-DOTFILES-UE-104](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-104-evaluate-starship-with-chezmoi-drift.md), and the ki.chezmoi decisions from this session (TERMINALS, orca-eval, RIG-APP-FOOTPRINT).
- I wrote the draft design and a first placement of every tool, both below. I made no commits, changed no files in any repository and ran no gate, because this run was read-only.

### Facts the design rests on

- **Rig rejects unknown keys.** Under RIG-CONF, Rig rejects any key it does not know, so a ring field in `conf.d/` cannot exist until tools-rig adds it to the schema.
- **The public export carries a fixed list of fields.** RIG-PUB-002 limits it to id, name, purpose, rationale, platforms and relationships, so the site cannot show a ring unless the export carries one.
- **Retired applications stay private.** `[retired-application]` already exists. It is inert, never installs anything, and RIG-PUB-012 keeps it out of every export.
- **`rig doctor` has no notion of an optional tool.** RIG-STATE-013 says so, and it has no dates either.
- **The site has a place waiting for this.** It pulls `rig export --profile public`, `rig show` per host profile, and curated `tool-links.json` and `hosts.json`. The `Exported` interface already has a `comment` slot that "Rig does not export yet".
- **A trial is already recorded by hand.** Orca's trial sits in its rationale ("Evaluating, 22 October 2026: …"), which is what a ring field should replace. Decision 179 keeps rationale for reasons only.
- **Unselected entries already work as a watch list.** `profiles = []` means declared but not installed: `chatgpt-current`, `rekordbox`, `tigervnc` and `paperclip`.
- **iTerm2 and Motion were never in the catalogue.** They were unmanaged apps on the KB-DOTFILES-UE-086 removal list. The catalogue has no record of anything that was never declared.

### Draft design

**Rings.** There are four rings on the radar plus one state off it. The words are Thoughtworks', and each maps onto one lifecycle state:

| Ring | Lifecycle state | Meaning | Catalogue shape |
| --- | --- | --- | --- |
| Adopt | adopted | The chosen tool for its job, used by default | Selected in `core`, or in a host profile by design (DaVinci on studio, The Tower on laptop) |
| Trial | evaluating | Installed for real use on a bounded profile until a review date, against named checks | Narrow profile, usually `laptop`. Needs `review.by` and `review.checks` |
| Assess | candidate | Worth a look but not installed. It may exist only as a roadmap record or a disposable kit | `profiles = []` (catalogue-only), or not declared at all |
| Hold | retiring | Still installed and allowed to run, but nothing new starts on it. A replacement is named or the removal step is pending | Keeps its profile until removal. Optional `replaced-by` and `review.by` |
| _(off the radar)_ | retired | Gone. Its remains can be watched | Declaration deleted. `[retired-application]` added where leftovers matter |

The ring is separate from the profile. The ring says how sure Kris is about a tool; the profile says where it runs. Three rules connect them, enforced by this repository's tests rather than by Rig:

- a Trial tool is never in `core`;
- an Assess tool is never selected;
- a Hold tool gets no new Dock item, default handler or service.

Services, scheduled jobs, settings and the Dock carry no ring, because they are operations rather than tool choices. Skills do carry one.

**Dated reviews.** Each review has three fields: `review.by = "2026-11-05"` (an ISO date), `review.checks` (short strings, for example `"replaces Delta for daily agent review"` or `"telemetry stays off after updates"`) and an optional `review.record = "KB-DOTFILES-UE-NNN"`. Trial requires `review.by`, and Hold may carry one as its removal deadline. The proposed default is two weeks for an application, set when the trial starts.

**Lifecycle.** The `ki-self` checklist's step 2 ("decide whether adopted, retired, or merely an alternative") becomes "set the ring". Each move has a defined action:

| Move | What happens |
| --- | --- |
| Assess → Trial | Declare the tool on a narrow profile and set the review fields |
| Trial → Adopt | Widen the profile, clear the review fields and write the reason into the rationale |
| Trial → retired | Delete the declaration and run the native uninstall, which needs its own approval |
| Adopt → Hold | Name the replacement and set a removal date |
| Hold → retired | Delete the declaration and add `[retired-application]` if leftovers are likely |

The weekly review in KB-DOTFILES-HK-003 gains one step: walk the Trial and Hold rings.

**Doctor or an audit.** `rig doctor` would report a selected tool whose `review.by` has passed as a `review-overdue` finding: owner `catalogue`, action "adopt, extend `review.by`, or retire". Bash 3.2 can compare ISO dates as strings, and doctor stays read-only. A Hold tool past its date would get the same finding, and an unexpired Hold would show only as information. Until tools-rig ships this, `tests/rig-catalogue.test.mjs` cannot see dates, so the interim check is the HK-003 walk.

**Rig site.**

- Each row and card gets a ring badge.
- A ring chip joins the filters, beside area and host.
- A fourth view, Radar, joins Table, Gallery and Sections. It shows rings as rows and the 12 categories as groups. A circular plot does not fit 12 categories well.
- A Hold tool reads "replaced by Ghostty" wherever the replacement is public.
- Trial and Hold tools are published only if they opt into `public`. Orca does not today.
- Retired tools stay off the site, in line with RIG-PUB-012.

### First placement

† marks a placement I am unsure of. It rests on catalogue text and this session's decisions, not on usage data.

**Applications (97)**

| Ring | Tool | Reason |
| --- | --- | --- |
| Adopt | Ghostty | Primary terminal under the TERMINALS decision (22 Oct) |
| Adopt | Claude, Claude Code, Codex | The working agents |
| Adopt | CodexBar | Usage limits in the menu bar. Orca covers this only while it is open |
| Adopt † | GitHub Copilot CLI | A third terminal agent, and its use is unknown |
| Adopt | ChatGPT Classic | The ChatGPT app in use |
| Assess | ChatGPT current | Declared as a "packaging watch item", unselected |
| Trial | Orca | Laptop only since 22 Oct, to be weighed against Delta, CodexBar and GitHub Desktop |
| Hold † | Delta | Orca would replace it. Moves to retired if Orca is adopted, or back to Adopt if not |
| Hold | Warp | Retiring for Ghostty. Its uninstall is staged as an attended step |
| Adopt | Zed, Visual Studio Code | Zed is the main editor. VS Code keeps the extension ecosystem † |
| Adopt | Beyond Compare | The main diff and merge tool |
| Hold † | Meld | A second diff tool alongside Beyond Compare |
| Adopt † | GitHub Desktop | Orca covers part of it |
| Trial † | GitButler | Stacked branches. The Git client choice after GitUp's retirement is still open |
| Hold † | Sourcetree | Third Git client. Nothing in the catalogue gives a reason to keep it |
| Adopt | Git Almanac, Rig, rumdl, Obscura, LaunchControl, Redis Insight †, UTM, CrossOver, ThinLinc † | Each has a single job and none overlaps another |
| Hold † | TigerVNC | Declared but unselected |
| Adopt | Alfred, Actions, Amphetamine, BetterDisplay, DisplayLink, DaisyDisk, Apple Configurator, iMazing, ProcessSpy, Tower Assistant | System tools with distinct jobs |
| Hold | Path Finder | Its rationale says the Finder replacement is still open, and it names ForkLift as the Assess candidate (not declared) |
| Adopt | Activity Monitor, Finder, Messages, Notes, Photos, Preview, System Settings | macOS built-ins, kept as reference points |
| Adopt | Granola, FluidVoice †, Ollama † | Meetings, dictation and local models. FluidVoice and Ollama overlap `openai-whisper` and see little use, as far as I know |
| Adopt | Obsidian, Notion, Linear, TickTick †, Raindrop.io, Goodnotes, Spark Desktop | Knowledge and task work. Spark is the default mail app |
| Adopt | Microsoft Word, Excel, PowerPoint, Outlook, Teams; Pages, Numbers, Keynote | Both suites are needed for client work |
| Adopt † | Diagram | A second diagram app beside draw.io |
| Adopt | draw.io | Diagrams as local files |
| Adopt | Google Chrome, Google Drive, OneDrive, Hazel | Browser, the sync stores and file automation |
| Adopt | 1Password, 1Password CLI, Tailscale, NetSpot, WiFi Explorer † | Security and networking. The two Wi-Fi tools overlap |
| Hold † | NordVPN | NORDVPN-HOLD went to ki.mac-studio-setup |
| Adopt | Slack, Discord, Zoom, Telegram, WhatsApp | Communications. The WhatsApp pipeline depends on WhatsApp |
| Adopt | Spotify, Sonos, GarageBand, VLC, Amazon Kindle | Media |
| Hold † | Rekordbox | Declared but unselected |
| Adopt | OBS, HandBrake, ImageOptim, iMovie, Insta360 Studio, DaVinci Resolve (studio) | Photography and video |
| Adopt | Home Assistant, HP | Home and printer |
| Adopt | The Tower, RendApp (laptop) | Laptop by design, not a trial |

**Command-line tools (93)**

| Ring | Tool | Reason |
| --- | --- | --- |
| Adopt | Starship | Adopted 22 Oct under Decision 204 |
| Hold † | git-radar | Starship replaces it. It stays only for the fallback prompt in `99_prompt` |
| Adopt | mise, Node.js, Bun, Python, uv, Rust, Zig, cargo-binstall, cargo-edit, cargo-nextest, cargo-outdated, cargo-watch, cargo-zigbuild, actionlint, git-cliff, lychee | Runtimes and tools that mise manages |
| Adopt | npm, Corepack, TypeScript, Turborepo, Wrangler, npm-check-updates, ImageOptim CLI, Skills CLI | npm tools that current repositories use |
| Adopt | Claude Swap, Headroom, Codex Multi Auth † | Agent account and context tools |
| Adopt † | Paperclip, Paperclip agent configuration | In use, but the base catalogue leaves them unselected |
| Adopt | dockutil, mas, chezmoi, ki, mgit, mcporter, gh, git, git-extras, git-filter-repo, git-lfs, granted, memo | The workstation's own machinery |
| Adopt | ripgrep, fzf, jq, tree, curl, wget, coreutils, rename, z, pandoc, poppler, exiftool, ffmpeg, imagemagick, media-info, tesseract, yt-dlp, graphviz, shellcheck, bats-core, swaks, nmap, dnstracer, pinentry-mac | Everyday utilities |
| Adopt | zsh, zsh-autosuggestions, zsh-completions, zsh-autocomplete †, readline | The shell and its libraries |
| Adopt | awscli, kubernetes-cli, helm, k9s | Cloud and cluster work |
| Hold † | ack | ripgrep does the same job |
| Hold † | adr-tools | KI Decision Records now follow `ki-decision-records` |
| Hold † | rbenv, ruby-build | They duplicate mise's runtime role |
| Hold † | gerrit-tools | No current Gerrit work in the catalogue |
| Hold † | deno | Bun is the KI runtime |
| Assess † | herdr | A terminal multiplexer for agents, overlapping Orca |
| Assess † | summarize | An AI extraction tool with no stated use |
| Adopt † | gcc, llvm@20, protobuf, onnx, pytorch, openai-whisper, platformio, merve | Build and machine-learning stacks. Each needs a named consumer, or it moves to Hold |

**Skills (2)**

| Ring | Skill | Reason |
| --- | --- | --- |
| Adopt | Caveman | Reviewed, and kept for compact communication |
| Adopt † | Archify | Reviewed and in use, but recent |

**Recent retirements (off the radar)**

| Tool | Retired | Reason |
| --- | --- | --- |
| GitUp and the `gitup` formula | 22 Oct | Retired from Rig |
| iTerm2 | Removing (B6c and C7c) | Never declared. Replaced by Ghostty |
| Motion | Removed on terra 22 Oct | Never declared |
| Adobe Photoshop, Lightroom Classic, Creative Cloud | 15 Oct | Watched as `[retired-application]` |
| Shadowlab Spark launcher | 20 Oct | Retired from Rig |

The KB-DOTFILES-UE-086 removal list also holds unmanaged apps that were never declared and need no ring: Fileside, Tagception, Webex, OneNote, Nitro, BlueStacks, Clockology and Prime Video.

Summary: 39 placements are marked † for Kris to confirm. Holding the overlap pairs would shrink the catalogue: Meld, Sourcetree, git-radar, ack, rbenv and deno.

## In Progress

Nothing is running. ki.chezmoi would hand over three parts once RADAR-DESIGN is decided:

- **tools-rig** (a new KI-TOOL-RIG-CORE record, not reserved by me):
  - optional `ring`, `review.by`, `review.checks`, `review.record` and `replaced-by` on `[tool]` and `[skill]`, with validation (Trial requires `review.by`, `replaced-by` must name a known tool);
  - `rig show` displays them, and `rig doctor` reports `review-overdue`;
  - the export adds `ring` and a closure-filtered `replaced-by`, with `review.by` optional under RADAR-PUBLIC;
  - spec changes in catalogue.md (a new RIG-CAT entry), RIG-STATE-013 and RIG-PUB-002 and -004;
  - an ADR on the ring vocabulary, then help, man and completion alignment.
- **Rig site** (KB-MIDNIGHT-RIG-SITE-002):
  - read `ring` from `rig.json` and add it to the `pull.ts` allow-check;
  - add the badge, the ring filter, the Radar view and "replaced by";
  - add tests.
- **chezmoi**:
  - ring values on all 192 entries, with the review fields moved out of Orca's rationale;
  - the three ring-and-profile rules in `tests/rig-catalogue.test.mjs`;
  - the `ki-self` lifecycle checklist update and the radar step in HK-003.

## Queries

**RADAR-DESIGN** (Needs: decision)

**Context:** Rig rejects keys it does not know, its export lists fixed fields, and `rig doctor` lives in tools-rig. So the ring can only show on the site and be checked by doctor if tools-rig carries it. The `ki-self` lifecycle also says this repository keeps no second catalogue in front of Rig.

**Query:** Where should the ring live?

**Options:**

a) (recommended, confidence high - the only option that supports doctor, the site and the single-catalogue rule together) Make it both. tools-rig owns the vocabulary, the review fields, doctor's `review-overdue` finding and the export field. chezmoi owns the values and the ring-and-profile rules. The site owns the display.

b) A personal sidecar file, `dot_config/rig/radar.toml`, outside `conf.d/`. chezmoi tests check it, and the site's pull reads it next to `tool-links.json`. It needs no tools-rig change, but it is a second catalogue that can drift, and doctor cannot see it.

c) An interim with today's grammar: three view profiles (`radar-trial`, `radar-assess`, `radar-hold`), each listed in a tool's `profiles`, with dates kept in roadmap records. The site could show rings now, but view closure rules may force dependencies into each view, profiles get crowded, and there are still no dated doctor findings.

**RADAR-PUBLIC** (Needs: decision)

**Context:** The site shows what the `public` view exports. Orca, the one Trial tool, is laptop-only and not public, and retired tools must stay private under RIG-PUB-012.

**Query:** How much of the radar should rig.midnight.ninja show?

**Options:**

a) (recommended, confidence medium - shows the direction of travel without publishing private dates or history) The ring and "replaced by" for public tools, with no review dates or checks and no retired list. Trial tools appear only when they opt into `public`.

b) The ring, review dates and checks for every public tool.

c) The ring only, with nothing about Hold replacements.
