# KI > Techne > Agora › roadmap-jobs-views

**🤖 → 👤 Handoff to supervisor · Run report at 20:17 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The Agora app has a **Roadmap** page. On the left is a summary of counts by territory, island, area or priority against status, and clicking any count, row or status filters the list. There are filter menus and chips for status, priority, horizon, area, size, territory and island, plus a word search and the record table. Clicking a record opens its details, Goal and Context in the right-hand tray, with **Open the file**.
- It also has a **Jobs** page. Every scheduled job and service Rig declares is grouped by territory, then repository, with its schedule in words, the Macs that run it, its last run and how it went. The tray shows the declaration and each Mac's recent runs. The page only shows jobs; running them stays with Rig.
- The installed apps don't have the pages yet. They appear once the household updates Agora on each Mac. Until then the app reads this Mac's jobs itself, and terra's appear once its Agora is updated.

## Done

- Roadmap and Jobs pages added in one commit, `f9b10f4` (`feat(app): add Roadmap and Jobs pages with filters and a details tray`), pushed to `main`.
- Choice: roadmap records are read directly from each island's `docs/roadmap/` or `Streams/Roadmap/` front matter by a pure, tested parser. The app refreshes them whenever it rereads the lands, every 3 minutes. I didn't use `ki` because it has no JSON record listing (`ki link` prints links only). I didn't use the Observatory's `/api/roadmap` because it has no priority, size, territory or record text, and it only works while its service runs.
- Choice: each Mac's Agora reads its own jobs at its review, at most once a minute, and shares them with the other Mac the same way Accounts does. The sources are Rig's declarations (`~/.config/rig/conf.d/*.toml`), `rig show --format json` for what runs on that Mac, and the scheduled-jobs reporter's records. A job's environment, arguments and output are never read. The jobs register household-sol planned (`.chezmoidata/jobs.yaml`, AGORA-JOBS) doesn't exist yet, so it isn't read.
- Choice: a job is placed by its declared working directory. A job with none sits with the chezmoi source, where Rig's own jobs are declared. A job outside every territory goes under Elsewhere.
- Choice: a Mac that hasn't shared jobs, a Rig that can't be read and a missing roadmap each show as a quiet notice.
- Updated the view API docs and example (`jobs` field), `docs/design/agora-app.md`, the README and AGENTS.md (a "Jobs, read only" boundary). Added the module boundaries and two development-check variables (`AGORA_APP_RECORD`, `AGORA_APP_JOB`).
- Checks: `bun run self:check` passed. `bun run test` passed (43 files, 427 tests, 28 new). I checked both pages with development screenshots in a separate capture profile; the installed apps weren't touched.

## In Progress

- Nothing in progress. Possible follow-up records, not created:
  - Agora judging a job overdue against its schedule, as the Observatory does.
  - A failed or overdue job raising the toolbar's "need a look".
  - Reading the household's jobs register once it lands.
  - Showing whether each service is actually running.
  - The Observatory's `/api/roadmap` carrying priority and size.

## Queries

None.

🧵 ki.prj.agora
