# Queries as discussions

Draft design note for [ki.prj.ways-of-working](../../work.md), written by run `discussions-design` on 31 October 2026 under QUERIES-AS-DISCUSSIONS. It decides nothing; it sets out one question for Kris.

## Why

Kris, 31 October 2026, 12:40 GMT: "these queries are really discussion points: you build up a number of discussion points, get to the end of them and end up with decisions. I am inclined to think these are in fact discussions."

The way we already work matches this. Points build up in `queries.md`, Kris works through them one at a time in the interactive pass (INTERACTIVE-QUERIES and QUERY-TURNS, 31 October), and the set ends with a mark (QUERY-SET-MARK, 31 October). What does not match is the word. "Query" sounds like a worker asking permission; "discussion point" says what it is: something Kris and the worker talk through until it becomes a decision. The gap is mostly in language, plus one missing step: the discussion's conclusion does not gather the decisions it reached.

## What would change

| Part | Today | As a discussion |
| --- | --- | --- |
| Concept | a query | a discussion point; the set of open points is the discussion |
| Report section | `## Queries` | `## Discussion` |
| Point heading and body | `### TAG - title`, then **Context**, **Query**, **Options** | unchanged; the **Query** line is still the question the point asks |
| Tags | "Needs tags" | "tags"; same rules, stable and never reused |
| Interactive pass | "Query 3 of 7" | "Point 3 of 7"; the pass is called "the discussion" |
| End of the set | mark, then Summary | the discussion concludes: one list of the decisions reached, then the mark, then a Summary whose `## Decided` lists them |
| A point that needs no decision | not provided for | may close as "noted, no decision", logged like any answer |
| Blind review | "query review" | "blind review" of a point; same rules |
| Blocked send | "blocking query" | "blocking point" |
| Package file | `queries.md`, `## Open`, `## Parked` | either kept, or `discussions.md` (see the options) |

Parking, the eight-point cap, confidence on option a), plain English and the blind review all stay as they are.

## Who reads these words

Anything that parses the report section or the file must accept both names before anything writes the new one, or open points silently drop out of view.

- **Harness:** the `ki-coordination` rubric (COORD-11 reads a report's `## Queries`); the `ki-work-package` rubric (open-point count from `queries.md` `## Open`, report sections, the file's heading check); the `ki-repo-kb` rubric's list of known package files; the `ki-delegation` brief footers and run prompt; the coordinator output style and the other generated surfaces.
- **`ki`** (`tools-ki`): `src/core/agent/events.ts` finds a report's outstanding points under `## Queries`; `src/core/agent/thread.ts` reads a point's options from it.
- **Observatory** (`apps-observatory.local`): `packages/evidence/src/review.ts` and `focus.ts` read `queries.md` `## Open` and reports' `## Queries`.

## Migration

About 59 live work packages across the territories carry a `queries.md`.

- **Renaming the section only:** no package moves. Readers learn to accept `## Discussion` beside `## Queries`; then the standard and generated surfaces switch the writers. Past reports keep `## Queries` for good, as earlier shapes already do. `tools-ki` and the Observatory each get a line in their own `messages.md` for their half, and the harness writers wait until both have landed.
- **Renaming the file too:** the same, plus every reader accepting both file names for a tolerance window, a territory sweep renaming about 59 files repository by repository, the closed list and the State of play package-creation rule updated, and the tolerance closed afterwards. Roughly three times the work and the moving parts, for a file Kris rarely opens directly.

## Challenges to earlier decisions

- **QUERIES-FILE and PARKED-HOME** (put every open and parked query in full in `queries.md`) stay sound; only the name is in question, and the file name is the costliest thing to change for the least visible gain.
- **QUERY-SET-MARK** (31 October) closes the set with a mark but does not gather what was decided. If points end in decisions, the conclusion should show them together; that is the one new behaviour this design proposes.
- **One answer per point** assumes every point ends in a decision. Discussions sometimes end in "noted" or in a new point; the rules should allow both.
- **Leaving it alone** was considered: the pass already behaves like a discussion. It is not offered, because Kris asked for this to be decided urgently and the word shapes how every report reads.

## The question for Kris

### DISCUSSIONS - How far to take "discussion points" in place of "queries"

**Context:** Queries already work like a discussion: they build up, Kris works through them one at a time, and the set ends with a mark. Only the words and the ending differ. The cheapest change renames what Kris sees, the report section `## Queries` to `## Discussion`, "Query 3 of 7" to "Point 3 of 7", and ends each discussion with a list of the decisions it reached, while keeping the package file `queries.md` as it is. Renaming the file as well touches about 59 work packages across the territories and every tool that reads them, `ki` and the Observatory included, for a file Kris rarely opens.

**Query:** Should we rename queries to discussion points in what Kris reads only, or in the package files too?

**Options:**

a) (recommended, confidence medium - it carries the intent everywhere Kris reads at a third of the cost, and is easy to extend later, but the file name is a matter of taste) rename the concept, the report section, the pass wording and the end of the set, add the closing list of decisions and the "noted, no decision" ending, and keep `queries.md`; readers in `ki` and the Observatory accept both section names before the writers switch

b) do all of a) and also rename `queries.md` to `discussions.md` in every package, with a tolerance window in which every reader accepts both file names, then a territory sweep
