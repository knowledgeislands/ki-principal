# [Rig](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/rig.md>) › [chezmoi](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md>) › host-locals-sol

**🤖 → 🧑 Handoff to supervisor · blocked · Run report at 09:17 BST · last mark 15:59 BST (15 October 2026)**

---

## Done

Sol bootstrap ran once and exited 0 under the [18 October migration authority](decisions.md#decision-84-2026-10-18t081504z); migration verification FAILED because exact config bytes changed. No further migration or recovery was attempted.

Installed build proof: `ki --version` is 0.11.0; `/Users/krisbrown/.local/bin/ki` resolves to `.ki-local-runner`, whose exact bytes execute Bun against `/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/main.ts`. Bun is 1.4.2; tools-ki branch is `main`, HEAD `6afdd4778c62f438e59a913a0b49e3a181d80ea6`. Exact ancestry of CLI-143 implementation `49686ca36a31ab79cd0a0b1de9b33e1ec3ae00a9` passed; implementation files match HEAD. No pull, fetch, build or source change occurred.

Implementation inspection: `src/agents/local-sources.ts` writes remembered mappings only when `locals.toml` is absent; `src/commands/bootstrap/ports.ts` wires migration into bootstrap; `src/core/harness/bootstrap/operation.ts` migrates before source selection and retains an active local binding, but subsequently reconciles configured skills. That reconciliation rewrote the live config in this run.

Protected before evidence captured doctor, share-safe and full diagnostics, exact config bytes, mappings and 23 harness/agent symlink bindings. Evidence is in `/Users/krisbrown/.local/state/ki/agents/chezmoi/host-locals-sol.evidence/`, directory mode 0700 and files 0600; raw config and full diagnostics are not committed or printed. Before `locals.toml` did not exist.

Before mappings in `/Users/krisbrown/.config/ki/config.toml`: `humansnotrobots/hnr-agentic-harness` → `/Users/krisbrown/workspaces/humans-not-robots/hnr-agentic-harness`; `knowledgeislands/ki-agentic-harness` → `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`.

After `/Users/krisbrown/.local/state/ki/locals.toml` is a regular file containing exactly those two mappings and no additional TOML keys. Bootstrap emitted exactly one migration message for two harnesses; no repeat bootstrap was run, so runtime idempotence was not independently tested.

Exact-byte check FAILED: config changed from 1556 to 1538 bytes; SHA-256 before `3e42a6f2f226ded478dc87994ba5b35ceffd5196cf48ac63d3f5ad7570840704`, after `c61124f13a65c35b578ac065ab625d1a50a7193aed1978e309f88813e29ad47a`. The only changed region is the `[territories]` ranking array at original lines 52-62, collapsed to one line with trailing-comma removal. Parsed TOML is exactly equal. Both snapshots remain protected; neither was restored or edited after failure.

Active bindings check passed: all 23 recorded symlink targets and resolved paths are identical. KI remains active from `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`; HNR remains an installed directory. Configured agents, harnesses and skills are semantically unchanged. No live on/off command was run.

Doctor before and after each exited 0: healthy, 17 pass, 0 warnings, 0 failures, 0 skipped. Every check was read; no doctor finding was present.

Diagnostics before and after each exited 0: valid config and registry, 2 agents, 2 harnesses, 10 skills, 50 repositories, 1 warning, 0 errors. The before warning says config locals await migration; the after warning says config locals are ignored because host-local state owns the checkouts. Both warnings were read. Diagnostics is therefore not warning-free, and the required all-clean step is not claimed.

Local on/off verification was not executed: the mandatory stop on config-byte difference took precedence over isolated fixture testing. Implementation review and unchanged live bindings do not establish full on/off behaviour. This verification remains incomplete.

Terra evidence search covered locally available shared ki-principal work reports/decisions and local agent report/state files. Only adoption, handoff and implementation-test references were found; no actual Terra host bootstrap and verification report was found. Common paths and test fixtures named Terra are not host verification. No remote host was contacted.

Chezmoi status before bootstrap was empty; source Git had an unrelated edit at `workspaces/knowledge-islands/dot_mgit.toml`, left untouched. Roadmap listing failed on the existing duplicate identifier ending 096, already recorded by the urgent drift run; no repair was attempted. Managed KI source remains untouched: no locals-table removal, source diff, apply or source commit. The source-change gate was not run because its two-host condition failed.

Prior urgent drift final outcome was checked in the [retained report](urgent-drift-20261018.report.md) and runtime review: all seven reviewed targets were applied and verified; no drift approval remains outstanding. Rig doctor retained two findings: UTM MAS source mismatch (`source-mismatch:unclassified`) and Headroom port ownership by Python instead of headroom-ai. These remain outside this task; no new Rig check or rollout change was made.

Previous SSH evidence, broader source delivery, Rig apply and job activation holds remain intact. No SSH, firewall, Headroom, scheduler, credential or other environment mutation occurred beyond the explicitly authorised bootstrap. No remote call, push, acceptance or pruning occurred.

Documentation preservation: this report, the request brief and its latest authority entry are the only intended commit paths in ki-principal. Commit and gate receipt will be recorded in the run-state handoff after the commit attempt.

## In Progress

Nothing running. Sol migration is blocked on the exact-byte failure; full on/off verification remains incomplete. Both-host success is unproven, so managed source removal and chezmoi apply remain held for Kris.

Outstanding - no action requested now: broader delivery remains parked; prior SSH and rollout holds are preserved. Protected evidence stays machine-local. No push is authorised; any documentation commit remains local to Sol's ki-principal `main` checkout and must be reconciled before work from another machine.

## Queries

### HOST-LOCALS-BYTES - bootstrap rewrote the protected config

**Context:** Bootstrap migrated both mappings and preserved active selection, but rewrote only the presentation of the territories ranking array. Parsed TOML is unchanged; the exact-byte requirement failed. The original bytes are protected, no restoration was authorised, and no actual Terra success evidence is available.

**Query:** How should the byte-preservation failure be resolved before either host is treated as passed?

**Options:**

a) (recommended, confidence high - the required invariant demonstrably failed) Keep source removal and apply held; arrange a bounded tools-ki byte-preservation correction and explicitly reviewed recovery/reverification, including isolated on/off checks and an actual Terra report.

b) Explicitly waive byte preservation for this formatting-only difference and issue a fresh bounded verification instruction; retain the two-host and apply gates.

### 🤖 → 🧑 Handoff to supervisor · blocked · since 09:17 BST

⛔ 1 blocked · 🧑 1 with you

- [blocked] Sol exact config bytes changed; migration verification stopped · run/host-locals-sol · since 09:17 BST
- [with you] HOST-LOCALS-BYTES · owner · since 09:17 BST
- [parked] broader delivery and existing SSH/job/source holds · coordinator · since 15:59 BST
- [unpushed] documentation persistence local only; no push authorised
