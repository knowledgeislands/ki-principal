# wow-overnight-plan - write the overnight burndown briefs

You plan; you deliver nothing. Write one run brief per unit of overnight work into `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/`, named `wow-night-<slug>.md`, plus `briefs/wow-night-order.md` giving the dispatch order, each run's runtime (`codex` or `claude`), effort, `--rules` (`none` or `push`), `--workdir`, `--add-dir` list and any `--wait-for`. Change no repository file outside that folder, commit nothing and make no remote call.

## Sources

- Kris's answers in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md`, the entry "2026-10-21 01:40 BST - overnight answers and mark", and the earlier OVERNIGHT-BURNDOWN entry. These are the only grants.
- The sweep and its blind review: `~/.local/state/ki/agents/ways-of-working/wow-overnight-sweep.report.md` and `wow-overnight-review.report.md`. Where they differ, the review's view is what Kris accepted.
- The held queues: `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md` and `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/messages.md`, with each work's `decisions.md` and `queries.md`.
- Each target record, its repository's `AGENTS.md`, roadmap guide and release guide.

## Units to brief

1. KI-TOOL-RIG-CORE-048 and KI-TOOL-RIG-CORE-067 in tools-rig: deliver against test fixtures, one run each, chained because they share a repository.
2. KI-TOOL-RIG-CORE-056: the written investigation only, `--wait-for` nothing but stating that it starts only once ki.chezmoi's Rig hook fix (RIG-PRECOMMIT-BATS) has landed on tools-rig main; the run checks that and stops if not.
3. KI-TOOL-KI-CLI-140: offline planning only.
4. KI-TOOL-KI-CLI-156: deliver, with read-only GitHub Actions reads on tools-ki only.
5. KI-OBSERVA-BRG-006: a headless check at exactly 1,440 and 760 px with screenshots, which replaces Kris's running-site check, then acceptance if it passes.
6. Release candidates for tools-ki and tools-rig once accepted work lands: prepare the named candidate (commit range, version, CI proof, the exact tag and publish commands) for Kris to tag; tag and publish nothing.
7. Each authorised or mechanical line in the two held queues: group lines that touch the same repository into one run; leave out any line needing a Kris decision, new capture beyond an approved split, a live apply, source deletion, credentials or publication, and list each left-out line with its reason in `wow-night-order.md`.
8. Parked queries in this work's and those two works' `queries.md` that are overtaken: one run that verifies each individually and strikes only those verified.
9. Any other record the review named as workable tonight in a `tools-*`, `mcp-*` or `apps-*` repository.

Do not brief: the 11 email-routing records in mcp-m365 and mcp-gsuite (hnr.email-routing owns them), KI-TOOL-KI-CLI-139, KI-TOOL-RIG-CORE-053, KI-TOOL-KI-CLI-145, KI-TOOL-RIG-CORE-064, KI-TOOL-KI-CLI-149, KI-TOOL-KI-CLI-160, the Observatory's TEN-COMMITS, MERMAID-HANDLER, BRIDGE-STALE and RESTRUCTURE, KI-OBSERVA-BRG-004, -005 and KI-WEBSITE-SITE-044.

## Each brief must carry

- One unit, its record by full ID, the target repository's absolute path, the done condition and the verification to run.
- An acceptance brief carries the sentence `Override: for <ID> only, this grant overrides the standing rule "Never accept work records"`, quoting the 01:40 decision.
- Rules: edits to ki-agentic-harness or tools-ki only in a worktree; commit by explicit path; never `--no-verify` and never force-push; push fast-forward only when the run's own commits alone are stacked, otherwise leave them unpushed and say so; never push another session's commits; create no new record (CAPTURE-GATE) and send follow-ups as one line in the owning work's `messages.md`; no live apply, credential access, source deletion, publication or tag; British English, ASCII hyphens only, they/them for people.
- Stop conditions written once, cleanly, with no later overrides.
- The report rule: the `ki-coordination` owner report to the coordinator, with any query in Context, Query and Options form.

## Report

Report the briefs written, the dispatch order, what was left out and why, and any query for Kris.
