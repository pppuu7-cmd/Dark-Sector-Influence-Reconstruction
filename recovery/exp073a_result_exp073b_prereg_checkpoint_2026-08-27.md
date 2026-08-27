# DSIR recovery checkpoint — Exp073A result + Exp073B preregistration — 2026-08-27

## New immutable result

Exp073A completed as

`INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`.

Provenance:

- merge `03c9d0281a6ea780d29c6fb4a689dbd55e51fdf5`;
- run `33032781761`;
- job `98388840817`;
- artifact `9630897385`;
- artifact digest `sha256:0f2212d691c38c3e953d2a0d823b498a5557b9485fc759079719000cdc48cb25`;
- extracted JSON SHA256 `a8bbafa971283cadf9ff27a27af4d0c4e3042bc0aec590d690142d39c919abb2`;
- P1–P8 all PASS.

The exact Exp072C geometric route was reproduced first. After the frozen perturbativity mask:

- `Delta2<=0.5`: retained dimension `0`;
- `Delta2<=1`: retained dimension `0`;
- `Delta2<=2`: retained dimension `0`.

At primary `Delta2<=1`, only `7/64` pairs individually remain within the unchanged 5% combined-invalid threshold. Median incremental non-perturbative fraction is `0.33104901805931586`; maximum sampled `Delta2` inside the geometry is `10.106721461271324`.

The pinned CAMB reference was finite, positive and non-extrapolated on all `348469` used cells. Unit roundtrip maximum relative discrepancy was `2.98e-15` versus frozen tolerance `2e-8`.

Therefore blind linear C3/C5 extension to the Exp072C frontier is scientifically blocked.

## Current preregistered next experiment

`experiments/073b_solver_neutral_nonlinear_matter_weyl_feasibility_prereg_v0_1.md`

is frozen before any Exp073B capability output.

It asks whether the existing pinned stack contains a physically defensible nonlinear route with independent

- `P_mm`;
- signed `P_Wm`;
- `P_WW`;

for both C3/GDM and C5/designer-f(R) over the required low-z/high-k support.

Forbidden shortcuts include GR matter-to-Weyl closure, rank-one nonlinear closure, generic GR HALOFIT/HMcode promoted to MG Weyl physics, linear-Weyl times nonlinear-matter boost, extrapolation, or downstream fit-driven closure choice.

Allowed completed Exp073B outcomes:

- `FEASIBLE_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B`;
- `GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B`;
- `FAIL_EXP073B_REPRODUCTION_OR_PROVENANCE`.

## Gate state

- covariance restriction: NOT AUTHORIZED;
- whitening: NOT AUTHORIZED;
- nuisance SVD/rank: NOT AUTHORIZED;
- G7 relation/null: NOT AUTHORIZED;
- G8: NOT AUTHORIZED;
- G7/G8/G9: OPEN.

Repository-sync policy remains active: update immutable result, provenance, checkpoint and next admissible preregistration after each research iteration.
