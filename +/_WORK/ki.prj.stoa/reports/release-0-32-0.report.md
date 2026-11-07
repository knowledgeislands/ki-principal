# [Foundations](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Stoa](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/stoa.md) › release-0-32-0

**🤖 → 👤 Handoff to supervisor · Run report at 02:50 GMT · blocked · last mark 02:46 GMT**

---

## Done

- `packages-stoa` `main` was clean and level with `origin`, at `e37e43c`; the fast-forward pull brought nothing new.
- Checks on `e37e43c`: tests pass (253 pass with 1 skipped in Stoa, 3 pass in the workbench), typecheck is clean and lint is clean.
- Workbench, viewed in the installed Chrome running headless: the four-square trigger opens the Command Bar. With an empty query it lists Home, Lab and Harbour Survey under Sites, leaving out Docs, the current site. Typing "Harbour" finds Harbour Survey at <https://harbour.example.org/>. All 44 new icon names render, giving 137 names in total. The server is stopped.
- Stopped at acceptance: [STOA-CMD-001](/Users/krisbrown/kis/knowledge-islands/packages-stoa/docs/roadmap/STOA-CMD-001-command-k-palette.md) was not accepted, and 0.32.0 was not released, tagged or pushed. The `ki-accept` skill first needs the repository to name its work-record setup (the "adapter"), and it allows no fallback. `packages-stoa` has no `.ki.toml` and never has had one, so that setup is undeclared and the skill refuses before touching the record. As the brief directs, I released nothing and made no commits. The checkout is still clean at `e37e43c`.
- Apart from that, the record would pass: it is `awaiting-review`, every Step is ticked, its six-part review packet is in order, and both checks named in its Verify section hold today.

## In Progress

Nothing. The run is held on the query below.

## Queries

### STOA-ADAPTER - Declare packages-stoa's roadmap so STOA-CMD-001 can be accepted

**Context**

Kris's STOA-RELEASE approval of 7 November 2026, 02:44 GMT, covers accepting STOA-CMD-001 and cutting 0.32.0. `ki-accept` will close a record only when the repository's `.ki.toml` declares how its work records are kept. `packages-stoa` keeps them in `docs/roadmap/`, and its `ROADMAP.md` says so in prose, but it has no `.ki.toml`. The `ki` tool also refuses the repository for the same reason. Everything else needed for the release is ready.

**Query**

How should the missing declaration be handled before the release runs again?

**Options**

a) (recommended, confidence high - this fixes the cause with the least scope and keeps the acceptance rule intact) Have a short authorised run add a `.ki.toml` to `packages-stoa` that declares the local `roadmap` adapter (for example with `ki repo init`), check that the roadmap audit passes, and commit it. Then rerun this release brief unchanged.

b) Kris waives the declaration check for this one closure, so STOA-CMD-001 can be closed by hand against its `docs/roadmap/` record before the release. The skill says there is no fallback, so the waiver would need his explicit words.

c) Release 0.32.0 now, leave STOA-CMD-001 `awaiting-review` until the declaration exists, and accept it afterwards. This splits what STOA-RELEASE approved as a single step, so it needs a fresh go.

A side note for whoever reruns the release: the STOA-RELEASE entry says to "date the CHANGELOG", but earlier release headings carry the bare version, such as `## 0.31.0`, and the brief asks for `## 0.32.0`. I would keep the bare heading unless Kris wants a date.

Candidate record: adding the `.ki.toml` declaration to `packages-stoa`, if option a) is done as tracked work rather than a direct fix.

### 🤖 → 👤 Handoff to supervisor · blocked · at 02:50 GMT

👤 1 with you · ⛔ 1 blocked

- [blocked] Stoa 0.32.0 release and STOA-CMD-001 acceptance · release-0-32-0 · 02:50 GMT

🧵 ki.prj.stoa
