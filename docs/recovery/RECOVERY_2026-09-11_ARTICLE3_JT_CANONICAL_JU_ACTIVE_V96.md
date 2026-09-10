# DSIR authoritative recovery V96 — Article III JT canonical lattices / JU active

Date: 2026-09-11. Scope: **DSIR only**. Repository and validated artifacts are source of truth.

## Stable scientific state

Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`. Exp073JI support remains feasible. Exp073JJ/JK remain support-only NOT_CONVERGED at `0.037280144773915974` and `0.016330535730270664`. Frozen Exp073JL science remains unchanged: canonical 2049->4097 common-grid comparison, native kpd20, `h=1e-4`, centered-cubic interpolation in ln(k), same 107-row observational traversal/accounting, `REL_TOL=1e-3`, same support/domain/invalid-row gates and all anti-rescue rules. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

**ARTICLE3_REPOSITORY_READINESS = 68%.** This is readiness of the DSIR repository as the scientific basis for preparing Article III, not manuscript-writing completion. Process/reproducibility work alone does not increase it. Funnel-freeze readiness remains 67%.

## JR/JQ preserved process authority

- Exp073JQ independently verified same-run history/fresh repeat exact PASS on fine 4097 geometry. Canonical fine node payload SHA256 `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`.
- Exp073JR v0.1 coarse-2049 direct four-live-vs-sequential exact PASS remains durable in `docs/dsir4/authority/EXP073JR_COARSE_2049_SEQUENTIAL_EXACT_EQUIVALENCE_RECEIPT_V0_1.json`. Canonical coarse node payload SHA256 `6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46`.
- JR v0.2 fine four-live attempts remain terminal `INVALID_INFRA_PLUS_0_PLUS_0` with zero fine numerical receipts. Do not reinterpret them as NOT_EXACT and do not blindly rerun the same four-live 4097 hosted architecture.

## Exp073JS terminal and conservative geometry audit

Corrected authoritative JS run `34535674581`, head `7676f64e811520e96a09b76c35c2bf3d49b0cf01`, completed with four local one-live lifecycle exact PASS receipts and aggregate PASS. Independent artifact audit found cross-host last-bit `np.geomspace` variation:

- `reference`, `alpha_minus`, `beta_plus` ran on canonical fine node SHA `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`;
- `beta_minus` ran on host variant SHA `80d5a13c9fa32e77a248b5a835ecf210b9e6afdda27decaffba27b829c261a92`.

All four local before/after lifecycle comparisons had max absolute and relative difference exactly `0.0` and unsupported `0`. Therefore JS is a valid local-grid lifecycle-isolation result but canonical-fine coverage is conservatively only 3/4, not 4/4.

Durable coverage audit: `docs/dsir4/authority/EXP073JS_ARTICLE3_LIFECYCLE_GEOMETRY_COVERAGE_AUDIT_V0_1.json`, commit `36aa369f57ca043e6242eb8c9ada993f6c1ad70c`, classification `LOCAL_LIFECYCLE_PASS_CANONICAL_FINE_COVERAGE_3_OF_4_PLUS_0_PLUS_0`. Missing canonical role: only `beta_minus`.

## Exp073JT canonical shared-lattice materialization PASS

Exp073JT was prospectively frozen before hosted replicas. It did not choose a convenient post-hoc grid: required SHAs were fixed by the pre-existing JR coarse and JQ fine authorities.

Run `34537725440`, aggregate job `103073186968`, aggregate artifact `10176063866`.

Independent aggregate verification:
- artifact ZIP SHA256 `4e17994a81ce8e2f7b17be59e5add65ab766f1cfc46370d13b19054bda3efba3`;
- result JSON SHA256 `6a9805233e580f571f0572e29641b318f957f09b9642d7180d5c21a0898b77b0`;
- classification `CANONICAL_SHARED_LATTICES_MATERIALIZED_PASS_PLUS_0_PLUS_0`;
- all 8 fixed receipts valid;
- coarse authority SHA reproduced by 2/4 fixed replicas (replicas 1,4), identical bytes; replicas 2,3 both produced host variant `133a353c269461a4d39050ccb0588963f0a76648946a18c49fb06b35f3375bba`;
- fine authority SHA reproduced by 4/4 replicas, identical bytes.

Canonical text streams:
- coarse 2049 u64hex SHA256 `72c732a02b9f6f4adeab70c7792f16e4490f038544c221aed9b72a14e5b1ec47`, decoded node SHA `6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46`;
- fine 4097 u64hex SHA256 `290075f777c88964aa6b670694063e9b4ad0d5d4dcb16ee12adad5103ca1b6c7`, decoded node SHA `f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb`.

Promotion workflow first failed only because NumPy was absent in its verification step after exact artifact SHA verification and before any commit; pure infrastructure +0/+0. Minimal repair added `numpy==1.26.4`. Corrected promotion run `34538060928`, job `103074168727`, completed successfully and committed exact canonical payloads at bot commit `6f59a22b6f391e2dd16ca8d0dae81c8bd3ad8c07`.

Durable files now in main:
- `docs/dsir4/canonical/EXP073JL_CANONICAL_COARSE_2049_NODES_U64HEX_V0_1.txt`;
- `docs/dsir4/canonical/EXP073JL_CANONICAL_FINE_4097_NODES_U64HEX_V0_1.txt`;
- `docs/dsir4/authority/EXP073JT_ARTICLE3_CANONICAL_SHARED_LATTICES_V0_1.json`, blob `2ed0f4d0a99e31e4e8ddf5644a10fc0a688a4469`.

Future recovered-JL execution MUST consume these committed exact payloads rather than regenerate geometry with host-dependent `np.geomspace`.

## Exp073JU active — only missing canonical lifecycle role

Purpose: close exactly the one JS canonical-fine coverage gap (`beta_minus`) using the committed exact fine payload. It does not rerun the other three roles and is process/support only `+0/+0`.

Prospective prereg:
`docs/dsir4/prereg/EXP073JU_ARTICLE3_CANONICAL_FINE_BETA_MINUS_LIFECYCLE_ISOLATION_V0_1.md`, commit `19c38f5cfb9d72f214f4e94774c6dde1a6006375`, blob `63ee0146247c3bc35ea3c1d83be50318537244b4`.

Helper:
`ci/exp073ju_article3_canonical_fine_beta_minus_lifecycle_isolation_v0_1.py`, commit `2eea658656f1a5bf9917f9401f21ba21132c3136`, blob `ebeff6a760ce6f5ecf952d1258f7065439915cba`.

Initial workflow run `34538264386`, job `103074794225`, failed only at a pre-install identity helper that imported NumPy; install/build/numerical steps were skipped. This is `INVALID_INFRA_PLUS_0_PLUS_0` with no numerical content.

Pre-result workflow hardening replaced that guard with stdlib `struct.pack`, commit `d31bf42744ef501e8520fd4af8e9b34aed123cb3`.

Corrected authoritative JU run: `34538302756`; job `103074914132`. At this V96 checkpoint it has passed checkout, frozen identity guard, stack installation and exact pinned CLASS-IV build, and is in `Execute canonical beta-minus lifecycle control`. Do not duplicate it.

Frozen JU PASS requires the committed fine text/node SHAs above, 4097 exact nodes, zero unsupported targets across all five fresh one-live instances, max lookup mismatch <=1e-12, and for beta-minus A/B before-vs-after exact array equality, exact `<f8` byte SHA equality, identical finite/positive masks, with max absolute and relative diagnostics exactly `0.0`. No tolerance/ULP/rounding rescue.

## Exact next action

1. Terminal-consume corrected JU run `34538302756` and independently verify artifact/digests against the prereg.
2. If JU valid PASS, create durable JU authority and prospectively freeze a separate sequential-execution authorization audit combining JR coarse direct exact PASS + JQ fine history/repeat exact PASS + CLASS-IV C2 instance-locality source audit + JS canonical 3/4 lifecycle receipts + JT committed exact canonical grids + JU canonical beta-minus lifecycle PASS + estimator-lifetime invariance.
3. Only if that separate audit authorizes the execution architecture may a recovered Exp073JL contract be preregistered. Recovered JL must preserve original JL science exactly and consume canonical committed coarse/fine grids; no geometry regeneration and no scientific operands crossing runner/process boundaries.
4. If JU gives a valid bitwise inequality, sequential recovered-JL route is blocked. If infrastructure failure, repair only the first causal infrastructure defect and preserve the scientific criteria.
5. Do not authorize covariance restriction or Wm_S3 until their own downstream prerequisites are met.
