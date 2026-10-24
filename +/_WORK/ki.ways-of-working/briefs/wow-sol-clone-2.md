# Clone terra's new repositories on sol

Kris, 23 October 2026: sol should have every repository terra has. Clone these fourteen into `/Users/krisbrown/workspaces/<path>` on sol:

humans-not-robots/apps-5g-emerge.io, apps-demo.5g-emerge.io, apps-p2ms3.5g-emerge.io, apps-phase2.5g-emerge.io, apps-phase3.5g-emerge.io, apps-eit.humansnotrobots.be, apps-home.humansnotrobots.be, apps-hr.humansnotrobots.be, apps-product.humansnotrobots.be, apps-sales.humansnotrobots.be, apps-sky.humansnotrobots.be, apps-snowflake.humansnotrobots.be; knowledge-islands/packages-portal-commons; personal/apps-legal.midnight.ninja.

## How

- If Rig or the KI local registry already declares these repositories and has a clone or apply step for them, use it (dry run first), so sol and terra stay declared the same way. Otherwise find each remote by the convention its territory's existing checkouts use (`git remote get-url origin` on a sibling, `gh repo view`) and `git clone` it. Do not guess a remote: if one cannot be found, skip it and say so.
- After cloning, run each repository's usual setup only if a sibling's README or `.ki.toml` makes it a standard step (for example installing hooks); otherwise stop at the clone.
- Read-only check, nothing changed: for the four replaced checkouts `humans-not-robots/5g-emerge-apex`, `5g-emerge-demos`, `5g-emerge-phase2`, `5g-emerge-phase3`, report whether each has unpushed commits, stashes or uncommitted files, since they had commits on 22-23 October.

## Bounds

Do not delete, move or change any existing checkout, including the four replaced ones and `personal/dotfiles`. No push, no commit in any repository. Smallest change that does the job.

## Report

The run report the launcher names, first line `VERDICT: <done|partial|blocked> · confidence <high|medium|low> - <one line>`; then one line per repository cloned or skipped, and the four replaced checkouts' state.

## Authority over the footer

This task's explicit rules override the generic footer line banning remote calls, as ki-delegation allows: Kris asked on 23 October 2026 for sol to get these repositories. You may make the read-only remote calls needed to clone them: `git fetch`, `git clone`, `gh repo view`/`gh repo list`, and the clone step of `mgit` or Rig. Every other remote call stays banned: no push, no remote write, no release.

## Addendum - after wow-sol-clone

wow-sol-clone found none of the fourteen in local Rig configuration or the territories' `.mgit.toml` on sol. terra may declare them in a newer `.mgit.toml` already on origin: fetch each territory's principal repository (humans-not-robots/hnr-principal, knowledge-islands/ki-principal, personal/personal-principal, or wherever `.mgit.toml` lives) and compare `origin/main`'s `.mgit.toml` with the local one. If the declarations are on origin, prefer the repository's own `mgit` clone step reading them; do not pull into a checkout that has uncommitted or staged changes, read the file from `origin/main` instead. Otherwise clone each from the remote its siblings' convention gives, confirmed with `gh repo view`.
