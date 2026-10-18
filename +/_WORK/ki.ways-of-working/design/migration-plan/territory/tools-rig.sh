#!/usr/bin/env bash
# Phase 4, tools-rig: its roadmap records name the Rig theme in place of the Rig Initiative.
#
# KI-TOOL-RIG-CORE-057 cites a ki-principal mac-studio-setup report deleted before the migration, as history in its
# context, and is left as it stands.

REPO=${REPO:-/Users/krisbrown/workspaces/knowledge-islands/tools-rig}
source "$(dirname "$0")/../lib.sh" "$@"
begin

say "Name the theme in each roadmap record"
printf '%s\n' 's~^initiative: rig$~theme: rig~' > "$SCRATCH/theme.sed"
while read -r record; do edit "$record" "$SCRATCH/theme.sed"; done < <(git grep -l -E '^initiative: rig$' -- docs/roadmap | sort)

say "By hand"
hand "apply after tools-ki accepts theme on roadmap records, so ki repo audit does not flag the key as unknown"
hand "tools-rig is ahead of origin by its own session's commits; push them first or apply on top and name them"

commit "docs(roadmap): records name the Rig theme"
