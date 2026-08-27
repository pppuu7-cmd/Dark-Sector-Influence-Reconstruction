# DSIR recovery checkpoint — Exp073R1 gate-lineage audit

**Date:** 2026-08-28

## Purpose

Record an independent gate-lineage/reproducibility audit while Exp073R1 is still active. This checkpoint changes no frozen scientific acceptance criterion and authorizes no downstream computation.

## Current immutable lineage

- Exp073P exact common physical-support audit was prospectively frozen in commit `e65930ea4dae3b63f2758be6b454f2fa6b4f4e33` before any Exp073P support fraction was evaluated.
- Its unchanged classifying rectangle is `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1`.
- Its unchanged coordinate support threshold is `f_invalid <= 0.05` and minimum retained full-coordinate dimension is `15`.
- Classifying DES map resolution remains `nside=4096`.
- The older Exp072a angular-support result remains a genuine frozen-criterion scientific hard FAIL. It is not reclassified as infrastructure failure and is not reopened by Exp073P.
- The G7 boundary document did not itself carry the numeric 5% value, but the later prospective Exp073P preregistration does. Therefore the repository-level frozen threshold is unambiguously 5%; it must not be changed after R1 output.

## Validated Exp073P prerequisites already present

The existing recovery chain records:

- Exp073P2 remaining DES Y1 release checksum identity binding: `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`.
- Exp073Q2 large-FITS schema/row-layout audit: PASS.
- Exp073S0 exact DES Y1 redMaGiC mask + released lens/source n(z) reproduction: `PASS_DESY1_REDMAGIC_MASK_NZ_REPRODUCTION_EXP073S0`.
- Exp073R0 raw-row decoder + HEALPix mapper equivalence ultimately obtained a genuine PASS and authorized R1.

## Active Exp073R1

GitHub Actions run `33108733415` was launched from commit `af0b3c40ac37a8847d3f7b5f2c38dda6f7f09da4` after genuine Exp073R0 PASS. At this audit it is still `in_progress` in the frozen `Execute frozen Exp073R1 one-pass construction` step.

Exp073R1 is strictly a reproduction/input-construction gate. Its workflow explicitly asserts:

- exact source/metacal row counts `136930995` each;
- exact checksum-bound DES Y1 inputs;
- frozen selection and `hp.ang2pix(4096, ra, dec, lonlat=True)` mapping;
- deterministic mask/provenance controls;
- `science_gate_scored == false`;
- `f_invalid_computed == false`;
- `covariance_read == false`;
- `G8_read == false`.

Do not duplicate this active heavy run.

## Next admissible transition

1. Resolve Exp073R1 under its already-frozen R1 classification only.
2. If R1 is `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`, verify the immutable artifact and that all Exp073P input/operator prerequisites are PASS.
3. Only then execute the already-preregistered Exp073P support calculation with the unchanged rectangle, 5% threshold, minimum dimension 15 and `nside=4096`.
4. Only a genuine `PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P` may authorize covariance restriction/whitening.
5. Nuisance tangent rank/SVD remains downstream of covariance restriction/whitening; quotient/relation/null remains downstream of nuisance control; fresh G8 withheld-family evaluation remains last.

If R1 deterministically violates its frozen reproduction contract, preserve a scientific/reproduction FAIL. If network/storage/package/runner interruption prevents complete deterministic evaluation, preserve `INCOMPLETE_EXP073R1` as infrastructure only. No threshold relaxation is authorized in either case.

## Gate state

- G7: OPEN
- Exp073P physical-support scoring: BLOCKED pending Exp073R1 resolution
- covariance restriction/whitening: CLOSED
- nuisance tangent rank/SVD: CLOSED
- quotient/relation/null control: CLOSED
- fresh G8 withheld family: CLOSED
