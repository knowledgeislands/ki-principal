# ki.tools-burndown queries

## Open

### SYNC-CATEGORIES - Outcome categories

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Today sync prints one line for each checkout that changed or has a problem, but it adds none of them up. The record needs a fixed set of outcomes that every repository falls into. Reviewer adds: specify precedence for dirty checkouts whose fetch also failed, retaining both reasons.

**Query:** Which outcomes should the tally count, and where does each kind of skip fall?

**Options:**

a) (recommended, confidence medium - every checkout gets exactly one outcome, and "failed" means Git itself went wrong) Use five outcomes: in sync, pulled, pushed, skipped and failed. Skipped covers local changes, detached HEAD, no upstream, diverged, failed fetch, bare repositories and your own `-i` refusals. Failed covers only `status failed`, `cannot compare`, `pull failed` and `push failed`.

b) Add a sixth outcome, "need attention", as `overview` has. It would take diverged, dirty, detached and no-upstream checkouts, and leave skipped for bare repositories and your refusals.

c) (reviewer's view, confidence high - A fetch error belongs with operational failures within five exclusive outcomes) Count a failed fetch as failed, not skipped.

### SYNC-TALLY - Tally shape

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Ordinary dispatch ends with `mgit: N repositories: ...` and always prints zero counts. A checkout can never both pull and push, because a branch that is both ahead and behind has diverged and is skipped. Reviewer adds: count selected checkouts under --all-worktrees, rather than distinct repositories.

**Query:** What should the closing tally line look like?

**Options:**

a) (recommended, confidence high - reviewed: the counts then always add up to the total, and the line reads like dispatch's) `mgit sync: 57 repositories: 55 in sync, 0 pulled, 1 pushed, 1 skipped, 0 failed`. It keeps the `mgit sync:` prefix that sync's other lines use, prints zero counts, and counts each repository once.

b) The same line, but leave out the zero counts.

c) Use dispatch's bare `mgit:` prefix.

### SYNC-SKIPDETAIL - Where skipped detail goes

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** With 50 or more repositories, a skip line printed early in the run scrolls off the screen long before the end. That is how the five unpushed commits went unnoticed.

**Query:** Where should the run name each skipped or failed repository and its reason?

**Options:**

a) (recommended, confidence high - reviewed: this repeats the warnings where you will see them, and stays readable when several repositories need attention) Keep the per-repository lines as they are. After the tally, add one indented line for each skipped or failed repository, such as `ki-agentic-harness: local changes, 5 ahead`.

b) List them on the tally line itself, as dispatch lists its failures.

c) Leave them only in the per-repository lines, with the counts added there.

### SYNC-HELD - Which held commits to count

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** A dirty checkout's branch is still fetched, so up-to-date ahead and behind counts are available for it. A checkout whose fetch failed can only be compared with the copy of the upstream from its last successful fetch. A detached HEAD, or a branch with no upstream, has nothing to compare with. Reviewer adds: check fetch freshness even for dirty checkouts, and distinguish unavailable comparisons from zero counts.

**Query:** Which unpushed and unpulled commits should the skipped detail report?

**Options:**

a) (recommended, confidence high - reviewed: this covers the stranded-work case without new scanning) Count the checked-out branch only, as `mgit st` does. Give a dirty checkout its up-to-date ahead and behind counts. Give a failed fetch its counts against the last-fetched upstream, marked `stale`. Give detached heads and branches without an upstream no counts.

b) The same as a), but give a failed fetch no counts.

c) Also count other local branches that are ahead of their upstreams.

### SYNC-STREAMS - Standard streams

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Today every sync line goes to standard output. The `ki-repo-tools` command-line conventions put warnings and progress on standard error. [KI-TOOL-MGIT-CLI-029](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-029-cli-convention-departures.md) owns departures from those conventions across the commands. Reviewer adds: include prompts and diagnostic detail on standard error; the proposed deferral record currently excludes new departures.

**Query:** Should this record move sync's warning lines to standard error?

**Options:**

a) (recommended, confidence medium - this keeps the record bounded, and lets one record settle streams for every command) Leave the streams as they are, and record the departure on KI-TOOL-MGIT-CLI-029.

