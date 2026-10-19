# Decisions

Struck at the mark of 2026-10-19T21:13:09Z. Git history holds every struck entry; [historical-decisions.md](design/historical-decisions.md) keeps the 11 to 14 October log as evidence.

## Standing push and branch-delete authorities (16 October)

Kris, 16 October 01:05 BST: "stop to ask me before any ki or mgit release", and from Master: state-of-play: "Remote branch deletes and any ki or mgit release ask me first."

Kris, 16 October 21:40 BST, UNPUSHED-COMMITS: "Push ki-principal's 16 commits fast-forward now and at each resting point, other sessions' included". Standing: push ki-principal fast-forward at each resting point.

## One tools-ki writer (16 October)

OWNER-LANE a), taken under BURN-OVERNIGHT on 16 October: "tools-burndown runs the only tools-ki writer for all in-scope records; tell the ways-of-working and knowledge-acquisition threads through Messages from Master, and they keep priority and acceptance input."

## RIG-TARGET-SPEED-LOAD (18 October)

Kris, 18 October 19:09 BST, "agreed with all the recommendations": Rig's configuration-load cost is left as it is, and no record is captured.

## KI-TOOL-KI-CLI-139 "Decision 55" deferral (18 October)

Kris, 18 October 03:55 BST: "we're in the process of moving some of the decisions around so that might be confusing to you." Read back as DECISION-55-CITATIONS: leave -139's citations while the decisions move; revisit after (source: hnr-principal 5g-emerge-phase3 decisions, SRC-TOOLING, 16 October).

## DIGESTS-SCAFFOLD (17 October)

Kris, 17 October: "Keep -/_DIGESTS/ as the declared scaffold."

## Pointers

- HOST-WRITES (14 October): the replacement-policy investigation stays parked with Techne: agent-host; held in [ki.estate-factorisation](../../_WORK_REVIEW/ki.estate-factorisation/work.md).
- HOST-GUARDS (14 October): [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) stays on Hold, review on 12 November; the record carries it.
- FOOTER-GRANTS (16 October): separate `--allow fetch` and `--allow machine` grants; [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) carries it.
- SIZE-PRIORITY (19 October): Kris, "work should have a size and a priority, even if its horizon isn't now or next"; handed to Ways of working through its Messages section, and Kris confirmed the handoff done on 19 October; [ki.ways-of-working](../ki.ways-of-working/work.md) carries it.
- RIG-SITE-001-POINTER a) (19 October): at Kris's acceptance of KB-MIDNIGHT-RIG-SITE-001, drop the bootstrap-guide pointer as overtaken by `c416154`.
- HIGH-CONFIDENCE (19 October), Kris: "do all high confidence items and then give me a summar about the reset. Take a mark". Still live: SITE-CONFIG-PREMISE a), tell the rig.midnight.ninja side the host columns would match today, shape provisional ([rig-site-reply](design/rig-site-reply.md)); ASK-B a), Ask B parked until the site side asks. KI-TOOL-KI-CLI-153 accepted and KI-TOOL-KI-CLI-156 captured carry the rest.
- CONSUMER-MIGRATE (17 October), Kris: "Wait for the mgit release, then migrate the chezmoi dot_mgit.toml source and the live manifest together." mgit v0.18.0 shipped on 19 October and [ki.chezmoi](../ki.chezmoi/work.md) carries it.
- RIG-SITE-CONFIG and RIG-OUTPUT-SCHEMA (19 October): carried by [KI-TOOL-RIG-CORE-065](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-065-resource-subject-links.md), [KI-TOOL-RIG-CORE-066](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-066-plan-managers-and-uv-prerequisite.md), [KI-TOOL-RIG-CORE-067](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md) and [KB-DOTFILES-UE-099](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-099-resource-subject-links-and-service-paths.md).
- MGIT-LEARN-UNATTENDED a) (19 October, "All recommended"): unattended learning stays impossible; a flag record only if a need comes up.
- GFM-CONVERTER (19 October): routed from ki.ways-of-working, Kris approved at 22:00 BST that tools-ki builds the GitHub-flavoured Markdown converter (GFM-ORDER a, GFM-LINK-FORM a) to the converter requirements in [gfm-migration](../ki.ways-of-working/design/gfm-migration.md); it blocks KI-PRINCIPAL-OPS-014. gfmconv builds it, local commits only; the release is ask-first, and ki.ways-of-working is told when it is out.

## Hooks (19 October)

HOOKS-STANDARD, Kris via ki.ways-of-working: "add an urgent message to it to standardise". This work owns the convention, the harness standard and rubric change, and the rollout through `ki repo`.

Kris, 21:34 BST: "NON-KI - 100% not included in this, only ki repos." Only repositories with `.ki.toml`.

Kris, 22:02 BST: "ok - I'm good with the recommendations, but one final thing on githooks, is there a recognised way of dealing with this in general?" GIT-HOOKS a): every KI repository keeps all hook content in a committed `.githooks`, bound by `core.hooksPath`; `prepare` sets the binding; Husky and `.husky` leave. HOOKS-CONVENTION and KB-AUDIT fall away.

Kris, 22:11 BST: "I agree with the recommendations. You may think though that perhaps given the usefulness of githooks that we should add some mechanical checks for this in the audit. I think that's actually a massive area that we need to go back and look at anyway, but that's probably something to pass up to the state of play." COMMIT-MSG a): `ki git check-message` for `.githooks/commit-msg`, pre-commit only until it ships. ROLLOUT-AUTHORITY a): one owner grant per wave, runs commit by explicit path locally, Kris pushes. HOOK-AUDIT: mechanical hooks checks join this work's rubric change. The estate-wide conformance audit went to State of play as AUDIT-CONFORMANCE.

Kris, 22:33 BST: "go with recommendations". WAVE-PLAN a): wave 1 granted, the pilot in ki-principal, tools-ki and va-principal, to run after the harness rule change (hookstd) and the tools-ki conform change (hookconf) land; runs commit locally by explicit path and Kris pushes; later waves come back to Kris one at a time.

- CLI161-TITLE (19 October, 22:51 BST): taken by the coordinator as a), this work having captured KI-TOOL-KI-CLI-161; hookconf retitles it.
- Kris, 19 October 23:21 BST: "Go ahead with the recommendations. Although the hook release, I'm not sure we need to wait for a repo confirmed because we'll never get there. So can we just get on with it? Happy for you to do it now, straight off the back of this." Taken: SCR5-CONFORM a), VA-HOOKS a), HOOK-CAPTURE a), and HOOK-RELEASE b): release now, granting this work the ki release, tag and tools-ki push. HOOK-GUARD reached Kris after this answer and stays open.
- Kris, 19 October 23:21 BST: "There are 23 tickets across triage for the tool projects, can we get those triaged immediately?" Taken: triage every triage record in tools-ki, tools-mgit and tools-git-almanac now, commits local.
