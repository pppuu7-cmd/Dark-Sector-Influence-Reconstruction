# ACT × unWISE CLEFT solver-neutrality boundary — 2026-08-26

## Purpose

This source audit determines whether the public ACT DR6 × unWISE CLEFT/nonlinear branch can be inserted unchanged into the DSIR solver-neutral observable interface for arbitrary dark-sector / modified-gravity families.

**Conclusion: no.** The public baseline remains valid for its intended cosmological analysis, but its CLEFT cross-term construction contains a GR-specific matter→Weyl conversion. DSIR must not silently promote that implementation into a model-independent bridge.

Pinned source:

`ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`.

## 1. Already validated solver-neutral linear interface

Exp066A separated the raw projection into independent physical inputs

\[
P_{WW}(k,z),\qquad P_{Wm}(k,z),\qquad P_{mm}(k,z),
\]

plus background geometry and released tracer kernels. Its anti-collapse control verified that changing any one spectrum affects only the expected projection components. No Poisson reconstruction of Weyl from matter is allowed in this interface.

Exp067E subsequently validated the CAMB↔CLASS physical convention for these three independent spectra on preregistered out-of-sample LambdaCDM references.

Exp068A tests this interface on real released Blue/Green kernels in the linear/no-CLEFT branch.

## 2. Public CLEFT branch contains a GR-specific conversion

The pinned upstream `unWISExkappa_model.py` and `unWISExkappa_model_freeCLEFT.py` form the CLEFT Weyl–matter contribution using

```python
matter2weyl_factor = 3/2 * cosmo.Omega_m * cosmo.H0**2 * (1+z) \
    * kGrid**2/(3*cosmo.curvature-kGrid**2)

cleft_pk_evals_weyl_dnonu = matter2weyl_factor \
    * cleft_interpolations_dtot_dnonu[...] / cosmo.h**3 / f_K(chi)**2
```

In a spatially flat background this reduces to a scale-independent signed factor proportional to

\[
-\frac32\Omega_mH_0^2(1+z),
\]

which is the GR Poisson-type conversion used to turn a matter CLEFT contribution into a Weyl–matter contribution.

This is materially different from accepting an independently supplied higher-order `P_Wm` correction.

## 3. Why this matters for DSIR

For modified gravity, interacting sectors, exotic stress, or other models in which the metric response is not fixed by the GR matter Poisson relation, the nonlinear/higher-order Weyl–matter correction need not equal a matter CLEFT term times the upstream `matter2weyl_factor`.

Therefore the following operation is forbidden as a model-independent DSIR step:

\[
\Delta P_{Wm}^{\rm NL}\stackrel{\rm forbidden}{:=}
F_{\rm GR}(z,k)\,\Delta P_{mm}^{\rm CLEFT}
\]

for an arbitrary family merely because the public likelihood uses that relation in its intended baseline model.

This does **not** criticize or invalidate the released likelihood. It defines the boundary of what DSIR may call solver-neutral.

## 4. Consequence for nuisance quotients

The source-level nuisance inventory contains 18 named ACT parameters. Four are free-CLEFT shift directions (`cb2`, `cbs` for Blue and Green). Those four become meaningful only when a nonzero physical CLEFT basis is present.

A full 18-parameter baseline tangent Jacobian therefore inherits the CLEFT physical convention. Applying it unchanged to arbitrary DSIR dark-sector/MG families would mix an observational nuisance quotient with an unvalidated GR nonlinear closure.

Accordingly, DSIR must distinguish:

### A. Linear/no-CLEFT observational subspace

Use the validated independent `P_WW/P_Wm/P_mm` interface, real survey kernels, released selected covariance and Exp067A whitening. The four CLEFT-shift tangent columns are identically absent/zero. A later rank gate may operate on the at-most-14 visible nuisance columns, with the actual numerical rank preregistered and measured rather than assumed.

Any G7 result obtained here must be labelled **linear/no-CLEFT scope** and must use an explicit validity/domain statement; it is not a full-baseline ACT likelihood claim.

### B. General nonlinear solver-neutral extension

A future DSIR nonlinear bridge must expose independent higher-order/nonlinear inputs rather than enforcing the GR conversion. At minimum the interface would need independently meaningful corrections analogous to

\[
\Delta P_{WW}^{\rm NL},\qquad
\Delta P_{Wm}^{\rm NL},\qquad
\Delta P_{mm}^{\rm NL},
\]

or a more fundamental family-specific response representation from which these are computed without a hidden GR identity.

Families for which such inputs are unavailable must be **masked**, never zero-imputed.

Only after such a bridge is physically validated can the full CLEFT-aware nuisance tangent be called solver-neutral across those families.

## 5. Recommended G7 path

The smallest rigorous next path is therefore:

1. finish Exp068A physical linear/no-CLEFT forward reproduction;
2. if PASS, preregister a selected-26D, Exp067A-whitened **linear/no-CLEFT nuisance tangent rank gate** using only genuinely active nuisance directions;
3. determine and freeze the numerical nuisance projector under step-size/SVD stability controls;
4. define an explicit linear-domain/validity policy before fitting any cross-channel G7 relation;
5. train one relation only on eligible training families and apply a nontrivial null/permutation control;
6. freeze the relation before selecting a fresh G8 withheld family;
7. treat full-baseline nonlinear/CLEFT closure as a later stronger observational-validation layer, not as an excuse to inject the GR Poisson relation into arbitrary models.

## 6. Current gate state

This audit is a methodological boundary, not a top-level gate closure.

- G7: OPEN.
- G8: OPEN.
- G9: OPEN.

The key preserved rule is:

> **solver neutrality must hold in the physical forward model before nuisance quotienting; a public baseline nuisance model may not be generalized beyond its physical assumptions by declaration.**
