# Window AWAY-31-OCT survey plan

Written by run `survey` at 01:40 GMT on Saturday 31 October 2026, for the unattended window AWAY-31-OCT that ends at 09:00 GMT (09:00 UTC). Read-only survey of every Knowledge Islands work package in `+/_WORK/` except this one, at ki-principal `3c232224`.

## Authority and limits

The grant is AWAY-31-OCT in this package's [decisions](../../decisions.md), confirmed by Kris at 01:29 GMT: "do as much as you can across all of those projects all those work packages", within decisions already made. Every unit below cites its own logged owner words. The window and this survey exclude deploy, publish, release and installation; credential and provider operations; adopting an open query's option; acceptance or pruning of records; Orca workers; HNR source; force-push, `--no-verify` and rebase, reset or stash in a shared checkout.

Two repository rules shape the lanes:

- **One tools-ki writer.** OWNER-LANE a), 16 October: "tools-burndown runs the only tools-ki writer for all in-scope records". The tools-ki units run as one serial lane, in the order below.
- **Harness review.** The harness `AGENTS.md` makes "an approved Ready item or explicitly scoped direct user instruction" eligible, and requires an independent review of the exact candidate before integration. Each harness unit therefore ends with a separate review run before its push.

No unit needs a roadmap adoption: each one either carries Kris's explicit, bounded words or only captures an unadopted record. Where a repository turns out to need a Ready record before delivery, the run captures it unadopted and stops.

## The hold question (HOLD-SCOPE)

Several authorised units sit in packages whose hold releases only on Kris's word:

- ki.prj.tools-burndown: "Kris says resume".
- ki.prj.agent-host: "when Kris brings this work package back up".
- ki.prj.baseline-rollout: "Kris says resume".
- ki.prj.observatory: with Kris under DRAIN-WITH-SUPERVISOR, "start nothing new".
- ki.prj.website: "when Kris opens this Project work".

The grant names "all those work packages" but does not say it releases a hold. Units that depend on this are marked **HOLD-SCOPE** under "Waits on". The survey report carries this as a query. Until the coordinator settles it, the units without that mark run first. Whatever the answer, run these units from this package's run group. Leave each held package's state and hold untouched, and send it one receipt line in its `messages.md` for each delivered unit. Queued message lines are allowed under the embargo.

## Lanes

Different repositories run in parallel; units in the same lane run in order.

| Lane | Repository | Units, in order |
| --- | --- | --- |
| H | ki-agentic-harness | U1, U9, U16 |
| T | tools-ki (one writer) | U2, U6, U10, U11, U15, U18, U19, U20, U23 |
| C | `~/.local/share/chezmoi` | U3, U13 |
| S | packages-stoa | U4 |
| G | tools-mgit | U5, U17 |
| P | ki-principal, this package and SoP | U7, U8, U12, U14, U22 |
| X | ki-techne-harness | U21 |
| D | ki-design | U24 |

Run about three at once: H, C and S or P first, while HOLD-SCOPE is settled; then T and G.

## Units, in order of value and independence

### U1 - Method text for decided owner answers

- **Package / repository:** ki.prj.ways-of-working / ki-agentic-harness (`ki-delegation`, `ki-coordination`, `output-styles/ki-coordinator.md`, banner test).
- **Authority:** BANNER-TRIM, Kris, 31 October: "If it's handed off, it's handed off ... why are we also putting things like committed there as well? ... I think the part of the summary itself". RECOMMEND-CONFIDENCE, Kris, relayed 30 October: "when you're making suggestions, regardless of where the suggestions are made, and even outside of the coordination capabilities, I definitely want to flag them as the recommendations, and I definitely want to have a confidence value on them". Owner answers of 30 October 2026, 06:15 GMT: ORCA-REACH a), WAKE-SESSION a) (the `ki-delegation` verb "stays with ki.prj.ways-of-working"), WAKE-DURABLE a), WORKTREE-OPTOUT a) and AGENT-HOME a).
- **Tier:** push. **Waits on:** nothing. **Size:** M.
- **Brief:** In ki-agentic-harness, in its own worktree, make the following standard and style changes, each exactly as decided and nothing wider:
  - Drop `[handoff]` and the housekeeping items `[committed]`, `[uncommitted]`, `[recovered]`, `[unlogged]` and `[behind]` from the glyph banner. Move what they reported into the report body: Done for commits, In Progress for uncommitted and behind. Keep the territory sweep findings unless the change wording plainly covers them; if it is unclear, keep them and report.
  - In the reply forms, make every suggestion in any reply form a recommendation carrying a confidence value.
  - In `ki-delegation`: Orca only on attended Macs, with packages opting in by logged decision; `ki agent` the only launcher on `vega`; an always-on Orca server only through the Enactment Process. One contract verb, `wait`, implemented natively by each launcher: one detached waiter at a time, bounded at five minutes and re-armed after each wake, proved per runtime and launcher before anyone relies on it, with session wakes best effort. The headless pass stays the durable wake, and Orca automations are not wakes. The worktree baseline is that only runs that write nothing inside any repository may skip their own worktree. Mark it as taking effect when the `ki` integrate command and the four worktree prerequisites land, with checkout-isolation's pilot rule standing until then. `ki agent` stays the maintained floor launcher, with no features that duplicate Orca.
  - Leave out WAKE-HOST, ORCH-NAME, LAYOUT, WORKER-WAIT and REVIEW-CHALLENGE, which are still open with Kris.
  - Run `bun run test`, `bunx tsc --noEmit` and the focused `ki repo audit --skill` for each changed skill, and commit by explicit path.
  - Hand the exact candidate to a separate review run, which must pass before the run pushes fast-forward.
  - Then send one REFRESH line to each live KI package's `messages.md`, naming the revision.

