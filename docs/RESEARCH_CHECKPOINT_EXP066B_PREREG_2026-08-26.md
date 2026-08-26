# DSIR recovery checkpoint — Exp066B preregistration (2026-08-26)

## Immutable prior evidence

- F27: hard prospective failure of the full-response R^2 centroid law.
- F29: hard prospective failure of the endpoint-half-transition law on C8 IDM-photon.
- F30: hard prospective pass of the frozen two-coordinate matter-response representation on C9 IDM-baryon, but not a G7 cross-channel law.
- F31 / Exp064A: no nontrivial common AP/growth/shape plane against the frozen covariance null.
- Exp065A: permanent eligibility FAIL for the unselected 236x236 ACT x unWISE covariance assembly.
- Exp065B: hard PASS for the exact upstream-selected 26x26 Blue/Green Clgg+Clkg covariance path, without regularisation.
- Exp066A: hard PASS for a solver-neutral raw ACT x unWISE projection interface with independent P_WW, P_Wm and P_mm inputs and no hidden GR Poisson collapse.

Top-level state before Exp066B: **G7 OPEN, G8 OPEN, G9 OPEN**.

## Exp066B frozen question

Does the remaining public forward path from raw ACT x unWISE basis components to the selected 26 observable bandpowers admit an exact solver-neutral closure, including free-CLEFT nuisance algebra, transfer/bandwindow operators and the white-noise template, under the preregistered conditions in `experiments/066b_act_unwise_selected_bandpower_closure_v0_1.md`?

The scientific contract was committed before the first Exp066B execution. It freezes upstream source/data provenance, nuisance point, RNG seed 20260826, synthetic ell count 64, equivalence tolerance 5e-13, shot-noise constant-mode tolerance 1e-10, selected scale cuts and final ordering.

No fresh withheld family is selected or inspected in Exp066B. No G7 relation is searched.

## Execution rule

Run `.github/workflows/act-unwise-selected-bandpower-closure-v0-1.yml`.

Permitted scientific outcomes are only:

- `PASS_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`, or
- `FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`.

A FAIL must not be repaired by changing nuisance values, scale cuts, ordering, CLEFT sectors, seed, tolerances, bandwindow reduction or covariance conventions. Infrastructure-only failures before scientific evaluation may be fixed without altering the frozen contract.

## After PASS

A PASS closes only the forward-operator bridge. Before any G8 withheld-family selection, the project must still preregister a covariance-whitened training-only cross-channel residual relation plus a null/permutation control. Whether an additional physical CAMB/CLASS convention bridge is required must be decided explicitly before that law search; it may not be inferred after seeing withheld results.
