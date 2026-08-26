# DSIR recovery checkpoint — Exp065B (2026-08-26)

## Immutable prior state

- F31 / Exp064A: `NO_NONTRIVIAL_COMMON_PLANE_RELATION_V0_1`; no ShapeFit common-plane law promoted.
- Exp065A: permanent `FAIL_ACT_UNWISE_OBSERVATIONAL_BINDING_ELIGIBILITY_V0_1` because the unselected raw Blue+Green 236×236 covariance is not positive definite. Do not relabel or erase this result.
- The post-Exp065A source audit showed that the official likelihood applies its scale cuts and `select_from_matrix` before assembling the covariance actually used by `XCorrACT`.

## Exp065B frozen corrective question

Using the same pinned `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179` and the same official data archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`, reproduce the official ACT scale selections exactly:

- `Clgg`: `[100,402]`;
- `Clkg`: `[51,402]`.

Then apply the literal `select_from_matrix` semantics to Blue, Green and Blue×Green covariance blocks. No jitter, clipping, shrinkage, diagonal loading, nearest-PSD projection or scale-cut retuning is allowed.

## Hard result

Workflow run `32980117716`, job `98214421282` returned:

`PASS_ACT_UNWISE_SELECTED_COVARIANCE_ELIGIBLE_V0_1`.

Per sample, the official selections retain 6 `Clgg` and 7 `Clkg` bins, 13 total. The selected midpoints are:

- `Clgg`: `126.5, 176.5, 226.5, 276.5, 326.5, 376.5`;
- `Clkg`: `76.5, 126.5, 176.5, 226.5, 276.5, 326.5, 376.5`.

Selected covariance diagnostics:

- Blue 13×13: `lambda_min=2.0718128137257107e-17`, Cholesky PASS, inverse residual `1.5417651827035471e-15`;
- Green 13×13: `lambda_min=2.1711842660783815e-17`, Cholesky PASS, inverse residual `1.0586612801907153e-15`;
- combined Blue+Green 26×26: `lambda_min=1.2742353176342933e-17`, `lambda_max=3.980349119528573e-15`, Cholesky PASS, inverse residual `3.8167569492587215e-15`.

Thus the official XCorrACT-selected observable block is numerically usable without regularization.

## Scientific meaning

This closes only the **observational eligibility/kernel-covariance prerequisite** for the ACT DR6 × unWISE Blue/Green `Clgg + Clkg` block. It is not a G7 physical law and is not a G8 withheld test.

The public theory module requests `Weyl×Weyl`, `Weyl×delta_nonu` and `delta_nonu×delta_nonu` spectra, but its implementation is tied to CAMB objects/cosmology helpers. DSIR must not treat that backend as solver-neutral by declaration.

## Exact next action

Create a separately numbered experiment that freezes a **solver-neutral observable-forward interface**:

1. survey-side immutable inputs: Blue/Green `n(z)`, bandwindow matrices, transfer functions, official scale selections and the Exp065B selected covariance;
2. theory-side abstract inputs: background distance/Hubble quantities plus `P_Weyl,Weyl(k,z)`, `P_Weyl,m(k,z)`, and `P_m,m(k,z)` in explicitly frozen units/conventions;
3. a deterministic mapping to raw/binned `Clgg` and `Clkg` with nuisance/bias handling explicitly separated from dark-sector response coordinates;
4. a regression test against the pinned official backend on a reference cosmology before any DSIR cross-channel law search.

Only after this bridge is frozen and validated may one training-only cross-channel relation/null statistic be preregistered. A fresh withheld theory family for G8 must still not be selected before that relation is frozen.

Top-level state remains: **G7 OPEN, G8 OPEN, G9 OPEN**.
