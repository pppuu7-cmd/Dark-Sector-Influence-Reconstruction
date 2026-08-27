# Exp072A pre-output implementation audit — 2026-08-27

**Status:** PRE-OUTPUT STATIC/METHODOLOGICAL AUDIT. No Exp072A leakage fractions, mask cardinalities, covariance, nuisance SVD/rank, G7 relation/null, G8 response, or article-selection quantity were inspected in preparing this note.

## Audit target

Implementation under review:

- PR #104, head `553f6867f1cf71d4661a9f7b1f739a970648d05d`;
- `ci/act_unwise_angular_support_leakage_mask_v0_1.py`;
- workflow `ACT x unWISE angular support leakage mask v0.1`.

Frozen scientific contracts already merged on `main` before this audit:

- `experiments/072a_act_unwise_angular_support_leakage_mask_prereg_v0_1.md`;
- `experiments/072a_act_unwise_angular_support_leakage_execution_binding_v0_1.md`.

At the time of this audit the first PR workflow had not reached the scientific evaluation step; it was still in external archive acquisition. Therefore this note is not output-conditioned.

## 1. Upstream observational operator semantics

Pinned upstream source:

`ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`.

The pinned likelihood constructs ACT Blue/Green NaMaster operators with:

- transfer column 1 for `Clgg`;
- transfer column 2 for `Clkg`;
- `hp.pixwin(2048)^2` multiplying raw `Clgg` before bandpower reduction;
- `hp.pixwin(2048)` multiplying raw `Clkg` before bandpower reduction.

The pinned `NaMasterPowerSpectrumBinning` signal-only algebra is

`D = bandwindow @ inv(coupling)`

and

`D @ (coupling @ C_ell) = bandwindow @ C_ell`,

followed by the released per-band transfer factor. Thus for the signal component the frozen Exp072A effective operator

`transfer_b * bandwindow[b,ell] * pixel_window_ell`

is consistent with the pinned upstream likelihood and does not require a separate coupling-matrix inversion in the leakage statistic.

The PR #104 implementation binds exactly these transfer columns and pixel-window powers, verifies the released coupling/bandwindow matrix dimensions, and applies the absolute value only after assembling the released signal operator weight as required by the frozen positive-support statistic.

## 2. Limber coordinate and quadrature semantics

The implementation reuses the already validated DSIR no-CLEFT geometry helpers and freezes

`k=(ell+1/2)/f_K(chi)`

on the same `N=96` Gauss-Legendre nodes and `ell=0,...,6143` domain used by Exp068B.

Its common positive quadrature factor is

`q_i = w_i * (Delta chi/2) / f_K(chi_i)^2`.

This matches the raw no-CLEFT projection measure: the provider spectra in `src/dsir/act_unwise_projection.py` are divided by `f_K^2`, while the Gauss-Legendre integration contributes `w_i Delta chi/2`.

No model power amplitude enters Exp072A.

## 3. Nuisance-independent kernel-envelope transcription

For `Clkg`, PR #104 uses:

- `Wm`: `abs(kappa) * sum_col(abs(bdndz_h_col)) * q`;
- `WW`: `abs(kappa*mu) * q`.

For `Clgg`, it uses:

- `mm`: `sum_col(abs(bdndz_h_col))^2 * q`;
- `Wm`: `2*abs(mu)*sum_col(abs(bdndz_h_col))*q`;
- `WW`: `abs(mu)^2*q`.

The `mm` expression is algebraically equal to the frozen ordered-pair sum

`sum_{a,b} |bd_a bd_b| = (sum_a |bd_a|)^2`.

The factor of two in the `Wm` `Clgg` block is retained. Algebraically zero no-CLEFT/CLEFT slots are not assigned artificial support weight.

This is therefore a nuisance-envelope geometry statistic, not a fitted-nuisance response statistic.

## 4. Frozen support binding

PR #104 hard-binds the immutable Exp071A PASS record:

- run `33027562195`;
- artifact `9629064009`;
- digest `sha256:4955a3a917992ad38423d9fe2dda3682822c7b86614950467faf5a46a7426675`;
- classification `PASS_COMMON_PHYSICAL_SUPPORT_MASK_V0_1`;
- retained provider cells `495`;
- five common redshift nodes;
- 33 common physical k nodes.

Nominal support `V0` and tightened support `V1` are literal closed coordinate envelopes from the frozen preregistration. The implementation does not interpolate `P_mm`, `P_Wm`, or `P_WW` amplitudes.

## 5. Leakage-ratio algebra audit

For each block, the implementation computes

`den = sum_i K_i * sum_ell |O_bell|`

and

`num(V) = sum_i K_i * sum_ell |O_bell| * 1[(z_i,k_iell) notin V]`,

where `K_i >= 0` is the block-specific positive survey-kernel envelope and

`|O_bell| = |bandwindow[b,ell] * transfer_b * pixel_window_ell|`.

Summing numerator and denominator over the active physical blocks gives exactly the preregistered

`L_j(V)=sum w_j 1[invalid]/sum w_j`.

The released transfer coefficient is constant over raw multipoles for a fixed bandpower row and therefore mathematically cancels from the ratio when nonzero, but retaining it in the implementation preserves the exact upstream operator binding and allows zero/non-finite operator failures to be diagnosed.

## 6. Scale-cut and ordering audit

The implementation freezes the 26 Exp065B coordinates:

- 6 Blue `Clgg`;
- 7 Blue `Clkg`;
- 6 Green `Clgg`;
- 7 Green `Clkg`;

with the already-certified scale cuts `Clgg [100,402]` and `Clkg [51,402]` and exact expected midpoints. It does not select rows by leakage before constructing the candidate list.

## 7. Downstream-isolation audit

Static inspection finds no covariance matrix load, Cholesky factorization, nuisance Jacobian/SVD/rank calculation, G7 relation/null statistic, G8 family response, or article-selection quantity in the Exp072A evaluator.

The evaluator records explicit false controls for these forbidden reads, and the workflow asserts them after evaluation.

## 8. Scientific criteria preservation

PR #104 preserves the already-frozen:

- invalid-support threshold `0.05`;
- exactly 26 candidates;
- nominal minimum retained dimension `15`;
- per-sample/channel survival requirements;
- `V1` monotonicity/subset robustness control;
- scientific FAIL as a normal immutable output rather than CI/infrastructure failure.

No threshold, support envelope, candidate coordinate, or acceptance criterion is modified by this audit.

## Audit conclusion

**PREOUTPUT_IMPLEMENTATION_AUDIT_PASS** for consistency of PR #104 with the already-frozen Exp072A operator/support contract.

This is not an Exp072A scientific PASS. The first complete frozen leakage evaluation may still return either scientific PASS or scientific FAIL. G7/G8/G9 remain OPEN.
