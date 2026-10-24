# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › comment-blind

**🤖 → 👤 Handoff to supervisor · Run report at 05:22 BST**

---

## Done

- **COMMENT-FIELD — Choose “Add a new optional `comment` field, allowed in the publishing spec so `rig export` carries it; retire `rationale`.” Confidence high:** this names the owner's intended concept explicitly and matches the site's existing optional-comment renderer without repurposing a reason field.
- **CORE-SET-COMMENTS — Choose “Leave them in the worksheet for the owner's review.” Confidence high:** earlier reasons for core membership do not establish that these are particular comments under the current direction, which excludes reasons for keeping an item.
- **Missing option, COMMENT-FIELD:** explicitly stage the transition: add optional `comment`, deprecate `rationale`, and retire the public field through a versioned contract change; publication version 1 forbids silently removing or repurposing it. Keep `requires` and `related` authoritative for dependency and pairing lines, and review existing distinct rationales individually rather than renaming all of them into comments.
- **Missing option, CORE-SET-COMMENTS:** exclude the core-selection reasons from comments entirely, preserving historical rationale in its existing record; propose only independently useful factual context, such as shared printer use, if the owner wants it.
- Pinned-declaration check passed at `d46a2ed`: parsed 191 tools and 55 settings; 177 tools repeat purpose in rationale, 14 differ; 35 settings repeat purpose and 20 retain provenance. All four core candidates repeat their purposes in declarations.
- Schema/export/site inspection passed: rationale is required; export already includes literal `rationale`, but supplies no optional-comment contract; the site renders optional `comment` separately from structured relationship lines. Evidence: [configuration validation](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/10-configuration.bash:1704), [export renderer](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/40-publication-lifecycle.bash:109), [publishing compatibility rule](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/publishing.md:79), and [site comment rendering](/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja/apps/site-rig/src/_includes/partials/rig-macros.njk:42).
- Evidence limitation: KB-DOTFILES-UE-079 is absent from the checkout, pinned tree and reachable roadmap history; its earlier decision was not independently verified. The four candidates are directly visible in the [worksheet](/Users/krisbrown/.local/share/chezmoi/-/rig-rationale-review.md:17), and [KB-DOTFILES-UE-027](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md) retains the owner-review hold.
- Checkout HEAD differs from the supplied revision; declarations were read directly from `d46a2ed` without switching branches or changing files.
- Commits: none; repository files unchanged by this review. No build, export, apply, install, push, network call or secret rendering performed; implementation gates were not run for this read-only review.
- Cleanup check passed: no root Git lock files in the three reviewed repositories; the designated temporary directory is empty. Prohibited work files and run reports were not read.

## In Progress

Nothing is running.

## Queries

No outstanding queries.
