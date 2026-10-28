# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-ci-pins

**🤖 → 👤 Handoff to supervisor · Run report at 08:28 GMT · last mark 01:07 GMT**

---

## Done

Current `tools-ki` release verified as v0.13.0 (latest tag and the GitHub "Latest" release). Twenty repositories pinned `ki`; `ki-agentic-harness` was already on v0.13.0 and `kw-website`, `packages-portal-commons` and `paperclip` have no `ki` pin. Every pin now reads v0.13.0 on `origin/main`, every primary checkout is level with its remote, and in every CI run the install step (install, `ki repo repair`, `ki diag`, harness check) passed on v0.13.0. The original `apps-knowledgeislands.info` failure, `ki repo repair` lacking `ki-diagrams`, is gone. Commits were made by this session, so the trailer names Claude Fable 5.1, per the commit-trailer rule, not the Opus 5.5 text in the brief.

- `apps-knowledgeislands.info` v0.8.4 → v0.13.0 · `7132ba1` · CI red: `ki repo audit` DEPS-1, DESIGN-2 (red on every prior run today).
- `apps-observatory.local` v0.11.3 → v0.13.0 · `4d6c9fb` · CI red: audit DEPS-1, DESIGN-2 (red since 21 Oct).
- `homebrew-tap` v0.11.3 → v0.13.0 · `6b0a79e` · CI green.
- `ki-specifications` v0.11.3 → v0.13.0 · `ec13839` · CI green.
- `ki-techne-harness` v0.11.3 → v0.13.0 · `3eb8a6b` · CI red: audit DEPS-1 (red since 20 Oct).
- `mcp-housekeeping-chatgpt` v0.11.3 → v0.13.0 · `1d703e2` · CI red: audit DEPS-1, DESIGN-2 (red since 19 Oct).
- `tools-ki` v0.12.0 → v0.13.0 · landed inside another session's `1e3c5500` `chore: bump libs` (see Queries) · CI red: audit DEPS-1, TEST-5 (red on the two prior runs).
- `tools-mgit` v0.11.3 → v0.13.0 · `746a6cc` · CI red: shellcheck SC2015 in `bin/mgit` lines 3286 and 3312 (red since 20 Oct).
- `tools-rig` v0.12.0 → v0.13.0 · `1d6060e` · CI green.
- `tools-techne` v0.11.3 → v0.13.0 · `3957100` · CI red: audit DEPS-1, DESIGN-2 (red since 22 Oct).
- `ki-design` v0.11.0 → v0.13.0 · `6c6f4a3` · CI red: audit BIO-1, BODY-11, DEPENDS-4, DEPS-1, DESIGN-2, FILENAME-0, FILENAME-1, FM-6, ROUTE-1 (red since 22 Oct).
- `ki-principal` v0.12.0 → v0.13.0 · `43b3b30e` · CI red: audit BODY-11, COORD-7, COORD-12, DEPENDS-4, DEPS-1, FOLDER-1, MD-mech, PRINCIPAL-5, RECORD-2, STRUCTURE-1 (red on every prior run today).
- `mcp-acquire-whatsapp` v0.11.3 → v0.13.0 · `292b322` · CI red: audit DEPS-1, DESIGN-2, TEST-5 (red since 19 Oct).
- `mcp-git-audit` v0.11.3 → v0.13.0 · `4d7126e` · CI red: audit DEPS-1, DESIGN-2 (red since 20 Oct).
- `mcp-gsuite` v0.11.3 → v0.13.0 · `3943b13` · CI red: audit DEPS-1, DESIGN-2 (red since 19 Oct).
- `mcp-housekeeping-claude` v0.11.3 → v0.13.0 · `14e0c14` · CI red: audit DEPS-1, DESIGN-2 (red since 19 Oct).
- `mcp-ki-kb-fs` v0.11.3 → v0.13.0 · `7d9c999` · CI red: audit DEPS-1, DESIGN-2, TEST-5 (red since 19 Oct).
- `mcp-ki-kb-notion-mirror` v0.11.3 → v0.13.0 · `445d9e6` · CI red: audit DEPS-1, DESIGN-2 (red since 19 Oct).
- `mcp-m365` v0.11.3 → v0.13.0 · `65fe01b` · CI red: audit DEPS-1, DESIGN-2 (red since 20 Oct).
- `tools-git-almanac` v0.11.3 → v0.13.0 · `e9b9735` · CI red: audit DEPS-1, DESIGN-2, TEST-5 (red since 19 Oct).

