# Article-3 exact NaMaster 2.7 AQ path audit and Exp073BL result — 2026-08-31

**Project:** DSIR only.  
**Classification:** nonclassifying source/root-cause/numerical QA.  
**Scientific readiness increment:** `+0`.  
**Draft/data readiness increment:** `+0`.

## 1. Exact NaMaster release inspected

GitHub release `v2.7` was published 2026-02-24. The exact tagged source, not current master, was inspected.

Python `NmtWorkspace.get_bandpower_windows()` in `pymaster/workspaces.py` calls the C wrapper `lib.get_bandpower_windows(...)` after requiring the unbinned matrix.

In exact tagged `v2.7` `src/nmt_master.c`, `nmt_compute_bandpower_windows`:

1. builds a binned-by-unbinned matrix by fixed nested loops over class, band and ell;
2. computes an inverse of the already-LU-decomposed binned MCM using
   `gsl_linalg_LU_invert(w->coupling_matrix_binned, w->coupling_matrix_perm, inv_mcm)`;
3. forms the bandpower windows using
   `gsl_blas_dgemm(CblasNoTrans, CblasNoTrans, 1, inv_mcm, mat_coupled_bin, 0, bpw_win)`.

The binned coupling matrix itself is LU-decomposed earlier by

`gsl_linalg_LU_decomp(w->coupling_matrix_binned, w->coupling_matrix_perm, &sig)`.

Therefore the historical Exp073AQ stock path contains explicit GSL LU and BLAS matrix-multiplication stages after the unbinned coupling matrix is constructed. This is the precise AQ-relevant source path; it replaces the earlier, weaker inference from current NaMaster master.

This does not yet identify which internal stage caused AQ's exact mismatch. The unbinned MCM construction, GSL LU/inversion and GSL BLAS multiplication are all candidates until isolated by further QA.

## 2. Relation to numerical-dispatch evidence

Local real-DES tests already proved that changing a runtime linear-algebra microkernel alone can change a full `[39,12288]` window at absolute scale `~2.8e-17`, comparable to AQ's frozen `2.08e-17` maximum mismatch.

The exact v2.7 source now confirms that AQ's actual stock bandpower-window path includes explicit low-level linear algebra (`gsl_linalg_LU_invert`, `gsl_blas_dgemm`). Thus a numerical-runtime-dispatch mechanism is technically present in the real AQ path, although causation remains unassigned between this stage and upstream unbinned-MCM construction.

## 3. Exp073BL prospective fixed-LU cross-host QA

Preregistration commit:

`e64353c6931a46ab952d7fe3df84196275b5c999`

Implementation commit:

`0241f1ff5f0ced07b65b887479ee869e2ba6a222`

Workflow commit:

`663b621f268773bcb9664faed7cb87669a41bca8`

Trigger/head:

`197ed792e73b4bd20e72ba03bdd91c4a522c4636`

Hosted run:

`33384216758`

Replica jobs:

- A `99463065082` — AMD EPYC 7763;
- B `99463065021` — AMD EPYC 7763;
- C `99463064862` — AMD EPYC 9V74;
- D `99463065089` — AMD EPYC 7763.

Comparator job:

`99463163837`

Comparator artifact:

- ID `9754932707`;
- digest `sha256:4aa0faf43a12957e0ad29309f34b7cada713ceee5eb2c3750efe570eb1e4bdd0`.

Terminal status:

`BL_Q1_FIXED_LU_EXACT_CROSSHOST_PASS`.

All four complete W arrays were `numpy.array_equal` and byte-SHA identical:

`f3a22c35dff1f3b27f5f22e7966c1c926fbbc3a965293f88a9bf0b84fa97cf79`.

All four had the same deterministic pivot permutation, identity `0..38` for this real Wm_S2 K.

All four produced exactly the same structural diagnostic:

- `max(abs(WQ-I)) = 1.2212453270876722e-15`.

All four produced exactly the same fixed-order residual on frozen probe columns `[0,29,30,272,309,967,3035,6508,10821,12287]`:

- max absolute residual `3.2526065174565133e-19`;
- relative L2 residual `3.3191074469026453e-16`.

## 4. Meaning of Exp073BL

Exp073BL demonstrates on a real DES-derived compact matrix that the finalizer equation can be implemented with an explicitly fixed scalar operation order and remain exactly reproducible across independent hosted runs spanning at least EPYC 7763 and EPYC 9V74.

This is a stronger reproducibility result than merely pinning a BLAS package because it removes BLAS/LAPACK solve dispatch from the finalizer itself.

It is still nonclassifying QA:

- it uses the provisional Exp073BD Wm_S2 compact payload;
- it does not authorize Wm_S2;
- it does not repair Exp073AQ;
- it does not modify active Exp073BJ;
- it gives `+0/+0`.

A future scientific successor may use this algorithm only after a separate prospective authority preregistration and an equivalence/accuracy contract frozen before data-dependent classification.

## 5. Current architectural implication

The remaining hard reproducibility/computational problem is increasingly isolated upstream of the finalizer:

`mask PCL -> full unbinned general coupling / MCM -> deterministic 39-row compact A`.

For future successors, two independent improvements are now supported by QA:

1. **stream/checkpoint the unbinned-coupling compression**, avoiding materialization of the full 12288x12288 object while preserving ascending-ell accumulation order;
2. **fixed-operation LU finalization**, avoiding runtime BLAS/LAPACK dispatch after compact A exists.

Together these could remove both the six-hour dense-coupling fragility and the last-bit finalizer-dispatch ambiguity, provided the row-generation equivalence is prospectively demonstrated.

## 6. Scientific accounting

`Verified: 52.0% | Draft/data: 53.7%`

Exp073AQ permanent FAIL preserved. Exp073BJ unchanged. Layer A/B, covariance/whitening, G7/G8/G9 remain unauthorized. No G8 jump.
