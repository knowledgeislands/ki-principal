# roadmap-census-2

Read-only. Make no writes or commits. Kris asked on 20 October: "things that are on hold, we need to re-validate everything, make sure it really is. On hold, why is anything on hold in the observatory, for example?" Kris also asked for every triaged item in Knowledge Islands to be progressed.

Cover every Knowledge Islands repository that the local registry and `Admin/Governance/Known Lands.md` list, plus chezmoi at `~/.local/share/chezmoi`, and every work package in `ki-principal/+/_WORK/`.

1. **Holds.** List every on-hold roadmap record and every on-hold work package. For each, give:
   - its hold condition and reason
   - whether the condition is met, still valid, stale or missing
   - its owning work
   - your recommendation (keep, release to a horizon, or cancel), with confidence and a one-line reason

   Answer the Observatory question directly: why each apps-observatory.local and ki-design hold exists, and whether it should still stand. Exclude the 12 email-routing records in mcp-m365 and mcp-gsuite, which now belong to Humans not Robots.
2. **Triage.** Count the unadopted triage records per repository now, and compare with about 57 on the evening of 19 October. Name each repository whose triage pile has no live work running a pass on it (check `ki agent status`). The lanes are:
   - ki.tools-burndown: tools-ki, tools-mgit, tools-git-almanac, mcp-git-audit
   - ki.mac-studio-setup: tools-rig
   - ki.observatory: apps-observatory.local, ki-design, website design adoption
   - ki.ways-of-working: ki-agentic-harness, ki-principal, ki-specifications
   - ki.chezmoi: chezmoi
3. Group releases by owning work, so State of play can route them in one line each. Put cancellations into one query for Kris.

## Rules

- CAPTURE-GATE (Kris, 19 October): create no roadmap record. List follow-ups in your report.
- HOOKS-MIGRATION: never run `ki repo conform` without `--dry-run`. Do not touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`.
- Other works' runs are active across the territory. Leave alone any file another session is changing, and name it in your report.
- Commit only your own changes, by explicit path on the commit command, using Conventional Commits and ending with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>". Do not push.
- British English, ASCII hyphens only.
- Report to the path your run packet names, as an owner report: Done, In Progress, Queries. Each query needs Context, Query and Options, with a) recommended and its confidence.
