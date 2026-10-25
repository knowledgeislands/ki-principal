# hold-drain brief

Work: ki, State of play, KI > SoP. Host sol. Kris asked at 02:00 GMT on 2026-10-25 to drain down (see the HOLD entry in `+/_WORK/ki/decisions.md`). Carry out the `ki-coordination` On hold steps for State of play's package `+/_WORK/ki/` under `ki-work-package`, so that a fresh session can pick everything up from the package alone.

## Steps

1. **Receive blind-accept.** `blind-accept.report.md` reviews the three queries in `queries.md` marked "(in blind review)": ACCEPT-KI-WEBSITE-SITE-044, ACCEPT-KI-PRINCIPAL-MOD-009 and ACCEPT-KI-TOOL-RIG-CORE-062.
   - Where the reviewer agrees, lift the confidence one level, with the reason beginning `reviewed`.
   - Where it disagrees, show both views.
   - Drop the "(in blind review)" markers, then delete the report and `briefs/blind-accept.md`.
2. **The failed run.** `accept-review-obs` exited without finishing, so the review of KI-OBSERVA-BRG-005 and KI-OBSERVA-VIS-030 is unprepared. BRG-005 already passes the roadmap audit, so Kris's precondition under ACCEPT-OBSERVATORY is met. Park it as ACCEPT-OBSERVATORY, with the next step "rerun the review prep", and delete `briefs/accept-review-obs.md`.
3. **Messages.**
   - Route the MGIT-PUSH-GUARD line (tools-mgit) to `+/_WORK/ki.tools-burndown/messages.md`, unchanged apart from a "routed by KI > SoP (ki)" note, and remove it here.
   - Keep the two IMPORTANT REFRESH lines at the top. They are re-reads for the next coordinator session.
   - Shorten any message line the work-package audit flags as long, keeping its pinned links.
4. **Outstanding work back to its owners.** For each open or parked query, decide whether it belongs to another work.
   - Route a query to that work's `messages.md` as one line only when that work can act on it within its own authority without a new owner decision. SITE-DEPS to ki.website is a likely case.
   - Everything that needs Kris stays in State of play's `queries.md`.
   - Create no roadmap records (CAPTURE-GATE).
5. **Park.** Move every open query under `## Parked` in `queries.md`, keeping each one's tag, title, Context, Query and Options in full, so it can be put to Kris without anything else being read. `## Open` reads `None.` The morning order (accepts first, then AGENT-HOST, CLI006-CONFIRM and CLI006-READY, ESTATE-CLOSE, KA-CLOSE, SITE-DEPS, SPECS-FOLDER, the homes, and the Capital baseline queries; PRE-REBASE-REF at terra) goes in `state.md`'s next steps.
6. **Compact state.md.**
   - Rewrite it under 400 words, with no history; Git holds that.
   - Front matter: `state: on-hold`, `hold.reason: paused`, `hold.release: when Kris says resume`, `since` and `mark` at the commit time in UTC, and `beat: null`.
   - Next steps: the morning order, the terra-only items (PILOT-SEED, STASH-DROP, PRE-REBASE-REF), the `.rumdl.toml` OWN-1 warning, and SITES-PIN's unowned half.
7. **Strike decisions.** Strike each entry a durable home wholly carries. Reduce to a one-line pointer each entry that still governs live work. Keep today's interactive read-backs, which govern parked queries, compacted where they are now carried by a query.
8. **Prune.**
   - Delete received briefs, and the `briefs/` folder once it is empty.
   - Keep `skills-assessment.report.md` only if a parked query still cites it.
   - Review `design/` under the design-note guards, keeping drafts, notes under review, notes others link to and any in doubt.
9. **ki.website.** Confirm it still passes its scoped work-package audit and stays on hold.
10. **Check and publish.**
    - Run the scoped work-package audit on `+/_WORK/ki/` and fix what is ours.
    - Commit by explicit path. The final commit is `docs(work): ki hold, paused`.
    - Pull with rebase and push fast-forward only. Never force a push and never use `--no-verify`.
    - Confirm `ki-principal` is level with origin.

## Limits

- Touch nothing of another session's: the uncommitted files in ki.ways-of-working, ki.chezmoi, ki.knowledge-acquisition, ki.baseline-rollout and `Admin/Governance/Known Lands.md`, and `+/_WORK/ki.specifications/`.
- No Admin, Pillars or Resources changes, no record changes, and no deletion outside `+/_WORK/ki/`.
- If any `messages.md` you need is dirty from another session, skip it and say so.

## Report

Write `/Users/krisbrown/.local/state/ki/agents/ki/hold-drain.report.md` in hold-report shape: `## Done` (one line per repository, plus each routing), `## Parked` (each tag with one line), and `## Left over` (or "Nothing").
