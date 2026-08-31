# Exp073BJ — Article-3 Wm_S1 two-thread Track-A successor v0.1 — preregistration

**Project:** Dark-Sector Influence Reconstruction (DSIR) only; RTK/RQIR excluded.  
**Frozen prospectively:** 2026-08-31, after terminal Exp073BI `BI_Q1_PARALLEL_EXACT_QA_PASS` and before any Exp073BJ result exists.  
**Classification:** classifying Track-A execution successor to Exp073BA; scientific/numerical contract inherited unchanged.  
**Readiness before execution:** `Verified 52.0% | Draft/data 53.7%`. No readiness increment exists unless and until a separately immutable final scientific authority is produced and the Article-3 ledger explicitly admits it.

## 1. Immutable predecessor state

Exp073AQ remains permanently:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Exp073BJ cannot rescue, average, round, tolerate, prefer or reinterpret either AQ replica.

Exp073AZ remains the only admitted Wm_S1 mask-PCL predecessor authority:

- run `33339663991`;
- head `0a9581e19f7f010e13bf9aa88307b1940d0105de`;
- terminal `PASS_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1`;
- canonical PCL `<f8 [12288]` as bound by the existing Exp073BA/BC provenance receipt.

Exp073BA run `33345968620` remains terminal infrastructure/execution incomplete with no scientific classification. No incomplete BA array is reusable by BJ.

Exp073BH run `33370998182` remains `BH_D2_TIMEOUT_OR_EXTERNAL_CANCELLATION_EVIDENCED`, infrastructure-only.

Exp073BI is the prospective execution-feasibility predecessor for this successor:

- run `33375467713`;
- artifact id `9751718353`;
- artifact digest `sha256:c857b24fdcc0a49b749fbfd538451a8e53bf98f4da9abd92cefce3c4a9df2752`;
- terminal `BI_Q1_PARALLEL_EXACT_QA_PASS`;
- independent two-thread QA outputs had `numpy.array_equal == True`;
- `sha_a == sha_b == 5e00c7377d50a71d88c98a324d53ef403617022c8dadd4a390eebbe7be4612ba`;
- synthetic stock-equivalence maximum absolute difference `8.881784197001252e-16`, under the prospectively frozen synthetic-only `1e-12` QA threshold.

BI is not scientific authority and contributes `+0/+0`; its only role here is prospective authorization to test the two-thread execution policy at full scale.

## 2. Only allowed change relative to Exp073BA

The scientific algorithm, inputs, shapes, thresholds, exact comparators and task ordering are unchanged.

The only intended change is execution engineering validated prospectively by Exp073BI:

- `OMP_NUM_THREADS=2`;
- `OPENBLAS_NUM_THREADS=2`;
- `MKL_NUM_THREADS=2`;
- `NUMEXPR_NUM_THREADS=2`;
- `BLIS_NUM_THREADS=2`;
- `OMP_DYNAMIC=FALSE`.

The historical BA `VECLIB_MAXIMUM_THREADS=1` is retained unchanged; the hosted runner is Ubuntu and BI did not alter/freeze this variable.

No timeout relaxation is introduced: compact replica jobs retain the hosted `timeout-minutes: 360` boundary.

## 3. Frozen physical/angular contract

Unchanged from Exp073BA and Article-3 authority:

- real DES Y1 masks;
- `NSIDE=4096`, RING;
- true ell `0..12287` inclusive;
- exactly 39 frozen bandpowers and frozen edges;
- PyMaster/NaMaster 2.7 lineage;
- Wm selected response `TE <- TE`;
- selected canonical array `<f8 [39,12288]`;
- support boundaries remain `0.295 <= z <= 2.33`, `0 < k <= 0.06664762008318016 Mpc^-1`, Layer-A `operator_f_invalid <= 0.05`, Layer-B invalid-row fraction `<=0.05`, retained dimension `>=15`;
- no radial/support/covariance/whitening/nuisance/quotient/relation/null/G8 read;
- no effective ell/z/k or fiducial-P shortcut;
- exact-threshold ambiguity remains `numerically_unresolved`.

