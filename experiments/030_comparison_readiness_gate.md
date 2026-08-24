# Experiment 030 — block-aware cross-family comparison readiness

Date: 2026-08-24
Status: **PASS — READY FOR BLOCK-AWARE MODEL COMPARISON**

## Question

Has DSIR reached the point where model-family response objects can be compared without mixing solver artifacts, invalid parameter directions, missing channels, or incompatible scale domains?

This gate does **not** rank models and does not search for a new law. It only determines whether the framework is ready to begin systematic model comparison.

## Low-k common block

Use the frozen response basis v0.1.1 grid

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\qquad
k=\{0.001,0.003,0.01,0.03,0.1\}\,h/{\rm Mpc}.
\]

The first aggregate contains:

- C1 smooth non-phantom DE: one-sided local ray in `epsilon_w=1+w>0`;
- C2 IDE: physical negative-alpha cone ray plus two-sided beta tangent line;
- C3 GDM: positive `cs2` and `cv2` local rays;
- C5 designer f(R): minimum resolved production ray `B0=1e-6` after subtracting the exact-zero response floor.

C0 LambdaCDM is the common reference origin and therefore is not represented by a nonzero tangent vector.

## Tangent-cone geometry rule

A one-sided physical parameter is an oriented **ray**. A genuinely two-sided perturbation is an unoriented **line**.

For ray-ray comparisons retain the signed orientation:

\[
\theta=\arccos(\hat u\cdot\hat v),\qquad 0\le\theta\le180^\circ.
\]

If either object is a two-sided line, its sign is conventional and the comparison uses

\[
\theta=\arccos|\hat u\cdot\hat v|,\qquad 0\le\theta\le90^\circ.
\]

## WDM block contract

Thermal WDM is **not** imputed into the common low-k block. Experiment 024 established that a 3 keV thermal WDM control is nearly invisible at `k=0.1 h/Mpc` but strongly suppresses the linear transfer function by `k=10 h/Mpc`.

The readiness gate therefore checks WDM as a separate small-scale transfer block. A low-k null is a domain/identifiability statement, not a zero physical response.

## Thresholds frozen before first aggregate run

1. exactly six nonzero low-k response objects must be present;
2. every vector must be finite and nonzero on the common 35-cell grid;
3. GDM `cs2`/`cv2` angle <= 1 degree;
4. IDE alpha/beta structure angle >= 30 degrees;
5. 3 keV WDM must satisfy `|r_T(0.1)| <= 1e-4` and `|r_T(10)| >= 0.05`;
6. the C1 smallest-step response must remain numerically resolved;
7. C5 must be a resolved production ray at `B0>=1e-6`, not the `1e-7` transition control.

## Hard result

GitHub Actions run `32772758188` completed successfully on commit `5a0893abef9f492677df01399a6339c10257c158`.

The machine result returned

`status = PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON`,

with `failures=[]`.

Positive controls reproduced:

- GDM `cs2`/`cv2`: `0.322616 deg`;
- IDE alpha/beta structure: `58.933798 deg`;
- WDM 3 keV: `r_T(0.1)=-3.46e-6`, `r_T(10)=-0.10375`.

The normalized six-direction descriptive singular spectrum was

\[
\sigma_i/\sigma_1 =
(1,0.52046,0.26140,0.20087,0.08299,5.9178\times10^{-4}).
\]

This spectrum is descriptive only. No intrinsic-rank threshold was frozen, and it must **not** be reported as `R_model=5`.

Artifact digest: `sha256:f110de1071cb11ce7e927b403f92002c766b03e384715ddd435af2c1c67c4131`.

## Meaning of PASS

DSIR is now ready to begin **block-aware model comparisons** in response space. This does not mean the models have been statistically ranked, that observational covariance has been applied to every theory channel, or that a new dark-sector law has been found. Raw theory-response geometry and later data-whitened geometry remain separate layers.