### U2 - Strip the coordinator's Orca identity from `ki agent` runs (ORCA-ENV-LEAK)

- **Package / repository:** ki.prj.tools-burndown / tools-ki.
- **Authority:** ORCA-SUBAGENTS, Kris, 30 October 2026: "fixing the way that we're using KI agent to make sure that they run in the same way that Orca does so that they come through as sub agents rather than primary agents". Sent as the IMPORTANT ORCA-ENV-LEAK line on 30 October.
- **Tier:** push, no release. **Waits on:** HOLD-SCOPE. **Size:** S. A security fix and the first tools-ki unit.
- **Brief:** In tools-ki, in its own worktree, change `src/core/agent/runtimes.ts` so that runtime children never inherit `ORCA_AGENT_SESSION_ID`, `ORCA_AGENT_SESSION_SPAWN_TOKEN`, `ORCA_STRUCTURED_SESSION` or `ORCA_CHAT_SCRATCH_DIR`. `ki`'s own dispatcher process keeps them, per Part A of [the Orca sub-agents design](../orca-subagents/design.md). Do not remove the pane, tab, worktree or hook variables that ki.prj.orca-evaluation's open ORCA-IDENTITY-LEAK query lists; that wider set waits for Kris. Add a boundary test proving the four are absent from a launched child's environment and present in the parent. Run the repository's checks once, as VERIFY-ONCE asks, then commit by explicit path and push fast-forward. Write no release or tag. Then send a receipt line to ki.prj.tools-burndown and ki.prj.orca-evaluation, and disposition the ORCA-ENV-LEAK line in tools-burndown's queue by a decisions entry. Part B, the Orca placement, waits for the pilot.

### U3 - Three decided chezmoi source changes

- **Package / repository:** ki.prj.chezmoi / `~/.local/share/chezmoi`.
- **Authority:** WHATSAPP-MCP-SCOPE, Kris's decision at about 01:25 GMT on 25 October "to leave the WhatsApp MCP server off sol". MGIT-PUSH-ALIAS, Kris adopted route B of [mgit-cache](../mgit-cache.md) on 26 October as an `mpush` alias. ZT-FINDINGS, routed under RESTART-ON-SOL on 25 October for homing in the chezmoi guides. The package's next step 1, "take the queue".
- **Tier:** push, source only, never `chezmoi apply`. **Waits on:** nothing. ki.prj.chezmoi is with Kris for four open queries, none about these lines. **Size:** S.
- **Brief:** In the chezmoi source repository, in its own worktree, make three changes:
  - Scope `mcp-acquire-whatsapp` to terra in the MCP inventory source (`mcp-servers.yaml`) using the inventory's own host-targeting field, so sol no longer starts it.
  - Add the `mpush` alias exactly as worded in the MGIT-PUSH-ALIAS line, in the alias file the source already uses.
  - Home the Zero Trust findings in `docs/guides/tools/cloudflare-tokens.md` or a sibling guide: the accounts and teams, the read gaps and the team-name rule. Take their text from `git show fbe4ebb0:+/_WORK/ki/messages.md` in ki-principal, line 115.

  Run the repository's tests and audits. Inspect `chezmoi diff` read-only for the touched targets, and record that it was not applied. Commit each change by explicit path and push fast-forward. Disposition the three lines in ki.prj.chezmoi's decisions, and send one line to personal.reg.rig-sol's `messages.md` saying sol needs an attended `chezmoi apply` of the MCP scope. Read or print no secrets.

### U4 - Stoa import cycle and Phosphor icon mappings (STOA-ICONS)

