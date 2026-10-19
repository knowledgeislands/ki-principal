# obs-triage-apply - apply Kris's triage answers

Repository: apps-observatory.local, `docs/roadmap/`. Kris answered on 2026-10-19 "go ahead with recommendations" (TRIAGE-ANSWERS in ki-principal `+/_WORK/ki.observatory/decisions.md`; read it). Apply exactly, by hand where `ki repo roadmap promote` refuses, following `ki-next` for adoption and horizons and `ki-accept` for closing a record as merged:

1. Adopt at `now`: KI-OBSERVA-VIS-043, BRG-006, APP-045, VIS-044, BRG-005. In BRG-005 record that the way-in field is out of scope and waits with KI-OBSERVA-OPS-004; scope and withheld-inputs fields stay in.
2. Adopt at `next`: APP-044, VIS-041, VIS-022; at `soon`: OPS-003. Record in APP-044 that step 3 counts as shipped once the Known Lands chart (VIS-030 minimal), the Act board parts (BRG-005) and commit authors (VIS-044) land; switchboard and tailnet view do not gate it.
3. Merge KI-OBSERVA-VIS-033 into APP-044 as a second rename step (Review queue to Waiting for you, `?view=review` redirected), carrying VIS-033's acceptance and noting the rename needs Kris's own go; close VIS-033 as merged with a pointer to APP-044. Do not delete it.
4. Hold, each with its own conditions written in the record: BRG-004 (BRG-006, harness `feedback/` kind KI-HARNESS-GOV-219, harness accepting the owner via the Observatory as a messages sender); INT-003 (rest of step 3, Git view, own approval of later phases); OPS-004 and VIS-029 (Host network unit 4); VIS-032, VIS-034, VIS-045 (APP-044 decision then Kris's approval of each); VIS-038 (consolidation waits for APP-044; tool-storage phase waits only on the storage-declaration owner decision); VIS-042 (KI-HARNESS-GOV-224 viewer receipt contract).

Change nothing else. Run the roadmap audit (FAIL=0), commit by explicit path in one commit, do not push. Never run `ki repo conform` without `--dry-run`. Report what changed per record; raise a query only if an answer cannot be applied as written.
