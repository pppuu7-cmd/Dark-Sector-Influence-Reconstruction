# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

## Current owner/process
- **DSIR-HOME-PC: RESERVED BY ONE LIVE EXP073BU HARDWARE-MATCHED 8-CORE SCIENCE PROCESS.**
- Workflow: `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-8core-v0-3.yml`.
- Run/job: `33901049626 / 101114995516`.
- Frozen activation source head: `d06829584f2cb91a05810ee92f2457982a80a048`.
- Science workflow blob: `c65464d661ac0361cac6f55153bbd7c4bfb05f76`.
- Hardware authority: the prior blocked 10-core attempt reported exactly `home_affinity_cpus=8`; this live process requires affinity >=8 and `DSIR_OMP_TEAM=8` before DES numerics.
- 8-core hosted exact-equivalence authority: `PASS_EXP073BU_8CORE_EXACT_EQUIVALENCE_V0_3`, run/job `33900913648 / 101114517184`, recovery `recovery/2026-09-04_exp073bu_8core_v0_3_exact_equivalence_pass.md`.
- Execution contract: `OMP_NUM_THREADS=8`; OpenBLAS/MKL/NumExpr/BLIS/Veclib nested threads pinned to 1; parametric full-window source compiled with `-DDSIR_WORKERS=8`.
- Physical checkpoint root: fresh run-specific `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-3-33901049626`; state from cancelled/blocked attempts is excluded.
- A namespace semantics remain `checkpoints/exp073bu-wm-s3-a-v0-1`.
- B namespace semantics remain `checkpoints/exp073bu-wm-s3-b-v0-1`.
- Execution order: fresh A, release replica-local live state, fresh B, then exact comparator.
- Science equality: whole canonical `<f8 [39,12288]` SHA256 equality **and** `numpy.array_equal`; no tolerance rescue.
- Allowed terminal classes: `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, `BLOCKED`.
- Required PASS token: `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`.

## Historical self-hosted attempts
- Run `33885834557`, job `101065302520`: manually cancelled after discovery that the claimed outer-worker count did not create actual worker parallelism. No terminal science comparison; infrastructure-only history.
- Run `33900526972`, job `101113324481`: blocked at hardware gate because Linux affinity exposed 8 CPUs rather than 10. No DES-scale numerics; infrastructure-only history.
- Neither attempt creates Wm_S3 numerical authority and neither is a scientific repeatability failure.

## Independent support authority
Exp073DD v0.1 remains terminal support PASS `D1_RESUME_LINEAGE_PROVENANCE_PASS +0/+0` from run/job `33892969489 / 101088831684`, artifact `9944582651`, recovery `recovery/2026-09-04_exp073dd_d1_resume_lineage_provenance_pass.md`. It is provenance-only and does not substitute for Exp073BU science.

## Authority boundary
Exp073CX v0.4 hosted activation readiness remains PASS. Exp073BU Wm_S3 numerical authority is absent until live run `33901049626` reaches a valid terminal A/B comparator result. Historical FAIL/infra results remain immutable.

Frozen Article-3 boundaries remain unchanged. No effective ell/z/k, fiducial-P, tolerance, smoothing, averaging, rounding or preferred-replica rescue is permitted.
