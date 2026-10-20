---
note_type: streams/project
slug: knowledge-acquisition
title: Knowledge acquisition
outcome: The provider-neutral acquisition lifecycle is documented in one Pillars note, AI sessions are acquired into their owning repositories with verified retirement of the source, and the browser-runtime and WhatsApp spool questions are settled.
theme: model
lifecycle: completed
lead: Kris Brown
target: null
updated: 2026-10-20T04:14:07Z
author: Written with Claude
---

# Knowledge Acquisition

## Outcome

Document the provider-neutral knowledge acquisition lifecycle in one Pillars note, acquire AI sessions into their owning repositories with source conversations retired only once each move is verified, and settle the browser-runtime and WhatsApp spool questions. The test: every record that names this Project is delivered or closed. The direction follows [ADR-KI-PRINCIPAL-001](../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-001-provider-neutral-knowledge-acquisition.md); Kris is to confirm the finite outcome.

This Project sits in [Model](../Themes/model.md).

---

## Notes

- The lifecycle note changes `Pillars/`, so it runs through the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>).
- The harness's AI-session acquisition is the work in flight; whether the lifecycle note should lead the remaining acquisition work depends on what that delivery has learnt.
- **The harness record was narrowed on 2026-10-14.** Kris chose in the state-of-play thread's roadmap census, answering its rescope question for the harness acquisition record with 'rescope now', to narrow the harness's AI-session acquisition record to what it has delivered: the read-only Claude, Codex and ChatGPT source adapters, the `tools-ki` acquisition command and registry, the published `ki-acquire-chatgpt` capability with its project-selector contract, and the one-time conversion and staging of the official ChatGPT account export into its territories with explicit omissions. That record is awaiting review. The unfinished steps of its original plan now sit here until a record is opened for each in its owning repository:
  1. Evaluate the hybrid incremental path: local-cache change nomination, browser retrieval of new or changed readable sessions through the isolated browser trial, and periodic full-export reconciliation before browser coverage is trusted.
  2. Connect ChatGPT acquisition to a readable, authorised source that can enumerate projects and return complete conversations with their write-ups and assets.
  3. Represent unmapped projects, overlapping receiver mappings, missing sessions, changed sessions and failed reads explicitly without guessing or silently dropping content.
  4. Add receiver-local triage after acquisition so complete sessions can be harvested, retained as source evidence, routed onward, or marked as containing no residual knowledge.
  5. Separate Claude and Codex acquisition guidance from their housekeeping skills, using exception-based full-session import rather than routine bulk import.
  6. Decide whether the existing `mcp-housekeeping-*` repositories remain shared read-only source adapters or need acquisition-specific names or projections.
  7. Implement a separately invoked source-retirement manifest and provider-supported deletion path that fails closed on incomplete, changed, uncommitted or unverifiable acquisitions; deletion stays unavailable until every manifest entry has a recoverable acquired copy, the source still matches the manifest and the human approves that exact current manifest.
  8. Verify one complete ChatGPT project move and one completed agent-session no-op before enabling any source deletion.

  Open questions carried with them: the provisional Spirituality project binding, and what happens to the 77 export files referenced by no conversation. The harness's staging checkpoint of 2026-10-14 holds the evidence pattern (immutable project bindings, explicit omissions, checksums from a clean checkout) the Pillars lifecycle note can draw on.
- **Known World part, 2026-10-15.** On 15 October Kris placed the foundations model in [Known World](<../../Pillars/Philosophy/Emerging Concepts/Known World.md>) and gave this Project its part: the inception loop, publishing a seed into acquire's ChatGPT context and folding back the capture that returns with `ki_project`. [Known World](<../../Pillars/Philosophy/Emerging Concepts/Known World.md>) is the loop's first pilot, and an [Emerging Concepts](<../../Pillars/Philosophy/Emerging Concepts/Emerging Concepts.md>) note is a seed and fold-back target as well as a Project's Notes.
- **Dispatch came from Personal, 2026-10-18.** On 18 October Personal retired its Acquire > Dispatch Activity and Kris brought it into this Project.

### Close-out assessment

Written 20 October 2026. Delivered against the Outcome: the provider-neutral lifecycle is documented in the [Acquisition Process](<../../Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>) note; Acquire is the port, with one capture entry point, thin provider skills, provider-free territory context and dispatch into each receiving principal's `+/_ACQUIRED/`, simplified on 20 October to keep no ledger, no intake receipts and no return route; the read-only Claude, Codex and ChatGPT source adapters and the `ki` acquisition command exist; and the official ChatGPT account export is converted and staged into its territories.

Not delivered: AI-session acquisition end to end, with Claude and Codex acquisition separated from housekeeping, the browser-runtime path and verified, human-approved retirement of source conversations; the WhatsApp spool question; and the Acquisition Process note lags the 20 October simplification. Each is carried elsewhere: the AI-session steps and the note's realignment by records under [Model](../Themes/model.md), the WhatsApp spool refresh under [chezmoi](chezmoi.md), the EBU sources sync under Humans Not Robots' Phase 3 Project, the receiver's `+/_ACQUIRED/` scaffold by a standalone harness record, and the Known World seed pilot by State of play. Acquire's day-to-day intake and skills stay with Personal's Acquire intake work. Kris completed the Project on 20 October 2026, taking PROJECT-CLOSE a).
