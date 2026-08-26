# C5 designer-f(R) exact-zero source mechanism audit

Date: 2026-08-27
Pinned upstream: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`

## Why this audit exists

Exp069B is a permanent scientific FAIL because the explicit designer-EFT `B0=0` branch missed the frozen ordinary-GR power closure threshold `5e-6` by a small amount. Exp069C then showed that the discrepancy already exists in same-node raw powers and does not converge away when `k_per_logint` is increased from 40 to 320. Therefore neither DSIR target interpolation nor the CAMB matter-power k sampling is an admissible corrective mechanism.

## Pinned-source findings

The pinned upstream source gives a more specific causal boundary:

1. Ordinary GR and designer f(R) are different EFTCAMB execution branches. The upstream GR test uses `EFTflag=0`, while the designer f(R) tests use `EFTflag=3`, `DesignerEFTmodel=1` and an explicit `EFTB0`.
2. The designer f(R) background initializer does not expose a special `B0==0 -> ordinary GR` short circuit. It calls `find_initial_conditions`, which maps the designer initial amplitude `A` to the requested present-day `B0`, and then solves/stores the designer equations.
3. `find_initial_conditions` solves `B0(A)=B0_wanted` with an ad-hoc bracketing procedure because `B0(A)` is not continuous. The final root solve uses `zbrent(...,1.d-50,self%B0,...)` and returns that root as `A_ini`.
4. The designer background equations are integrated with DLSODA using hard-coded `rtol=1.d-12` and `atol=1.d-16` in this pinned source. These are not ordinary INI knobs.
5. The designer model allocates equispaced linear interpolators for stored background/EFT functions; the source reads a configurable `model_background_num_points` with default 6000.
6. EFTCAMB also exposes a Return-to-GR path with configurable `EFTCAMB_GR_threshold` (default `1e-8`) and `EFTCAMB_skip_RGR`. The RGR module samples 1000 logarithmic scale-factor points and decides whether EFT functions are below the requested GR threshold.
7. In a designer model the expansion history is parametrized first and does not depend on the EFT functions; the EFT functions are computed on top of that expansion history. Thus a GR-vs-designer-zero background comparison is an informative discriminator between geometry/background and perturbative-EFT mechanisms.

## Consequence

The next admissible experiment is not another generic CAMB accuracy scan. It should separately vary the **designer background storage resolution** and the **Return-to-GR controls**, while measuring both geometry/background outputs and the same three power blocks (`P_mm`, signed `P_Wm`, `P_WW`).

Possible mechanism labels are therefore restricted to:

- `DESIGNER_BACKGROUND_GRID_LIMITED`;
- `RETURN_TO_GR_PATH_SENSITIVE`;
- `BACKGROUND_GEOMETRY_MISMATCH`;
- `PERTURBATION_EFT_BRANCH_FLOOR`;
- `MIXED_OR_UNRESOLVED_DESIGNER_ZERO_MECHANISM`.

This is a causal audit only. None of these labels can reclassify Exp069B or certify C5 by itself.
