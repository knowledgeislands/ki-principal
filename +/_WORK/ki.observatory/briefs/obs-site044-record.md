# obs-site044-record - bring KI-WEBSITE-SITE-044 up to date for acceptance

Repository: apps-knowledgeislands.info. KI-WEBSITE-SITE-044 (design v1) says In progress with work uncommitted on `feat/design-v1`, but the work is on `main` in 5370af7 and bc6dbdf, the branch is fully merged and its last unticked step ("commit the ledger advance, then this change") is done. Verify those facts against Git and the site's checks (build, tests, lint, roadmap audit). If they hold, update the record to match (tick the step, cite the commits, remove the uncommitted-branch wording) and move it to Awaiting review under `ki-implement`'s closing rules; do not accept it and do not delete the branch. If they do not hold, change nothing and report what differs. Commit by explicit path, one commit, do not push. Create no records. Never run `ki repo conform` without `--dry-run`.

## Relaunch, 00:15 BST

The hooks conversion is now committed (783effb) and the tree was clean at 00:14, but `node_modules` was left nearly empty. Before the checks: if `git status` is still clean, run `bun install --frozen-lockfile` to restore dependencies from the committed lockfile, then run the checks. If the tree is dirty or the install would change `bun.lock`, stop and report.
