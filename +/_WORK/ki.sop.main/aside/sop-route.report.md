# [Knowledge Islands](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › sop-route

**🤖 → 👤 Handoff to supervisor · Run report at 01:48 GMT · last mark 16:17 GMT**

---

## Done

- STOA-ICONS and both addenda (hnr.sop.5ge) went to [ki.reg.main messages](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.reg.main/messages.md) as one line, because no KI work package or Project scopes `packages-stoa`. The line carries the runtime cycle (0.28.0 to v0.30.2, `element.js:5` to `sun-dial.js:13`), all 46 icon mappings and hnr.sop.5ge's `messages.md` as the reply address. Stoa is unchanged.
- DIAGRAM-TOOLS (ki.prj.ways-of-working) went to [ki.reg.main messages](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.reg.main/messages.md) because no work's scope takes `ki-diagrams` or `ki-authoring` skill changes. The line carries Kris's ranking in full and links the [DIAGRAM-TOOLS decision](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md#diagram-tools---2026-10-29). ki.prj.baseline-rollout scopes only rolling out archify, not changing the skills.
- Both lines are in one commit, `4b52fcd8` (`docs(work): ki.reg.main receive STOA-ICONS and DIAGRAM-TOOLS messages`), because both went to the same package. The pre-commit audit passed.
- The two ACCEPT queries are drafted below. Neither record was accepted or changed.
- [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) was re-checked read-only at tools-rig `HEAD`: `tests/rig-default-applications.bats` passes 22 of 22, including the two new confirmation tests; `shellcheck` on the module passes; `scripts/assemble-rig --check` passes.
- [PERSONAL-DOTFILES-UE-106](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-106-apply-tower-assistant-at-applications.md) was re-checked read-only on sol: the app exists only in `/Applications`, there are no test plists, and `rig doctor` has no `dock-item-path-missing:tower-assistant`. terra could not be checked from here.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- ki.reg.main now holds STOA-ICONS and DIAGRAM-TOOLS. It owns their priority and execution, and its replies go to hnr.sop.5ge and ki.prj.ways-of-working.
- Since 29 October, sol's `rig doctor` also reports eight npm-installed tools as missing, among them `typescript`, `wrangler` and `turbo`. This is outside both records and is left for sol's health work.

## Queries

### ACCEPT-RIG-070 - Accept the default-handler confirmation wait in Rig

**Context:** [KI-TOOL-RIG-CORE-070](/Users/krisbrown/kis/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) has been awaiting review since 27 October (commit `e882998`). It changes how `rig apply` sets a default app for a file type, such as Zed for `.toml`. When macOS asks you to confirm the change, Rig used to check straight away, see the old app and record a failure, so a second run was needed. Now it waits up to 120 seconds when run from a terminal, and not at all when unattended, with an environment variable to override the wait. It reports four outcomes separately: confirmed, unanswered or declined, unattended, and ineffective. The full test suite (648 tests) and the gate passed at delivery. Today's read-only re-check passed the default-applications tests (22 of 22, both new tests included), shellcheck and the assembly check. Not yet done: the record's own attended check, a real `rig apply` that raises the macOS prompt, which only you can do. sol currently has `.toml` opening in VS Code instead of Zed, so a `rig apply` there would raise that prompt. Two concerns remain: a declined prompt looks the same as an unanswered one, and a run piped from a terminal gets no wait unless the variable is set.

**Query:** Do you accept KI-TOOL-RIG-CORE-070 as done?

**Options:**

a) (recommended, confidence medium - the code, tests and documents check out, but the one real-prompt check has not been run) Accept it after one attended `rig apply` on sol: accept the macOS prompt for `.toml`, and confirm Rig records Zed as applied on that first run.

b) Accept it now on the test evidence, and treat the attended prompt as observed the next time a handler apply happens.

c) Leave it awaiting review until both terra and sol have shown the prompt behaviour.

### ACCEPT-UE106 - Accept the Tower Assistant move to /Applications

**Context:** [PERSONAL-DOTFILES-UE-106](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-106-apply-tower-assistant-at-applications.md) moved Tower Assistant 2.1 to `/Applications` on both Macs (commit `9667f9e`). Each Dock now points there, `rig doctor` no longer reports the missing Dock path, and the leftover test preference files on terra are gone: fourteen were removed rather than the planned eleven, with apps-tower's confirmation. The record's Verify asks for exactly two things: no test plists on terra, and no `dock-item-path-missing:tower-assistant` on either Mac. sol meets both today. I re-checked it read-only: the app is only in `/Applications`, there are no test plists, and `rig doctor` has no missing-path finding. terra rests on evidence from 24 October and could not be re-checked from sol. sol's `rig doctor` is still unhealthy for unrelated reasons, all outside this record: Dock order drift, `.toml` opening in VS Code, the Screen Sharing firewall anchor, UTM, and, new since 29 October, eight missing npm tools. The app's own attended checks stay with apps-tower (PERSONAL-TOWER-APP-005 and PERSONAL-TOWER-APP-006).

**Query:** Do you accept PERSONAL-DOTFILES-UE-106 as done?

**Options:**

a) (recommended, confidence medium - sol meets Verify today, but terra's half rests on evidence that is six days old) Accept it now, leaving sol's other `rig doctor` findings to sol's health work.

b) Accept it only after a read-only `rig doctor` and test-plist check on terra confirms its half still holds.

c) Leave it awaiting review until apps-tower's attended checks (PERSONAL-TOWER-APP-005 and PERSONAL-TOWER-APP-006) are done.

### 🤖 → 👤 Handoff to supervisor · since 01:48 GMT

👤 2 with you · 📥 2 to accept

- [with you] ACCEPT-RIG-070 · owner · since 01:48
- [with you] ACCEPT-UE106 · owner · since 01:48
- [committed] ki.reg.main messages

🧵 ki.sop.main
