# Exp073BW — Article-3 streaming general-coupling exact-equivalence QA v0.1 — preregistration

**Project:** DSIR only.  
**Classification:** NONCLASSIFYING numerical / implementation-equivalence QA.  
**Accounting:** `+0 Verified / +0 Draft-data` for every outcome.

Frozen prospectively on 2026-08-31 after Exp073BV terminal `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED` and before any BW implementation result.

## Immutable predecessor state

- Exp073BJ run `33379013167` remains terminal Track-A exact Wm_S1 authority PASS.
- Exp073AQ remains permanently `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and is forbidden downstream.
- Exp073BV run `33420824723`, artifact `9768866582`, digest `sha256:33f013a8c7c06ce2f5f68e62a324b80f2b1911ff2a3cd3ff89a6af4add179cc5`, head `6010f094782a277017cbf0bb2a9af63331bb3282`, is terminal `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`.
- Exact upstream NaMaster v2.7 source commit is `24365fa59a38c15732f4f37e8b29265b75c442d5`.
- Existing DSIR low-memory implementation `ci/exp073az_article3_low_memory_general_coupling_v0_1.py` remains unchanged; BW does not alter its scientific definitions.

## Exact source algorithm frozen for replication

At upstream v2.7, `pymaster.get_general_coupling_matrix` calls SWIG `comp_general_coupling_matrix`, which calls `nmt_compute_general_coupling_matrix` in `src/nmt_master.c`.

For each matrix element indexed by `(ll2,ll3)`, the frozen stock algorithm is:

1. `lstart = max(s1,s2)`;
2. `wl_mask[l] = pcl_mask[l]*(2*l+1)/(4*M_PI)`;
3. `drc3jj(ll2,ll3,n1,-s1,...)` and, unless `(s1,n1)==(s2,n2)`, `drc3jj(ll2,ll3,n2,-s2,...)`;
4. increasing-`l1` accumulation:
   `xi += wl_mask[l1]*wsn1*wsn2` for `abs(ll2-ll3) <= l1 <= min(ll2+ll3,lmax)`;
5. final `xi *= (2*ll3+1.0)`.

The runtime `_nmtlib` used by Exp073BJ/BV exports global `drc3jj`; BW may dynamically resolve and call that exact runtime symbol. It may not substitute a different Wigner library or recurrence.

## Sole purpose

Test whether a low-memory C helper can reproduce stock NaMaster v2.7 general-coupling matrices and the existing DSIR row-compression **exactly**, while avoiding the need to materialize the full general matrix in the streaming-compressed mode.

BW is not Wm_S2/WW Track-A authority and cannot authorize Layer A/B or later gates.

## Frozen helper requirements

The helper must expose two modes through a shared library called from Python:

1. **full mode**: materialize a full `(lmax+1) x (lmax+1)` matrix using the exact source operation order above and the runtime `_nmtlib:drc3jj` symbol;
2. **stream-compressed mode**: for each frozen band, compute complete stock-order matrix rows in increasing `ll2`, and add each completed row into that band's accumulator in the same increasing-row order used by DSIR `compress_general`; divide each band row by the exact integer band width only after all rows in that band are accumulated.

Rows/columns below `lstart` remain exact zero as in stock output.

The helper may parallelize independent full rows and independent compressed bands only. Within one matrix element, `l1` order may not change. Within one compressed band, `ll2` accumulation order may not change.

Frozen compilation flags for the helper:

```text
-O2 -shared -fPIC -fopenmp -fno-fast-math -fno-associative-math -ffp-contract=off -fno-tree-vectorize -ldl -lm
```

No `-ffast-math`, reassociation or post-hoc flag changes are allowed for BW.

## Frozen environment

Hosted `ubuntu-24.04` with the already successful BJ/BV environment lineage:

```bash
conda create -y -p "${RUNNER_TEMP}/nmt27" -c conda-forge python=3.11 namaster=2.7 healpy astropy numpy
echo "NMT_PY=${RUNNER_TEMP}/nmt27/bin/python" >> "${GITHUB_ENV}"
```

The workflow must bind the immutable BV artifact `9768866582` and require `status == BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`, exact upstream commit, wrapper byte equality, same runtime extension object and `drc3jj` symbol evidence before running BW comparisons.

## Frozen comparison matrix

Scientific signatures to cover, because they are exactly the DSIR AZ calls needed downstream:

- Wm: `(s1,s2,n1,n2) = (0,2,0,2)`;
- WW same-parity building block: `(2,2,2,2)`;
- WW flip-parity building block: `(2,-2,2,-2)`.

Frozen sizes:

- `lmax = 24`, edges `[0,3,7,12,18,25]`;
- `lmax = 63`, edges `[0,5,12,24,40,64]`;
- `lmax = 127`, edges `[0,7,19,41,73,128]`.

Frozen deterministic PCL families:

1. `signed_dyadic`: `pcl[l] = ((l % 11) - 5) / 2**(3 + (l % 5))`;
2. `positive_dyadic`: `pcl[l] = (1 + (l % 7)) / 2**(4 + (l % 6))`.

All arrays are canonical contiguous `<f8`.

For every `(signature,size,PCL family)` case:

- obtain stock full matrix using `pymaster.get_general_coupling_matrix`;
- obtain helper full matrix with helper thread count 1 and 2;
- obtain helper stream-compressed matrix with helper thread count 1 and 2;
- obtain stock compressed reference by applying the frozen DSIR row-compression operation to the stock full matrix.

## Frozen exact comparators

No tolerance is classifying.

For each comparison require both:

- `numpy.array_equal(...) == True`;
- canonical contiguous `<f8` byte SHA256 equality.

Additionally require helper 1-thread and 2-thread outputs to be exactly equal and SHA-identical for both full and compressed modes.

`max_abs_diff` may be recorded only as diagnostic metadata and can never rescue exact mismatch.

## Frozen terminal labels and precedence

If essential setup, BV binding, compilation or comparison is incomplete:

`BW_Q5_INFRASTRUCTURE_OR_DIAGNOSTIC_INCOMPLETE`

Otherwise classification precedence is:

1. if helper 1-thread vs 2-thread or repeated-output exact equality fails in either mode:  
   `BW_Q4_THREAD_REPEATABILITY_EXACT_MISMATCH`;
2. else if any helper full matrix differs exactly from stock:  
   `BW_Q2_FULL_MATRIX_EXACT_MISMATCH`;
3. else if all full matrices match stock but any stream-compressed output differs exactly from stock-compressed reference:  
   `BW_Q3_STREAM_COMPRESSED_EXACT_MISMATCH_AFTER_FULL_PASS`;
4. else:  
   `BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS`.

No failed BW outcome may be rescued by tolerance, ULP, rounding, averaging, alternate compiler flags, majority vote or preferred case.

## Consequence firewall

- Q1 permits only consideration of a **separately preregistered full-scale execution-feasibility / Track-A successor architecture** using the exact BW helper lineage. It does not itself authorize Wm_S2 or WW.
- Q2/Q3/Q4 are preserved negative QA results; a future successor must diagnose and preregister a materially justified change before execution.
- Q5 is incomplete only.
- No Exp073BD provisional artifact can be used as scientific comparator/authority.
- No covariance/whitening/nuisance/quotient/relation/null/G8 read or claim.
- No G8 jump.
- Every BW outcome has `scientific_readiness_increment=0` and `draft_data_readiness_increment=0`.

**Readiness remains:** `Verified 52.0% | Draft/data 53.7%`.
