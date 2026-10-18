# Decisions

Struck at the mark of 2026-10-18T18:09:07Z. Git history holds every struck entry; [historical-decisions.md](design/historical-decisions.md) keeps the 11 to 14 October log as evidence.

## Standing push and branch-delete authorities (16 October)

Kris, 16 October 01:05 BST: "stop to ask me before any ki or mgit release", and from Master: state-of-play: "Remote branch deletes and any ki or mgit release ask me first."

Kris, 16 October 21:40 BST, UNPUSHED-COMMITS: "Push ki-principal's 16 commits fast-forward now and at each resting point, other sessions' included". Standing: push ki-principal fast-forward at each resting point.

## One tools-ki writer (16 October)

OWNER-LANE a), taken under BURN-OVERNIGHT on 16 October: "tools-burndown runs the only tools-ki writer for all in-scope records; tell the ways-of-working and knowledge-acquisition threads through Messages from Master, and they keep priority and acceptance input."

## tools-ki deferred until ki 0.10.6 (18 October)

FIRST-STEP, the Ways of working hand-back of 04:02 BST, acted on at 18:10 BST: tools-ki is left alone until migrate-phase2b reports ki 0.10.6 here; the ki release and `.github/ki-version` bump are dropped from this work (Ways of working owns them); KI-TOOL-KI-CLI-127 joins the tools-ki ki-accept group.

## ACCEPT-PRUNE (18 October)

Kris, 18 October, relayed by Ways of working: "anything which is awaiting acceptance can be accepted, and then we can prune anything which is in a state of done". Read back as taken:

- tools-rig: accept KI-TOOL-RIG-CORE-060 on its recorded verification evidence, and prune it once Done. Other Rig work's records are left to their owners.
- tools-mgit and tools-git-almanac: accept each Awaiting review record whose verification evidence is recorded, list those without it, and prune the Done ones. KI-TOOL-MGIT-CLI-017, -024 and -025 are left to Ways of working.
- tools-ki: deferred until 0.10.6 has been released.
- MCP repositories: none is in this work's scope, so they are listed but not acted on (MCP-SCOPE).

## PRUNE-SWEPT (18 October)

Kris, 18 October 19:09 BST, "agreed with all the recommendations": `3a33d51` in tools-rig stands as the prune of KI-TOOL-RIG-CORE-060. This is an exception to the prune-only-commit rule, recorded here.

## MGIT-OVERTAKEN (18 October)

Kris, 18 October 19:09 BST, "agreed with all the recommendations": MGIT-PLAN and MGIT-REVIEW-LOWS are closed as overtaken by KI-TOOL-MGIT-CLI-020, -021, -022 and -025. This work keeps only the prune of the Done mgit records, KI-TOOL-MGIT-CLI-020, -021 and -022, keeping -017, -018 and -019 for Ways of working.

## RIG-TARGET-SPEED-LOAD (18 October)

Kris, 18 October 19:09 BST, "agreed with all the recommendations": Rig's configuration-load cost is left as it is, and no record is captured.

## KI-TOOL-KI-CLI-139 "Decision 55" deferral (18 October)

Kris, 18 October 03:55 BST: "we're in the process of moving some of the decisions around so that might be confusing to you." Read back as DECISION-55-CITATIONS: leave -139's citations while the decisions move; revisit after (source: hnr-principal 5g-emerge-phase3 decisions, SRC-TOOLING, 16 October).

## CONSUMER-MIGRATE (17 October)

Kris, 17 October: "Wait for the mgit release, then migrate the chezmoi dot_mgit.toml source and the live manifest together."

## DIGESTS-SCAFFOLD (17 October)

Kris, 17 October: "Keep -/_DIGESTS/ as the declared scaffold."

## Pointers

- HOST-WRITES (14 October): the replacement-policy investigation stays parked with Techne: agent-host; held in [ki.estate-factorisation](../../_WORK_REVIEW/ki.estate-factorisation/work.md).
- HOST-GUARDS (14 October): [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) stays on Hold, review on 12 November; the record carries it.
- FOOTER-GRANTS (16 October): separate `--allow fetch` and `--allow machine` grants; [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) carries it.

## Messages acted on at the mark (18 October)

PIN-DONE-LINKS, relayed by Ways of working at 19:30 BST: "Kris answered PRUNE-HELD a) on 18 October; these Done records are held only by local links, so at your next mark pin each link to the GitHub copy at the revision named, or delete the report if it is spent." Read back as taken: tools-ki, tools-rig and this work folder's roadmap-overview, mgit-diverge and mgit-prune reports pin their links; MGIT-PRUNE-LINKS is now held only by KI-TOOL-KI-CLI-140's link to KI-TOOL-MGIT-CLI-021, so the mgit prune follows the tools-ki pin.

CLI-DEPARTURES, relayed by Ways of working at 19:31 BST: "Kris answered CLI-DEPARTURES a) on 18 October. Add these departures from the ki-repo-tools command-line conventions (KI-HARNESS-GOV-218) to each tool's existing records and fix them at its next change." Read back as taken: the departures are recorded now on tools-mgit, tools-rig and tools-ki records; each fix waits for that tool's next change; `-f, --filter` stays excluded under CLI-F-FILTER.

tools-ki gate read as met: tools-ki shipped v0.11.3 (`4b2506f1`), past the ki 0.10.6 the deferral waited for, so ACCEPT-PRUNE for tools-ki and the ki-accept group restart at this mark.

## ROADMAP-DIAGNOSTICS (18 October)

Kris, 18 October 20:3x BST, pasting the estate roadmap overview's diagnostics: "Can you fix this while I review". Read back as taken: fix each diagnostic and warning at its source record, in apps-rig.midnight.ninja (KB-MIDNIGHT-RIG-SITE-001 horizon), personal-principal (KB-PRINCIPAL-002 to -034 theme or legacy initiative, not both; KB-PRINCIPAL-043 baseline_ref), er-principal (ER-PRINCIPAL-004 to -008 field `candidate`) and legal-principal (LGL-PRINCIPAL-EVD-001 to -004 and LGL-PRINCIPAL-OPS-018 field `priority`), committed locally and not pushed. apps-yorkphotosoc.org having no roadmap is reported, not acted on.

## All recommendations of the 20:29 Summary (18 October)

Kris, 18 October 20:31 BST: "go ahead with all the recommendations". Read back as taken:

- TKI-PRUNE-LINKS a): relaunch tki to pin every remaining local link to the 17 Done tools-ki records at `a22214ee`, in tools-ki, ki-agentic-harness and ki-principal work folders, then prune them in one prune-only commit.
- MGIT-PRUNE-PIN a): free KI-TOOL-MGIT-CLI-020, -021 and -022, then prune them in a prune-only commit. Their last holder, mgit-prune.report.md, is spent and deleted at this tidy, which PIN-DONE-LINKS allows.
- TOOLS-PUSH a): push tools-ki, tools-rig and tools-mgit fast-forward now, and each prune commit as it lands.
- UNCLEAR-REPORTS a): the open tags in cli-133, commit-thread, summary-reconcile, mgit-diverge and roadmap-overview close as overtaken; the five reports, and the spent mark-tidy and mgit-prune reports, are deleted; Git history keeps them.
