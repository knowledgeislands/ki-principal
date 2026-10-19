# obs-pies-tables - Records to replace the email triage pies

This run is for KI > Model > Observatory (`ki.observatory`). On 2026-10-19 Kris decided (PIES-TABLE-BARS in ki-principal `+/_WORK/ki.observatory/decisions.md`): "drop that. Put a table, and then put a sort of bar in a column as well, which kind of shows the relative sizing of it to the others."

The pies are in personal-principal (`Pillars/Productivity/Knowledge Management/KB Specifics/Email/Email Triage Status.md` and the template that writes it) and in hnr-principal (`Admin/Knowledge Management/KB Specifics/Email/Email Status.md` and its template). Find each template.

In each repository, add one roadmap record under that repository's own work adapter and conventions (read its `AGENTS.md` and `.ki.toml`). The record should cover:

- dropping the Mermaid pie from the note and its template;
- sorting the table by count, descending;
- adding a bar column, a plain-text bar such as Unicode block characters scaled to the largest row, so it renders anywhere;
- adding a one-line total.

Include a short example of the target table in each record. Change neither the notes nor the templates: each repository's owner delivers the record. Commit by explicit path under `ki-git`, and do not push.

Report in owner-report shape, kept short: Done gives each record with its link. Queries: `No outstanding queries` unless something blocks.
