# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-29 (EEST)
**Stable historical manual:** `docs/RECOVERY_MANUAL.md`
**Current detailed checkpoint:** `recovery/2026-08-29_exp073r1_v06_attempt1_pep668_incomplete_checkpoint.md`
**Active execution:** none; v0.7 replacement authority is being frozen before execution

DSIR remains independent of RTK.  Preserve all negative results,
preregistration chronology, missing-domain masks and the distinction between
infrastructure outcomes, reproduction results and scientific classifications.

## Current frontier

The G7 chain is blocked immediately before real Exp073P physical-support
evaluation:

`validated physical providers -> R1 exact weak-lensing-mask reproduction -> Exp073P aggregate prerequisite join -> Exp073P physical support -> covariance/whitening -> nuisance SVD/rank -> quotient/relation/null -> fresh G8`.

Current state:

- C3 physical provider: certified;
- C5 physical provider: certified with raw-k provenance corrected;
- BOSS finite mm component: frozen `54/240`, `27/120` per cap, `9/40` in each P0/P2/P4 block;
- DES public-input, large-object, P2 and S0 parents: immutable and validator-compatible;
- Exp073R0 raw-row/HEALPix equivalence: PASS;
- canonical Exp073R1 v0.6 run `33212521957`, attempt 1:
  **INCOMPLETE** at the PEP 668 runtime-install boundary, no result artifact;
- Exp073P aggregate evaluator: implemented and synthetic CI PASS;
- actual aggregate-join Actions route: preregistered, implemented and synthetic CI PASS, but real join BLOCKED on R1;
- Exp073P physical support: BLOCKED;
- covariance/whitening and every later stage: BLOCKED;
- G7: OPEN;
- G8: OPEN;
- G9: OPEN.

## Canonical R1 authority

The previously sole v0.6 authority is terminal and incomplete:

- run `33212521957`;
- job `98988824629`, `metacal-map-longrun`;
- head `79abf2a9694e57e7a2ba1fbb563a0f6413e891f9`;
- workflow `.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`;
- preregistration commit `7e801ce0352faf3a5b8ac232a0cd6e965d22762a`;
- frozen evaluator blob `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`.

Job `98988824629` passed checkout, the unchanged-evaluator firewall and both
immutable parent metadata bindings, then failed on
`python3 -m pip install --user numpy healpy` with
`externally-managed-environment`.  No parent artifact was downloaded, the
84 GB GET never started, zero metacal rows were read and no result artifact
exists.  Classify only `INCOMPLETE_EXP073R1`; aggregate evaluator v0.1 must
remain fail-closed and cannot be repointed.

The old v0.4 run `33160570463` and noncanonical v0.6 attempts are cancelled and
must not supply artifacts.  Actions `success` alone is insufficient: require
internal `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` plus every frozen
hash, row-count, mapper, bin, repeatability, parent and no-leakage control.

## Exp073P aggregate-join readiness

- evaluator preregistration: `c947a30cdcc1457c72e2501c6030f003ca9f037d`;
- implementation: `6d32ce32d16c33d3731031d543776e2045eb8115`;
- synthetic CI run: `33217294341`, success;
- artifact: `9703832682`, digest
  `sha256:6d4779be4a5e9dce1a582ed1e742b3c9f5766c551d7ee487c325f842cc1eddfe`;
- synthetic status:
  `PASS_EXP073P_AGGREGATE_JOIN_SYNTHETIC_SELFTEST_V0_1`;
- real-parent compatibility audit: PASS;
- actual execution-route preregistration: `df9a9b06b01d1c81bbc64e58495772676872c6f1`;
- actual route implementation: `0f9173eaf67925eeabceee9c27b6120f301aeec9`;
- route self-test run `33220212976`, job `99012479309`: success;
- route self-test artifact `9704867271`, digest
  `sha256:25f242b3385842a8506b6d80985c033559297ee15820b8d0df1ce7b84c46fa64`;
- route synthetic status:
  `PASS_EXP073P_ACTIONS_METADATA_ROUTE_SYNTHETIC_SELFTEST_V0_1`;
- real production workflow is manual-dispatch only and has not run;
- real prerequisite PASS: not evaluated;
- `support_executor_authorized=false` until the real R1-bound join passes.

## Frozen scientific boundaries

Never modify post hoc:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- classifying `nside=4096`;
- support uses the positive absolute final-response envelope;
- production Wm remains signed;
- all radial tails outside the rectangle remain invalid;
- no crop-before-normalization, effective ell, fiducial-P/model weighting or post-hoc cuts;
- no covariance, nuisance SVD/rank, quotient/relation/null, held-out or G8 leakage into support selection.

## Exact next actions

1. Hold `DSIR-HOME-PC` with the read-only reservation workflow while a v0.7
   replacement route is prospectively frozen.
2. Permit only the PEP 668-scoped installation override; preserve the
   unchanged evaluator and every frozen parent/science boundary.
3. Queue v0.7, record its exact run/job/head authority before releasing the
   runner, and add a superseding aggregate-join preregistration.
4. If v0.7 is interrupted, classify only `INCOMPLETE_EXP073R1`; preserve no
   partial mask as authority.
5. After genuine R1 PASS, freeze the returned artifact ID/digest as inputs to
   the already-implemented manual actual aggregate-join workflow and execute it.
6. Require the superseding real aggregate prerequisite PASS before the physical-support
   executor may start.
7. Require
   `PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P` before opening
   covariance/whitening.
8. Preserve downstream order: nuisance SVD/rank -> quotient/relation/null ->
   fresh G8 withheld family.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_LATEST.md`
3. `recovery/2026-08-29_exp073r1_v06_attempt1_pep668_incomplete_checkpoint.md`
4. `experiments/073r1_v0_6_selfhosted_longrun_stageb_prereg.md`
5. `experiments/073p_aggregate_prerequisite_join_evaluator_prereg_v0_1.md`
6. `experiments/073p_actual_aggregate_join_execution_route_prereg_v0_1.md`
7. `ci/exp073p_actions_metadata_bundle_v0_1.py`
8. `.github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-1.yml`
9. `data/derived/g7/exp073p_actual_join_route_readiness_audit_v0_1.json`
10. `data/derived/g7/exp073p_aggregate_join_parent_compatibility_audit_v0_1.json`
11. `recovery/2026-08-28_exp073r1_to_exp073p_execution_integrity_matrix.md`
12. `experiments/073p_cosmotheka_desy1_boss_exact_common_physical_support_prereg_v0_1.md`