- **Package / repository:** ki.reg.main / packages-stoa.
- **Authority:** STOA-ICONS a), Kris agreed on 29 October at 14:12 GMT: "one release fixing both" (relayed by ki.sop.main on 30 October).
- **Tier:** push to `main` only. The release itself is excluded and waits for Kris. **Waits on:** nothing. packages-stoa has no CI workflow, so a push does not publish. **Size:** M.
- **Brief:** In packages-stoa, in its own worktree, make two changes:
  - Remove the runtime import cycle between `packages/stoa/src/theme-engine/element.js` (line 5 imports `defineStoaSunDial`) and `sun-dial.js` (line 13 imports `solarScrub`) without changing either export's behaviour. For example, move `solarScrub` into a leaf module that both import.
  - Add Phosphor Duotone mappings in `src/icons/mapping.js` so that `renderIcon` renders all 46 names listed in ki.reg.main's STOA-ICONS line.

  Prove both with tests: a dependency-cruiser or import-graph check showing no cycle, and a render test over the 46 names. Run the repository's checks, then commit by explicit path and push fast-forward. Do not bump the version, tag, publish or change visibility. The repository is private and mentions HNR customers, so copy none of its content elsewhere. Leave a release-ready note in ki.reg.main's decisions and a line for Kris's return asking for the release go.

### U5 - `mgit sync` pushes only with `--push` (MGIT-PUSH-GUARD)

- **Package / repository:** ki.prj.tools-burndown / tools-mgit.
- **Authority:** MGIT-PUSH-GUARD, 25 October 01:04 GMT: "Kris adopted, after a blind review, 'sync pushes only with --push'".
- **Tier:** push, no release ("stop to ask me before any ki or mgit release", 16 October). **Waits on:** HOLD-SCOPE. **Size:** M.
- **Brief:** In tools-mgit, in its own worktree, capture the record if tools-mgit's roadmap requires one, as the line asks.
  - Change `mgit sync` so that by default it fetches and fast-forwards only. It reports ahead-only branches as "ahead N, not pushed (pass --push)". `mgit sync --push` publishes. `git config mgit.syncPush false` is a hard per-repository veto that neither `--push` nor `-i` overrides (`bin/mgit` around line 3130).
  - Update `sync_usage`, the zsh completion and the man page, and add a changelog line announcing the changed default.
  - Test the default no-push, explicit push, veto precedence, interactive mode and linked worktrees, in disposable repositories under the run's temporary folder.
  - Commit by explicit path and push fast-forward. Do not tag or release.

### U6 - `ki agent wait`: a bounded wait that loses no event (WAKE-SESSION, tools half)

- **Package / repository:** ki.prj.tools-burndown / tools-ki.
- **Authority:** WAKE-SESSION a), Kris, 30 October 2026: "exactly one detached waiter armed at a time, bounded at five minutes by the waiter ... no seen event is lost". LESSONS-TERRA (1), 31 October, sent under Kris's LEARN-LOOP: `--next` first returns older unseen events.
- **Tier:** push, no release. **Waits on:** U2 (same lane) and HOLD-SCOPE. **Size:** M.
- **Brief:** In tools-ki, after U2:
  - Add a `--timeout <seconds>` option to `ki agent wait`.
  - Make `--next` acknowledge an event only after it has been delivered to the caller, so that a waiter killed after the read loses nothing. For example, use a separate `ki agent ack`, or acknowledge at the next wait.
  - Scope `--next` so that it does not return stale events from runs older than the waiter's arming, or name them as stale.
  - Prove all of this with boundary tests that kill a waiter between read and acknowledgement. Record the result under both Claude Code and Codex in the record or test notes.
  - Commit and push fast-forward, then send a receipt line to ki.prj.tools-burndown.

### U7 - Shape HOOK-STASH as a reviewed query

- **Package / repository:** ki.prj.ways-of-working / ki-principal (this package only).
- **Authority:** This work's scope owns `ki-delegation` and the coordinator style. HOOK-STASH was returned to ki.sop.main on 30 October as "a cross-cutting delegation-rule question". Shaping a query adopts nothing.
- **Tier:** push. **Waits on:** nothing. **Size:** S.
- **Brief:**
  1. Read HOOK-STASH in ki.sop.main's `messages.md` and the plan069 exception: Kris's "a bounded exception, not a general change to the no-stash rule".
  2. Write the query HOOK-STASH, with Context, Query and unranked Options, in a brief for one masked blind review on Codex at high effort. The reviewer reads no `queries.md`, `decisions.md` or report, and may challenge the existing rule.
  3. Write the reviewed query into this package's `queries.md` with the review's verdict folded in.
  4. Disposition the SoP line with a pointer line in ki.sop.main's `messages.md`.

  Change no rule.

### U8 - Make the Finished-folder kick delete the folder (FINISHED-TIDY-KICK)

