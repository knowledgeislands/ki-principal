# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › footer-layout

**🤖 → 👤 Handoff to supervisor · Run report at 13:59 GMT · last mark 13:05 GMT**

---

## Done

- **Footer laid out top to bottom in `ki-coordination`** (harness `f04b0d61`): the banner heading now shows the state alone with no brackets, then the counts, then the items, then, each after a blank line, `↪️ draining → <target>` or `↪️ finishing → <target>` only while heading for a hold or a handoff, then one line per mode (`👂 listening`, `🔇 not listening` or `🔇 not listening while draining`, and `🔄 syncing for <host>` only on a host sync thread), then `🧵 <work-id>` last. The form line also lost its bracket. The bracketed heading and the old "· sync thread for" suffix are gone, and reports saved earlier stay readable.
- **Examples updated:** the With worker, handoff, hold and Finished banners use the new mode lines. A new example shows a banner draining towards a hold, and the output style now includes it too. The standard also shows how a host sync thread's footer ends.
- **Output style regenerated** from the standard. No other generated file changed.
- **Banner test rewritten** for the new layout. It now rejects bracketed headings and the old listening-line wording.
- **Work Process note** (Principal `c2b7fb41`): updated its Banner section to the same layout.
- **Checks:** banner test passed (24 tests). Full harness tests passed. Type check passed. The focused `ki-coordination` audit passed with its two usual binding warnings. The full harness audit, run in a separate test home, failed only on Biome's read-only check: the installed Biome (2.6.3) does not match the version the config expects (2.5.15), and the findings are in files this run didn't touch. That failure also happens on `main` without this change. Commit hooks passed in both repositories, and both commits are published.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Harness Biome version drift: the Biome installed in the primary checkout (2.6.3) is ahead of `biome.json`'s schema (2.5.15), so the full audit's Biome check fails on code this run didn't touch. A toolchain run could fix it with `biome migrate` and the lint fixes.
- The REFRESH rollout to every live coordinating thread is the separate `refresh-all` run under FOOTER-LAYOUT.

## Queries

### FOOTER-MODE-SPACING - A blank line between the two mode lines

**Context:** The brief asked for one line per mode after a blank line. When Markdown is rendered, as in Orca, two lines with no blank line between them run together into one line, which would put listening and syncing back on a single line. So the standard puts a blank line before each mode line, as it does before every other part of the footer. This only shows on a host sync thread, which has both a listening line and a syncing line.

**Query:** Should the listening and syncing lines keep a blank line between them?

**Options:**

a) (recommended, confidence high - rendered Markdown otherwise joins the two lines, which undoes the separate-line layout Kris asked for) Keep the blank line between mode lines, as delivered.

b) Put the mode lines directly one under the other with no blank line, accepting that some renderers will show them on one line.

### 🤖 → 👤 Handoff to supervisor · since 13:59 GMT

🏁 1 finished

- [finished] footer layout in ki-coordination, output style, banner test and Work Process note

🧵 ki.prj.ways-of-working
