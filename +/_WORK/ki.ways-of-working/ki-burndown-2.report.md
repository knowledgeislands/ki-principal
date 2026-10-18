# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › ki-burndown-2

**🤖 → 🧑 Handoff to supervisor · Run report at 06:32 BST · last mark 06:05 BST**

---

## Done

I tested against isolated HOME and XDG fixtures only. Both repositories are pushed fast-forward to `main`; no other session's commits were beneath mine. Nothing live was touched, and I made no release.

- HARNESS-PATHS: [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md) is adopted and planned (`f2ef98e2`) with Fable's two refinements, and delivered (`49686ca3`). Awaiting review.
  - Each Mac now keeps its remembered harness checkouts in its own `$XDG_STATE_HOME/ki/locals.toml`.
  - `ki bootstrap` and `ki dev local set` copy `config.toml` `[locals]` there once. After that, `config.toml` entries are ignored with a warning, and `config.toml` itself is left untouched.
  - `ki dev local on` refuses when the remembered checkout is missing, rather than picking another source.
  - Checks: the full coverage suite (1309 tests) passes at 100%; tsc, Biome, the man-page lint and the commit gate pass.
- DESK-KIT-SOP a): state-of-play's [work file](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/work.md) has the Messages line to drop desk-kit from next step 3, THREADS-ORPHANS and "KI > mics / webcams" (`b7a8956`). The commit gate passes.

Provisional, for Kris to confirm. Each is recorded in KI-TOOL-KI-CLI-143's review:

- adopting KI-TOOL-KI-CLI-143 on Fable's opinion;
- the file name `locals.toml` and its `[locals]` shape;
- keeping `config.toml` `[locals]` verbatim rather than deleting it;
- read-only commands and `on|off` reading the entries before they move;
- plain `ki bootstrap`, not only `--refresh`, doing the move;
- `ki repair` reading the same combined configuration as `ki doctor`.

## In Progress

Nothing is running.

Waiting for Kris:

- Accept [KI-TOOL-KI-CLI-126](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-126-unavailable-store-breaks-repair.md). [KI-TOOL-KI-CLI-131](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-131-host-absent-store-state.md) is planned but stays in draft until then, because the roadmap audit refuses an active record whose blocker is not done. [KI-TOOL-KI-CLI-136](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-136-errors-suggest-fixes.md) follows -131. I started neither.
- Review KI-TOOL-KI-CLI-143 alongside the tools-ki ki-accept group. TOOLS-RELEASE now covers -143 too.
- The mgit row has nothing left for me. [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) waits for you to accept it. [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md) to [KI-TOOL-MGIT-CLI-022](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-022-external-member-review-findings.md) are in triage and wait for adoption.

Outstanding - no action requested now:

- [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) and [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) stay blocked. [KI-TOOL-KI-CLI-147](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-147-agent-state-folder-tooling.md) is in triage. -138, -135 and -133 are awaiting review.
- [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md)'s "Decision 55" citations stay parked.

## Queries

### HARNESS-PATHS-LIVE - moving Terra and Sol to the host-local file

**Context:** Neither Mac runs KI-TOOL-KI-CLI-143 yet. Once an installed build carries it, every `ki` command warns until `ki bootstrap` moves the entries. After the move it warns that `config.toml` `[locals]` is ignored, until the chezmoi source drops the table.

**Query:** How should the live move happen?

**Options:**

a) (recommended, confidence medium) After the release that carries -143, run `ki bootstrap` on Terra and on Sol and check each Mac's development status. Then remove `[locals]` from the chezmoi source in its own chezmoi record. b) Do the move now, from a development build, before any release. c) Keep `[locals]` in the chezmoi source and live with the warning.

### 🤖 → 🧑 Handoff to supervisor · since 06:32 BST

🧑 1 with you · 🏁 run finished

- [with you] HARNESS-PATHS-LIVE · owner · since 06:32
- [with you] accept KI-TOOL-KI-CLI-126 to unblock -131 and -136 · owner · since 06:32
- [committed] tools-ki and ki-principal, pushed
