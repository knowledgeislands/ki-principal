# mgitrel - KI-TOOL-MGIT-CLI-023 acceptance and the mgit release

Repository: /Users/krisbrown/workspaces/knowledge-islands/tools-mgit. Starts after the burndown run. Work package: /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown.

Kris ran the hands-on check of [KI-TOOL-MGIT-CLI-023](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-023-hands-on-behaviour-check.md) and it passed (19 October, MGIT-RELEASE a) in ki.ways-of-working decisions). The record still reads `draft`.

1. Record Kris's passed check as the record's evidence and bring it to Awaiting review under `ki-implement`'s rules; do not set it to done, because Kris accepts under `ki-accept` (MGIT-GO).
2. Prepare one mgit release as a local commit: version bump, changelog covering everything since the last tag, with KI-TOOL-MGIT-CLI-023 and [KI-TOOL-MGIT-CLI-028](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-028-learn-majority-output.md). Verify with the repository gate and the release dry run if one exists.
3. Report the exact tag, the steps to cut, push and publish it, and the CONSUMER-MIGRATE step that follows (chezmoi `dot_mgit.toml` source and the live manifest together, ki.chezmoi's).

Work under ki-delegation and ki-git: commit your own changes by explicit path, never push, tag, publish or delete a remote branch, never use --no-verify. Write your report to /Users/krisbrown/.local/state/ki/agents/tools-burndown/mgitrel.report.md in the ki-coordination owner-report shape (Done, In Progress, Queries with Context, Query and lettered Options, a) recommended with confidence). Raise a blocking query in the report and stop rather than guess.
