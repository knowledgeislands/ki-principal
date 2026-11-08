# [KI > Techne](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/techne.md) › [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/agora.md) › wake-map

**🤖 → 👤 Handoff to supervisor · Run report at 03:40 GMT · last mark 00:04 GMT**

---

## Done

- **The wake map is written:** [docs/design/wake-map.md](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/design/wake-map.md) in apps-agora.local, commit `b15e917`. It covers Orca chat and Orca terminal (each with Claude Code and with Codex), Claude Desktop and Claude Design. For each it gives what reaches it today, what can and cannot wake it, what is proved and what is untested, and the target route through Agora's call. It has a Mermaid diagram and nine gaps, each with an owner. It builds on personal.reg.inbox-sol's wake research and does not repeat it.
- **Proved on sol, with no setting, configuration or other session touched:**
  - A file wait wakes a Claude Code session. This run waited in the background on a test call file, and writing the file woke it within a second.
  - `orca terminal send` reaches a terminal. I created a throwaway Orca terminal for the test, sent a command into it, saw the command run, then closed the terminal.
  - Agora's own Orca look, run read-only, sees six live agents on sol. All six are Claude **chats**, so Agora's built terminal wake has nothing it can wake on sol today.
  - Orca 1.4.248 has no `chat` command yet.
  - `fswatch` is not installed, so the call wait falls back to a two-second poll.
- **Checks:** `bun run self:check` passed and `bun run test` passed (220 tests). Both ran on a clean copy of the committed code with the new note added, because the shared checkout holds another session's unfinished code changes that fail the type check (next section).
- **Choices I made:**
  - I wrote the call's path as `doorbell/<work-id>`, with the rename to `call/` noted as coming, because the rename has not landed.
  - I did not send `SendMessage` or any other message to another session. I did not start an agent in a terminal. So agent submission receipts, `codex queue` and Orca orchestration mail from outside a Run are marked untested, not proved.
  - Legal's listening round-trip report was not present at the path given, so Legal's own message is the evidence for its case.
  - I created no roadmap record.

## In Progress

- **Shared checkout, not mine.** apps-agora.local has uncommitted changes from another session in `src/agora.ts`, `agora.test.ts`, `config.ts`, `config.test.ts`, `files.ts`, `files.test.ts`, `ki.ts`, `ki.test.ts`, `review.ts`, `state.ts`, `sync.ts` and `view.test.ts`. They look like the call rename in progress, and they fail `tsc` for now. I left them untouched.
- **Roadmap candidates** for the coordinator to capture. Each is a gap in the note:
  - G5: Agora rings the owning package's call when a `ki agent` run finishes, fails or blocks.
  - G7: Agora notifies Kris about packages whose thread cannot be woken.
  - G2: pilot the `asyncRewake` hook on Agora's call. This was already agreed as Q16 in inbox-sol's spec.
  - G3: pilot `codex queue` against a test Orca Codex chat.
  - G4: Orca orchestration as the route for run results. This could sit under `KI-AGORA-WRK-001`.
- **Two packages may both answer Legal (C15 in the alignment).** OVERNIGHT-PLAN puts the answer to Legal with this Project, so the reply below names ki.prj.agora as owner. personal.reg.inbox-sol's spec still lists the same answer as its own, so it should be told to drop that line.
- **Reply to Legal, for the coordinator to send** to lgl.sop.main's `messages.md`:

  > LEGAL-AUTOMATION-AGORA-20261104 · receipt from 🧵 KI > Techne > Agora (ki.prj.agora), the accountable owner for waking threads and the wake map; Orca chat send itself is Orca's upstream (stablyai/orca#33115). Verified on sol, 6 November 2026, with Orca 1.4.248 and Codex 0.166.0, nothing configured or sent to your thread. (1) Unsolicited message wake of a structured Orca Codex chat: not possible today. Orca has no command to send into a chat (`orca chat` is unknown in this release), Codex has no self-watch, and Agora can see your chat but holds its wake. A message is read only in a turn Kris or the thread starts. (2) Agent-result wake: not possible today for a `ki agent` run. A worker started as an Orca orchestration worker is documented to wake its coordinating chat on `worker_done`, but this is untested. (3) Unattended supervision: not possible in a Codex chat. It works today only for a Codex thread in an Orca terminal that its package names in Agora's watch list: Agora types one fixed wake line there when the thread is between turns (built; terminal delivery proved). Map: apps-agora.local `docs/design/wake-map.md` (`b15e917`). Next: Agora adopts `orca chat send` when it ships, and pilots `codex queue` and orchestration results. Until then, an unattended Codex window that must hear results should run in an Orca terminal (asked of Kris).

## Queries

### WAKE-CODEX-TERMINAL - Where should unattended Codex work run?

**Context:** Nothing can wake a Codex thread in an Orca chat until Orca ships chat send. That is why Legal's overnight work finished unheard. Agora can already wake a thread in an Orca terminal, but nothing on sol runs in one, and no watched package names one.

**Query:** For a window you leave unattended, should a Codex thread that must hear messages and results run in an Orca terminal, with its package naming that terminal in Agora's watch list?

**Options:**

a) (recommended, confidence medium - it is the only route that works today without waiting on Orca, and it uses a wake Agora already has, though agent submission is not yet proved here) Yes: for unattended windows, start such Codex threads with `orca agent launch --surface terminal`, and have the household name them in Agora's watch list. Chats stay for attended work.

b) Keep Codex in chats, and accept that it hears only when you give it a turn until Orca ships chat send.

c) First pilot `codex queue` and Orca orchestration results on a test Codex chat you open, then decide.

## New and noteworthy

- One page, `docs/design/wake-map.md` in apps-agora.local, now shows for each place you work (Orca chat or terminal, Claude Code or Codex, Claude Desktop, Claude Design) whether it can hear a message or a finished run on its own, and how.
- It is now proved on sol that a Claude Code thread waiting on Agora's call wakes as soon as the call rings. It is also proved that Orca can type into a terminal on Agora's behalf, so a thread run in an Orca terminal can be woken without you.

🧵 ki.prj.agora
