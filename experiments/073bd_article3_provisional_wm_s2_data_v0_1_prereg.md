# Exp073BD — Article-3 provisional Wm_S2 data production v0.1 preregistration

**Project:** DSIR only. RTK/RQIR excluded.  
**Track:** Exp073BB Track P only.  
**Authority:** false.  
**Scientific readiness:** 52.0% before/after; `+0`.  
**Purpose:** produce a complete two-branch Wm_S2 angular data object for provisional downstream sensitivity propagation and working Article-3 drafting while Track A resolves Exp073BA Wm_S1.

## Frozen separation from Track A

This experiment cannot satisfy, replace, skip, or modify any Track-A prerequisite. In particular it cannot admit Wm_S2 scientific authority before a full exact Exp073BA Wm_S1 PASS and a separately prospective future Wm_S2 Track-A preregistration. Exp073AQ remains permanent FAIL.

No result from Exp073BD may be called a scientific PASS. `scientific_pass_claimed=false`, `authority=false`, `readiness_increment=0`, and `recompute_before_final_submission=true` are mandatory.

## Frozen numerical/physical contract

Use the unchanged low-memory implementation `ci/exp073az_article3_low_memory_general_coupling_v0_1.py` at its frozen implementation lineage, with:

- real DES Y1 R1 mask authorities;
- real DES Y1 lens mask;
- `NSIDE=4096`, RING;
- ell `0..12287` inclusive;
- 39 frozen bandpowers;
- task exactly `Wm_S2`;
- Wm selected response `TE <- TE`;
- PyMaster/NaMaster 2.7 lineage;
- selected window `<f8 [39,12288]`;
- fixed-order low-memory row accumulation;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- no support/covariance/whitening/nuisance/quotient/relation/null/G8 read.

Thread controls are exactly:

`OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`, `VECLIB_MAXIMUM_THREADS=1`, `BLIS_NUM_THREADS=1`, `OMP_DYNAMIC=FALSE`.

## Frozen branch rule

Two independent hosted branches A and B are required. Each branch independently computes:

`mask PCL -> low-memory compact general coupling -> final selected Wm_S2 window`.

No branch may consume numerical output from the other. No averaging, preferred replica, tolerance, ULP, rounding, clipping, smoothing, majority vote, or closeness-to-prior route is allowed.

If both final branch windows are complete, finite, shape `[39,12288]`, and every band has positive `sum(abs(W))`, the pair receives only the provisional input class:

`PROVISIONAL_WM_S2_BRANCH_PAIR_ELIGIBLE_FOR_DOWNSTREAM_SENSITIVITY_PROPAGATION`.

This class does not assert downstream Layer-A or manuscript-claim robustness. Later downstream quantities must be propagated separately on both branches; only then can a claim become P1/P2 under Exp073BB.

If either branch is incomplete/malformed, class is `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and earns zero draft-data credit.

## Exact diagnostics

After both branches complete, compare final arrays exactly and record:

- `numpy.array_equal`;
- canonical `<f8` SHA for each branch;
- differing entry count;
- differing band count;
- maximum and mean absolute difference;
- RMS(delta)/RMS(A) when defined;
- sign-bit mismatches;
- zero/nonzero mismatches;
- per-band absolute normalization spread.

Exact equality is useful diagnostics but does not convert this Track-P experiment into Track-A authority.

## Dual readiness accounting

Under `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`, only a complete two-branch final Wm_S2 object eligible for sensitivity propagation earns the angular object credit `12/14 = 0.8571428571428571` draft-data percentage points. Scientific readiness remains 52.0%.

At current baseline `Draft/data = 53.714285714285715%`, a successful complete Exp073BD branch pair would yield `54.57142857142857%` (display 54.6%) without altering Track A.
