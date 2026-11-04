# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › self-focus

**🤖 → 👤 Handoff to supervisor · Run report at 05:07 GMT · last mark 01:41 GMT (1 November)**

---

## Done

- ki.prj.ways-of-working now uses the focus-folder layout: ki-principal `76d86a11`, `refactor(work): ki.prj.ways-of-working focus layout`, is published. It holds 116 tracked files.
- `queries.md` was renamed to `discussions.md` with `git mv`, and its content and headings are unchanged. `state.md`'s next step now names `discussions.md`.
- `work.md` has a `## Focus` section after Scope with 14 areas. Nine are the design topics from section 2 of the plan: `package-layout`, `discussions`, `host-sync`, `host-reconcile`, `inbox-wake`, `orca-subagents`, `capture-model`, `empty-board` and `window-31-oct`. The tenth is `aside`.
- I added four areas for groups of files that fit none of those topics: `landscape` (7 landscape notes), `work-model` (state machine, typed ids, model shape and tags), `rollout` (conform, burn-down and field-migration reports) and `personal-shape` (the Personal shape and handover runs). The plan listed 13 design topics, but only nine topic subfolders were tracked.
- Briefs are now `<area>/<run>.brief.md` and reports sit beside them. Each design topic subfolder was flattened into its focus folder.
- Links were repointed in 50 files: those in the package, ki.sop.main's decisions and design note, the messages files of three other packages, an Observatory report, a chezmoi design note, the Project note and KI-PRINCIPAL-MOD-011. Links to pinned GitHub revisions were left alone.
- Two links were already broken before the move and point at the same place as before: `capture-model/brief.md` to `attachments/01-3.jpg`, and `work-model/mod011-wording.md` to `work-model.svg`.
- Audit before and after: the same 23 failures, and warnings went from 185 to 186. The move added no failure.
  - The package's remaining failures were there before: the `syncing_status` field in `state.md`, the heading and the AGENDA block in `discussions.md`, and `messages.md` being empty when it should say "None".
  - The closed-list failure comes from the two untracked files in `reports/`.
- personal.reg.assistant-sol got a one-line done message in its `messages.md`: assistant `addf5e6`, published.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- 92 untracked files were left where they were, as the brief asked:
  - 88 loose reports at the top level of the package: acq-process-note, acq-recheck, acquire-held-2, acquire-held, acquire-line, apply-orca-reviews, apply-reviews, blind-broken-links, blind-dryrun, blind-e2e, blind-focus, blind-hnr, blind-last5, blind-layout, blind-orca, blind-ps, blind-queries-1, blind-queries-2, blind-rebase, blind-rename-name, blind-sync-snapshot, blind-top-level, capture-settled, conform-apps-knowledgeislands-info, conform-apps-observatory-local, conform-homebrew-tap, conform-ki-design, conform-ki-principal, conform-ki-specifications, conform-ki-techne-harness, conform-mcp-acquire-whatsapp, conform-mcp-git-audit, conform-mcp-gsuite, conform-mcp-housekeeping-chatgpt, conform-mcp-housekeeping-claude, conform-mcp-ki-kb-fs, conform-tools-ki, conform-tools-mgit, conform-tools-rig, conform-tools-techne, discussions-plan, discussions-readers, dry-run-survey, finished-tidy-fix, finished-tidy, focus-layout, footer-fields, footer-rename, handover-plan, hnr-conflicts, holding-wording, hook-nostash, ki-e2e-draft, move-procedure-add, orca-adapter, orca-release, outside-watcher, personal-shape, pin-drift, principal-resolve-2, principal-resolve-3, principal-resolve, rebase-review, rename-paperclip, reports-folder, resolve-4, resolve-5, resolve-6, resolve-7, review-finished-tidy, review-new-queries, skill-assistant, start-name, stocktake, store-rename, sweep-hnr-principal, sweep-ki-principal, sweep-legal-principal, sweep-personal-principal, sweep-va-principal, territory-stock, token-approval, top-level-cause, withdraw-adr-007, wow-cleanup, wow-lint, wow-tidy-4 and wow-tidy-move, each a `.report.md`.
  - Two notes in `reports/`: `hold-request-20261030-z.md` and `z-session-retirement-20261030.md`.
  - Two briefs in `briefs/`: `resolve-5.md` and `resolve-6.md`.
  - Because these files are untracked, `briefs/` and `reports/` still exist. The steward should receive or prune these files and move them into focus folders. Some share a name with a tracked report that has now moved, such as `conform-tools-ki`.
- Both views from `blind-focus` are still to be added to the FOCUS-SLOT-OWNER query, now that `discussions.md` exists. That is the coordinator's job.
- The audit still asks for `discussions.md`'s first heading to read "discussions". The brief said to keep the headings, so I left it.

## Queries

No outstanding queries
