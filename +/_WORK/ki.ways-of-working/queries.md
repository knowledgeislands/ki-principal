# ki.ways-of-working queries

## Open

### WORKTREE-AUDIT - Write down the worktree audit recipe

Reviewed (cg-review), high. Explained again to Kris 20 October. a) harness record adds the isolated-home plus `ki repo repair` recipe to `AGENTS.md` Verification and `ki-delegation`, validated against CI's pinned `ki` and never touching the real registry; b) `ki repo audit` reports it as one setup finding.

### CAPTURE-ORIGIN - Checkable capture gate with an origin field

Explained again to Kris 20 October; HANDOFF-AS-MESSAGE now carries most of it. a) drop it, the handoff rule already stops runs creating records; b) add an `origin` field and a check.

### STASH-DROP - Drop two old ki-principal stashes

Reviewed (stash-review: both fully on main), high. a) drop `stash@{0}` and `stash@{1}`; b) keep them.

### MATURITY-DECLINE - How the island-maturity record reads "decline"

Reviewed (md-review agrees, five conditions: full precedence with failure first, latest whole-repository audit, rollout consequence accepted, wording replaced in record and standard, four reader cases tested): high. a) decline is any WARN and no failure in the latest full audit, no age; b) 30-day tolerance with audit history in tools-ki. Unblocks KI-HARNESS-GOV-223 Ready.

### GFM-HOSTING-RULES - Keep or remove the three `main` rulesets

Read by harness-moves: classic protection off everywhere; rulesets on ki-agentic-harness, homebrew-tap and apps-knowledgeislands.info, all with admin bypass. a) leave as is, high; b) remove the harness ruleset.

### MARK-HABIT - How marks get struck

a) strike a mark at every send and every owner answer turn; Kris says "mark" only for a clean line; b) Kris announces a mark before substantive answers.

### SINGLE-FIGURES - What single figures counts

a) each Knowledge Islands repository under ten; b) the territory as a whole.

### SIZED-EMBEDS - from gfm-convert

Reviewed (gfm-review-2 agrees): high. a) plain GFM images, Format drops the width-800 rule; b) keep as Obsidian-only exceptions; c) HTML `<img>`.

### TEMPLATE-LINKS - from gfm-convert

Reviewed (gfm-review-2 agrees): high. a) rewrite the 14 placeholders as GFM links; b) leave wikilinks for the touch rule.

### LINK-REVIEW-NAME - from gfm-convert

Reviewed (gfm-review-2 agrees, rename bounded and every reference updated together): high. a) rename the Activity Link Review, trigger "ki link review"; b) keep the name; c) retire it.

### RENDER-CHECK - from gfm-convert

Reviewed (gfm-review-2 agrees): high. a) open the Library link and an alert note in GitHub, Obsidian, Zed and the Observatory before accepting KI-PRINCIPAL-OPS-014; b) accept without, noting the Observatory's fragment loss.

### WORKTREE-INTEGRATE - from worktree-flow

Reviewed (wf-review agrees, on condition the primary-checkout write window is serialised and independent review still precedes acceptance): high. a) every worktree run fast-forwards its own branch into local `main` after gates pass, else keeps the worktree and reports it stranded; b) runs stop at the branch and a merge run follows.

### WORKTREE-START - from worktree-flow

Reviewed (wf-review agrees; F3 and F5 confirmed needed by source inspection): high. a) start the trial now in code repositories under F1 and F4, ki-principal once F5 lands; b) wait for F2, F3 and F5.

### SWEEP - Roadmap sweep batches

sweep-review kept most merges and cancels; sweep-queries recounts and drafts the accept, merge, convert and cancel queries for Kris.

## Parked

- NO-GATE (with PKGLESS-GATE) - project shape commit gate; Kris will come back to it. a) `ki repo audit --skill ki-repo` staged, check-only; review prefers widening KI-HARNESS-GOV-225.
