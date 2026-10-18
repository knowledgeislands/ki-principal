#!/usr/bin/env bash
# Phase 3 step 1: take the design folders out of Streams.
#
# The Model theme's territory-selection papers are deleted, their outcome being ADR-KI-PRINCIPAL-002 and Git keeping
# them. Each Project's design folder moves into its work folder, in +/_WORK or +/_WORK_REVIEW as the classification
# places the work. The two loose Mac Studio setup files go into its design folder, so the work folder keeps to the
# closed list. Merging hosts.md, folding decisions-in-force.md and demoting the Projects' extra sections are by hand.

source "$(dirname "$0")/../lib.sh" "$@"
begin

say "Delete the territory-selection design papers"
remove Streams/Initiatives/knowledge-islands-model/design

say "Move each Project's design folder into its work folder"
for project in agent-host mac-studio-setup paperclip-capture-and-rebuild ways-of-working; do
  move "Streams/Projects/$project/design" "$(area "ki.$project")/ki.$project/design"
done
for file in adobe-remove.sh favicons-headroom.svg; do
  move "Streams/Projects/mac-studio-setup/$file" "$(area ki.mac-studio-setup)/ki.mac-studio-setup/design/$file"
done

say "By hand"
hand "merge +/_WORK/ki.mac-studio-setup/design/hosts.md into Pillars/Engineering Practice/Architecture/Hosts, Roles and Layers.md, then git rm it"
hand "fold +/_WORK/ki.mac-studio-setup/design/decisions-in-force.md into the Mac Studio setup Project note's Notes, then git rm it"
hand "Mac Studio setup Project note: make ## Remit a ### under ## Notes"
hand "Paperclip capture and rebuild Project note: make ## Capture, ## Shut down, ## Design and ## Rebuild ### under ## Notes"
hand "point each design folder's design.md index at its new parent, the work file"

commit "docs(streams): move Project design folders into their work folders"
