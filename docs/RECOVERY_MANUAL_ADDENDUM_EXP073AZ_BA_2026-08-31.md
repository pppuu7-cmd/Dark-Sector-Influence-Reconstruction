# DSIR Recovery Manual Addendum — Exp073AZ / Exp073BA low-memory authority succession

**Date:** 2026-08-31  
**Scope:** DSIR Article-3 angular execution authority only.  
**Readiness:** strict Article-3 readiness remains `52%`.

## Why this addendum exists

The old `controlled_single_thread_exact_v1` successor route reached a valid hosted exact-repeatability FAIL at Exp073AQ Wm_S1. The failure is permanent and blocks Wm_S2 under that route.

A new route was therefore prospectively defined instead of relaxing the exact criterion. Its candidate authority class is:

`low_memory_general_coupling_deterministic_v1`.

## Permanent predecessor FAIL

Read first:

`recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`.

Never reinterpret the ~`2.08e-17` maximum AQ discrepancy as a pass. Exact SHA and `numpy.array_equal` were frozen requirements and failed.

## Low-memory algorithm

At `L=12288`, stock spin-2 full unbinned workspace is too large for the 4-GiB local execution cgroup. The successor route uses public PyMaster/NaMaster 2.7 scalar general-coupling matrices.

### Wm

From the admitted mask PCL:

`G02 = get_general_coupling_matrix(PCL,0,2,0,2)`.

Keep only one `L x L` heavy matrix. Compress by deterministic fixed-order summation to

`A[39,L]`.

Delete G02.

Compute compact binned matrix K by deterministic fixed-order column-band sums and finalize:

`W = solve(K,A)`.

Selected Wm authority remains `TE <- TE`, `<f8 [39,12288]`.

### WW

Sequentially compute, never simultaneously:

`Gsame = get_general_coupling_matrix(PCL,2,2,2,2)`

and

`Gflip = get_general_coupling_matrix(PCL,2,-2,2,-2)`.

Each is compressed immediately to `[39,L]` and the heavy matrix is freed.

Then

`Aplus=(Asame+Aflip)/2`,

`Aminus=(Asame-Aflip)/2`.

Build only the compact EE/BB system and finalize the selected `EE <- EE` block. No stock `4L x 4L` unbinned workspace is allocated.

## Exact authority decomposition

A task can pass only through exact stages:

1. two independently executed real mask-PCL replicas exact SHA + `numpy.array_equal`;
2. two independent compact general-coupling replicas exact SHA + `numpy.array_equal`;
3. two fresh finalizer processes exact SHA + `numpy.array_equal`;
4. only then task authority PASS.

No tolerance, ULP, rounding, preferred replica, majority vote, AQ targeting or closeness criterion exists.

## Exp073AZ — current active gate

Preregistration commit:

`279e09696263432def4ce20c15752b4832bba298`.

Implementation commit:

`d77b7ba88801f6788f3d386e72b445c7859c7153`.

Qualification workflow commit:

`7ba874e48a7c3e6509d114745a301e63a06229a2`.

Workflow-freeze commit:

`f49b9ab07b5d59eb0c6f275d8fa862bc4daeb089`.

Trigger/head:

`0a9581e19f7f010e13bf9aa88307b1940d0105de`.

Run:

`33339663991`.

At the latest checkpoint:

- selftest `99332875031` completed/success;
- Wm_S1 PCL replica A `99332874913` running;
- Wm_S1 PCL replica B `99332875116` running.

Do not infer PASS from selftest. The real PCL exact comparator is classifying for route qualification.

## Exp073BA — frozen contingent production gate

Preregistration commit:

`b445066a36c838b18e4cea2ca56f2f6abee56406`.

Comparator commit:

`a0b5bd8065c590e20c648215b8d993452fb7339c`.

Workflow commit:

`fc0ca8b4c0e31673c1470418060a95ac507b3759`.

Workflow-freeze commit:

`f9f19f80ed62090b22d69e6a667ea96fc7cf1f82`.

There is no trigger yet.

If AZ exact PCL PASSes, create `experiments/073ba_article3_low_memory_wm_s1_az_binding_v0_1.json` binding the immutable AZ run/job/artifact/digest and canonical PCL SHA. Then and only then create BA trigger.

If BA full final PASSes, Wm_S1 is admitted under `low_memory_general_coupling_deterministic_v1`, +0 readiness, and Wm_S2 may then be separately preregistered.

## Remaining task order

Never leapfrog:

`Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

Each task must have its own exact authority. Only all 14 admitted angular authorities can feed real Exp073AR; only then can real Exp073AS create the complete immutable 1410-row pre-support candidate manifest.

## Scientific accounting

All route qualification and individual angular task PASSes give `+0` readiness. The strict readiness stays 52% until the previously frozen real-candidate-manifest accounting gate is legitimately reached.

All Layer-A/B thresholds and anti-leakage firewalls remain unchanged.
