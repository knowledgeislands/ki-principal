# ki.portable-specifications queries

## Open

### LINK-FIELDS - drop the acquire and knowledge link fields entirely

Raised by revise-3, 20 October. Draft 0.4 removed `metadata.acquired-with` on knowledge ("refresh by re-running this acquire package and curating the result") and `metadata.produces` on acquire ("the knowledge package this method feeds"); provenance now lives only in the knowledge package's required `## Sources` section, which may cite an acquire package or its output by external reference. SPEC-LOCATION's rule that added fields sit in `metadata` as strings is unchanged.

**Query:** Should the drafts keep both link fields removed, rather than keep a one-way citation field?

**Options:** a) (recommended, confidence medium - follows KNOWLEDGE-AS-SKILL's "drop the transition" most closely, but removes fields drafts 0.2 and 0.3 carried) Keep both removed, with provenance carried only by Sources. b) Restore a one-way `metadata` key on knowledge, an optional machine-readable list of the external references cited, with no field on acquire.

## Parked

None
