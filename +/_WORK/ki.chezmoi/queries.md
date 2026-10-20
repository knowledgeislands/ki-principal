# ki.chezmoi queries

## Open

- APPLY (drift-fix, high): apply four drifted targets, all committed source; with Kris 05:08.
- ACCEPT-BATCH (accept-prep, high): accept KB-DOTFILES-UE-077 and KB-DOTFILES-UE-093; with Kris 05:08.
- CLEAR-BATCH (accept-prep, high): merge UE-087 into UE-101, UE-097 to Hold, five sizes; with Kris 05:08.
- TIDY: with Kris.
- COMMENT-FIELD (merged with RATIONALE-FIELD): comment-blind high for a new `comment` field, staged rationale deprecation; with Kris 05:23.
- CORE-SET-COMMENTS: comment-blind high, leave in the worksheet Kris reviews anyway; not raised separately.
- KIND-SOURCE, RATIONALE-FILTER (purpose-render; site commit `4701e8f`, unpushed): reviewed by site-blind (agrees on COMMENT-FIELD and KIND-SOURCE; RATIONALE-FILTER disagrees: remove now, high); with Kris 05:15.
- SPARK-REMOVE (spark-history high; spark-blind medium, retire, missing option: deselect and defer uninstall): with Kris 05:10.
- RAT-UNCONFIRMED, RAT-READING: superseded by Decisions 179 and 181. SPARK-TOOL (rig-purpose, retire, medium; overlaps Alfred) folded into SPARK-REMOVE.
- FIREWALL-EXPOSURE (rig-purpose): `exposed-beyond-tailnet` seen 05:16; coordinator re-check 05:18 shows only `anchor-changed`. Transient; not raised as a query; reported to Kris.
- APPLY: rig-purpose done (chezmoi `a59b19f`, `c65e539`, `d46a2ed`; doctor 4 before and after), so the fragments 10, 15, 16, 40 can join the apply.

## Held

None. Batch 1 (hooks) is decided in Decisions 164 to 172.
