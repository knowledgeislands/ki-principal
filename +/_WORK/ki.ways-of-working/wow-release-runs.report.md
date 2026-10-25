# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-release-runs

**🤖 → 👤 Handoff to supervisor · Run report at 08:11 GMT · last mark 01:07 GMT**

---

## Done

No commits: read-only GitHub metadata and job-log reads only, nothing triggered, re-run, cancelled or changed.

Short answer: tools-ki → tap → tap CI → website receiver succeeded at every hop for all three releases, and every tap intake came from the dispatch, not the poll. The quiet failures are downstream of the receivers: the website's bot pull requests could not auto-merge because the website's required `build` check has failed on every commit to main since 2026-10-19, and the harness never receives a dispatch at all, so its pin moves only on the daily poll, which also skipped v0.11.5 and timed out on v0.12.0. Only v0.13.0 reached both consumers' main, the website by Kris's manual merge on 2026-10-24 and the harness by the poll.

v0.11.5 (released 2026-10-19 20:41 UTC)

- tools-ki Release, Notify Homebrew tap: succeeded · <https://github.com/knowledgeislands/tools-ki/actions/runs/39320969455>
- Tap intake: from the dispatch (repository_dispatch at 20:41:52), opened and auto-merged PR #49 to `45393a2` · <https://github.com/knowledgeislands/homebrew-tap/actions/runs/39321467960>
- Tap CI, Notify release consumers: succeeded, dispatched to the website · <https://github.com/knowledgeislands/homebrew-tap/actions/runs/39321763412>
- Website receiver: succeeded, opened PR #48 with auto-merge, but the required `build` check failed so it never merged; Kris closed it on 2026-10-24 as superseded by v0.13.0 · <https://github.com/knowledgeislands/apps-knowledgeislands.info/actions/runs/39322008636>
- Harness update-ki-pin: skipped. No dispatch reaches the harness, and the next daily poll (2026-10-20 12:07 UTC) found v0.12.0 already latest, so v0.11.5 was never proposed · <https://github.com/knowledgeislands/ki-agentic-harness/actions/runs/39419889890>

v0.12.0 (released 2026-10-19 23:49 UTC)

- tools-ki Release, Notify Homebrew tap: succeeded · <https://github.com/knowledgeislands/tools-ki/actions/runs/39343624861>
- Tap intake: from the dispatch (23:49:13), opened and auto-merged PR #50 to `a0aec08` · <https://github.com/knowledgeislands/homebrew-tap/actions/runs/39343900911>
- Tap CI, Notify release consumers: succeeded · <https://github.com/knowledgeislands/homebrew-tap/actions/runs/39344116042>
- Website receiver: succeeded, opened PR #49 with auto-merge; `build` failed, never merged; Kris closed it on 2026-10-24 as superseded · <https://github.com/knowledgeislands/apps-knowledgeislands.info/actions/runs/39344318345>
- Harness update-ki-pin: recovered by poll, then failed to land. The 2026-10-20 12:07 UTC schedule run opened PR #33 with auto-merge; its `build` check was cancelled after the Test step ran for six hours, so it never merged; Kris closed it on 2026-10-24 as superseded · <https://github.com/knowledgeislands/ki-agentic-harness/actions/runs/39419889890> · check run <https://github.com/knowledgeislands/ki-agentic-harness/actions/runs/39419916984>

v0.13.0 (released 2026-10-22 01:23 UTC)

- tools-ki Release, Notify Homebrew tap: succeeded · <https://github.com/knowledgeislands/tools-ki/actions/runs/39705072920>
- Tap intake: from the dispatch (01:23:12), opened and auto-merged PR #51 to `f31b194` · <https://github.com/knowledgeislands/homebrew-tap/actions/runs/39705370956>
- Tap CI, Notify release consumers: succeeded · <https://github.com/knowledgeislands/homebrew-tap/actions/runs/39705504069>
- Website receiver: succeeded, opened PR #50 with auto-merge; `build` failed, so Kris merged it by hand on 2026-10-24 18:50 UTC as `4037b87`, together with the stale mgit v0.18.0 and rig v0.7.0 bot PRs · <https://github.com/knowledgeislands/apps-knowledgeislands.info/actions/runs/39705616072>
- Harness update-ki-pin: recovered by poll. The 2026-10-22 12:22 UTC schedule run opened PR #34, `build` passed and the bot auto-merged it as `fcc0f38` at 12:27 · <https://github.com/knowledgeislands/ki-agentic-harness/actions/runs/39777745320>

