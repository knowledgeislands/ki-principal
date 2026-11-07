# ki.prj.orca-evaluation discussions

## Open

None; all parked on hand-over to the assistants, 2 November.

## Parked

Handed to personal.reg.assistant-terra on 2 November 2026 and carried by it.

### ORCA-UPSTREAM - The rest of the feedback to Orca

focus: trial

**Context:** Five items of feedback for Orca have been gathered. The first, the question card dropping line breaks, you authorised on 31 October, and it is being filed now as its own bug report. Four await you: (2) while a chat waits on a background task, its row reads "Monitoring background tas..." instead of its name, which hits every waiting coordinator; (3) a hidden sidebar item can only be restored from Settings > Appearance > Sidebar, with no hint, and the Mobile message points to the wrong Settings page; (4) Orca has no supported read-only way to export settings, so comparing settings across terra and sol would mean reading Orca's database directly; (5) a session Orca did not start cannot declare a parent or name, which matters less now Orca starts this work's runs. The stock-take suggested one bundled request with all five (medium confidence); the independent review disagreed: send one report per problem, and not more than you have approved, with items 2 and 3 as the useful next ones. Each report is public.

**Query:** Which of the four remaining items should go to Orca now?

**Options:**

a) (recommended, confidence high - reviewed: the independent review proposed it, and items 2 and 3 are defects you have hit yourself) Send items 2 and 3 now as separate short reports; keep item 4 as a later feature request if the cross-Mac settings check needs it; drop item 5 unless a session outside Orca shows the need again.

b) Send all four now, each as its own report, item 5 marked lower priority.

c) Send none of the four for now; only the card bug goes.

### THREADS-TRY - Test archiving one worker thread first

focus: trial

**Context:** Each Codex worker Orca starts leaves a saved conversation that shows in the ChatGPT app's recent list on the Mac that ran it: 50 on terra and 3 on sol so far, vega not yet counted. Orca has no setting for this; it keeps its own copy of each worker's output when the worker is released, and the brief and report are in the work package. Codex's own command line can archive a conversation (undone with `codex unarchive`) or delete it for good. Nobody has yet shown that archiving from the command line removes it from the ChatGPT app's list. Hand-editing app files is ruled out after 31 October.

**Query:** May a run on terra archive one finished worker conversation, check it leaves the ChatGPT app's list, then unarchive it and check it returns?

**Options:**

a) (recommended, confidence high - reviewed: the independent review proposed it; one reversible step settles the only unproven point before anything is done in bulk) Yes, one conversation on terra, through Codex's own commands only.

b) Skip the test and go straight to the clear-out.

### THREADS-SWEEP - Clear finished worker threads on each Mac

focus: trial

**Context:** If the one-thread test works, the existing worker conversations (50 on terra, 3 on sol, vega to be counted) can be archived in bulk through Codex's own command, matching only conversations that open with Orca's worker preamble and whose Orca worker has finished, never one still running. New ones keep appearing after every Orca Run until Orca can do this itself. You said they "should just be deleted"; deleting is permanent, while archived ones can be deleted later once nothing has needed them.

**Query:** Once the test works, should a run on each Mac archive every finished worker conversation, repeated after each Orca Run, with deletion a separate later step?

**Options:**

a) (recommended, confidence high - reviewed: the independent review agreed, reversible now and gets to deletion safely) Yes: archive now and after each Orca Run; after about two weeks with nothing restored, a later run deletes the archived ones, on your go.

b) Delete straight away instead of archiving, for the same matched conversations.

c) Archive the existing ones by hand in the ChatGPT app and do nothing automatic.

### THREADS-FR - Ask Orca to tidy a worker's conversation on release

focus: trial

**Context:** The lasting fix is in Orca: when a worker is released, Orca already keeps its own copy of the output, so it could then archive or delete the Codex conversation itself. Nobody has asked Orca for this; the nearest open requests are about filtering worker notifications and removing worktrees after release. A request is public. A "never save" mode for workers is not the right ask, because Orca reads the conversation while the worker runs.

**Query:** Should one short feature request go to Orca asking for an opt-in setting to archive or delete a worker's Codex conversation when it is released?

**Options:**

a) (recommended, confidence high - reviewed: the independent review recommended exactly this request; it is specific and opt-in) Yes, file it now as its own report.

b) Hold it until the clear-out has run for a while.
