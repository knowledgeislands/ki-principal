# wow-hnr-level

## Goal

Level the primary hnr-principal checkout with `origin/main` (`bb404954` or later). Its local `main` holds `6043f001`, a line our run wrote and has since published, rewritten as `bb404954`; the checkout is otherwise clean and 89 behind.

## Do

1. Confirm the tree is clean and that `6043f001`'s patch is on `origin/main` (`git cherry origin/main main` shows it as `-`).
2. Run `git -C <checkout> pull -q --rebase`, which drops the already-applied commit. Do not use `reset --hard`.
3. Confirm `main` equals `origin/main` and the tree is clean.
4. Stop without changing anything if the tree is dirty, if `git cherry` does not show the patch as applied, if any other local commit exists, or if the rebase conflicts.

## Rules

Touch only that branch pointer by the rebase above. No push, no other file, no other repository.

## Report

Owner report: Done, In Progress, Queries.
