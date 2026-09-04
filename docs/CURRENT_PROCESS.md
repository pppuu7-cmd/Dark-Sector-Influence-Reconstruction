# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

## Current owner/process
- **DSIR-HOME-PC: RESERVED BY ONE LIVE EXP073BU HARDWARE-MATCHED 8-CORE v0.4 SCIENCE PROCESS.**
- Workflow: `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-8core-v0-4.yml`.
- Run/job: `33901458494 / 101116305364`.
- Run start: `2026-09-04T17:36:14Z`.
- Frozen activation/source head: `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`.
- Science workflow blob: `f8c70a4206321b0dc10b57f63a2a06163da2249a`.
- Checkpoint root: `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`.
- A/B checkpoint namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`.
- Expected gate/token: exact A/B comparator; required science PASS token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`.
- Current state at latest live reconciliation: `IN_PROGRESS`; step `Fresh live exclusivity and Exp073BU 8-core A-then-B science`.
- Last durable checkpoint claimed by repository authority before terminal consumption: **NONE CLAIMED/INSPECTED WHILE ACTIVE**. Do not inspect partial numerical/checkpoint payloads to tune or reinterpret the frozen gate. Terminal consumption must establish the exact durable checkpoint identity from immutable evidence.
- Hardware authority: live Linux affinity on `DSIR-HOME-PC` exposes exactly 8 CPUs.
- Exact-equivalence authority: `PASS_EXP073BU_8CORE_EXACT_EQUIVALENCE_V0_3`, run/job `33900913648 / 101114517184`.
- v0.4 activation authority: `PASS_EXP073BU_8CORE_ACTIVATION_AUDIT_V0_4`, run/job `33901386471 / 101116035558`, artifact `9947758011`, digest `sha256:1517ccb3cfb2a6f8ee036de1062c7e181494a4b519441089530b418d967d1f7c`.
- Execution contract: `OMP_NUM_THREADS=8`; OpenBLAS/MKL/NumExpr/BLIS/Veclib nested threads pinned to 1; full-window source compiled with `-DDSIR_WORKERS=8`; runtime must prove `DSIR_OMP_TEAM=8` before DES numerics.
- Execution order: fresh A, release replica-local live state, fresh B, then exact comparator.
- Science equality: whole canonical `<f8 [39,12288]` SHA256 equality and `numpy.array_equal`; no tolerance rescue.
- Allowed terminal classes: `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, `BLOCKED`.

## Exact next action by terminal class
- **SUCCESS / valid PASS token:** download and independently inspect the raw evidence artifact; verify artifact digest, frozen source/workflow/implementation lineage, contract fingerprint, A/B namespace and checkpoint identities, canonical dtype/shape, whole-payload SHA equality and `numpy.array_equal`. Only then admit Wm_S3 authority and dispatch the next prospectively permitted gate.
- **SCIENTIFIC_REPEATABILITY_FAIL:** preserve the exact negative result and raw comparator evidence; do not repair arithmetic or tolerances. Move only to the next scientifically preregistered branch allowed by the frozen governance.
- **INFRASTRUCTURE_INCOMPLETE / cancellation / runner loss / malformed or missing artifact:** diagnose the first causal failure from complete logs, preserve every verified durable complete-stage checkpoint, and use only a prospectively audited resume binding. Do not rerun verified expensive stages.
- **BLOCKED:** record the exact external prerequisite and keep the home runner unowned only after the tracked job is terminal.

## Live noncompetition state at latest reconciliation
- GitHub Actions `in_progress`: exactly `1`, this run `33901458494`.
- GitHub Actions `queued`: `0`.
- Do not dispatch any competing DSIR heavy/self-hosted process while this remains true.

## Historical self-hosted attempts
- `33885834557 / 101065302520`: manually cancelled after discovery that the claimed worker count did not create actual parallel workers. No terminal science comparison.
- `33900526972 / 101113324481`: blocked before science because only 8 CPUs were exposed, not 10.
- `33901049626 / 101114995516`: 8-core v0.3 passed affinity, environment, R1/lens staging and compilation, but runtime probe used system Python lacking NumPy; science step was skipped. Infrastructure-only failure.
- None of these attempts creates Wm_S3 authority or constitutes a scientific repeatability failure.

## Authority boundary
Exp073CX v0.4 hosted activation readiness remains PASS. Exp073BU Wm_S3 numerical authority is absent until live run `33901458494` reaches a valid terminal A/B comparator result and that raw result is independently consumed against the frozen contract. Historical FAIL/infra results remain immutable.

Frozen Article-3 boundaries remain unchanged. No effective ell/z/k, fiducial-P, tolerance, smoothing, averaging, rounding or preferred-replica rescue is permitted.