- **Package / repository:** ki.prj.ways-of-working / ki-principal `design/`, then ki-agentic-harness if one course is plainly within Kris's words.
- **Authority:** FINISHED-TIDY-KICK, relayed at Kris's request on 30 October: "Sort out the method so that the kick actually gets the folder deleted".
- **Tier:** push. **Waits on:** nothing. **Size:** S to M.
- **Brief:**
  1. Read `ki-coordination`'s Finishing Project work step 4 and the territory tidy step that today only names a flagged folder in its own `messages.md`.
  2. Write `design/finished-tidy-kick.md`. It covers the gap and the knowledge-acquisition case, plus one recommended mechanism with its confidence. Options include State of play deleting a Finished work's folder itself after checking the closing mark and that every decision is homed, or a rubric check that blocks State of play's own mark.
  3. If the recommendation is high confidence after a masked blind review, apply the standard change as in U1's review route. Otherwise, put it as a query.

  Do not delete `ki.prj.knowledge-acquisition`'s folder here, because its closure is the parked KA-CLOSE query in ki.sop.main.

### U9 - Rank diagram tools in `ki-diagrams` and `ki-authoring` (DIAGRAM-TOOLS)

- **Package / repository:** ki.reg.main / ki-agentic-harness.
- **Authority:** DIAGRAM-TOOLS, Kris, 29 October: "that should all [be] sent into authoring and diagramming skills ... I really like Archify. Stately might [be] pretty decent ... C4 ones, they're really good ... I love Isoflow as well". Also DIAGRAM-AGREED, Archify for the beautify step. ki.reg.main's hold release, "new regular work arriving", is met by the line itself.
- **Tier:** push. **Waits on:** U1 (same repository). **Size:** M.
- **Brief:** In ki-agentic-harness, after U1:
  - Add to `ki-diagrams` a per-diagram-kind preference order built only from Kris's stated likes: Archify first; Stately/XState, LikeC4 and Isoflow/FossFLOW liked; then Mermaid, D2/TALA, D3, Typst/fletcher and TikZ. SaaS tools (Ilograph, Eraser, IcePanel, Napkin) are inspiration only.
  - Add the sketch-in-Mermaid, beautify-in-Archify step. Note infoschematics as KI's own tool to grow.
  - In `ki-authoring`, note Typst as an authoring alternative while Markdown stays.
  - Mark Mermaid's place "pending re-evaluation on current rendering (state, Sankey)" rather than settling it.
  - Review, test and push as in U1, then disposition the line in ki.reg.main.

### U10 - Opener label and session name (OPENER-LABEL, THREAD-RENAME tools half)

- **Package / repository:** ki.prj.tools-burndown / tools-ki.
- **Authority:** OPENER-LABEL, Kris answered "Send it" on 25 October. THREAD-RENAME a), Kris, 25 October: "Name + rename line".
- **Tier:** push, no release. **Waits on:** U6 and HOLD-SCOPE. **Size:** S.
- **Brief:**
  - Change `src/core/work/prompts.ts` (line 43) so that each opener's Label line prints `<label> (<id>)`.
  - Make `ki agent prompts` openers launch with `claude --name "<label> (<id>)"`.
  - Add tests, commit and push fast-forward, then send receipt lines.

### U11 - `ki agent` launcher faults

- **Package / repository:** ki.prj.tools-burndown / tools-ki.
- **Authority:** CLOSE-CLEANS-UP, Kris, 25 October, PERM-PROMPTS-SCRATCH: "Close cleans up". LAUNCHER-FAULTS a), Kris, 27 October: KI takes the `ki agent` faults. RUN-CLOSE-PID and AGENT-SEND-NO-RUN are faults of that class.
- **Tier:** push, no release. **Waits on:** U10 and HOLD-SCOPE. **Size:** M.
- **Brief:** In tools-ki:
  - Make `ki agent close` empty and remove `$TMPDIR/ki-agents/<run>/<name>/`, and align the progress-protocol footer with harness `c4b423c7`.
  - Check process identity (start time or command) as well as the pid before treating a run as live.
  - Make `ki agent send` find any run that `ki agent status` lists, and make the run-name error name the existing run.
  - Close the four LAUNCHER-FAULTS items, or document them where they are intended: a never-run brief needing `--relaunch`, a DONE run showing "EXITED WITHOUT DONE", unhomed reports blocking sync, and the undocumented `ki agent dequeue`.

  Write one test per fault, then commit and push fast-forward.

### U12 - Capture model design (CAPTURE-MODEL, strands 1 and 2)

