# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

## Current owner/process
- **DSIR-HOME-PC: RESERVED BY ONE LIVE EXP073BU HARDWARE-MATCHED 8-CORE v0.4 SCIENCE PROCESS.**
- Workflow: `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-8core-v0-4.yml`.
- Run/job: `33901458494 / 101116305364`.
- Frozen activation source head: `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`.
- Science workflow blob: `f8c70a4206321b0dc10b57f63a2a06163da2249a`.
- Hardware authority: live Linux affinity on `DSIR-HOME-PC` exposes exactly 8 CPUs.
- Exact-equivalence authority: `PASS_EXP073BU_8CORE_EXACT_EQUIVALENCE_V0_3`, run/job `33900913648 / 101114517184`.
- v0.4 activation authority: `PASS_EXP073BU_8CORE_ACTIVATION_AUDIT_V0_4`, run/job `33901386471 / 101116035558`.
- Execution contract: `OMP_NUM_THREADS=8`; OpenBLAS/MKL/NumExpr/BLIS/Veclib nested threads pinned to 1; full-window source compiled with `-DDSIR_WORKERS=8`; runtime must prove `DSIR_OMP_TEAM=8` before DES numerics.
- Fresh checkpoint root: `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`.
- A/B namespace semantics remain frozen as `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`.
- Execution order: fresh A, release replica-local live state, fresh B, then exact comparator.
- Science equality: whole canonical `<f8 [39,12288]` SHA256 equality and `numpy.array_equal`; no tolerance rescue.
- Allowed terminal classes: `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, `BLOCKED`.
- Required science PASS token remains `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`; v0.4 changes activation infrastructure only.

## Historical self-hosted attempts
- `33885834557 / 101065302520`: manually cancelled after discovery that the claimed worker count did not create actual parallel workers. No terminal science comparison.
- `33900526972 / 101113324481`: blocked before science because only 8 CPUs were exposed, not 10.
- `33901049626 / 101114995516`: 8-core v0.3 passed affinity, environment, R1/lens staging and compilation, but runtime probe used system Python lacking NumPy; science step was skipped. Infrastructure-only failure.
- None of these attempts creates Wm_S3 authority or constitutes a scientific repeatability failure.

## Authority boundary
Exp073CX v0.4 hosted activation readiness remains PASS. Exp073BU Wm_S3 numerical authority is absent until live run `33901458494` reaches a valid terminal A/B comparator result. Historical FAIL/infra results remain immutable.

Frozen Article-3 boundaries remain unchanged. No effective ell/z/k, fiducial-P, tolerance, smoothing, averaging, rounding or preferred-replica rescue is permitted.
