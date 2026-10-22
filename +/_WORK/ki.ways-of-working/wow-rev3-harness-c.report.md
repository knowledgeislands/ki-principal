# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev3-harness-c

**🤖 → 👤 Handoff to supervisor · Run report at 08:58 BST · last mark 08:24 BST**

---

## Done

VERDICT KI-HARNESS-GOV-189: ACCEPT · PRUNE: NO · confidence high · the narrowed scope (repository level check and `[behind]` banner item) is delivered and durably homed in the coordination standard; live links from tools-ki, two ki-principal design notes and chezmoi would break on prune. VERDICT KI-HARNESS-OPS-010: ACCEPT · PRUNE: NO · confidence high · receiver-local triage with its four dispositions is in `standards-acquisition.md`, `standards-acquired-triage.md`, ACQUIRE-5 and the rubric; the record is still `awaiting-review`, so it must be committed `done` before any prune commit, and only report links survive. VERDICT KI-HARNESS-OPS-011: ACCEPT · PRUNE: NO · confidence high · agent-session acquisition has its own standard linked from `ki-acquire/SKILL.md` and the adapter decision is in ADR-KI-HARNESS-SKILLS-007; same done-before-prune sequencing as OPS-010, and only report links survive. VERDICT KI-HARNESS-GOV-209: ACCEPT · PRUNE: NO · confidence high · already `done` (accepted 21 October); two live ki-principal work-package links and the GOV209-ROLLOUT message line still point at the record and must be repointed to the principal standard before a prune. VERDICT NO-GATE: REFUSE · PRUNE: NO · confidence medium · both hook variants now run a staged, check-only, fully offline `ki-repo` audit, verified by real-CLI interception, but the new offline path passes the directory basename as the repository identity, so FILES-2 fails spuriously whenever `.ki.toml` is staged in a hosted repository.

Findings, in verdict order.

