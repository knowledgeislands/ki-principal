# Coordination for any work package: review by Claude Opus 5.5

**Reviewer:** Default Claude runtime, Claude Opus 5.5. **Date:** 2026-10-28. **Read-only:** yes.

**Provenance:** Detached run `ways-of-working/wow-coord-any-review-claude`, report at 15:16 GMT. Own view was recorded in runtime temporary `stage1.md` before reflections; no other review or governing decisions/queries/reports was read. This homed copy preserves the review and its independently ranked choices; headings and wide tables are adapted to the design template. The brief was initially committed as `c43d1a14`; its unchanged content is recoverable in final trailer-corrected commit `12ed2066`.

## Own view

**Recommendation.** Coordination should be a session role that the owner opens explicitly. It should be available on any valid five-file package, whatever its level. Neither a package's existence nor its level, id segment or home should ever make a session a coordinator.

- **Regular and ad hoc work** stay self-coordinating by default, and conversational sessions remain the default for one-off work such as captures.
- **Opening a coordination thread on regular work** is for a bounded episode, such as Acquire's backlog. The opening decision in that package's `decisions.md` records an end condition. When the backlog drains or is handed back, the work returns to self-coordination: On hold, more expected.
- **State of play** is the same role, applied to the territory package and the packages assigned to it.
- **Under the role,** every rule for a responsive coordinator applies unchanged: delegation, the turn budget, the heartbeat, the banner and the owner report.

Confidence: high on direction, because it is the owner's own proposal and the canonical work-versus-session distinction already supports it. Medium on whether a coordination episode must be bounded or may be permanent.

**Home.** Packages live in the principal by default. A member-repository home is a deliberate exception: the owner approves it, the package's `decisions.md` logs it, and `work.md`'s Scope declares it in a `Home:` line. The checker should then verify that line. The retained MOD011 candidate already carries this principal-default sentence. So this design should depend on that candidate, not restate it. Acquire stays a member-homed exception, and its `origin/main` Scope `:25` already declares it. Confidence: medium-high.

**Pointer.** Reject a two-file pointer package under `+/_WORK/`, for three reasons:

- It breaks the closed five-file list (`standards-work-package.md:64-82`).
- It creates a second queue, and with it duplicates, loss and loops.
- It doubles the repositories a multi-host sync has to reconcile.

Keep one authoritative `messages.md` in the real home, and let senders write to it as they do today. A sender in a member repository writing to a Capital package already writes across repositories, so the pointer removes no real cross-repository write.

Discovery should go through what already exists: the parent State of play's `covers` register, plus one plain-prose home reference in that State of play's `work.md`. No field or schema is needed. Later, readers should resolve member homes only for ids that `covers` names, never by scanning for packages. Confidence: medium.

**Tending.**

- The package's own worker tends it, and its parent State of play tends it at each mark through `covers`.
- Findings reach the package as lines in its `messages.md`.
- Acquire's absence from Personal's `covers` is a conformance gap in Personal's State of play: `covers` lists `personal.regular.rig`, `-tower` and others, but not `personal.regular.acquire-intake`. It needs no new mechanism.
- Two gaps remain:
  - METHOD-NUDGE skips regular packages (hook `:91`).
  - It sees only the checkout it runs in, so member homes are never nudged from the Capital.

**Gates.** The affected sources are listed below. The canonical change needs an Enactment record and has to be sequenced after the MOD011 candidate, which edits the same two canonical documents.

## Fact check

The brief's facts F1 to F9 hold against the sources. These are the points worth checking or adding:

| Claim | Evidence | Verdict |
| --- | --- | --- |
| Evidence † | See source note † below. | See note. |
| Evidence ‡ | See source note ‡ below. | See note. |
| Evidence § | See source note § below. | See note. |
| Evidence ¶ | See source note ¶ below. | See note. |
| Evidence ‖ | See source note ‖ below. | See note. |
| Evidence †† | See source note †† below. | See note. |
| Evidence ‡‡ | See source note ‡‡ below. | See note. |

## Points (Agree / Differ / Add on each reflection)

