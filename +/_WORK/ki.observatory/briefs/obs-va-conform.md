# obs-va-conform

Work: KI > Model > Observatory. Decisions: `+/_WORK/ki.observatory/decisions.md` in ki-principal (VA-CONFORM). Background: `~/.local/state/ki/agents/observatory/obs-dr-vallearmonia.report.md`. Repository: apps-vallearmonia.com.

Kris on 19 October: "yes, fix it please and commit and push".

1. The roadmap audit fails ITEM-1 (every record identifier) and ROAD-7 (ledger not in `last_id` form). Bring the roadmap to the current standard with `ki repo conform`, preview first, then apply; fix by hand only what conform leaves, under `ki-work-roadmap`.
2. Renaming an identifier must carry every reference with it: links, file names, front matter and anything else in the repository that cites it. Lose no record or history.
3. Change nothing outside the roadmap and its references. Touch no file another session has dirty; name it.
4. The roadmap audit and the repository's gate must pass. Commit by explicit path; push fast-forward only your own commits. A push to main may rebuild the live site; that is expected. Report in one short owner report: what changed, the audit result, commits.
