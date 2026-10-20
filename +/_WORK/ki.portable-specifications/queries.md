# ki.portable-specifications queries

## Open

### SPEC-TEXT - accept draft 0.8 as the text of the three specifications

Draft 0.8 of `work`, `knowledge` and `acquire`, with the overview `specs.md` and the house mapping `work-house-profile.md`, is in `design/specs/`. It carries every owner decision, KNOWLEDGE-AS-SKILL and LINK-FIELDS included. Six blind reviews (draft-review-2 to draft-review-6, Codex) drove revisions 0.4 to 0.8; draft-review-6 found every earlier finding fixed, no new finding, and called it ready for the owner's read. One stated limit: the full `skills-ref` validator was never run, as its dependencies are not installed; its field checks were run from source. Accepting the text starts plan step 6, homing each spec as a reference in `ki-work-package`, `ki-acquire` and a new `ki-knowledge-package` in ki-agentic-harness; publication stays a later, separate query.

**Query:** Do you accept draft 0.8 as the specification text, to be homed in the three skills?

**Options:** a) (recommended, confidence high - reviewed six times, last review found nothing) Accept draft 0.8 and home it in the three skills. b) Name changes first; one revise run and one review, then back to you.

### HOMING-EDITS - accept the four homing edits as part of the spec text

**Context:** SPEC-TEXT is your approval of the three texts. Homing them into the harness needs four mechanical edits:

1. a version 1 Status line;
2. the attribution kept as it is;
3. links between the specifications made into plain names, because a relative link across skills breaks the harness link rule and naming house skills would make the specs house-specific;
4. a Contents list.

Any other wording change would come back to you.

**Query:** Do you accept these four edits as part of approving SPEC-TEXT, so the homed files count as your approved text?

**Options:** a) (recommended, confidence high - each edit is mechanical and changes no rule) Accept them with SPEC-TEXT; each run applies only these four. b) Approve each homed file again after its run.

### CATALOGUE-WRITE - one write-mode catalogue regeneration in 6c

**Context:** Adding a skill means regenerating the harness catalogue, the root README counts and two diagram files, which are checked as must-haves. The tool that writes them is `ki repo conform --skill ki-repo-harness` in write mode. HOOK-GUARD still applies in ki.ways-of-working's state, and every brief bans conform without `--dry-run`. mac-studio-setup's log calls HOOK-GUARD superseded but keeps the caution.

**Query:** May the 6c run's brief allow exactly one write-mode `ki repo conform --skill ki-repo-harness` in the harness, with every other conform staying dry-run?

**Options:** a) (recommended, confidence medium - the generator is the only route the harness supports, but the HOOK-GUARD status is not settled in one place) Allow that one command in 6c's brief, run with `--dry-run` first and its diff checked before writing. b) Keep the ban: 6c writes the generated sections by hand and the ki-repo-harness audit verifies them.

### HOMING-REVIEW - harness records and review for step 6

**Context:** The plan gates step 6 on "a harness record under ki-next, Steward review". The harness's last record is KI-HARNESS-GOV-227. The Paperclip Steward flow applies to Paperclip deliveries, and these are coordinator runs.

**Query:** How should step 6 be recorded and reviewed?

**Options:** a) (recommended, confidence medium - it keeps the harness's record trail without waiting on Paperclip) One small run captures three harness records, one for each of 6a, 6b and 6c, before they start; each homing run then gets one blind Codex review in place of the Steward before you accept it. b) Send all three through the Paperclip Steward and Convenor flow.

## Parked

None
