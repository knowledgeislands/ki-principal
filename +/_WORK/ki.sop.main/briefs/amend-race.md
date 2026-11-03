# amend-race (ki.sop.main)

Goal: add an amend guard to the `ki-git` skill in ki-agentic-harness, as Kris decided under ACCEPT-BY-CRITERIA a) (31 Oct): "amend in a shared checkout only inside the serialised write window after confirming `HEAD` is this session's own unpushed commit, otherwise make a new commit". Cause: in shared hnr-principal a run amended `HEAD` after another package's commit landed, so `a1d61be4` became `21f4f02b` with attribution lost. Also add, in the same change, a check or line that flags `pull.autostash` / `rebase.autoStash` as conflicting with the never-stash rule (HOOK-STASH a), 1 Nov): on 3 Nov a plain pull in a shared checkout autostashed another session's uncommitted line and conflicted.

Follow the harness's own AGENTS.md, regenerate any generated surfaces, run its checks and tests. Do not touch other skills' files. Commit by explicit path, push fast-forward only (pull with `-c pull.autostash=false -c rebase.autoStash=false`); never stash, rebase a dirty tree, reset, force or --no-verify.

Report: run report with the commit, checks, and any query for Kris in Context/Query/Options form.
