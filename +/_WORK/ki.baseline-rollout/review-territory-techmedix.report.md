# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Baseline rollout](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/baseline-rollout.md) › review-territory-techmedix

**🤖 → 👤 Handoff to supervisor · Run report at 23:45 BST · last mark 23:27 BST**

---

## Done

- Verified the [Techmedix declaration](/Users/krisbrown/workspaces/techmedix/tmx-principal/.ki.toml) includes the archived repository by its exact canonical identity.
- Verified [Techmedix Known Lands](</Users/krisbrown/workspaces/techmedix/tmx-principal/Admin/Governance/Known Lands.md:18>) explicitly retains it as an internal member, archived read-only because its domain is unregistered.
- Parsed the [local registry](/Users/krisbrown/.local/state/ki/registry.toml): no entry matches that identity; its conventional Techmedix checkout is absent.
- Verified [HNR Known Lands](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/Admin/Governance/Known Lands.md:32>) and the [principal standard](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/.agents/skills/ki-repo-kb-principal/references/standards-principal.md) separate local availability from governed membership.
- Verified [ADR-KI-PRINCIPAL-002](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-002-territory-derived-repository-selection.md) and [TERRITORY-003](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/specs/territories.md:27) explicitly require missing registration to fail selection.
- Traced [the resolver](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/territory/resolution.ts:177) and [audit/show callers](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/territory/index.ts:45): missing registration throws exit 2 before either report is rendered.
- Read the [selection contract tests](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/tests/cli/territory/selection.test.ts:80): they assert failure even when a filter excludes an unregistered member; tests were not executed.
- Completed the blind review without repository writes, commits, registration or network calls; only the authorised run-state files were written.

## In Progress

Nothing is running. TERRITORY-TECHMEDIX awaits the supervisor's disposition.

Outstanding - no action requested now: the executable audit was not rerun; the exit path was verified from local source. Remote archival status and the archived repository's own KI declaration remain unverified.

## Queries

### TERRITORY-TECHMEDIX - Preserve membership and expose incomplete audit coverage

**Context:** Techmedix declares `techmedix/apps-childhealthyorkshire.co.uk` as an internal member and records it as archived read-only. It has no local registration or conventional checkout. Both audit and show use the strict selector, which stops at this member before rendering findings. The inventory principle does not itself contradict that failure: membership remains declared, while the accepted selection contract requires full registration. The practical gap is that diagnostic commands cannot report the available members alongside the missing one. Changing this requires an explicit diagnostic contract and corresponding tests. Removing the declaration solely to obtain a passing audit would change the governed set; cloning would address this machine's registration gap without fixing diagnostic reporting.

**Query:** Should Techmedix retain its declared membership and request a tools-ki change so audit and show report unavailable declared members while checking those available?

**Options:**

a) (recommended, confidence high - preserves verified membership and exposes incomplete coverage through a bounded handoff) Hand a record to tools-ki for diagnostic audit/show reporting. Keep the declaration; identify the unregistered member explicitly, continue checking available members, and retain a non-zero audit result while coverage is incomplete. Preserve strict, atomic selection for roots and operational consumers. Include reconciliation of the accepted contract and tests in the handoff; this is a behaviour change, not a claim that today's implementation violates its contract.

b) Clone the archived repository locally and register it after explicit authorisation. This needs a network fetch and registry mutation; its KI declaration and Capital identity would still need checking before claiming the audit is unblocked.

c) Remove it from `territory_members` through Techmedix's Enactment Process and retain a historical reference in Known Lands. This requires an intentional membership decision and reconciliation of Known Lands' current internal-member designation, rather than merely omitting the unavailable member from selection.

### 🤖 → 👤 Handoff to supervisor · since 23:45 BST

👤 1 with you

- [with you] TERRITORY-TECHMEDIX · supervisor · since 23:45 BST
