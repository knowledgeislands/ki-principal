# obs-link-pins - Pin links to pruned records

Work in apps-observatory.local for KI > Model > Observatory (work package ki-principal `+/_WORK/ki.observatory/`; do not edit it), under `ki-work-roadmap`. This is a mechanical record correction, the same as the KI-OBSERVA-APP-042 pins in fc1864d.

1. Commit fa16595 pruned KI-OBSERVA-APP-042, BCN-008, BRG-002, INT-004, VIS-023 and VIS-024. Pin every relative link to them that no longer resolves to `https://github.com/knowledgeislands/apps-observatory.local/blob/22ea8dc/docs/roadmap/<file>` (check the file exists at 22ea8dc; use the last commit where it existed if not): in KI-OBSERVA-BRG-004, VIS-029, VIS-033 and VIS-041, and the two in the done KI-OBSERVA-VIS-031. Also check every record created or shaped since, including any obs-triage commits.
2. In KI-OBSERVA-APP-044, repoint the line saying Workers is a later phase in KI-OBSERVA-VIS-031 to KI-OBSERVA-VIS-045.

Link-only changes: no scope, status, horizon or wording beyond the link. One commit by explicit path; run `ki repo audit`; do not push. Report in owner-report shape: Done with each link fixed, the commit and the audit result; In Progress; Queries, or `No outstanding queries`.
