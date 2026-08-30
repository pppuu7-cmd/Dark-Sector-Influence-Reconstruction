# Exp073BA — Article-3 low-memory Wm_S1 production v0.1 preregistration

**Project:** Dark-Sector Influence Reconstruction (DSIR) only. RTK/RQIR excluded.  
**Classification:** first classifying task under candidate successor authority `low_memory_general_coupling_deterministic_v1`.  
**Execution condition:** this gate is forbidden unless Exp073AZ first returns exact hosted `PASS_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1` and an immutable canonical `<f8 [12288]` PCL artifact is bound prospectively in a separate receipt/freeze before trigger.  
**Readiness:** `52%` before and after this individual task; `+0` readiness.

## 1. Immutable predecessor state

Exp073AQ remains permanently:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Exp073BA does not rescue, average, round, tolerate, prefer, or reinterpret either AQ replica. No AQ numerical payload may be used as a target value or acceptance reference.

The only allowed numerical input to the heavy coupling stage is the canonical Wm_S1 mask PCL emitted by a successful Exp073AZ exact PCL gate.

## 2. Frozen physical/angular contract

Unchanged from Article-3 authority:

- real DES Y1 masks;
- `NSIDE=4096`, RING;
- ell `0..12287` inclusive;
- exactly 39 frozen bandpowers and the previously frozen edges;
- PyMaster/NaMaster 2.7 lineage;
- Wm selected response `TE <- TE`;
- selected array `<f8 [39,12288]`;
- no radial/support/covariance/whitening/nuisance/quotient/relation/null/G8 read;
- no effective ell/z/k or fiducial-P shortcut;
- all scientific support thresholds unchanged.

## 3. Frozen heavy computation

Each compact-coupling replica receives exactly the same immutable canonical `<f8 [12288]` Wm_S1 PCL authority from Exp073AZ and computes:

`G02 = pymaster.get_general_coupling_matrix(PCL, 0, 2, 0, 2)`

then deterministically compresses it by fixed-order row accumulation within each frozen output band:

`A[b,:] = sum_{ell=edge[b]}^{edge[b+1]-1} G02[ell,:] / (edge[b+1]-edge[b])`.

No BLAS reduction is allowed for this compression. `G02` is released immediately after `A` is formed.

Canonical compact output is exactly `<f8 [39,12288]`.

## 4. Exact compact gate

Two fresh independent hosted replicas A and B are required.

PASS requires simultaneously:

- both bind the same frozen Exp073AZ canonical PCL receipt;
- `numpy.array_equal(A_A,A_B) == True`;
- canonical `<f8` SHA256 equality;
- identical shape `[39,12288]`;
- all entries finite;
- no forbidden downstream reads.

Any complete exact mismatch is

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073BA_WM_S1_COMPACT_EXACT_V0_1`.

Failure before valid comparator authority is infrastructure-INCOMPLETE.

No tolerance, ULP, rounding, majority-vote or preferred-replica rule exists.

## 5. Frozen finalizer

Only if the compact gate PASSes may its exact admitted compact `A` be finalized.

Construct frozen band-expansion matrix `Q` implicitly: each column b has value 1 for all integer ell in the corresponding frozen edge interval and 0 elsewhere.

Compute compact binned coupling:

`K[:,b] = sum_{ell=edge[b]}^{edge[b+1]-1} A[:,ell]`

using fixed-order addition.

Selected window:

`W = numpy.linalg.solve(K,A)`

with no pseudoinverse, regularization, jitter, rounding, clipping or post-hoc rescue.

Two fresh finalizer processes/jobs receive the same admitted `A` and must produce exact identical `<f8 [39,12288]` W.

PASS requires:

- `numpy.array_equal(W_1,W_2) == True`;
- canonical SHA256 equality;
- finite entries;
- every frozen band has strictly positive `sum(abs(W[b,:]))`;
- all anti-leakage flags remain false.

A complete exact mismatch is

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073BA_WM_S1_FINALIZER_EXACT_V0_1`.

## 6. Task authority

Wm_S1 obtains successor authority only if:

- Exp073AZ PCL exact gate PASSed;
- Exp073BA compact exact gate PASSed;
- Exp073BA finalizer exact gate PASSed.

Success token:

`PASS_EXP073BA_WM_S1_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`.

Authority class:

`low_memory_general_coupling_deterministic_v1`.

Even this PASS gives `+0` readiness.

Only after this exact PASS may Wm_S2 receive its own separately frozen classifying gate. No later task may leapfrog Wm_S1.

## 7. Anti-leakage/accounting firewall

Must remain false throughout:

`physical_support_evaluated`, `operator_f_invalid_computed`, `retained_coordinates_evaluated`, `layer_b_evaluated`, `fiducial_P_weighting_used`, `covariance_read`, `whitening_performed`, `nuisance_geometry_read`, `nuisance_svd_performed`, `relation_null_read`, `chi_square_read`, `p_value_read`, `G8_read`, `scientific_pass_claimed`.

Article-3 readiness is exactly `52%`; G7/G8/G9 remain OPEN.

## 8. Trigger discipline

This preregistration alone does not authorize execution. Before trigger, a separate immutable binding receipt must freeze:

- Exp073AZ run/job/artifact/digest;
- Exp073AZ canonical PCL SHA256;
- exact Exp073BA implementation commit;
- exact workflow commit/freeze;
- exact dependency lineage and thread controls.

The trigger may be created only after those values are known from a valid Exp073AZ PASS, without altering the scientific/numerical acceptance rules above.
