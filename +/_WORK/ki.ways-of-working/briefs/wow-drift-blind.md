# wow-drift-blind

Masked blind review of four questions about a coordinator AI thread that Kris (the owner) works with. Do not read `+/_WORK/ki.ways-of-working/queries.md`, `decisions.md`, any `*.report.md` or `design/` note. You may read, in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, `skills/change-management/ki-coordination/references/standards-coordination.md`, `output-styles/ki-coordinator.md` and `hooks/coordinator-reminder.sh`. Read-only: change, commit and push nothing. For each question pick one option or a better one, with a confidence (high, medium, low) and a two-line reason.

## Q1 - the re-bootstrap report

Context: The standard asks for a re-bootstrap report "in three lines"; the style and the standard's Banner section say every re-bootstrap report closes after `## Queries` with the banner; the hook's rule 4 omits re-bootstrap; the openers say "report in three lines". A re-bootstrap on 24 October gave three numbered lines and a banner with no heading, form line, sections or open queries in full.

- Keep three lines, but say plainly they sit under the heading and form line, carry open query tags in the banner and stand in for the three sections; add re-bootstrap to hook rule 4.
- Make it a full owner report (heading, `Re-bootstrap at` form line, Done, In Progress, Queries with every open query in full, banner); hook rule 4 names re-bootstrap and full summary; openers drop "in three lines".

## Q2 - Summary after a gap

Context: The standard gives a Summary "when the owner returns after a gap" with no threshold; the style omits the trigger. After 80 minutes away with eleven queries open, the coordinator replied in one line naming the first query.

- Leave the gap undefined; rely on the banner rule plus "summary" on request.
- The first reply after 30 minutes or more without an owner message, while queries are with the owner, answers the message and then gives the Summary; the style carries the same trigger.

## Q3 - a context-compression proxy

Context: A local proxy appends a steering block at the end of every system prompt: "Never restate code, file contents, diffs, or tool output that already appear in this conversation - reference them by path and line instead". The style says no proxy block shortens a report and that open queries are restated in full each time. The proxy also strips function words from shell tool output (templates read through the shell arrive corrupted); file-read tool output arrives intact. The proxy is connection-critical.

- Turn the output shaper off for this client, managed in the dotfiles, under a run with a tested restore path.
- Leave the proxy unchanged; the standard's Bootstrap and Re-anchoring say the standard, style and package are read with the file-read tool, not the shell; the style names the "never restate" block as overridden for open queries.

## Q4 - stale method warning

Context: Each work's `state.md` records `method_read`, the harness revision of the method last read. At re-bootstrap it was 27 commits behind and the coordinator neither re-read nor said so. Nothing mechanical catches this.

- Leave it to coordinator habit and the bootstrap rule.
- The coordinator hook prints one warning line naming both revisions when `method_read` differs from the harness revision.

## Output

Write `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-drift-blind.report.md` and give the same in your final message.
