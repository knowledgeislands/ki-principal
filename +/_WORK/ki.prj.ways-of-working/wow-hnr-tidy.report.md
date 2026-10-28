# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-hnr-tidy

**🤖 → 👤 Handoff to supervisor · Run report at 21:32 GMT · last mark 01:07 GMT**

---

## Done

- HNR-LEVEL: hnr-principal was clean with no stash and one local commit `6043f001` adding one line to `+/_WORK/hnr/messages.md`; that line is byte-identical in `bb404954` and in the current `origin/main` `923674cf` (checked with a fixed-string whole-line match after a fetch, since `git cherry` fails only because surrounding lines moved). Ran `git -C /Users/krisbrown/workspaces/humans-not-robots/hnr-principal reset -q --keep origin/main`: `main` is now `923674cf`, level with `origin/main`, working tree clean, no stash. Nothing to commit or push.
- TIDY-GAPS, read-only: both owners traced from Git history and the work packages; evidence and recommendations are in Queries below. Nothing was changed in ki-principal, ki-agentic-harness or chezmoi.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The two harness commit ids that the ki.chezmoi log names for the REV-012 filing (`ca98fd44e`, `63f850c23`) no longer exist in ki-agentic-harness; the record was committed as `7a759440` on 24 October, so the log's ids are stale pointers, not lost work.

## Queries

### SPEC-ORPHAN-OWNER - the orphan `+/_WORK/ki.specifications/` folder belongs to ki.portable-specifications

**Context:** `+/_WORK/ki.specifications/` was opened on 19 October 2026 as the Project work package for KI Specifications (`cd388627`). That day the Project was renamed under its PROJECT-NAME decision: the rename run's own report (`rename.report.md`, in the orphan folder) records that the whole package became [`+/_WORK/ki.portable-specifications/`](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/work.md), Project [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) under theme Model; Git confirms every tracked file moved as a pure rename in `a90aea3b`, and the renamed package has been on hold since 20 October (`release: Kris says resume`). The 25 `*.report.md` files left in the old path were run reports that nobody had ever tracked, so the rename did not carry them; all 25 are byte-identical copies of the run reports still held in `/Users/krisbrown/.local/state/ki/agents/specifications/`, and they were swept into Git by the `chore: baseline` commit `e78fff63` on 24 October. The renamed package holds no reports and had already pruned its only tracked one (`create-project.report.md`, `5b8ac0f3`) as homed. The orphan folder therefore has no identity of its own and carries nothing that its run packets do not.

**Query:** Do you accept ki.portable-specifications as the owner, with the repair being a bounded run that removes `+/_WORK/ki.specifications/` by explicit path once that package confirms its reports are homed?

**Options:**

a) (recommended, confidence high - every file is a verified byte-identical copy of a run report still in the specifications run directory, and the rename report names the new package) Owner ki.portable-specifications. Send one line to its `messages.md` naming the 25 reports; when it resumes, it checks each against its decisions log and deletes the folder by explicit path in a `docs(work)` commit; nothing is deleted before that check.

b) Owner ki.portable-specifications, but delete the folder now in a bounded run, relying on the run packets as the surviving copy, without the package's own homing check.

c) Keep the folder as it is until the Project resumes, with no message sent.

### RADAR-REPORT-HOME - `radar-confirm-2.report.md` came from ki.chezmoi and its evidence already lives in UE-108

**Context:** [KI-HARNESS-REV-012](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-REV-012-thoughtworks-radar-input.md) cites `/Users/krisbrown/.local/state/ki/agents/chezmoi/radar-confirm-2.report.md` as a "verified source check". That path is a run packet of the [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) work (Project [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md), theme Rig). Its decisions log shows the chain on 24 October 2026: radar-confirm launched at 12:28 BST (`b5c6c299`), relaunched as radar-confirm-2 at 12:31 BST with a read-only fetch grant for the public ThoughtWorks pages under Kris's 12:25 instruction (`230aadc8`), its finding that the fourth ring is Caution recorded at 12:35 BST (`1d9613dd`), and radar-confirm-3 then homing that finding at 12:41 BST in two places: the chezmoi record [PERSONAL-DOTFILES-UE-108](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-108-decide-tool-radar.md), whose "Confirmed scope and ring vocabulary" section carries the source URLs, the check date and the verbatim FAQ ring excerpts, and the harness record REV-012 (`7a759440`, `c4285065` in the log). The report file itself was never copied into the ki.chezmoi package, never tracked in any repository, and no longer exists in the chezmoi run directory or the archive; both records cite a dead local path. UE-108 holds everything the citation stood for.

**Query:** Do you accept ki.chezmoi as the owner, with the durable home being UE-108's ring-vocabulary section rather than a recreated report, and the repair a repointing of both citations?

**Options:**

a) (recommended, confidence high - the report's content is carried verbatim in UE-108 and the file is gone, so no provenance is invented) Owner ki.chezmoi. A bounded run repoints REV-012's citation to the public ThoughtWorks Radar and FAQ pages plus UE-108's section, and replaces UE-108's self-citation of the dead path with the same public pages and the 24 October check date; two small `docs(roadmap)` commits, one per repository, with REV-012 kept at triage.

b) Owner ki.chezmoi, and ask it to recreate the source check as a tracked note under the harness `ki-model-radar` sources reference, then cite that from both records.

c) Leave both citations as they are, treating the dead path as historical.