- **Package / repository:** ki.prj.ways-of-working / ki-principal `design/`. The Acquire repository is read only.
- **Authority:** CAPTURE-MODEL, relayed at Kris's request on 30 October: "Kris wants Ways of working to take over improving the capture model now".
- **Tier:** push, this package only. **Waits on:** nothing. **Size:** M.
- **Brief:** Under `ki-work-design`, write the brief stage `design/capture-model/brief.md`:
  - **Purpose at capture:** every captured point tagged with a purpose (buy, consider, design digest and so on), with open items managed properly. The OneDrive intent folders are one source of purpose, not the mechanism.
  - **Where an idea lives and moves on:** ideas stay out of the roadmap.
  - **The succinct-capture rule** for `CAPTURE.md`.

  Use the source digests the line names, reading them in place. Recommend with confidence, and leave every choice for Kris. Do not edit Acquire's `CAPTURE.md`, which is excluded below.

### U13 - Orca preferences declaration and checker design (ORCA-PREFS)

- **Package / repository:** ki.prj.chezmoi / ki-principal package `design/`.
- **Authority:** ORCA-PREFS, Kris's ORCA-CONFIG-SCOPE a), amended, 31 October: read Orca's settings "on both and looking for differences and then flagging that up ... we still put it in the dot files somewhere".
- **Tier:** push, design only. **Waits on:** nothing. **Size:** M.
- **Brief:** From the survey `personal-principal +/_WORK/personal.reg.rig-terra/orca-config.report.md` and a read-only, copy-free inspection of sol's own Orca profile schema (never written, never opened for write, and no SSH to terra), design:
  - a dotfiles declaration of Orca preferences, split into shared and per-host values;
  - a read-only checker that flags differences between terra and sol.

  Write it to `+/_WORK/ki.prj.chezmoi/design/orca-prefs.md`, with recommendations and confidence. Build nothing.

### U14 - Package queue receipts in this work

- **Package / repository:** ki.prj.ways-of-working / ki-principal (this package).
- **Authority:** ORCA-ROUTING, Kris chose a machine-local runtime routing record (relayed 31 October). LESSONS-TERRA, sent under Kris's LEARN-LOOP.
- **Tier:** push. **Waits on:** nothing. **Size:** S.
- **Brief:**
  - Fold ORCA-ROUTING's decided shape into [the Orca sub-agents design](../orca-subagents/design.md) as a settled input: keyed by `<repository>/<work id>`, no Run id in package files, and `messages.md` as the durable channel.
  - Route LESSONS-TERRA (1) into U6's brief.
  - Note that (2) is already in the brief guidance and that (3) stays with Kris in chezmoi.
  - Leave RESTART-SUGGEST-LANDED for Kris's review, and CAPTURE-MODEL and FINISHED-TIDY-KICK to U12 and U8.
  - Disposition each line in `decisions.md` and remove it in the naming commit.

### U15 - Captures Kris asked for in tools-ki

- **Package / repository:** ki.prj.tools-burndown / tools-ki `docs/roadmap/`.
- **Authority:**
  - AGENT-HOME a), 30 October: "Please capture the record".
  - WORKTREE-OPTOUT a), 30 October: "Please capture those as tools-ki records".
  - CLI-BOOTSTRAP, Kris's PKG-HELD-WORK a), 24 October: "please capture as tools-ki work".
  - The state machine rollout plan's U2, report-home compatibility, which the plan says may "be planned now" by its receiving owner.
- **Tier:** push. Capture only, unadopted triage, under `ki-next`. **Waits on:** U11 and HOLD-SCOPE. **Size:** S.
- **Brief:** Capture these as unadopted triage records, each quoting its owner words and linking the landscape report rows:
  - one AGENT-HOME record: design the separation of `decide`, `reconcile`, `home` and `prompts` command by command;
  - four WORKTREE-OPTOUT prerequisite records: registry resolution of linked worktrees, worktree base from committed `main`, package anchoring to the primary checkout, and a tested skills-and-dependencies check;
  - one CLI-BOOTSTRAP record;
  - one report-home compatibility record from [the state machine rollout plan](../state-machine-rollout-plan.md).

  Adopt, size-promote or plan none of them. Commit and push fast-forward. The AGENT-HOME follow-up is due on 2 November.

### U16 - Two harness records Kris asked for (PRODUCT-RECORDS)

- **Package / repository:** ki.prj.baseline-rollout / ki-agentic-harness `docs/roadmap/`.
- **Authority:** VA-HIGH a), Kris, 25 October, read back as "one bounded run captures harness records for Always Use HTTPS on by default for own-domain Cloudflare zones and the FILES-6 `node_modules` symlink gap".
- **Tier:** push, capture only. **Waits on:** U9 (same repository) and HOLD-SCOPE. **Size:** S.
- **Brief:** Capture the two unadopted triage records in ki-agentic-harness, quoting VA-HIGH and linking the detail at ki-principal `fbe4ebb0` `+/_WORK/ki/messages.md` lines 79 and 81. Commit and push fast-forward, then send a receipt line to ki.prj.baseline-rollout.

### U17 - `mgit pull` carries on past a bad checkout, and the MGIT-AUTO idea

