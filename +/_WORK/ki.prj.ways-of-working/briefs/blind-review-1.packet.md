<!-- rumdl-disable MD041 -->

### WORKER-WAIT

**Context:** The agreed role model distinguishes the orchestrator from a worker. The current coordination contract includes an orchestrator mid-turn and authorised work waiting for worker capacity in With worker; the newer source says a worker run holds that state. No worker is in flight in either case. The agreed diagram does not settle that distinction. This choice blocks only those two cases, not the agreed shape, portable stop, report layout or compatible-reader planning. The run settled REST-PORTABLE, FINISH-FROM, REST-NAMES and ROLE-WORDS and found WAIT-RESUME and WORK-REENTRY to be factual compatibility work, in the [state-machine rollout plan](../design/state-machine-rollout-plan.md).

**Query:** Should With worker include these cases as worker-side ownership with an explicit queued/orchestrating description, or require an actual worker role holder before entering it?

**Options:**

- Require an actual worker role holder; qualify the dispatch/entry procedure and who holds authorised work before dispatch before enabling these cases, without inventing a state or redrawing the agreed machine in this rollout.
- Include both cases as worker-side ownership; say explicitly that this need not mean a run is in flight and show queued/orchestrating work accurately. Align the narrower source sentence and holder projections with that reading.

### HOST-CADENCE

**Context:** The owner requested regular equivalent work with offsets and gave an hour/five-minute example. No actual cadence, host offset or zone is adopted. Independent reviews establish that offsets cannot prevent overlap or certify completion. Rig and chezmoi would own any later realisation.

**Query:** Which cadence should the receiving owners prepare, without activating it?

**Options:**

- Keep cadence unchosen and prepare attended passes only until the pilot establishes phase duration and a suitable interval.
- Prepare hourly GMT/UTC phases: Terra primary :00 and secondary consumption :05; Sol primary :02 and secondary consumption :07, subject to explicit exclusion and pilot evidence.

### HOST-SECONDARY-PUBLISH

**Context:** The source wants the primary to read secondary updates but does not choose how those updates reach Git. Pulling primary work on a secondary cannot publish secondary-origin commits. Scheduling read-back alone therefore cannot fulfil that requirement. Existing per-repository grants still apply.

**Query:** Should secondary-origin changes continue to be published only through separately authorised attended work, or should Rig prepare a recurring secondary-publication phase for later review?

**Options:**

- Ask Rig and the Git-tool owner to prepare a distinct opt-in secondary-publication phase with repository eligibility and authority-at-effect checks; do not activate it or assume a grant from HOST-SYNC.
- Keep secondary consumption pull-only in the recurring proposal; secondary-origin changes reach Git through separately authorised attended work. Read-back consumes only what is actually published and reports outstanding unpublished work as outside its coverage.

### HOST-READBACK

**Context:** Kris explicitly left primary read-back to be decided and suggested a resync in short order. This is independent of secondary publication, message forwarding and request/reply trades. No timing guarantee can cover unpublished work or an absent host.

**Query:** Should primary read-back wait for its next hourly occurrence, or should the receiving owners prepare an additional short-delay phase?

**Options:**

- Prepare an extra pull-only read-back at Terra :10 and Sol :12, separately bounded and guarded; retain next-occurrence recovery if a prior phase is late or absent. This adds promptness, not publication authority or an acknowledgement guarantee.
- Read published secondary-origin updates at the start of the primary's next authorised hourly occurrence, before evaluating eligible primary publication. State the resulting delay explicitly; make no immediate-convergence promise.

### AMEND-RACE

**Context:** In the shared hnr-principal checkout a run amended `HEAD` after another package's explicit-path commit had landed, so `a1d61be4` became `21f4f02b` under the amending run's subject and trailer. The tree is identical and no content was lost, but the other package's commit subject and attribution were replaced. The `ki-git` standard already says to record and re-check `HEAD` before staging, to serialise the write window that advances shared `HEAD`, to rebuild only a commit "this session has not pushed" when it captured unrelated work, and to "never rewrite another actor's commit or a published commit"; it has no explicit check that `HEAD` is still the session's own commit before an amend. Its isolated-index procedure already uses that pattern: record the parent before committing and stop if `HEAD` has moved. The proposed rule would change `ki-git` in the KI Agentic Harness, which owns the change; no skill was changed here.

**Query:** Should `ki-git` allow an amend in a shared checkout only after confirming `HEAD` is the session's own unpublished commit, or forbid amending there altogether?

**Options:**

- Change no rule: the existing standard already forbids rewriting another actor's commit, so log the incident as a lapse in Mistakes and Lessons only.
- Never amend in a shared checkout: correct with a follow-up commit, and rewrite the standard's own-unpushed-commit repair path to match. Send it to the KI Agentic Harness as a message line for `ki-git`.
- Amend in a shared checkout only inside the serialised write window and only after confirming `HEAD` equals the commit this session itself recorded and has not pushed; otherwise make a new commit. Send it to the KI Agentic Harness as a message line for `ki-git`.
