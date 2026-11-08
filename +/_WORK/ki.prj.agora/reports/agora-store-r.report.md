# KI > Techne > Agora › agora-store

**🤖 → 👤 Handoff to supervisor · Run report at 03:58 GMT · last mark 00:04 GMT**

---

## New and noteworthy

Version 1 implements Kris’s individual Markdown file layout. The previous attempt’s log records only the session limit: it left no earlier report, implementation or commits to resume. The first commit hook exposed inherited Git index settings reaching fixture repositories; the runner now removes repository overrides, with a regression test. No hook was bypassed.

Differences from the read-only [interim MCP draft](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora-mcp.md), read during this run while another run may edit it:

- Kris’s `messages/<territory>/<recipient>/<timestamp>-<uuid>.md` replaces `store/v1/<territory>/messages/<yyyy-mm>/<id>.json`. Full UTC millisecond filenames, then alphabetic UUID order, govern processing. UUIDv7 is generated.
- `sent`, a Markdown body, `from.work_id` and `from.rig` replace draft `at`, JSON `text`, `from.workId` and `from.mac`. One concrete work ID is the recipient. The six requested kinds replace the draft’s additional owner broadcast kind.
- `roster/<territory>/<work-id>.md` replaces the draft’s per-seat `<mac>.<work-id>.json` under `store/v1`. Presence is package-owned, not one file per rig seat. The entry carries rig, role, focus, listening and last seen; simultaneous seats must coordinate its single writer.
- No receipt files or mutable sent messages: v1 unread means not acknowledged or answered. Inbox reads do not mutate state. Audit has the requested three statuses; an ack is terminal for harvest even when the original requested a reply, unlike the draft’s separate receipt and answer obligations.
- Harvest deletes eligible complete threads in one commit and leaves Git history as the archive. There is no `archive/` move or monthly archive threshold. Only Kris can truncate history externally.
- A checkpoint is an ancestor Git commit hash. `since` returns file changes including harvested additions and deletions, rather than the draft’s composite `git:…;live:…` checkpoint and message/time fallbacks.
- Local writes commit and push immediately. Only the current operation’s own unpublished commit can be replayed after a push race; dirty stores, unknown unpublished commits, divergence and conflicts stop safely. No write is silently left for a later batching round.
- Version 1 serves the eight requested tools plus `harvest` and `presence`. Mutations preview by default and pass an annotation-based access gate. Full UUIDs are accepted; short IDs, focus/everyone addressing, broadcasts, live TTLs, client retry IDs, rich roll-call counts, owner-only marks and live/cloud adapters remain outside this build. It is a trusted personal store, not the draft’s multi-tenant trust service.
- `wait` is cancellable bounded polling, up to once per second, rather than the draft’s live signal/filesystem watch. Local waits observe committed state already in the clone and do not fetch. Beacon refresh and wake integration remain the next run.
- Remote message and roster writes use Contents API. Atomic multi-file harvest uses GitHub’s Git data API with a non-forced reference update because Contents API cannot delete an entire thread in one commit. This distinction is documented in both repositories.

## Done

- `mcp-agora` commit `a94100f`: implemented the store library, local/remote writers, stdio tools, CLI, private Bun scaffold, Node build, CI definition and repository guidance.
- `ki-agora-beacon` commit `f366c88`: defined the store contract, updated navigation and added the two empty directory markers; its Markdown and commit-message hooks passed.
- `bun run check`: passed, including Biome, TypeScript, 20 tests across four suites and the Node build; the full check also passed inside the successful commit hook.
- Isolated tests passed for UUID ordering, YAML validation, exact bodies, ownership, durable roster, unread/response state, archived audit, whole-thread harvest, single and repeated push races, dirty-store refusal, symlinks, cancellation, remote API retry/harvest/history, stdio access gates and inherited-index isolation.
- Compiled Node stdio protocol check: passed. Markdown checks and whitespace checks: passed. Post-hook commit contents contain only intended paths.
- Both primary checkouts are clean on `main`. CI was defined but its remote execution was not inspected; no live GitHub API request was made.

