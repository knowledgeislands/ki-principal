# pin - harness pin for ki v0.11.5

Repository: /Users/krisbrown/workspaces/knowledge-islands/tools-ki. The cli155 run prepared `v0.11.5` locally (`chore(release): prepare v0.11.5`) and reported the pin as the remaining step; read /Users/krisbrown/.local/state/ki/agents/tools-burndown/cli155.report.md, In Progress.

Authority for this run, under Kris's KI-PATCH-RELEASE ("can you sort that please", 19 October): exactly one read-only network fetch, `https://codeload.github.com/knowledgeislands/ki-agentic-harness/tar.gz/bda6e4a0d91e2e7c2feda8d04d5d09e6c1059c61`, to compute its sha256. No other network call.

1. Confirm ki-agentic-harness `bda6e4a0` contains `ec30caaf` and provides `ki-work-package`.
2. Commit `fix(bootstrap): pin the harness carrying ki-work-package`: the codeload URL and sha256 in `src/core/storage/registry.ts`, the matching digest in `src/tests/cli/bootstrap/bootstrap.test.ts`, and the Harness pin paragraph in `CHANGELOG.md`.
3. The wpreader run is writing in this tree at the same time. Stage only your own paths. If `CHANGELOG.md` already carries another run's uncommitted change, leave it alone, commit the other two files, and report the paragraph text for a later commit.
4. Rerun the gate (full suite with coverage, tsc, Biome, man-page lint, `ki repo audit`) and report the exact commit to tag `v0.11.5` on.

Work under ki-delegation and ki-git: commit your own changes by explicit path, never push, tag, publish or delete a remote branch, never use --no-verify. Write your report to /Users/krisbrown/.local/state/ki/agents/tools-burndown/pin.report.md in the ki-coordination owner-report shape (Done, In Progress, Queries with Context, Query and lettered Options, a) recommended with confidence). Raise a blocking query in the report and stop rather than guess.