1. **Agree.** **Add:** say plainly that `level` stays descriptive, and that a coordinating opener plus an owner decision selects the role. The bootstrap check becomes "the opener names a valid package and its decisions log carries an opening decision", not a level match. Without that, a stale opener could promote a package by itself.
2. **Agree.** **Add:** the hook's runtime filter (`:91`) and the style's applicability sentence are separate gates. The generator rewrites the style, but not the hook's filter, which must be edited by hand.
3. **Agree.** **Add:** the interim exception currently runs against written gates. Bootstrap step 3 tells an Acquire coordinator to stop on `regular`; the hook line and the style say "elsewhere ignore". Acquire `AGENTS.md:29` says "no PMO or delegation ceremony, background runs, routine banners or heartbeat". The interim decision should be quotable in Acquire's own `decisions.md` so that a bootstrapping session can find it. Otherwise a compliant session will refuse to coordinate, or will coordinate against its repository rule without citing the exception. REGULAR-WORK-ROLE (Acquire `messages.md:4`) will need a disposition that names the exception, so the two do not read as contradictory.
4. **Agree.** **Add:** the rubric enforces none of this today. The smallest enforcement is a check that a package outside the Capital carries a `Home:` Scope line, and that its parent State of play's `covers` lists it.
5. **Agree.** **Add:** "existing governed discovery surfaces" should mean, concretely, the parent `covers` register and one prose home reference. Today nothing maps a member-homed id to its repository except the `Home:` line inside the package itself, which is circular for discovery.
6. **Agree.** **Add, if a relay is ever chosen:** it must avoid two specific failures.
   - Duplicates: two hosts both relay a line before either pushes. Dedupe on the date, tag and sender key.
   - Loss: the source line is removed before the destination commit has been pushed, not merely committed.

   Direct messaging avoids both, and should be the default.
7. **Agree.** This reflection is compressed in the brief, so I read its intent as named ownership for opening, moving, findings and stale or unreachable homes, without assuming foreign stewardship. **Add:** an unreachable member home should be visible and age-flagged at the State of play's mark, matching the candidate's rule for host requirements. Nothing should be taken over.
8. **Agree.** **Add:** canonical changes to `Admin` and `Pillars` need an Enactment record. Sequence this amendment after the MOD011 candidate's integration, or fold it into that integration, because both edit Work Process and GDR-KI-PRINCIPAL-009.

I did not change my stage-one view after reading the reflections. They agree with it; the Adds are the additions above.

## Affected sources (later implementation; owners named)

- **Principal (Enactment):** Work Process `:46-48` (levels table row and "Regular work is self-coordinating"), and GDR-KI-PRINCIPAL-009 `:30`, re-grounded on candidate `996bcf64`.
- **Harness standard, `ki-coordination`, authored:** levels table `:122-130` (the Coordinates and Report forms rows), `:134`, Session kinds `:430-432`, and bootstrap step 3 `:848`.
- **Harness standard, generated:**
  - The `hook-line` source at `:592` becomes `hooks/coordinator-reminder.sh:17`.
  - The `output-style` source at `:616-632` becomes `output-styles/ki-coordinator.md:14`.
  - The generator is `skills/change-management/ki-coordination/scripts/generate/index.ts:61-90`. Run it once after the source edits.
- **Harness hook, authored:** `hooks/coordinator-reminder.sh:91` (the METHOD-NUDGE level filter).
- **Harness `ki-work-package`:** standard `:56-58` (principal default, member exception, `covers` including member-homed work), and the rubric `scripts/rubric/contexts/work-package.ts` for the member-home and `covers` checks.
- **tools-ki:** `src/core/work/prompts.ts:32,40,56-68` (thread kinds, package location, regular filter), and `src/commands/agent/index.ts:328-329` (reads only the Capital).
- **Acquire (owner-local):** `AGENTS.md:29`, the interim exception's record in its own `decisions.md`, and the disposition of `messages.md:4`.
- **Personal Principal:** `+/_WORK/personal/work.md` `covers`, which lacks `personal.regular.acquire-intake`. The fix goes as a message line to Personal's State of play, not as a direct edit.
- **Untouched:** the MOD011 candidate, HNR's identities and holds, and the typed-id target and its defaults (`work-id-shape-plan.md:38`).

## Risks

- **Role inflation.** Every regular package could start carrying banners and heartbeats. The guard is that opening needs an owner decision and an end condition.
- **Gate contradiction during the interim.** See point 3. A session may refuse to coordinate or act without a citation.
- **Sequencing collision with the unintegrated MOD011 candidate** on the same two canonical documents.
- **A relay, if adopted:** duplicates, loss, loops and multi-host retry. No exactly-once delivery is achievable with Git commits.
- **Invisible member homes:** CLI prompts and status read only the Capital, so the threads exist but have no opener listed.
- **Stale local checkouts.** Acquire's local `work.md` lacks its `Home:` line, while `origin/main` has it. A writer on that host could overwrite the newer remote content.

## Independently recommended decisions

### ELIGIBILITY - Who may open coordination on which package

**Context:** At present only territory and Project work may hold a coordinating session (standard `:134`, `:430`, `:848`). The owner proposes that any work package may hold one. The open question is whether such an episode is bounded or open-ended.

**Query:** Should coordination be an owner-opened role on any valid package, with regular and ad hoc episodes bounded by a logged end condition?

**Options:**

