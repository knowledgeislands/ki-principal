# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › purpose-render

**🤖 → 👤 Handoff to supervisor · Run report at 05:12 BST**

---

## Done

- The Rig table now follows Decision 179. Commit `4701e8f` in `apps-rig.midnight.ninja` is on `main`, local only and one ahead of `origin/main`.
  - The "Why it is here" column and "No reason written yet" are gone from all three views: Table, Sections and Gallery.
  - Each row names the tool with its kind and install route underneath, for example "Application · Homebrew cask", then gives its purpose in one line.
  - The page shows a comment as subtext only when Rig supplies one. No comment means no subtext and no placeholder.
- **Where the kind was lost.** The site never had it. Rig's public export has never carried a tool's kind or install route, because its publishing spec deliberately leaves out providers and installation metadata, and `pull.ts` blocks those fields. The kind (cask, formula, mas) exists only in the declarations' `install.provider` and `install.kind` fields. It was called `kind = cask` before chezmoi commit `fd7c3b4`.
- **How it is restored.** `self:rig:pull` now reads each public tool through `rig show <id>` and writes `data/install.json`. That file holds only the provider, the install kind, whether the tool is an application bundle, and whether it comes with macOS. It never holds a locator or a path. The site works out the kind from that: an application bundle is an Application, anything else a provider installs is a Command-line tool. The 10 tools with no provider show as "Installed outside Rig", and macOS's own apps as "Part of macOS". `AGENTS.md` records this as a narrow widening under Decision 179, like the hosts.
- **The five sample tools**, from the built page (screenshot: [purpose-render.table.png](/Users/krisbrown/.local/state/ki/agents/rigsite/purpose-render.table.png)):
  - Zoom: Application · Homebrew cask. "Video meetings where Zoom is the required platform."
  - ack: Command-line tool · Homebrew formula. "Provide the ack Homebrew package for the workstation."
  - ChatGPT Classic: Application · Homebrew cask. "General AI conversation, voice, research, and desktop assistance."
  - Claude Code: Command-line tool · Homebrew cask. "Anthropic's primary terminal coding agent."
  - Codex: Application · Homebrew cask. "OpenAI's primary coding agent and desktop development workspace."
- Checks: type-check passed; tests passed (31 site, 14 view-common), including new tests that the install data names only public tools, holds no locator, and that the page shows no reason column or placeholder; Biome and rumdl clean; the commit went through the repository's hooks. No dev server ran, no `.git` lock is left, and nothing was pushed, deployed or applied, and chezmoi and tools-rig are untouched.

## In Progress

- The pull also refreshed `rig.json` and `host-tools.json`. I put both back as they were, because refreshing the data is the weekly MIDNIGHT-HK-001 job and the rig-purpose rewrite has not reached the live Rig config yet. The only change it brought was dropping Paperclip, which is now off every machine. Until the next refresh, Paperclip shows with no kind or route line.
- Purposes still read the way the declarations do now, for example ack's "Provide the ack Homebrew package…". The rig-purpose rewrite will reach the page at the next refresh, after `chezmoi apply`.
- My scratch folder (`/var/folders/…/ki-agents/rigsite/purpose-render/`) still holds the screenshot working copy and a Chrome profile, because removing it was not approved. It is safe to delete, and `ki agent close` will refuse until it is empty.

## Queries

**1. A field for the comment**

**Context:** Rig has two text fields, purpose and rationale. The rationale is the reason Kris asked to drop, so the page has nothing to use as a comment and shows none. The page will show a `comment` field as soon as Rig exports one.

**Query:** What field should tools-rig add for the comment?

**Options:** a) (recommended, confidence high - this is a small change to the spec and the export, and the site already reads `comment`) Add an optional `comment` string to tool declarations, and add it to the publishing spec's allowed fields so `rig export` carries it. b) Show the rationale as the comment. c) Keep the comments in this site, in a curated file like `tool-links.json`.

**2. Where the kind and install route should come from**

**Context:** The site currently reads the kind and install route from `rig show`, one tool at a time. That makes the pull take about two minutes, and it relies on Rig's display text ("homebrew (cask: zoom)"), so a wording change in Rig could break it. Rig also has no field that says what kind of thing a tool is, so the site works it out; for example, Node.js, Bun and Python show as "Command-line tool".

**Query:** Should Rig export these itself?

**Options:** a) (recommended, confidence medium - it is the most robust option, but it changes Rig's public-data boundary, which only Kris can decide) Change the publishing spec so `rig export` carries the provider and install kind but never the locator, and add a declared `kind` (application, command-line tool, runtime, …) to tools. b) Keep it as it is in the site, using `rig show`. c) Ask Rig for a structured install field in `rig show --format json` and leave the export unchanged.

**3. The "Awaiting a rationale" filter**

**Context:** The page no longer shows reasons, but the "Awaiting a rationale" stat, its filter and the "to write" counts in the area strip are still there, so the page still lists the entries under rationale review.

**Query:** Should those stay now that the reason column is gone?

**Options:** a) (recommended, confidence medium - it is still useful while the rationale review is open, and it costs nothing) Keep them until the review finishes, then remove them. b) Remove them now.
