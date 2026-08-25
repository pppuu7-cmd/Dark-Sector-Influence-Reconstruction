# Experiment 043 — GDM gauge precision convergence v0.1

**Date:** 2026-08-25  
**Status:** protocol frozen before p10 target output  
**Scope:** numerical diagnosis of the failed Experiment 042 synchronous/Newtonian comoving-matter bridge

## Motivation

Experiment 042 reached its pre-frozen gauge bridge and returned scientific status `FAIL_GDM_SYNC_NEWTONIAN_DELTA_BRIDGE_V0_2`. The failure must not be repaired by loosening thresholds after inspection.

The observed p8 diagnostics were nevertheless structured: the model/reference response bridge remained below its pre-frozen `1e-6` ceiling, while the absolute comoving-Delta bridge was at a few `1e-6`. Experiment 043 asks whether the absolute mismatch is dominated by perturbation-integration precision.

## Immutable physics

Pinned upstream and frozen C3 manifold are unchanged:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

The four diagnostic models are `gdm0`, `gdmcs2_1em6`, `gdmcv2_1em6`, and `gdmcv2_1em4`. Cosmological and microphysical INI parameters remain identical to the hard C3 artifact.

Both synchronous and Newtonian runs request only additional `mTk,vTk` outputs. The p8 precision file is the exact frozen `dsir_p8.pre` from the source artifact.

## Precision intervention

The p10 diagnostic changes only

- `tol_perturb_integration: 3e-10 -> 3e-12`;
- `perturb_sampling_stepsize: 0.00035 -> 0.00015`.

No physics parameter, gauge convention, k range, redshift, or response definition changes.

## Operator

For baryons+GDM with frozen `w_gdm=0`, use

\[
\delta_m=w_b\delta_b+w_g\delta_g,\qquad
\theta_m=w_b\theta_b+w_g\theta_g,
\]

and

\[
\Delta_m=\delta_m+3{\cal H}\theta_m/k^2.
\]

Each gauge output is interpolated independently onto the frozen DSIR nodes before comparison. The raw CLASS transfer grids are not required to be identical because their adaptive sampling is gauge-dependent.

## Thresholds frozen before p10 output

Experiment 043 passes only if all of the following hold:

1. p10 maximum absolute `ln|Delta_S/Delta_N| <= 1e-6`;
2. p10 maximum model/reference Delta-response difference between gauges `<=1e-6`;
3. the absolute bridge residual decreases by at least a factor of two relative to the p8 rerun:

\[
R_{conv}=\frac{E_{p10}}{E_{p8}}\le0.5.
\]

These thresholds are frozen before any p10 target output.

## Claim boundary

A PASS would support a numerical-precision explanation for the Exp042 absolute bridge failure, but would **not** retroactively convert Experiment 042 into PASS and would not validate any exploratory velocity angle or `D_RSD` value. A FAIL leaves the GDM Newtonian velocity/RSD route unvalidated and motivates an analytic gauge/source-output audit rather than threshold relaxation.
