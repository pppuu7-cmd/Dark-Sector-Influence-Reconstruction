# DSIR recovery checkpoint — Exp073AZ low-memory qualification active; Exp073BA frozen

**Date:** 2026-08-31 (+03:00)  
**Project:** DSIR only. RTK/RQIR excluded.  
**Strict Article-3 readiness:** `52%`.

## Immutable predecessor

Exp073AQ run `33327372191` is terminal hosted authority:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

This FAIL remains permanent. Wm_S1 is not admitted under `controlled_single_thread_exact_v1`, Wm_S2 is blocked, and no tolerance/rounding/ULP/preferred-replica rescue exists.

Authority details remain in:

`recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`.

## Low-memory route rationale

A true local stock NaMaster NSIDE=4096 WW test hit the model execution cgroup hard ceiling of 4 GiB. The failure was `LOCAL_INFRASTRUCTURE_OOM_BENCHMARK_ONLY`, not scientific/numerical FAIL.

Independent algebraic validation established a memory-reduced MASTER construction based on public PyMaster/NaMaster 2.7 `get_general_coupling_matrix`:

- one scalar `[12288,12288]` general matrix at a time (~1.125 GiB float64);
- deterministic fixed-order compression to `[39,12288]`;
- Wm: one `(0,2;0,2)` general matrix;
- WW: sequential `(2,2;2,2)` and `(2,-2;2,-2)` general matrices, then parity plus/minus reconstruction;
- compact binned MASTER solve only after heavy matrices are released.

Small-resolution real NaMaster diagnostics reproduced the stock selected windows at ~machine precision and repeated identical-input general matrices bitwise exactly. These diagnostics are nonclassifying and +0 readiness.

## Exp073AZ authority succession

Prospective preregistration:

`experiments/073az_article3_low_memory_general_coupling_authority_v0_1_prereg.md`

commit:

`279e09696263432def4ce20c15752b4832bba298`.

Candidate successor class:

`low_memory_general_coupling_deterministic_v1`.

Implementation:

`ci/exp073az_article3_low_memory_general_coupling_v0_1.py`

commit:

`d77b7ba88801f6788f3d386e72b445c7859c7153`.

Qualification workflow:

`.github/workflows/exp073az-article3-low-memory-general-coupling-qualification-v0-1.yml`

workflow commit:

`7ba874e48a7c3e6509d114745a301e63a06229a2`.

Workflow freeze commit:

`f49b9ab07b5d59eb0c6f275d8fa862bc4daeb089`.

Trigger/head:

`0a9581e19f7f010e13bf9aa88307b1940d0105de`.

Hosted run:

`33339663991`.

At this checkpoint:

- selftest job `99332875031`: completed/success;
- PCL replica A job `99332874913`: IN_PROGRESS at real Wm_S1 mask-PCL computation;
- PCL replica B job `99332875116`: IN_PROGRESS at real Wm_S1 mask-PCL computation;
- selftest artifact `9740152065`, digest `sha256:16a15e517adafb4d968b14362a5b7a14b4fbe36c9deb7b981d032e912c2d7465`;
- no classifying PCL comparator authority yet.

Exp073AZ first requires the two real NSIDE=4096 Wm_S1 mask-PCL replicas to be bitwise identical. PASS token:

`PASS_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1`.

A complete mismatch is:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1`.

Failure before comparator is infrastructure-INCOMPLETE.

## Exp073BA prospectively frozen before AZ result

Preregistration:

`experiments/073ba_article3_low_memory_wm_s1_production_v0_1_prereg.md`

commit:

`b445066a36c838b18e4cea2ca56f2f6abee56406`.

Exact comparator:

`ci/exp073ba_compare_low_memory_wm_s1_v0_1.py`

commit:

`a0b5bd8065c590e20c648215b8d993452fb7339c`.

Production workflow:

`.github/workflows/exp073ba-article3-low-memory-wm-s1-production-v0-1.yml`

workflow commit:

`fc0ca8b4c0e31673c1470418060a95ac507b3759`.

Workflow freeze:

`experiments/073ba_article3_low_memory_wm_s1_production_v0_1_workflow_freeze.md`

freeze commit:

`f9f19f80ed62090b22d69e6a667ea96fc7cf1f82`.

**No BA trigger exists.** BA is forbidden unless AZ first produces a valid exact PCL PASS. If AZ PASSes, a separate immutable binding receipt must freeze AZ run/job/artifact/digest and canonical PCL SHA before BA trigger.

BA frozen sequence:

1. two independent Wm_S1 compact general-coupling replicas from the same admitted AZ PCL;
2. exact compact SHA + `numpy.array_equal` comparator;
3. only on compact PASS, two fresh finalizers;
4. exact final selected-window SHA + `numpy.array_equal` comparator;
5. only full PASS yields `PASS_EXP073BA_WM_S1_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1` and class `low_memory_general_coupling_deterministic_v1`.

Even BA PASS gives +0 readiness. Only then may Wm_S2 be separately preregistered/executed.

## WW semantics audit

For the current source-count maps, `NmtField` is a standard map-based field, not `NmtFieldCatalog`; therefore `Nw=0`. The implemented same-bin WW expression `alm2cl(mask_alms,mask_alms)-Nw` is numerically the standard mask PCL and introduces no extra correction.

## Current resume rule

1. Re-check Exp073AZ run `33339663991`.
2. If exact PCL PASS: freeze AZ binding receipt and trigger already-frozen Exp073BA.
3. If exact PCL FAIL: preserve FAIL; do not run BA; diagnose harmonic-stage determinism separately.
4. If infrastructure-INCOMPLETE: repair prospectively without converting it to repeatability FAIL.
5. Wm_S2 remains blocked until a valid BA Wm_S1 successor PASS.
6. Article-3 readiness remains 52%; no route qualification or individual angular authority earns readiness credit.
