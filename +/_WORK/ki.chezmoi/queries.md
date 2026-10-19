# ki.chezmoi queries

## Open

### READY-PREFLIGHT - One-run exception for 20 existing roadmap warnings

Needs: decision

**Context:** ready-rest stopped before writing anything: `ki-plan` and `ki-next` stop on any audit warning, and chezmoi's roadmap carries 20 existing migration warnings (16 missing sizes, four retired `initiative` fields) in other records ([ready-rest](/Users/krisbrown/.local/state/ki/agents/chezmoi/ready-rest.report.md)).

**Query:** May the retry ignore only those 20 existing warnings for the approved split and Ready check, stopping on any new warning or failure?

**Options:** a) (recommended, confidence high - confines the exception to the approved split and keeps every other readiness check) One-run exception. b) First clear the 20 warnings in a separate reviewed migration pass, then retry.

## Parked

None.
