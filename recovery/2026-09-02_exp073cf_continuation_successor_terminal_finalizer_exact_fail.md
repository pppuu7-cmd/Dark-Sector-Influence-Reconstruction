# Exp073CF continuation successor — terminal finalizer exact repeatability FAIL

**Date:** 2026-09-02  
**Scope:** DSIR Article 3 / Wm_S2 only. RTK/RQIR excluded.  
**Run:** `33601943300`  
**Head SHA:** `313a8b332dc982154eb14671e68ada9ebd2c10e5`  
**Workflow:** `Exp073CF continuation successor Wm_S2 v0.1`

## Terminal classification

The continuation successor reached complete valid replica A and replica B inputs and therefore reached the preregistered exact scientific comparator chain.

The expensive compact Wm_S2 construction is an **exact scoped PASS**, but the subsequent frozen finalizer is an **exact scientific repeatability FAIL**.

Authoritative terminal token:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073CF_WM_S2_FINALIZER_EXACT_V0_1`

This classification is not rescued by tolerance, ULP proximity, rounding, averaging, smoothing, majority vote, preferred replica, or post-hoc environment selection. The GitHub workflow's overall green conclusion is infrastructure status only: the scientific authority is the comparator payload/artifact below.

Article-3 readiness impact: `+0/+0`.  
Readiness remains **Verified 52.0% | Draft/data 53.7%**.  
No G7 authorization and no G8 jump.

## Completed self-hosted authority inputs

Hosted authorization job `100157365487`: PASS.

Replica A job `100157400671`: terminal success on `DSIR-HOME-PC`.

- restored durable A checkpoint from 32/39;
- completed all 39/39 bands;
- compact artifact `9841348367`;
- artifact digest `sha256:d6703819745b22eadc9c6557c4d89d926ed9675c09bd41cb19e79d4050ef399b`.

Replica B job `100157400821`: terminal success on `DSIR-HOME-PC`.

- restored durable B checkpoint from 28/39;
- completed all 39/39 bands;
- compact artifact `9848067175`;
- artifact digest `sha256:7e655144c07959f4ba7c6c6d82db0685b58e425958fa308e6b9e698ad6e30737`.

The durable checkpoint branches now contain 39/39 completed bands for both A and B.

## Compact exact comparator — scoped PASS

Comparator job: `100260974130`.

Frozen result:

- shape: `[39,12288]`;
- `array_equal=true`;
- PCL SHA A = B = `4d5516c56aa48b2b169512bb61a0b09ded6982249b4af41677eeac49298fca84`;
- compact canonical `<f8` SHA A = B = `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`;
- `no_tolerance_used=true`;
- status `PASS_EXP073CF_WM_S2_COMPACT_EXACT_V0_1`.

Authority artifact: `9848084775`, digest `sha256:29ac6e91f703734cfffcbffd1504fda9c861aa12dcb88822b83af50842983dd2`.

This is a real positive scoped result: the full-scale independent A/B compact Wm_S2 construction is bit-for-bit reproducible. It does **not** override the downstream finalizer failure.

## Frozen finalizers and terminal exact FAIL

Finalizer A job `100261101481`: infrastructure success.

- final artifact `9848151035`;
- artifact digest `sha256:51c89b5ebbb06138f29b51a7b871f9519aff6c9e72475825e2082610d77eef17`;
- final window SHA `fc94c71f8e004fe3340d7ab3df79a70b93d0236902e7f8d72f7387c33829de84`.

Finalizer B job `100261101527`: infrastructure success.

- final artifact `9848148422`;
- artifact digest `sha256:a124bd9c796b152cf2536f10ecdaaa2eeb67254f6f80e46aed13adb48f65a1d7`;
- final window SHA `bed762740b625f932f016d0988be17500a2583daee08bee9a5da550de786193e`.

Final exact comparator job `100261645358`:

- `array_equal=false`;
- `sha_equal=false`;
- `scientific_authority=false`;
- `no_tolerance_used=true`;
- status `SCIENTIFIC_REPEATABILITY_FAIL_EXP073CF_WM_S2_FINALIZER_EXACT_V0_1`.

Final authority artifact `9848162380`, digest `sha256:f291447e109b2149958114baa30baf37edb6aa75efe9c2b41498d88fe4e193a1`.

## Exact finalizer implementation implicated

The frozen Wm finalizer in `ci/exp073az_article3_low_memory_general_coupling_v0_1.py` is

1. `A=np.asarray(d['A'], dtype=np.float64)`;
2. deterministic fixed-order construction `K=k_from_a(A)`;
3. `W=np.linalg.solve(K,A)`;
4. canonical contiguous `<f8` output.

Because the compact A/B arrays are exactly identical before this step, the first presently plausible numerical locus is the dense linear solve / BLAS-LAPACK execution environment. This is a **hypothesis, not a classification**.

The two finalizer jobs were independent GitHub-hosted Ubuntu workers. Their logs show different Azure host regions (`westus2` for A and `westus3` for B) while using the same declared workflow and thread caps. Fresh conda environments installed NaMaster 2.7, Python 3.11, NumPy/OpenBLAS-family linear algebra. Cross-host CPU/OpenBLAS kernel dispatch is therefore a concrete diagnostic target, but causality has not yet been established.

## Descriptive magnitude audit — nonclassifying

An immediate read-only comparison of the two immutable final window arrays found differences at the level expected for floating-point solve path variation, while still violating the exact gate:

- differing entries: `392922 / 479232` (~81.99%);
- maximum absolute difference: `2.7755575615628914e-17`;
- median nonzero absolute difference: `6.617444900424221e-23`;
- mean absolute difference: `1.3838545569119878e-20`;
- median relative difference on differing entries: ~`5.19e-16`;
- maximum relative difference: ~`3.53e-10`.

ULP statistics, if inspected, are diagnostic only and **must never be used as a rescue criterion**. These magnitude observations do not change the exact FAIL token.

## Exact next permitted gate

Do **not** rerun the expensive full-scale compact A/B calculation merely to chase final bits: compact repeatability is already exactly established.

The next permitted gate is a **prospectively preregistered hosted-only finalizer determinism diagnostic** using one immutable, hash-bound compact input. It must:

- preserve Exp073CF's finalizer FAIL permanently;
- reconstruct and hash `K` before the solve;
- run the same finalizer on multiple independent hosted workers;
- capture CPU model, NumPy configuration/runtime, BLAS/LAPACK/OpenBLAS information and thread controls;
- test exact within-worker repeated solves and exact cross-worker solves;
- distinguish `K` construction nondeterminism, within-runtime solve nondeterminism, and cross-host BLAS/LAPACK dispatch nondeterminism;
- use tolerances/ULPs only descriptively, never for acceptance;
- remain diagnostic/nonclassifying `+0/+0`.

Only after the source of nondeterminism is isolated may a **new prospectively versioned deterministic finalizer** be preregistered. It may be tested as a new version, but it may not retroactively convert Exp073CF into a PASS.

## Preserved boundaries

Exp073BJ Wm_S1 exact Track-A PASS remains preserved. Exp073AQ historical scientific FAIL remains preserved. Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`. The required Article-3 order and all frozen support/invalid-fraction/dimension boundaries remain unchanged.

### Status

- ✅ Full-scale Wm_S2 A = 39/39.
- ✅ Full-scale Wm_S2 B = 39/39.
- ✅ A/B compact exact repeatability PASS.
- ❌ Frozen A/B finalizer exact repeatability FAIL.
- 🟡 Hosted-only finalizer determinism diagnosis is the next gate.
- ❌ No downstream G7/G8 authorization from Exp073CF.

**Verified 52.0% | Draft/data 53.7% | readiness delta +0/+0.**
