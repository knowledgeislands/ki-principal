# Decisions

## 2026-10-09 - Project closures deferred

- Kris deferred Project closures until acquire-ChatGPT knowledge items are checked against them.

## 2026-10-09 - Website records held

- Kris: Keep KI-WEB-SITE-001 and KI-WEB-SITE-039 on hold.

## 2026-10-09 - Projects and roadmap count

- Kris wants everything captured in Projects/threads, ideally as ideas or roadmap items, and the roadmap count brought down.

## 2026-10-09 - PRFLOW

- PRFLOW: Kris chose (a) - background agents keep pushing directly to harness main through the admin bypass, after tests and audit.
- 2026-10-10: PRFLOW reconfirmed: push directly to ki-agentic-harness main.

## 2026-10-09 - PIN

- PIN: Kris chose (a) - tools-ki CI builds ki from its own source instead of taking a pin; KI-HARNESS-GOV-168 excludes tools-ki.

## 2026-10-09 - STATE retention rule

- STATE: Kris approved (1) a run-folder retention rule in ki-delegation, parked with the ways-of-working Project

## 2026-10-11 - macOS defaults split parked

- Kris (2026-10-11): Parked: splitting macOS defaults out of Rig (not now).

## 2026-10-12 - DESIGN-SYSTEM

- Kris, 2026-10-12 05:40 BST: DESIGN-SYSTEM approved - roll ki-design-system out to every apps-* repository (website and app repos). Read-only assessment now; changes land after the step 9 renames so no agent works in a folder that is moving.
- Kris, 2026-10-12 05:58 BST: DESIGN-SYSTEM - Techmedix sites wait until adopted; kris.me.uk gets full conformance; midnight.ninja holds three sites (apex, rig, tower) and Kris is minded to split it.

## 2026-10-12 - SPEC-REVIEW and KI-RELEASE order

- Kris, 2026-10-12 06:45 BST: SPEC-REVIEW starts only once the known Knowledge Islands roadmap records are near zero. KI-RELEASE (ki and mgit) yes, after their roadmaps reach zero. Drive the Knowledge Islands roadmaps towards zero first.

## 2026-10-12 - Other territories parked

- Kris, 2026-10-12 ~19:50 BST: only Personal and Valle Armonia masters running among other territories; keep others parked until Knowledge Islands is bottomed out, then Paperclip helps.

## 2026-10-14 - Roadmap burn-down focus

- Kris 2026-10-14: roadmap has grown ~50% since last measured. Standing focus: burn the roadmap down; no new feature records. Capture only blockers, defects or Kris-requested items; prefer closing, merging or rejecting. Applies to every Knowledge Islands thread and every agent brief. Also: stay available and delegate everything.

## 2026-10-14 - RIG-REL-PATCH and capture landing

- Kris 2026-10-14 morning: RIG-REL-PATCH accepted; follow-up releases stop and ask first from now on.
- Kris 2026-10-14 morning: Kris wants: always land the information even if imperfect (uncertain territory goes to a triage territory), record the agentic system's session or thread ID in front matter

## 2026-10-14 - ROADMAP-SIZING

- Kris 2026-10-14: ROADMAP-SIZING agreed: one design record to ways-of-working; daily count snapshots first, sizing and ID allocation after.

## 2026-10-14 - ROUTE-LOCAL

- ROUTE-LOCAL (Kris, 14 Oct, pasted from acquire-intake): act on the prepared Master message. Coordinate receiving ownership of KB-ACQUIRE-002 and KB-ACQUIRE-003 with knowledge-acquisition, and return the proposed MCP home, hosting and concrete first-probe scope for review before implementation. Review only: no records, repositories, code, migration, credentials, live tests, deployment or push.

## 2026-10-14 - Model fallback

- Kris, 2026-10-14 21:2x BST: we hit a limit on fable. If any of our threads get stuck, change them to claude-opus-5-5 at their same effort, at least until the next reset.

