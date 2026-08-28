# DSIR G7 checkpoint — Exp073P frozen-contract hardening

Date: 2026-08-28

## State observed

- `main` before this iteration: `9f3269d0686ce9ca24da277225ca7269e24f9a9d`.
- Exp073R1 run `33108733415` remained `in_progress`; therefore no duplicate R1 run and no Exp073P support classification was launched.
- Frozen Exp073P preregistration remains `experiments/073p_cosmotheka_desy1_boss_exact_common_physical_support_prereg_v0_1.md`.

## Independent work completed while R1 is running

Added `ci/exp073p_frozen_contract_selftest_v0_1.py` and `.github/workflows/exp073p-frozen-contract-selftest-v0-1.yml`.

The self-test executable binds only already-preregistered semantics and is explicitly NON-CLASSIFYING.  It checks:

- support rectangle boundaries `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`;
- classifying `nside=4096`;
- inclusive support threshold `f_invalid <= 0.05`, including an exact-boundary test that `0.05` passes and the next floating-point number above it fails;
- positive-envelope denominator semantics: zero, negative or non-finite normalization maps to reproduction/numerical failure, not scientific support FAIL;
- minimum retained full-coordinate dimension constant `15`;
- literal preservation of PASS / scientific dimension FAIL / reproduction FAIL / infrastructure INCOMPLETE result classes;
- P8 downstream blindness by rejecting covariance, whitening, nuisance-SVD/rank, quotient/relation/null and G8/withheld-family keys in support-input records;
- textual binding of the workflow to the frozen preregistration statements.

## Important non-claim

This does **not** close the previously recorded end-to-end Exp073P executor gap.  It closes only the threshold/unit/taxonomy drift surface.  The physical Wm/WW support-row construction and the preregistered full-coordinate combination rule still require an R1-bound implementation before Exp073P may be scientifically classified.

No attempt was made to infer or invent the full-coordinate aggregation rule from the already-retained `54/240` BOSS record; doing so would risk post-preregistration semantic drift.  The future executor must derive that rule from the frozen observational-coordinate construction and existing lineage, not from the fact that 54 exceeds the minimum dimension 15.

## Gate ordering preserved

`validated physical forward/power-input bridges -> R1 reproduction prerequisite -> Exp073P physical support-validity classification -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.

Until Exp073P emits `PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P`, covariance and all later stages remain blocked.
