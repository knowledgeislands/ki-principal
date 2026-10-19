# ki.observatory queries

## Open

### BRG-005-COUNTS - Counts on the Act board

**Context:** KI-OBSERVA-BRG-005 wants counts on the confirm step and the receipt. Every Act operation today acts on one target, the record excludes batch operations, and it is still in triage, so this shapes it for later rather than building it now.

**Query:** How should the Act board counts be handled?

**Options:**

a) (recommended, confidence high - reviewed: honest with today's single-target operations; the count is of operations, never files) Count one operation per request, the receipt showing its outcome, and leave batch operations for a later record.

b) Add batch operations.

c) Leave the counts out.

### VIS-031-TABLES - Where the "who is working" column appears

**Context:** KI-OBSERVA-VIS-031 adds a worker column showing which run or person is working where. The reviewer adds that a repository match alone does not prove who owns a particular record, so the column should say when it is repository-level.

**Query:** Which tables should carry it?

**Options:**

a) (recommended, confidence medium - reviewed: matches the record's goal of repositories and records) Repositories and Roadmap rows, plus what each run touches on Sessions, labelled where the match is repository-level.

b) Repositories only, at first.

### TAB-ROOM - Making room for the Known Lands tab

**Context:** The minimal Known Lands chart is built (KI-OBSERVA-VIS-030); its tab is ready but unmerged. A test requires every tab to fit the bar without scrolling on a 1,440 px window: fifteen tabs take 1,341 of 1,392 px, and a sixteenth titled `known lands` makes 1,454 px. The reviewer found that shortening `review queue` to `review` is not enough alone (1,412 px); the new tab must also be called `map`. The reviewer prefers letting the bar scroll, which PDR-KI-OBSERVA-002 already specifies with edge fades, focus visibility and wheel scrolling, keeping full titles; only the wide-window fit check would change. The 760 px rule is unaffected either way.

**Query:** How should the bar make room for the Known Lands tab?

**Options:**

a) (recommended, confidence medium - review disagrees: keeps the width test whole and the bar unscrolled) Shorten `review queue` to `review` and title the new tab `map`.

b) (reviewer's choice, high) Add the tab as `known lands` and let the bar scroll at 1,440 px with its existing fade, changing only the wide-window fit check.

c) Add no tab yet; show the chart at the top of an existing view, such as Trade routes, until the designs place it.

d) Tighten the spacing between tabs, changing the look ahead of the designs.

## Parked

None.
