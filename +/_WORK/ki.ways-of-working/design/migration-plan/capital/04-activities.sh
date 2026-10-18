#!/usr/bin/env bash
# Phase 3 step 4: the recurring Activities name the Model theme in place of the Initiative.
#
# Saying in each Activity that the territory's regular work, ki.regular, is its home is by hand.

source "$(dirname "$0")/../lib.sh" "$@"
begin

say "Name the theme in each Activity"
printf '%s\n' 's~^initiative: knowledge-islands-model$~theme: model~' 's~^initiative: platform-foundations$~theme: foundations~' > "$SCRATCH/activity.sed"
while read -r note; do edit "$note" "$SCRATCH/activity.sed"; done < <(grep -rl -E '^initiative: ' Admin/Operations/Activities | sort)

say "By hand"
hand "Briefings Activity, Schedule and Tending Activity: name the territory's regular work, ki.regular, as each one's home, taking the Model page's Recurring work paragraph"

commit "docs(admin): activities name the Model theme"