- **Baseline and tree.** Review ran on `main` at `0809ff80`, clean tree, no remote call, no write outside this report and the status file. Fix commit `d9c4a6e2` was read in full (12 files).
- **Verification on HEAD, all offline.** `bun run test` passes (1431 tests, 183 files). `bunx tsc --noEmit` passes. Focused `ki repo audit --skill ki-work-roadmap` and `--skill ki-repo-project` pass. Rubric publication is in sync for ki-coordination, ki-acquire and ki-repo-kb-principal. Both hook assets under `skills/repo-structure/ki-repo-project/assets/githooks/` are byte-equal to the composer output (HOOK-4 holds).
- **[KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md).** Status `awaiting-review`, baseline `db5e3cff`, narrowed on 22 October under GOV189-SCOPE a) to the repository level check and the `[behind]` banner item; all three Steps ticked; Done-when and Review met against `ki-coordination/references/standards-coordination.md` (repository level check, `[behind]` item, 18 October approval) and `output-styles/ki-coordinator.md`. Deferred host-move questions are homed in `ki-coordination/references/sources.md#deferred-host-move-evidence`. Minor: the record's Context link to the Mac Studio setup note uses a nested path, but the note lives flat at `ki-principal/Streams/Projects/mac-studio-setup.md`; an outbound stale link, harmless to acceptance.
- **GOV-189 inbound references a prune would break.** Live, non-report: `tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md:43`, which still says GOV-189 "owns moving a thread between hosts", a claim the narrowing made stale; `ki-principal/+/_WORK/ki.ways-of-working/design/unparked-queries.md:54`; `ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sweep.md:111`. Reports under `ki-principal/+/_WORK/ki.ways-of-working/`: wow-rev-harness-a (11, 19), wow-rev-harness-b (13, 50), wow-rev-harness-c (11), wow-rev2-harness-a (25), records-fold (14), roadmap-sweep.report (124), wow-burn-plan (27), lane-triage (58), sweep-queries (105), harness-burn (29, 91), unpark-review (65), harness-queries (12), wow-fix-harness (9, 13, 25), wow-burn-harness (9), harness-moves (9), sweep-review (65). Outside the workspace root but noted: chezmoi `docs/roadmap/KB-DOTFILES-UE-096-thread-identity-hook-registration.md:32`. No knowledge lacks a durable home.
- **[KI-HARNESS-OPS-010](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-010-receiver-local-acquisition-triage.md).** Status `awaiting-review`, baseline `ed49d2f2`, Steps ticked; Done-when met: `ki-repo-kb/SKILL.md` and `references/standards-acquired-triage.md`, `ki-acquire/references/standards-acquisition.md` receiver-local triage with four dispositions, ACQUIRE-5 [J] in `scripts/rubric/items/acquisition.ts` and the generated `rubric.md`. KI-HARNESS-OPS-009 now cites these standards rather than the OPS-010 record.
- **OPS-010 inbound references.** Reports only, all under `ki-principal/+/_WORK/ki.ways-of-working/`: wow-rev-harness-a (22, 31), wow-rev-harness-b (14, 62), wow-rev-harness-c (12), wow-rev2-harness-a (27), wow-burn-plan (32), wow-signoff-ops009 (10), wow-burn-harness (10), wow-fix-harness (10, 15, 25). No knowledge lacks a durable home.
- **[KI-HARNESS-OPS-011](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-011-separate-agent-session-acquisition.md).** Status `awaiting-review`, baseline `d2e2a896`, Steps ticked; Done-when met: `references/standards-agent-session-acquisition.md` linked from `ki-acquire/SKILL.md:20`, housekeeping SKILL.md's updated, adapter decision at ADR-KI-HARNESS-SKILLS-007 line 32, `skills/README.md` catalogue current.
- **OPS-011 inbound references.** Reports only, same folder: wow-rev-harness-a (33), wow-rev-harness-b (15), wow-rev-harness-c (13), wow-rev2-harness-a (29), wow-burn-plan (33), wow-signoff-ops009 (10), wow-burn-harness (11), wow-fix-harness (11, 15, 25). No knowledge lacks a durable home.
- **[KI-HARNESS-GOV-209](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md).** Already `done`, accepted 21 October by wow-day-gov-209-accept, baseline `f59c0069`. Durable homes present: principal `assets/templates/acquired/README.md`, PRINCIPAL-5, `standards-principal.md#acquired-packet-scaffold`; `ki-repo-kb-principal/references/sources.md` now points at the standard and the pinned commit rather than the record.
- **GOV-209 inbound references a prune would break.** Live, non-report: `ki-principal/+/_WORK/ki.knowledge-acquisition/decisions.md:10` and `ki-principal/+/_WORK/ki/messages.md:54` (the GOV209-ROLLOUT line, which itself says the record is pruned once the durable home is cited). Reports under `ki.ways-of-working`: wow-rev-harness-a (43, 52), wow-day-gov-209-accept (9, 37), wow-burn-plan (18), wow-rev-harness-c (14), wow-burn-harness (13), wow-fix-harness (12, 25), wow-day-gov-209 (9, 17, 21, 35), harness-queries (10), wow-rev-harness-b (16), wow-rev2-harness-a (31), wow-day-prune-review-1 (17), -2 (10), -3 (10), harness-burn (18, 29, 65). Outside the workspace root but noted: `personal/acquire/+/_WORK/kb.regular.acquire-intake/` briefs/ka-finish.md (10), ka-close.report.md (14), ka-finish.report.md (11), prune-007.report.md (13, 27). Bare identifier mentions in `ki.ways-of-working/state.md:17`, `decisions.md`, the three wow-rev3 briefs and `thread-tidy.report.md`, and the fixture string in `ki-coordination/scripts/rubric/contexts/coordination.test.ts:269–272`, are not links and would not break.
- **NO-GATE, offline contract.** Both `package` and `no-package` variants run `KI_REPO_OFFLINE=1 ki repo audit --repo "$root" --staged --concise --progress never --reporter-levels FAIL "$@"` and then the full retry under the same variable. In a temp fixture with a hosted origin and a staged `.ki.toml`, with logging fakes for `gh`, `curl`, `wget` and `ssh` first on PATH, neither the quiet attempt nor the full retry made any provider call. The positive control without the variable called `gh auth status` and `gh repo view fixture/hosted`. `tools-ki` loads the rubric in-process with `environment: process.env`, so the variable reaches the collector. The fix's `canonical-project-gate.test.ts` exercises this through the shell launcher, both variants, with and without LICENSE.
- **NO-GATE, defect.** In `ki-repo/scripts/rubric/contexts/audit.ts` the branch `if (offline || !t.nameWithOwner)` calls `auditLocalContent(t.label, …)`, and `t.label` is the directory basename. FILES-2 then demands that `.ki.toml` equal "the canonical GitHub home for <basename>". On the harness checkout, `KI_REPO_OFFLINE=1 ki repo audit --repo . --skill ki-repo` reports FAIL=1 on FILES-2 ("… for ki-agentic-harness"), whereas without the variable it reports FAIL=0 WARN=1 (the existing MATURITY-1 warning). In the fixture the offline message reads "… for repo" while the unauthenticated path uses `t.nameWithOwner` and reports only the README H1 mismatch. The staged verdict scope narrows failing findings by subject path, so this bites exactly when `.ki.toml` is staged in any hosted Project repository: the hook blocks a correct declaration and the only way past is the forbidden `--no-verify`. The fix's tests run only FILES-1, which is why they did not catch it. The fixture also showed environmental RUNTIMES-2 failures in both modes, not attributable to the fix.
- **Prior refusal (wow-rev2-harness-a) items.** Its grounds, an online `gh` call in the hook and record-level citations in the sources files, are both resolved by `d9c4a6e2`.

