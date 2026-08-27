# DSIR recovery checkpoint — Exp073F FOUND / Exp073G preregistered

**Date:** 2026-08-27

## Verified parent

Starting `main` for this iteration: `94553dd1053b062b274f030ee842530ea62f24b1` (`Merge Exp073E completion boundary and Exp073F preregistration`).

Preserve permanently:

- Exp073E: `C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E`;
- ACT x unWISE linear/nonlinear C3 route remains blocked before covariance;
- G7/G8/G9 remain OPEN.

## Exp073F completed landscape classification

`PERTURBATIVE_OBSERVATIONAL_ROUTE_CANDIDATE_FOUND_EXP073F`.

Primary candidate:

`KiDS-1000 + BOSS 3x2pt with prospective BNT physical-scale localization`

Landscape label:

`PROMISING_FOR_EXACT_SUPPORT_AUDIT`.

This is **not** a support PASS. The candidate is promising because public 3x2pt structure supplies separate matter clustering, galaxy-galaxy-lensing cross and cosmic-shear channels, while BNT provides an operator-level route to localize tomographic shear support in redshift/physical k.

No covariance entries, nuisance rank/SVD, relation residuals, G8 or held-out performance were used in the ranking.

Frozen support remains exactly:

- `z in [0.295, 2.33]`;
- `k in [0.000704833374744468, 0.06664762008318016] Mpc^-1`;
- positive-weight leakage <= `0.05`.

## Next gate frozen before exact support output

Exp073G preregistration:

`experiments/073g_kids_boss_bnt_exact_physical_support_prereg_v0_1.md`

Only Exp073G may decide whether this candidate actually passes physical support.

Important frozen rules:

- exact public release/archive identities and SHA256 before classification;
- exact BNT matrix convention frozen before transformed support output;
- support uses non-negative envelopes, while physical `P_Wm` remains signed;
- broad released windows must be integrated, not replaced by effective coordinates;
- no covariance/rank/relation/G8 reads;
- support PASS requires separate retained mm/Wm/WW channels and >=15 total retained coordinates;
- only `PASS_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073G` may authorize later covariance restriction/whitening.

## Resume procedure

1. Read current `main`; do not assume this branch has merged until verified.
2. Verify Exp073F result + machine JSON + Exp073G prereg are on `main`.
3. Resolve the exact KiDS-1000 public data/repository archive identities linked by the release pages and freeze their hashes/version IDs.
4. Implement Exp073G as a provenance-first operator audit. Before calculating any final support retained dimension, freeze n(z), BNT convention, eligible BOSS lens selections and released angular/window objects.
5. Run exact support integration. Treat download/build/source-binding failure as reproduction/infrastructure, never scientific support FAIL.
6. After a completed iteration, update result provenance and this recovery lineage in the repository.

G7 OPEN. G8 OPEN. G9 OPEN.
