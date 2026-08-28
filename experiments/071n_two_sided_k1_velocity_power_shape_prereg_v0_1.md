# Exp071N — two-sided K1 primordial-tilt velocity-power-shape control v0.1

**Preregistered:** 2026-08-28, after Exp071M was frozen as `INVALID_FOR_SCIENCE_EXP071M` and before any Exp071N K1/GDM velocity-power angle is calculated.

## Why this is a new representation rather than a repair of Exp071M

Exp071M preregistered a `t_tot` **transfer-only** response. Its fresh K1 plus/minus CLASS runs completed, but the science evaluator fail-closed because changing only primordial tilt `n_s` produced a zero `t_tot` transfer response. The nonzero-vector integrity gate is retained and Exp071M is permanently classified `INVALID_FOR_SCIENCE_EXP071M`.

Exp071N asks a distinct question in a representation that includes both parts of the linear power carried by a transfer variable: primordial power and transfer response. No Exp071M threshold or integrity rule is relaxed.

## Immutable provenance

Bind:

1. Exp071M fresh two-sided K1 run
   - run `33185652795`
   - artifact `9691596312`
   - artifact name `exp071m-two-sided-k1-velocity-shape-e79c2f5852a325154c704d65c48893b23cb6d300`
   - artifact SHA256 `d0878a71adb7bbf97d7b00a67e306c0ae9c86b8b2e705cbafd00b354ede23b21`
   - pinned official CLASS `e85808324f51fc694d12e3ed7439552a3c3f9540`
   - `n_s = 0.965, 0.970, 0.960` for reference, plus, minus.

2. Exp071I GDM/common-velocity parent
   - run `33181895623`
   - artifact `9690064470`
   - artifact name `exp071i-k2-gdm-total-velocity-49996b5053b6b15428a2ff936efb4fd21fac266c`
   - artifact SHA256 `ba41e25e6bcdfd2c23c4c9c8bc48bf9ddd85d7776a2e5bb7976e2e061d531e14`
   - positive GDM parents `cs2=1e-7`, `cv2=1e-7`, same frozen reference.

The K1 step magnitude remains inherited from Exp071C/Exp071M:

`|Delta n_s| = 0.005`.

## Frozen physical response

For a linear transfer variable `T=t_tot`, define the response of its linear power proxy at fixed k as

`r_vv(z,k) = Delta ln P_R(k) + 2 Delta ln |T(z,k)|`.

With fixed `A_s` and `k_pivot`, the primordial factor for a pure tilt change is

`Delta ln P_R(k) = Delta n_s * ln(k_phys/k_pivot)`.

Therefore use exactly

`r_vv(model/ref) = (n_s_model-n_s_ref) * ln(k_phys/k_pivot) + 2 ln |t_tot_model/t_tot_ref|`.

For the GDM parents `Delta n_s=0`, so the first term is exactly zero.

Frozen constants:

- `h = 0.67`
- `k_pivot = 0.05 Mpc^-1`
- CLASS transfer output support `k_h = [0.001,0.003,0.01,0.03,0.1] h/Mpc`
- convert to physical wavenumber as `k_phys = h * k_h` before the primordial logarithm.

The primary per-redshift shape projection subtracts the mean over k. Consequently any common constant shift in `ln(k_phys/k_pivot)` is removed; nevertheless the physical conversion above is fixed explicitly and may not be changed after the result.

## Frozen support

Use exactly

- `z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`
- `k_h = [0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`.

No crop, fitted weights, covariance, survey window, or nuisance fit is allowed.

## Tangent orientation and shape quotient

For K1 plus and minus, preserve the actual displacement orientation by dividing each full `r_vv` response by the positive step magnitude `0.005`; do **not** multiply the negative displacement by another minus sign.

For GDM divide the positive `cs2` and `cv2` responses by `1e-7`.

For every tangent matrix `R(z,k)` apply the unchanged Exp071J quotient

`R_shape(z,k) = R(z,k) - mean_k R(z,k)`.

Equal weights over the five k nodes.

## Integrity gates before science classification

1. Exact immutable artifact identities/digests for Exp071M and Exp071I.
2. Fresh Exp071M reference must reproduce the immutable Exp071I official-CLASS reference on the frozen support in both matter power and `t_tot` to maximum relative difference `<=1e-10`.
3. Confirm the Exp071M transfer-null diagnosis quantitatively by reporting maximum absolute K1 plus/minus `ln|t_tot_model/t_tot_ref|`; this is diagnostic and does not replace the full `r_vv` response.
4. Every projected full velocity-power tangent must satisfy `norm(projected) > 1e-12 * norm(raw)`.
5. All values must be finite and the frozen k/z support complete.

Any failure is `INVALID_FOR_SCIENCE_EXP071N`.

## Frozen primary statistic

Compute four oriented Euclidean angles in `R_shape`:

- K1(+) vs GDM `cs2(+1e-7)`
- K1(+) vs GDM `cv2(+1e-7)`
- K1(-) vs GDM `cs2(+1e-7)`
- K1(-) vs GDM `cv2(+1e-7)`.

Inherited separator: **45 degrees**.

Primary PASS iff all four angles are `>=45 deg`.

Frozen classifications:

- `K1_TWO_SIDED_VELOCITY_POWER_SHAPE_SEPARATED_FROM_BOTH_GDM_AXES_EXP071N`
- `K1_TWO_SIDED_VELOCITY_POWER_SHAPE_OVERLAPS_GDM_EXP071N`

No average angle can rescue an individual failure.

## Frozen diagnostics, non-classifying

Report:

- K1(-) vs K1(+) mutual angle;
- nonlinear antisymmetry error;
- line-angle prediction from K1(+) alone `min(theta,180-theta)` and its discrepancy from the fresh K1(-) angle;
- retained shape norm fractions;
- GDM `cs2` vs `cv2` projected mutual angle;
- maximum absolute K1 transfer-only response, documenting why Exp071M was null.

## Interpretation boundary

If PASS:

> The tested two-sided primordial-tilt nuisance line is separated from both tested positive GDM rays in the preregistered linear velocity-power-shape representation on the frozen theory support.

If FAIL:

> The tested primordial-tilt nuisance line overlaps at least one tested positive GDM ray even after primordial and transfer contributions are combined in the preregistered velocity-power-shape representation.

This is a theory-space linear power-response proxy, **not** tracer RSD, `f sigma_8`, survey distinguishability, covariance whitening, observational nuisance marginalization, unique microscopic identification, or dark-sector detection.

## Gate state

Regardless of outcome:

- G7 OPEN
- G8 OPEN
- G9 OPEN
- covariance/whitening NOT AUTHORIZED
- observational nuisance quotient NOT AUTHORIZED