## In Progress

Nothing is running.

Outstanding - no action requested now

- Prune sequencing for OPS-010 and OPS-011: commit each `done` first, then a dedicated prune-only commit after the reference preflight, under `ki-accept` §4.
- GOV-189's outbound Mac Studio setup link and tools-ki CLI-145's stale ownership sentence are candidates for a one-line tidy in their own repositories; neither affects acceptance.

## Queries

### NOGATE-FILES2 - offline audit identity

**Context:** The fix delivers the offline, staged, check-only gate the criterion asked for, and the interception evidence shows no provider call in either variant. But the offline branch in `audit.ts` hands FILES-2 the directory basename instead of the declared `nameWithOwner`, so staging a correct `.ki.toml` in a hosted Project repository fails the hook. The repair is small: use `t.nameWithOwner ?? t.label` in the offline branch and add a gate test that stages `.ki.toml`.

**Query:** Should NO-GATE be refused back to a fix run for the FILES-2 identity repair, or accepted now with the repair as a follow-up record?

**Options:** a) (recommended, confidence medium - the spurious failure is demonstrated on the harness checkout itself, but the literal criterion is met and the repair is one line plus a test) Refuse NO-GATE and send it to one fix run that repairs the offline identity and adds a staged `.ki.toml` gate test; re-review that commit alone. b) Accept NO-GATE now and capture the FILES-2 repair as a new harness record, accepting that commits touching `.ki.toml` in hosted Project repositories will fail the hook until it lands.

### GOV209-REPOINT - GOV-209 live links before prune

**Context:** GOV-209 is accepted and its knowledge is homed in `standards-principal.md#acquired-packet-scaffold` and the principal `sources.md`. Two live ki-principal work-package files still link the record file: `ki.knowledge-acquisition/decisions.md:10` and `ki/messages.md:54`. Report links are acceptable breakage under the prune policy; these two are not reports.

**Query:** Should the two live links be repointed to the principal standard before GOV-209 is pruned?

**Options:** a) (recommended, confidence high - both files are owned by ki-principal work packages and the durable home exists) Repoint both to `standards-principal.md#acquired-packet-scaffold` in a ki-principal commit, then prune GOV-209 in a dedicated harness prune commit. b) Prune GOV-209 now and leave the two links to resolve to the pinned hosted URL when the work packages are next tidied.

### 🤖 → 👤 Handoff to supervisor · since 08:58 BST

👤 2 with you · 📥 3 to accept

- [with you] NOGATE-FILES2 · owner · since 08:58
- [with you] GOV209-REPOINT · owner · since 08:58
- [to accept] KI-HARNESS-GOV-189 · owner · since 08:58
- [to accept] KI-HARNESS-OPS-010 · owner · since 08:58
- [to accept] KI-HARNESS-OPS-011 · owner · since 08:58
- [committed] harness checkout clean at 0809ff80

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
