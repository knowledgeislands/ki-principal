# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-obs-review-design

**🤖 → 👤 Handoff to supervisor · Run report at 22:46 GMT · last mark 01:07 GMT**

---

## Done

- Wrote the one-page proposal [observatory-review.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/observatory-review.md): what the Observatory already has to reuse, the view, the answer path and its authority, privacy, what would change in the harness and tools-ki, the smallest first slice and the roadmap records it would become, named and not created. Committed as `1580dfcc` on `main`, that path alone, and pushed fast-forward to `origin`; rumdl clean, no non-ASCII dashes, the repository's commit-time audit passed.
- Finding worth knowing: the Observatory's Review queue already lists every open `queries.md` tag across the scope, and its feedback send already writes a `messages.md` line and commits it alone without pushing; sending is only switched off under KI-OBSERVA-BRG-004, whose hold condition the `ki-work-package` standard now appears to meet, since it lists the feedback package and names the owner through the Observatory as a sender. So the proposal is an extension of two existing paths, not a new instrument.
- Nothing changed in the Observatory, the harness, tools-ki or any other repository.

## In Progress

Nothing is running.

## Queries

### ANSWER-VECTOR - whether the first slice writes the answer line itself or waits for a `ki work answer` command

**Context:** The proposal's first slice has the Observatory compose the `messages.md` line and commit it through its own declared file effect, the path `feedback-send` already implements and tests, so the slice needs no tools-ki change. The Observatory's contract prefers consuming stable `ki` commands over duplicating work semantics, and a `ki work answer <id> <TAG> --option a --note "..."` command would make the line's shape one tool's and give the Observatory an argument vector instead. Waiting for it adds a tools-ki unit and a pin before anything can be answered in the Observatory; building the file effect first means a later swap to the command.

**Query:** Should the first slice write the line through the Observatory's own file effect, with the `ki work answer` command as a later record, rather than wait for the command?

**Options:**

a) (recommended, confidence medium - the file effect and its gate exist and are tested, and the swap later is one operation's vector, but the Observatory's own contract leans the other way) Build the first slice on the existing file effect; capture `ki work answer` and `ki work queries` for tools-ki as a later message and the Observatory's KI-OBSERVA-INT-005.
b) Wait for tools-ki to provide `ki work answer`, and have the Observatory's first slice declare it as its vector from the start.

### 🤖 → 👤 Handoff to supervisor · since 22:46 GMT

👤 1 with you

- [with you] ANSWER-VECTOR · owner · since 22:46
- [committed] design/observatory-review.md

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
