# DSIR recovery checkpoint — Exp073R1 → Exp073P execution-integrity matrix

**Date:** 2026-08-28

## Purpose

Preserve a prospective execution-integrity audit while Exp073R1 is still running. This document does not change any frozen scientific acceptance criterion, does not score Exp073P, and does not authorize downstream G7 stages.

## Bound current state

- `main` before this checkpoint: `bc22ed867c6ddfade4a0d6f83a6dbdec3a680eb5`.
- Active Exp073R1 Actions run: `33108733415`.
- Run head: `af0b3c40ac37a8847d3f7b5f2c38dda6f7f09da4`.
- At audit time the job is still in `Execute frozen Exp073R1 one-pass construction`; parent R0 binding and runtime installation have passed.
- The active run must not be duplicated while it remains live.

## Frozen Exp073P controls versus current R1 role

| Exp073P control | Frozen requirement | R1 status / boundary |
|---|---|---|
| P1 parent binding | Preserve Exp073O and frozen BOSS mm lineage | R1 binds only its immediate genuine Exp073R0 PASS; full Exp073P P1 remains to be asserted by the Exp073P execution record. |
| P2 DES checksum binding | Every consumed DES Y1 object checksum-bound before support scoring | R1 recomputes exact source/metacal SHA256; earlier P2/S0 chain binds the remaining release objects. Exp073P must re-bind the complete consumed set before scoring. |
| P3 operator reproduction | Pinned Cosmotheka/NaMaster semantics | R1 constructs the full DES weak-lensing mask only. It does not claim P3 completion. |
| P4 positive-envelope normalization | Finite positive total envelope for every classifying row | Not evaluated in R1; must remain downstream. |
| P5 physical units | Explicit `ell`, distance, `k [Mpc^-1]` controls | Not evaluated in R1; must remain downstream. |
| P6 unchanged support threshold | `f_invalid <= 0.05`, `0.295 <= z <= 2.33`, `k <= 0.06664762008318016 Mpc^-1` | R1 explicitly has `f_invalid_computed == false`; therefore it cannot contaminate or tune P6. |
| P7 full-coordinate rule | Combine Wm, WW, BOSS only after valid block masks; minimum dimension 15 | Not evaluated in R1. |
| P8 no downstream leakage | No covariance/whitening, nuisance SVD, quotient/null, G8 | R1 asserts `covariance_read == false` and `G8_read == false`; science scoring is false. |

## Post-R1 admissibility checklist

If and only if a canonical Exp073R1 execution completes successfully and its immutable artifact is present:

1. Verify workflow identity and successful conclusion; do not infer PASS from Actions success alone.
2. Download the single authoritative Exp073R1 artifact and verify the JSON classification is exactly `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.
3. Recheck exact source/metacal row counts `136930995` each.
4. Recheck authoritative source SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5` and metacal SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`. The previously transcribed source value `491f4bb742762fefe3aaab6d53d4342b6ff4a65401bc7b588d2918fdce3ee6fd` is obsolete/wrong per the dedicated provenance-fix checkpoint and MUST NOT be accepted.
5. Require every R1 hard control true and preserve mask hashes, selected-row counts and immutable provenance.
6. Require `science_gate_scored == false`, `f_invalid_computed == false`, `covariance_read == false`, `G8_read == false`.
7. Bind the already frozen Exp073P preregistration without modifying rectangle, threshold, dimension floor, `nside=4096`, bin edges or classification labels.
8. Only then execute the physical-support calculation needed for P3–P7.

If R1 deterministically violates its frozen reproduction contract, preserve that reproduction FAIL. If execution is interrupted by runner/network/storage/package conditions before a trustworthy deterministic result, record infrastructure `INCOMPLETE_EXP073R1`; do not relabel it scientific FAIL.

## Downstream lock

Until Exp073P itself returns `PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P` under the unchanged preregistration:

- covariance restriction/whitening: BLOCKED;
- nuisance tangent rank/SVD: BLOCKED;
- quotient/relation/null control: BLOCKED;
- fresh G8 withheld family: BLOCKED.

The older Exp072a support result remains a frozen scientific hard FAIL and is not reopened by this route.
