# wow-review-release - blind review of two release-delivery questions

Read-only. Do not read anything under `+/_WORK/`. Use the repositories under `/Users/krisbrown/workspaces/knowledge-islands/` (homebrew-tap, ki-agentic-harness) and read-only `gh` calls. Change nothing.

1. The tap's `.github/tool-release-consumers.json` names only apps-knowledgeislands.info. The harness's `.github/workflows/update-ki-pin.yml` accepts a `tool-release-published` dispatch but nothing sends it, so its pin moves only on a daily poll that runs five to seven hours late and skipped v0.11.5. Options, unranked: add the harness to the consumer list, keeping the poll; leave the harness poll-only. Check the history for any sign poll-only was deliberate.
2. On 2026-10-20 the harness CI run for the v0.12.0 pin pull request ran its Test step for six hours before cancellation. Current `ci.yml` declares a 30-minute job and 10-minute step timeout. Options, unranked: treat it as a one-off and watch the next pin pull request; check when the timeouts were added and investigate if they predate the run.

Report, for each: your recommended option, confidence high, medium or low, and a one-paragraph reason with the evidence you read.
