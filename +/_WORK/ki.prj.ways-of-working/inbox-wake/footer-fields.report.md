# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › footer-fields

**🤖 → 👤 Handoff to supervisor · Run report at 12:54 GMT · last mark 01:41 GMT**

---

## Done

- The four thread capability fields (`listening_enabled`, `listening_status`, `syncing_enabled`, `syncing_status`) are now part of the `ki-work-package` state file, under Kris's FOOTER-CAPABILITY-STATUS-2. The rubric enforces the rule that a syncing thread must also be a listening thread, and that each status is present only while its capability is enabled. Committed and pushed as ki-agentic-harness `1f01cb7c`.
- The `ki-coordination` standard and the output style now show a capability's line only when that capability is enabled, and always with its status: `👂 listening` or `🔇 not listening`, and `🔄 syncing for <host>` or `🔄 not syncing for <host>`. The draining and hold examples now show `🔇 not listening`, and `banner.test.ts` covers the new pairs and the cross-field rule. This refines FOOTER-NOT-LISTENING. Same commit.
- Checks: `bun run test` passes (1521 tests), `bunx tsc --noEmit` is clean, the generated surfaces are regenerated and verified, and the focused `ki-coordination`, `ki-work-package` and `ki-skills` audits all pass. `ki-skills` shows 3 warnings that were already there before this change.
- Sent one IMPORTANT REFRESH line, pointing at `1f01cb7c`, to every live package except this one: 60 packages across chezmoi, er-principal, hnr-principal, ki-principal, legal-principal, assistant, personal-principal, si-principal, tmx-principal and va-principal. This is the same set the 31 October refresh reached, plus packages created since. Each package got its own commit, and each repository was pushed fast-forward only.
- Three packages (hnr.prj.5g-emerge-p2ms3, hnr.prj.m365-tenant and personal.prj.tower-public-site) had a stray `None` above their message lines, which made the Markdown check fail. I removed that placeholder when adding the line. personal.reg.household-terra was briefly being edited by another session; I waited and sent its line once the edit was committed. The acquire repository was renamed to `assistant` during the run, and its three packages got the line at the new path.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Kris also raised the auto-compact window in FOOTER-CAPABILITY-STATUS: Claude Code's `autoCompactWindow` can only be set per user or per repository, not per thread. This run did not address it. It belongs with the outside-watcher design under LISTEN-SYNC-OUTSIDE-THREADS.
- Messages that put the date first, as in `- 2026-10-31 · IMPORTANT · ...`, count as ordinary under the rubric, so the new REFRESH line sits above them. This follows the rubric as written.

## Queries

### SYNC-OFF-WORDING - How the footer says a sync thread is not syncing

**Context:** Kris's rule pairs `👂 listening` with `🔇 not listening`, and asks for a matching syncing pair, giving `🔄 syncing` and "a 'not syncing' form" as an example. The sync line already reads `🔄 syncing for <host>`, as in `🔄 syncing for sol`. I used `🔄 not syncing for <host>` for the off state. It keeps the same symbol, because there is no obvious "not syncing" symbol in the way 🔇 stands for not listening.

**Query:** Should the off state of the sync line read `🔄 not syncing for <host>`?

**Options:**

a) (recommended, confidence medium - it follows Kris's example wording, but Kris did not name a symbol) Keep `🔄 not syncing for <host>`.

b) Use a different symbol for the off state, for example `⏹️ not syncing for <host>`, so the two lines read differently at a glance, as the listening pair does.

### STOP-LISTENING-CAPABILITY - What "stop listening" does to the capability

**Context:** Each thread now has a capability flag and a status. I wrote that "stop the wake" or "stop listening" turns the status off and keeps the capability. So afterwards the thread shows `🔇 not listening` until Kris asks it to listen again. I also wrote that a Project closing at Finished clears both capabilities, so a finished thread shows no line. Kris's rule did not say which of these "stop listening" should do.

**Query:** Should "stop listening" leave the listening capability on, so the footer shows `🔇 not listening`?

**Options:**

a) (recommended, confidence medium - it fits "the line always shows when the thread has the capability", but it is my reading) Yes: "stop listening" turns the status off and keeps the capability, and only Kris withdrawing the capability removes the line.

b) No: "stop listening" also clears the capability, so the line disappears until Kris asks the thread to listen again.

### 🤖 → 👤 Handoff to supervisor · since 12:54 GMT

👤 2 with you

- [with you] SYNC-OFF-WORDING · owner · since 12:54
- [with you] STOP-LISTENING-CAPABILITY · owner · since 12:54

🧵 ki.prj.ways-of-working
