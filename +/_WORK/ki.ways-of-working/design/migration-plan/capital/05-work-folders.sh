#!/usr/bin/env bash
# Phase 3 step 5: checkpoints and thread folders become work folders, in +/_WORK or +/_WORK_REVIEW.
#
# Each classification row becomes +/<area>/<id>/. Its checkpoint becomes work.md in the ki-checkpoint work-file form:
# the closed front matter, carrying created_at; the H1 as the id; Next steps from the pick-up block and Next step;
# Parked from Open questions; and a MIGRATED line in Messages for the work's next mark. Objective, Current state,
# Decisions made and Files touched are dropped, Git keeping them, and each relative link goes one level deeper. Its thread
# folder's decisions log and reports go to the work folder's root, briefs to briefs/, and anything else, which the
# closed list does not admit, to design/, each named as a stray. A row with no checkpoint gets a fresh work.md. A
# row any of whose sources is held is left whole for the next run. The review area gets an index note.

source "$(dirname "$0")/../lib.sh" "$@"
begin

level() {
  case $1 in
    *.*.* | *.regular) echo regular ;;
    *.*) echo project ;;
    *) echo territory ;;
  esac
}
value() { [ "$1" = - ] && echo null || printf '%s' "$1"; }

front_matter() {
  local id=$1 title=$2 project=$3 theme=$4 state=$5 hold=$6 release=$7 mark=$8 created=$9
  echo ---
  echo "id: $id"
  echo "level: $(level "$id")"
  echo "title: '$title'"
  [ "$project" = - ] || echo "project: $project"
  echo "theme: $(value "$theme")"
  echo "worker: agent"
  echo "supervisor: owner"
  echo "state: $state"
  [ "$state" = on-hold ] && printf 'hold:\n  reason: %s\n  release: %s\n' "$hold" "$release"
  echo "since: $NOW"
  echo "received: null"
  echo "beat: null"
  [ "$mark" = - ] || echo "mark: $mark"
  [ -z "$created" ] || echo "created_at: $created"
  echo ---
}

migrated() {
  printf '%s\n' "- MIGRATED - this file was $1 until the work migration of ${NOW%%T*}. At your next mark, cut it to next steps, Messages and the tags of parked queries, each linked to its report; move anything else to its durable home, then remove this line."
}

# held_row CHECKPOINT THREAD: why the row is held, if either source is.
held_row() {
  local path why
  for path in "$@"; do
    [ "$path" = - ] && continue
    if why=$(held "$path"); then echo "$path: $why" && return 0; fi
  done
  return 1
}

# +/_WORK/ holds work folders only, ki-checkpoint's STRUCTURE-1, and `+` working areas need no index note; the review
# area, which no checker reads, gets one listing why each folder is there.
say "Create the review area's index note"
{
  cat <<'NOTE'
# Work for review

Work folders the migration could not place with confidence. Each waits here for Kris's review and moves itself to `+/_WORK/` at its next mark, or is finished and deleted, with Git keeping it. This area is not counted, and its folders are not checked against the closed list until they leave it.

NOTE
  rows | awk -F '\t' '$2 == "_WORK_REVIEW" { printf "- [[%s/work|%s]] - %s\n", $1, $1, $13 }'
} | create +/_WORK_REVIEW/README.md

