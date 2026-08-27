# Exp073A — GR-reference linear/no-CLEFT perturbativity eligibility result v0.1

**Date:** 2026-08-27  
**Scientific classification:** `INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`

## Immutable provenance

- implementation merge: `03c9d0281a6ea780d29c6fb4a689dbd55e51fdf5`;
- workflow run: `33032781761`;
- workflow job: `98388840817`;
- artifact: `9630897385`;
- artifact digest: `sha256:0f2212d691c38c3e953d2a0d823b498a5557b9485fc759079719000cdc48cb25`;
- extracted JSON SHA256: `a8bbafa971283cadf9ff27a27af4d0c4e3042bc0aec590d690142d39c919abb2`.

All frozen P1–P8 controls passed. This is therefore a completed scientific negative result, not an infrastructure outcome.

## Result

Exp073A first reproduced the exact unique Exp072C geometric frontier and its 15-coordinate route, then applied the preregistered GR-reference perturbativity mask using

`Delta2_m = k^3 P_mm^lin/(2*pi^2)`.

The primary `Delta2_m<=1` route retains `0/26` full observation coordinates. The two preregistered non-classifying sensitivity masks also retain `0/26`:

- `Delta2_m<=0.5`: `0/26`;
- `Delta2_m<=1`: `0/26`;
- `Delta2_m<=2`: `0/26`.

At the primary threshold only `7/64` coordinate-block pairs individually remain below the unchanged 5% combined-invalid fraction, but no full coordinate survives all of its required blocks.

Primary pair diagnostics:

- median incremental non-perturbative fraction: `0.33104901805931586`;
- maximum incremental non-perturbative fraction: `0.8399156776753174`;
- median combined invalid fraction: `0.34145708039221284`;
- maximum combined invalid fraction: `0.9501004682310411`;
- maximum sampled `Delta2_m` inside the frozen geometry: `10.106721461271324`.

## Reference integrity

The pinned CAMB linear matter reference was evaluated on `348469` geometrically valid frontier cells. Every used `P_mm` and `Delta2_m` value was finite and positive; every cell was inside the non-extrapolated interpolator support. The physical-unit roundtrip control achieved maximum relative discrepancy `2.98e-15`, far below the frozen `2e-8` tolerance.

Therefore the loss of the route is not attributable to k-unit conversion, extrapolation, parent-geometry reproduction or provenance failure.

## Scientific interpretation

The unique Exp072C rectangle is geometrically sufficient but not compatible with the current purely linear/no-CLEFT premise even under the relaxed diagnostic `Delta2_m<=2` screen.

This closes the proposed strategy of blindly extending the existing linear C3 and C5 providers to approximately `k=4.818 Mpc^-1` and `z=0.00873`. Such an extension could produce numbers but would not restore a physically eligible linear observational route under the already-frozen criteria.

This is not a failure of GDM, designer-f(R), dark energy, modified gravity or DSIR. It is a negative result for the current linear ACT×unWISE observational realization.

## Downstream rule

No covariance restriction, whitening, nuisance SVD/rank, G7 relation/null calculation or G8 selection is authorized.

The next admissible research branch is a separately preregistered solver-neutral nonlinear feasibility audit requiring independent matter/Weyl treatment. In particular, nonlinear matter power may not be silently converted into nonlinear Weyl auto/cross power through a GR matter-to-Weyl closure for MG/dark-sector models.

Exp072A/B/C classifications remain unchanged. G7/G8/G9 remain OPEN.
