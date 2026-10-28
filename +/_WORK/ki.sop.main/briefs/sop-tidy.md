# sop-tidy: bring ki.sop.main to a clean baseline

Authority: Kris on 28 October (BASELINE-CLEAN). Work only in `+/_WORK/ki.sop.main/` in ki-principal, plus single appended lines in other packages' `messages.md` when routing. No roadmap records, no acceptance, no launches, no change to any repository but ki-principal. Read `ki-work-package` and `ki-coordination` (installed skills under `/Users/krisbrown/.agents/skills/`) for the package rules, routing and tidying. Do not edit `decisions.md` except to append one line per message disposition that needed judgement, if the standard asks for it.

1. **messages.md.** Leave every `IMPORTANT ... REFRESH` line in place (the coordinator handles those). For every other line, in queue order, decide one disposition and act:
   - done, superseded or stale: evidence (commit, record state, later message) in the report; remove the line;
   - belongs to a KI package: append it as one line to that package's `messages.md` (`from KI > SoP (ki.sop.main)`), remove it here; current package ids are `ki.prj.*`, `ki.reg.main`, `ki.sop.main`;
   - belongs to another territory: append to that territory's State of play `messages.md` only if that route is already authorised in the work packages; otherwise treat as needs-Kris;
   - needs Kris: add a query under `## Open` in `queries.md` (`### <TAG> - <title>`, Context, Query, Options with a) recommended first carrying confidence and reason), remove the line;
   - needs work State of play should launch: keep the line, and list it in the report as a proposed launch with brief outline.
2. **queries.md parked.** Check each parked query against current evidence. Do not delete any; list in the report those obsolete by events, with evidence, and those still live.
3. **Other files.** For `skills-assessment.report.md` and each `design/` note, delete only where the tidy and design-note guards clearly allow (outcome homed, queries copied, graduated or superseded), naming the evidence; keep anything in doubt.
4. **state.md.** Rewrite the body (not the front matter) as a compact current picture, under about 250 words: Now, next steps, and nothing historical that Git holds.
5. Commit by explicit path only, in logical commits with subjects `docs(work): ki.sop.main tidy, <what>`, each ending `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Fetch, pull fast-forward only, push fast-forward only; never force or `--no-verify`; stop on divergence. Leave other sessions' uncommitted files alone and name them.

Report to `/Users/krisbrown/.local/state/ki/agents/ki-sop-main/sop-tidy.report.md` in owner-report form: Done (counts and each disposition, one line each), In Progress (proposed launches, obsolete parked queries with evidence), Queries (any new needs-Kris queries in full, or "No outstanding queries"). Plain British English, no em-dashes.
