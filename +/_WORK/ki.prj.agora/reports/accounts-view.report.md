# KI > Techne > Agora › accounts-view

**🤖 → 👤 Handoff to supervisor · Run report at 19:58 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The Agora app has a new **Accounts** page: each Mac's Claude accounts (from cswap) and Codex accounts (from codex-multi-auth), with which one is active on that Mac, 5-hour and 7-day usage with reset countdowns and pace, per-model limits, and login expiry flagged when expired or within 48 hours.
- "Cloud Multi-Auth" is **codex-multi-auth**, your Codex account manager (chezmoi's ADR-PERSONAL-DOTFILES-007). It is read as the second source, through its offline cached `limits --json`, which already masks emails.
- You won't see it until the Portal and app are rebuilt and relaunched on both Macs. I didn't install or relaunch anything.

## Done

- `41e52da` feat(accounts): each Agora reads `cswap list --json` and `codex-multi-auth limits --json` at its review, never more than once a minute. Each reading is cut down to alias, organisation, plan, active, usage windows with pace, per-model limits, login expiry and when it was measured. The result goes into the picture each Mac already swaps with the other, so either Mac shows both. The app gets a sidebar **Accounts** page with a count of accounts that need action now. A missing or failing tool shows as a quiet notice and never crashes anything.
- Safety: no token, email address or organisation id is kept. A personal organisation named after its email shows as "Personal". Any email in a label is masked as `•••`, including in a picture received from the peer. The tools' stderr is never read or logged. Only the two listing commands are run, never switch, auto, add, remove or `--token-status`.
- Parsing is pure and tested with made-up fixtures in `src/accounts.ts` and `src/app/accounts.ts`. Running the tools is kept at the edge in `src/account-tools.ts`. The view API (`docs/api/view-v1.md` and its example), the app design note, README and AGENTS.md now describe it.
- Checks: `bun run self:check` passes with only the 11 warnings that were already there. `bun run test` passes: 40 files, 396 tests.

## In Progress

- Nothing running. I haven't seen the page with real data: I ran neither tool myself, because that would have reached the usage API and printed account details, and I didn't open the app window. On the first review after a relaunch, check that both tools answer when started from the Portal. codex-multi-auth runs through its mise shim, and the Portal starts with a bare PATH.
- Possible roadmap items, not created: a Portal tray line saying which account each Mac is on; showing cswap's pay-as-you-go spend, if you want it.

## Queries

None. Choices I made: the page refreshes on the normal review, every 5 minutes by default, and never faster than once a minute. A Mac with no codex-multi-auth simply has no Codex section. The Codex reading uses its cache, so it is only as fresh as codex-multi-auth's own last check.

🧵 ki.prj.agora
