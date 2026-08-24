# Experiment 039 — ShapeFit growth-operator contract v0.1

**Date:** 2026-08-25  
**Status:** analytic/operator contract defined; family-level numerical audit pending  
**Gate role:** prerequisite for family-complete corrected-ShapeFit growth whitening

## Why this contract is necessary

The corrected DESI ShapeFit data vector labels its growth coordinate as `f_sigma_s8`. It must **not** be interpreted as a naive textbook `f sigma_8` for arbitrary DSIR models.

ShapeFit defines

\[
s\equiv r_d/r_d^{ref},
\]

and

\[
\boxed{\sigma_{s8}\equiv \sigma(R=s\,8h^{-1}{\rm Mpc})}.
\]

The original ShapeFit derivation explicitly states that the classic fixed-template RSD analysis measures `f sigma_s8`, not an amplitude smoothed at an absolute fixed `8 h^-1 Mpc` scale. It also introduces the no-wiggle pivot amplitude

\[
A_{sp}=s^{-3}P^{lin}_{nw}(k_p/s),
\]

and relates the reported growth amplitude to `f A_sp^{1/2}` by a reference-template normalization.

Primary reference: Brieden, Gil-Marin & Verde, *ShapeFit: extracting the power spectrum shape information in galaxy surveys beyond BAO and RSD*, arXiv:2106.07641, especially Eqs. (3.5)-(3.6), (3.11)-(3.12) and the surrounding interpretation.

Therefore a DSIR prediction must explicitly track the sound-horizon rescaling and the ShapeFit amplitude convention.

## Additional DSIR problem: scale-dependent growth

Several frozen DSIR families have scale-dependent perturbation responses. In that case the standard RSD template assumption

\[
\Theta(k,z)=f(z)\,\delta(k,z)
\]

with one scale-independent growth rate can fail even in linear theory. Here use the dimensionless velocity-divergence convention `Theta` for which the GR pressureless growing mode has `Theta=f delta`; the exact solver sign/normalization must be fixed before numerical use.

A single compressed `f sigma_s8` coordinate is then not automatically a model-independent observation operator.

## Representability moments

For a chosen tracer-relevant density/velocity pair and smoothing radius

\[
R=s\,8h^{-1}{\rm Mpc},
\]

define weighted linear moments

\[
S_{\delta\delta}(R)=\int d\ln k\;\Delta^2_{\delta\delta}(k)W_{TH}^2(kR),
\]

\[
S_{\delta\Theta}(R)=\int d\ln k\;\Delta^2_{\delta\Theta}(k)W_{TH}^2(kR),
\]

\[
S_{\Theta\Theta}(R)=\int d\ln k\;\Delta^2_{\Theta\Theta}(k)W_{TH}^2(kR).
\]

For exactly scale-independent linear growth, `Theta=f delta`, so

\[
\frac{S_{\delta\Theta}}{\sqrt{S_{\delta\delta}}}
=\sqrt{S_{\Theta\Theta}}
=f\,\sigma_{s8}.
\]

This motivates two generalized amplitudes

\[
g_{cross}=\frac{S_{\delta\Theta}}{\sqrt{S_{\delta\delta}}},
\qquad
 g_{auto}=\sqrt{S_{\Theta\Theta}},
\]

which coincide only when the one-parameter RSD amplitude is representable over the weighted k-range.

## RSD representability defect

Define

\[
\boxed{\mathcal D_{RSD}
=1-\frac{S_{\delta\Theta}^2}
{S_{\delta\delta}S_{\Theta\Theta}}}.
\]

By Cauchy-Schwarz, for a positive covariance measure,

\[
0\le \mathcal D_{RSD}\le1.
\]

`D_RSD=0` when the velocity-divergence field is proportional to the density field in the weighted response space. A nonzero value quantifies the failure of one scalar growth amplitude to describe both density-velocity and velocity-velocity RSD contributions.

For deterministic `Theta=f(k) delta`, `D_RSD` is also sensitive to variation of `f(k)` across the weighted k-range: it need not vanish merely because density and velocity are perfectly phase-correlated at each individual k.

This diagnostic is a **compression-validity test**, not a new dark-sector law.

## Required tracer/gauge contract before production

Do not yet compute `D_RSD` from an arbitrary total-matter variable. For each family the numerical implementation must specify:

1. the density field entering the RSD template;
2. the physical velocity-divergence field followed by galaxy tracers;
3. gauge/sign/normalization conventions;
4. whether dark-sector momentum exchange can generate tracer velocity bias;
5. the sound horizon `r_d` and thus `s`;
6. the k/window weighting relevant to the actual ShapeFit compression.

The already validated total-matter comoving `Delta_m` remains the production structure-response variable, but that does **not** by itself prove it is the correct velocity-tracer variable for RSD.

## Production decision tree

For each family/direction:

1. compute the exact ShapeFit smoothing scale `R=s*8 h^-1 Mpc`;
2. construct matched density/velocity transfer responses from the validated solver lineage;
3. evaluate `D_RSD` with a pre-frozen numerical tolerance;
4. if `D_RSD` is negligible and the ShapeFit amplitude bridge is accurate, admit a scalar `f sigma_s8` prediction;
5. if not, keep the growth cell masked for scalar compression and move to a survey/window-aware anisotropic RSD forward operator rather than forcing a number into `f sigma_s8`.

## Connection to Experiment 034

Experiment 034 already showed an analogous compression problem for shape: the finite-node `m+n` basis leaves about 36% residual for GDM/f(R). Experiment 039 imposes the corresponding guardrail on the growth coordinate before full covariance whitening.

The general lesson is methodological:

> compressed observables are valid DSIR coordinates only where the model response is representable by the assumptions of the compression.

## Claim boundary

This contract does not yet show that any frozen family has nonzero `D_RSD`; that is the next numerical test. It does not close G5, does not define intrinsic rank, and does not advance G7/G8.
