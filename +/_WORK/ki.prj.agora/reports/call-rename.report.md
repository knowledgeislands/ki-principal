# KI > Techne > [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › call-rename

**🤖 → 👤 Handoff to supervisor · Run report at 03:45 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- Agora's call has its name: each agent's call now lands in `~/.local/state/ki/agora/call/<work-id>`. Agents still waiting on the old `doorbell/` path keep working until 20 November.
- "Ahead, push it" is quiet now. It waits about a minute, so a commit another session pushes straight away calls no one, and in a shared checkout such as ki-principal only the agent whose `Work-Id` is on the commits hears it.
- Agora leaves alone any checkout an agent is working in, and each run in the view now lists the checkouts it is using.
- The territory list is simpler. Agora takes what `ki territory roots` gives it and names any member `ki` warns about.

## Done

- **Agora's call (AGORA-CALL).** I renamed the doorbell to Agora's call across apps-agora.local: the state folder, the code, the tests, the view, the tray and log wording, the README, `AGENTS.md`, the view schema doc, the example config and the changelog.
  - Agora writes each call to `call/<work-id>`, and the same line to the old `doorbell/<work-id>` while the transition lasts.
  - The README says the old path stops with the first Agora built after 20 November 2026.
  - The view adds `calledAt` and keeps `doorbellAt` beside it with the same value, so the view stays `agora/view/v1`. Its own rule makes a rename a new version, and no viewer reads the field. The Observatory does not use it.
  - The `ring` message between rigs keeps its name, so older peers still understand it.
- **Territory listing (TERRITORY-NAMES).** I removed the fallback that read territories through `ki territory show` and mGit. Each `ki: warning:` line from `ki territory roots` now becomes a named member that is not kept, and the Territories menu shows it.
  - `[sync] workspaces` is no longer read. A config that still sets it gets a log line at start rather than an error.
- **Runs as JSON.** Runs now come from `ki agent status --format json` (`ki/agent-status/v1`), each with the checkouts its agent may be working in.
  - Runs from an older peer are still accepted, with an empty checkouts list.
  - The view shows each run's checkouts.
  - **Run guard:** I added this from the backlog's TERRITORY-NAMES item (AGORA-RUN-GUARD). A clean checkout that is only behind is not fast-forwarded while a running agent lists it. The log names the run, and the checkout catches up once the run ends.
- **Ahead, push it (AHEAD-RING-NOISE).** Agora now waits 60 seconds at the same head, fetches and re-reads, and calls only if the checkout is still clean and only ahead.
  - It calls only the watched packages named in the unpushed commits' `Work-Id` trailers.
  - **My choice:** if any unpushed commit has no `Work-Id`, every package watched in that checkout is called, which is today's behaviour. If the commits name only packages not watched here, no one is called and the log says so.
- **Listening values (LISTEN-HOW).** Agora does not yet report how an agent listens anywhere. So the four values, `agora-call`, `poll`, `on-open` and `off`, are written into the README's Agora's call section with their meanings, crediting personal.reg.inbox-sol for the wording. The roster slice should use them when it reads the `workers:` register.
- **Inbox ids (INBOX-RENAME).** README examples, the example config, the view example, fixtures and tests now use `krisb/inbox`, `~/kis/personal/inbox` and `personal.reg.inbox-*`. Roadmap and design records were left as they are, since they are history.
- **Tests:** there are new tests for the call and its old path, the 60-second wait (a commit pushed in time calls no one), routing by `Work-Id`, the run guard, reading runs from JSON, and territory warnings.
- **Commit:** `659d20f` "feat: rename the doorbell to Agora's call, with small fixes", pushed to `origin/main`.
- **Checks:** `bun run self:check` passed; `bun run test` passed (225 tests); the commit hooks passed.

## In Progress

- **The installed Agora still uses the doorbell path.** `~/Applications/Agora.app` keeps writing only `doorbell/` until the households install this build, which this run did not do. Live agents should move their waits to `call/<work-id>` after that install and before 20 November. Telling them is for the coordinator; this run started no agent and sent nothing.
- **Roadmap candidates (no records created):**
  - stop writing `doorbell/` and drop `doorbellAt` from the view after 20 November 2026, as `agora/view/v2` if it ever matters;
  - show each agent's listening value from the `workers:` register in the roster;
  - start the run guard before the first sync after a restart. Today the first sync runs before the first review has read any runs, and `ki agent status` takes about 20 seconds, so that one sync is unguarded.

## Queries

None.

🧵 ki.prj.agora
