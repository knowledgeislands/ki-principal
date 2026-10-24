# KI > Foundations > Timelines › tl-qreview

**🤖 → 👤 Handoff to supervisor · Run report at 00:30 BST · last mark unavailable under the blind-review boundary**

---

## Done

Reviewed all four queries against permitted local sources; excluded recommendations and run reports remained unread.

Connector inspection confirmed publication gaps; naming inspection confirmed all three names are available; dated-item inspection confirmed real numeric durations and dates into February 2027.

No repository changes or commits; no remote calls, account tests or test-suite execution.

## In Progress

Nothing is running. Provider subscription, revocation and actual free/busy behaviour remain unverified and belong to the later adapter proof.

## Queries

Independent recommendations follow; these are review findings, not owner approvals.

## FEED-HOME

**Context:** Directly verified Google's timed-only create/update payloads and missing transparency/stable create key in [calendar implementation](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/src/main/calendar/index.ts:87), and Microsoft's default-calendar create with no returned event ID in [create.ts](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/src/main/calendar/create.ts:10); its registration has no update tool. Took the no-site/private-base context on trust. A provider's private subscription address and account-specific availability were not verified.

**Query:** How should private sets be published?

**Options:**

a) (recommended, confidence high - local-only v1 is reversible and avoids connector gaps verified in source) Choose course 4, conditional on proving the later provider route: local views first; separate account-sync adapter after connector work; test calendar, then a few personal dates. Verify private subscription, refresh and revocation before promising them. Treat any provider secret URL as a bearer credential, not stronger access control merely because the provider hosts it.

b) Build a token-checking host if independent subscription remains necessary after that proof; it also needs a demonstrated client and access-control model.

## SKILL-NAME

**Context:** Directly verified the [naming grammar](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-003-dependency-order-for-multi-skill-composition.md:28), absence of all three candidate skill names, and no timeline mention anywhere in the inspected ki-diagrams Markdown/TypeScript. The local AGENTS.md confirms Calendar's note-folder role. Took Kris's quoted wording from the supplied brief.

**Query:** Which name should the skill take?

**Options:**

a) (recommended, confidence medium - it names the subscribable sets Kris asked for, while a folder name does not reserve a skill concern) Use `ki-calendars`, with a description explicitly covering milestone-centred dated sets, generated timelines and feeds. Document the boundary with Calendar period notes.

b) Use `ki-key-dates` if naming the canonical items matters more than the delivered calendar sets; `ki-timelines` remains valid, but emphasises one rendering.

## ADOPTION-ORDER

**Context:** Directly verified eleven untimed 5G entries, its [all-day feed builder](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3/apps/site/lib/ics.ts:141), locally documented public calendar hosting, and legal's existing generated timeline and dated Items through February 2027. Took personal's readiness and live host operation on trust; no deployment or client was tested.

**Query:** In what order should adoption proceed?

**Options:**

a) (recommended, confidence high - it separates a small extraction proof from private publication while delivering legal's local value early) Choose course 3: bounded 5G parity pilot, then 5G's source merge and legal's local timeline independently; adapter proof on a test calendar, then a small personal set, then legal sync. Do not make legal's local view wait for the 5G merge. Add offline cases for timed events, spans, busy validation and privacy because 5G's dates cannot prove those behaviours.

b) Legal-first local adoption if even the bounded pilot would delay its needed view; defer legal sync regardless.

## TIMED-BUSY

**Context:** Directly verified [Command Centre date semantics](</Users/krisbrown/workspaces/legal/legal-principal/Pillars/Command Centre/Command Centre Guide.md:169>) and four Items with integer `duration_minutes` alongside `event_at`. Took the supplied RFC no-end semantics on trust; no standards or client check was possible offline. Kris's no-invention rule is settled input.

**Query:** What happens when a timed busy item has no end?

**Options:**

a) (recommended, confidence high - requiring recorded duration preserves the settled rule and makes busy mean an actual interval) Choose course 3: fail validation without an explicit end or positive `duration_minutes`; require end after start and reject inconsistent values when both are supplied. Keep the invalid item visible with a diagnostic; do not silently omit it from a supposedly complete publication.

b) Allow a zero-duration busy item only by changing the promised busy semantics; do not substitute an all-day block.

### 🤖 → 👤 Handoff to supervisor · since 00:30 BST

👤 4 review findings with supervisor

- [with supervisor] FEED-HOME, SKILL-NAME, ADOPTION-ORDER, TIMED-BUSY · coordinating session · since 00:30 BST
