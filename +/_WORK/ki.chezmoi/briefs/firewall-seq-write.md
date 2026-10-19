# Brief: firewall-seq-write

Work: KI > Rig > chezmoi in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`. Authority: Kris's go-ahead for the attended Terra firewall rehearsal (19 October, 21:04 BST), with the blind review's RESEQ b), high, applied. You write the sequence; you run nothing mutating, and nothing with `sudo`, on any machine. Commit nothing.

Read first: `/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-seq-review.report.md` (the six corrections; implement all of them), `firewall-freeze.report.md` (the empty-`$L` shutdown) and `firewall-rehearse.report.md` (recorded pre-state and expected eight rules), all in `/Users/krisbrown/.local/state/ki/agents/chezmoi/`.

Write `/Users/krisbrown/.local/state/ki/agents/chezmoi/firewall-rehearse-v2.md`: the sequence Kris pastes, block by block, terminal A being `ssh -t terra` from Sol and terminal B a plain shell on Sol. Requirements:

- No shell variable or state carried between blocks; every label and path literal.
- Every block safe when pasted alone, into the wrong shell or host, twice, or out of order: each mutating block runs inside a subshell or function that checks host identity (Terra's hardware UUID or serial, which you read now over SSH without `sudo`), that it is an SSH session, and that the expected pre-state for its phase holds, and otherwise prints why and changes nothing. A refused block must never close Kris's shell.
- Flush filter rules only in the named anchor; record pf enable references before and after; fallback only reloads the anchor when pf is already enabled, otherwise stops.
- Fresh SSH checks from Sol with `-o ControlMaster=no -o ControlPath=none -o ConnectTimeout=10 -o BatchMode=yes`, requiring exit 0 and `terra`.
- Restore proven by bounded polling for a new daemon invocation exiting 0, rules matching the recorded eight, the parent ruleset calling the child anchor, and pf still enabled.
- Each block says in one line what Kris should see, and what to do if they do not (`stop and paste`).

Prove the guards: paste each block's guard on Sol locally and confirm it refuses and leaves the shell open; run any non-`sudo`, read-only part over SSH on terra. Keep it short enough to paste. Report under the owner report with the work's report heading and `› firewall-seq-write`, naming anything in the review you could not implement.
