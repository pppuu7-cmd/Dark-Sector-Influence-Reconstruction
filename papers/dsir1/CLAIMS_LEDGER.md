# DSIR-I claims ledger

**Working title:** *Dark-Sector Influence Reconstruction I: Observable-response geometry, channel-conditional equivalence, and failure-resistant model comparison*

**Status:** manuscript v0.1 scope lock, 2026-08-27.

This ledger separates statements that are already supported by frozen DSIR evidence from statements that remain outside the first-paper claim boundary.

## A. Claims allowed in DSIR-I

1. **Response-space comparison is model- and channel-conditional.** A microscopic model label does not define a unique observational distance. For a chosen channel set `B`, physical projection `K_B`, positive-definite covariance whitener `W_B`, and retained nuisance quotient `Q_B`, the formal observational signature operator is
   
   `A_B = Q_B W_B K_B`,
   
   with exact channel-conditional equivalence
   
   `r1 ~_B r2  <=>  A_B (r1-r2)=0`.
   
   This is a linear-algebraic identifiability statement, not a new physical law.

2. **The compact additive low-k core `(G,T,tau)` is falsified for the tested atlas.** With
   
   `R(z,k)=mu+T(k)+tau(z)+I(z,k)` and `chi_I=||I||^2/||R||^2`, the irreducible scale-time interaction is negligible for the tested IDE directions but material for GDM and especially designer-f(R).

3. **A robust descriptive response hierarchy exists on the frozen tested domains.** Finite-amplitude envelopes are non-overlapping:
   
   `IDE < smooth-w < GDM < designer-f(R)`
   
   in `chi_I`, with sampled ranges approximately
   
   - IDE: `1.44e-11 ... 5.49e-11`
   - smooth-w: `1.0805e-3 ... 1.0881e-3`
   - GDM: `1.301e-2 ... 4.541e-2`
   - designer-f(R): `1.733e-1 ... 3.133e-1`.
   
   The tier ordering survives all 12 deterministic single-node deletion tests. This is an atlas result, not a universal law.

4. **Pairwise separation can be localized in the nonseparable component.** For normalized pairwise response-shape difference `d`, define `eta_I=||d_I||^2/||d||^2`. GDM/f(R) pairs have about 61% of their response-shape separation power in the irreducible `k x z` component on the frozen low-k grid, robust under node deletion. `eta_I` must be reported together with total angle/distance.

5. **Degeneracy is channel dependent.** The frozen theory atlas contains explicit examples:
   
   - GDM `cs2` and `cv2` are nearly collinear in low-k matter power (angle about `0.3226 deg`) but are strongly separated by metric slip (about `137.94 deg`; equalized Weyl+slip about `56.96 deg`).
   - GDM and designer-f(R) can be nearly degenerate in the leading scale mode (about `0.08-0.10 deg`) while time evolution/full response separates them strongly.
   
   These are theory-response statements until the full observational kernel/covariance/nuisance quotient is frozen.

6. **Low representation dimension is not microscopic parameter count.** One-dimensional physical parameter rays can curve in response space. Sampled direction turns reach about `7.18 deg` for GDM viscosity and `12.14 deg` for designer-f(R), so `N_micro`, manifold dimension, linear representation rank, and discriminant count must remain distinct.

7. **Mechanism diversity survives withheld/interpolation tests.** Thermal WDM exhibits a strong high-k but nearly time-separable response (`chi_I ~ 2e-10`) and a monotonic cutoff coordinate `k_0.1` for preregistered withheld masses. A genuinely withheld DCDM-to-dark-radiation family passes the preregistered temporal-localization direction, with `z_R` moving `0.6304573 -> 0.6562403` as `Gamma/H0` goes `0.25 -> 2`. These support the usefulness of localization/trajectory geometry but do not define a universal law.

8. **Failure-resistant provenance is part of the method.** Scientific FAILs are preserved rather than overwritten by later corrective providers. In particular, the original C5 q=1 bridge failure and C3 target-grid interpolation failure remain provenance even though separately justified providers later pass their own prospectively frozen contracts.

## B. Claims explicitly prohibited in DSIR-I

- No claim of discovery of new fundamental physics.
- No claim that DSIR has discovered a dark-sector invariant or universal residual law.
- No claim that G7, G8, or G9 is closed. They remain OPEN.
- No claim of a universal dark-sector no-hair theorem.
- No claim that `(G,T,tau,I)` is a fundamental four-parameter description.
- No claim that the raw six-direction singular spectrum implies `R_model=5` or any fixed intrinsic rank.
- No claim that theory-space angular separation is already survey-level detectability.
- No zero-imputation of undefined/masked theory-channel cells.
- No retrospective threshold tuning to convert failed experiments into passes.

## C. First-paper scope

DSIR-I is a **methodological and phenomenological response-atlas paper**. It establishes a common language for comparing physically different dark-sector mechanisms, shows with frozen examples why single-channel or low-dimensional summaries fail, formalizes channel-conditional equivalence, and documents prospective/withheld validation practice.

A later paper may address fully observational quotient distances after the common support mask, covariance whitening, nuisance tangent SVD, and fresh withheld-family relation tests are completed.