# KI > Techne > Agora › guilds-view

**🤖 → 👤 Handoff to supervisor · Run report at 20:28 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The Agora app has a **Guilds** page. Guild badges run across the top. Each one shows a monogram, the guild's name, a line on what it is about and a bank of skill badges. Click a skill and the pane below shows its `SKILL.md`, with one tab for each document and folder inside it, such as `references/`, `scripts/` and `assets/`.
- The guilds are provisional and the page says so: each is a folder that a harness sorts its skills into. The guildmaster's package, ki.reg.guilds, has not yet set out which skills belong to which guild. Its role catalogue brief only defines a guild as "a set of skills, such as change management". So one module, `src/app/guild-catalogue.ts`, holds the whole mapping, and that module is all the guildmaster's catalogue needs to replace.
- It finds 15 guilds and 77 skills across 8 harnesses: the 8 folders in ki-agentic-harness, plus one guild for each other territory's own unsorted skills.

## Done

- **Guilds page** (`4adbf38`, pushed):
  - The page has a row of guild panels, each with its badge, name, a line on what it is about, a skill count and a bank of skill badges.
  - A word search finds skills by name, description or guild.
  - The skill pane shows the skill's guild and harness, its description, the rest of its front matter and its body drawn as formatted text.
  - A folder tab lists its files beside the chosen file. A link to another of the skill's own files opens that file.
  - Binary files, and files over 256 KB, are named but not shown. Escape closes the pane.
- **Reading:** read-only, from each `*-agentic-harness` island on the lands. It handles both `skills/<guild>/<skill>/` and `skills/<skill>/`, and refreshes each time the app reads the lands, about every three minutes.
  - A harness without a `skills` folder gives a quiet notice, and so do lands with no harness on them.
  - A file is opened only if it is inside a skill that was read. Paths that climb out of the skill, and links pointing out of it, are refused.
  - Markdown is drawn as page elements, never as raw HTML.
- **Choices:**
  - Guild descriptions are my own one-line wording for the 8 folders.
  - Each other territory's unsorted skills form one guild named "<Territory> skills".
  - A guild with no logo gets a two-letter monogram on a colour that stays the same for that guild. The page will show a logo once the catalogue supplies one as a `data:` image.
  - The Portal does not carry skills. The app reads this Mac's harnesses itself, like the Roadmap page does.
- **Docs:** the Guilds section, the module table rows, the development switches `AGORA_APP_SKILL` and `AGORA_APP_SKILL_TAB`, and a screenshot are in `docs/design/agora-app.md`. The README lists the new place.
- **Checks:**
  - `bun run self:check` passes. The only warnings are 22 CSS ordering warnings that were already there.
  - `bun run test` passes: 461 tests in 49 files, including new suites for guilds, Markdown and skill reading against their own temporary folders.
  - A development screenshot confirmed the row, the pane and a folder tab, in night and day themes. No installed app was touched.
- **Incident:** partway through, I ran `git stash` on the shared checkout by mistake. Another session's edits were uncommitted there at the time. I popped the stash straight back, with no conflict and nothing lost. That session later committed its own work cleanly, and my commit holds only my paths.

## In Progress

- Nothing is running.
- Candidate home for guild logos and descriptions, for ki.reg.guilds to own (not created): `skills/<guild>/GUILD.md` in each harness. Its front matter would give `title` and `about`, with a `logo.svg` beside it. `guild-catalogue.ts` would then read those files instead of its fixed list. The alternative is one `skills/guilds.toml` per harness.
- Candidate roadmap records (none created):
  - Read the guildmaster's catalogue once it exists, including guilds that span several harnesses.
  - Show which roles or seats use each guild's skills.
  - Count a skill's dependencies (`ki-depends-on`) and draw them as links between badges.

## Queries

None.

🧵 ki.prj.agora
