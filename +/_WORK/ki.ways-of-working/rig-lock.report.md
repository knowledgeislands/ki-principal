# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › rig-lock

**🤖 → 🧑 Handoff to supervisor · Run report at 06:35 BST · last mark 06:33 BST**

---

## Done

I built the shared apply/upgrade lock under RIG-APPLY-LOCK a) in tools-rig's main checkout, tested it against fixture locks only and pushed `main` fast-forward. Nothing live was touched: no `rig apply`, `rig upgrade`, `config.toml` migration, chezmoi change or release.

Rig (tools-rig):

- [KI-TOOL-RIG-CORE-058](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-058-apply-lock-handler-history.md), lock half (`55ee447`). Live `rig apply` (any scope or target) and live `rig upgrade` now share one lock per platform. They take it before calling Homebrew, uv or any other provider, and hold it until the run ends. The existing reconciliation lock now sits inside it and is otherwise unchanged, so a tool-only apply still never takes it (RIG-ORCH-037). A second run that finds the lock held stops with status 2 and names the holder as active, stale or unknown. Rig never removes the lock itself. Dry runs and read-only commands take no lock. When an unattended upgrade is refused this way, the last-upgrade report records why nothing ran (`operation-lock=STATE owner=apply|upgrade|unknown`, zero counts, no paths). The record is now Awaiting review.
- Specification: RIG-STATE-025 now covers the operation lock as well as the reconciliation lock, and RIG-STATE-030 covers the refused-run report, as the Fable opinion noted. RIG-STATE-035's verify text and its out-of-date test counts are corrected. The manual, the commands and unattended-updates guides, and the changelog are updated.
- [KI-TOOL-RIG-CORE-061](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-061-removal-lock-diagnostics.md), new triage record (`cbf19bd` reserves the number, `7f86bef` adds the record). It covers two gaps that fall outside KI-TOOL-RIG-CORE-058: `rig remove --apply` takes no lock yet, and doctor does not name a held or stale lock. Capture only.

Checks:

- Full test suite: all 572 Bats tests pass.
- `ki repo audit`: passes, with only the existing HOOK-1 warning.
- ShellCheck, Bash syntax and the assembly drift check: clean.
- Fixture benchmark: within budget.
- Native-provider version smoke (`brew --version`, `uv --version` only): passes.
- `mandoc` lint and `git diff --check`: clean.

Other Rig rows of the tools burndown [work file](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/work.md):

- RIG-TARGET-SPEED-ACCEPT: the independent review is already recorded. What remains is your acceptance of [KI-TOOL-RIG-CORE-060](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md), which I did not do.
- RIG-TARGET-SPEED-LOAD: parked by design, with recommendation a) to leave the configuration load as it is. No work done.

No other Rig row was open for an agent.

Provisional, for Kris to confirm. I took the recommended course each time:

- A refused run exits with status 2, the existing code for "rejected before work started".
- Only a lock refusal writes the last-upgrade report. Other status-2 rejections, such as a bad flag or profile, still write none.
- The owner detail in the report is reduced to `apply`, `upgrade` or `unknown`, so it never carries a path.
- The apply-history concurrency test now stands in a fixture writer that holds no lock, because two live applies can no longer overlap.
- Capturing KI-TOOL-RIG-CORE-061.

## In Progress

Nothing is running.

Waiting for Kris:

- Review and accept KI-TOOL-RIG-CORE-058 (both halves are now delivered) and [KI-TOOL-RIG-CORE-060](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md). The other Rig records from the tools-burndown run (KI-TOOL-RIG-CORE-042, -052, -054 and -055) are still Awaiting review too.
- Neither Mac has the lock until a Rig release, which is your call (RIG-LOCK-RELEASE).

Outstanding - no action requested now:

- I left the held drafts KI-TOOL-RIG-CLI-026, KI-TOOL-RIG-CORE-048 and KI-TOOL-RIG-DIST-011 and the triage records KI-TOOL-RIG-CORE-053 and -057 alone.

## Queries

### RIG-LOCK-CHOICES - confirming the provisional lock choices

**Context:** KI-TOOL-RIG-CORE-058 was delivered under RIG-APPLY-LOCK a), which was approved provisionally on Fable's opinion. The detailed choices are listed under Done.

**Query:** Do you confirm the lock as delivered?

**Options:**

a) (recommended, confidence medium - it follows option a) closely and reuses the existing rejection code) Confirm all of the provisional choices as they stand. b) Use a distinct exit status for a refused run, so wrappers can tell contention apart from other rejections. c) Have every status-2 rejection of an unattended upgrade write the last-upgrade report, not only a lock refusal.

### RIG-LOCK-RELEASE - getting the lock onto both Macs

**Context:** The lock is on tools-rig `main` but unreleased. An unattended upgrade on a Mac can still run beside a manual apply until a release is installed. On 18 October you said no release until told.

**Query:** When should Rig be released with the lock?

**Options:**

a) (recommended, confidence medium - one review pass covers all the queued Rig records) Once you have reviewed KI-TOOL-RIG-CORE-058 alongside the other Awaiting-review Rig records. b) Now, ahead of review. c) Hold for KI-TOOL-RIG-CORE-061 as well.

### RIG-LOCK-FOLLOWUP - adopting KI-TOOL-RIG-CORE-061

**Context:** KI-TOOL-RIG-CORE-061 is capture-only. `rig remove --apply` still calls uninstallers without the lock, and a stale lock is visible only in the refusal message or the unattended report.

**Query:** Should KI-TOOL-RIG-CORE-061 be adopted?

**Options:**

a) (recommended, confidence medium - small, and it closes the last unlocked native-manager path) Adopt it next for Rig, once KI-TOOL-RIG-CORE-058's design is confirmed. b) Keep it in triage.

```text
RIG-LOCK-CHOICES a)
RIG-LOCK-RELEASE a)
RIG-LOCK-FOLLOWUP a)
```

### 🤖 → 🧑 Handoff to supervisor · since 06:35 BST

🧑 3 with you · 🏁 run finished

- [with you] RIG-LOCK-CHOICES · owner · since 06:35
- [with you] RIG-LOCK-RELEASE · owner · since 06:35
- [with you] RIG-LOCK-FOLLOWUP · owner · since 06:35
- [committed] tools-rig, pushed
