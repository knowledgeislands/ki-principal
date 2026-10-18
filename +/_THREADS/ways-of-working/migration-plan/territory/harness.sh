#!/usr/bin/env bash
# Phase 4, KI Agentic Harness: its one thread folder goes to review, and its housekeeping records name their theme.
#
# skill-reviews is the archived skill-diagram thread of KI-HARNESS-GOV-193, with no checkpoint and no registered
# Project, so it goes to +/_WORK_REVIEW/ki.regular.skill-reviews/ as ad hoc work: decisions and reports at its root,
# its brief-*.md files in briefs/, and scratch/ and screens/ in design/ as strays. The empty +/_CHECKPOINTS scaffold
# and the empty +/_THREADS folder go. The four housekeeping records' initiative key becomes the Foundations theme;
# the ki-work-recurring examples are the harness's own phase-1 text and are left to it.

REPO=${REPO:-/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness}
source "$(dirname "$0")/../lib.sh" "$@"
begin

id=ki.regular.skill-reviews
src=+/_THREADS/skill-reviews
dst=+/_WORK_REVIEW/$id

say "Create the review area's index note"
create +/_WORK_REVIEW/README.md <<NOTE
# Work for review

Work folders the migration could not place with confidence. Each waits here for Kris's review and moves itself to \`+/_WORK/\` at its next mark, or is finished and deleted, with Git keeping it. This area is not counted, and its folders are not checked against the closed list until they leave it.

- [$id]($id/work.md) - the archived skill-diagram thread of KI-HARNESS-GOV-193, committed at the territory hold on 15 October with no checkpoint; probably finished.
NOTE

say "Move skill-reviews to review"
if why=$(held "$src"); then
  note "HELD, left for the next run ($why)"
else
  create "$dst/work.md" <<NOTE
---
id: $id
level: regular
title: 'KI > Regular > Skill reviews'
theme: null
worker: agent
supervisor: owner
state: on-hold
hold:
  reason: paused
  release: Kris's review
since: $NOW
received: null
beat: null
created_at: $NOW
---

# $id

## Next steps

- Decide with Kris whether this archived thread is finished; if it is, delete the folder, Git keeping it.

## Messages

- MIGRATED - this folder was \`$src/\` until the work migration of ${NOW%%T*}. At your next mark, move it out of review or finish it, then remove this line.

## Parked

None.
NOTE
  for path in "$src"/*; do
    name=$(basename "$path")
    case $name in
      decisions.md | *.report.md) move "$path" "$dst/$name" ;;
      brief-*.md) move "$path" "$dst/briefs/${name#brief-}" ;;
      *)
        note "stray outside the closed list: $path -> design/"
        move "$path" "$dst/design/$name"
        ;;
    esac
  done
fi

say "Retire the empty checkpoint scaffold"
if [ -z "$(find +/_CHECKPOINTS -mindepth 1 -not -name README.md 2> /dev/null)" ]; then
  remove +/_CHECKPOINTS/README.md
else
  note "+/_CHECKPOINTS holds more than its README.md; left"
fi

say "Name the theme in the housekeeping records"
printf '%s\n' 's~^initiative: platform-foundations$~theme: foundations~' > "$SCRATCH/theme.sed"
for record in docs/housekeeping/KI-HARNESS-HK-*.md; do edit "$record" "$SCRATCH/theme.sed"; done

say "By hand"
hand "apply after tools-ki ships ki work status and accepts theme on records, and after the ki-checkpoint work-file standard in flight in skills/governance/ki-checkpoint is committed"
hand "rewrite citations of $src/ in live harness files once moved: git grep -n '+/_THREADS/skill-reviews' -- ':(exclude)$dst'"

commit "docs(work): move the skill-reviews thread to review and name the housekeeping theme"
