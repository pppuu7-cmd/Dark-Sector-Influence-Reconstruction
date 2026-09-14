# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Active authoritative frontier — V0.15 cross-host environment fingerprint reproducibility audit

Parent terminal authority: `docs/dsir4/authority/LAYERB_BETA_SAME_RUN_SOLVER_DETERMINISM_V0_14.json`, creation commit `1a752a42223043b6efed79dd1294406532d2b48e`.

Parent classification: `SAME_RUN_REPEATED_SOLVER_DETERMINISM_SUPPORTED`, effect `+0/+0`; authorized successor exactly `PROSPECTIVELY_FROZEN_CROSS_HOST_ENVIRONMENT_FINGERPRINT_REPRODUCIBILITY_AUDIT`.

Prospective V0.15 contract: `docs/dsir4/contracts/LAYERB_BETA_CROSS_HOST_FINGERPRINT_V0_15.json`, commit `8bdfee04fbdbeece06824d215088797866ed579a`.

Executor: `ci/layerb_beta_cross_host_fingerprint_v0_15.py`, commit `ad811e5da24bb20f654b0bc4d0646640e561150f`, blob `1a51344f0c571704b2b1d01bf4ecb04fe4508083`.

Workflow: `.github/workflows/layerb-beta-cross-host-fingerprint-v0-15.yml`, commit `c3003bf0c8862fee75167bd3afdc415db80e9a99`.

Launch: `docs/dsir4/launch/LAYERB_BETA_CROSS_HOST_FINGERPRINT_V0_15_LAUNCH.json`, head/commit `64968099805f6701424881562b1b5263a56d0e0b`.

Authoritative active run: `34792546153`. Exactly one run was created for the launch head. Frozen invariant-audit is terminal `success`. The production matrix contains exactly 16 independent hosted jobs: `GRID768/GRID1024 × R1..R8`, `PURE_PAIR` only, with workflow `max-parallel: 16`; hosted-runner capacity may queue some lanes. Decision is allowed only after invariant plus all sixteen lanes are terminal.

Do not inspect or use partial substantive lane values before the single frozen decision barrier.

## Frozen V0.15 object and fingerprint

Target hypothesis: the V0.13 cross-job numerical variation is associated with the prospectively fixed stable hardware/software environment fingerprint, or else persists within identical recorded fingerprints and therefore requires deeper runtime-state localization.

Object: across-independent-job pairwise relative spread of signed centered beta responses on the exact V0.13/V0.14 diagnostic cells, grouped only by the frozen normalized combined fingerprint.

Frozen numerical identities: production `h=1e-4`; scientific response threshold `<1e-3`; technical replay threshold `<1e-5`; exact binding `<=1e-12`; production sampling `0.00035`; TOL300 `1e-12`; CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`; unchanged baseline/precision/JJ/V12 extraction identities.

Frozen scientific fingerprint hardware fields: runner architecture; platform machine; CPU vendor/family/model/stepping/microcode/model-name; hash of sorted CPU flags. Frozen software fields: runner/image OS and image version; platform/kernel fields; normalized `/etc/os-release`; libc; gcc/gfortran/ldd; Python/NumPy/SciPy; NumPy build-config hash.

Ephemeral runner name, GitHub run/job IDs, run attempt, timestamps and dynamic CPU frequency are provenance only and cannot define scientific fingerprint groups or classifications.

## Frozen classifier

- invariant/anchor/identity/fingerprint failure -> `CROSS_HOST_FINGERPRINT_AUDIT_INCONCLUSIVE`, no scientific promotion;
- all failure cells cross-job stable below `1e-5` -> `V013_CROSS_JOB_NONDETERMINISM_NOT_REPRODUCED_IN_V015`;
- cross-job variation reproduced and any repeated identical combined-fingerprint group varies at/above `1e-5` -> `RECORDED_HOST_FINGERPRINT_INSUFFICIENT_CROSS_JOB_VARIATION_PERSISTS`;
- cross-job variation reproduced, repeated fingerprint groups internally stable, and at least two distinct repeated fingerprint groups on the same grid differ in failure-cell mean at/above `1e-5` -> `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED`;
- otherwise reproduced but insufficient/mixed grouping -> `HOST_ENVIRONMENT_FINGERPRINT_AUDIT_UNDERPOWERED_OR_MIXED`.

Interpretation ceiling: numerical reproducibility localization only. No V0.15 outcome itself validates full Layer-B, covariance, whitening, nuisance treatment, relation-null, `Wm_S3`, global traversal, dark-sector inference or a physical signal.

## Parent V0.14 fact

Run `34787822995` was terminal `success`; decision artifact `10327458719`, SHA256 `12e9ea528dfbb12d2041ae927be6f551e84abff8478c74e19508e7b5e3345576`. All five frozen diagnostic cells were exactly stable across three sequential same-process repeats in all four grid/profile lanes, so V0.13 variation was localized away from same-run repeated-solver behavior and toward cross-job/runner/environment variation.

## Frozen boundaries / anti-duplication

No full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 or science gate is authorized. Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and scientific frontier `67%`; reproducibility diagnosis alone changes neither.

Do not launch another V0.15 while run `34792546153` is non-terminal. Consume only its terminal decision after all 16 lanes plus invariant are terminal; then verify artifacts/hashes, write a durable V0.15 authority, and follow only the encoded `next_stage`.
