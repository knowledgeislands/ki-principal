# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-summary-drift

**🤖 → 👤 Handoff to supervisor · Run report at 23:58 BST · last mark 02:10 BST**

---

## Done

### What each reply lacked

Session ee47a74e, from the re-bootstrap at 21:38 BST to Kris's question at 23:49 BST, six replies to Kris:

- **21:44 BST, re-bootstrap report:** three numbered lines and the banner with its thread line; no report heading, no `Re-bootstrap at` form line, no `## Done`, `## In Progress` or `## Queries`, and DRAIN-END and SORT-ARM only named, not given in full.
- **21:41 and 21:49 BST, timed updates:** right shape; the 21:49 one carries the banner, as a state change needs.
- **21:53 BST, Summary:** heading, form line, three sections, eleven queries and the banner are all present. It falls short in three ways: Done is not one line each (two items carry seven and six nested bullets); COORD-COMMANDS and DRAIN-END each give two "recommended" options with two confidences, where the query-review rule keeps one recommended a), starts the reason with `review disagrees` and puts the reviewer's view in Context; and the work ids ki.tools-burndown and ki.portable-specifications, the Tending note, the findings design note and hnr's prompt are named but not linked.
- **23:11 BST, the Legal > SoP opener:** a plain reply, which is right for a prompt you asked for; a borderline case only because it says THEME-CLOSE is still waiting.
- **23:20 BST, "thats done":** "Here, 11 decisions are with you, starting with LAUNCH-FIRST, and nothing is running." It says where the work stands, so it owed the banner and has none. You were back after an 80-minute gap with eleven unanswered queries, so a Summary restating them in full was owed: the standard gives one "when the owner returns after a gap", and the style says no report says "see earlier".

### Causes, with evidence

- **The style is not stale.** `~/.claude/output-styles/ki-coordinator.md` is a symlink to the harness file. The copy loaded into the session matches the harness copy byte for byte, apart from the tool list that follows it. The hook line was current and fired on every message.
- **The re-bootstrap rule contradicts itself.** The standard's Bootstrap step 7 asks for a report "in three lines" under the heading. Report forms calls it "the three-line report". The style and the standard's Banner section, though, say every re-bootstrap report closes "after `## Queries`" with the banner. Hook rule 4 lists "every Summary, recap and hold report" and leaves out re-bootstrap. The opener's "report in three lines" comes from `ki agent prompts` (tools-ki `src/core/work/prompts.ts`) and the standard's templates. The coordinator took "three lines" literally and also dropped the heading and form line, which even the three-line form requires.
- **No rule says when a gap triggers a Summary.** "Returns after a gap" has no threshold, and the style leaves the trigger out entirely. So the 23:20 reply could treat itself as conversational.
- **The method refresh was not run.** At 21:38 the coordinator read revision 111b853a, but it did not re-read the standard, did not set `method_read` (still eff6163b, 27 commits behind) and did not tell you what changed. Of the standard it loaded only SKILL.md, not `standards-coordination.md`, so Bootstrap step 1 was skipped too. This mattered less than it might have, because the style and hook carry the current rules.
- **The proxy pulls the other way.** The Headroom proxy runs with `HEADROOM_OUTPUT_SHAPER=1`. Its log shows the L2 block applied to about 1,240 requests across all its clients between 21:00 and 23:59, and the block is appended at the end of the system prompt, after the style. It says "Never restate ... tool output that already appear in this conversation - reference them by path and line instead", which pulls against "restated in full each time". That fits the 23:20 "starting with LAUNCH-FIRST" reply, but it is inference: the transcript does not record what the proxy injected. Token mode also compresses Bash tool output lossily: in this run, a grep of the standard came back with "With", "to" and "of" stripped ("### 🤖 worker", "Handoff supervisor"). Read-tool output came through whole. A coordinator that reads its templates through Bash sees corrupted templates.
- **The quiet level is not a cause.** `communication.md` defers to the Reply forms and says no level shortens an owner report. Its "do not relay ... only the outcome" may add a little pull towards brevity, but it is weak.
- **The coordinator made its own errors too:** the nested Done bullets, the double recommendations, the unlinked work ids and the missing banner at 23:20 all break rules the loaded style states plainly.

### Habit fixes for the coordinator (no approval needed)

- Give every re-bootstrap report under the heading and form line, until REBOOT-SHAPE settles its sections.
- End every reply that says where the work stands with the banner. Give the Summary, with every open query in full, when you return after a gap.
- Run the refresh rule at every bootstrap, and set `method_read` once the standard has been read.
- Read the standard, the style and the package with the Read tool, not with Bash.

### Checks

- Report written and committed in ki-principal as c5cd2a9a, `docs(work): ki.ways-of-working summary drift report`; the pre-commit audit passes for its path.
- No standard, style, hook, chezmoi or Headroom file was changed.
- No pull before committing: the brief's no-remote-call rule rules out the fetch, so I could not tell whether ki-principal had moved.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The coordinator reviews these queries at receive under the query-review rule. REBOOT-SHAPE, GAP-SUMMARY, PROXY-SHAPER and METHOD-NUDGE are medium confidence.
- The opener text lives in tools-ki, so any change to it goes to ki.tools-burndown as a `messages.md` line once REBOOT-SHAPE is answered.