## 2026-10-14 - GRANOLA-SUPPORT, BINARY-HOME and ACQ-FOCUS

- Kris, 2026-10-14 ~21:40 BST, replies to the re-bootstrap report. GRANOLA-SUPPORT: adopt KI-TOOL-KI-CLI-128 as the tools-ki half and create only the harness record; local delivery; migration separately gated.
- Kris, 2026-10-14 ~21:40 BST, replies to the re-bootstrap report. BINARY-HOME: iPhone check first, then the private mcp-acquire-chatgpt repo and local synthetic build; 'a candidate that should be handed off to the Knowledge Acquisition project/thread'.
- Kris, 2026-10-14 ~21:40 BST, replies to the re-bootstrap report. ACQ-FOCUS: adopt as delivery priority (mac-studio-bootstrap and agent-host first; hold unchanged; policy wording only when asked).

## 2026-10-15 - SEAT-RECORD host binding

- SEAT-RECORD (Kris, 2026-10-15): '... A message to Rig: chezmoi asks it to bind home to terra and hub to sol in host data.'

## 2026-10-15 - FW-DECLARE

- Kris, 2026-10-15, FW-DECLARE: "The Rig: chezmoi thread commits the firewall declaration as conf.d/private_45-firewall.toml with profiles = [\"laptop\"], and does not apply chezmoi on sol until sol's Rig is 0.6.0 or later; then give me the terra steps."

## 2026-10-15 - FW-ADR

- Kris, 2026-10-15, FW-ADR: "On a pass, the acceptance run accepts KI-TOOL-RIG-CORE-047 and marks both ADR-KI-TOOL-RIG-009 and ADR-KI-TOOL-RIG-010 accepted."

## 2026-10-16 - FW-DECLARE-NOW and SSH-SPARE-KEY

- FW-DECLARE-NOW: "Rig: chezmoi commits the FW-DECLARE firewall declaration (dot_config/rig/conf.d/private_45-firewall.toml, profiles = ["laptop"]) as its first step; no chezmoi apply on sol until sol's Rig is 0.6.0 or later; then give me the terra steps for KI-TOOL-RIG-CORE-047."
- SSH-SPARE-KEY: "Both Macs are always within physical reach, so the console is the restore path: no spare key is needed, and Rig: chezmoi notes the console fallback in the chezmoi macOS workstation guide before key-only SSH applies on terra."

## 2026-10-17 - Kris's intake dump, items not yet homed

Kris: "I've now destroyed all my notes about it" - this log is the durable capture until each item reaches its owning thread.

