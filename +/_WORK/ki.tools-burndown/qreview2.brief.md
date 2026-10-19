# qreview2 - blind review of two release queries

Blind query review under the ki-coordination standard's Query review section. Two open queries follow, with Context, Query and Options only; option letters carry no ranking. Check what you can directly and read-only: /Users/krisbrown/workspaces/knowledge-islands/tools-ki (local `v0.11.5` preparation and the pin run's work), /Users/krisbrown/workspaces/knowledge-islands/tools-mgit (`9a3564d` and HEAD), /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness, and the reports in /Users/krisbrown/.local/state/ki/agents/tools-burndown/ (cli155, pin if present, mgitrel, mgitdep). Rerun the repository gates read-only where you can. Give your own pick, a confidence and a one-line reason, plus one line on what you verified. Change nothing; no network calls.

Write the result to /Users/krisbrown/.local/state/ki/agents/tools-burndown/qreview2.report.md: one `### <TAG>` section per query with `**Pick:**`, `**Confidence:**`, `**Reason:**`, `**Checked:**`. Then stop.

## MGIT-GO - Accept KI-TOOL-MGIT-CLI-023 and cut the mgit release

**Context:** Through ki.ways-of-working: you ran the hands-on check of [KI-TOOL-MGIT-CLI-023](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-023-hands-on-behaviour-check.md) and it passed, and MGIT-RELEASE a) asks for acceptance with you and then one mgit release. The record still reads `draft`. [KI-TOOL-MGIT-CLI-028](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-028-learn-majority-output.md) is also Awaiting review. KI-TOOL-MGIT-CLI-023 is now Awaiting review with your check as its evidence, and `v0.18.0` is prepared locally (`9a3564d`): Bats 135 of 135, shellcheck, mandoc and `ki repo audit` FAIL=0. mgitdep then added KI-TOOL-MGIT-CLI-029 (the four CLI departures) as two roadmap-only commits on top; the tag goes on the gated `9a3564d` (MGIT-TAG-TARGET a), taken by the coordinator). Cutting it pushes main and the tag, creates the GitHub release, verifies the installer and lets the Homebrew tap notifier open its formula pull request; CONSUMER-MIGRATE (ki.chezmoi) follows.

**Query:** May I accept KI-TOOL-MGIT-CLI-023 on your passed check and cut, push and publish the mgit release once the tools-mgit gate passes?

**Options:**

a) asks for exactly this, but publishing rests on run reports I have not verified directly) Yes, accept KI-TOOL-MGIT-CLI-023, and cut the release when the gate passes; KI-TOOL-MGIT-CLI-028 rides with it only if you accept it in the burndown acceptance batch.

b) Bring the acceptance and the finished release back to you before the tag.

### KI-RELEASE-GO - Cut the ki patch release once it is ready

**Context:** Through ki.ways-of-working you asked for one `ki` patch release "soon", carrying KI-TOOL-KI-CLI-155 so `priority` and `size` stop dropping 18 records, and pinning a ki-agentic-harness that provides `ki-work-package`, so ki-principal CI stops failing at "Install released KI". Your standing rule is to ask before any `ki` release. The cli155 run is building the change now and stops before tagging, pushing or publishing.

**Query:** May I cut, push and publish the patch release as soon as KI-TOOL-KI-CLI-155 passes verification and the harness pin sits at or after the harness-link-fix commit?

**Options:**

a) Yes: cut it on those two conditions, then reply with the tag in ki.ways-of-working's `messages.md`.

b) No: bring the finished change back to you before the tag.
