# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › tools-burndown

**🤖 → 🧑 Handoff to supervisor · Run report at 06:05 BST · last mark 04:30 BST**

---

## Done

I worked through the order in the tools burndown [work file](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/work.md), tested each row against fixtures only and pushed every repository fast-forward to `main`. Nothing live was touched, and I made no release.

Rig (tools-rig):

- [KI-TOOL-RIG-CORE-060](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md), single-target speed: the independent review is recorded (`71bab11`, `5f593ab`). It found nothing blocking, so the record waits for you to accept it.
- [KI-TOOL-RIG-CORE-042](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md), profile-filtered Dock items (`7cbe340`): one shared Dock layout is now filtered by the resolved profile, so laptop and studio each show only their own apps, in the shared order. Awaiting review.
- [KI-TOOL-RIG-CORE-052](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-052-doctor-service-launch-prerequisites.md), [KI-TOOL-RIG-CORE-054](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-054-command-line-tools-check.md) and [KI-TOOL-RIG-CORE-055](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-055-interpreter-port-owner-matching.md) (`8432f33`): doctor now names a service that cannot launch, outdated Command Line Tools, and a Python port owner running as a module such as headroom. All three are awaiting review.
- [KI-TOOL-RIG-CORE-058](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-058-apply-lock-handler-history.md), history half (`59e13f2`): a failed default-application step now writes its outcome to the apply history and shows up in status and doctor. The same fix covers firewall steps, which had the same gap. The shared apply/upgrade lock is not started (see RIG-APPLY-LOCK), so the record stays In progress.

mgit (tools-mgit), records only:

- `55fecf0` and `ca71902` hold the mgit plan records:
  - [KI-TOOL-MGIT-CLI-018](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-018-estate-scale-output.md) and [KI-TOOL-MGIT-CLI-019](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-019-pass-through-escape-hatch.md) are reworded;
  - [KI-TOOL-MGIT-CLI-020](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-020-safe-parallel-sync.md), [KI-TOOL-MGIT-CLI-021](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-021-estate-overview.md) and [KI-TOOL-MGIT-CLI-022](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-022-external-member-review-findings.md) are new, all in triage.
- [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md) waits for you to accept it.

ki (tools-ki), unreleased on `main` since v0.11.0:

- [KI-TOOL-KI-CLI-146](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-146-ki-quiet-setting.md), the `KI_QUIET` setting, is captured as an unadopted record (`d835eab8`).
- The tools-burndown run's `events.seen` is moved from 2 to 21, so `ki agent wait` no longer replays old finishes.
- [KI-TOOL-KI-CLI-144](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-144-older-runs-start-seen.md) (`2777b4d6`): the first read of an older run counts agents that had already ended as seen. Awaiting review.
- [KI-TOOL-KI-CLI-142](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-142-preserve-harness-release-settings.md) (`c79ff4c6`): bootstrap no longer drops configured harness release settings when it rewrites `config.toml`. Awaiting review. I did not run it on Terra or Sol.
- [KI-TOOL-KI-CLI-137](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-137-agent-run-tmp-home.md) (`0e48ca27`): each agent gets `$TMPDIR/ki-agents/<run>/<name>/`. `ki agent close` refuses while the folder holds anything, then removes it. Awaiting review. The state-folder tooling in its plan is split out to the new [KI-TOOL-KI-CLI-147](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-147-agent-state-folder-tooling.md) (`a69278e9`).
- [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) (`df1c24ed`), two of its three parts:
  - the launch footer now starts at its `## Rules` heading, and its links are made absolute;
  - launch and queue warn when a brief names a second report path.

  The grant texts wait on [KI-HARNESS-GOV-201](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md), so the record stays In progress.

Provisional, for Kris to confirm. Each is recorded in its record, and I took the recommended course each time:

- the parked mgit answers: MGIT-PLAN, ESTATE-HOME, ESCAPE-NAMES, OVERVIEW-VERB, MGIT-RECORDS and MGIT-REVIEW-LOWS, all a);
- KI-TOOL-RIG-CORE-042's deviation: the missing-item evidence goes in observation detail, not a separate list;
- the plan choices for KI-TOOL-RIG-CORE-052, -054 and -055;
- the plan choices for KI-TOOL-KI-CLI-144 and -142;
- for KI-TOOL-KI-CLI-137:
  - the folder is derived from `TMPDIR` when `close` runs;
  - `/tmp` is the fallback;
  - an empty folder passes;
  - the KI-TOOL-KI-CLI-147 split;
- delivering two parts of KI-TOOL-KI-CLI-134 ahead of its grants;
- KI-TOOL-RIG-CORE-058 delivered in part, with firewall included;
- the `events.seen` move.

## In Progress

Nothing is running.

Waiting for Kris:

