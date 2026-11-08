# KI > Techne > Agora › settle

**🤖 → 👤 Handoff to supervisor · Run report at 03:56 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- When both Macs change the same repository at once, such as the dotfiles the two households share, the Mac that got in second now hears from Agora within about a minute, in plain words: "terra went first at 9e3b1f0; bring your 2 commits in on top of it, then push". Agora still never merges or pushes for anyone.
- Each Mac can now see when the other one has to settle. It shows in the tray, in the shared state and in the read endpoint.
- Agora's log now says how many seconds each push took to reach the other Mac, so "within seconds" can be checked rather than assumed.

## Done

- **Push reaching the other Mac (task 1).** The `pushed` signal path already works on the live installed Agora. Tonight's log on sol shows terra's dotfiles, ki-principal and inbox pushes fetched and fast-forwarded here about 1.5 to 2 seconds after the signal arrived. No news has been left to the 15-minute fallback since the log began. Two improvements are now in the code:
  - The signal carries the time Git recorded the push. Each Mac logs when it heard the signal and when its checkout held the commit, for example `… is at 3a50509 here 2s after terra pushed it`.
  - Another clone of the same repository on the pushing Mac is fetched straight away, rather than at the fallback.
- **Settle call (task 2).** A kept checkout that is diverged, or dirty and behind, gets about a minute to come right on its own. After that, Agora calls the package that owns it, once for each commit the other side went first at, with the line `settle: <repo> on <Mac>: <who> went first at <commit>; bring your <n> commits in on top of it, then push`. For uncommitted work the line says "your uncommitted changes" instead. The owning package is the one watched in that checkout on this Mac, narrowed by the commits' `Work-Id:` trailers in the same way as `ahead, push it`. On sol, the live configuration maps `~/.local/share/chezmoi` to personal.reg.household-sol. "Who went first" is the peer whose `pushed` signal named that commit, or "the other side" when no peer did. When the checkout comes level again, the log says `<repo> has settled`.
- **Shown to both households (task 3).** The tray's checkout line reads `diverged: ahead 2, behind 1, settle on 9e3b1f0`, and a one-time "A checkout must settle" notice names who went first and who was called. The picture each Mac shares with the other, `state.json` and the read endpoint now carry a `settles` list, and the other Mac's disagreement line says `terra must settle …`. README, AGENTS.md (the Keeping level duty), How Agora works and the view API documentation are updated.
- **Commit and checks.** `c6ba5e1` (feat: call the owning package to settle a checkout the other side went first on, and time each push) is on `main`. `bun run self:check` passed. `bun run test` passed 243 of 243 after the rebase, using only the suites' own temporary repositories.
- **Choices I made:**
  - The call waits for the same settle time as `ahead, push it`, about a minute, so a thread already rebasing is not interrupted.
  - "Once per new state" means once for each upstream commit the other side went first at. A new local commit while the household is already settling does not ring again; a new push from the other side does.
  - A checkout that no package on this Mac owns calls no one. It is still shown and shared.
  - The settle call does not wake an Orca thread. The wake line stays the one fixed line, as for `ahead, push it`; a listening thread hears it through its call file.
  - Which settles have already been called is held in memory only, so a restart re-calls a checkout that is still unsettled, once.
  - I worked in a temporary worktree, now removed, because the mark-all, spec and roster runs were editing the same files in the main checkout. I rebased onto their commits and resolved two documentation conflicts, keeping both sides.

## In Progress

- **The roster run has to bring this commit in on top of its own work.** Its uncommitted changes in the main checkout touch `src/state.ts` and `src/review.ts` in the same places this commit changed: `Review.self` now takes the settles, and `RigState` and `parseRigState` now carry `settles`. Expect a small conflict when it pulls with rebase. Keep both fields.
- **The households need to install the new build** for the settle call to run. The installed Agora is still the older one.
- **Possible roadmap records** (not created):
  - Store which settles have been called in Agora's state folder, so a restart does not call again.
  - Time the watched packages' fetch separately from the 15-minute fallback, so a change made where no Agora runs (a cloud agent, GitHub on the web) arrives sooner.

## Queries

None.

🧵 ki.prj.agora
