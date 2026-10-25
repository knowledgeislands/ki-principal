# wow-replay-smoke - prove the tap's dispatch reaches the harness

Under HARNESS-CONSUMER ("Add, keep poll", 2026-10-25) and tap commit `ef2ad37`, run step 6 of the tap's onboarding guide once: `gh workflow run CI --repo knowledgeislands/homebrew-tap -f formula=ki`. Watch the tap run until it finishes and confirm its summary reports dispatching ki v0.13.0 to `knowledgeislands/ki-agentic-harness`. Then find the harness `update-ki-pin` run the dispatch triggered and confirm it exits with "pin v0.13.0 is current; nothing to propose".

Make that one dispatch and read-only `gh` calls only. Change no file, setting or credential, cut no release, and do not re-run anything. If the dispatch fails, stop and report it.

Report as an owner report: Done with both run links and results, In Progress, and Queries with Context, Query and Options, recommended first with confidence and reason.
