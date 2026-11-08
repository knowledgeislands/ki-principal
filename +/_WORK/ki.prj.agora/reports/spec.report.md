# KI > Techne > [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/agora.md) › spec

**🤖 → 👤 Handoff to supervisor · Run report at 03:50 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- Agora now has a one-page specification, [docs/spec/agora.md](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agora.md): what it is and is not, the five goals with what "done" means for each, routing by focus, scope, boundaries and who owns what.
- Each of the 21 conflicts in the alignment check now has one line saying whether the spec settles it (15, three of them with a smaller part left open) or it is still Kris's to decide (6), so the open ones are easy to find.
- [How Agora works](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/how-agora-works.md) is now in Agora's own docs as a two-minute read, corrected so it no longer says Agora pushes and calls the signal Agora's call.

## Done

- Wrote `docs/spec/agora.md` from the agreed objectives, FOCUS-ROUTING and FOCUS-FIT a, with the closing conflict-by-conflict section (C1 to C21).
- Took household-terra's "How Agora works" (chezmoi `44b85f3`) into `docs/how-agora-works.md`, in the repository's voice. Corrections: Agora never pushes (the original said it pushes a clean checkout that is ahead); "doorbell" became Agora's call, with the old path noted until 20 November; sol's watch list follows Kris's 03:30 correction (four live, tower listed but not live); Ping is named as the way to see who is really listening.
- Linked both from `README.md` (one line) and the spec from `AGENTS.md` (one line, saying the spec governs where they differ).
- Corrected two `AGENTS.md` lines the objectives clearly settle: run-once jobs are now captured, not built, and out of scope for now; `ki agent` steers only runs Kris opened, and Agora starts no agent on its own (FOCUS-FIT a).
- Also corrected the README's "What it owns" sentence, which listed run-once jobs, floating doers and waking workers as owned; it now says running jobs and starting agents on their own are out of scope for now. This went beyond the one link line the brief asked for; I made it because otherwise the README would contradict the spec.
- Commit `3380b16` (docs(spec)), pushed to `origin/main`.
- Checks: `bun run self:check` and `bun run test` passed on a clean copy of `main` with only this change (230 tests). In the shared checkout `self:check` fails on a formatting issue in another session's unfinished `src/broadcast.ts`, which I did not touch.

## In Progress

- Another session has uncommitted changes under `src/` in the same checkout (it looks like the Mark all work). They are untouched; the pull before the push put them aside and restored them cleanly.
- Spec wording choices: it calls threads and sessions "agents" (Kris's word since KEEPALIVE) and calls rigs and hosts "Mac", until the naming pass (C13) settles the words.
- Left for the next docs slice, not changed here: `docs/design/identity.md` and two roadmap records still name `personal.reg.assistant-sol` (C14); the README's Forward work line ("signing the app and waking workers") is out of date; the README states broadcast reading and Away as settled while Q37 and Q38 are open (C17); the `AGENTS.md` "Floating doers" line (see the query below).
- For the coordinator: C21 says the package's `work.md` Scope and Focus should be rewritten against the five goals. No roadmap record is needed for this run's work.

## Queries

### SPEC-STATUS · Does the spec stay a draft until it is rewritten as a skill?

**Context:** The spec is plain English and marked `status: draft`. The overnight brief says it may be rewritten in RFC style (MUST, SHOULD, MUST NOT) inside a skill once that approach is agreed.

**Query:** Should `docs/spec/agora.md` stay a draft until that rewrite, or count as agreed now?

**Options:**

a) (recommended, confidence medium - the goals and boundaries are already ones you agreed, and agents need one place to check against tonight) Mark it agreed now as Agora's working spec; the RFC rewrite in a skill comes later and replaces it.

b) Keep it a draft until the RFC-style version in a skill is agreed.

### FLOATING-DOERS · Is the list of doers waiting for work still Agora's?

**Context:** `AGENTS.md` still says Agora will own "floating doers": a list of doers waiting for work on each Mac, with a cap on work in progress. The agreed objectives do not name it, and it sits close to starting agents, which is out of scope. I left the line as it is.

**Query:** Should floating doers stay in Agora's boundary as a later slice, or go out of scope for now?

**Options:**

a) (recommended, confidence medium - handing work to waiting doers drifts towards running work, which the spec says Agora does not do) Mark it out of scope for now, captured with KI-AGORA-WRK-001.

b) Keep it as a later slice in Agora's boundary.

🧵 ki.prj.agora
