# [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › [KI-OBSERVA-APP-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-045-name-unregistered-territory-member.md) › obs-build-app045

**🤖 → 👤 Handoff to supervisor · Run report at 00:20 BST**

---

## Done

- [KI-OBSERVA-APP-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-045-name-unregistered-territory-member.md) planned to Ready (`d111037`) and delivered to Awaiting review (`5847e74`), committed locally, not pushed or accepted. When a territory can't be observed because a member isn't registered, the reason and the status line now name it, for example `territory member https://github.com/knowledgeislands/ki-design is not registered on this machine`. Only `ki`'s exact one-line message for the requested handle is recognised, and only a validated `https://` host/owner/repository URL is carried. Every other failure keeps the path-free exit-status reason.
- tools-ki still has no machine-readable report (KI-TOOL-KI-CLI-154 is a draft), so the strict-match fallback is what was delivered.
- Checks: `bun run test` passed, including `degraded.test.ts`. Typecheck passed. Biome found no errors on the touched files. The roadmap audit reported FAIL=0, with 3 warnings on other records from before this run.
- 1,440 px and 760 px: `self:test:browser` skipped because Playwright's Chromium isn't installed. I checked instead with system Chrome against a temporary server whose fake `ki` returned the error. The message fits on one line at 1,440 px and wraps to three lines at 760 px, with no overflow at either width.

## In Progress

- Nothing. The Observatory service hasn't been restarted, so it is still serving the previous delivery.

## Queries

**Context:** The brief asked for a service restart. The repository's AGENTS.md says a detached background run never restarts the service and should report it as due, and the run rules forbid environment changes. I followed the repository rule.
**Query:** Should the next interactive session run the restart?
**Options:** a) (recommended, confidence high - AGENTS.md assigns it there) Run `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"` in the next interactive session and check http://127.0.0.1:1675/. b) Authorise detached runs to restart it in future briefs, which would mean changing AGENTS.md.
