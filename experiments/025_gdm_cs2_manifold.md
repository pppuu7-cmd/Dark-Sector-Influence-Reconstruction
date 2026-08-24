# Experiment 025 — nonzero GDM sound-speed response manifold

Date: 2026-08-24
Status: CALIBRATION; geometry rerun in progress
Gate: G3B family-manifold construction / rank interpretation

## Question

After validating the GDM -> CDM zero-closure limit, what does a genuinely nonzero GDM perturbation family look like in the frozen DSIR response basis?

Use the pinned solver

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`

with the already validated p8 precision preset. Hold

\[
w=0,\qquad c_{vis}^2=0,
\]

and vary only a constant rest-frame sound speed across all GDM time bins:

\[
c_s^2=10^{-8},10^{-7},10^{-6},10^{-5},10^{-4}.
\]

The same-solver reference is the zero-closure GDM model `c_s^2=0`, not an absolute spectrum from another solver.

For each model compute

\[
\boxed{r_\Delta(k,z;c_s^2)=\ln\frac{P_\Delta(k,z;c_s^2)}{P_\Delta(k,z;0)}}
\]

on the frozen nodes

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\ h/{\rm Mpc}.
\]

This first scan is calibration only: no hard tolerance and no rank/discovery claim is imposed.

## First clean-room result

GitHub Actions run `32741457384` completed successfully. Maximum absolute response over the 35 frozen z x k cells:

| cs2 | max |r_Delta| |
|---:|---:|
| 1e-8 | 9.4632e-4 |
| 1e-7 | 9.4656e-3 |
| 1e-6 | 9.4899e-2 |
| 1e-5 | 9.7340e-1 |
| 1e-4 | 6.0298 |

The response is negative and grows rapidly toward high k, as expected for pressure-supported suppression of clustering.

For example at `z=0.295`, `k=0.1 h/Mpc`:

\[
r_\Delta\approx
-9.46\times10^{-4},
-9.47\times10^{-3},
-9.49\times10^{-2},
-9.73\times10^{-1},
-5.77
\]

for increasing `c_s^2` from `1e-8` to `1e-4`.

The weakest scanned deformation is already much larger than the validated zero-limit numerical floor, so the observed local trend is not being inferred from solver noise.

## Local tangent behavior

Flatten each model response into a 35-component vector `r(cs2)` ordered by explicit redshift headers and frozen k nodes.

For very small sound speed the perturbation equations contain the pressure-gradient scale `c_s^2 k^2`, so the expected first-order response is

\[
r_\Delta(k,z;c_s^2)=c_s^2\,t(k,z)+O(c_s^4),
\]

with a one-dimensional local tangent vector `t`.

Using the first clean-room artifact, scaled responses `r/c_s^2` are extremely stable near the origin. Relative L2 change with respect to the `1e-8` scaled response is approximately:

| cs2 | relative change of r/cs2 |
|---:|---:|
| 1e-7 | 2.11e-4 |
| 1e-6 | 2.33e-3 |
| 1e-5 | 2.36e-2 |
| 1e-4 | 2.59e-1 |

Direction cosine with the weakest-deformation response remains nearly unity through `1e-5`; corresponding direction angles are approximately

- `1e-7`: `0.0025 deg`
- `1e-6`: `0.0279 deg`
- `1e-5`: `0.276 deg`
- `1e-4`: `11.29 deg`

Thus the family is locally almost a straight one-dimensional tangent direction, but the strong `1e-4` point exhibits visible curvature in response space.

## Known-physics k^2 positive control

In the local subset `c_s^2 <= 1e-6`, the tangent is well described by

\[
\boxed{r_\Delta(k,z)\simeq-c_s^2\,A(z)\,k^2}
\]

on the frozen k nodes. A least-squares `k^2` factorization of the local tangent has only about `0.2%` relative L2 residual per redshift in the first artifact.

This is **not a new DSIR law**. It is a positive control reflecting the familiar pressure-gradient structure of the GDM perturbation equations.

## Critical methodological result: tangent dimension != global SVD span

This scan has one varied physical parameter, so its parametric manifold dimension is one by construction. However a curved one-dimensional manifold can require more than one linear singular vector to represent globally.

For the first artifact, SVD of all five 35-dimensional response vectors gives approximately

\[
\sigma_2/\sigma_1\simeq2.50\times10^{-2},
\]

while the second-mode variance fraction is about

\[
6.24\times10^{-4}.
\]

That second global linear-span mode is primarily curvature of the one-parameter response curve, **not evidence for a second microscopic GDM degree of freedom**.

Therefore DSIR must separate:

1. **local tangent/Jacobian rank** — intrinsic local response dimension;
2. **global linear-span rank** — number of linear modes needed to approximate a finite curved manifold;
3. **curvature diagnostics** — how rapidly tangent directions rotate with parameter displacement.

A future `R_model(pi)` result must specify which notion is being reported. Global SVD rank must not be casually called the number of independent dark-sector degrees of freedom.

## Automated geometry rerun

The workflow now records redshift directly from each CLASS output header and runs `ci/gdm_manifold_geometry.py`, which reports:

- local tangent estimate from `c_s^2 <= 1e-6`;
- angle and nonlinearity of every response vector relative to that tangent;
- local and global linear-span singular spectra;
- the known-physics `k^2` tangent residual;
- an explicit warning that global span rank is not intrinsic dimension.

No PASS boundary for "linear enough" is frozen from this first scan. If DSIR later needs a tangent-domain cutoff, a tolerance must be stated before a separate refinement run with intermediate `c_s^2` values.

## Next steps

1. Rerun the augmented artifact with explicit redshift provenance and automated geometry metrics.
2. Retain `c_s^2 <= 1e-6` as a provisional local-tangent calibration subset only, not yet a hard physical boundary.
3. If a hard tangent-domain boundary is needed, pre-freeze a nonlinearity metric and run intermediate values such as `2e-6,3e-6,5e-6,7e-6`.
4. Add independent GDM axes (`c_vis^2`, and later nonzero `w`) separately before estimating the full GDM family Jacobian rank.
5. Do not use the one-axis global SVD second mode as evidence for a second field/degree of freedom.
