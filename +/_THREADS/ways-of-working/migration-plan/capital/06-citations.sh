#!/usr/bin/env bash
# Phase 3 step 6: rewrite every live citation of a moved path or an old thread id.
#
# The path map joins what steps 01, 02, 03 and 05 would still move, from their --map, which leaves out every held
# row, with every move already applied, from the move log and the applied map. rewrite-links.pl rewrites relative links, absolute and ki-principal/ paths, quoted and
# backticked repository paths, and backticked thread stems, in the live notes and +/diagrams. Reports, decisions
# logs, design papers, roadmap records, the Calendar and pinned GitHub links are history and stay as they are. Run
# after 01 to 05; a dry run before them shows what the whole migration's citations will become. Each apply adds its
# map to the applied map in the migrated plan folder, so a later run for a held row still rewrites citations of
# paths an earlier run moved, such as an in-flight checkpoint's links to the ways-of-working reports.

source "$(dirname "$0")/../lib.sh" "$@"
begin

capital=$STEP_DIR
for step in 01-design-tidy 02-themes 03-projects 05-work-folders; do
  REPO=$REPO bash "$capital/$step.sh" --map
done > "$SCRATCH/new-map.tsv"
applied=${MIGRATE_APPLIED_MAP:-+/_WORK/ki.ways-of-working/design/migration-plan/applied-map.tsv}
cat "$SCRATCH/new-map.tsv" "$MOVE_LOG" "$applied" 2> /dev/null | sort -u > "$SCRATCH/map.tsv" || true

while IFS=$'\t' read -r id _ _ checkpoint thread _; do
  [ "$checkpoint" = - ] && continue
  held "$checkpoint" > /dev/null || { [ "$thread" != - ] && held "$thread" > /dev/null; } && continue
  printf '%s\t%s\n' "$(basename "$checkpoint" .md)" "$id"
done < <(rows) > "$SCRATCH/ids.tsv"

say "Path map: $(wc -l < "$SCRATCH/map.tsv" | tr -d ' ') moves, $(wc -l < "$SCRATCH/ids.tsv" | tr -d ' ') thread ids"
[ "$MODE" = map ] || sed 's/^/    /' "$SCRATCH/map.tsv"

say "Rewrite the live citations"
{
  live_notes
  find +/diagrams -type f \( -name '*.json' -o -name '*.toml' -o -name '*.md' \) 2> /dev/null || true
} | sort -u > "$SCRATCH/files"
: > "$SCRATCH/dead"
while read -r file; do
  perl "$capital/rewrite-links.pl" "$SCRATCH/map.tsv" "$SCRATCH/ids.tsv" "$file" 2>> "$SCRATCH/dead" | replace "$file"
done < "$SCRATCH/files"

say "Dead links, left as they are"
if [ -s "$SCRATCH/dead" ]; then sed 's/^/  - /' "$SCRATCH/dead"; else note "none"; fi

if [ "$MODE" = apply ] && [ -d "$(dirname "$applied")" ]; then
  cp "$SCRATCH/map.tsv" "$applied"
  git add -- "$applied"
  touched "$applied"
  echo "  applied map: $applied"
fi

say "By hand"
if [ "$MODE" = apply ]; then
  git grep -n -I -E '\+/_CHECKPOINTS|\+/_THREADS|Streams/Initiatives' -- AGENTS.md CLAUDE.md Admin Pillars Streams '+/_WORK' '+/diagrams' ':(exclude)*/briefs/*' \
    ':(exclude)Streams/Roadmap/KI-*' ':(exclude)*.report.md' ':(exclude)*decisions.md' ':(exclude)*/design/*' |
    sed 's/^/  HAND: residual citation: /' || note "no residual citations"
else
  hand "after the apply, this step lists each live citation the rewrite left, for a hand check"
fi
hand "each dead link above points at a report deleted before the migration; drop it or relink it to the report's last revision on GitHub"

commit "docs: rewrite citations of the moved work and theme paths"
