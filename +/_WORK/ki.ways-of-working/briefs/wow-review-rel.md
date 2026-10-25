# wow-review-rel - independent review of two release decisions

You are an independent reviewer. Read only the tools-ki repository at /Users/krisbrown/workspaces/knowledge-islands/tools-ki (read-only: `git fetch` and reading files and GitHub Actions logs with `gh` are fine; make no commits, pushes, tags, workflow dispatches or edits anywhere). Do not read anything under `+/_WORK/` in any repository, nor any decisions log or run report. For each question below, say which option you would choose, your confidence (high, medium or low) and a reason of one to three sentences grounded in what you checked. If none fits, say what you would do instead.

## Question 1 - how should a failed release proceed?

Context: tools-ki's Release workflow runs `bun run test` on each packaging runner before packaging. For tag `v0.14.0` (commit `09316eb5`), Release run 40192625875 passed on linux-x64, but on both macOS runners the vitest worker for `src/tests/cli/agent-control.test.ts` (about 5284 lines, 544 tests, changed after v0.13.0) died with "Reached heap limit ... JavaScript heap out of memory" after 2111 of 2150 tests had passed; the jobs ran 38 and 50 minutes against about 2 for v0.13.0. The same file passes locally on macOS in 153 s. Nothing was published. The `v0.14.0` tag is on origin and published tags are never moved, so any fix means a new version. Twelve downstream repositories stay red on one audit rule until a release ships.

Options, unranked:

- Fix the test footprint on main (split the file or free fixtures between groups) and also set a `NODE_OPTIONS=--max-old-space-size` ceiling on the package job's test step; release v0.14.1.
- Only raise the heap ceiling in `release.yml` for the package test step; release v0.14.1.
- Run the test suite on Linux only and let macOS jobs package without testing; release v0.14.1.
- Leave the release unpublished for now.

## Question 2 - fold a related change into that release work?

Context: tools-ki's own CI installs released ki v0.13.0 and audits itself. Its dependency-checker root is still `tooling/boundaries` (and `ci.yml` installs it there), while the current harness expects `tooling/depcruise`. Nothing fails today, but once tools-ki bumps its own `KI_VERSION` to a release carrying the new harness pin, that audit rule fails.

Options, unranked:

- Fold the rename and tools-ki's own `KI_VERSION` bump into the v0.14.1 release work.
- Capture it as a separate tools-ki work record and leave tools-ki on v0.13.0 for now.

## Report

Write a short report: for each question, your choice, confidence and reason, and anything you found that changes the picture.
