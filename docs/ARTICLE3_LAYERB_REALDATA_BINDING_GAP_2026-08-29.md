# Article 3 Layer-B real-data coordinate-binding gap

**Date:** 2026-08-29  
**Status:** pre-execution audit; no real support score has been evaluated.

## Finding

The later Article-3 coordinate/common-response support contract is synthetically well tested but is not yet uniquely bindable to the real DES/BOSS finite observation operator.

Two missing real-data definitions were identified before any output:

1. a real Wm/WW pseudo-C_ell or BOSS finite-matrix observation row has a broad support kernel/window over physical `(k,z)` and therefore does not possess a unique exact scalar `(z,k)` pair;
2. the contract requires a vector `final_response_abs_values` containing all preregistered response components in a frozen order, but the current repository contract does not identify the real operator-level component names or the producer that supplies that vector.

Synthetic rows such as `(z=0.5, k=0.01, final_response_abs_values=[1,2])` validate classifier arithmetic but do not resolve either real-data definition.

## Evidence from the pinned real operator

The current DES route is pinned to `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`.

That implementation constructs a NaMaster mode-coupling workspace and obtains full bandpower windows using

`wins = w.get_bandpower_windows()`.

The frozen Exp073P operator-support preregistration then propagates the **positive absolute bandpower-window envelope** through lens/source redshift kernels to physical `(k,z)`. This broad-envelope treatment is precisely why an effective ell or a single representative `(k,z)` value is not sufficient to certify physical support.

The same issue exists for BOSS: the frozen component is a composed finite matrix `C=W@M`, and support is evaluated from the absolute row envelope over the true-k input columns, not from one scalar effective k.

## Consequence

No real Article-3 Layer-B execution is authorized merely by possessing:

- a DES bandpower effective ell;
- an effective redshift;
- a support-weighted centroid;
- a midpoint k;
- or any other scalarized `(z,k)` proxy

unless that scalarization is separately and prospectively frozen with a proof that it serves the intended Layer-B semantics rather than replacing broad operator support.

Likewise, no real producer may invent the contents of `final_response_abs_values` after inspecting support/covariance/nuisance/G7 results.

## Current safe interpretation

The broad **Layer-A operator-support leakage gate** from `docs/ARTICLE3_DUAL_SUPPORT_HIERARCHY_AMENDMENT_2026-08-29.md` is the current physically well-defined support test for real survey rows.

Layer B is retained as a separate prospective **final-coordinate/common-response integrity layer**, but its real-data binding remains BLOCKED until the component vector and geometric-eligibility representation are explicitly resolved.

This is not a scientific FAIL. It is an architecture/interface gap discovered before real scoring.

## Candidate resolution paths — not yet selected

A future prospective amendment may choose one of the following only after a representation audit independent of real support outcomes:

### Route A — inherit physical eligibility from Layer A

Treat `S_op`, the rows that passed the broad operator-support gate, as the physically eligible Layer-B input set. Layer B then checks only immutable coordinate identity/order plus a prospectively defined operator/common-response validity vector. Scalar `(z,k)` values, if retained for diagnostics, are not used to reclassify broad support.

This route avoids pretending that a wide bandpower is a point in `(k,z)`.

### Route B — define a canonical scalarization

Define a deterministic scalar `(z,k)` functional of the **full uncropped positive support envelope**, freeze it before real output, prove invariance/units/boundary behavior, and show that it does not permit a row with unacceptable broad leakage to pass. Layer A remains required regardless.

No effective-ell-only shortcut is admissible.

## Additional inventory recovered

From the pinned Cosmotheka configuration and pair-generation semantics:

- DES has 5 `DESgc` lens tracers and 4 `DESwl` source tracers;
- `DESgc-DESwl: all` gives 20 unique lens-source pairs;
- `DESwl-DESwl: all` gives 10 unique source auto/cross pairs under upper-triangular pair ordering;
- the frozen edge list has 40 edges and therefore 39 bandpowers;
- NaMaster spin ordering is `(aE,aB)` for spin-0 x spin-2 and `(EE,EB,BE,BB)` for spin-2 x spin-2;
- the preregistered science blocks select signed Wm `aE` and WW `EE`;
- therefore the DES scalar science inventory before support contains 20*39 = 780 Wm coordinates and 10*39 = 390 WW coordinates;
- the frozen BOSS mm component contributes 240 observed even-multipole rows before its support mask.

Thus the currently reconstructable full scalar observation inventory is **1410 candidate rows** before support, subject to final provenance verification when the real producer is implemented.

This count does **not** define the unresolved `final_response_abs_values` component vector and earns no scientific PASS.

## Gate state

- hosted Exp073R1 reproduction: pending;
- hosted prerequisite receipt: prospectively frozen, pending;
- full pre-support finite-operator producer: OPEN implementation task;
- Layer A operator support: BLOCKED pending upstream authority/operator;
- Layer B real-data binding: BLOCKED by this documented interface gap;
- covariance/whitening: BLOCKED;
- G7/G8/G9: OPEN.

Article-3 scientific readiness remains **44%**.