Local gates: each repository's `ki repo audit` ran after the edit and the pre-commit and commit-msg hooks ran on each commit; no failure named the pin file, and every local failure matches the CI failure above. The `tools-ki` local audit's `test:coverage` ran past 20 minutes twice and was stopped; CI ran that suite instead. The TEST-5 failures (`mcp-acquire-whatsapp`, `mcp-ki-kb-fs`, `tools-git-almanac`) are each a boundaries test expecting `dependency-cruiser` `^18.7.0` where the repository declares `^18.6.0`; the DESIGN-2 failures want the root `prepare` script to install the boundary toolchain. Both are dependency and engineering drift, not the pin, and not a mechanical consequence of the new `ki` within the CI file, so they are left as queries. `tools-mgit`'s shellcheck finding is likewise outside the CI file.

## In Progress

Nothing is running.

## Queries

### Q1 - tools-ki pin landed inside another session's commit

**Context**: while this run's local audit of `tools-ki` was running on the edited checkout, another session committed and pushed `1e3c5500` `chore: bump libs`, which swept the one-line pin edit into its commit alongside `package.json` and `bun.lock`. The pin is correct on `origin/main` and CI's install step passed on it, but there is no pin-only Conventional Commit for `tools-ki`, and the commit carries neither this run's message nor its trailer.

**Query**: accept the pin as landed in `1e3c5500`, or have the pin re-landed as its own commit?

**Options**:
a) (recommended, confidence high - the pin is correct on main and verified by CI; re-landing would be a no-op diff and Git history already shows the change) accept it as landed and note it in the decisions log.
b) revert the pin line in a follow-up and re-commit it as `chore(ci): install ki v0.13.0`, which produces two more commits for no change in state.

### Q2 - the repositories stay red on audit rules outside this unit

**Context**: 16 of 20 runs are red after the pin move, and every one was red before it. The install step passed everywhere; the failures are DEPS-1 (bun 1.4.2 → 1.4.3 and, in places, `@types/node` and `rumdl`, all 15 days past the window), DESIGN-2 (the `prepare` script must install `tooling/depcruise` or `tooling/boundaries`), TEST-5 (`dependency-cruiser` `^18.6.0` versus `^18.7.0` in three repositories), the `ki-design` and `ki-principal` document-structure rules, and shellcheck in `tools-mgit`. DEPS-1 is the separate unit the brief names; DESIGN-2 and TEST-5 look like one harness rule change that the dependency work would also clear.

**Query**: how should the remaining red be routed?

**Options**:
a) (recommended, confidence high - DEPS-1, DESIGN-2 and TEST-5 are all dependency-and-toolchain drift and one unit can clear them together across the 15 affected repositories) fold DESIGN-2 and TEST-5 into the DEPS-1 unit, and open separate records for the `ki-design` and `ki-principal` document rules and the `tools-mgit` shellcheck finding.
b) open one record per rule per repository.
c) leave the red as is until the harness rule set settles.

### 🤖 → 👤 Handoff to supervisor · since 08:28 GMT

🤖 0 running · 👤 2 with you · ⛔ 0 blocked · 📥 0 to accept

- [with you] Q1 tools-ki pin landed in another session's commit · Kris · since 08:28 GMT
- [with you] Q2 routing of the remaining CI red (DEPS-1, DESIGN-2, TEST-5, document rules, shellcheck) · Kris · since 08:28 GMT

🧵 Coordination thread · Ways of working (ki.ways-of-working)
