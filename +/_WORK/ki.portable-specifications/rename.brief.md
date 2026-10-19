# Brief - specifications/rename

Kris decided PROJECT-NAME on 19 October: the paused Project `Streams/Projects/specifications.md` stays exactly as it is, and this Project becomes `portable-specifications`. Read `+/_WORK/ki.specifications/decisions.md` (OPEN-PROJECT and PROJECT-NAME) and `work.md` first.

## Do

1. Write `Streams/Projects/portable-specifications.md`, title "Portable specifications", theme Model, `lifecycle: active`, shaped like its sibling Project notes, with its outcome taken from `+/_WORK/ki.specifications/design/plan.md` if present, else from the goals in `work.md`: three portable specs, `work`, `knowledge` and `acquire`, held in their owning skills, published on the website later and moved into KI Specifications. Register it in `Streams/Projects/Projects.md` and on `Streams/Themes/model.md`, following the existing entries.
2. `git mv '+/_WORK/ki.specifications' '+/_WORK/ki.portable-specifications'`; in it set `id: ki.portable-specifications`, `title: 'KI > Model > Portable specifications'` and `project: portable-specifications` in `work.md`, `id:` in `state.md`, and the headings of the five files; link the work file's Goals to the new Project note's outcome, replacing the PROJECT-NAME line.
3. Repoint every link and mention of `ki.specifications` or `+/_WORK/ki.specifications` in this repository outside Git history, including `+/_WORK/ki.ways-of-working/` and `+/_WORK/ki/`, leaving past commit subjects and quoted owner words unchanged.
4. Commit by explicit path, `docs(work): ki.portable-specifications rename from ki.specifications, add Project note`. Do not push.

Never run `ki repo conform` without `--dry-run` (HOOK-GUARD). Touch nothing in `Streams/Projects/specifications.md`.

## Report

Write your report as the run packet directs: Done, one line per step with the commit; Queries, or `No outstanding queries`.
