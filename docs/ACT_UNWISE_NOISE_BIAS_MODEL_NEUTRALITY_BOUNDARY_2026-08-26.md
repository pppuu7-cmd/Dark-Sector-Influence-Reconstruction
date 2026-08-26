# ACT × unWISE redshift-PCA noise-bias model-neutrality boundary — 2026-08-26

## Scope

This note records how the released ACT DR6 × unWISE redshift-distribution noise-bias correction interacts with the DSIR linear/no-CLEFT observable bridge. It is a methodological boundary only: no G7/G8/G9 closure, no relation fit, and no change to Exp068A.

Pinned source: `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`.

Published analysis: Farren et al., *The Atacama Cosmology Telescope: Cosmology from Cross-correlations of unWISE Galaxies and ACT DR6 CMB Lensing*, Appendix C.2.

## 1. Physical origin of the correction

The correction is not a CLEFT identity. It is a bias induced by marginalizing over noisy redshift-distribution degrees of freedom after imposing smoothness/positivity. Because the final angular spectra are nonlinear functions of those redshift-distribution variables,

\[
\langle C_\ell(\eta_z)\rangle \neq C_\ell(\langle\eta_z\rangle).
\]

The published construction draws 9000 PCA-coefficient realizations from the redshift-distribution priors at a fiducial cosmology and forms a term-by-term noise-bias correction

\[
\Delta C_\ell^{XY,\,noise}
=\langle C_\ell^{XY}(\eta_z)\rangle-C_\ell^{XY}(\eta_z=0),
\]

then subtracts it from the theory prediction. The released implementation scales the precomputed templates with the relevant galaxy-bias and magnification nuisance parameters.

## 2. What the pinned code does when CLEFT is disabled

`unWISExLensTheory.load_sample_data()` loads the released noise-bias files whenever `use_noise_bias_correction=True`.

If a CLEFT helper exists, corrections are loaded for the full relevant set of basis pieces. If the CLEFT helper is absent, the code explicitly retains nonzero released corrections for

- `gg_bsq`,
- `gmu_b`,
- `kg_b`,

while setting the CLEFT-specific `gg_b` correction slot to zero.

Therefore the upstream **linear/no-CLEFT** semantics still include a redshift-PCA noise-bias correction; simply setting every correction to zero would not reproduce the public wrapper's no-CLEFT behavior.

## 3. Model-neutrality issue

The released correction was precomputed at a fixed fiducial cosmology. Its mathematical origin depends on the response of the projected spectra to redshift-PCA perturbations, so in general

\[
\Delta C_\ell^{noise}
=\Delta C_\ell^{noise}[P_{WW},P_{Wm},P_{mm},H,\chi,\ldots].
\]

For a sufficiently different dark-sector or modified-gravity model, the exact PCA-marginalization bias need not equal the released fiducial-template value.

Consequently DSIR must distinguish two legitimate but different contracts.

### A. Upstream-fidelity linear/no-CLEFT contract

Use the released fixed noise-bias templates exactly as the pinned public wrapper does, with frozen nuisance scaling. This is an **observational-likelihood replication approximation** tied to the published fiducial correction. Any G7 result using it must state that scope explicitly.

### B. Strict model-neutral contract

Recompute the PCA noise-bias correction for each theory response using the same released PCA priors and the validated solver-neutral raw projector:

\[
\Delta C_\ell^{noise}(\pi)
=E_{\eta_z}[C_\ell(\pi,\eta_z)]-C_\ell(\pi,\eta_z=0).
\]

This avoids assuming that a LambdaCDM-fiducial correction is invariant under arbitrary dark-sector/MG changes. It is computationally heavier and needs a separately preregistered convergence rule for the PCA expectation.

## 4. Consequence for the nuisance tangent gate

A future 26D nuisance-tangent/rank experiment must freeze which of these two contracts is used **before** evaluating singular values.

If upstream-fidelity v0.1 is chosen, the released templates and their hashes become part of the survey operator; derivatives with respect to bias/magnification must include their nuisance-dependent scaling exactly as in the pinned code.

If strict model-neutral mode is chosen, the PCA expectation procedure, random/quasi-random design, convergence threshold, and covariance treatment must be frozen before model-family outputs are inspected.

The two modes must never be mixed after seeing G7 performance.

## 5. Recommended DSIR sequencing

For the smallest rigorous first G7 attempt:

1. finish Exp068A raw physical forward reproduction;
2. separately validate raw-to-selected 26D **linear/no-CLEFT upstream-fidelity** nuisance/bandpower closure, including released PCA noise-bias templates and exact shot-noise template;
3. freeze and measure the nuisance tangent rank under the Exp067A whitener;
4. label any resulting G7 v0.1 law as an upstream-fidelity linear/no-CLEFT observational subspace result;
5. later repeat with model-neutral recomputed PCA noise bias as a stronger robustness layer.

No claim in this note closes G7, G8, or G9.
