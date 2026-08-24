# Experiment 034 — DESI ShapeFit shape-block observational whitening v0.1

**Date:** 2026-08-24  
**Status before hard run:** method and acceptance rules frozen; numerical result pending CI.  
**Scope:** first partial observation-space bridge for the frozen six-direction DSIR low-k atlas. This is **not** a full DESI likelihood projection and does not close G5.

## 1. Scientific question

The raw DSIR comparison uses theory responses

\[
r_\Delta(k,z)=\ln\frac{P_{\Delta,\mathrm{model}}(k,z)}{P_{\Delta,\mathrm{ref}}(k,z)}.
\]

Raw theory-space angles are not observational significance. The next required layer is an observation operator followed by covariance whitening,

\[
Z=C^{-1/2}\,\Delta O.
\]

For the first controlled step we use only the corrected DESI DR1 ShapeFit `m+n` channel, because that channel has a direct local-shape relation to a log-power response while the current frozen atlas does not yet provide family-complete predictions for all four ShapeFit coordinates.

## 2. Shape proxy operator

Use the ShapeFit deformation basis

\[
\delta\ln P(k)=A+\frac{m}{a}\tanh\!\left[a\ln\frac{k}{k_p}\right]
+n\ln\frac{k}{k_p},
\]

with

\[
a=0.6,\qquad k_p=0.03\;h\,\mathrm{Mpc}^{-1}.
\]

At the pivot the logarithmic slope perturbation is `m+n`. On the five frozen DSIR nodes

`k={0.001,0.003,0.01,0.03,0.1} h/Mpc`,

fit each theory response row to the three columns

\[
1,\quad \frac{1}{a}\tanh[a\ln(k/k_p)],\quad \ln(k/k_p),
\]

and define

\[
K_{\rm shape}[r_\Delta](z)\equiv \widehat m(z)+\widehat n(z).
\]

For a deformation exactly in the ShapeFit span this operator must recover `m+n` to floating-point accuracy. For a generic theory response this is explicitly a **finite-node proxy** for the ShapeFit compression, not a replacement for the DESI survey window and full likelihood kernel. Therefore the fit residual is reported for every family/redshift.

The projected history is linearly interpolated from the frozen DSIR redshift grid to the informative DESI ShapeFit bins

`LRG1, LRG2, LRG3, ELG2, QSO`.

BGS is not needed for this first cross-family shape-history gate.

## 3. Conservative covariance rule

The corrected erratum covariance is four-dimensional in

`[DV/rd, DH/DM, f_sigma_s8, m+n]`.

The current frozen DSIR atlas does **not** yet predict the other three observables for every family. Applying the full inverse covariance while inserting zero responses in those unpredicted channels would create a false assumption and potentially artificial significance.

Therefore the production whitening used here is only

\[
Z_i^{\rm shape}=\frac{\Delta(m+n)_i}{\sqrt{C_{ii}^{m+n,m+n}}},
\]

using the marginal `m+n` variance separately in each informative redshift bin.

The Schur-complement conditional error

\[
\sigma^2_{m+n\mid\mathrm{others}}
=C_{ss}-C_{sN}C_{NN}^{-1}C_{Ns}
\]

is computed only as a diagnostic of how much information could become available after family-complete predictions for the other channels exist. It is **not** used as evidence in Experiment 034.

## 4. Frozen acceptance rules before first hard run

Experiment 034 passes its method gate only if all of the following hold:

1. A synthetic exact ShapeFit deformation with coefficients `A=0.13, m=0.20, n=-0.03` recovers `m+n=0.17` with absolute error `<1e-12`.
2. Every selected DESI covariance matrix is symmetric positive definite.
3. Every projected theory direction is finite and nonzero on the five-bin shape block.
4. No pairwise scientific angle threshold is introduced after seeing the result.
5. Any singular spectrum is descriptive only; no intrinsic-rank threshold or `R_model` value is inferred from this experiment.

## 5. Outputs

The hard run must report:

- marginal and conditional `m+n` errors;
- per-family projected `m+n(z)` proxy histories;
- projection residuals relative to the finite-node ShapeFit basis;
- raw and marginally-whitened oriented/unoriented pairwise angles;
- a descriptive singular spectrum of unit whitened directions;
- explicit limitations and the next required observation-operator layer.

## 6. Interpretation boundary

A PASS means only:

`PASS_PROXY_OBSERVATIONAL_WHITENING_SHAPE_BLOCK`.

It does **not** mean:

- G5 is closed;
- a family pair is globally observationally distinguishable;
- the full ShapeFit likelihood has been reproduced;
- an intrinsic dark-sector rank has been measured;
- G7 or G8 has passed;
- a new law or discovery has been found.

## 7. Next hard requirement

Build family-complete operators for at least `DH/DM` (or equivalent AP geometry) and `f_sigma_s8`, then validate a survey/window-aware shape map. Only then is it legitimate to use the full corrected ShapeFit covariance for a joint cross-family observational geometry.
