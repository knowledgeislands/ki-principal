# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-build-app046

**🤖 → 👤 Handoff to supervisor · Run report at 01:35 BST**

---

## Done

- [KI-OBSERVA-APP-046](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-046-browser-smoke-check-red.md>) planned to Ready (7ccad45), built (bb6ab2b) and moved to Awaiting review with its Review section (0d58592), in `apps-observatory.local` on `main`, not pushed.
- The fix touches only the smoke check. Readings are now stamped a minute before the run's own clock. A new step ages one pane past its threshold on purpose and confirms it shows as stale and dimmed. Sessions, work, review and known-lands now have their reads named. The Mermaid steps allow the feedback draft's refusal and the hostile label's refused inline handler; every containment check still stands. No product file changed.
- [KI-OBSERVA-VIS-041](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md>)'s Review line now says the browser smoke check passes, so its Verify item is met (0d58592).
- Checks: browser smoke check passes with full Chromium, twice in a row; tests pass (8 of 8); typecheck passes; lint has no errors (nine existing warnings elsewhere); roadmap audit FAIL=0.
- The live service was neither restarted nor stopped. No restart is due, because no product code changed.

## In Progress

Nothing.

## Queries

**Context** The hostile Mermaid label's `onerror` stays in the drawing frame just long enough for the frame's content policy to refuse it, although no drawn element keeps it. The check now counts that refusal as containment, which the record's Outstanding concerns note.
**Query** Should Mermaid's sanitising be made to strip the handler before the policy has to refuse it?
**Options** a) (recommended, confidence medium - the frame's policy is the designed containment and nothing runs) accept as is and leave it as a review note. b) capture a triage record to harden the label sanitising.
