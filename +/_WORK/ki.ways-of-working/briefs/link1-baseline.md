# link1-baseline

Fix run for ki.ways-of-working in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, under Kris's GFM-ORDER a) (2026-10-19 22:00 BST), whose review required a recorded baseline for pre-existing failures.

## Problem

Harness `012090a2` made `ki-repo-kb` LINK-1 resolve every internal link in exact case. Existing islands hold unresolved, wrong-case and template links (ki-principal about 29, personal-principal about 635), so their full `ki repo audit` now fails (ki-principal FAIL=1 at 22:08 BST) before any conversion has started.

## Task

1. Keep LINK-1 failing exactly where it failed before `2d28656f` (ambiguous wikilinks); report the new resolution findings (unresolved, wrong case) at WARN, so no island turns red until it is converted. If the rubric supports an explicit opt-in to strict resolution, add it as a repository-level `.ki.toml` setting for converted islands; otherwise say so and stop at WARN.
2. Prove it: run the full `ki repo audit` with the harness checkout on ki-principal, personal-principal and hnr-principal, and compare each with the result at `9c17df3c` (no new FAIL). Add fixtures.
3. Run the harness tests, type check and audits; regenerate surfaces. Commit by explicit path; pull with rebase and push fast-forward only when your own commits alone are stacked, else name the others. Never `--no-verify` or force-push. Edit nothing outside the harness.

## Report

Commits, the before-and-after audit lines per island, pushed or why not, queries with options.
