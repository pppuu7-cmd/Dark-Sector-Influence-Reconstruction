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
- Live state at latest reconciliation: job `101065302520` remains `IN_PROGRESS`, step `Fresh live exclusivity and Exp073BU A-then-B science`; no partial numerical output consumed.

## Independent support process consumed this iteration
Exp073DD v0.1 is terminal authoritative support PASS `D1_RESUME_LINEAGE_PROVENANCE_PASS +0/+0` from run/job `33892969489 / 101088831684`, activation/head `fbe6156d95cafdca3630c058808d74ac139cce46`, artifact `9944582651`, independently verified ZIP SHA256 `06c971ec7b97fae34b0fa1e113fb449d0bffc9b0e126f0045a9660eb1f6a1056`. Immutable note: `recovery/2026-09-04_exp073dd_d1_resume_lineage_provenance_pass.md` (record commit `b936dc9d93f70100a6ffa72d6d9b44cd80c51803`).

Exp073DD validates a prospective provenance-only resume repair: invocation-local reconstruction counts are separated from immutable cumulative `{lens:1,source:1}` lineage; missing/malformed/wrong cumulative lineage fails closed. It delegates frozen v0.1 science and exact comparator unchanged. It does **not** change the source of the active Exp073BU run and creates no Wm_S3 scientific authority. A future interrupted-run resume may use v0.2 only after explicit prospective binding; silent source substitution is forbidden.

## Authority boundary
Exp073CX v0.4 hosted activation readiness is PASS. Exp073BU numerical authority is absent until run `33885834557` reaches a valid terminal comparator result. Historical FAIL/infra results remain immutable.

Frozen Article-3 boundaries remain unchanged. No effective ell/z/k, fiducial-P, tolerance, smoothing, averaging, rounding or preferred-replica rescue is permitted.
