#!/usr/bin/env bash
# Phase 3 step 7: the ignore block and the checks that close the Capital's migration.
#
# The .gitignore names none of the old folders, so the ignore block needs no change and this step only confirms it.
# The audits are read-only: the dry run names them and the apply runs them, each for one declared skill. ki work
# status is a phase-2 deliverable; the step runs it when the installed ki has it.

source "$(dirname "$0")/../lib.sh" "$@"
begin

say "Ignore block"
if grep -n -E '_CHECKPOINTS|_THREADS|_WORK|Streams/Initiatives' .gitignore > "$SCRATCH/ignore"; then
  sed 's/^/  HAND: .gitignore names an old or new work area: /' "$SCRATCH/ignore"
else
  note ".gitignore names no work area; nothing to change"
fi

say "Audits"
check() {
  echo "  $*"
  if [ "$MODE" = apply ]; then "$@" || echo "  FAILED: $*"; fi
  return 0
}
for skill in ki-repo-kb ki-repo-kb-streams ki-decision-records ki-checkpoint ki-pmo; do
  check ki repo audit --skill "$skill" --concise --progress never --reporter-levels FAIL
done
if ki work status --help > /dev/null 2>&1; then
  check ki work status
else
  note "ki $(ki --version 2> /dev/null) has no work status; run ki work status once tools-ki ships it"
fi

say "By hand"
hand "read each audit's FAIL lines; a work folder outside the closed list or a held row's tolerance warning is expected until its session lands"
