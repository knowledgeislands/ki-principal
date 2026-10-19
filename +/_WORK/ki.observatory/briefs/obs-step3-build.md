# obs-step3-build - Build the authorised step 3 Observatory work

Work in apps-observatory.local for KI > Model > Observatory, whose work package is ki-principal `+/_WORK/ki.observatory/` (read `decisions.md` there; do not edit the package). Kris has said "so, can you get some of the changes moving?" (GET-MOVING): build the step 3 work already authorised, under the repository's AGENTS.md, its engineering standards and `ki-work-roadmap`.

**Authorised, in Kris's words in `decisions.md`:** STEP3-ANSWERS (step 3 Act first; island maturity declared, not commit age; HEXMAP vendored mechanically from a pinned ki-design commit with a drift check; CAPITAL-GLYPH `capital`), STEP3-LATER (RUN-EVIDENCE: the Sessions tab's run repository), NEW-MARK (new since the previous observation), LARGE-SCREEN-REVISIT (large screens first, not only; keep PDR-KI-OBSERVA-002's 760 px rule and width test), NARROW-DECLARE (new tables declare their dropped columns), PUSH-ALL (lose nothing; retire no tab, route or capability).

**Do:**

1. Read the step 3 records, including KI-OBSERVA-BRG-005, KI-OBSERVA-BCN-008, KI-OBSERVA-VIS-030 and KI-OBSERVA-VIS-031, and any other record step 3 names. Choose the order by dependency, Act board parts (KI-OBSERVA-BRG-005) first unless something blocks it.
2. For each record in turn: plan it to Ready where it is not, build it, run the repository's checks and tests, mark it done under `ki-work-roadmap`, and commit it by explicit path, one commit per record. Restart the service with `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"` and check <http://127.0.0.1:1675/> still serves each tab.
3. Stop after three records or about 90 minutes, whichever comes first, at a clean commit.

**Not in scope:** the switchboard and the tailnet view (STEP3-LATER), merging KI-OBSERVA-VIS-029, VIS-032, VIS-033 or VIS-034, KI-OBSERVA-VIS-042 (waits on KI-HARNESS-GOV-224), records in any other repository, and any push. Where a record needs a decision the authorised words do not cover, stop that record, leave it uncommitted or unbuilt, and raise a query; move to the next record if it is independent.

Report in owner-report shape: Done gives one line per record with its commit, tests run and the service check; In Progress says what is left; Queries carries Context, Query and Options with a recommended option and confidence, or `No outstanding queries`.