- **Package / repository:** ki.prj.tools-burndown / tools-mgit.
- **Authority:** MGIT-TOLERANT, under RESTART-ON-SOL, 25 October, a defect seen failing. MGIT-AUTO a), Kris, 27 October: "asks for a tools-mgit idea".
- **Tier:** push, no release. **Waits on:** U5 and HOLD-SCOPE. **Size:** S to M.
- **Brief:** Make `mgit pull` report an unsafe or missing repository path and carry on with the rest, with a non-zero exit summarising the skips. Test it in disposable repositories. Add the MGIT-AUTO idea to tools-mgit's `_IDEAS.md`: `sync --merge`, `--exclude <prefix>`, and `--json` with reason codes; never force, stash or touch uncommitted files. Commit and push fast-forward.

### U18 - One verification pass per unchanged tree (VERIFY-ONCE)

- **Package / repository:** ki.prj.tools-burndown / tools-ki.
- **Authority:** VERIFY-ONCE, 27 October: "Kris explicitly requests avoiding repeated verification".
- **Tier:** push. **Waits on:** U15 and HOLD-SCOPE. **Size:** M.
- **Brief:** Map the overlapping checks in tools-ki's verify and audit paths. CLI-160 ran coverage standalone and again inside `ki repo audit`. Make one aggregate pass sufficient for the same unchanged tree, keeping every required gate and its evidence. Prove that a gate failure still fails. Commit and push fast-forward.

### U19 - Align hook tests with check-only hooks (HOOKS-CHECK-ONLY, no release)

- **Package / repository:** ki.prj.tools-burndown / tools-ki.
- **Authority:** COMMIT-VS-CI a), as routed in HOOKS-CHECK-ONLY on 26 October.
- **Tier:** push. The release that rolls the hooks out is excluded. **Waits on:** U18 and HOLD-SCOPE. **Size:** S to M.
- **Brief:** Align `src/tests/cli/repo/canonical-hooks.test.ts`, `hooks.test.ts`, `estate/hooks.test.ts` and the lint-staged rendering in `src/core/repository/operations/conform.ts` with harness `d174adbc`: check-only, with no `--write` or `--fix`. Commit and push fast-forward. Leave a line asking Kris for the release go.

### U20 - `ki work opener <id>` (WORK-OPENER)

- **Package / repository:** ki.prj.tools-burndown / tools-ki.
- **Authority:** WORK-OPENER, 21 October: "Kris wants `ki work opener <id>` to print the ki-coordination opener for a work".
- **Tier:** push, no release. **Waits on:** U19 and HOLD-SCOPE. **Size:** M.
- **Brief:** Implement `ki work opener <id>`:
  - It fills the coordination standard's single opener template from the package (label, package path, Capital checkout, run), choosing by state among opener, re-bootstrap, send line and resume line.
  - It adds a launch command that starts in the Capital checkout.
  - Reuse `prompts.ts` rather than copying the template, and add tests.
  - Commit and push fast-forward, then send a receipt line to ki.prj.observatory for its button.

### U21 - Two decided agent-host recipe changes (VEGA-XDG, TS-OAUTH-PARAM)

- **Package / repository:** ki.prj.agent-host / ki-techne-harness.
- **Authority:** VEGA-XDG a), ki.prj.chezmoi Decision 158, 20 October. TS-OAUTH-PARAM, tools-techne's delivered field, 20 October, within the Techne Programme Focus.
- **Tier:** push. No provisioning, and nothing run on `vega`. **Waits on:** HOLD-SCOPE. **Size:** S.
- **Brief:**
  - Add the four unset-only XDG defaults to the harness's `env.sh` in the `: "${X:=$HOME/...}"` form.
  - Add an optional `[parameters.tailscale_oauth_item]` to the agent-host recipe, with `env = "AGENT_HOST_TAILSCALE_OAUTH_ITEM"` and `scripts = ["provision", "destroy"]`, and a sentence in the operator guide's Key minting section.
  - Read no secret. Run the repository's checks, then commit and push fast-forward.
  - VEGA-RIG-LINK is excluded below.

### U22 - Open the Stoa Project package (STOA-HOME)

- **Package / repository:** ki.sop.main / ki-principal.
- **Authority:** STOA-HOME, 31 October: "Kris chose to split hnr.prj.portal-framework: the Stoa work moves to Knowledge Islands ... Please open a Stoa Project".
- **Tier:** push. **Waits on:** nothing, but run it after U4, so that U4's release line can move into the new package. **Size:** S.
- **Brief:** Following `ki-work-package` entry points:
  - Create the minimal five-file package `+/_WORK/ki.prj.stoa/`, on hold until Kris opens it.
  - Create its Project note in `Streams/Projects/`, under the theme the registry gives packages-stoa, and add the registry line.
  - Queue STOA-HOME and the STOA-ICONS release-go line in its `messages.md`.
  - Disposition STOA-HOME in ki.sop.main.

  Open nothing beyond the seed.