- **MGIT-ESCAPE** (tools burndown, tools-mgit): "we could do with better output from mgit. A lot of the commands in mgit are effectively pass-throughs ... anything which I create at the mgit level overrides the pass-through ... There should be some kind of escape hatch". Proposed: `--bare` runs the git subcommand in each child bypassing mgit's own command; `--raw` (rather than `-B`) runs any command as a shell in each repository directory; mind clashes with the physical and follow-symlinks options. "Git has got work tree. We've got mgit work tree, so it'd be nice to have an escape hatch".
- **MGIT-OUTPUT** (tools-mgit): "I really want MGIT to have much better output ... if I do MGIT status over the entire estate, because there's like 50 projects, it scrolls off the screen ... I really, really want this kind of idea of it giving me a progress bar ... and then it gives me the results at the end ... anything which has got no changes, it doesn't tell me about it, it only tells me ... the ones that have changed ... sync could be the way to try that out first ... if it pulls and it gets a rebase or a merge warning, it should effectively automatically abort that and give me a warning instead ... some of this might be better off done as like we did with the Git Almanac, so we can put some code behind it". References: the Claude Code terminal UI ("a little windowing toolkit within a prompt"), Omarchy (DHH's Arch distro).
- **MGIT-ESCAPE** (part 1) restated: bare and raw modes let "commands that I wrap over the top of existing ones".
- **GIT-SURFACE**: "we should think about how we document the entire Git work surface ... Not just Git and Git Almanac ... Git is like this kind of tool of decentralized knowledge ... durable knowledge ... the ability to go back and see what changed over history ... we can choose to condense history."
- **TOML-OPENER**: ".toml files are currently opening up in [Warp], and I don't want that. I'd rather they opened up in [Zed] ... I think it must have some kind of default opener on it."
- **MAC-CLOUD** (Rig, long term): "can we build a Mac on AWS EC2? ... a service that offers a Mac mini in the cloud and I can ... install myself onto it and then more and more so I become a dumb terminal towards that ... that's more long term, and that's definitely rig-focused for the future".
- **CAPTURE-ONLY**: "I don't want you to start spinning out loads of designs from this. The whole thing here is to capture everything ... and then we can go through a prioritization phase". "I don't want them to go into intake ... these can become part of this ideas of stuff".
- **DIAGRAMS-BLACK** (2026-10-17 14:10 BST): "the preview and markdown for the themes.md is largely speaking black diagrams. I can see some kind of faint things on it, but whatever you're doing to render those, it's not looking right." Screenshot: dark frames and boxes on a black canvas, no legible text.

## 2026-10-17 14:20 BST - replies to the 14:02 BST summary

- **AWAITING-REVIEW:** "Clear the backlog one repository group at a time through ki-accept: tools burndown presents KI-TOOL-KI-CLI-126, -130, -133, -141 and KI-TOOL-MGIT-CLI-017 after the tools-ki push; ways of working presents KI-HARNESS-GOV-195, -198, -203 and KI-HARNESS-OPS-005; knowledge acquisition presents KI-PRINCIPAL-MOD-006; the five personal records wait for the personal master thread; the owning threads prune KI-PRINCIPAL-ECO-014 and KI-TOOL-RIG-CORE-059."
- **KI-AGENTS-NAME:** "Keep "agents"; ways of working logs the decision in its decisions log and nothing is renamed."
- **GO-AHEAD** (2026-10-17 14:22 BST): "hopefully, all this gets captured back into Knowledge Island in the Knowledge Base, and then there's the observatory's built, we can start to look at and understand all these in a reader-only fashion. Not everything that we do needs to be in the public set of information on the website. Although, of course, much of this would be. So, you've got permission to get on with anything."

## 2026-10-18 01:12 BST - PILOT-SEED

- **PILOT-SEED:** "At the next state-of-play session with the terra checkout, after a fetch, copy section 4 of foundations-coherence.report.md into +/_THREADS/state-of-play/pilot-seed.md with a provenance line, push it and tell knowledge acquisition through its Messages block."

## 2026-10-19 18:58 BST - SEND-BACK

- **SEND-BACK:** "Send KI > SoP back to its worker in /Users/krisbrown/workspaces/knowledge-islands/ki-principal under current ki-coordination and ki-delegation since 2026-10-15T15:14:39Z: re-read the work package, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner." Taken on sol; mark struck at 18:58 BST.
- Messages: FIRST-STEP dispatched as `sop-mark` (check description, Goals and Scope against `ki-work-package`, set `method_read`). REPORT-SWEEP: sop-restock received, its four queries already in queries.md and its outcome homed in state.md, so the report is pruned; pilot-seed kept until PILOT-SEED-HOME is answered and a terra session homes it. REVIEW-HOLD, five items in ki-principal and one in ki-agentic-harness: dispatched `review-hold` for a live-or-dead recommendation each, to be raised as one query. All four lines removed.
- PILOT-SEED-HOME, LIVE-MAN-SWITCH, THREADS-CHECKINS and RIG-FULLSCREEN put back as open; their release was Kris's answer.
- Mark: the decisions strike is dispatched as `sop-mark`.

## 2026-10-19 19:40 BST - REFRESH

- Ways of working's IMPORTANT REFRESH line (QUERY-REVIEW in the ki-coordination standard; REFRESH-RESUMMARY, Kris 19 October: "I want the other threads to pick it up and resummary me so that I get the better recommendations") is acted on: `query-review` dispatched under Codex at high effort as one blind review of the six medium-confidence queries (REVIEW-HOLD, HOMELESS-STANDING, MODEL-FALLBACK, PILOT-SEED-HOME, THREADS-CHECKINS, RIG-FULLSCREEN); CHEZMOI-CARRY and LIVE-MAN-SWITCH are high and not destructive. A fresh Summary follows its report. Line removed.
- 19:45 BST: `query-review-2` received. Agrees on REVIEW-HOLD, PILOT-SEED-HOME and RIG-FULLSCREEN; disagrees on HOMELESS-STANDING, MODEL-FALLBACK and THREADS-CHECKINS. queries.md carries the reviewed queries. Limitation: the run read queries.md and the review-hold report, so it saw the recommendations and was not fully blind.

## 2026-10-19 23:08 BST - ROADMAP-GROWTH

- **ROADMAP-GROWTH:** "the roadmap keep growing, I need to get this sorted, help me get there". Taken as: measure the territory's roadmaps and their inflow and closure, diagnose the growth, and bring Kris a burn-down plan with a few decisions. Dispatched `roadmap-census`, read-only; no record is changed until Kris decides.

## 2026-10-19 23:09 BST - HIGH-CONFIDENCE

- **HIGH-CONFIDENCE:** "do high confidence recommenations". Read back as taken: option a) on the four queries whose recommendation is high confidence:
  - CHEZMOI-CARRY a): route line sent to ki.chezmoi's messages.md; strike the five here once its package carries them.
  - PILOT-SEED-HOME a): the terra session stages section 4 as a seed pack in `-` under SEED-HOME with a provenance line and tells knowledge acquisition in one messages line.
  - LIVE-MAN-SWITCH a): dispatched `live-man-switch` to capture the idea in the Host network Project's Notes as a design input for the firewall and key-only SSH rollouts.
  - RIG-FULLSCREEN a): route line sent to ki.mac-studio-setup's messages.md, idea only.
