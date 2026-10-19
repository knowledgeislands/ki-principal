# [Knowledge Islands model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/knowledge-islands-model/knowledge-islands-model.md) › [Knowledge acquisition](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/knowledge-acquisition.md) › stock-take

**Run report at 22:40 BST · last mark 00:26 BST (15 Oct)**

---

## Done

Read-only stock-take of acquire, the harness, tools-ki, `mcp-acquire-whatsapp`, chezmoi and this island, under INTAKE-SCOPE and IMAGE-SOURCE. Nothing was changed except this report. The three parts follow, then the queries.

### Part 1 - Overview of the knowledge acquisition area

Stages are those of the [Acquisition Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Acquisition Process/Acquisition Process.md>): Discover, Acquire, Stage, Harvest, Durable knowledge, Archive or delete source.

| Source | Tool or command | Lands in | Stage reached | Owner and record | Missing |
| --- | --- | --- | --- | --- | --- |
| ChatGPT, account export | `ki acquire import --adapter chatgpt` (tools-ki), skill `ki-acquire-chatgpt` | acquire `captures/<territory>/chatgpt/` and `.acquire/chatgpt/` | Stage done: 334 packages verified 2026-10-14. Harvest is receiver-side | Harness [KI-HARNESS-OPS-005 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/bf227839/docs/roadmap/KI-HARNESS-OPS-005-acquire-ai-sessions.md), awaiting review | Incremental source, project enumeration, binaries, retirement; the eight steps moved to the Project and have no record |
| ChatGPT, mobile or web chat | Paste-in capture by connector, rules in [CAPTURE-CHATGPT.md](/Users/krisbrown/workspaces/personal/acquire/CAPTURE-CHATGPT.md) | acquire `captures/<territory>/chatgpt/<date>-<topic>/` | Stage; text only. Binaries blocked at the connector | Acquire [KB-ACQUIRE-003 (pruned)](https://github.com/krisb/acquire/blob/e370006a8a5f5d79346146998030fb94ad30aa58/docs/roadmap/KB-ACQUIRE-003-investigate-binary-bridge.md), awaiting review | A binary route (BINARY-HOME, BINARY-HOLD); ZIP handoff is the interim |
| ChatGPT, seeds going out | Seed packs staged in `-` (SEED-HOME, 17 Oct) | acquire `context/chatgpt/<territory-key>/seeds/` | Not built; PILOT-GO waits on state-of-play | Knowledge-acquisition, seed-and-return loop | The single acquire item that BACK-LINK asked for |
| Claude Code | `mcp-housekeeping-claude` read-only discover, list, checkpoint, read | Nowhere; nothing staged | Discover and Acquire only | Harness [KI-HARNESS-OPS-005 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/bf227839/docs/roadmap/KI-HARNESS-OPS-005-acquire-ai-sessions.md) | tools-ki ships only the `granola` and `chatgpt` adapters; no content hash, no creation time |
| Codex | `mcp-housekeeping-codex` read-only; some `captures/*/codex/` folders exist | acquire `captures/personal/codex`, `captures/sacred-inquiry/codex` | Stage, manually | Same record | No adapter in tools-ki; how those folders arrived is not recorded in what I read |
| Granola | `ki acquire import --adapter granola`, skill `ki-acquire-granola` | acquire `captures/<territory>/granola/` and `.acquire/granola/` | Stage done; Harvest by receivers | Acquire [KB-ACQUIRE-004 (pruned)](https://github.com/krisb/acquire/blob/e370006a8a5f5d79346146998030fb94ad30aa58/docs/roadmap/KB-ACQUIRE-004-granola-acquired-workflow.md), awaiting review; [KB-ACQUIRE-002](/Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-002-migrate-granola-state.md) draft; tools-ki [KI-TOOL-KI-CLI-128 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/a22214ee581b73a1f395da88f9a118ad89814bb9/docs/roadmap/KI-TOOL-KI-CLI-128-granola-retention-safeguards.md) draft | State move to `+/_ACQUIRE/`; reset refusal; retirement |
| WhatsApp | `mcp-acquire-whatsapp` (live sync, app-export ZIP import), Rig job `acquire-whatsapp-spool-refresh` at 10:15 | An external spool outside Git, with a human reading view and `.meta/` authority; media sit in `.meta/media/` | Discover, Acquire and a spool-level Stage. No hand-off into acquire or an island | chezmoi [KB-DOTFILES-UE-035](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-035-install-whatsapp-spool-refresh.md) on hold; the MCP's own roadmap holds only its ledger | Where the spool lives is not fixed in what I read; no Harvest route; the Project's "WhatsApp spool question" is unsettled |
| Voice notes | `voicenotes-sync` plugin (island `+/_Voice Notes/`, agents never write there) | Island `+/_Voice Notes/` (empty in this checkout); 162 legacy recordings retained in acquire `captures/_review/voice-notes/retained-legacy/` (756 KB) | Plugin-managed; legacy is evidence only | Acquire owner Decision 9 | No staged route into acquire; legacy is not new capture |
| Direct intake | Conversational `intake` role, receipts in acquire `intake/` (9 so far) | acquire `captures/<territory>/intake/` | Stage | [acquire AGENTS.md](/Users/krisbrown/workspaces/personal/acquire/AGENTS.md); coordination stays here (INTAKE-ROLE) | None found; this is the nearest thing to a bulk drop |
| Images and screenshots | None. Granola screenshots arrive as meeting attachments only | 326 images in acquire Git (288,680 KB, 282 MB) | Stage as a side effect | None | Everything: IMAGE-SOURCE is the first request |
| Video | None | None | None | None | Everything |

Other sources exist as repositories (`mcp-gsuite`, `mcp-m365`, `mcp-ki-kb-notion-mirror`) but I did not examine them for acquisition.

In short, text sources are well covered up to Stage. Harvest and retirement are the weak end for every source, and binaries have no route at all except Granola attachments and the ChatGPT ZIP interim. The ADR's sixth stage, retirement, is still undecided. Four owners are involved: acquire for captures, tools-ki for commands, the harness for skills and adapters, and chezmoi for scheduling.

### Part 2 - Open acquisition items

| Item | State | Owner | Evidence |
| --- | --- | --- | --- |
| ACQ-FINISH: commit the nine Acer photos | Open and changed. The finish line asked for resized copies, but acquire reversed that on 2026-10-15. The Acer folder holds its README only. Now means ZIP handoff, then local commit from the ZIP | acquire-intake, for the commit | [Acer folder](/Users/krisbrown/workspaces/personal/acquire/captures/personal/chatgpt/2026-10-13-acer-windows-11-performance/README.md); acquire `afafe14` |
| RESIZE-RULE | Superseded, with nobody told. Acquire `755e619` (resize and retry) was reversed by `afafe14`, and chezmoi `799933a` followed. No resize rule is live. The old ACQ-FINISH finish line is now wrong | acquire-intake | [CAPTURE-CHATGPT.md](/Users/krisbrown/workspaces/personal/acquire/CAPTURE-CHATGPT.md) step 7; [chezmoi ChatGPT guide](/Users/krisbrown/.local/share/chezmoi/docs/guides/tools/chatgpt.md) |
| `.acquire/chatgpt/` inventory line | Done: the exact-path inventory is in [KB-ACQUIRE-002](/Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-002-migrate-granola-state.md) | acquire-intake | [KB-ACQUIRE-002](/Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-002-migrate-granola-state.md) line 33 |
| [KI-TOOL-KI-CLI-128 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/a22214ee581b73a1f395da88f9a118ad89814bb9/docs/roadmap/KI-TOOL-KI-CLI-128-granola-retention-safeguards.md) refusal step | Open. Draft, Next. Both refusal steps unchecked: ordinary reset and `--rebuild` must refuse when a handled disposition would be lost, plus the sandbox proof. RESET-FIRST confirmed | tools-ki, Project knowledge-acquisition | Record lines 54-55 |
| BINARY-HOME | Open. Candidate home is a private `mcp-acquire-chatgpt` on Cloudflare Workers, Kris as host owner, created only after the zero-build check fails. No-one has run that check on the iPhone | Knowledge-acquisition (engineering owner) | [KB-ACQUIRE-003 (pruned)](https://github.com/krisb/acquire/blob/e370006a8a5f5d79346146998030fb94ad30aa58/docs/roadmap/KB-ACQUIRE-003-investigate-binary-bridge.md); route-local-review (deleted 2026-10-15, commit `585d56b^`) |
| BINARY-HOLD | Open. Proposed answer: a private probe outside the [Techne Programme Hold](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne Programme Hold.md>), time-boxed, with a kill switch and teardown, recorded before any host grant. [KB-ACQUIRE-003 (pruned)](https://github.com/krisb/acquire/blob/e370006a8a5f5d79346146998030fb94ad30aa58/docs/roadmap/KB-ACQUIRE-003-investigate-binary-bridge.md) says the in-principle exception is "resolved", but no host grant is recorded | Kris | Same record; Hold policy |
| [KB-ACQUIRE-003 (pruned)](https://github.com/krisb/acquire/blob/e370006a8a5f5d79346146998030fb94ad30aa58/docs/roadmap/KB-ACQUIRE-003-investigate-binary-bridge.md) | Awaiting review. Offline acknowledgement slice delivered with a disclosed payload-read verification breach. Full proof is engineering-blocked (no suitable iPhone tool connected) | Knowledge-acquisition | Record |
| [KB-ACQUIRE-004 (pruned)](https://github.com/krisb/acquire/blob/e370006a8a5f5d79346146998030fb94ad30aa58/docs/roadmap/KB-ACQUIRE-004-granola-acquired-workflow.md) | Awaiting review | Knowledge-acquisition | Record |
| [KB-ACQUIRE-002](/Users/krisbrown/workspaces/personal/acquire/docs/roadmap/KB-ACQUIRE-002-migrate-granola-state.md) | Draft, Next. Support split open (Harness rubric paths, nested proof inside the rebuild-deleted folder). GRANOLA-PLAN and GRANOLA-CARRIER were to be closed under the 17 Oct decision log, which I did not see actioned | Knowledge-acquisition and acquire-intake | Record; route-local-review (deleted 2026-10-15, commit `585d56b^`) |
| [KI-HARNESS-OPS-005 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/bf227839/docs/roadmap/KI-HARNESS-OPS-005-acquire-ai-sessions.md) open steps | The record is awaiting review with its delivered steps ticked; Kris accepts. The eight unfinished steps (hybrid incremental path, readable project source, explicit unmapped and failed states, receiver triage, Claude and Codex guidance split, adapter naming, retirement manifest and deletion, one complete move before deletion) have no record. Open questions carried: the provisional Spirituality binding and 77 unreferenced export files | Kris to accept; knowledge-acquisition to write the successor record | Record "Review" and the [Project note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/knowledge-acquisition.md) |
| [KB-DOTFILES-UE-035](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-035-install-whatsapp-spool-refresh.md) | On hold, review 2026-10-21. Two boxes unchecked: verify count reporting against a known success (the record already names the cause, a mixed-output `{` parse, fixed), and recheck spool growth against history after a good 10:15 run | chezmoi thread | Record lines 53, 56 |
| [KI-PRINCIPAL-MOD-006 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/37b5f55/Streams/Roadmap/KI-PRINCIPAL-MOD-006-knowledge-acquisition-lifecycle.md) | Done. Accepted as `37b5f55`, committed locally and not yet pushed | Kris accepted | Commit `37b5f55` |
| Seed-and-return loop (SEED-HOME, FIELD-SHAPE, BACK-LINK, PILOT-GO) | Decided 17 Oct, one acquire roadmap item not yet captured; PILOT-GO waits on state-of-play copying section 4 | Knowledge-acquisition | [loop-design report](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_THREADS/knowledge-acquisition/loop-design.report.md); decisions log |
| ADR-HARBOUR follow-up | Decided, record not yet captured | Knowledge-acquisition | Decisions log, 17 Oct 22:30 |
| Source retirement | Undecided by design | Receiving repositories | Acquisition Process note |
| IMAGE-SOURCE | This report; one proposed record below | Kris | Part 3 |

I found no open records in `mcp-acquire-whatsapp` (its roadmap folder holds only the ledger) and nothing else open in the harness beyond the items above. I did not check Paperclip or the other Capitals.

### Part 3 - Images and video

**Holding area.** Bulk drops need a place that takes anything, keeps bytes untouched and decides nothing. Today there is none: images that arrive other than as Granola attachments have no route, and the only drop-like thing is a text intake receipt.

**Measured facts.**

- Acquire's Git directory is 512 MB (505.71 MiB pack); `captures/` is 355 MB. 326 images (307 PNG, 19 JPEG, 1 JPG) make up 282 MB of it. The largest is about 2 MB; no file is over 5 MB. No video exists anywhere in it.
- There is no Git LFS in acquire: its `.gitattributes` only disables line-ending changes for ChatGPT export payloads.
- Acquire is private. Its AGENTS.md forbids pushing or compacting history without instruction, so a mistaken commit of a large or private file cannot be undone without a rewrite.
- OneDrive: total 292 GB. Source stores per island, such as `sources-personal` (429 MB), `sources-techmedix` (627 MB) and `sources-legal` (20 GB), already hold bulky private material outside Git. tools-ki knows three store roles (`notes`, `sources`, `legacy`) and resolves physical paths through the local registry. I did not verify that a non-island repository such as acquire can bind a `sources` store; that is a point to check before building.

**Git versus OneDrive source store versus both.**

| Criterion | Git (acquire) | OneDrive source store | Both (recommended) |
| --- | --- | --- | --- |
| Size | Grows forever; images are already 55% of the pack; video would dwarf it | Fits any size; 292 GB in use already | Bytes outside, a small manifest inside |
| LFS | Possible, but adds GitHub storage and bandwidth and a remote service; not recommended | Not needed | Not needed |
| Retention | Permanent, pushed, copied to every clone | Deletable, with OneDrive recycle bin | Holding is deletable; only promoted items are permanent |
| Privacy | EXIF location, faces and third-party WhatsApp content become permanent history | Private to the account; can be pruned | Same as OneDrive until promoted |
| Provenance | Strong: commit, hash, history | Weak alone: a file path | Strong: Git manifest names hash, size, dimensions, source |
| Triage cost | One place | Triage must open a second place | One extra step, but only for promoted items |
| Multi-host | Via fetch and push | Via OneDrive sync | Both, each doing what it is good at |

Git alone is workable for screenshots, as Kris suggests and as Granola already does, but it commits acquire to every photo ever dropped and to video later. OneDrive alone loses the receipt and provenance model that intake already has.

**How a dropped item is filed for later.**

1. Kris drops files into a dated batch folder in the holding area: `holding/<YYYY-MM-DD>--<source>--<slug>/` with originals unchanged (source being `phone`, `whatsapp`, `screenshots`, `other`).
2. A receipt in acquire's existing `intake/` namespace records the batch: file count, total bytes, a `SHA256SUMS`, the source tool, the drop time and status `held`. No relevance screening and no interpretation, as intake already requires.
3. Later triage sets each file `held`, `routed` (to a territory), `promoted` (copied into `captures/<territory>/images/` with its hash and a note if small and worth keeping), or `retired` (decided, never automatic). Nothing is deleted without Kris's word, matching the undecided retirement rule.
4. Suggested defaults: a Git size cap of about 2 MB per promoted image; no video in Git; a review prompt after 90 days, not an auto-delete.

**Fit with the open questions.**

- _BINARY-HOME._ The bridge is the iPhone-to-acquire route for binaries. The holding area is its natural destination: the bridge stays a no-write probe now, and a later version delivers into a batch folder rather than committing to Git. This lowers the pressure on the bridge, since a drop does not have to go through ChatGPT at all.
- _BINARY-HOLD._ The Hold restricts remote execution and environment management. A local OneDrive folder is neither, so the holding area sits outside it. The question stays live for the bridge's hosting only.
- _WhatsApp spool._ The spool is already an external, replaceable path with its own `.meta/` authority and a cleanup step. Do not make the spool the holding area, because it is transient and cleanable by design. Treat its media as a source: a disposition step could copy chosen media into a batch folder with source `whatsapp`, and the spool's disposition record then carries the hash. The spool's physical location is the open point.

### Proposed record

- **Repository:** acquire, next ID `KB-ACQUIRE-005`. Reserve it in a ledger-only commit before writing (ledger at 4).
- **Title:** Image and video holding area.
- **Goal:** One declared place outside Git where bulk drops of images, screenshots and, later, video are held untouched, each batch receipted in acquire's intake namespace, so they can be triaged later and only chosen items are promoted into Git.
- **Scope:** Store binding for the holding area (including checking whether acquire can bind a `sources` store); the batch folder and receipt shape; the triage states and promotion cap; how WhatsApp media enters a batch; its relation to BINARY-HOME and BINARY-HOLD. Out of scope: building the iPhone bridge, any remote hosting, OCR or transcription, retirement of sources, and moving existing Granola images.
- **Coordination:** knowledge-acquisition coordinates, as BACK-LINK did for the seed-and-return item.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- [KI-PRINCIPAL-MOD-006 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/37b5f55/Streams/Roadmap/KI-PRINCIPAL-MOD-006-knowledge-acquisition-lifecycle.md) acceptance commit `37b5f55` is on local `main` and unpushed. It is another session's commit, so I did not push.
- I found no live resize rule, so the stale finish line for ACQ-FINISH should not be pasted. This belongs with the HOLDING-RECORD answer.
- The seed-and-return acquire item and ADR-HARBOUR follow-up wait for their records; nothing restarts until you have read this list.

## Queries

### HOLDING-RECORD - Approve the image and video holding area record

**Context:** You asked for one proposed record for bulk images and later video. Acquire's Git is already 512 MB, 282 MB of it Granola screenshots, without LFS or any size policy. A holding area outside Git keeps originals and privacy under control while Git keeps receipts and chosen items.

**Query:** Shall acquire get the `KB-ACQUIRE-005` record above, with a OneDrive-held store for bulk drops and Git for receipts and promoted items?

**Options:**

a) (recommended) Approve the record as proposed: holding area outside Git, receipts in Git, 2 MB promotion cap, no video in Git, review at 90 days. b) Git only, with the same receipts and cap, accepting that history grows permanently. c) OneDrive only, with no Git receipt. d) Git LFS, accepting the remote storage and bandwidth cost.

### ACQ-STALE - Retire the stale resize hand-off

**Context:** The nine Acer photos were to be finished by pasting a finish line that tells the chat to commit resized copies. Acquire reversed that rule on 15 October, so the pasted line would now contradict the repository. The Acer folder still holds only its README.

**Query:** Shall ACQ-FINISH be redone as the ZIP handoff under the current rule, with the resize wording dropped everywhere?

**Options:**

a) (recommended) Yes: acquire-intake finishes the Acer photos by ZIP handoff, and the resize finish line is discarded. b) Leave the photos uncommitted until the holding area exists, then drop them there. c) Drop the nine photos.

