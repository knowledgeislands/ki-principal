# ki.ways-of-working queries

## Open

### TOUCH-SCOPE - what "touch" converts

since 2026-10-19 21:36 BST · from gfm-scope · blind review (gfm-review, Codex) at 21:40 BST: agrees on the whole file, at lower confidence

**Context:** "If you touch a file, it changes" could mean the whole file or only the edited lines. Scoping said whole file at high. The review agrees but at medium: a touched file may hold unresolved links, generated content or constructs with no GFM form, so the converter must stop and flag those rather than rewrite them, and generated or protected files need rules before the rule switches on.

**Query:** Does editing a file convert the whole file, once the safe converter exists?

**Options:**

a) (recommended, confidence medium - reviewed: the review backs whole-file conversion only once the converter refuses unsafe files; scoping had it high) whole file in the same change, via the converter; an unsafe file is flagged or given a recorded exception

b) edited lines only during the transition, the rest left for a batch

## Parked

Nothing parked.
