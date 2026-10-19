# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-step2

**🤖 → 👤 Handoff to supervisor · Run report at 09:05 BST**

---

## Done

[KI-OBSERVA-APP-043](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-043-shell-polish-without-regrouping.md) is built and awaiting your review. Its review packet is in the record. The Observatory header now shows the domed mark beside its name. It also has an optional job lens that shows only the tabs for Observe, Attend, Act or Extend, never hides the open tab, and is remembered by the browser. Beside the lens is a workers chip that counts running agent runs (DESIGN-WORKERS-CHIP a) and opens Sessions. Every pane now names its state as observed, observing, empty, partial, not observed or stale. Stale comes after 30 minutes by default, 10 for Sessions and 60 for Activity (DESIGN-STALE a). A repository filter now follows you between the views that filter by repository, with one clear. The status line ends with the address you came in by. No tab, route, `?view=` address or capability changed, and the header keeps its height. The decisions are recorded in [PDR-KI-OBSERVA-009](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-009-the-shell-names-each-pane-state-and-the-job-lens-filters-the-tabs.md).

Commits `393d093` (record Ready, citing your "All as recommended" of 19 October 2026, STEP-2 a), `90b8b4f` (the shell, tests, PDR, guide, CHANGELOG) and `69be84f` (Awaiting review with packet), pushed fast-forward to `origin/main`.

Tests: pass, with the layout and degraded tests unchanged. Typecheck: pass. Build: pass. Lint: biome reports only the 13 warnings and infos that were there before; knip and rumdl pass. Roadmap audit: `ki repo audit` shows no failures and only warnings that were there before. Browser smoke check: skipped, because Chromium is not installed for Playwright on this host.

## In Progress

The Observatory service needs a restart to serve this delivery. A detached run may not restart it, so the next interactive session should run it.

## Queries

**Context:** The record first placed the workers chip out of scope, waiting on KI-OBSERVA-VIS-031. Your DESIGN-WORKERS-CHIP answer placed it in this step, so I built it here and noted the change in the record and the PDR. **Query:** Should the workers chip stay in KI-OBSERVA-APP-043? **Options:** a) (recommended, confidence high - your answer put it in step 2, and it reads only the existing Sessions answer) Keep it in KI-OBSERVA-APP-043 as delivered. b) Take it out and leave the chip to KI-OBSERVA-VIS-031.
