# Experiment 025 — nonzero GDM sound-speed response manifold

Date: 2026-08-24
Status: CALIBRATION PASS; geometry audit reproduced
Gate: G3B family-manifold construction / rank interpretation

## Question

After validating the GDM -> CDM zero-closure limit, what does a genuinely nonzero GDM perturbation family look like in the frozen DSIR response basis?

Pinned solver:

`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`

Validated precision preset: `p8`.

Hold

\[
w=0,\qquad c_{vis}^2=0,
\]

and vary only constant rest-frame sound speed

\[
c_s^2=10^{-8},10^{-7},10^{-6},10^{-5},10^{-4}.
\]

Same-solver reference: GDM with `c_s^2=0`.

For each model

\[
\boxed{r_\Delta(k,z;c_s^2)=\ln\frac{P_\Delta(k,z;c_s^2)}{P_\Delta(k,z;0)}}
\]

on frozen nodes

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\ h/{\rm Mpc}.
\]

## Clean-room response amplitudes

Initial run `32741457384` and augmented geometry run `32742672863` completed successfully.

Maximum absolute response over 35 frozen cells:

| cs2 | max |r_Delta| |
|---:|---:|
| 1e-8 | 9.4632e-4 |
| 1e-7 | 9.4656e-3 |
| 1e-6 | 9.4899e-2 |
| 1e-5 | 9.7340e-1 |
| 1e-4 | 6.0298 |

The response is negative and grows rapidly toward high k, as expected for pressure-supported suppression of clustering. Even the weakest scanned deformation is far above the validated zero-limit numerical floor.

## Local tangent behavior

Flatten each response into a 35-vector ordered by explicit redshift headers and frozen k nodes. In the small-deformation regime the expected first-order form is

\[
r_\Delta(k,z;c_s^2)=c_s^2\,t(k,z)+O(c_s^4).
\]

The automated audit uses `c_s^2 <= 1e-6` to estimate the local tangent. Its local sampled linear-span singular-value ratio is

\[
\boxed{\sigma_2/\sigma_1=4.40\times10^{-5}}.
\]

Thus the local family is numerically extremely close to one tangent direction.

At the strong `c_s^2=1e-4` point the response direction rotates by approximately

\[
\boxed{11.3^\circ}
\]

relative to the local tangent. This is measurable manifold curvature.

## Known-physics k^2 positive control

In the local subset the tangent is well described by

\[
\boxed{r_\Delta(k,z)\simeq-c_s^2 A(z)k^2}.
\]

The augmented automated run gives maximum relative L2 residual over redshift

\[
\boxed{2.01\times10^{-3}}.
\]

This is not a new DSIR law. It is a positive control reflecting the pressure-gradient structure of the GDM perturbation equations.

## Critical methodological result: tangent dimension != global SVD span

This scan varies one physical parameter and therefore defines a one-dimensional parametric manifold by construction. Nevertheless, SVD over the entire finite scan gives

\[
\boxed{\sigma_2/\sigma_1\simeq2.50\times10^{-2}}.
\]

The second global linear mode is primarily curvature of a one-parameter response curve, not evidence for a second microscopic degree of freedom.

DSIR therefore keeps three distinct objects:

1. local Jacobian/tangent rank — intrinsic local response dimension;
2. global linear-span rank — number of linear modes needed to approximate a finite curved manifold;
3. curvature diagnostics — rotation/nonlinearity of tangent directions across parameter space.

A future `R_model` result must state which notion is used. Global SVD rank must not be interpreted as a field count.

## Gate result

- response extraction with explicit redshift provenance: PASS;
- nonzero `c_s^2` family construction: PASS as calibration;
- local tangent geometry audit: PASS;
- `k^2` known-physics positive control: PASS;
- hard tangent-domain cutoff: NOT YET DEFINED;
- new-law/discovery claim: NONE.

## Next steps

1. Add independent GDM `c_vis^2` axis.
2. Later add nonzero `w` as a separate axis.
3. Estimate the multi-axis local GDM Jacobian rank rather than inferring dimension from global SVD.
4. If a hard tangent-domain cutoff is needed, pre-freeze a nonlinearity metric and run intermediate `c_s^2` values such as `2e-6,3e-6,5e-6,7e-6`.
