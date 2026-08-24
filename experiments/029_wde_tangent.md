# Experiment 029 — smooth-w dark-energy local tangent

Date: 2026-08-24
Status: CALIBRATION DEFINED; RUN PENDING
Gate: comparison-readiness / C1 local response patch

## Purpose

The existing cross-solver bridge uses a finite smooth-w deformation `w=-0.9`. That is excellent for solver-response validation, but it is not methodologically homogeneous with the local tangent/cone directions already extracted for IDE, GDM and designer f(R). Before cross-family local comparison, DSIR therefore calibrates a one-sided non-phantom tangent at the LambdaCDM boundary.

Define

\[
\epsilon_w=1+w>0.
\]

Use `epsilon_w={1e-4,1e-3,1e-2}`, with `wa=0` and `cs2=1`, relative to a same-solver LambdaCDM reference in pinned GDM_CLASS at the validated p8 precision.

The response coordinate is

\[
r_\Delta(k,z;\epsilon_w)=\ln\frac{P_{w}(k,z)}{P_{\Lambda CDM}(k,z)}.
\]

The comparison tangent is the smallest-step one-sided estimate

\[
t_w \approx r_\Delta(10^{-4})/10^{-4}.
\]

Larger steps are retained only as finite-difference convergence/curvature diagnostics. No intrinsic-rank or discovery claim is made in this run.

Frozen response nodes are the standard DSIR 7 redshifts and 5 linear-core k values from response basis v0.1.1.
