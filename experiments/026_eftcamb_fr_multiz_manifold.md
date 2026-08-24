# Experiment 026 — H-EFTCAMB designer-f(R) common-baseline multi-z manifold

Date: 2026-08-24
Status: CALIBRATION DEFINED; RUN PENDING
Gate: MG-S1 / G3B family-manifold construction

## Why this experiment is necessary

Experiment 021 closed the H-EFTCAMB designer-f(R) GR limit (MG-S0), but that clean-room gate intentionally used the upstream author `base_params.ini` cosmology. A solver zero-limit test does not by itself guarantee that the nonzero f(R) response used in the six-family atlas is evaluated around the same baseline cosmology as the CLASS-family controls.

For cross-family response geometry, DSIR therefore requires a common baseline before admitting the nonzero C5 manifold.

## Common baseline

The MG-S1 calibration uses

- `h = 0.67` (`hubble = 67` in CAMB),
- `omega_b = 0.0224`,
- `omega_cdm = 0.1200`,
- no massive-neutrino density (`omnuh2=0`),
- `massless_neutrinos = 3.046`,
- `A_s = 2.10e-9`,
- `n_s = 0.965`,
- `YHe = 0.2404`,
- flat geometry,
- linear matter power only.

This matches the working CLASS-family response baseline as closely as the two solver parameter conventions permit. Remaining code/convention differences are handled by same-solver reference quotients rather than by comparing absolute spectra.

## Frozen response grid

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\;h/{\rm Mpc}.
\]

Each redshift is assigned an explicit CAMB matter-power filename (`z1_matterpower.dat`, ..., `z7_matterpower.dat`) so the extractor does not infer redshift order from an implicit solver convention.

## Models

Reference:

`EFTflag=0` GR on the common baseline.

Designer family:

`EFTflag=3`, `DesignerEFTmodel=1`, `EFTwDE=0`, with

\[
B_0=0,10^{-7},10^{-6},10^{-5},10^{-4},10^{-3}.
\]

The nonzero points are all safely above the pinned H-EFTCAMB

`EFTCAMB_GR_threshold=1e-8`.

`B0=1e-2` is deliberately excluded from the first production-oriented manifold calibration because the z=0 calibration already shows a very strong response; it can be added later as a strong-deformation stress point rather than allowing it to dominate the first family geometry.

## Response

For every B0:

\[
\boxed{r_\Delta(k,z;B_0)=\ln\frac{P_{f(R)}(k,z;B_0)}{P_{GR}(k,z)}}.
\]

The same pinned H-EFTCAMB solver, common baseline and numerical settings are used in numerator and denominator.

## Stability rule

Every designer run must contain the upstream marker

`EFTCAMB: theory stable`.

A missing stability marker is a failed model instance, not a zero response and not a reason for imputation.

## Common-baseline exact-zero diagnostic

This first multi-z run includes exact `B0=0` and reports

\[
\max_{z,k}|r_\Delta(B_0=0)|.
\]

The z=0 MG-S0 hard threshold `2e-6` is **not automatically promoted to a seven-redshift hard threshold**. This first common-baseline multi-z result is calibration only. If the exact-zero residual is stable and small across all 35 cells, DSIR will freeze a separate multi-z threshold before a fresh rerun.

## Manifold-rank interpretation

The B0 scan is one-parameter by construction. A finite curved response curve can have more than one nonzero global SVD singular value. The workflow records the global linear-span spectrum for compression diagnostics, but this is not called an intrinsic degree-of-freedom count.

The same tangent-versus-global-span distinction discovered in Experiment 025 applies here.

## Next step after first run

1. Inspect exact-zero residual over all 35 cells and stability logs.
2. Inspect monotonicity and curvature of the B0 response surface.
3. Freeze a multi-z zero-limit hard threshold before a fresh rerun if calibration supports it.
4. Promote stable nonzero points to C5 atlas instances with full provenance.
5. Compare full H-EFTCAMB response to the old BZ-like toy only on the QS-safe `k={0.01,0.03,0.1}` subset.
6. Never use the BZ toy to fill low-k cells.