### U23 - Answer the canonical report question (CANONICAL-REPORT-RESOLUTION)

- **Package / repository:** ki.prj.tools-burndown, read-only in tools-ki, with a reply line in ki.prj.observatory's `messages.md`.
- **Authority:** The 29 October line asks only "Please name existing command/schema and refusal semantics, or confirm none exists. ... no record or implementation requested".
- **Tier:** read-only, plus one queue line. **Waits on:** HOLD-SCOPE. It writes no tools-ki file, so it may run outside the T lane. **Size:** S.
- **Brief:** Search tools-ki for a supported public command and schema that resolves a repository-scoped historical or typed work ID to its one canonical report home, refusing ambiguity. Answer with the command, schema and refusal semantics, or confirm that none exists, as one line in ki.prj.observatory's `messages.md`.

### U24 - ki-design adopts `ki-specs` (ROUTE-1)

- **Package / repository:** ki.prj.observatory / ki-design.
- **Authority:** ROUTE-1, "taken under the 27 October bulk reading for ki-design ... Please deliver".
- **Tier:** push. **Waits on:** HOLD-SCOPE. ki.prj.observatory is with Kris under DRAIN-WITH-SUPERVISOR. **Size:** S.
- **Brief:** In ki-design, in one run:
  - Rename `docs/spec/` to `docs/specs/`.
  - Add `ki-specs` front matter to each specification and repoint every link.
  - Leave the two hex-terrain proposals as drafts.
  - Run the repository's audits, then commit and push fast-forward.

## Excluded units

### Open queries: no option is adopted by the grant

- **ki.prj.ways-of-working:**
  - The 25 open queries: WORKER-WAIT-*, HOST-*, PUBLIC-REPORT-*, AMEND-RACE, ORCH-NAME-*, LAYOUT-*, REVIEW-CHALLENGE, REVIEW-LIFT, READ-FEEDBACK-NOW, ORCA-CLOSE-OUT, ORCA-SUBAGENT-PILOT, ORCA-PLACEMENT, ORCA-QUEUE and WAKE-HOST.
  - Delivery of the state machine contract (rollout plan U1, U3 to U5). It overlaps LAYOUT-*, WORKER-WAIT and ORCH-NAME, and the plan itself requires a record selected by its owner. U15 captures only the tools-side record.
  - The REVIEW-INDEPENDENCE standard text, until REVIEW-CHALLENGE and REVIEW-LIFT are answered.
- **ki.prj.orca-evaluation:** TRIAL-UNITS, TRIAL-PUBLISH, TRIAL-ASK, TRIAL-PRACTICE, NEST-TRIAL, NEST-FR, ORCA-IDENTITY-LEAK, ORCA-SIDEBAR-FR and LABEL-FIRST.
- **ki.prj.mac-studio-setup:** RIG-INTAKE, which governs RIG-TUI, RIG-SSH-CHECK, RIG-COMMENT-KIND, RIG-CLI-CONSISTENCY, RIG-APP-FOOTPRINT, both RIG-NOTIFICATIONS lines, RIG-MACHINE-MANAGEMENT, WAKE-SUBSTRATE and RIG-REMINDER-DOCTOR. Also RIG-069-PROBE and the parked queries.
- **ki.prj.observatory:** its nine open queries.
- **ki.sop.main:** CHAIN-QUIET, CHAIN-START-*, MAIL-ASKS (with CORR-GUARD-ASK, whose owner MAIL-MCP-HOME leaves undecided), ACCESS-ADMINS-ROUTE, OBSOLETE-DROP, OLD-ORPHANS and ADOBE-SCRIPT-HOME.
- **ki.prj.tools-burndown:** SYNC-RECIPE, which waits on `mgit chain`'s acceptance and the CHAIN-* queries. REPO-ORDER and AGENT-AUDIT-ROOTS, which are questions to settle. GATE-BASELINE-SIBLING, a proposal with no decision. HELD-ROADMAP-KNIP and ASK-B, which are parked. TAKE-STOCK, CLI-DEPARTURES, CAPTURE-FOLLOWUPS, WORKTREE-FIXES and BRING-UP-LEFTOVER, which are still pending decisions.
- **ki.prj.portable-specifications:** SPEC-TEXT and HOMING-EDITS, which are parked.
- **ki.prj.timelines:** OVERNIGHT-CONFIRM and CAPTURE-ADOPTION.
- **ki.prj.chezmoi:** its four open queries. TRUST-COMPLETE's Decision Record and SYNC-RECONCILE were not checked against those queries, so they are not shown to be unblocked.

