# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › coordination-rename

**🤖 → 🧑 Handoff to supervisor · Run report at 10:36 BST · last mark 22:34 BST**

---

## Done

- ACCEPT-136: [KI-TOOL-KI-CLI-136](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-136-errors-suggest-fixes.md) accepted as done, with the `storeFix` access-grant follow-up recorded, in tools-ki `f20eaa65`, pushed.
- PMO-NAME and DESIGN-NAME: `ki-pmo` is now `ki-coordination` and `ki-pmo-design` is now `ki-work-design`, with no alias. The change renames the folders, standards and guide, renames the rubric family `PMO` to `COORD` (item numbers kept), and updates every live reference, the catalogue, the hook, the output style, `.ki.toml` and the tests. Harness `c4cbb5aa`, pushed. `bun run test` passed (1253), `bunx tsc --noEmit` passed, 7 generated surfaces are in sync, and the focused audits found no new failure.
- Harness diagrams: the skill map and the coordination and records-and-code area diagrams were rebuilt at the rename commit, and the thread-model's traced source and README prose were repointed, in `157896d3`, pushed. Tests passed and `ki-diagrams` reports WARN only.
- STREAMS-SLIM: `ki-repo-kb-streams` no longer has the ITERATE, PROPOSE, READY and ROLLOUT modes or their files. It now links to `ki-work-roadmap`'s status and horizon table instead of repeating it, and keeps its container and Enactment-gate jobs. Harness `92c0db6c`, pushed. Tests and tsc passed, `ki-skills` and `ki-repo-harness` are back at their baseline warnings, and the audit against Knowledge Islands Principal passes with WARN only.
- [KI-HARNESS-GOV-217](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-217-coordination-and-work-design-renames.md) is at awaiting review with its review packet, in `437e0543`, pushed.
- CLI side and WORKER-CLI: `ki` now requires `ki-work-design` as a bootstrap skill. Comments, the manual, `man/ki.commands.json` and the background-agents guide now name `ki-coordination`. The `ki agent` help for `home`, `decide`, `reconcile`, `status`, `send --from`, `--repo`, `--log` and `--class` now says work folder and the work's decisions log, and one CHANGELOG line records the change. [KI-TOOL-KI-CLI-148](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-148-coordination-rename-cli-side.md) is at awaiting review. tools-ki `53bee079` (number reserve) and `f33b95d7`, pushed. `bun run test` passed (1334), and tsc, knip and mandoc passed. `ki repo audit --repo .` still fails BIO-1 on files this change does not touch and on a `biome.json` schema that names 2.5.12 while 2.5.15 is installed; the touched files pass Biome.
- ki-principal: `.ki.toml` declares `[skills.ki-coordination]`, and the AGENTS.md reply-forms pointer and the ways-of-working and skill-refresh Project notes are updated, in `dec5595`, pushed. `ki repo repair` relinked the projected skills and reports healthy, so the coordinator's held work-folder files can now pass the hook. The pull was refused because other sessions have staged files there, but origin had not moved, so the push was a fast-forward of my commit alone.
- Other territories: the COORD-RENAME-HANDOFF line in the [ways-of-working work file](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md) Messages lists the seven `.ki.toml` files outside Knowledge Islands that still declare `[skills.ki-pmo]` (er, hnr, legal, si, tmx, va and personal principals) and the chezmoi source files, in ki-principal `fcf8624`, pushed. No other territory was changed.
- Net open roadmap records from this run: ki-agentic-harness +1 (GOV-217 opened); tools-ki 0 (CLI-148 opened, CLI-136 closed); ki-principal 0. Other sessions opened GOV-211 to GOV-216 and CLI-149 in the same window.
- Every push carried only this run's commits. No other session's commit was pushed, and no other session's dirty file was touched: ki-principal's `+/_WORK/ki.chezmoi/decisions.md`, `+/_WORK/ki.ways-of-working/decisions.md` and its staged reports, `+/_THREADS/`, and `+/_WORK/ki.ways-of-working/design/work-folder.md`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The thread-model diagram stays pinned at `b7d3b53e`, where its `ki-pmo` paths and lines still exist. Renaming its label and sources means re-tracing it at HEAD, which is a separate diagram refresh.
- `ki agent` output strings still say "thread home" (`no thread home` and "Thread home of <run> is now"). Tests assert them as behaviour, and they are noted in CLI-148.
- The tools-ki BIO-1 Biome failure predates this run.
- `ki-checkpoint` and the work-folder, clean-out and close-out rules are untouched, as the 10:15 amendment set, and are left for `work-folder-design`.

## Queries

### RELEASE-REPIN - Release a `ki` that pins the renamed harness

**Context:** Released `ki` (v0.11.1 and the v0.11.0 that ki-principal's CI installs) pins harness `4cae827`, which still has `ki-pmo` and `ki-pmo-design`. CI in any repository that now declares `[skills.ki-coordination]`, starting with ki-principal, will fail its `ki repo repair` step, and a fresh bootstrap from tools-ki source will refuse the pinned harness. Repinning needs the pushed harness commit (`437e0543` or later) and its archive digest, and any release after v0.11.1 asks you first.

**Query:** Shall a release run cut v0.11.2, repinning the canonical harness to the current pushed harness `main`?

**Options:**

a) (recommended, confidence medium - the CI break is certain, but release timing is yours) Yes: launch a release run to repin `canonicalHarnessRelease` to the current harness `main` with its digest, cut v0.11.2, and bump ki-principal's `.github/ki-version`.

b) Not yet: accept failing CI in declaring repositories until the next planned release.

### USER-SKILL-LINKS - Fix the user-level links and chezmoi config

**Context:** `~/.claude/skills/` and `~/.agents/skills/` still hold `ki-pmo` and `ki-pmo-design` links that now point at missing folders. The chezmoi-managed `~/.config/ki/config.toml` still declares `[skills.ki-pmo]` and `[skills.ki-pmo-design]`. The chezmoi source also names them in `tests/ki-config-skills.test.mjs`, `dot_claude/private_communication.md`, `dot_claude/private_delegation.md.tmpl` and `dot_codex/private_AGENTS.md.tmpl`. Fixing this changes the environment, so I did not do it.

**Query:** Shall the ki.chezmoi work rename these in the chezmoi source, apply after a reviewed `chezmoi diff`, then run `ki repair` to relink the user skills?

**Options:**

a) (recommended, confidence medium - a mechanical rename, but it changes the live environment) Yes: route it to the ki.chezmoi work through the handoff line already in the ways-of-working Messages, with your approval of the diff before `chezmoi apply` and `ki repair`.

b) Leave it until the chezmoi work next picks it up on its own.

### DECIDE-NUMBERS - `ki agent decide` still numbers decisions

**Context:** `ki agent decide` appends `## Decision <n>` headings and `reconcile` finds entries by that number. The coordination standard keeps the decisions log without numbering, and the log's own entries are headed `## <date> <time> BST - <subject>`. The help text, now in work-model words under WORKER-CLI, still says "numbered" because it describes the behaviour truthfully; changing the behaviour was outside this run.

**Query:** Shall tools-ki capture a record to make `decide` write timestamped, unnumbered headings and `reconcile` address entries by timestamp?

**Options:**

a) (recommended, confidence medium - it aligns the tool with the standard, but it changes a command other runs use) Yes: capture one tools-ki record at Next for the behaviour change.

b) No: keep the numbered headings and note the difference in the standard.
