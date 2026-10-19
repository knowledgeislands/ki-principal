# obs-build-brg006 - build KI-OBSERVA-BRG-006

Repository: apps-observatory.local. Kris approved building KI-OBSERVA-BRG-006 on 2026-10-19 (TRIAGE-ANSWERS in ki-principal `+/_WORK/ki.observatory/decisions.md`; read it, and GET-MOVING). The record is at `now`.

Follow `ki-plan` to make the record Ready within its shaped scope, then `ki-implement` to deliver it to Awaiting review: tests, lint, typecheck, the roadmap audit and the 1,440 px and 760 px checks the repository declares. Where the change is visible in the Observatory, restart the service (`launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"`) and check <http://127.0.0.1:1675/>. Commit locally by explicit path; do not push, do not self-accept.BRG-006

Never run `ki repo conform` without `--dry-run`. If you touch `package.json` or `bun.lock`, commit them in your unit (the estate's hooks migration skips repositories with uncommitted changes there). If planning needs a decision outside the shaped scope, stop at Ready and report it as a query with a recommendation.
