# Exp069E — result: C5 exact-zero source-native RGR function floor v0.1

Date: 2026-08-27  
Status: **SCIENTIFIC COMPLETE / MECHANISM RESULT — NOT A C5 PROVIDER PASS**

Preregistration: `experiments/069e_c5_exact_zero_rgr_function_floor_prereg_v0_1.md`  
Run: `33021872783`  
Merge head: `016681f5dc4fdca675673332d704def5be246a96`  
Artifact digest: `sha256:850abec97ae2d7b3f066328292c17cac85990ad7c911e166f294ac6419ead584`

## Frozen primary result

The exact-zero source-native classification is

`EXACT_ZERO_RGR_SUBSET_NONZERO`.

The maximum selected Return-to-GR subset entry is

`F0 = 4.7401579076280133e-17`.

Relative to float64 machine epsilon,

`F0 / eps_float64 = 0.2134777338647083`.

The corresponding all-block ordinary-GR power residual is

`M0 = 5.302921926164412e-6`.

Thus the literal designer-zero branch does contain a nonzero selected EFT-function residue, but it is below one float64 epsilon in the frozen normalized source coordinates and is about eleven orders of magnitude below the observed power discrepancy scale. The hypothesis that a finite source-native background EFT residue of comparable magnitude directly explains the ppm power floor is therefore rejected.

## Frozen positive controls

| B0 | F(B0) | M(B0) |
|---:|---:|---:|
| 0 | 4.7401579076280133e-17 | 5.302921926164412e-6 |
| 1e-12 | 1.9731606304867062e-13 | 5.302921926164412e-6 |
| 1e-10 | 1.974815515417979e-11 | 5.302921926164412e-6 |
| 1e-8 | 1.9748136785694854e-9 | 5.302921926164412e-6 |
| 1e-6 | 1.9748134096796163e-7 | 1.3245195366540058e-2 |

The frozen descriptive diagnostics are:

- `F_monotone_nondecreasing = true`;
- `M_monotone_nondecreasing = true`;
- `Pearson(log10 B0, log10 F) = 0.9999999990049508`;
- `Pearson(log10 F, log10 M) = 0.7745778738675414`.

The source-native EFT amplitude therefore tracks B0 extremely cleanly, while the power result exhibits a fixed low-B0 floor before the production-scale signal emerges.

## Post-output diagnostic that does not alter the frozen classification

After the frozen result was read, the immutable case artifacts were compared directly. This is explicitly retrospective/descriptive.

For `B0 = 1e-12, 1e-10, 1e-8`, every stored raw and target power value in all three blocks

- `P_mm`,
- signed `P_Wm`,
- `P_WW`

is bitwise identical to the explicit-EFT `B0=0` case, while the underlying EFT-function measure `F(B0)` changes by orders of magnitude.

The ordinary-GR versus explicit-zero residual has a nearly common shape across the three blocks. On the frozen target grid the residual-array correlations are approximately

- `corr(mm,Wm) = 0.9998508557`;
- `corr(mm,WW) = 0.9995629927`;
- `corr(Wm,WW) = 0.9998044549`.

It is also much more scale-dependent than redshift-dependent. Typical target residual means across redshift are approximately

- near `k=0.03 Mpc^-1`: `+5.1e-6`;
- near `k=0.20 Mpc^-1`: `-5.2e-6`;

with only ~1e-7-level redshift variation around those scale-dependent means.

The raw k and z grids of ordinary GR and designer zero are exactly identical in the stored artifacts, so this pattern is not a mismatch of sampled k nodes.

## Source-level interpretation

The pinned Return-to-GR routine scans EFT functions from `EFTCAMB_pert_turn_on` to `a=1`. If no selected full RGR entry exceeds `EFTCAMB_GR_threshold`, it returns `RGR_time=1.1`. In `results.f90`, that value replaces `EFTCAMB_pert_turn_on`.

The Exp069E low-B0 plateau is therefore consistent with the EFT perturbation sector never activating for the tiny-B0 cases. Yet those cases retain the same 5.3 ppm difference from ordinary GR.

Together with the near-redshift-independent, common-block, k-dependent residual shape, this pushes the origin of the floor upstream of late-time EFT perturbation evolution, toward the explicit-EFT background/thermal/transfer numerical path or its general integration accuracy.

## What Exp069E changes

Exp069E rules out the most direct finite-background-residue explanation of the power floor. It does **not** certify a special-case GR dispatch and it does not justify subtracting the B0=0 floor from production spectra.

The scientifically cleaner next test is a preregistered general-accuracy convergence ladder at fixed physics and fixed k sampling. If higher integration accuracy restores the already-frozen `5e-6` GR-limit criterion, a high-precision C5 provider route can be tested prospectively without source patches or special-casing. If it does not, the next audit must target explicit-EFT background/thermal branch semantics.

## Preserved history and gates

- Exp069B remains permanent `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.
- Exp069C remains `RAW_POWER_ZERO_LIMIT_RESIDUAL + KGRID_NONCONVERGENCE`.
- Exp069D remains formally incomplete because the skip-RGR case is unstable.
- C5 physical provider remains **NOT ELIGIBLE**.
- support-validity mask is not authorized.
- G7 = OPEN.
- G8 = OPEN.
- G9 = OPEN.
