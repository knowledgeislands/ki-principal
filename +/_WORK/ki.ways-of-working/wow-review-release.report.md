# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-release

**🤖 → 👤 Handoff to supervisor · Run report at 08:17 GMT · last mark unavailable: work records excluded**

---

## Done

- Consumer-history review — recommend adding the harness while retaining polling; examined tap commits `8a4e591`, `d6f3b0c` and harness commits `2628dd21`, `e4377ffa`.
- Timeout-history check — both limits first appeared in harness commit `81b8c8c7`; exact comparison confirms neither existed in its parent.
- Read-only review — no repository changes, commits, remote calls or access under `+/_WORK/`; only the requested runtime report and status files were written.

## In Progress

Nothing running.

Outstanding — no action requested now: GitHub scheduling delays, the skipped release, the exact cancelled run revision and App installation permissions were not independently verified. The brief both permits read-only `gh` and prohibits all remote calls; this review used local evidence only. The coordinator's mark and authoritative work label were not supplied and were not retrieved from excluded work records; the thread label below follows the standard's Ways of working example.

## Findings

### RELEASE-CONSUMER - Add the harness and retain polling

**Goal:** Recommend whether to register the harness as a release consumer or retain poll-only delivery, including whether history records a deliberate poll-only choice.

**Scope:** Both repositories' release workflows, consumer-registry history, harness receiver history, engineering guidance and tap onboarding guide; excluded work records and remote evidence.

**As of:** 2026-10-25 08:17 GMT, local checkout evidence.

**Recommendation: add the harness to the consumer list, keeping the poll. Confidence: high.** The receiver's introducing commit `2628dd21` (8 October) explicitly presents polling as a fallback for missed dispatches; `e4377ffa` (9 October) changes merge safeguards without removing either trigger. The [engineering contract](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-engineering/references/standards-engineering.md:158) describes dispatch plus daily fallback and permits registration to reduce latency. The tap registry was introduced for the website on 20 September (`8a4e591`), before the harness receiver existed; its only subsequent change renamed that website (`d6f3b0c`, 12 October). I found no recorded harness-specific decision for poll-only delivery in this history. Registration fits the receiver's intended use and the reported latency problem. Follow the [consumer onboarding checks](/Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/docs/guides/maintainer/release-app-operations.md:30), including selected App installation and a replay; dispatch still selects the latest immutable release, so this improves responsiveness rather than guaranteeing every intervening version gets a PR.

Decision raised: RELEASE-CONSUMER below.

### RELEASE-TIMEOUT - Monitor the safeguards added after the hangs

**Goal:** Recommend whether to watch the next pin PR or investigate a six-hour run despite the current timeout settings.

**Scope:** Harness CI history, the timeout-introducing commit and its parent, and current CI; no GitHub run logs or run-revision verification.

**As of:** 2026-10-25 08:17 GMT, local checkout evidence.

**Recommendation: watch the next pin PR under the current limits. Confidence: medium.** Commit `81b8c8c7`, dated 20 October at 22:22 BST, introduced both timeout safeguards; its parent has neither. Its explanation explicitly identifies Test-step hangs on 19 and 20 October that reached the six-hour cancellation limit, establishing that this change responded to those incidents. Current [job](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/.github/workflows/ci.yml:13) and [Test-step](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/.github/workflows/ci.yml:86) safeguards therefore are not evidence that the cancelled run ignored configured limits. The chronology check is already done, and it supports monitoring a run containing the fix rather than investigating an apparent timeout failure. However, calling this a one-off would be inaccurate: history records two hangs, and timeouts bound their impact without explaining their cause. Confidence is medium because the cancelled run's exact workflow revision and subsequent run outcomes remain unverified; a recurrence warrants investigating the test hang.

Decision raised: RELEASE-TIMEOUT below.

## Queries

### RELEASE-CONSUMER - Release-delivery choice

**Context:** Local history supports dispatch with polling as fallback and contains no harness-specific poll-only decision; installation permissions still need checking before implementation.

**Query:** Which delivery option should the implementation follow?

**Options:**

a) (recommended, confidence high - matches the receiver's original design and reduces dependence on delayed polling) Add the harness to the tap consumer list, retaining the poll and verifying onboarding.

b) Leave the harness poll-only.

### RELEASE-TIMEOUT - Next CI action

**Context:** The timeout change explicitly followed two six-hour hangs; the run's exact revision was not checked remotely, and the underlying hang remains unexplained.

**Query:** Should the next step be monitoring a pin PR that includes the fix, or further historical run investigation now?

**Options:**

a) (recommended, confidence medium - local history establishes a remedial timeout change, while exact run metadata remains unverified) Watch the next pin PR under the current safeguards; investigate if the hang recurs.

b) Verify the cancelled run's exact workflow revision now and investigate further if the safeguards predate it.

### 🤖 → 👤 Handoff to supervisor · since 08:17 GMT

👤 2 with you

- [with you] RELEASE-CONSUMER · owner · since 08:17 GMT
- [with you] RELEASE-TIMEOUT · owner · since 08:17 GMT

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
