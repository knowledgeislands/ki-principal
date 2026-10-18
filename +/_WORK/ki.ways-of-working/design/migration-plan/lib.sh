# Shared helpers for the work-migration plan scripts, sourced by every step.
#
# Every step is a dry run unless it is given --apply: it prints each command it would run and a unified diff of
# each edit, and changes nothing. --map prints the old and new repository-relative path of each planned move, tab
# separated, for the citations step. With --apply a step stages its own changes as it goes and commits them by
# explicit path at its end, through the repository's normal gate; MIGRATE_NO_COMMIT=1 leaves them staged instead.
#
# A step refuses to apply while anything is already staged, so it never sweeps another session's staged work into
# its commit. A path is held, and never moved or edited, when defer.list names it for this repository or when it
# has unstaged or untracked changes, which are another session's.

set -euo pipefail

PLAN_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
MODE=dry-run
for arg in "$@"; do
  case $arg in
    --apply) MODE=apply ;;
    --dry-run) MODE=dry-run ;;
    --map) MODE=map ;;
    -h | --help)
      sed -n '2,/^$/s/^# \{0,1\}//p' "$0"
      exit 0
      ;;
    *)
      echo "unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

STEP_DIR=$(cd "$(dirname "$0")" && pwd)
REPO=${REPO:-$(git -C "$PLAN_DIR" rev-parse --show-toplevel)}
REPO_NAME=${MIGRATE_REPO_NAME:-$(basename "$REPO")}
cd "$REPO"
NOW=${MIGRATE_NOW:-$(date -u +%Y-%m-%dT%H:%M:%SZ)}
TRAILER=${MIGRATE_TRAILER:-'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'}
CLASSIFICATION=$PLAN_DIR/classification.tsv
# The plan folder is this migration's own, so its new files never hold the folder that carries it.
case $PLAN_DIR in "$REPO"/*) OWN=(":(exclude)${PLAN_DIR#"$REPO"/}") ;; *) OWN=() ;; esac

mkdir -p "$REPO/tmp/ways-of-working"
SCRATCH=$(mktemp -d "$REPO/tmp/ways-of-working/migrate-plan.XXXXXX")
trap 'rm -rf "$SCRATCH"' EXIT
: > "$SCRATCH/touched"

say() { [ "$MODE" = map ] || printf '%s\n' "$*"; }
note() { [ "$MODE" = map ] || printf '  - %s\n' "$*"; }
hand() { [ "$MODE" = map ] || printf '  HAND: %s\n' "$*"; }

begin() {
  [ "$MODE" = map ] && return 0
  printf '== %s (%s) in %s at %s\n' "$(basename "$0")" "$MODE" "$REPO_NAME" "$NOW"
  if [ "$MODE" = apply ] && ! git diff --cached --quiet; then
    echo "refusing to apply: the index already holds staged changes" >&2
    exit 1
  fi
}

# deferred PATH: true when defer.list names PATH, a parent of it or a path inside it, for this repository.
deferred() {
  local path=$1 repo entry
  while read -r repo entry; do
    case $repo in '' | '#'*) continue ;; esac
    [ "$repo" = "$REPO_NAME" ] || continue
    case $path in "$entry"*) echo "in flight: $entry" && return 0 ;; esac
    case $entry in "$path"/*) echo "holds in-flight $entry" && return 0 ;; esac
  done < "$PLAN_DIR/defer.list"
  return 1
}

# held PATH: deferred, or carrying another session's unstaged or untracked changes.
held() {
  local path=$1
  deferred "$path" && return 0
  if ! git diff --quiet -- "$path" ${OWN[@]+"${OWN[@]}"} 2> /dev/null; then echo "unstaged changes" && return 0; fi
  if [ -n "$(git ls-files --others --exclude-standard -- "$path" ${OWN[@]+"${OWN[@]}"})" ]; then echo "untracked files" && return 0; fi
  return 1
}

touched() { printf '%s\n' "$@" >> "$SCRATCH/touched"; }

# Every applied move is logged, so the citations step can rewrite paths that earlier steps or runs have moved.
MOVE_LOG=$REPO/tmp/ways-of-working/migration-moves.tsv

act() {
  printf '  %s\n' "$*"
  if [ "$MODE" = apply ]; then "$@"; fi
  return 0
}

# move SRC DST: git mv, creating DST's parent.
move() {
  local src=$1 dst=$2 why
  if [ "$MODE" = map ]; then
    deferred "$src" > /dev/null || printf '%s\t%s\n' "$src" "$dst"
    return 0
  fi
  if [ ! -e "$src" ]; then note "absent, skipped: $src" && return 0; fi
  if why=$(held "$src"); then note "SKIP $src ($why)" && return 0; fi
  if [ -e "$dst" ]; then note "target exists, skipped: $src -> $dst" && return 0; fi
  act mkdir -p "$(dirname "$dst")"
  act git mv -- "$src" "$dst"
  [ "$MODE" = apply ] && printf '%s\t%s\n' "$src" "$dst" >> "$MOVE_LOG"
  touched "$src" "$dst"
}

# remove PATH: git rm -r.
remove() {
  local path=$1 why
  [ "$MODE" = map ] && return 0
  if [ ! -e "$path" ]; then note "absent, skipped: $path" && return 0; fi
  if why=$(held "$path"); then note "SKIP $path ($why)" && return 0; fi
  act git rm -r -q -- "$path"
  touched "$path"
}

# create PATH < content: write a new file and stage it; the dry run prints the content.
create() {
  local path=$1
  [ "$MODE" = map ] && { cat > /dev/null; return 0; }
  cat > "$SCRATCH/create.out"
  if [ -e "$path" ]; then note "exists, left: $path" && return 0; fi
  echo "  create $path"
  sed 's/^/    | /' "$SCRATCH/create.out"
  if [ "$MODE" = apply ]; then
    mkdir -p "$(dirname "$path")"
    cat "$SCRATCH/create.out" > "$path"
    git add -- "$path"
    touched "$path"
  fi
}

# edit FILE SEDSCRIPT: apply an extended-regex sed script; the dry run prints the unified diff.
edit() {
  local file=$1 script=$2 why
  [ "$MODE" = map ] && return 0
  [ -f "$file" ] || { note "absent, skipped: $file" && return 0; }
  sed -E -f "$script" "$file" > "$SCRATCH/edit.out"
  cmp -s "$file" "$SCRATCH/edit.out" && return 0
  if why=$(held "$file"); then note "SKIP edit $file ($why)" && return 0; fi
  echo "  edit $file"
  diff -u --label "a/$file" --label "b/$file" "$file" "$SCRATCH/edit.out" | sed 's/^/    /' || true
  if [ "$MODE" = apply ]; then
    cat "$SCRATCH/edit.out" > "$file"
    git add -- "$file"
    touched "$file"
  fi
}

# re TEXT and rep TEXT: escape TEXT for a sed -E pattern or replacement delimited by #.
re() { printf '%s' "$1" | sed -e 's/[][\.*^$+?(){}|#/]/\\&/g'; }
rep() { printf '%s' "$1" | sed -e 's/[\&#]/\\&/g'; }

# column ID N: field N of the classification row for work ID.
column() { awk -F '\t' -v id="$1" -v n="$2" '$1 == id { print $n }' "$CLASSIFICATION"; }

# area ID: the folder a work id goes to, +/_WORK or +/_WORK_REVIEW.
area() { printf '+/%s' "$(column "$1" 2)"; }

# rows: the classification rows, without the header.
rows() { awk -F '\t' 'NR > 1 && $1 != ""' "$CLASSIFICATION"; }

commit() {
  local subject=$1
  [ "$MODE" = apply ] || return 0
  sort -u "$SCRATCH/touched" | sed '/^$/d' > "$SCRATCH/pathspec"
  if [ ! -s "$SCRATCH/pathspec" ]; then echo "nothing to commit" && return 0; fi
  if [ -n "${MIGRATE_NO_COMMIT:-}" ]; then echo "left staged (MIGRATE_NO_COMMIT)" && return 0; fi
  printf '%s\n\n%s\n' "$subject" "$TRAILER" > "$SCRATCH/message"
  git --literal-pathspecs commit -q -F "$SCRATCH/message" --pathspec-from-file="$SCRATCH/pathspec"
  echo "committed: $subject"
}

# at SRC DST: DST once an earlier step has moved SRC there, else SRC; a dry run edits each note where it stands.
at() { if [ -e "$2" ]; then printf '%s' "$2"; else printf '%s' "$1"; fi; }

# live_notes: the Markdown notes a rewrite may change. History is left as it stands: the Calendar, roadmap records,
# reports, decisions logs, briefs and design papers.
live_notes() {
  {
    printf '%s\n' AGENTS.md CLAUDE.md Streams/Roadmap/Roadmap.md
    find Admin Pillars Streams +/_CHECKPOINTS +/_WORK +/_WORK_REVIEW -name '*.md' 2> /dev/null || true
  } | grep -v -E '(^Streams/Roadmap/.+/|^Streams/Roadmap/KI-|/design/|\.report\.md$|/decisions\.md$|/briefs/|\.brief\.md$)' | sort -u
}

# replace FILE < content: replace FILE's content; the dry run prints the unified diff.
replace() {
  local file=$1 why
  [ "$MODE" = map ] && { cat > /dev/null; return 0; }
  cat > "$SCRATCH/replace.out"
  cmp -s "$file" "$SCRATCH/replace.out" && return 0
  if why=$(held "$file"); then note "SKIP edit $file ($why)" && return 0; fi
  echo "  edit $file"
  diff -u --label "a/$file" --label "b/$file" "$file" "$SCRATCH/replace.out" | sed 's/^/    /' || true
  if [ "$MODE" = apply ]; then
    cat "$SCRATCH/replace.out" > "$file"
    git add -- "$file"
    touched "$file"
  fi
}
