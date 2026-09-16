# Exp069D — C5 designer-zero branch mechanism audit v0.1

Date frozen: 2026-08-27

## Purpose

Exp069B remains permanently `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`. Exp069C localized its exact-zero defect to solver-returned same-node powers and found `KGRID_NONCONVERGENCE` under `k_per_logint=40,80,160,320`.

Exp069D is a **mechanism audit only**. It asks whether the remaining explicit-designer `B0=0` versus ordinary-GR discrepancy is controlled by:

1. the designer background/EFT interpolation-grid resolution;
2. EFTCAMB Return-to-GR (RGR) logic;
3. an actual background/geometry mismatch;
4. a residual perturbative explicit-EFT branch floor;
5. or mixed/unresolved behavior.

It cannot certify C5 and cannot reclassify Exp069B.

## Frozen provenance

- DSIR base: `77aab549aef38a794533a758dbbabdcc0efcc03c`.
- pinned solver: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.
- Exp069B frozen threshold remains `5e-6`; it is not reused as a tunable threshold here.
- Exp069C result labels: `RAW_POWER_ZERO_LIMIT_RESIDUAL`, `KGRID_NONCONVERGENCE`.
- Source audit: `docs/C5_DESIGNER_ZERO_SOURCE_MECHANISM_AUDIT_2026-08-27.md`.

## Frozen cosmology and power outputs

Reuse the exact Exp069B/069C cosmology/configuration and variables:

- redshifts `z=[0.0,0.295,0.51,0.934,1.491,2.33,3.0]`;
- physical target `k=[0.003,0.01,0.03,0.10,0.20] Mpc^-1`;
- `kmax=0.30 Mpc^-1`;
- linear powers only;
- blocks:
  - `P_mm`: `delta_nonu x delta_nonu`;
  - signed `P_Wm`: `Weyl x delta_nonu`;
  - `P_WW`: `Weyl x Weyl`;
- physical units: `hubble_units=False`, `k_hunit=False`;
- explicit designer point: `EFTflag=3`, `DesignerEFTmodel=1`, `EFTwDE=0`, `EFTB0=0` with the same stability flags as Exp069B;
- ordinary GR comparator: no explicit EFT activation (`EFTflag=0`).

For all Exp069D runs freeze `k_per_logint=320`, because Exp069C already demonstrated that changing the matter-power k sampling over 40..320 does not remove the defect.

## Scan A — designer background-grid resolution

Vary only the explicit designer parameter

`model_background_num_points = [3000,6000,12000,24000]`.

The ordinary-GR comparator is rerun for each pair but receives no designer background-grid parameter.

For every resolution record:

- target-grid signed fractional residual fields for all three power blocks;
- target maximum absolute residual for each block;
- raw same-node residuals where the GR/designer raw grids are bitwise equal;
- `H(z)` and comoving radial distance `chi(z)` from the two result objects at the frozen redshifts;
- designer readback of the requested EFT parameters and branch identity.

### Frozen background-grid attribution rule

Define

`M_N = max over {mm,Wm,WW} of target max-abs residual at model_background_num_points=N`.

Classify `DESIGNER_BACKGROUND_GRID_LIMITED` iff **both**:

1. `M_24000 <= 0.5 * M_6000`, and
2. `M_24000 < M_12000 < M_6000`.

Otherwise this label is false.

No scientific provider threshold is implied by this 2x mechanism-attribution rule.

## Scan B — Return-to-GR sensitivity

At `model_background_num_points=6000`, run the designer-zero branch under exactly these RGR settings:

- baseline: `EFTCAMB_skip_RGR=False`, `EFTCAMB_GR_threshold=1e-8`;
- skip: `EFTCAMB_skip_RGR=True`, `EFTCAMB_GR_threshold=1e-8`;
- tight: `EFTCAMB_skip_RGR=False`, `EFTCAMB_GR_threshold=1e-10`;
- loose: `EFTCAMB_skip_RGR=False`, `EFTCAMB_GR_threshold=1e-6`.

The ordinary-GR comparator remains unchanged.

Let `M_s` be the all-block target max residual for each setting.

Classify `RETURN_TO_GR_PATH_SENSITIVE` iff

`max(M_s)/min(M_s) >= 2`.

This is a causal sensitivity label only. No RGR setting is promoted as a corrective provider by this experiment.

## Background/geometry discriminator

For every scan case compare ordinary GR and designer-zero at the frozen redshifts using:

- `H(z)`;
- comoving radial distance `chi(z)`.

Define

`B = max(max_rel_H, max_rel_chi_nonzero_z)`.

Freeze the geometry-match boundary at `1e-9`.

Classify `BACKGROUND_GEOMETRY_MISMATCH` iff the baseline `B > 1e-9`.

This threshold is an attribution boundary, not a C5 certification tolerance. The prior same-designer-branch AP audit already found the C5 manifold background/AP-null at `1e-8`; Exp069D tightens the direct GR-vs-designer-zero diagnostic by one decade because Python result objects avoid text-table rounding.

## Perturbative branch-floor discriminator

Classify `PERTURBATION_EFT_BRANCH_FLOOR` iff all of the following hold:

1. baseline geometry discriminator passes: `B <= 1e-9`;
2. `DESIGNER_BACKGROUND_GRID_LIMITED` is false;
3. `RETURN_TO_GR_PATH_SENSITIVE` is false;
4. the baseline power residual is nonzero and `>= 1e-6` in at least one of the three blocks.

The `1e-6` floor is intentionally below the already-observed Exp069B/069C ~5e-6 residual and is used only to require a material, reproducible perturbative discrepancy rather than roundoff.

## Mixed/unresolved rule

If none of the four labels above gives a unique causal localization, or if more than one of `DESIGNER_BACKGROUND_GRID_LIMITED`, `RETURN_TO_GR_PATH_SENSITIVE`, `BACKGROUND_GEOMETRY_MISMATCH` is simultaneously true, classify

`MIXED_OR_UNRESOLVED_DESIGNER_ZERO_MECHANISM`.

If exactly one primary mechanism is true, retain that primary label and report all descriptive secondary diagnostics.

## Controls

Exp069D must also verify:

- pinned solver commit exact match;
- explicit designer branch/readback remains active in all designer runs;
- requested `EFTB0=0` reads back as exactly zero to the same numeric readback contract used in Exp069B;
- all runs remain linear (`NonLinear_none`);
- no target-k, redshift, cosmology, transfer-variable, sign, or physical-unit change from Exp069B/069C;
- no modification of upstream Fortran source;
- no change to DLSODA hard-coded `rtol=1e-12`, `atol=1e-16`;
- Exp069B status remains permanent FAIL in the output;
- C5 certification remains false;
- common support-validity mask remains unauthorized;
- gate state exactly `G7=OPEN, G8=OPEN, G9=OPEN`.

## Output status

Exp069D has descriptive status

`DESCRIPTIVE_C5_DESIGNER_ZERO_BRANCH_MECHANISM_AUDIT_V0_1`.

It does **not** have a scientific PASS that certifies a provider.

## Next-step boundary

A corrective C5 provider may be preregistered only after Exp069D identifies a causal mechanism that supports a physically legitimate, solver-faithful construction. In particular:

- a background-grid or RGR sensitivity may motivate a new provider experiment, but the new provider must receive its own frozen exact-GR-limit criterion;
- a `PERTURBATION_EFT_BRANCH_FLOOR` or unresolved result forbids threshold relaxation and requires either a source-level exact-zero branch control or a different validated physical provider strategy.

Until then the common C3+C5 support-validity mask is forbidden and G7/G8/G9 remain OPEN.
