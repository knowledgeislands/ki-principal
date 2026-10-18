# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Knowledge acquisition](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/knowledge-acquisition.md) › ports-wording

**Run report at 01:40 BST · last mark not struck**

---

## Done

- Acquisition Process note now calls the capability "ports" (acquire is the port, one port of entry per source) and says "harbour" is its Arcadian register, linked to the [Arcadia](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Realisation/Arcadia/Arcadia.md) note.
- Dispatch step now reads: the port delivers whole packets into the receiving principal's `+/_ACQUIRED/` only, retires its copy once delivered and read back, and takes back returns marked by the island.
- Committed as cbf5de6 by explicit path; repository audit passed with no failures.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Not pushed. Two commits are stacked locally: my cbf5de6 and b726598 (log of the go-ahead on dispatch, returns, routing and ports), which is not mine. I did not push, as instructed.
- `git pull --rebase` refused because another session's `+/_THREADS/chezmoi/decisions.md` is dirty; I left it alone. Origin has no new commits (0 behind, 2 ahead).
- The note's Retirement step (6) and Source retirement section still say "once dispatched"; I changed only what you named.

## Queries

### PUSH-STACKED - push the two stacked commits

**Context:** cbf5de6 is mine. b726598 is another session's log commit on the same branch, so I did not push.

**Query:** Shall the two commits be pushed fast-forward only?

**Options:** a) (recommended, confidence high - origin is level and both are plain docs commits) Push both, fast-forward only. b) Leave both local.

```text
PUSH-STACKED

Push cbf5de6 and b726598 to origin fast-forward only, never forced.
```

╭─ run report · 2026-10-18T00:40:00Z ──────────────╮ │ │ │ █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀ · thread at rest │ │ █▀▀▄ █▀▀ ▀▀▀█ █    · nothing running │ │ █ █ █▄▄▄ ▄▄▄█ █    · nothing queued │ │ │ ╰──────────────────────────────────────────────────╯

- [at rest] nothing running or queued
- [waiting] PUSH-STACKED
- [unpushed] cbf5de6 and b726598 on main
