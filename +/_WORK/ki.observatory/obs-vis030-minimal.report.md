# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-vis030-minimal

**🤖 → 👤 Handoff to supervisor · Run report at 21:39 BST · blocked**

---

## Done

- I committed the chart's backend locally on `main` as `21be3a6` (`feat(known-lands)`). It is not pushed.
  - The territory parser now keeps each territory's declared Capital.
  - `GET /api/known-lands` answers a new contract, `observatory/known-lands/v1`. It gives one archipelago per territory and matches the declared Capital to a repository on the backend. A territory that cannot be read gives its reason. The repositories in no territory form one more group, with no Capital.
  - `GET /api/known-lands/svg` draws the chart as a read-only image under the existing SVG policy. It uses the vendored renderer's fixed layout: no saved positions, no write route and no boundary spec change. The page's nonce policy is unchanged.
- [KI-OBSERVA-VIS-030 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/0966ac3e/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) is updated and stays in progress. It records the backend as in place and the tab as blocked on the query below. It says that positions (VIS-030-POSITIONS), the fuller interaction and the look await Kris's designs. The CHANGELOG has an entry too.
- Checks: the full gate passed (`bun run test`, `self:typecheck`, `build`, `knip`, `rumdl`), and the commit hooks passed. `ki repo audit` passed with no failures; VIS-030's only warning is the size field, which the audit asks for on many records.
- Service: I restarted it and it answers at <http://127.0.0.1:1675/>. All 15 existing tabs load. On the real estate the chart draws 9 archipelagos and 51 repositories, every Capital is in place, and no local path appears in the image or the data. Techmedix shows as unread because one of its members is not registered (that registration problem was already known). The chart can be opened directly at <http://127.0.0.1:1675/api/known-lands/svg>.

## In Progress

- The `known-lands` tab is built and tested but not committed. It shows the chart image with a plain list of each territory's repositories underneath, each linking to its row in Repositories. It is saved, title `known lands`, at `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/observatory/obs-vis030-minimal/tab/` (`known-lands.ts` and `registration.patch`). The patch also changes the tab-bar stub in `shell.test.ts` from 1000 to 1200 px. Still to do: add the tab to `degraded.test.ts`, then update the README and operator guide.

## Queries

**Context:** The record adds Known Lands as a sixteenth tab and requires the width tests to pass unchanged. `layout.test.ts` requires every tab to fit the bar without scrolling at the 1,440 px window. Fifteen tabs take 1,341 of the 1,392 px available. Any sixteenth tab overflows, even one titled `map` (1,398 px). The 760 px rule is not affected.

**Query:** How should the bar make room for the Known Lands tab?

**Options:**

a) (recommended, confidence medium - this keeps the tab, the width test and the narrow rule unchanged, and renames no capability) Shorten one existing tab's title, for example `review queue` to `review`. That saves about 42 px, and all sixteen tabs fit (about 1,356 px).

b) Add the tab and let the bar scroll at 1,440 px with its existing fade. This changes the wide-window part of the width test.

c) Don't add a tab yet. Show the minimal chart at the top of an existing view, such as Trade routes, until the designs place it.

d) Tighten the spacing between tabs in the stylesheet. This changes the look ahead of the designs.
