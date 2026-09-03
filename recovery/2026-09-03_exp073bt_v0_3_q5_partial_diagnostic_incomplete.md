# Exp073BT v0.3 — terminal hosted source-linkage diagnostic

Date: 2026-09-03
Scope: DSIR only. RTK/RQIR excluded.

## Provenance
- run: `33794449690`
- head: `7e1d98c8fcddf6c91a54c54bee7db26930c87309`
- hosted static-audit job: `100778636054` — SUCCESS
- hosted diagnostic job: `100778710837` — SUCCESS
- preregistration commit: `ee82324ebc0e80ec2d3282283d9831840b890bc4`
- workflow implementation commit: `ef4a2655b7906666bed01be6cf95fa6d8b38db98`
- inherited diagnostic harness commit: `8a70892c9533206e4011eee041914ca89bae2290`
- artifact: `9908640902`
- artifact digest: `sha256:e3fc8d1f390101900d35f90e03f0317f62675e23a6971fb01aff4bc233f86dd9`

## Frozen-contract classification
The workflow completed successfully, but workflow SUCCESS is not a scientific/source-linkage PASS. The raw diagnostic receipt is:

- `pymaster_version = 2.7`
- `extension_import.ok = false`
- `extension_import.error = ModuleNotFoundError("No module named 'pymaster._nmtlib'")`
- installed-tree text search for `drc3jj` completed with return code 0 but found no matching installed source text
- frozen status: `BT_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`
- classification: `NONCLASSIFYING_INFRASTRUCTURE_SOURCE_LINKAGE_DIAGNOSTIC`
- authority: false
- scientific readiness increment: 0
- draft/data readiness increment: 0

Therefore Exp073BT v0.3 is **Q5 incomplete, +0/+0**. It does not resolve Q1/Q2/Q3/Q4 and creates no Wm_S2/Wm_S3/WW/Layer-A/B/new-physics authority. Exp073AQ remains historical FAIL and Exp073BJ Track-A exact PASS remains preserved.

## Additional live reconciliation
A subsequent push-triggered run `33794533063` of the malformed historical v0.1 workflow completed as failure with **zero jobs**. This is the already-known historical control-plane defect being retriggered by a later documentation commit; it is infrastructure `+0/+0`, not a new numerical result and not a reason to rerun v0.1.

## Frontier
Exp073CR v0.3 remains the authoritative resource PASS `+0/+0`; Wm_S3 scientific angular authority remains absent. The next permitted scientific process is still the prospectively frozen fresh-independent-PCL Wm_S3 A/B successor, with hosted static audit and explicit activation before exactly one checkpointed home workload.
