# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-smoke-baseline

**🤖 → 👤 Handoff to supervisor · Run report at 01:20 BST**

---

## Done

None of the browser smoke failures come from [KI-OBSERVA-VIS-041](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md>). They are already there at baseline 04a2ebb. They also happen with the full Chromium build, so the headless shell does not cause them either.

- Full Chromium build installed for Playwright 1.64.1 (chromium-1248) with `bunx playwright install chromium`. No tracked file or package.json changed.
- Baseline 04a2ebb, in a temporary detached worktree with dependencies installed frozen: `bun run self:test:browser` fails.
- Primary checkout at main 4d967aa (includes d27363a): `bun run self:test:browser` fails.
- Flow by flow, the two runs match line for line. There is one difference: main has an extra passing line, the Git viewer flow ("counted, narrowed, searched, sorted and diffed the repositories, and kept them on reload"). Both runs pass every view's open and refresh, diagrams, live artifacts, view switching, the sources store, the tab bar and the graph fitting. Both fail in the same two places:
  - Dimming: every view reports "once read" and "after refresh" as still dimmed, and the Beacon also does on opening and after the scope change. Four views (sessions, work, review, known-lands) also report "the smoke check names no read for this view".
  - Mermaid: there is a refused request to `/api/feedback/draft` and `/api/knowledge-bases/asset`, a console 403, and a content-policy refusal of an inline handler.
- No fix and no commit: nothing is new with VIS-041. The record's Review section is unchanged.
- The smoke check serves on an ephemeral loopback port, so the live service was never touched. It still answers 200 at 127.0.0.1:1675.
- The temporary worktree was removed with `git worktree remove`. The primary checkout is clean, and the smoke check's report folder is ignored by Git.

## In Progress

Nothing.

## Queries

**Context** The dimming and Mermaid failures in the smoke check were already there before VIS-041 and still happen with the full Chromium build. So the check has been red for something else, and it fails on main whichever browser runs it. VIS-041's Verify asks for "the browser smoke check passes", and that cannot be met until this is fixed.
**Query** How should the existing smoke failures be dealt with?
**Options** a) (recommended, confidence high - the failures predate the record and are outside its files) accept VIS-041 against its own Git viewer flow, which passes, and capture the dimming and Mermaid failures as a separate triage record to find and fix their cause; b) hold VIS-041's acceptance until a separate run makes the whole smoke check pass; c) look for when they started (for example with `git bisect` over the smoke check) before deciding.
