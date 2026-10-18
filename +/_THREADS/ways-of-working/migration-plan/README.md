# Migration plan

Dry-run scripts that apply phases 3 and 4 of the [work migration brief](../work-migration.brief.md) once tools-ki is released, written by the `migrate-plan` run of 18 October 2026. Each script prints what it would do unless given `--apply`, and saves nothing; its dry run sits beside it as `<script>.dry-run.txt`.

- [lib.sh](lib.sh): the shared helpers. A path in [defer.list](defer.list), or with another session's unstaged or untracked changes, is held and named, never touched. An apply refuses while anything is staged, and commits only the paths it touched, by explicit path, through the normal gate.
- [classification.tsv](classification.tsv) and [classification.md](classification.md): every checkpoint and thread folder, its work id, area and reason.
- `capital/`: Knowledge Islands Principal, in this order:
  1. [01-design-tidy.sh](capital/01-design-tidy.sh): design folders out of Streams.
  2. [02-themes.sh](capital/02-themes.sh): Initiatives to `Streams/Themes/`, with the wikilinks and the Work Process tree.
  3. [03-projects.sh](capital/03-projects.sh): flat Project notes with `theme:`.
  4. [04-activities.sh](capital/04-activities.sh): the Activities' `theme:`.
  5. [05-work-folders.sh](capital/05-work-folders.sh): checkpoints and thread folders into `+/_WORK/` and `+/_WORK_REVIEW/`.
  6. [06-citations.sh](capital/06-citations.sh) with [rewrite-links.pl](capital/rewrite-links.pl): live citations of every moved path.
  7. [07-checks.sh](capital/07-checks.sh): the ignore block and the audits.
- `territory/`: the other repositories, listed in [territory.md](territory/territory.md), with [harness.sh](territory/harness.sh) and [tools-rig.sh](territory/tools-rig.sh).

To apply, from a clean index in the Capital, copy this folder out first, because step 5 moves it into `+/_WORK/ki.ways-of-working/design/`:

```sh
cp -R '+/_THREADS/ways-of-working/migration-plan' tmp/ways-of-working/plan
for step in tmp/ways-of-working/plan/capital/0*.sh; do "$step" --apply || break; done
```

Each step commits its own paths. `MIGRATE_NO_COMMIT=1` leaves them staged instead. A held row stays where it is; remove its `defer.list` line once its session has landed and run steps 5 and 6 again, which pick it up and rewrite citations of every path moved so far: each applied move is logged in `tmp/ways-of-working/migration-moves.tsv`, and step 6 saves the whole map as `applied-map.tsv` in the plan's new home. Each step ends with its hand steps, which the apply does not do.
