# [KI](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/work.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-build-brg006

**🤖 → 👤 Handoff to supervisor · Run report at 00:13 BST**

---

## Done

[KI-OBSERVA-BRG-006](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md) is planned to Ready (`36dfdb8`) and delivered to Awaiting review (`107c852`), committed locally and not pushed.

- A feedback send to a work package now adds one line at the end of the package's `messages.md`, replacing a lone `None`, and leaves `work.md` untouched. A single-file work still takes the line in its `## Messages` section. A package with no `messages.md` is refused with that reason, and the refusal gets a receipt. Sending stays switched off.
- The give-feedback guide, OBS-ACT-014 in the authority specification and the changelog now say where a send lands.
- Tests: all 8 tasks pass, with five new tests for the package shape and the degraded check. Typecheck passes and lint reports no errors.
- Roadmap audit: FAIL=0. Its three warnings are about other records and were there before this run.
- The service at http://127.0.0.1:1675/ answers. The 1,440 px and 760 px browser checks were skipped because Chromium isn't installed for Playwright, and installing it needs the network. Nothing on screen changes while sending is off.

## In Progress

- The service still needs a restart. This was a detached run, so I didn't restart it. The next interactive session should run `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"`.
- The records diagram `capture-feedback` still labels the send's target `work.md ## Messages`. That is still right for a single-file work. Re-rendering it needs Archify and Chromium, so it waits for a diagram pass.
- The record is waiting for your `ki-accept` review. Once it's accepted, KI-OBSERVA-BRG-004 (turning sending on) is no longer blocked by it.

## Queries

None.