## 4. Frozen heavy computation

Each fresh BJ compact replica A and B independently binds the same immutable Exp073AZ canonical `<f8 [12288]` Wm_S1 PCL and computes exactly the inherited BA algebra:

`G02 = pymaster.get_general_coupling_matrix(PCL, 0, 2, 0, 2)`

then fixed-order band compression:

`A[b,:] = sum_{ell=edge[b]}^{edge[b+1]-1} G02[ell,:] / (edge[b+1]-edge[b])`.

No BLAS reduction is allowed for this compression. `G02` is released after `A` is formed. Canonical compact output is `<f8 [39,12288]`.

## 5. Exact compact classification

Two complete fresh hosted compact replicas are mandatory.

Compact PASS requires simultaneously:

- both bind the same frozen Exp073AZ PCL authority;
- both bind the terminal Exp073BI Q1 execution receipt;
- `numpy.array_equal(A_A,A_B) == True`;
- canonical `<f8` byte-SHA256 equality;
- identical shape `[39,12288]`;
- all entries finite.

A complete valid exact mismatch is:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073BJ_WM_S1_COMPACT_EXACT_V0_1`.

Cancellation, timeout, missing/invalid artifact or any failure before two complete valid comparator inputs is:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073BJ`.

No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue exists.

## 6. Frozen finalizer

Only an exact compact PASS admits the canonical compact `A` to finalization.

Construct K by the inherited fixed-order band accumulation and solve exactly as BA:

`W = numpy.linalg.solve(K,A)`

with no pseudoinverse, regularization, jitter, rounding, clipping or post-hoc rescue.

Two fresh BJ finalizer jobs receive the same admitted compact `A` and must produce exact identical `<f8 [39,12288]` W.

Final PASS requires:

- `numpy.array_equal(W_1,W_2) == True`;
- canonical byte-SHA256 equality;
- finite entries;
- every frozen band has strictly positive `sum(abs(W[b,:]))`;
- all anti-leakage flags remain false.

A complete valid final mismatch is:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073BJ_WM_S1_FINALIZER_EXACT_V0_1`.

Successful task authority token:

`PASS_EXP073BJ_WM_S1_TWO_THREAD_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`.

## 7. Authority and accounting firewall

A GitHub workflow success by itself is not a scientific PASS. Scientific PASS exists only if the immutable hosted final authority JSON carries the frozen BJ success token after both exact comparator stages complete.

Until that authority exists:

`Verified increment = 0`

`Draft/data increment = 0`

The following remain forbidden inputs throughout BJ:

`physical_support_evaluated`, `operator_f_invalid_computed`, `retained_coordinates_evaluated`, `layer_b_evaluated`, `fiducial_P_weighting_used`, `covariance_read`, `whitening_performed`, `nuisance_geometry_read`, `nuisance_svd_performed`, `relation_null_read`, `chi_square_read`, `p_value_read`, `G8_read`.

## 8. Trigger discipline

Before trigger, a separate immutable BJ binding receipt must freeze at minimum:

- this preregistration commit;
- Exp073BI run/artifact/digest/Q1 token and exact QA SHA;
- Exp073AZ run/head/status and canonical PCL binding;
- exact inherited low-memory implementation lineage;
- exact BJ comparator implementation commit;
- exact BJ workflow creation/freeze commit;
- exact two-thread environment above.

Only after those values are known may the trigger be committed. The binding receipt cannot alter any scientific acceptance rule.

## 9. G7 firewall

Required order remains:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

Exp073BJ concerns only Wm_S1 authority succession. It does not authorize Layer A/B, covariance/whitening, nuisance geometry, relation/null analysis or G8. No G8 jump is permitted.