### Acceptance, closure or pruning

- **ki.sop.main:** ACCEPT-KI-TOOL-RIG-CORE-070, ACCEPT-PERSONAL-DOTFILES-UE-106, ACCEPT-KI-TOOL-MGIT-CLI-032 and every parked ACCEPT-* query.
- **Closure:** ESTATE-CLOSE (ki.prj.estate-factorisation) and KA-CLOSE. KA-CLOSE includes deleting `ki.prj.knowledge-acquisition`'s folder, although CAPTURE-MODEL relays that Kris wants it cleaned up; it is parked in ki.sop.main.
- **Kris's review:** RESTART-SUGGEST-LANDED, which was sent "for your review".

### Deploy, release, installation or publication

- Every `ki` and `mgit` release, including gfmconv's converter, hooksv2's wave grant, the HOOKS-CHECK-ONLY release and the STOA-ICONS release.
- SITE-DEPS in ki.prj.website: it adopts dependencies through a package-registry install, and the package is unopened.
- STOA-PUBLIC: making packages-stoa public is a visibility change over HNR-confidential content and needs Kris's go.
- Website publication. The `website-learn` unit is already planned as commit only.

### Credentials, providers or connection-critical changes

- BUILDS-TOKEN-PATH in chezmoi: a token selector, whose testing needs live token reads, and Kris creates the tokens.
- ACCESS-ADMINS for the website and the Observatory: Cloudflare Access, which is provider and connection-critical.
- GH-LIVE for ki-design: a GitHub settings call.
- CI-PIN-RECEIVER: GitHub App installation per repository, and an estate-wide write better done attended.
- SITE-RENAME: a repository rename at the provider.

### Environment, scheduler or remote host changes

- TRIAGE-HOURS-APPLY: `rig apply` on terra.
- MCP-PROCS: a process inspection on terra.
- VEGA-RIG-LINK: relinking on `vega`.
- WAKE-SUBSTRATE, DISPATCHER, TRIAGE-HOURS and MGIT-SYNC-JOB in chezmoi: scheduler design that waits on WAKE-HOST and the Observatory's SYNC-DIRECTION.
- MANAGED-COVERAGE: waits on terra's findings.
- Every attended item at sol's or terra's screen in ki.prj.mac-studio-setup and ki.prj.chezmoi.

### Orca workers or outward Orca requests

- **Orca dispatch:** ki.prj.orca-evaluation's trial units, the Orca half of WAKE-SESSION, and the homing of ORCA-DISPATCH-LEARNINGS. ORCA-OPTIN b) requires every new unit there to go through Orca.
- **Outward requests:** ORCA-REMOTE-VIEW and ORCA-SETTINGS-READ, which are outward-facing requests or remote-host work.
- **Not due:** the ORCA-REACH follow-up, due on 6 November.

### Holds that stand on their own terms

- **ki.prj.paperclip-capture-and-rebuild:** PAPERCLIP-OUT triage. The hold stands under the Techne Programme Focus, and the line asks for no action.
- **ki.prj.portable-specifications:** the whole work.
- **ki.prj.timelines:** rollout steps 2 to 4.
- **ki.prj.agent-host:** the `vega` host name in `status.sh`.
- **ki.prj.baseline-rollout:**
  - HARNESS-DEFECTS, WEBSITE-SKILL, REPO-METADATA, REPO-CODE-CAP, HARNESS-FEEDBACK, HARNESS-FEEDBACK-2, SITE-STD-GAPS and SPA-FALLBACK-SCOPE: harness-owner proposals with no owner decision on their content.
  - TYPED-ID-ROLLOUT: receiver-owned, after the core readers.
  - The rollout's own LEDGER-FORM, SIZE-KIND and conform passes: they wait on Kris's go per repository and on tools-burndown lifting the conform guard.
- **ki.prj.website:** WEBSITE-DRIFT, because the package is unopened and the line carries no owner decision on content.
- **ki.prj.observatory:** VIS-SIZES, ROADMAP-AUDIT and its other design asks, under DRAIN-WITH-SUPERVISOR.
- **ki.prj.tools-burndown, lower value beyond the window:**
  - WORK-MODEL alignment, AGENT-SCOPE, RUNHOME-RENAME and HOOK-PAYLOAD. Each is size L and is better planned attended.
  - PIN: the CI guide may need a query about `$KI_VERSION`.
  - BOOT-HOME: "consider a later `ki doctor` check", with no request to build it.
  - WORK-TIDY and WOW-TIDY-NIGHT: package tidies for the steward when it resumes.

### Other Capitals or HNR

- Revising Acquire's `CAPTURE.md` (CAPTURE-MODEL strand 3): Personal's repository, so it follows U12's design for Kris's go.
- The consumer side of HNR's Stoa re-vendor: HNR source.
