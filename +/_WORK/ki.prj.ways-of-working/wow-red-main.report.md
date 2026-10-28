# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-red-main

**🤖 → 👤 Handoff to supervisor · Run report at 08:56 GMT · blocked**

---

## Done

- **Harness main is green.** Run [40177741593](https://github.com/knowledgeislands/ki-agentic-harness/actions/runs/40177741593) on `5cb52973` passed: audit, tests and TypeScript all green.
- Harness `c9825bfc` `fix(skills): cite the principal design proposals by pinned URL`: the ki-coordination, ki-delegation and ki-work-package `references/sources.md` files linked two ki-principal design proposals by an absolute path on this machine, which KI-LINK-2 could not resolve on any other machine; this is what turned harness main red at 02:31 GMT (commit `1af72f2e`), not `fa9c6739` or `0404754a`. They now cite the tracked, public ki-principal files by GitHub URL pinned to each file's last commit. Local ki-skills audit FAIL=0.
- Harness `5cb52973` `chore(toolchain): adopt Bun 1.4.3` in `mise.toml` and `package.json`, clearing DEPS-1. Tests 1466 pass, `tsc` clean, ki-engineering audit PASS.
- Website `fa5b988` `fix(toolchain): keep Biome off Markdown`: this morning's Biome 2.6.3 bump switched on Markdown formatting, which rewrote every Docs page and failed BIO-1; Markdown is rumdl's under ki-authoring, so Biome's Markdown formatter and linter are disabled. `biome check` clean.
- Website `188f31f` `fix(boundaries): follow the dependency-cruiser bump into the checker root`: the same bump moved the root dependency-cruiser range to ^18.7.0 but not `tooling/depcruise`, so the boundaries suite failed and DESIGN-2 could not run its proof locally. Root `bun run test` now passes; this would have failed the CI `test` step once the audit passed.
- Website `13c7bea` `chore(toolchain): adopt Bun 1.4.3`, clearing DEPS-1.
- Website run [40177745190](https://github.com/knowledgeislands/apps-knowledgeislands.info/actions/runs/40177745190) on `13c7bea`: audit FAIL=1 (DESIGN-2 only, see Queries); the other two failures and the Biome findings are gone. Local full audit against the moving harness: FAIL=0.
- No open bot pull requests in either repository, so nothing to leave to auto-merge.
- Clean temporary clones were used throughout; the dirty primary harness checkout was not touched. Both pushes were fast-forward after a rebase of only this run's commits onto `origin/main`.

Notes: the brief's `Co-Authored-By` line named Claude Opus 5.5; the commits carry Claude Fable 5.1, the model that made them, under the standard's rule that the trailer names the committing model. Toolchain provisioning in the clones (`mise install` of Bun 1.4.3, `bun install`, and a `bun install` in `tooling/depcruise` to move its lockfile) was treated as the repositories' own build steps, not new software. `gh run` reads were used as the brief's Do section directs; the only writes were the two Git pushes.

## In Progress

Nothing. The website's remaining failure is blocked on the query below.

## Queries

### WEB-PIN - the website's DESIGN-2 failure is checker drift in the released ki, not a website defect

**Context** The website CI installs released `ki` v0.13.0, whose canonical harness pin is harness commit `52779419` of 2026-10-21. That harness names the isolated boundary checker root `tooling/boundaries`. The harness renamed it to `tooling/depcruise` on 2026-10-22 (`db5e3cff`) and the website followed on the same day (`31d02de`). Until this morning the website CI ran ki v0.8.4, which did not carry DESIGN-2; the 07:24 bump to v0.13.0 (`7132ba16`) surfaced the mismatch. The website's own AGENTS.md says a rule that disagrees with the local moving harness is checker drift owed to tools-ki as a pin bump, not a defect to work around in the website; the local moving harness passes the website with FAIL=0. Releasing is outside this run's authority, so the website main stays red on this one finding.

**Query** How should the pinned checker catch up with the website?

**Options**
a) (recommended, confidence high - fixes the drift at its source, keeps the website's CI model as AGENTS.md describes it, and tools-ki already has a release workflow) Bump `canonicalHarnessRelease` in tools-ki to the current green harness main `5cb52973`, release ki v0.14.0, then bump `KI_VERSION` in the website's `.github/workflows/ci.yml`. Two bounded runs: one in tools-ki with release authority, one in the website after the release.
b) (confidence medium - unblocks the website today but changes its CI model) Have the website CI check out the harness at a pinned commit and activate it with `ki dev local set` and `ki dev local on`, as the harness CI does for itself, and amend AGENTS.md to say CI audits the pinned harness rather than the tools-ki canonical pin.
c) (confidence low - reverts a deliberate rename and would fail the local moving harness) Move the website's checker root back to `tooling/boundaries`.