## Queries

### REBOOT-SHAPE - make the re-bootstrap report a full owner report

**Context:** The standard asks for a re-bootstrap report "in three lines" (Bootstrap step 7, Report forms). The style and the Banner section say it closes "after `## Queries`". Hook rule 4 leaves re-bootstrap out. The opener from `ki agent prompts` and the standard's templates both say "report in three lines". On 24 October this produced a 21:44 report with no heading, form line, sections or full queries. The fix is one harness change (the standard, the hook line and the style, regenerated, with the banner test) plus a tools-ki opener change. **Query:** Should the re-bootstrap report become a full owner report, with the three lines kept as what its sections hold, and the openers say "report in the re-bootstrap form"? **Options:** a) (recommended, confidence medium - it ends the contradiction that produced the 21:44 report, but it lengthens every re-bootstrap) Re-bootstrap report = heading, `Re-bootstrap at` form line, `## Done` (role and where the work stands), `## In Progress` (what is running), `## Queries` (every open query in full), then the banner; hook rule 4 names re-bootstrap and full summary; openers drop "in three lines". b) Keep three lines, but state plainly that they sit under the heading and form line, carry the open query tags in the banner, and stand in for the three sections; add re-bootstrap to hook rule 4.

### GAP-SUMMARY - set when a returning owner gets the Summary

**Context:** The standard gives a Summary "when the owner returns after a gap", with no threshold, and the style leaves that trigger out. At 23:20, after 80 minutes away and with eleven queries open, the reply said "11 decisions are with you, starting with LAUNCH-FIRST", with no banner and no queries. **Query:** Should the standard and style define the gap, and require the Summary with every open query in full in the first reply after it? **Options:** a) (recommended, confidence medium - a fixed threshold is mechanical and would have caught 23:20; 30 minutes is a judgement) The first reply after 30 minutes or more without an owner message, while queries are with you, answers what you asked and then gives the Summary; the style carries the same trigger. b) Leave the gap undefined, and rely on the banner rule plus "summary" on request.

### PROXY-SHAPER - the Headroom output shaper and compression in coordinator sessions

**Context:** The proxy appends an L2 steering block ("Never restate ... reference them by path and line instead") at the end of every system prompt, after the style. That conflicts with restating open queries in full, and the style already says no proxy shaping block shortens a report. Token mode also strips function words from Bash tool output, which corrupts templates read that way; Read-tool output arrived intact in this run. The Headroom proxy is connection-critical, so any change to it needs a tested restore path. **Query:** Should the proxy stay as it is, with the read path fixed in the standard instead? **Options:** a) (recommended, confidence medium - no change to a connection-critical service, and the style's override held for the 21:53 Summary; the 23:20 link to the proxy is inferred) Leave Headroom unchanged; add to the standard's Bootstrap and Re-anchoring that the standard, style and package are read with the file-read tool, not the shell; the style names the shaper's "never restate" as overridden for open queries. b) Turn the output shaper off for Claude Code (`HEADROOM_OUTPUT_SHAPER=0`, managed in chezmoi) under a run with a tested restore path.

### METHOD-NUDGE - warn when a coordinator's method_read lags

**Context:** At re-bootstrap the coordinator read harness revision 111b853a against `method_read: eff6163b`, 27 commits behind, but did not re-read the standard, update `method_read` or tell you what changed. Nothing mechanical catches this; the rubric says it cannot judge whether a coordinator refreshed. **Query:** Should the coordinator hook print one warning line when the work's `state.md` `method_read` differs from the harness revision? **Options:** a) (recommended, confidence medium - one cheap line at each prompt makes a skipped refresh visible; it touches the generated hook and its test) Add the check to `hooks/coordinator-reminder.sh`, naming both revisions. b) Leave it to coordinator habit and the bootstrap rule.

### REVIEW-CHECK - flag a query with two recommended options

**Context:** In the 21:53 Summary, COORD-COMMANDS and DRAIN-END each carried two "recommended by ..." options with two confidences, against the query-review rule: one recommended a), with its reason starting `review disagrees` and the reviewer's view in Context. Rubric item COORD-11 already checks confidence on recommended lines. **Query:** Should COORD-11 also warn when a query carries more than one `(recommended` option? **Options:** a) (recommended, confidence high - a narrow warning beside an existing check, easily reversed) Extend COORD-11 to warn on a second recommended option in one query. b) Leave it to coordinator habit.

### 🤖 → 👤 Handoff to supervisor · since 23:58 BST

👤 5 with you

- [with you] REBOOT-SHAPE · owner · since 23:58
- [with you] GAP-SUMMARY · owner · since 23:58
- [with you] PROXY-SHAPER · owner · since 23:58
- [with you] METHOD-NUDGE · owner · since 23:58
- [with you] REVIEW-CHECK · owner · since 23:58
- [committed] summary-drift report

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