- [mcp-agora README](/Users/krisbrown/kis/knowledge-islands/mcp-agora/README.md): setup, configuration, Claude Code and Codex mount examples, tool arguments, local and remote behaviour, CLI and limits.
- [Store library](/Users/krisbrown/kis/knowledge-islands/mcp-agora/src/main/store/index.ts): layout, UUIDv7, YAML front matter, exact bodies, ordering, roster ownership, status, harvest and history audit.
- [Local writer](/Users/krisbrown/kis/knowledge-islands/mcp-agora/src/main/store/local.ts): clone lock, clean published baseline, immediate explicit-path commit and push, bounded race retries and symlink containment.
- [Remote writer](/Users/krisbrown/kis/knowledge-islands/mcp-agora/src/main/store/remote.ts): injected GitHub transport, just-in-time `gh auth token` implementation, Contents writes and atomic harvest. Tested without invoking `gh` or contacting GitHub; live credential permissions and API operation remain unverified.
- [Store contract](/Users/krisbrown/kis/personal/ki-agora-beacon/STORE.md), [store README](/Users/krisbrown/kis/personal/ki-agora-beacon/README.md), and empty `messages/.gitkeep` and `roster/.gitkeep`. No real messages or presence records written.
- Private repository unchanged in visibility; no registry publication, agent mount, global install, credential change, roadmap record or delegated agent. Dependencies were installed from the existing local cache with network access disabled.

## In Progress

Nothing is running once this handoff is delivered. Outstanding — no action requested now: binding Beacon to the store is the next implementation run; no `apps-agora.local` file was changed here.

Recommended next run (confidence high — these are the existing configuration, lifecycle, roster and wake seams):

1. In [apps-agora.local/AGENTS.md](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/AGENTS.md), narrowly permit commit/push for the configured Agora store adapter. Its present blanket ban on Agora commits and pushes otherwise conflicts with the required store writer; keep ordinary checkout syncing governed by its existing restrictions.
2. Add one optional **`[store]`** configuration table in [src/config.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/config.ts): `mode = "local" | "remote"`, `path` (absolute registered clone root, local), `repository` (owner/repo, remote), `branch = "main"`, and bounded `retries = 3`. Absence keeps today’s behaviour. Each rig has exactly one binding. Its local path maps to the MCP’s **`MCP_AGORA_STORE`**; remote repository maps to **`MCP_AGORA_REPOSITORY`**. The household owns rendering the rig’s configuration; this run changed none of it.
3. Add **`src/store.ts`** as an Electron-free adapter over `@knowledgeislands/mcp-agora/store`; add its source dependency and lock entry in `package.json`/`bun.lock`, without a package registry. Use the sibling source during development and a pinned Git reference for distribution. Open the configured backend once, serialise its writes and expose refresh, inbox/change reads, presence and send/ack/reply. Retain the library’s clean-checkout and non-forced push safeguards.
4. Wire that adapter through **`AgoraDeps` and `Agora.start()/stop()` in [src/agora.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.ts)**. Start with a refresh, retain its Git checkpoint, run refresh on the existing fallback/review cadence, consume `since(ref)`, and stop timers on shutdown. Keep the store writer separate from generic [src/git.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/git.ts), [src/sync.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/sync.ts) and [src/review.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/review.ts); those must not acquire general commit/push authority.
5. Use **[src/packages.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/packages.ts)** `readRoster` and **[src/roster.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/roster.ts)** mappings to publish only each local watched package’s own record under that package’s identity. Map package ID, territory, rig, role, focus text, listening state and read time to the durable fields. Never publish peer copies over another package’s entry. Merge durable rows into `Agora.rosterRows()` with provenance and staleness; keep richer local package details for existing views.
6. Route newly received store messages through **[src/calls.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/calls.ts)** and **[src/waker.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/waker.ts)** using their existing call/debounce policy. Add a store change source alongside **[src/watch.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/watch.ts)**, retaining legacy package-file watching during the pilot. Derive message passes and acknowledgements from immutable IDs/`re` in **[src/talk.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/talk.ts)**; do not mirror messages into mutable shared lists or acknowledge merely because a viewer fetched them.
7. Feed the resulting roster/message state through **[src/state.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/state.ts)** and existing `Agora` snapshots to **[src/local.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/local.ts)** and **[src/phone.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/phone.ts)**. Keep read endpoints read-only. **[src/door.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/door.ts)** and **[src/broadcast.ts](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/broadcast.ts)** retain today’s owner broadcast behaviour until a separate broadcast contract exists; v1 does not invent a broadcast kind or owner grant.
8. Extend `config.test.ts`, add `store.test.ts`, and extend `agora.test.ts`, `roster.test.ts`, `calls.test.ts` and `talk.test.ts` with injected/temporary-store fixtures. Run Beacon’s `bun run self:check` and `bun run test`, then pilot two temporary clones for refresh, wake, ack/reply, offline failure, race retry, restart checkpoint and harvested audit before enabling real traffic. Harness mounts remain a separate authorised action.

## Queries

No outstanding queries. Live GitHub verification and Beacon binding are receiver-owned follow-up work, not approval requests in this run.

### 🤖 → 👤 Handoff supervisor · at 03:58 GMT

👤 1 with you

- [with you] Agora store v1 and Beacon binding handoff · supervisor · since 03:58 GMT

🧵 ki.prj.agora
