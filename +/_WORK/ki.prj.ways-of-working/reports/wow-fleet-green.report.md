# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-fleet-green

**🤖 → 👤 Handoff to supervisor · Run report at 10:51 GMT · last mark 10:51 GMT**

---

## Done

Each repository was fixed in a clean clone of `origin/main`, tested and audited locally, committed by explicit path and pushed fast-forward. "CI red: DESIGN-2 only" means the one remaining failure is the released `ki` v0.13.0 checking for `tooling/boundaries` where the repository has `tooling/depcruise`; that clears fleet-wide when wow-ki-pin-release ships ki v0.14.0 and the pin bumps, so it was left alone as wow-red-main did.

- tools-mgit: `334e9b2` groups the two SC2015 branch guards in `bin/mgit`. CI green.
- ki-techne-harness: `00ef1d2` Bun 1.4.3; `3826fa5` Biome 2.6.3 schema with Markdown and YAML left to rumdl and infra; `1deddca` groups two more SC2015 guards in the agent-host scripts that CI's shellcheck caught. CI green.
- mcp-ki-kb-fs: `e201038` Bun 1.4.3; `6cddbcb` checker root to dependency-cruiser ^18.7.0 (TEST-5). CI red: DESIGN-2 only.
- mcp-acquire-whatsapp: `e115148` Bun 1.4.3; `f7455a4` checker root ^18.7.0 (TEST-5). CI red: DESIGN-2 only.
- tools-git-almanac: `0bcc68f` Bun 1.4.3; `36f61ff` checker root ^18.7.0 (TEST-5). CI red: DESIGN-2 only.
- apps-observatory.local: `f365917` Bun 1.4.3; `5e103a3` checker root ^18.7.0 (TEST-5). CI red: DESIGN-2 only.
- mcp-gsuite: `1148ac6` Bun 1.4.3. CI red: DESIGN-2 only.
- mcp-m365: `655ac04` Bun 1.4.3. CI red: DESIGN-2 only.
- mcp-housekeeping-claude: `bb13cd8` Bun 1.4.3. CI red: DESIGN-2 only.
- mcp-housekeeping-chatgpt: `a9734ae` Bun 1.4.3. CI red: DESIGN-2 only.
- mcp-ki-kb-notion-mirror: `7c8b81d` Bun 1.4.3. CI red: DESIGN-2 only.
- mcp-git-audit: `ac5a4ae` Bun 1.4.3. CI red: DESIGN-2 only.
- tools-techne: `3d0c10b` Bun 1.4.3 in the pins and in the hard-coded exact-version checks in `install.sh`, the doctor command, its tests and the installing guide. CI red: DESIGN-2 only.
- ki-design: `8a1d4a1` Bun 1.4.3; `8d0cdfe` checker root ^18.7.0 (TEST-5); `ccd6bfd` Biome 2.6.3 schemas with Markdown left to rumdl (BIO-1). CI red: DESIGN-2 plus the document rules listed below.
- ki-principal: `eb9c2869` Bun 1.4.3. CI red: document and work-record rules only, listed below.
- tools-ki: `11663563` Bun 1.4.3, pulled with rebase onto the other session's main before the push; the full suite passed locally (97 files, 2150 tests). CI red: TEST-5 only, the agent-compatibility footer snapshots under FG-1, which pre-date this run; DEPS-1 cleared. Its local `ki repo audit` was left to CI after the coverage suite passed the 20-minute limit twice.
- `bun outdated` listed nothing stale in any repository, so DEPS-1 was the Bun runtime pin alone; no `@types/node` or `rumdl` bump was needed.
- Document-rule failures left alone, as instructed: ki-design FILENAME-0, FILENAME-1, FM-6, BODY-11, DEPENDS-4, ROUTE-1, MERGE-1; ki-principal COORD-7, COORD-12, RECORD-2, FOLDER-1, DEPENDS-4, BODY-11, STRUCTURE-1, PRINCIPAL-5, MD-mech. ki-design's local audit also fails GitHub-settings rules (GH-3, TOGGLE-1, TOPICS-1, DEP-1, SEC-1), which this run may not change.
- `ki repo repair` cannot act on an unregistered clone, so every fix was a hand edit; `ki repo audit` ran in each clone.

## In Progress

Nothing. Every repository in scope is pushed and its CI has reported.

## Queries

### FG-1 - tools-ki main stays red on a snapshot mismatch that is not drift

**Context** tools-ki's CI fails TEST-5 because `test:coverage` fails two snapshot tests in `src/tests/cli/agent-compatibility.test.ts` ("baseline role-free footer none" and "baseline role-free footer push"). The same suite passes in full in a clean clone of `origin/main` on this machine (97 files, 2150 tests), so the mismatch is specific to the CI environment, not to the Bun or dependency drift this run was asked to clear. The footer under test is another session's feature work, and this run's only tools-ki change is the Bun 1.4.3 pin, which clears DEPS-1. The brief named tools-ki for DEPS-1 only.

**Query** Who takes the agent-compatibility snapshot mismatch on tools-ki's CI?

**Options** a) (recommended, confidence high - the test and the footer it snapshots belong to the session already working in tools-ki, and a passing local run says the snapshot encodes something environment-dependent that its author should see) Route it to the tools-ki session as a note: make the footer snapshot environment-independent or regenerate it, then CI's TEST-5 clears. b) (confidence medium - quick, but risks baking a CI-only rendering into the snapshot without understanding why it differs) A bounded run regenerates the snapshot from CI output and commits it. c) (confidence low - leaves tools-ki red and blocks the release that wow-ki-pin-release needs green CI for) Leave it until the feature work lands.

### FG-2 - DESIGN-2 stays red fleet-wide until the released ki catches up

**Context** Twelve repositories in this run end with exactly one CI failure, DESIGN-2, because released `ki` v0.13.0 pins a harness that names the checker root `tooling/boundaries` while the repositories moved to `tooling/depcruise`. wow-red-main raised this as WEB-PIN and its recommended option, a canonical-pin bump and ki v0.14.0, is queued as wow-ki-pin-release, held until this run finished. Every local audit against the moving harness passes DESIGN-2. This needs no new decision; it is listed so the red is read as expected.

**Query** None beyond confirming that wow-ki-pin-release may now start.

**Options** a) (recommended, confidence high - the held run exists for exactly this and nothing in this run changed its premise) Release wow-ki-pin-release now; after ki v0.14.0 and the `.github/ki-version` or `KI_VERSION` bumps, the twelve DESIGN-2 reds clear with no further change. b) (confidence low - reverts a deliberate rename) Move the checker roots back to `tooling/boundaries`.

### 🤖 → 👤 Handoff to supervisor · since 10:51 GMT

🤖 0 running · 👤 2 with you · ⛔ 0 blocked · 📥 0 to accept

- [with you] FG-1 tools-ki agent-compatibility snapshot mismatch on CI · Kris · since 10:51 GMT
- [with you] FG-2 release wow-ki-pin-release to clear the fleet's DESIGN-2 reds · Kris · since 10:51 GMT

🧵 Coordination thread · Ways of working (ki.ways-of-working)
