# KI > Techne > Agora › atlas-design

**🤖 → 👤 Handoff to supervisor · Run report at 22:23 GMT · last mark 00:04 GMT**

---

## New and noteworthy

The Atlas now has the pack's shell and its three Work and Guilds pages. Each was checked against its artboard in dark and light from a throwaway capture run.

Shell (★0.3a) is close. It has the grouped sidebar: Agora, then Work, then Guilds alone between rules, then Observatory, KIV (folded, "soon"), Coming, and Accounts, Settings and Updates at the foot. It also has the portal and Beacon lines, tabs (each a place, ⌘-click opens a new one), and the context control (territory with ⌘1 to ⌘9, plus the plane). A page that ignores the territory or the plane shows it greyed. The tray pushes the page narrower and the bottom pane can be dragged to resize.

Some of the artboard is left out:
- the window lights, because they are native;
- the Lantern line, because there is no Lantern data;
- the Home sub-places (Who's doing what and the rest), because those pages do not exist yet.

Roadmap (★7.1a) is very close. It has:
- status tallies, with Closed hidden until chosen;
- a gold top edge on Awaiting review only;
- the dashed context chip, then Filter (fields with counts under the other filters), find, and Group by Status, Island, Area or None;
- folding group rows, with "Show N more";
- the record tray with one brass "Open to review" when a record awaits review, plus "Read in full", which opens the whole text in the bottom pane;
- the nothing-matching state.

When "Open to review" is shown, the tray foot wraps to two lines.

Jobs (★7.2a) is close. It has:
- tallies by standing;
- grouping by territory then repository, by Mac, or none, where a group with a failure or findings opens and says so;
- the Next column, worked out from the calendar or the interval;
- a tray with each Mac's run ticks;
- "Show runs", which opens a bottom pane with every run beside the declaration, and no run log tab.

These differ from the artboard:
- "Open its file" is omitted, because nothing in the app can open a job's file;
- the ticks show at most 5 runs per Mac, which is all the app keeps;
- there is no Filter menu yet on Jobs; tallies and find do the filtering.

Guilds (★8.1a) is close:
- the guild badges run across as the tallies;
- All guilds shows the ledger (8.1c);
- a chosen guild shows its skill badges beneath;
- a skill opens in the bottom pane, with SKILL.md (front matter and where it lives beside the text), references/, scripts/ and assets/ as tabs.

The rename run did not wire in the illustrator's badges (`guild.logo` is null), so the badges are monograms on hued shields. With 15 guilds the strip wraps to two rows (open point 29).

I found and fixed two problems along the way:
- **Next-run hang.** The next-run sum looped forever on a zero interval. I rewrote it to a closed form, made hourly calendars work, and added tests.
- **Capture wait.** The window only told the capture harness it was ready after drawing the Home map. Reopening on a list page therefore never captured. It now signals once the lands and the Beacon are in, whichever page is open.

## Done

Commit `6e2b452` (feat(atlas): rebuild the shell, Roadmap, Jobs and Guilds after the design pack) is pushed to `origin/main`, fast-forward only. Checks:
- `bun run self:check` passes, with 60 lint warnings, all CSS selector-order warnings (22 before).
- `bun run test` passes: 54 files and 502 tests.
- The captures ran for Roadmap, Jobs, Guilds and Home in dark, and Roadmap, Jobs and Guilds in light, with a record, a job and a skill open.

Nothing was installed, packaged or relaunched, and no other repository was changed.

## In Progress

Nothing is running. These are left for a later pass:
- a Filter menu on Jobs;
- a capture-harness hook for the runs pane (it shares the record and skill pane code, which were captured);
- reordering the new CSS so the selector-order lint warnings go.

## Queries

**Q1 · Who owns a job (point 21)**

**Context:** Rig's job declarations name no owner. Jobs groups each job under the repository it works in, but a failed job cannot say whom to tell.

**Query:** Should a job's declaration name its owning work package?

**Options:**
a) (recommended, confidence medium - it lets a failure reach the right thread, and Rig owns the declaration) Add an optional `owner` such as `work/hnr.sop.main` to Rig's declaration, and show it in the tray.
b) Keep inferring it from the repository.

**Q2 · Next run (point 22)**

**Context:** The app now works out the next run from the calendar (weekday, hour and minute) or from the interval since the last run. It shows nothing for other calendar keys.

**Query:** Is a worked-out next run good enough?

**Options:**
a) (recommended, confidence medium - it is right for every job declared today and needs no other change) Keep working it out in the app.
b) Have Rig or the reporter state the next run.

**Q3 · How much run history (point 23)**

**Context:** The pack assumes 14 days of runs. Agora keeps 5 runs per Mac, and the runs pane says Agora keeps each Mac's last runs.

**Query:** How deep should the runs pane go?

**Options:**
a) (recommended, confidence medium - it holds a week of a daily job without growing the shared picture much) Raise it to 10 runs per Mac and say how old the oldest is.
b) Keep 5.
c) Read 14 days from the reporter on demand.

**Q4 · Is review Kris's act (point 24)**

**Context:** Awaiting review carries the gold edge and the one brass "Open to review", on the reading that review waits on Kris.

**Query:** Should that stay so?

**Options:**
a) (recommended, confidence medium - most records awaiting review today await Kris's acceptance) Keep it.
b) Gold only when the assignee is Kris.

**Q5 · Folding long groups (point 25)**

**Context:** Roadmap shows six rows of a long group, then "Show N more". Group rows fold by a click, for this session only.

**Query:** Fold or scroll?

**Options:**
a) (recommended, confidence low - it fits every heading in one window as the pack wanted) Keep folding, and remember each group's fold.
b) One long scroll.

**Q6 · Statuses outside the order (point 26)**

**Context:** Any other status gets its own tally after triage, unmarked. None exists today.

**Query:** Should another status be allowed?

**Options:**
a) (recommended, confidence high - the lifecycle is fixed by the work-roadmap standard) No: keep the seven and leave the fallback.
b) Name one more now.

**Q7 · HNR's skills (point 27)**

**Context:** The lands now show 15 guilds, including Humans Not Robots skills (6) and one-skill guilds for Equal Remedy, Legal, Personal, Sacred Inquiry, Techmedix and Valle Armonia.

**Query:** Should each territory's unsorted skills stand as a guild of their own?

**Options:**
a) (recommended, confidence medium - it is what the provisional catalogue does, and the catalogue can fold them later) Yes, until `ki.reg.guilds` places them.
b) Gather them under one "Territory skills" guild.

**Q8 · Guild colours (point 28)**

**Context:** Each guild has a hue for identity only. At 15 guilds some hues sit close.

**Query:** How should guilds be told apart?

**Options:**
a) (recommended, confidence medium - the logos already have a field) Wire the illustrator's logos into the catalogue next.
b) Keep hues and widen their spread.

**Q9 · More than one row of badges (point 29)**

**Context:** 15 guilds wrap to two rows of 118-point badges beside the sidebar.

**Query:** Which form at ten or more?

**Options:**
a) (recommended, confidence low - it keeps every guild in view without a scroll) Two rows as now.
b) A narrower badge of shield and name only.
c) One row that scrolls.

🧵 ki.prj.agora
