# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › site-blind

**🤖 → 👤 Handoff to supervisor · Run report at 05:14 BST**

---

## Done

- **COMMENT-FIELD — Add an optional `comment` string to tool declarations in tools-rig and permit it in `rig export`. Confidence high — a particular tool remark belongs beside its catalogue description; substituting rationale would restore the reason the owner removed.**
- **KIND-SOURCE — Widen the publishing spec to export provider and install kind without locators, and declare tool `kind`. Confidence medium — this supplies both meanings from their authority in one structured export, removing repeated display-text parsing and unreliable application-bundle inference.**
- **RATIONALE-FILTER — Remove them now. Confidence high — public rationale-review counters contradict the requested description-only presentation, and none of the 184 checked public entries currently has a recognised placeholder rationale.**

COMMENT-FIELD needs no additional option: the existing `requires` and `related` relationships already supply “needs” and “pairs with” subtext; use `comment` only for an additional remark. The current export contains no comments, although the site conditionally renders them in all three views: [export renderer](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/40-publication-lifecycle.bash:109), [remark macro](/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja/apps/site-rig/src/_includes/partials/rig-macros.njk:43).

KIND-SOURCE has a missing option: a batch structured catalogue/show response containing explicit tool kind and coarse install routes, with the publication export unchanged. This is a credible alternative if keeping the current disclosure contract is an overriding requirement. Merely structuring the install field fixes wording fragility but leaves kind inference and repeated configuration loads unresolved: [show implementation](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/30-commands.bash:2392), [pull parsing](/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja/apps/site-rig/pipeline/pull.ts:101), [kind inference](/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja/apps/site-rig/src/_data/rig.ts:175).

The recommended export change requires an explicit, narrow allow-list revision. Keep locators, artifact paths and machine state excluded; distinguish tool kind from provider-native install kind. Preserve platform-specific routes rather than flattening the active machine's binding into a platform-independent export: [disclosure contract](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/publishing.md:17), [platform variants](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/catalogue.md:79). The precise kind vocabulary needs definition; the current inference even labels the public `readline` library a command-line tool.

RATIONALE-FILTER has a missing option: retain any unfinished rationale review in private work tracking while removing its public controls now. The checked declaration files also contain no recognised rationale placeholders; this does not establish that a separate review has been accepted or closed.

- Evidence check: reviewed site HEAD `4701e8f08b5a7c04abadbbe071ddb2ed8bf6b5c4`, its guidance, page, macros, data adapter, pull script and data; compared Rig's publishing and declaration contracts, show renderer and the application, command-line and Homebrew declarations.
- Boundary check: no prohibited files, secrets or run reports read; no network calls or prohibited commands run; no repository edits or commits made; site working tree clean and neither repository has a Git lock file.
- Runtime validation: not run, as required by the read-only brief; the stated pull duration was not independently measured.

## In Progress

Nothing is running.

## Queries

No outstanding queries.
