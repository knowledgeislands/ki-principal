#!/usr/bin/env bash
# Phase 3 step 2: Initiatives become themes in Streams/Themes, under the short names Kris chose (WORK-THEME-SLUGS).
#
# Each Initiative note moves to Streams/Themes/<slug>.md, its front matter retyped and renamed, and every live
# wikilink to it is rewritten to the path form [[Themes/<slug>|<Title>]]. The Work Process tree is brought into line.
# Rewriting each page as a theme page (why a theme, what matters, direction, common guidance) is by hand.

source "$(dirname "$0")/../lib.sh" "$@"
begin

old=Streams/Initiatives
new=Streams/Themes

say "Move the Initiative notes to theme pages"
move $old/Initiatives.md $new/Themes.md
move $old/knowledge-islands-model/knowledge-islands-model.md $new/model.md
move $old/platform-foundations.md $new/foundations.md
move $old/rig.md $new/rig.md
move $old/techne.md $new/techne.md

say "Retype and rename the theme pages"
cat > "$SCRATCH/page.sed" <<'SED'
s~^note_type: streams/initiative$~note_type: streams/theme~
s~^slug: knowledge-islands-model$~slug: model~
s~^title: Knowledge Islands model$~title: Model~
s~^# Knowledge Islands Model$~# Model~
s~^slug: platform-foundations$~slug: foundations~
s~^title: Platform foundations$~title: Foundations~
s~^# Platform Foundations$~# Foundations~
s~^# Initiatives$~# Themes~
SED
edit "$(at $old/Initiatives.md $new/Themes.md)" "$SCRATCH/page.sed"
edit "$(at $old/knowledge-islands-model/knowledge-islands-model.md $new/model.md)" "$SCRATCH/page.sed"
edit "$(at $old/platform-foundations.md $new/foundations.md)" "$SCRATCH/page.sed"
edit "$(at $old/rig.md $new/rig.md)" "$SCRATCH/page.sed"
edit "$(at $old/techne.md $new/techne.md)" "$SCRATCH/page.sed"

say "Rewrite live wikilinks to the theme pages"
cat > "$SCRATCH/links.sed" <<'SED'
s~\[\[(Streams/)?(Initiatives/)?knowledge-islands-model(/knowledge-islands-model)?(\|[^]]*)?\]\]~[[Themes/model|Model]]~g
s~\[\[(Streams/)?(Initiatives/)?platform-foundations(\|[^]]*)?\]\]~[[Themes/foundations|Foundations]]~g
s~\[\[(Streams/)?(Initiatives/)?rig(\|[^]]*)?\]\]~[[Themes/rig|Rig]]~g
s~\[\[(Streams/)?(Initiatives/)?techne(\|[^]]*)?\]\]~[[Themes/techne|Techne]]~g
s~\[\[(Streams/)?Initiatives(/Initiatives)?(\|[^]]*)?\]\]~[[Themes\3]]~g
SED
while read -r note; do edit "$note" "$SCRATCH/links.sed"; done < <(live_notes)

say "Bring the Work Process tree into line"
cat > "$SCRATCH/tree.sed" <<'SED'
s~^(│   ├── )knowledge-islands-model\.md         (theme page)~\1model.md                           \2~
s~^(│   ├── )platform-foundations\.md$~\1foundations.md~
s~^(│   ├── ways-of-working\.md +theme: )knowledge-islands-model$~\1model~
SED
edit "Pillars/Philosophy/Model/Processes/Work Process/Work Process.md" "$SCRATCH/tree.sed"

say "By hand"
hand "rewrite each theme page as a theme page: why a theme, what matters, direction, common guidance; no Project or design pointers"
hand "move the Model page's Recurring work paragraph, and Foundations' recurring-upkeep paragraph, to the Activities they describe"
hand "rewrite Themes.md (was Initiatives.md) as the theme index; reword Initiative to theme in the prose the link rewrite leaves"
hand "Streams/Roadmap/Roadmap.md: [[Themes|Initiative]] reads as theme"
hand "git rm the empty Streams/Initiatives folder once nothing is left in it"

commit "docs(streams): Initiatives become themes in Streams/Themes"
