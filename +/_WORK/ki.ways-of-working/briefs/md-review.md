# md-review - blind review of MATURITY-DECLINE

Blind review. Do not read any `+/_WORK/` file or run report. Read-only: KI-HARNESS-GOV-223 in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/`, the `ki-repo` standard and `ki repo audit` source in tools-ki. No edits, commits, launches or network calls.

**Context:** KI-HARNESS-GOV-223 adds a declared island maturity level (founding, growing, settled, thriving) to `.ki.toml`. "Ruin" and "decline" are derived from audit health, not declared: "ruin" is failing checks or an audit that cannot run. "Decline" was described as warnings left open beyond a tolerance, but no tolerance is set and `ki repo audit` keeps no history, so nothing knows a warning's age. A tools-ki reader that shows the signal waits on this record. **Query:** How should "decline" be defined so the record can go Ready? **Options:** (unranked)

- Decline is: the latest audit has open warnings and no failures; no age or tolerance.
- Keep an age rule with a 30-day tolerance, and give the tools-ki reader the job of keeping audit history to measure it.

## Report

Owner report: Done (pick, confidence, reason, conditions), In Progress, Queries.
