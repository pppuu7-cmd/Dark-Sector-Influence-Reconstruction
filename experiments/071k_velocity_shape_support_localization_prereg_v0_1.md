# Exp071K — velocity-shape support localization v0.1

**Preregistered:** 2026-08-28, after terminal Exp071J and before any Exp071K ablation angle is calculated.

## Motivation

Exp071J showed that K2 bar1 remains strongly separated from both tested GDM axes after removing the entire scale-independent constant-in-k mode independently at every redshift:

- K2 vs GDM cs2 shape: `166.4386944060 deg`;
- K2 vs GDM cv2 shape: `164.9270967302 deg`.

Exp071K asks whether this result is broadly supported on the frozen `(z,k)` domain or is carried by a single k node or redshift slice.

No new solver run, new model parameter, new channel, fitted weight, covariance, survey window or nuisance model is allowed.

## Immutable parent

Use only the Exp071I immutable velocity artifact that underlies Exp071J:

- run `33181895623`
- artifact `9690064470`
- artifact SHA256 `ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14`

The evaluator must reconstruct the Exp071J full-support primary projected angles from the parent transfer files and reproduce them to `1e-8 deg` before any ablation is scored.

Frozen grids:

- `z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`
- `k = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`

Raw response and tangent normalizations are inherited unchanged from Exp071I/Exp071J.

## Frozen full-support projection

For a tangent matrix `R(z,k)`:

`R_shape(z,k) = R(z,k) - mean_k R(z,k)`.

Equal weights are used over the currently retained k nodes.

Primary K2 point remains **bar1**.

The directional separator remains the inherited **45 degrees**.

## Primary ablation family A — leave one k node out

For each of the five frozen k nodes, remove that k column from K2 bar1, GDM cs2 and GDM cv2 raw tangent matrices.

On the remaining four k nodes independently at every redshift, recompute the quotient:

`R_shape_LOk(z,k_remaining) = R(z,k_remaining) - mean_{k_remaining} R(z,k_remaining)`.

Then compute oriented Euclidean angles:

- K2 bar1 vs GDM cs2;
- K2 bar1 vs GDM cv2.

This gives 10 preregistered leave-one-k angles.

## Primary ablation family B — leave one redshift slice out

For each of the seven frozen redshift slices, remove that entire z row from K2 bar1, GDM cs2 and GDM cv2.

On the remaining six redshift rows, retain the same per-row five-k quotient:

`R_shape_LOz(z_remaining,k) = R(z_remaining,k) - mean_k R(z_remaining,k)`.

Then compute the two oriented K2/GDM angles.

This gives 14 preregistered leave-one-z angles.

## Frozen primary classification

`BROAD_SUPPORT_PASS` iff **all 24 preregistered ablation angles are >=45 degrees**.

Frozen classifications:

- `K2_VELOCITY_SHAPE_BROAD_SUPPORT_PASS_EXP071K`
- `K2_VELOCITY_SHAPE_SINGLE_SUPPORT_DEPENDENCE_EXP071K`

No average-angle criterion is allowed to rescue a failed individual ablation.

Numerical resolvability is an integrity requirement, not a science threshold: every ablated projected vector must satisfy

`norm(projected) > 1e-12 * norm(corresponding retained raw vector)`.

Any unresolved primary ablation invalidates the science classification rather than counting as a PASS or FAIL.

## Frozen quantitative summaries

Report, without changing the classification:

1. minimum K2-vs-cs2 angle over all leave-one-k ablations;
2. minimum K2-vs-cv2 angle over all leave-one-k ablations;
3. minimum K2-vs-cs2 angle over all leave-one-z ablations;
4. minimum K2-vs-cv2 angle over all leave-one-z ablations;
5. the deletion causing the largest absolute shift from the full-support Exp071J angle for each GDM axis;
6. the full distribution/range of all leave-one-k and leave-one-z angles;
7. GDM cs2-vs-cv2 mutual angles under the same ablations as non-classifying context.

## Additional non-classifying robustness

Apply the same leave-one-k and leave-one-z construction to K2 bar2-bar5 only to summarize whether the K2 finite-step family changes the support-localization pattern. These diagnostics cannot change the bar1 primary classification.

## Interpretation boundary

If BROAD_SUPPORT_PASS:

> The Exp071J velocity-shape separation is not dependent on any single frozen k node or redshift slice under the preregistered leave-one-support tests.

If SINGLE_SUPPORT_DEPENDENCE:

> The full-support Exp071J result remains valid, but at least one single-node/slice removal restores an overlap below 45 degrees and localizes a critical support region.

Neither outcome is tracer RSD, survey distinguishability, an observational nuisance quotient, covariance whitening, or unique microscopic identification.

## Gate state

Regardless of outcome:

- G7 OPEN
- G8 OPEN
- G9 OPEN
- covariance/whitening NOT AUTHORIZED
- nuisance quotient NOT AUTHORIZED
