# DSIR recovery checkpoint — Exp066C (2026-08-26)

## Result

Run `32983242318`, job `98224843271` returned

`PASS_ACT_UNWISE_EXACT_SHOT_NOISE_TEMPLATE_V0_1`.

Exp066C was separately preregistered after the permanent Exp066B failure. It did not modify the failed Exp066B constant-mode criterion.

## Exact correction

Pinned upstream uses `D=W C^{-1}` and injects constant pseudo-spectrum shot noise as `N*w2*1`. Exp066C computes the exactly equivalent template by solving

`C y = 1`

and evaluating

`t_N = N*w2*(W@y) odot T`.

No inverse, pseudoinverse, jitter, shrinkage or coupling modification is required.

### Small-matrix control

Literal `(W@inv(C))@(N*w2*1)*T` versus solve-based expression:

- maximum absolute difference: `2.117582368135751e-21`;
- frozen tolerance: `5e-13*max(1,max|reference|)`;
- solve residual: `8.881784197001252e-16`.

### Released ACT matrix

- coupling: `6144×6144`;
- bandwindow: `59×6144`;
- solve residual `max|Cy-1| = 4.884981308350689e-15`;
- frozen threshold: `1e-10`;
- all 59 exact template values finite and nonconstant;
- all six selected Blue and Green shot-noise contributions finite and nonzero.

The permanently rejected Exp066B shortcut differs from the exact template by about `0.389%` for Blue and `0.415%` for Green in the descriptive full-template metric. This small final difference does not rescue Exp066B; it explains why the shortcut was numerically tempting despite its false 36% constant-mode identity.

## Combined ACT × unWISE operator bridge

Immutable evidence now composes as:

- Exp065B selected 26×26 covariance: PASS;
- Exp066A raw independent `P_WW/P_Wm/P_mm` projection: PASS;
- Exp066B B1 free-CLEFT nuisance algebra: PASS;
- Exp066B B2 signal bandwindow/transfer mapping: PASS;
- Exp066B B3 constant-mode shortcut: **FAIL, permanent**;
- Exp066B B4 selected 26-bin ordering: PASS;
- Exp066C exact white-noise replacement: PASS.

Therefore the **ACT DR6 × unWISE selected-bandpower operator bridge is PASS** for this pinned v0.1 implementation.

This is not a G7 law discovery. Top-level state remains **G7 OPEN, G8 OPEN, G9 OPEN**.

## Next gate

Before searching a cross-channel law, freeze a physical solver-convention bridge for the independent inputs used by the ACT projector:

1. CAMB `Weyl` is documented as the gauge-invariant Weyl potential `(Phi+Psi)/2`;
2. CAMB density transfer columns and power interpolators have different transfer normalisations, so raw transfer-table columns must not be compared naively;
3. define a physical `k` convention and power units for `P_WW`, `P_Wm`, `P_mm`;
4. define the matter species convention matching upstream `delta_nonu`;
5. validate the mapping on a fixed LambdaCDM reference before applying it to any dark-sector family;
6. preserve `P_WW`, `P_Wm`, `P_mm` as independent inputs—never reconstruct Weyl from matter through a GR Poisson equation inside the adapter.

Only after that convention bridge passes may a training-only covariance-whitened G7 relation/null be preregistered. No fresh withheld family may be chosen before the relation is frozen.
