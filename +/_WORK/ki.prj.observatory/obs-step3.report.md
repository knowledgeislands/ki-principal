# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-step3

**🤖 → 👤 Handoff to supervisor · Run report at 12:25 BST · last mark 08:47 BST**

---

## Done

- CAPITAL-GLYPH a) and HEXMAP a): [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) now uses ki-design's published `capital` glyph and vendors the hex renderer and terrain tokens by script, at a pinned ki-design commit, with a digest drift check. The renderer question is closed, and the record is ready to promote to Next. The design handoff's ask 3 is removed and marked as met (`-/design-handoff/INSTRUCTION.md`). Commit `e3b47b2`.
- CONDITION: Kris's model is recorded in [KI-OBSERVA-BCN-008](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BCN-008-beacon-signal-anatomy.md) and KI-OBSERVA-VIS-030 as a verbatim quote from STEP3-ANSWERS: each island declares its maturity, and decline or ruin is a separate quality scale. Neither is read from commit age, and until a home is chosen the chart draws condition as unknown. The quotes were tidied to verbatim in `80c1a1b`. Nothing is decided; the home is the query below.
- STEP3-ACT a): [KI-OBSERVA-BRG-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-003-governed-act-presentation.md) was planned to Now and Ready (`80c1a1b`), then built and moved to Awaiting review with its review packet (`9e4094b`):
  - Rig's and Repositories' operations sit in a region edged in the boundary colour, with a heavier top rule and a `governed` tag.
  - A plan now reads as a declaration: operation, tier, confirmation, command, limit, effect, and issued and expiry times.
  - One confirm button names the action.
  - Rig's receipts show outcome, requested, took, exit code, command and detail, newest first.
  - No operation, tier, confirmation, route or receipt changed.
  - The Feedback panel uses the same shared fragment, so its send plan takes the same layout.
- Parts of the board with no field in the plan or receipt contract are left out and listed in the record: the scope row, withheld inputs, the button's count, the receipt's counts and its way in.
- Checks:
  - `bun run test`, typecheck, build, knip and rumdl pass.
  - biome is clean on the touched files.
  - `ki repo audit` has no failures; the warnings were there before.
  - The browser smoke check was skipped because Playwright's Chromium is not installed.
- Pushed `e3b47b2`, `80c1a1b` and `9e4094b` fast-forward to `origin/main` after a fetch. No other commit was stacked.
- A restart of the Observatory service is due: `main` now carries the governed-act layout, and this run did not restart it.
- `ki agent note` does not exist in this `ki`, so progress went to the status file only.
- `ki repo roadmap promote` refused because of an unrelated `size` field in KI-OBSERVA-APP-045, so the horizon was set by hand.

## In Progress

Nothing. KI-OBSERVA-BRG-003 is waiting for your review and acceptance.

## Queries

**CONDITION-HOME**

**Context:** You set the condition model on 19 October: each island declares its maturity, and decline or ruin is a separate quality scale. These are the places it could live:

- The island's `.ki.toml`, which every repository already has and which the Observatory already reads through `ki`.
- The Capital's Known Lands inventory in ki-principal.
- A KI specification in ki-specifications that defines the two scales.
- `ki repo audit` health, which already scores each repository mechanically.

Every option needs a change in another repository, because the Observatory must read the value through a stable `ki` contract rather than invent one. That means the ki-repo standard in ki-agentic-harness and the `ki` contract in tools-ki, and ki-specifications or ki-principal for some options. Nothing was written there.

**Query:** Where should an island declare its maturity, and where should decline or ruin come from?

**Options:** a) (recommended, confidence medium - the island owns its maturity, as you said, and decline is a quality measure that audit already produces mechanically) Maturity is a field the island declares in `.ki.toml` under `[skills.ki-repo]`, from a fixed scale defined by the ki-repo standard. Decline or ruin is derived from `ki repo audit` health, and `ki` exposes both in a machine contract the Observatory reads. b) Both are declared in `.ki.toml`: maturity, plus a declared decline or ruin state the owner sets by hand. c) Both are held in the Capital's Known Lands inventory: one place to edit, but the Capital speaks for each island rather than the island speaking for itself. d) A KI specification in ki-specifications defines both scales and their meaning, with the values stored as in a). This adds a formal definition first and takes longer.
