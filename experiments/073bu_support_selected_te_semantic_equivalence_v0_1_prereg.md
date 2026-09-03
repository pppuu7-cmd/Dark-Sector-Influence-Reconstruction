# Exp073BU support QA — stock full-window vs selected low-memory TE semantic equivalence v0.1

Status: **PREREGISTERED NON-SCIENTIFIC SUPPORT QA**
Accounting: `+0/+0` for every outcome. This QA cannot create Wm_S3 authority and cannot change the frozen Exp073BU A/B comparator.

## Question frozen before output

For a deterministic synthetic spin-0 x spin-2 mask pair under exact PyMaster/NaMaster 2.7, compare:

A. stock `NmtWorkspace.compute_coupling_matrix` followed by `get_bandpower_windows()`, requiring full shape `[2, nb, 2, L]` before selecting `stock[0,:,0,:]` (`TE <- TE`);

B. the repository low-memory selected-component algebra used by the validated coupling architecture:
`mask PCL -> get_general_coupling_matrix(pcl,0,2,0,2) -> fixed ascending-ell band compression -> K-from-A -> np.linalg.solve(K,A)`.

This QA tests semantic/equation linkage only. It does not authorize substituting B for the full-shape runtime requirement unless the result is Q1 exact and a later prospective BU implementation-binding audit explicitly permits that use without weakening the preregistration.

## Frozen synthetic domain

- `nside=16`, `L=48`, `lmax=47`;
- RING maps generated deterministically from pixel `theta,phi`;
- lens mask: finite positive nontrivial weighted scalar field with deterministic hard support;
- source mask: a different finite positive nontrivial weighted field with deterministic hard support;
- exact band edges `[0,4,8,12,16,24,32,40,48]`;
- spin signature `(0,2)`;
- PyMaster/NaMaster lineage exactly `2.7` or `2.7.x`.

## Frozen comparison and outcomes

Canonical selected arrays are C-order little-endian `<f8 [8,48]`.

- **Q1_EXACT_SELECTED_TE_EQUIVALENCE**: stock full shape is exactly `[2,8,2,48]`; selected stock and low-memory arrays have equal canonical SHA256 **and** `numpy.array_equal=True`.
- **Q2_NUMERIC_ONLY_SELECTED_TE_EQUIVALENCE**: provenance/shape valid, exact equality false, but `max_abs_difference <= 1e-12`. This is semantic QA only and does **not** authorize a runtime substitution in Exp073BU.
- **Q3_SELECTED_TE_SEMANTIC_MISMATCH**: provenance/shape valid and `max_abs_difference > 1e-12`, or nonfinite/noncanonical output. Reject the low-memory selected-component route for BU science unless a new prospective scientific contract is created.
- **Q4_INFRASTRUCTURE_INCOMPLETE**: dependency/install/runtime failure before valid paired arrays. Diagnose infrastructure; no scientific conclusion.

No tolerance, rounding, smoothing, averaging, ULP rule, preferred output or result-dependent criterion change may convert Q2/Q3 into Q1. The `1e-12` threshold exists only to distinguish semantic QA Q2 from Q3; it is not an Exp073BU scientific acceptance tolerance.

## Firewall

No DES data, Exp073R1 artifacts, historical Wm arrays, historical PCL arrays, physical-support masks, covariance, nuisance geometry, G7/G8/G9 or current Wm_S3 outputs are read. The test is synthetic and hosted-only.