### BINARY-NEXT - Order BINARY-HOME and BINARY-HOLD behind the holding area

**Context:** Both questions are still open and nothing is running. A holding area gives the bridge somewhere safe to deliver, and a local folder falls outside the Techne Programme Hold, so the questions shrink to the bridge's hosting only.

**Query:** Shall BINARY-HOME and BINARY-HOLD wait until the holding area record is accepted, with the iPhone zero-build check run first?

**Options:**

a) (recommended) Yes: park both, and run the zero-build check on the iPhone before any home or host grant. b) Settle BINARY-HOME now with the private `mcp-acquire-chatgpt` on Cloudflare Workers, and BINARY-HOLD as a time-boxed exception. c) Withdraw the bridge and rely on drops and ZIP handoff.

### SUCCESSOR-RECORD - Write a record for the eight moved harness steps

**Context:** [KI-HARNESS-OPS-005 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/bf227839/docs/roadmap/KI-HARNESS-OPS-005-acquire-ai-sessions.md) was narrowed on 14 October and awaits your acceptance. Its eight unfinished steps wait in the Project note with no record, so they cannot be planned or reviewed.

**Query:** Shall the knowledge-acquisition thread write one successor record for those steps, once you have accepted the harness record?

**Options:**

a) (recommended) Yes: accept the harness record, then the thread captures one successor record in the harness, held at Next. b) Split into several records, one per step. c) Leave them in the Project note.

