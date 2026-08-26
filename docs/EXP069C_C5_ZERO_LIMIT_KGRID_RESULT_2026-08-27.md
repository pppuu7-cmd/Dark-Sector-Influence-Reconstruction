# Exp069C result — C5 exact-zero k-grid mechanism audit

Date: 2026-08-27

## Scientific classification

Exp069C is descriptive only and cannot certify C5.

Frozen classifications:

- `RAW_POWER_ZERO_LIMIT_RESIDUAL`
- `KGRID_NONCONVERGENCE`

Exp069B remains permanently `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.

## Immutable provenance

- PR: #78
- preregistration commit: `44a9f5540eef7e4702c8ca9545048f239a36eb05`
- implementation/workflow head: `8ed8028b3fafc656ddc7ee6b217a812aa9be2521`
- workflow run: `33016782748`
- artifact id: `9625109424`
- artifact digest: `sha256:efbf9f80d71bce59f3441e51295d97c66073dd28d2583268c478636968c85cb8`
- pinned solver: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`

## Frozen k-grid scan

The audit compared ordinary GR and explicit designer-EFT `B0=0` at

`k_per_logint = [40,80,160,320]`

without changing the Exp069B physics, redshifts, target physical k grid, variable pairs, or kmax.

GR and designer-zero raw k grids are bitwise identical in all three blocks at every scan point. Therefore there is no `RAW_GRID_MISMATCH`.

### Target-grid maximum absolute residuals

| k_per_logint | P_mm | P_Wm | P_WW |
|---:|---:|---:|---:|
| 40 | 5.3455474764e-6 | 5.3688467371e-6 | 5.2658168439e-6 |
| 80 | 5.3064260596e-6 | 5.2898467572e-6 | 5.3517542934e-6 |
| 160 | 5.4137258816e-6 | 5.3628951192e-6 | 5.3694073737e-6 |
| 320 | 5.2875321151e-6 | 5.2608867052e-6 | 5.3029219262e-6 |

The preregistered convergence rule required the `k_per_logint=320` maximum to be at most half the `80` value in all three blocks. This fails strongly: the residual remains essentially unchanged. Hence `KGRID_NONCONVERGENCE`.

### Same-node raw-power residuals

Maximum raw-grid residual inside the region bracketing the frozen target k values:

| k_per_logint | P_mm | P_Wm | P_WW |
|---:|---:|---:|---:|
| 40 | 7.3195261045e-6 | 7.3797138355e-6 | 7.4069065014e-6 |
| 80 | 7.4917398825e-6 | 7.3462552739e-6 | 7.3268902554e-6 |
| 160 | 7.4917413034e-6 | 7.4328104134e-6 | 7.4208286014e-6 |
| 320 | 7.5672233042e-6 | 7.5957975807e-6 | 7.5958592006e-6 |

Thus the ppm-scale exact-zero discrepancy already exists in the solver-returned same-node powers. It is not created by DSIR target-grid interpolation. This is the hard basis for `RAW_POWER_ZERO_LIMIT_RESIDUAL`.

### Cross-block structure

Flattened target residual fields remain almost common-mode across `P_mm`, `P_Wm`, and `P_WW`. At `k_per_logint=320` the correlations are approximately:

- mm/Wm: `0.9998508557`
- mm/WW: `0.9995629927`
- Wm/WW: `0.9998044549`

The high correlation is descriptive evidence that the zero-limit defect is predominantly shared across the three returned power blocks, but it does not identify its deeper solver mechanism by itself.

## Scientific consequence

Exp069C rules out the simplest corrective hypothesis: increasing `k_per_logint` does not restore the frozen `5e-6` Exp069B GR-limit criterion, and interpolation is not the source of the discrepancy.

Therefore no corrective C5 bridge may be justified merely by changing the k-grid/interpolator. The next admissible step is a separately preregistered solver-mechanism audit of the explicit designer `B0=0` branch versus ordinary GR, focusing on branch/accuracy/background/source evolution rather than k sampling.

G7/G8/G9 remain OPEN. A common C3+C5 support-validity mask is still forbidden until C5 has a certified physical provider.
