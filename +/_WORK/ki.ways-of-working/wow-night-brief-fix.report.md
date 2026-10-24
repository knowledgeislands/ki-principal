# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-night-brief-fix

**🤖 → 👤 Handoff to supervisor · Run report at 02:04 BST · last mark 01:40 BST**

---

## Done

- [wow-night-harness-queue.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-night-harness-queue.md>): stop conditions rewritten in place to skip and continue, with the safety-stop list.
- [wow-night-principal-queue.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-night-principal-queue.md>): the same rewrite.
- [wow-night-observatory-queue.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-night-observatory-queue.md>): the same rewrite.
- [wow-night-parked-queries.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-night-parked-queries.md>): the same rewrite.
- [wow-night-tools-ki-queue-b.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-night-tools-ki-queue-b.md>): new. It is the first tools-ki brief with the same rewrite, LAUNCH-DEFAULTS removed from TAKE-STOCK and deferred to Kris as DEFAULTS-CONTRACT, and the writer, report, status and worktree paths renamed to `wow-night-tools-ki-queue-b`, which matches its designation in `state.md`.
- [wow-night-wave2-plan.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-night-wave2-plan.md>): the skip-and-continue rule added to its requirements for any brief covering more than one line or record.
- In the four in-place briefs, the writer-designation safety stop names "this run, by its launch name" rather than a fixed name, because `state.md` designates the harness lane writer as `wow-night-harness-queue-b`. A fixed name would have tripped the stop.
- Checks: none of the six briefs still has the old stop text, each has one safety-stop clause, there are no en or em dashes, and `git diff --check` passed. Nothing is committed, as the brief instructs, and no other file was touched.

## In Progress

Nothing is running.

Outstanding - no action requested now: the briefs remain uncommitted in the shared ki-principal checkout, alongside the other briefs already untracked there and the modified `state.md`.

## Queries

### QUEUED-SNAPSHOTS - queued runs still carry the old stop rule

**Context:** The queue holds `wow-night-harness-queue-b.queued.md`, `wow-night-principal-queue.queued.md` and `wow-night-parked-queries.queued.md` in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/`. Each one embeds the full brief text from when it was queued, including the old "Stop at the first missing authority" section, and none of them refers back to the brief file. The edits in this run therefore do not reach those queued runs. `wow-night-observatory-queue` has already launched with the old text.

**Query:** Should the coordinator re-queue the three queued runs from the edited briefs before they launch?

**Options:**
a) (recommended, confidence high - the queued prompts were checked directly and embed the old text) Dequeue the three queued runs and queue them again from the edited briefs under the same names, keeping their order and `--wait-for` chain; leave the running observatory run as it is.
b) Leave them queued; they would stop at their first unclear line, as `wow-night-tools-ki-queue` did.

### 🤖 → 👤 Handoff to supervisor · since 02:04 BST

👤 1 with you

- [with you] QUEUED-SNAPSHOTS · coordinator · since 02:04
- [uncommitted] six briefs in `+/_WORK/ki.ways-of-working/briefs/`