```text
HOLDING-RECORD

Approve KB-ACQUIRE-005 "Image and video holding area" in acquire as proposed in stock-take.report.md: holding area outside Git in a OneDrive source store, a receipt per batch in acquire's intake namespace, triage states held, routed, promoted and retired, a 2 MB per-image promotion cap, no video in Git and a 90-day review prompt. Knowledge-acquisition coordinates. Reserve the number in a ledger-only commit first.

---

ACQ-STALE

Finish the nine Acer photos by ZIP handoff under the current CAPTURE-CHATGPT.md rule, and discard the resize finish line everywhere it appears.

---

BINARY-NEXT

Park BINARY-HOME and BINARY-HOLD until the holding area record is accepted, and run the iPhone zero-build check first, before any home or host grant.

---

SUCCESSOR-RECORD

Accept KI-HARNESS-OPS-005 as delivered, then have knowledge-acquisition capture one successor record in the harness, held at Next, for the eight steps moved to the knowledge-acquisition Project.
```

╭─ run report · 2026-10-17T21:41:00Z ──────────────╮ │ │ │ █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀ · thread at rest │ │ █▀▀▄ █▀▀ ▀▀▀█ █    · nothing running │ │ █ █ █▄▄▄ ▄▄▄█ █    · nothing queued │ │ │ ╰──────────────────────────────────────────────────╯

- [at rest] nothing running or queued
- [waiting] HOLDING-RECORD
- [waiting] ACQ-STALE
- [waiting] BINARY-NEXT
- [waiting] SUCCESSOR-RECORD
- [unpushed] report committed locally; `37b5f55` from another session sits beneath it

```text
Resume knowledge-acquisition under current ki-pmo and ki-delegation since 00:26 BST (15 Oct): re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.
```
