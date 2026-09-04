# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

## Current owner/process
- **DSIR-HOME-PC: RESERVED FOR ONE EXP073BU HARDWARE-MATCHED 8-CORE SCIENCE PROCESS.**
- Authorized workflow: `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-8core-v0-3.yml`.
- Exact workflow blob: `c65464d661ac0361cac6f55153bbd7c4bfb05f76`.
- Hardware authority: live self-hosted run `33900526972 / 101113324481` reported exactly `home_affinity_cpus=8`; that 10-core attempt stopped before DES numerics.
- 8-core hosted exact-equivalence authority: `PASS_EXP073BU_8CORE_EXACT_EQUIVALENCE_V0_3`, run/job `33900913648 / 101114517184`, recovery `recovery/2026-09-04_exp073bu_8core_v0_3_exact_equivalence_pass.md`.
- Execution contract: `OMP_NUM_THREADS=8`; OpenBLAS/MKL/NumExpr/BLIS/Veclib nested threads pinned to 1; full-window OpenMP runtime must prove `DSIR_OMP_TEAM=8` before DES numerics.
- A namespace semantics remain `checkpoints/exp073bu-wm-s3-a-v0-1`.
- B namespace semantics remain `checkpoints/exp073bu-wm-s3-b-v0-1`.
- Physical checkpoint storage for the next activation must be a fresh run-specific root; no cancelled/blocked attempt state may be restored.
- Execution order: fresh A, release replica-local live state, fresh B, then exact comparator.
- Science equality: whole canonical `<f8 [39,12288]` SHA256 equality **and** `numpy.array_equal`; no tolerance rescue.
- Allowed terminal classes: `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, `BLOCKED`.
- Required 8-core PASS token: `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`.

## Historical self-hosted attempts
- Run `33885834557`, job `101065302520`: manually cancelled after discovery that the claimed outer-worker count did not create actual worker parallelism. No terminal science comparison; infrastructure-only history.
- Run `33900526972`, job `101113324481`: blocked at hardware gate because Linux affinity exposed 8 CPUs rather than 10. No DES-scale numerics; infrastructure-only history.
- Neither attempt creates Wm_S3 numerical authority and neither is a scientific repeatability failure.

## Independent support authority
Exp073DD v0.1 remains terminal support PASS `D1_RESUME_LINEAGE_PROVENANCE_PASS +0/+0` from run/job `33892969489 / 101088831684`, artifact `9944582651`, recovery `recovery/2026-09-04_exp073dd_d1_resume_lineage_provenance_pass.md`. It is provenance-only and does not substitute for Exp073BU science.

## Authority boundary
Exp073CX v0.4 hosted activation readiness remains PASS. Exp073BU Wm_S3 numerical authority is absent until the hardware-matched 8-core run reaches a valid terminal A/B comparator result. Historical FAIL/infra results remain immutable.

Frozen Article-3 boundaries remain unchanged. No effective ell/z/k, fiducial-P, tolerance, smoothing, averaging, rounding or preferred-replica rescue is permitted.
