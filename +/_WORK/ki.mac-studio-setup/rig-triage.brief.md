# rig-triage brief

Run for the work `ki.mac-studio-setup` in Knowledge Islands Principal: the tools-rig lane's triage pass.

## Task

1. List every unadopted Triage record in `/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/`. For each, use `ki-next` to give a recommended disposition (adopt into Now, Next, Future, hold, merge into another record, cancel) with its confidence (`high`, `medium` or `low`) and a one-line reason.
2. Adopt every record whose high-confidence recommendation is to adopt it into Now, and deliver each one, one at a time, with `ki-plan` to Ready and then `ki-implement` to Awaiting review. tools-rig's own checks and tests must pass for each. Never self-accept.
3. Record, but do not apply, every medium- or low-confidence recommendation and every cancellation, merge or deletion. They go to Kris as one lane query.
4. Leave alone KI-TOOL-RIG-CORE-062 (draft, waiting for Kris's answers) and KI-TOOL-RIG-CLI-027 (being planned by the run before you).

## Authority

- Owner decisions, Kris, 19 October, relayed by State of play. TRIAGE-ALL: "Okay, there's a lot of items in triage. I need them all triaging. So I want them all running out with the high order functions and anything which is High confidence recommended. Let's move it into now and get it done. Especially to focus on anything to do with the tools burn-downs first." No roadmap cap.
- CAPTURE-GATE: create no new records. Small audit fixes may be done without a record. Ideas go to the coordinator in your report, not into records.
- Work only in `/Users/krisbrown/workspaces/knowledge-islands/tools-rig`. Run `git -C /Users/krisbrown/workspaces/knowledge-islands/tools-rig status` before you start. If another session has uncommitted changes there, do not touch them, and stop and report if they overlap your files.
- Commit each completed, verified unit by explicit path under `ki-git`, with Conventional Commit subjects of at most 100 characters and the closing line `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Never use `--no-verify`.
- Do not push, release, tag, accept, prune or touch any other repository. No remote operations beyond `git fetch`. Do not change sol's or terra's live configuration: no `chezmoi apply`, `rig apply`, `sudo`, `launchctl`, `pfctl` or firewall changes.
- Leave `package.json`, `bun.lock`, `.husky/` and `.githooks/` committed and clean (HOOKS-MIGRATION). Never run `ki repo conform` without `--dry-run`.
- If an item needs Kris, stop on that item at a safe point and carry on with the others.

## Report

Write `/Users/krisbrown/.local/state/ki/agents/mac-studio-setup/rig-triage.report.md` in the `ki-coordination` owner-report shape. Include a table of every triage record with its disposition, confidence, reason and what you did, and every commit. Give one lane query, `RIG-TRIAGE`, listing the medium- and low-confidence items and every cancellation, merge or deletion, each with a lettered recommendation. Cite every record by its full identifier, linked to its local file by absolute path. Use British English and ASCII hyphens only.
