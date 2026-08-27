# Exp072A — ACT×unWISE angular support/leakage execution binding v0.1

**Date frozen:** 2026-08-27  
**Status:** PROSPECTIVE EXECUTION BINDING; NO Exp072A LEAKAGE FRACTION HAS BEEN EVALUATED

This file resolves exact upstream-observational operator details that were not numerically explicit in `experiments/072a_act_unwise_angular_support_leakage_mask_prereg_v0_1.md`. It does not alter the frozen 5% leakage threshold, support envelopes, 26 candidate coordinates, retained-dimension requirement, family set, or PASS/FAIL semantics.

## Exact upstream signal operator

The pinned likelihood source `unWISExLens_lklh/unWISExLensLklh.py` at commit `6302c30d9e70f8e4ff2d4a84a9977b4471705179` constructs, for ACT XCorr:

- `NaMasterPowerSpectrumBinning(..., transfer_function=transfer_function[:,1])` for `Clgg`;
- `NaMasterPowerSpectrumBinning(..., transfer_function=transfer_function[:,2])` for `Clkg`;
- `_pixwin_correction_gg = hp.pixwin(2048)**2`;
- `_pixwin_correction_kg = hp.pixwin(2048)`;
- `want_lensing_lklh_correction: False` in the inherited defaults.

Before binning, the upstream signal is multiplied by the appropriate HEALPix pixel-window correction. Therefore the Exp072A positive bandpower operator factor is frozen as

`abs( bandwindow[b,ell] * transfer[b] * pixwin_channel[ell] )`,

where

- `pixwin_gg[ell] = healpy.pixwin(2048)[ell]**2`;
- `pixwin_kg[ell] = healpy.pixwin(2048)[ell]`.

This factor replaces the shorter notation `abs(transfer_b * bandwindow[b,ell])` in the preregistration only by making explicit an upstream multiplicative factor that was already part of the pinned ACT likelihood operator. No Exp072A output has been inspected in making this clarification.

## Bandwindow semantics

For each sample load the released object selected by pinned `binning_setup.yaml` and use:

- `obj['gg']['bandwindow']` for `Clgg`;
- `obj['kg']['bandwindow']` for `Clkg`.

The signal-only identity already validated in DSIR remains binding: the upstream NaMaster path reduces to released bandwindow acting on the pixel-windowed raw signal, followed by the released transfer function. Coupling matrices are loaded only for provenance/shape checks and are not inverted for the positive support statistic.

The bandwindow column coordinate is the exact integer input multipole returned by the pinned NaMaster operator, starting at ell=0. The evaluator must require that the released bandwindow column count covers the full frozen raw `ell=0,...,6143` domain used by Exp072A; if it does not, this is a scientific/operator-contract FAIL, not a reason to truncate the frozen raw domain after inspection.

## Transfer rows and selected coordinates

The first transfer-file column is the released bandpower ell coordinate, the second is `Clgg` transfer and the third is `Clkg` transfer, exactly as bound by pinned upstream source.

Candidate selection must be recomputed from pinned `ell_bin_edges`, the transfer row count, and the frozen official cuts:

- `Clgg: [100,402]` using `(100 <= edge_left) & (edge_right < 402)`;
- `Clkg: [51,402]` using `(51 <= edge_left) & (edge_right < 402)`.

The resulting midpoint lists must match the preregistered 6/7 values exactly to absolute `1e-10`; otherwise A3 fails.

## Positive raw survey-kernel envelope

Use the same 96 Gauss-Legendre chi nodes and the same literal Blue/Green tracer objects as Exp068B.

At each node define the kernel envelopes exactly as follows, before any bandwindow action:

### `Clkg`

`K_Wm(i) = abs(kappa_kernel(i)) * sum_c abs(bdndz_h(i,c))`

`K_WW(i) = abs(kappa_kernel(i) * mu_kernel(i))`

### `Clgg`

`K_mm(i) = (sum_c abs(bdndz_h(i,c)))**2`

This is exactly the sum over all ordered column pairs of `abs(bdndz_h_a*bdndz_h_b)`.

`K_Wm(i) = 2 * abs(mu_kernel(i)) * sum_c abs(bdndz_h(i,c))`

`K_WW(i) = abs(mu_kernel(i))**2`

All are multiplied by the positive Gauss-Legendre weight and `Delta chi/2`. The common `1/f_K(chi)^2` projection factor is also frozen into every block envelope because it is part of the raw Limber operator and varies with redshift:

`K_block(i) <- K_block(i) / f_K(chi_i)^2`.

No model power amplitude is used. The `1/f_K^2` factor is geometry, not a theory-family response.

For every `(i,ell)` use `k=(ell+0.5)/f_K(chi_i)` and test nominal/tightened support exactly as preregistered.

## Source/provenance controls

The evaluator must verify from the pinned source text before computing leakages that all of these literal contracts are present:

1. transfer column 1 is used for gg;
2. transfer column 2 is used for kg;
3. `hp.pixwin(... )**2` is used for gg;
4. single `hp.pixwin(...)` is used for kg;
5. XCorrACT has `include_lensing_auto_spectrum: False`;
6. inherited `want_lensing_lklh_correction: False`;
7. scale-cut conditions use the pinned left-inclusive/right-strict inequalities.

Any failure enters A1/A3 and produces the frozen scientific FAIL label if the evaluation otherwise completes.

## No retuning

After the first Exp072A leakage output, do not change:

- pixel-window inclusion;
- `1/f_K^2` inclusion;
- absolute bandwindow weighting;
- full literal mean+PCA nuisance-envelope sum;
- support envelopes `V0/V1`;
- threshold 0.05;
- minimum retained dimension 15;
- per-sample/per-channel coverage requirement;
- 26-coordinate order;
- PASS/FAIL labels.

Infrastructure repair is allowed only if all of these scientific rules remain identical.

G7/G8/G9 remain OPEN.