b) (reviewer's view, confidence medium - Apply the existing stream convention while changing this output contract) Do it here: move the skip, warning and progress lines to standard error, and keep the tally and the per-repository result lines on standard output.

### SYNC-EXIT - Exit status

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Today every skip except your own `-i` refusal makes sync exit with `1`, and so does any bare repository. Answering `q`, or input ending, under `-i` exits `1` with no closing lines at all. Reviewer adds: label incomplete runs and targets not reached; counts cannot explain every non-zero exit, and q currently reprompts rather than quits.

**Query:** Should the exit status change, and what should a quit under `-i` print?

**Options:**

a) (recommended, confidence high - reviewed: the exit status stays stable, and a quit no longer hides what was reached) Keep the exit status exactly as it is, with no extra explanation on the tally line, since the skipped and failed counts already show why. When you quit under `-i`, print the tally and detail for the repositories reached so far.

b) Keep the exit status, and keep quitting silent, as now.

c) Exit `1` only for failed checkouts, and treat skips as success.

### SYNC-JSON - Machine output

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Dispatch and `overview` both give `--json` a `summary` object; sync has no `--json`. No consumer has asked for one, and the record is already size m.

**Query:** Should sync gain `--json` in this record?

**Options:**

a) (recommended, confidence high - reviewed: nothing needs it yet, and adding it would grow the record past size m) Defer it to a new triage record.

b) Add it here, with a `summary` object that matches dispatch and `overview`, and one result for each repository.

### SYNC-VERBOSE - Verbose mode

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Today bare repositories are counted only without `-v`. With `-v`, each one gets its own line instead.

**Query:** Should the tally depend on `-v`?

**Options:**

a) (recommended, confidence high - reviewed: one fixed output is simpler to read and to test) Print the same tally with and without `-v`, with bare repositories always counted as skipped. `-v` then adds only progress lines.

b) Keep today's split, and count bare repositories in the tally only without `-v`.

### SYNC-CLEANFETCH - Clean-branch wording

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** MGIT-WS-018, the manual and the running-commands guide say sync fetches every _clean_ tracking branch. The code fetches every tracking branch, which is why a dirty checkout's behind count is up to date. Reviewer adds: qualify local upstreams with remote '.', which need no remote fetch.

**Query:** Should the documents change to match the code, or the code to match the documents?

**Options:**

a) (recommended, confidence high - reviewed: the code's behaviour is what makes the dirty-checkout counts possible) Correct the specification, manual and guide to say that every tracking branch is fetched.

b) Narrow the fetch to clean branches, which loses the up-to-date behind counts for dirty checkouts.

### TRIAGE-NEXT - Plan the two high-priority tools-ki records

since 2026-10-19 · from tritools.report.md in the run state folder · blind review qreview7 pending

**Context:** KI-TOOL-KI-CLI-161 and KI-TOOL-KI-CLI-152 are both high priority but sit at Soon. Next needs a full plan, and each still has design questions open.

**Query:** Should both go to `ki-plan` now, so they can reach Next?

**Options:**

a) (recommended, confidence medium - 161 blocks the estate commit-msg hooks and the FAIL step, and 152 is a live close-gate bug) Plan KI-TOOL-KI-CLI-161 first, then KI-TOOL-KI-CLI-152, splitting out its gate fix as a small record if planning finds it separable.

b) Leave both at Soon until the burndown reaches them.

### HOOK-ADOPT - Adopt the three hook follow-up records

since 2026-10-19 · from tritools.report.md in the run state folder · blind review qreview7 pending

**Context:** The three new hook records stay in triage, as HOOK-CAPTURE a) said. The pilot has finished, and the estate-wide migration Kris ordered at 23:24 BST needs the binding sweep for the second machine.

**Query:** Should they be adopted now?

**Options:**

a) (recommended, confidence medium - the sweep is on the path to the FAIL step, while claims only matter for repositories with neither hook nor Husky) Adopt KI-TOOL-KI-CLI-164 at Next for planning, and KI-TOOL-KI-CLI-165 and KI-HARNESS-GOV-225 at Soon, with the harness record first.

b) Leave all three in triage until the estate migration reports.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
