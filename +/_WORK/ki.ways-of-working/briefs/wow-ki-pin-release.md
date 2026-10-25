# wow-ki-pin-release - catch released ki up with the harness so the website goes green

## Goal

Under Kris's RED-MAIN answer on 2026-10-25 ("Fix mains first") and AWAY-GRANT-2, which allows cutting a release under the repository's release process: the website CI installs released ki v0.13.0, whose canonical harness pin `52779419` names the boundary checker root `tooling/boundaries`; the harness and the website renamed it `tooling/depcruise` on 2026-10-22, so the website's DESIGN-2 fails. The website's AGENTS.md calls this checker drift owed to tools-ki as a pin bump.

## Do

1. In a clean temporary clone of `tools-ki` from `origin/main` (pull with rebase first; wow-fleet-green has just worked there), bump the canonical harness pin to the newest harness `main` commit whose CI is green (at least `5cb52973`). Run tools-ki's tests and audits; commit by explicit path, push fast-forward only, and watch main's CI go green.
2. Cut ki v0.14.0 under tools-ki's documented release process, and watch the release fan-out: release bot, homebrew-tap formula, tap CI and its notify job.
3. In a clean temporary clone of `apps-knowledgeislands.info`, bump `KI_VERSION` in the CI workflow to v0.14.0 unless the tap's release notification has already opened or merged that change; run its tests and audits, commit, push fast-forward only, and watch main's CI.
4. Stop and report a query if the pin bump breaks tools-ki's tests, the release process needs a credential or setting change, or the website still fails for a reason other than this drift.

## Rules

Push tier. Fast-forward only, never force or `--no-verify`. No DNS, Cloudflare Access, routes, Zero Trust, credentials or GitHub settings. No messaging to people. Commit trailers follow the standard's commit-trailer rule. Never use the dirty primary checkouts; leave scratch removal to `ki agent close`.

## Report

Owner report: Done (each commit, the release, each CI run with its link and result), In Progress, Queries.