a) (recommended, confidence high - this is the owner's own proposal, and the bound guards against role inflation) Any valid package, opened only by an owner decision logged in that package. Regular and ad hoc episodes carry an end condition and fall back to self-coordination, On hold with more expected, once it is met.

b) Any valid package, with no bound. The coordinator stays until the owner closes it.

c) Keep coordination to territory and Project work, and handle Acquire's backlog as a short Project.

### HOME-EXCEPTION - Default home for regular and ad hoc packages

**Context:** The package standard (`:56`) allows any regular package to live in its member repository. HNR's METHOD point asks for the principal as the default, with member homes as a deliberate exception, and the retained MOD011 candidate already carries that rule. Acquire's published Scope already declares its member home.

**Query:** Should the principal be the default home, with a member home allowed only as an owner-approved exception declared in Scope and checked by the rubric?

**Options:**

a) (recommended, confidence medium - this matches HNR's point and the candidate, and keeps Acquire as it is; rubric cost is unverified) Principal by default. A member home needs owner approval logged in the package's `decisions.md` and a `Home:` Scope line, which the rubric enforces.

b) Keep today's broad allowance for member homes, and only add the rubric check.

c) Principal only: move Acquire's package. This is a destructive move and outside this design.

### POINTER-SHAPE - How the Capital points at a member-homed package

**Context:** PKG-POINTER proposes a two-file pointer package in the Capital, with lines relayed to the real home. That breaks the package contract's closed list and adds a second queue, and with it the risks of duplicates, loss and multi-host retry.

**Query:** How should a member-homed package be made discoverable from the Capital?

**Options:**

a) (recommended, confidence medium - it uses existing surfaces with one queue; the tooling cost is a later change to readers) No pointer package. The parent State of play's `covers` lists the package, and its `work.md` carries one prose home reference. Senders write directly to the real `messages.md`.

b) The same as a), plus a relay route through the State of play's own queue, with idempotent receipt and with the destination commit pushed before the source line is removed.

c) Adopt the two-file pointer package by amending the package contract (a new schema).

### TEND - Who tends regular and member-homed work

**Context:** `covers` is the existing register of tended work. Personal's `covers` omits Acquire intake. METHOD-NUDGE skips regular packages and sees only the local checkout.

**Query:** Should tending rest on `covers`, with the method nudge extended to regular packages that have an open coordination episode?

**Options:**

a) (recommended, confidence medium - it fixes the observed misses without a scheduler; the cost of resolving member homes in the hook is unverified) The parent State of play tends through `covers` at each mark. Send Personal's State of play a line to add Acquire intake. Extend the hook's level filter to cover any package with a non-null `method_read`.

b) `covers` only, and leave the hook unchanged.

c) A separate tending register or scheduler, which this design does not justify.

† F1: canonical exclusion; Work Process `:48` "Regular work is self-coordinating. It needs no coordination thread"; GDR-KI-PRINCIPAL-009 `:30`; Holds

‡ F2: gates; Standard `:122-136` table and `:134`; `:430` Session kinds; `:848` bootstrap step 3 "on `regular` or a mismatch it says so in one line"; hook `:17` (generated from the `hook-line` source block at standard `:592`); hook `:91` `case "$level" in territory\|project)`, which is authored and not generated; style `:14` (generated from source `:632`); Holds; line numbers shift slightly

§ F5: Acquire home; Local `work.md` Scope has no `Home:` line; `origin/main` Scope has "Home: this package lives in Acquire, not Personal's Capital"; Holds; the local checkout is behind, not a published defect

¶ F7: package contract; `standards-work-package.md:56` allows member homes for regular work only, declared in Scope; `:58` says `covers` is the register of "the Project and ad hoc work it coordinates"; Holds; Acquire's id `personal.regular.acquire-intake` is ad hoc in shape, so `covers` should already list it

‖ F8: CLI readers; `prompts.ts:68` filters out `level !== 'regular'`; `:40` hard-codes "in ${capital}"; `:32` names only territory or Project as the kind. `agent/index.ts:328-329` reads only `readWorkDefinitions(capital.path)`; Holds. Added: member-homed packages are invisible to `ki agent prompts`, whatever their level

†† Rubric; `work-package.ts` checks the Goals and Scope headings (`:61`, `:807`) and checks that `parent` resolves in the Capital (`:890`). Nothing checks a member-home declaration; Confirms the PKG-HOME gap

‡‡ F9: MOD011 candidate; `996bcf64` (3 files) already adds: Capital/principal as the default home for Project, regular and ad hoc packages; a member home as a "deliberate exception declared in `work.md` Scope"; package and thread "not one-to-one"; a principal-seated thread bootstrapping into its territory; Holds. This design sits on top of the candidate; replaying the same wording would duplicate it
