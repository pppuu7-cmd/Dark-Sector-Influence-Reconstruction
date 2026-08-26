# Exp069C — C5 zero-limit k-grid/interpolation mechanism audit v0.1

**Date:** 2026-08-26  
**Status:** descriptive mechanism audit frozen before new Exp069C numerical output.

## Purpose

Exp069B remains permanently `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1` because its exact designer `B0=0` versus standard-GR residual exceeded the frozen `5e-6` threshold by a small amount. Exp069C does **not** retest or rescue that gate. It asks why the residual is strongly k-dependent and nearly common across `P_mm`, `P_Wm`, and `P_WW`.

The immutable Exp069B artifact shows, after averaging over redshift and all three blocks, signed residuals approximately

- near zero at `k=0.003 Mpc^-1`;
- `+5.11e-6` at `k=0.03 Mpc^-1`;
- `-3.63e-7` at `k=0.10 Mpc^-1`;
- `-5.19e-6` at `k=0.20 Mpc^-1`;

with inter-block residual correlations above `0.9992`.

A prior independent pinned native-executable exact-`B0=0` calibration (run `32735136430`) had a maximum total-matter residual `1.0926960404022163e-6` on its then-frozen core grid, showing that a smaller zero-limit residual is possible in the same solver lineage.

## Frozen solver/physics

Use the same H-EFTCAMB commit, cosmology, explicit EFT dictionary, `B0=0`, redshift grid, physical target k grid and direct variable pairs as Exp069B. No physical parameter is changed.

Pinned solver:
`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Target grid:

`z = {0,0.295,0.51,0.934,1.491,2.33,3.0}`

`k = {0.003,0.01,0.03,0.10,0.20} Mpc^-1`.

## Frozen diagnostic scan

Repeat only the standard-GR and explicit-designer-`B0=0` calculations at

`k_per_logint = {40,80,160,320}`

with `kmax=0.30 Mpc^-1`; all other settings remain fixed.

For each precision point and each block `mm`, `Wm`, `WW`, record:

1. the raw k/h nodes returned by `get_linear_matter_power_spectrum` for GR and designer zero;
2. whether the raw k grids are bitwise identical;
3. raw-grid signed relative residuals where grids coincide;
4. the standard `get_matter_power_interpolator` residual on the Exp069B target grid;
5. mean/std/min/max residual by target k over redshift;
6. correlations of flattened target-grid residuals between the three blocks;
7. maximum absolute residual on the target grid.

## Descriptive classifications fixed before output

This audit has no PASS capable of certifying C5. It may report one or more of:

- `RAW_GRID_MISMATCH` if GR and designer-zero raw k grids differ;
- `RAW_POWER_ZERO_LIMIT_RESIDUAL` if same-node raw powers already carry the ppm-scale structure;
- `INTERPOLATION_AMPLIFICATION` if target-grid spline residual materially exceeds same-region raw-grid residual;
- `KGRID_CONVERGENCE` if increasing `k_per_logint` systematically reduces the target-grid maximum residual;
- `KGRID_NONCONVERGENCE` otherwise.

For the convergence label only, define prospectively: compare the maximum target-grid residual at 80 versus 320. `KGRID_CONVERGENCE` requires the 320 value to be at most half the 80 value in all three blocks. This is diagnostic, not a C5 certification threshold.

No new GR-limit acceptance threshold may be introduced here.

## Interpretation boundary

If the audit identifies a numerical mechanism, a separately numbered future corrective bridge may preregister a justified numerical setting while retaining a hard GR-limit criterion. Exp069B remains FAIL regardless.

G7/G8/G9 remain OPEN.
