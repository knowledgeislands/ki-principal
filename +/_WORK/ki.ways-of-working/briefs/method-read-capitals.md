# method-read-capitals

Run for ki.ways-of-working, authorised by Kris on 2026-10-19 at 21:34 BST: "you could add something about it to the SoP work pacjage in all the capitals".

## Task

1. Find every territory capital other than Knowledge Islands Principal (already done) from the local registry (`ki` registry or Known Lands); expected: er-principal, hnr-principal, legal-principal, personal-principal, tmx-principal, va-principal. Report any capital that has none.
2. In each, find the State of play work package: the `+/_WORK/<id>/` whose `work.md` declares `level: territory`. Append one line to its `messages.md`, keeping the file's existing shape:

   `- 2026-10-19 21:34 BST · from ki.ways-of-working (Knowledge Islands Principal) · METHOD-READ: several works recorded a UTC time in `state.md` `method_read`, where the `ki-work-package` standard expects the short harness revision whose method the work last read. At your next refresh, check each of your works and have any with a non-revision value set it at its own next refresh.`
3. In each repository: commit only that file by explicit path, subject `docs(work): <sop id> message from ki.ways-of-working, METHOD-READ`; pull with rebase and push fast-forward only when your commit alone is stacked; otherwise do not push and name the other commits. Never `--no-verify` or force-push. If a repository is dirty in that file or a hook fails, stop for that repository and report it.

## Report

One line per capital: SoP id, commit, pushed or why not.
