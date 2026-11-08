# KI > Techne > Agora › stale-agent

**🤖 → 👤 Handoff to supervisor · Run report at 06:43 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- `bun run self:install` now finds the old launch agent `info.knowledgeislands.agora` that still starts `Agora.app/Contents/MacOS/Agora` and exits 78 at every login. It unloads that agent, removes any plist it left, and says so in one line. When the agent is absent it does nothing.
- The old agent was never a file in `~/Library/LaunchAgents`. macOS's background-items service registered it from inside the old Portal bundle, and it has the same label the Portal uses today. So the check looks at which program the registered job runs, not just whether the label exists, and the Portal's own agent is left alone.
- terra and sol clear it the next time their households run `self:install`.

## Done

- Retiring the old launch agent: a new pure decision in `src/install.ts` (`staleAgent`, `agentProgram`) reads the job's program from `launchctl print`, and from any plist for the label in `~/Library/LaunchAgents`. It retires the job only when that program is the old Portal's `Contents/MacOS/Agora`. The installer carries the decision out (`launchctl bootout`, removes the plist, prints the line) before it starts the new Portal. If the unload fails, it prints the command to run by hand. Commit fa71734, pushed.
- Tests: five new cases (reading the program, unloading, removing a plist, and leaving an absent agent or the Portal's own alone).
- README: the install section gains one sentence, and the test table mentions the new check.
- Checks: `bun run self:check` passed (11 lint warnings, none in the files this run changed). `bun run test` passed, 377 tests.
- Choices made: I matched on the program rather than the label, because both apps' agents share the label. I check only `~/Library/LaunchAgents` for a plist, because the old installer never wrote one there (Git history confirms it). The old in-bundle plist goes when the installer replaces `Agora.app` with the Agora app, as it already did. Following the brief, I installed nothing and did not touch this Mac's agent. I only read it with `launchctl print` to see how it is registered.

## In Progress

- Not verified on a real Mac: after the unload, the new Portal registers its own agent when it starts. That assumes the background-items service does not reload the stale registration at the next login. The households should check `launchctl print gui/$(id -u)/info.knowledgeislands.agora` after the next login on terra and sol. If it still names `Contents/MacOS/Agora`, a candidate follow-up record is to clear it through `sfltool` or a Portal-side unregister and re-register (not created).

## Queries

None.

🧵 ki.prj.agora
