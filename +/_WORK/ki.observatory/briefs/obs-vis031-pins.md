# obs-vis031-pins - pin links to the pruned KI-OBSERVA-VIS-031

Repository: apps-observatory.local. Mechanical link fix, same kind as b6bd1f9.

KI-OBSERVA-VIS-031 was pruned in af4d39d; its last revision is 24c4bd8bfb1956c5ee9e0e2beef846bd06e298a5. Repoint every remaining link in `docs/roadmap/` to the pruned VIS-031 file (including KI-OBSERVA-VIS-044 and KI-OBSERVA-VIS-030) to `https://github.com/knowledgeislands/apps-observatory.local/blob/24c4bd8bfb1956c5ee9e0e2beef846bd06e298a5/docs/roadmap/<VIS-031 file name>`, keeping the link text and adding " (pruned)" where the text is the identifier. Change link targets and `updated_at` only; reword nothing. Run the roadmap audit (FAIL=0 expected), commit by explicit path in one commit `fix(roadmap): pin links to pruned KI-OBSERVA-VIS-031`, do not push. Never run `ki repo conform` without `--dry-run`. Report the commit and files; raise no queries unless a link cannot be pinned.
