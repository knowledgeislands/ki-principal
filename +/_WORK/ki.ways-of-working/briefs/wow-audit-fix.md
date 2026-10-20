# wow-audit-fix - clear this work's governing-audit failures in ki-principal

Work: `ki.ways-of-working` (KI > Model > Ways of working), package `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/`.

## Why

accept-wow failed [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md) (`0c8f4a32`) because ki-principal's `ki-authoring`, `ki-coordination` (161 findings, including COORD-7 report links) and `ki-work-package` (46 findings: STRUCTURE-1, RECORD-2, FOLDER-1) audits fail, some in this work's own package. Its report: `/Users/krisbrown/.local/state/ki/agents/ways-of-working/accept-wow.report.md`.

## Do

1. Run the three audits in ki-principal and split every finding by owning work folder (or no work).
2. For this work's package only, fix every finding:
   - Prune the work folder under the `ki-coordination` pruning rule. Its many untracked `*.report.md` files are received reports: delete one only where an identical copy exists at `/Users/krisbrown/.local/state/ki/agents/ways-of-working/<same name>` (compare with `cmp`); list any without an identical copy and leave it.
   - Keep the five package files, `briefs/` (do not touch `briefs/wow-audit-fix.md` or any other open brief) and `design/` notes in use.
   - Fix the remaining findings in the five package files, including MD-mech and the `state.md` prose that gives the mark as 04:22 BST (the front matter's `2026-10-20T04:20:00Z`, 05:20 BST, is canonical).
3. For each other work folder with findings, append one line to that work's `messages.md` naming the audit, finding codes and counts, and asking its worker to clear them. Write no other change in another work's folder. Findings outside any work folder go as one line to State of play's `messages.md`.
4. Re-run the three audits and report which findings remain and whose they are.
5. Commit by explicit path (a commit for this package, one for the routed lines), with conventional subjects of at most 100 characters and the pre-commit hook in force. Never `--no-verify`. Do not push.

## Bounds

- Create no roadmap record (CAPTURE-GATE). Do not change ECO-013's status.
- Do not touch other sessions' uncommitted files.
- No `ki repo conform` without `--dry-run`.
- British English, ASCII hyphens only.

## Report

The owner-report shape, written to your report path: Done, In Progress, Queries.