while IFS=$'\t' read -r id where confidence checkpoint thread project theme title state hold release mark reason; do
  dst=+/$where/$id
  say "$id -> $dst ($confidence)"
  if why=$(held_row "$checkpoint" "$thread"); then
    note "HELD, left for the next run ($why)"
    continue
  fi

  if [ "$checkpoint" != - ] && [ ! -e "$checkpoint" ] && [ -e "$dst/work.md" ]; then
    note "already migrated"
    [ "$MODE" = map ] && printf '%s\t%s\n' "$checkpoint" "$dst/work.md"
  elif [ "$checkpoint" != - ]; then
    move "$checkpoint" "$dst/work.md"
    file=$(at "$checkpoint" "$dst/work.md")
    {
      front_matter "$id" "$title" "$project" "$theme" "$state" "$hold" "$release" "$mark" \
        "$(awk '/^created_at:/ { print $2; exit }' "$file")"
      awk -v id="$id" -v line="$(migrated "\`$checkpoint\`")" '
        function out(text) { if (part == "next") next_steps = next_steps text "\n"; else if (part == "parked") parked = parked text "\n"; else dropped++ }
        NR == 1 && /^---$/ { skip = 1; next }
        skip && /^---$/ { skip = 0; next }
        skip { next }
        /^# / && !titled { titled = 1; part = "next"; next }
        /^## / {
          heading = substr($0, 4)
          if (heading ~ /^(Pick-up|Next step)/) part = "next"
          else if (heading ~ /^(Open|Parked) (questions|queries)/) part = "parked"
          else { part = "drop"; gone = gone (gone ? ", " : "") heading }
          next
        }
        part == "" { next }
        { gsub(/\]\(<?\.\.\//, "&../"); if (/^###+ /) { sub(/^###+ /, ""); $0 = "**" $0 "**" } out($0) }
        function trim(text) { sub(/^\n+/, "", text); sub(/\n+$/, "", text); return text == "" ? "None." : text }
        END {
          printf "\n# %s\n\n## Next steps\n\n%s\n\n## Messages\n\n%s\n\n## Parked\n\n%s\n", id, trim(next_steps), line, trim(parked)
          if (gone) printf "dropped, Git keeping them: %s (%d lines)\n", gone, dropped > "/dev/stderr"
        }
      ' "$file" 2> "$SCRATCH/dropped"
    } | replace "$file"
    [ -s "$SCRATCH/dropped" ] && note "$(cat "$SCRATCH/dropped")"
  elif [ "$MODE" != map ]; then
    {
      front_matter "$id" "$title" "$project" "$theme" "$state" "$hold" "$release" "$mark" "$NOW"
      printf '\n# %s\n\n## Next steps\n\n- %s\n\n## Messages\n\n' "$id" "$reason"
      migrated "new"
      printf '\n## Parked\n\nNone.\n'
    } | create "$dst/work.md"
  fi

  [ "$thread" = - ] && continue
  [ "$MODE" = map ] && printf '%s\t%s\n' "$thread" "$dst"
  [ "$MODE" = apply ] && printf '%s\t%s\n' "$thread" "$dst" >> "$MOVE_LOG"
  for path in "$thread"/* "$thread"/.[!.]*; do
    [ -e "$path" ] || continue
    name=$(basename "$path")
    case $name in
      decisions.md | *.report.md) move "$path" "$dst/$name" ;;
      *.brief.md) move "$path" "$dst/briefs/${name%.brief.md}.md" ;;
      *)
        note "stray outside the closed list: $path -> design/"
        move "$path" "$dst/design/$name"
        ;;
    esac
  done
  [ "$MODE" = apply ] && rmdir "$thread" 2> /dev/null || true
done < <(rows)

say "Retire the old areas"
for old in +/_CHECKPOINTS +/_THREADS; do
  left=$(find "$old" -mindepth 1 -not -name README.md -not -name .DS_Store 2> /dev/null | head -1)
  if [ "$MODE" = apply ] && [ -z "$left" ]; then
    [ -e "$old/README.md" ] && remove "$old/README.md"
  else
    note "$old keeps its README.md while anything is left in it"
  fi
done

say "By hand"
hand "+/_WORK/ki/work.md: cut the State of play body, which runs long, to next steps, Messages and parked tags at its first mark"
hand "+/_WORK/ki.mac-studio-setup/: its checkpoint says the decisions log is machine-local on sol; reconcile it with the tracked decisions.md"
hand "each work's first mark prunes its settled reports, under the Work Process"

commit "docs(work): checkpoints and thread folders become work folders"