- Still with Kris: REVIEW-HOLD, HOMELESS-STANDING, MODEL-FALLBACK, THREADS-CHECKINS (medium).

## 2026-10-19 23:11 BST - MESSAGES

- `live-man-switch` added the idea to Host network but its commit was refused: Project notes may not name work records (STREAM-9). Relaunched as `live-man-switch-2` to drop the pruned record reference and commit.
- MCPORTER-LEAK (from Rig: chezmoi): dispatched `mcporter-route` to find the owning work and route it there.
- METHOD-READ (ways of working): `method_read` set to harness `84b61942`.
- AUDIT-CONFORMANCE (tools burndown, Kris's words): the estate-wide audit and conformance review of skills is placed after the roadmap burn-down, in state.md; hooks checks stay with ki.tools-burndown.
- TECHNE-FOCUS (Acquire intake, Kris's 14 October words): drafted as a query, held for blind review with the census queries.
- HOLD-POINTERS (ways of working): seven items carried in state.md.
- All five lines removed.

## 2026-10-19 23:14 BST - ACCEPT-AWAITING

- **ACCEPT-AWAITING:** "I think we should accept all the awaiting reviews." Read back as taken: accept as done, under `ki-accept`, every work record in Awaiting review across the Knowledge Islands territory's repositories, Kris's approval standing for each; no pruning and no push. A record that another session is changing is not touched but routed to its owning work. Dispatched `accept-awaiting`.
- 23:17 BST: ki.chezmoi carries FW-DECLARE, FW-DECLARE-NOW, SSH-SPARE-KEY, SEAT-RECORD and TOML-OPENER in its own decisions log; strike them here at the next mark (CHEZMOI-CARRY closed). Line removed.
