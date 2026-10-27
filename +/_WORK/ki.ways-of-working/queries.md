# ki.ways-of-working queries

## Open

None

## Parked

- PERM-PROMPTS-SETTINGS - whether to change the chezmoi-managed permission settings; Kris, 25 October: "can we come back to it later?". Recommended: not now, revisit if Kris leaves bypass mode.
- STEWARD-FIELD - where a package records who looks after it; reviews disagree, the harness carries the model with a marked placeholder and the Valle Armonia pilot runs on `worker` as it is. Recommended: a new dedicated field taking `work/<id>` values only. Parked under the 27 October bulk reading; comes back if the pilot needs it.
- LEGACY-PREFIX - whether a `repo_code` rename stays a one-sweep change; renames are rare and Personal's runs as one sweep, while an allowance costs two checkers and tools-ki. Recommended: write the one-sweep rename into `ki-work-roadmap`. Parked under the 27 October bulk reading; comes back at the next rename.
- PARTIAL-REPOS - how a repository with only Pillars and Resources fits the model; Kris's own words defer it and HNR's tracked-notes workaround holds. Recommended: record the idea on the Ways of working Project note and open a `ki-work-design` brief when Kris takes it up. Parked under the 27 October bulk reading; comes back when Kris opens it.
- UNATTENDED-FIELD - recording unattended eligibility on records; a new record field with reviews disagreeing while the roadmap is cut to next to nothing. Recommended: adopt the optional `unattended` mapping and criteria. Parked under the 27 October bulk reading; comes back if a window plan needs it.
- UNATTENDED-AND-DUE-DATES - adopting the eight criteria as the unattended assessment; the due-date half is done and the criteria stay Personal's prototype. Recommended: adopt the criteria in `ki-delegation`, leaving UNATTENDED-FIELD to decide where the verdict is recorded. Parked under the 27 October bulk reading; comes back with UNATTENDED-FIELD.
- CLI-PREVIEW - whether public state-changing commands write by default and preview with `--dry-run`; a fleet-wide tool convention while tools are not ready and releases are deprioritised. Recommended: write by default, `--dry-run` and `-n` preview, both standards reconciled first and each tool changed through its own work. Parked under the 27 October bulk reading; comes back when a repair command is next touched.
- AREA-COLUMN - how the skill catalogue shows functional areas; the inline finder is live and the recommendation needs a harness change, a sync change and a new pin. Recommended: keep the live finder and ask the harness to publish the area table in its README block. Parked under the 27 October bulk reading; comes back if a harness refactor breaks the sync.
- REPO-STANDARDS-SET - which skills the Repository standards area lists; the live twelve serve and the difference is one box on one docs page. Recommended: include all sixteen, knowledge-base skills marked as applying only to knowledge bases. Parked under the 27 October bulk reading; comes back if a reader is misled.
- MGIT-CACHE-SCOPE - what to build first for the mgit cache; Kris asked for the concept in plain language first, and the design note keeps the six routes. Recommended: `--repos-from` with `--to-cache` and `--from-cache` in one record, `sync --push-only` and `--pull-only` in a second. Parked under the 27 October bulk reading; comes back when Kris wants the cache built.
- MGIT-CACHE-FAILED - whether a checkout the sweep failed on goes into the cached set; same feature as MGIT-CACHE-SCOPE. Recommended: exclude them, keep their names and count as diagnostics, and warn on every `--from-cache` that the selection is incomplete. Parked under the 27 October bulk reading; comes back with MGIT-CACHE-SCOPE.
- RECORD-2 - work-package schema failures in thirteen folders; forty judgement fixes across live packages with reviews disagreeing on who makes them, and the full audit now runs only in CI. Recommended: one run per territory sweep, read-back of every changed field. Parked under the 27 October bulk reading; comes back when the work-package standard settles or a package is next tidied.
- FOLDER-1 - extras in two work folders; a rename of nine old reports and a script's home, with the review finding the counts wrong. Recommended: rename the nine to `<name>.report.md`, move `adobe-remove.sh` beside its design note and `spec-sched.brief.md` to `briefs/`. Parked under the 27 October bulk reading; comes back when those packages are next tidied.
- COORD-7-REST - fifty-one identifiers in reports with no local target; a known floor in old run reports that marks will prune, and fixing it needs a fetch and a rewrite run. Recommended: authorise the fetch of the two personal checkouts, write pruned links and rewrite the 25 tag-like identifiers. Parked under the 27 October bulk reading; comes back if the reports survive pruning.
- LINT-WHERE - where generated Markdown gets linted; the check-only staged hook of 26 October stops a bad report at commit with CI the backstop, and a generator check is extra machinery. Recommended: check-only in the generator, after FORM-VS-RUMDL. Parked under the 27 October bulk reading; comes back if bad reports still reach `+/_WORK`.
- MISSING-TOOLS - installing the missing hook tools in three package repositories; the recommendation is itself to wait, and installing would add new software. Recommended: leave them until the second convergence and bring any needed tool to Kris as its own decision. Parked under the 27 October bulk reading; comes back at that convergence.
- REL-X64-TIMEOUT - darwin-x64 packaging fails on three five-second test timeouts; a test-only fix and a v0.14.2 release while releases are deprioritised, so it stands or falls with the releases-and-CI decision. Recommended: a bounded run gives the three lock-wait tests an explicit timeout, prepares v0.14.2 and runs the Release workflow. Parked under the 27 October bulk reading with v0.14.1 unpublished; comes back if Kris reopens releases.
- MIRROR-TOKEN - the Notion integration token and 1Password item behind the retired mirror; taken under the 27 October bulk reading, but the action is Kris's own and needs Notion and a credential change, both outside the window's limits. Recommended: revoke the integration in Notion and delete the 1Password item after `chezmoi apply` removes the last reference, finishing any HNR Notion page removal first. Parked for Kris to do at the machine.

