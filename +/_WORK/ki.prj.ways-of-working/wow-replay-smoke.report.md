# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-replay-smoke

**🤖 → 👤 Handoff to supervisor · Run report at 08:39 GMT**

---

## Done

- Dispatched the tap CI replay once with `formula=ki` under HARNESS-CONSUMER ("Add, keep poll") on tap `ef2ad37`, at 08:35 GMT. No file, setting or credential was changed, no release cut, nothing re-run, and no commit was made.
- Tap run: https://github.com/knowledgeislands/homebrew-tap/actions/runs/40177165661 · success. All four jobs passed: Detect formula changes, KI governance, Homebrew formula gates and Notify release consumers.
- Dispatch evidence: the Notify job selected `ki` v0.13.0 from tap commit `ef2ad37`, minted the release App token scoped to `apps-knowledgeislands.info` and `ki-agentic-harness`, and its dispatch step succeeded. The job's step summary text is not exposed through `gh` or the REST API, so "Dispatched ki v0.13.0 to knowledgeislands/ki-agentic-harness" was not read verbatim; the equivalent proof is the harness run below, which arrived four seconds after the dispatch step.
- Harness run: https://github.com/knowledgeislands/ki-agentic-harness/actions/runs/40177247914 · success. Workflow `update-ki-pin.yml`, event `repository_dispatch`, type `tool-release-published`, ran on harness `a122a201` and printed "pin v0.13.0 is current; nothing to propose". It opened no pull request and made no commit.
- Also observed, read-only: the website receiver's "Update tool release" run on the same dispatch succeeded (https://github.com/knowledgeislands/apps-knowledgeislands.info/actions/runs/40177247506), so the fan-out reached both listed consumers.

## In Progress

Nothing. The run is complete.

## Queries

### SUMMARY-VISIBLE - the dispatch summary is not machine-readable

**Context**: The brief asked to confirm the tap run's summary line naming the consumer and version. GitHub exposes a job's step summary only on the Actions web page; `gh run view` logs, the check-runs API and the jobs API all return it empty. This run proved delivery through the receiver's run instead.

**Query**: Should the Notify job also echo each "Dispatched <tool> <version> to <consumer>" line to the job log, so a future replay can be confirmed from `gh` alone?

**Options**:
a) (recommended, confidence high - a one-line change in the tap workflow, no behaviour change, makes step 6 of the guide verifiable without a browser) Echo the line to stdout as well as the step summary, as a small tap change with the guide's step 6 amended to point at the log line.
b) Leave as is and treat the receiver's run as the proof, amending the guide's wording to say so.
c) Do nothing.
