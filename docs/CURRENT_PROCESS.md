# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

## Current owner/process
- **DSIR-HOME-PC: RESERVED BY EXP073BU v0.1 via activation shell v0.3.**
- Workflow: `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-v0-3.yml`.
- Run/job: `33885834557 / 101065302520`.
- Frozen activation source head: `a2f14dfd5a9e54a30fb467f6d0e717bd4f00bd35`.
- Science workflow blob: `b95346a1c8243074a1ca49878919847b675a9269`.
- Contract fingerprint: `a400a7cee61f59c89099ac8b2c5ec67286b8c38002d5855a5f3a150c59838147`.
- A namespace: `checkpoints/exp073bu-wm-s3-a-v0-1`.
- B namespace: `checkpoints/exp073bu-wm-s3-b-v0-1`.
- Execution order: fresh A, release replica-local live state, fresh B, then exact comparator.
- Science equality: whole canonical `<f8 [39,12288]` SHA256 equality **and** `numpy.array_equal`; no tolerance rescue.
- Allowed terminal classes: `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, `BLOCKED`.
- Required PASS token: `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

## Authority boundary
Exp073CX v0.4 hosted activation readiness is PASS. Exp073BU numerical authority is absent until this run reaches a valid terminal comparator result. Historical FAIL/infra results remain immutable.

Frozen Article-3 boundaries remain unchanged. No effective ell/z/k, fiducial-P, tolerance, smoothing, averaging, rounding or preferred-replica rescue is permitted.
