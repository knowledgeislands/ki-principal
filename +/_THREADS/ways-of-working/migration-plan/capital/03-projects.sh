#!/usr/bin/env bash
# Phase 3 step 3: Project notes go flat in Streams/Projects, each naming its theme.
#
# The four foldered Project notes move up a level, losing one ../ from each relative link. Every Project note's
# initiative key becomes its theme key, and the Projects index drops the sentences that name each Project's
# Initiative. Run after 01-design-tidy, which empties the Project folders of their design papers.

source "$(dirname "$0")/../lib.sh" "$@"
begin

dir=Streams/Projects

say "Flatten the foldered Project notes"
printf '%s\n' 's~(\]\(<?)\.\./~\1~g' > "$SCRATCH/up.sed"
for project in agent-host mac-studio-setup paperclip-capture-and-rebuild ways-of-working; do
  move "$dir/$project/$project.md" "$dir/$project.md"
  edit "$(at "$dir/$project/$project.md" "$dir/$project.md")" "$SCRATCH/up.sed"
done

say "Name each Project's theme"
cat > "$SCRATCH/theme.sed" <<'SED'
s~^initiative: knowledge-islands-model$~theme: model~
s~^initiative: platform-foundations$~theme: foundations~
s~^initiative: (rig|techne)$~theme: \1~
SED
while read -r note; do edit "$note" "$SCRATCH/theme.sed"; done < <(find $dir -name '*.md' -not -path '*/design/*' | sort)

say "Drop the Initiative sentences from the Projects index"
printf '%s\n' 's~ It sits under \[\[[^]]*\]\]\.~~g' > "$SCRATCH/index.sed"
edit $dir/Projects.md "$SCRATCH/index.sed"

say "By hand"
hand "Streams/Projects/ways-of-working.md: drop [[ways-of-working/design/design|design folder]], since a Project note does not link down"
hand "Streams/Projects/Projects.md: rewrite the Initiatives section and the overview's Initiative wording as themes; the secrets-hygiene line keeps a reason, so reword it"
hand "Streams/Streams.md: ## Initiatives becomes ## Themes, its paragraph describing theme pages"
hand "Streams/Projects/mac-studio-setup.md: repoint [[hosts]] at the Hosts, Roles and Layers note and drop [[decisions-in-force]], once step 1's merges are done"
hand "remove each now-empty Project folder"

commit "docs(streams): flat Project notes name their themes"