- Review and accept these records:
  - [KI-TOOL-RIG-CORE-060](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-060-single-target-operation-speed.md), -042, -052, -054 and -055;
  - [KI-TOOL-MGIT-CLI-017](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-017-unified-external-members.md);
  - [KI-TOOL-KI-CLI-144](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-144-older-runs-start-seen.md), -142 and -137.
- Accept [KI-TOOL-KI-CLI-126](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-126-unavailable-store-breaks-repair.md). That unblocks [KI-TOOL-KI-CLI-131](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-131-host-absent-store-state.md) and [KI-TOOL-KI-CLI-136](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-136-errors-suggest-fixes.md), which I did not start.
- Accepting KI-TOOL-RIG-CORE-042 on `sol` needs three things: a chezmoi record for the Dock declaration change, your placement decision for studio-only apps, and your approval of a live run.

Outstanding - no action requested now:

- These records are blocked, so I did not start them:
  - [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) waits for [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md) Phase 1, and ways of working dispatches it.
  - [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md) waits for [KI-TOOL-MGIT-CLI-021](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-021-estate-overview.md) and [KI-HARNESS-GOV-203](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-203-git-clean-down-criteria.md).
- [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md)'s "Decision 55" citations stay parked under DECISION-55-CITATIONS: that decisions log has not moved yet.
- DESK-KIT-SOP a) is not delivered: `ki agent send` refused because state-of-play is not live (see DESK-KIT-SOP).
- I did not do the thread-folder tidy. The common rules put `+/_THREADS/tools-burndown/` off limits, and migrate-apply has since moved it into `+/_WORK/ki.tools-burndown/`, whose MIGRATED line is the tools burndown thread's own to act on.
- I left KI-TOOL-RIG-CORE-026, -048 and KI-TOOL-RIG-DIST-011 held, and left techne alone.

## Queries

### RIG-APPLY-LOCK - shape of the shared apply/upgrade lock

**Context:** KI-TOOL-RIG-CORE-058's other half makes `rig apply` and `rig upgrade` refuse to run at the same time. Today the only lock is the resource reconciliation lock. A tool-only apply must not take that lock (RIG-ORCH-037), and an unattended upgrade reports through its last-run report (RIG-STATE-030).

**Query:** Which lock design should KI-TOOL-RIG-CORE-058 take?

**Options:**

a) (recommended, confidence medium) A separate per-platform operation lock that wraps the reconciliation lock and leaves it unchanged. An unattended upgrade that finds the lock held records a refused last run and exits non-zero. b) One lock that replaces the reconciliation lock everywhere. This amends RIG-ORCH-037's tool-only behaviour. c) Drop the lock half and accept the history half alone.

### TOOLS-RELEASE - cutting v0.11.1

**Context:** tools-ki `main` carries KI-TOOL-KI-CLI-144, -142, -137 and part of -134 since v0.11.0. KI-TOOL-KI-CLI-142 fixes bootstrap losing harness release settings. On 18 October you said no release until told; 0.11.1 is the one pre-approved fix release.

**Query:** When should v0.11.1 be cut?

**Options:**

a) (recommended, confidence medium) Once you have reviewed the three Awaiting-review tools-ki records, so the -142 fix reaches both Macs. b) Now, ahead of review. c) Hold for more of the ways-of-working changes.

### HARNESS-PATHS - adopting KI-TOOL-KI-CLI-143

**Context:** [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md) is capture-only. It moves remembered local harness checkout paths out of the chezmoi-managed `config.toml`, and needs a host-local ownership model and a migration that keeps behaviour. Its prerequisite, -142, is delivered.

**Query:** Should KI-TOOL-KI-CLI-143 be adopted, and on which model?

**Options:**

a) (recommended, confidence medium) Adopt it with a host-local file under ki's state directory that is read first. Bootstrap moves `[locals]` there once, and chezmoi's source drops the entries in the same change. b) Keep it in triage until the ways-of-working changes settle.

### DESK-KIT-SOP - the state-of-play line

**Context:** Your DESK-KIT-SOP a) has state-of-play drop its desk-kit lines. `ki agent send` refused because state-of-play is not live, and my brief lets me edit no other work file.

**Query:** How should the line reach state-of-play?

**Options:**

a) (recommended, confidence high) Ways of working adds it to the Messages in state-of-play's work file, for its next live session. b) Send it when state-of-play is next live.

```text
RIG-APPLY-LOCK a)
TOOLS-RELEASE a)
HARNESS-PATHS a)
DESK-KIT-SOP a)
```

### 🤖 → 🧑 Handoff to supervisor · since 06:05 BST

🧑 4 with you · 🏁 run finished

- [with you] RIG-APPLY-LOCK · owner · since 06:05
- [with you] TOOLS-RELEASE · owner · since 06:05
- [with you] HARNESS-PATHS · owner · since 06:05
- [with you] DESK-KIT-SOP · owner · since 06:05
- [committed] tools-rig, tools-mgit and tools-ki, pushed
