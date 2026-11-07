# [Foundations](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Stoa](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/stoa.md) › licence-mit

**🤖 → 👤 Handoff to supervisor · Run report at 04:56 GMT · last mark 04:56 GMT**

---

## Done

Stoa is now licensed under MIT, copyright Kris Brown, as decided in STOA-LICENCE on 7 November 2026 ([decisions log](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.stoa/decisions.md)). Commit `a50b307`, `chore(repo): license Stoa under MIT`, adds `LICENSE` (the same text as `tools-mgit`) and declares `license = "MIT"` in `.ki.toml` and `"license": "MIT"` in the root `package.json`.

Repository audit: the missing-file finding and the `package.json` finding are cleared, and nothing new fails. One licence finding remains: GitHub's own licence field still reads "none". GitHub fills it in by reading the pushed `LICENSE` file, so it should clear on the next audit.

Tests, type-check and lint: all pass. The checkout is clean.

The audit did not ask for a licence declaration in `packages/stoa/`, so the vendored tree and its version are unchanged.

## In Progress

Nothing.

## Queries

None. No candidate roadmap record came out of this run. The audit's other existing failures, such as the GitHub description and merge settings, were outside this brief and were left alone.