### RIG-ATTENDED - Existing Rig attended prerequisites

since 2026-10-27 · from run/wow-rig-remainder; parked until Kris is available for the existing attended checks.

**Context:** These are existing prerequisites, not a request for another item-by-item approval. No live evidence was obtained in this run.

**Query:** Coordinator to route the existing attended checks and CORE-068 planning questions when Kris is available; keep both records in draft meanwhile.

**Options:**

a) (recommended, confidence high - preserves the plans' explicit gates) Arrange the existing attended checks and record the existing owner answers before another bounded delivery run.

b) Leave both drafts parked until those prerequisites are available.

### CLI160-EXTRA-FILES - disposition of additional ignored files

since 2026-10-27 · from run/wow-retire-cli160; operational follow-up parked until wow-retire-cli160-preserve reports, not a new owner choice.

**Context:** The report named only two untracked symlinks, but inspection also found 799 ignored paths under `.rumdl_cache/` and `reports/`. The brief requires stopping and preserving everything for any different dirt or missing proof.

**Query:** How should the additional files be reviewed and preserved or explicitly disposed of before a separately authorised retirement attempt?

**Options:**

a) (recommended, confidence high - preserves all material and respects this run's exact deletion boundary) Retain the checkout and branch; have the steward establish ownership and retention needs for the 799 additional files, then issue a bounded follow-up instruction.

b) Keep this checkout and branch retained without scheduling another retirement attempt.

### ANSWER-VECTOR - whether the first slice writes the answer line itself or waits for a `ki work answer` command

**Parked:** Parked with ki.observatory, which owns the feature and redesign. Release when its steward or the owner returns a route decision; neither option is selected here.

**Context:** The proposal's first slice has the Observatory compose the `messages.md` line and commit it through its own declared file effect, the path `feedback-send` already implements and tests, so the slice needs no tools-ki change. The Observatory's contract prefers consuming stable `ki` commands over duplicating work semantics, and a `ki work answer <id> <TAG> --option a --note "..."` command would make the line's shape one tool's and give the Observatory an argument vector instead. Waiting for it adds a tools-ki unit and a pin before anything can be answered in the Observatory; building the file effect first means a later swap to the command.

The review also found that the `ki-work-package` entry points let the owner, through the Observatory, commit a feedback package with its linking message, but grant no standalone answer-line write, so either option needs that authority written into the standard; sending stays off (`FEEDBACK_SENDING` false, KI-OBSERVA-BRG-004 still on hold).

**Query:** Should the first slice write the line through the Observatory's own file effect, with the `ki work answer` command as a later record, rather than wait for the command?

**Options:**

a) (recommended, confidence medium - the file effect and its gate exist and are tested, and the swap later is one operation's vector, but the Observatory's own contract leans the other way) Build the first slice on the existing file effect; capture `ki work answer` and `ki work queries` for tools-ki as a later message and the Observatory's KI-OBSERVA-INT-005. b) (blind review's pick, confidence medium - putting answer validation, the line's shape and the repository effect in one tools-ki command avoids a temporary second implementation; the feedback effect proves the mechanism, not an answer contract) Wait for tools-ki to provide `ki work answer`, and have the Observatory's first slice declare it as its vector from the start.

### WEBSITE-CLOSE - The website Project has no open records

**Parked:** Parked because MIRROR-SITE is back in active delivery and website source remains unpublished. Release when ki.website confirms its current delivery/rollout is complete; no Project closure is inferred.

**Context:** Pruning KI-WEBSITE-SITE-044 leaves the `website` Project with no open records; ki-principal's audit now warns that it needs a close-out assessment in `Streams/Projects/website.md`. The site is live on ki-design v1 and nothing else is queued.

**Query:** Should the website Project be closed out?

**Options:**

a) (recommended, confidence medium - nothing else is queued for the site) A short close-out assessment goes into the Project note under Notes in a later pass, capturing any follow-up as a record.

b) Leave the warning until website work resumes.

Coordinator note: held for the action plan; not raised to Kris yet.

### PUB-REVIEWED-CODE - Publish the three reviewed local code bundles

since 2026-10-27 · one blind review by run/wow-push-scope-blind; asked through the asynchronous input interface, then parked unanswered for the owner's return.

**Context:** The verified bundles are tools-ki's two-flag staged-check repair with its coupled routing-record closure/reference documentation; tools-rig's canonical staged-only pre-commit hook; and ki-techne-harness's independent agent-host role extraction. The reviewer inspected every unpublished ancestor and actual paths, confirmed the named main refs are fast-forward candidates, and found only manual-dispatch declared workflows and no configured pre-push hook. The personal standing rule excludes code/runtime publication, and ki-git separates committing from pushing. Website publication is outside this scope because its main push deploys. The later Rig wording correction is not silently added to the frozen reviewed tips.

**Query:** May I fast-forward push those three reviewed bundles to their origin/main branches?

**Options:**

a) (recommended, confidence high - one independent review found a bounded non-deploying Git scope, with completed local verification) Publish the three reviewed ranges and only their inspected coupled closure/reference documentation after final source/ancestry revalidation, without release, tag, package publication or deployment.

b) Keep the code commits local and retain the explicit repository, sol.local and branch handoffs.

**Release:** An affirmative owner answer; silence supplies no publication authority.