Cross-cutting observations

- The tap's own daily polls after each release (2026-10-20 and 2026-10-22) reported every formula already current, confirming the dispatch did the work each time · <https://github.com/knowledgeislands/homebrew-tap/actions/runs/39417058711> · <https://github.com/knowledgeislands/homebrew-tap/actions/runs/39774592454>
- The tap's consumer list, `.github/tool-release-consumers.json`, names only the website. The harness's update-ki-pin workflow accepts the same `tool-release-published` dispatch but nothing sends it, so every harness run on record is a schedule run.
- Both daily backstops fire well after their cron time: the tap's 06:17 UTC poll ran between 11:44 and 11:58 UTC, and the harness's 06:41 UTC poll between 11:35 and 13:54 UTC, so poll-only delivery lags a release by up to a day plus five to seven hours.
- The website's main CI has failed on every commit since 2026-10-19 10:27 UTC, and the harness's main CI is also failing as of 2026-10-25 08:07 UTC, both in the KI repo audit step. While a required check is red on main, no bot pull request in either repository can auto-merge, so the fan-out's last hop depends on manual merges.

## In Progress

Nothing. Run complete.

## Queries

### Q1 - Red `build` on main blocks every bot pull request in the website and the harness

**Context** The website's required `build` check has failed on every main commit since 2026-10-19 (KI repo audit: at first "projection is missing" for every claude-code and chatgpt-codex skill plus ki-work-roadmap failures, now down to one failing check with three findings as of 2026-10-25 07:55 UTC). The harness's main audit is also failing as of 2026-10-25 08:07 UTC. Bot pull requests #48, #49 and #50 on the website and #32 and #33 on the harness all opened with auto-merge armed and never merged.

**Query** How should bot pull requests land while main's required check is red?

**Options** a) (recommended, confidence high - auto-merge is the designed delivery path and only works on a green main) Get both repositories' main audit green first, then let the next release prove the fan-out end to end with no manual merge. b) Keep the current practice of merging stale bot pull requests by hand every few days, accepting the catalogue and pin lag. c) Remove `build` from the required checks for the bot's automation branches so they merge regardless; this hides real breakage and is not recommended.

### Q2 - The harness is not enrolled as a tap consumer, so its pin only moves by poll

**Context** The tap's consumer list names only the website. The harness's update-ki-pin workflow already filters for a `tool-release-published` dispatch whose `source_repository` is tools-ki, and the tap's dispatch payload carries that field, so enrolment looks like a one-line change to the consumer list. The daily poll skipped v0.11.5 entirely and lagged v0.12.0 and v0.13.0 by about twelve hours.

**Query** Should the harness be enrolled in the tap's consumer list so releases reach it by dispatch?

**Options** a) (recommended, confidence medium - the workflow is dispatch-ready and the poll demonstrably skips intermediate releases; medium only because the design may have left the harness poll-only on purpose) Add `knowledgeislands/ki-agentic-harness` to the tap's consumer list and keep the schedule as the backstop. b) Leave the harness poll-only as designed and accept that only the latest release at poll time is pinned.

### Q3 - Harness pull request #33's `build` ran for six hours before cancellation

**Context** The harness CI run for the v0.12.0 pin pull request had its Test step start at 2026-10-20 12:07 UTC and get cancelled at 18:08 UTC. Current main declares a 30-minute job timeout and a 10-minute Test step timeout, so either those limits were added after 2026-10-20 or they did not take effect on that run.

**Query** Is this hang worth chasing, or treat it as a one-off now that timeouts are declared?

**Options** a) (recommended, confidence medium - a single occurrence, timeouts now declared, and the v0.13.0 run on the same workflow completed in minutes) Treat it as a one-off and watch the next pin pull request's Test step. b) Check the ci.yml history to confirm when the timeouts were added, and if they predate 2026-10-20 investigate why the step limit did not fire.

🧵 Coordination thread · Ways of working (ki.ways-of-working)
