# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › records-fold

**🤖 → 🧑 Handoff to supervisor · Run report at 18:17 BST · last mark 18:04 BST**

---

## Done

- MGIT-017-CONFIRM: [KI-TOOL-MGIT-CLI-017 (pruned)](https://github.com/knowledgeislands/tools-mgit/blob/1b7b486eb7c75b27acd8ed2c349e8c4448818a4e/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) now records Kris's confirmation of the provisional acceptance, quoting the 17:59 BST answer. Commit tools-mgit `ff7f44e`.
- BATS-CLEANUP, tools-mgit: captured [KI-TOOL-MGIT-CLI-027 (pruned)](https://github.com/knowledgeislands/tools-mgit/blob/524d487debb2633aca479714136532beb10db292/docs/roadmap/KI-TOOL-MGIT-CLI-027-fatal-bats-assertions.md) as a triage record covering the two territory suites (7 lines). No existing record covered this. Ledger reservation `0c03d68`, capture `c76b4d5`.
- BATS-CLEANUP, tools-rig: captured [KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md) as a triage record covering nine suites (64 lines). Capture `9752f68`.
- CONFIG-UNDER-CONTROL: no tools-rig record and no ki-principal Activity (Operations or Model) owned either concern, so I captured [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md) as a triage record. It quotes Kris's words, with "chezmoi" written in for the speech-to-text garble, and covers a recurring scan for unmanaged configuration, starting with `~/.config/mgit/`, and Rig managing app configuration. Both tools-rig records share the ledger reservation `29aae42`; this capture is `3a33d51`.
- MARK-FIELDS: [KI-HARNESS-GOV-214 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md) replaces its open field-name question with the names settled "for now": `work`; `run` and `agent` for a background run; `session` for an interactive one; and the `mark.toml` sidecar. Planning still has to name the time field. Commit harness `0fd8cb4d`.
- SYNC-GUARD: folded into [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md). Before a work resumes on another Mac and at every mark, the repositories are checked with `mgit fetch` and then `mcp-git-audit`, and anything behind or unpushed shows in the banner as `[behind]` or `[unpushed]`. `[behind]` is not yet one of the standard's housekeeping items, so the record notes that planning adds it. Commit harness `18df4784`.
- CHANNEL-TELEMETRY: this went into the notification-strategy idea in the [Ways of working Project note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md), not into [KI-TOOL-KI-CLI-123 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/683abf5f46e6e6e7076033c82b16981b90a73b56/docs/roadmap/KI-TOOL-KI-CLI-123-agent-run-events.md). That record is Done, puts phases 2 to 4 out of its scope, and is due to be pruned under ACCEPT-AND-PRUNE, so a note there would be lost. The phase plan lives in the Project note. It now records ntfy on `sol`, tailnet-only, behind the generic-push adapter, an evaluation against Gotify, Apprise and a plain tailnet webhook before phase 2 commits, and telemetry deferred. Commit ki-principal `6bdda00`. The first attempt was refused by the gate's STREAM-9 check, which bars record identifiers in a Project note; I removed the identifier and the second attempt passed.
- GRANT-INTERIM: [KI-TOOL-KI-CLI-134 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/f4811dd9310b48d8809d9143ca8864fc7b4be5e2/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) now has a Discussion paragraph: the interim hand-append sentence stays, and is removed when `--allow` ships, with the delivery's review packet naming that harness follow-up. Commit tools-ki `4e9f7e46`.
- ACQUIRE-RENAME: line 89 of `/Users/krisbrown/workspaces/personal/acquire/.ki.toml` now reads `[skills.ki-work-folder]`. Only `.ki.toml` was committed, as acquire `e94ee6a`. `ki repair` ran but exits with FAIL on two user skills unrelated to this change (query USER-SKILL-STALE).
- Pushes: every commit was pushed fast-forward in tools-mgit, tools-rig, ki-agentic-harness, ki-principal, tools-ki and acquire, and each repository was level with origin afterwards. In tools-mgit, tools-ki and ki-principal another session's dirty files stopped `pull --rebase`; in each case I fetched first and origin had not moved. Another session's commit went out beneath mine in ki-principal: `12fb1ec docs(work): mark ki.chezmoi at 18 October 18:12 BST`.
- Checks:
  - Every pre-commit gate passed, apart from the one ki-principal refusal fixed above.
  - `ki repo audit --skill ki-work-roadmap`: pass in tools-mgit, tools-rig and ki-agentic-harness.
  - `ki repo audit --skill ki-authoring`: pass in ki-agentic-harness.
  - `bun run test` and `bunx tsc --noEmit` were not run in the harness, because only roadmap Markdown changed.
  - `ki repo audit --skill ki-work-folder` fails in acquire (query ACQUIRE-CHECKPOINTS).
- Net records per repository:
  - tools-mgit: +1 ([KI-TOOL-MGIT-CLI-027 (pruned)](https://github.com/knowledgeislands/tools-mgit/blob/524d487debb2633aca479714136532beb10db292/docs/roadmap/KI-TOOL-MGIT-CLI-027-fatal-bats-assertions.md)); [KI-TOOL-MGIT-CLI-017 (pruned)](https://github.com/knowledgeislands/tools-mgit/blob/1b7b486eb7c75b27acd8ed2c349e8c4448818a4e/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) updated.
  - tools-rig: +2 ([KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md) and [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md)).
  - ki-agentic-harness: +0; [KI-HARNESS-GOV-214 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md) and [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md) updated.
  - tools-ki: +0; [KI-TOOL-KI-CLI-134 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/f4811dd9310b48d8809d9143ca8864fc7b4be5e2/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) updated.
  - ki-principal: +0; the Project note updated.
  - acquire: +0.
- Report path: under the progress protocol this report is written only at this state path, so nothing was committed for it in ki-principal.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Other sessions' uncommitted files, left untouched:
  - ki-principal: `+/_WORK/ki.chezmoi/decisions.md` (modified), `+/_WORK/ki.chezmoi/work.md` (staged), `+/_WORK/ki.chezmoi/briefs/publish-first-step.md` (untracked) and `+/_WORK/ki.ways-of-working/review-gov194-201.report.md` (untracked).
  - tools-mgit: `tests/mgit.bats`.
  - tools-ki: five `src/` agent files.
- The new triage records await adoption by their own repositories: [KI-TOOL-MGIT-CLI-027 (pruned)](https://github.com/knowledgeislands/tools-mgit/blob/524d487debb2633aca479714136532beb10db292/docs/roadmap/KI-TOOL-MGIT-CLI-027-fatal-bats-assertions.md), [KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md) and [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md).

## Queries

### ACQUIRE-CHECKPOINTS - acquire still tracks the retired checkpoints folder

**Context:** With `[skills.ki-work-folder]` now declared, `ki repo audit --skill ki-work-folder` in acquire fails STRUCTURE-1 because the tracked `+/_CHECKPOINTS/` still holds `README.md` and `acquire-intake.md`. Kris authorised only the `.ki.toml` change in that repository, so I left the folder alone.

**Query:** Should one run move acquire's checkpoint into a work folder under `ki-work-folder` and retire `+/_CHECKPOINTS/` there?

**Options:**

a) (recommended, confidence medium - it clears the only audit failure the rename exposed, and the work-folder skill already defines the move) Authorise one acquire run to move `acquire-intake.md` into `+/_WORK/<id>/work.md`, remove `+/_CHECKPOINTS/`, commit and push.

b) Leave it inside the old-checkpoint tolerance window and let acquire's own next session migrate it.

### USER-SKILL-STALE - user configuration still names two renamed skills

**Context:** `ki repair` fails because the live `~/.config/ki/config.toml` still lists user skills `ki-pmo` and `ki-pmo-design`, renamed on 18 October to `ki-coordination` and `ki-work-design`. The chezmoi source `dot_config/ki/config.toml` no longer names them, so this looks like an unapplied source change rather than a source fault. I made no change to configuration.

**Query:** Should ki.chezmoi confirm that the source carries the new names and bring this through Kris's `chezmoi diff` review and apply?

**Options:**

a) (recommended, confidence medium - the source already looks right, so only the reviewed apply is missing) Send ki.chezmoi a Messages line to check the `ki` user configuration in `chezmoi diff` and include it in Kris's next reviewed apply.

b) Leave it until the next routine `chezmoi apply`, accepting that `ki repair` reports FAIL until then.

### 🤖 → 🧑 Handoff to supervisor · since 18:17 BST

🧑 2 with you

- [with you] ACQUIRE-CHECKPOINTS · owner · since 18:17
- [with you] USER-SKILL-STALE · owner · since 18:17
- [committed] tools-mgit, tools-rig, ki-agentic-harness, ki-principal, tools-ki and acquire, pushed
