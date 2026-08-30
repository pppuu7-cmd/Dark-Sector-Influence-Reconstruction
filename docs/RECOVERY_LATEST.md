# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-31.  
**Strict Article-3 scientific repository readiness:** **52%**.  
**Article-2 repository-for-writing readiness:** **100%** for declared scope only; not G7/G8/G9 closure.

Repository/hosted authority outranks chat wording. RTK/RQIR are excluded from DSIR authority/readiness.

## Read first

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `recovery/2026-08-31_exp073az_low_memory_qualification_active_ba_frozen.md`
4. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
5. `experiments/073az_article3_low_memory_general_coupling_authority_v0_1_prereg.md`
6. `experiments/073ba_article3_low_memory_wm_s1_production_v0_1_prereg.md`
7. `docs/LOCAL_COMPUTE_BENCHMARK_2026-08-31.md`
8. `docs/DSIR_ALL_CHAT_REPOSITORY_RECONCILIATION_2026-08-30.md`
9. `docs/RECOVERY_MANUAL_ADDENDUM_EXP065B_EXP067E_2026-08-30.md`
10. Exp073AT/AU/AV/AW/AX addenda as needed.

## Current scientific state

- strict Article-3 readiness = `52%`;
- Layer A = OPEN;
- Layer B = OPEN;
- covariance/whitening = BLOCKED;
- G7 = OPEN;
- G8 = OPEN;
- G9 = OPEN.

Synthetic, infrastructure, provenance, numerical-QA, route-qualification and individual angular-authority work add `+0` readiness.

## Exp073AQ — permanent hosted repeatability FAIL

Frozen run `33327372191` completed with authority:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Comparator authority artifact `9739725913`, digest `sha256:5184bb3034bd2c1bd497ad30db3dbd4e1550d09a0c25af328cdee553385fef03`.

Frozen facts:

- `array_equal=false`;
- SHA equality=false;
- A selected-window SHA `979c61faea99cf60146078ccdd5a9c75547dcc5a689ee48c4c5f309cf6a10b69`;
- B selected-window SHA `5b02a691607dd21ede7601f081767ac3713e300abd5a9e358e4593a6ec486225`;
- differing entries `472997/479232`;
- differing bands `39/39`;
- max absolute difference `2.0816681711721685e-17`.

The numerical smallness is irrelevant. No tolerance/ULP/rounding/preferred-replica/majority-vote rescue exists. Exp073AQ is never erased or reclassified.

The previous `controlled_single_thread_exact_v1` Wm_S1 route is blocked and may not launch Wm_S2.

## Low-memory execution discovery

The model execution container has an exact 4-GiB cgroup ceiling. A stock NaMaster `NSIDE=4096` WW workspace hit OOM; classification is `LOCAL_INFRASTRUCTURE_OOM_BENCHMARK_ONLY`, not scientific FAIL.

A new algebraic route was validated nonclassifying:

- use public PyMaster/NaMaster 2.7 scalar `get_general_coupling_matrix`;
- retain at most one `[12288,12288]` scalar matrix (~1.125 GiB float64) at a time;
- deterministically reduce each heavy matrix by fixed-order summation to `[39,12288]`;
- Wm requires one `(0,2;0,2)` matrix;
- WW requires sequential `(2,2;2,2)` and `(2,-2;2,-2)` matrices followed by parity plus/minus reconstruction;
- solve only the compact binned MASTER system after heavy matrices are released.

Small-resolution stock-NaMaster diagnostics reproduced selected windows at ~machine precision, and repeated identical-input general matrices were bitwise exact. These diagnostics are not tolerance authority and give +0 readiness.

## Exp073AZ — active successor-route qualification

Candidate authority class:

`low_memory_general_coupling_deterministic_v1`.

Prereg commit `279e09696263432def4ce20c15752b4832bba298`.
Implementation commit `d77b7ba88801f6788f3d386e72b445c7859c7153`.
Workflow commit `7ba874e48a7c3e6509d114745a301e63a06229a2`.
Workflow-freeze commit `f49b9ab07b5d59eb0c6f275d8fa862bc4daeb089`.
Trigger/head `0a9581e19f7f010e13bf9aa88307b1940d0105de`.
Hosted run `33339663991`.

Latest checkpoint state:

- selftest job `99332875031`: completed/success;
- PCL replica A `99332874913`: IN_PROGRESS on real NSIDE=4096 Wm_S1 mask-PCL;
- PCL replica B `99332875116`: IN_PROGRESS on the same stage;
- selftest artifact `9740152065`, digest `sha256:16a15e517adafb4d968b14362a5b7a14b4fbe36c9deb7b981d032e912c2d7465`;
- no classifying PCL comparator result yet.

Valid AZ PCL terminal classes:

- `PASS_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1`;
- `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1`.

Only exact SHA + `numpy.array_equal` PASS admits a canonical Wm_S1 PCL to the next stage. No tolerance rule exists.

## Exp073BA — fully frozen, NOT triggered

Exp073BA was preregistered and its production workflow frozen before the AZ PCL result was known.

- prereg commit `b445066a36c838b18e4cea2ca56f2f6abee56406`;
- exact comparator commit `a0b5bd8065c590e20c648215b8d993452fb7339c`;
- workflow commit `fc0ca8b4c0e31673c1470418060a95ac507b3759`;
- workflow-freeze commit `f9f19f80ed62090b22d69e6a667ea96fc7cf1f82`.

No BA trigger exists.

If and only if AZ PCL exact PASSes, first create an immutable AZ binding receipt with run/job/artifact/digest and canonical PCL SHA, then trigger BA.

BA frozen classifying sequence:

1. two independent low-memory Wm_S1 compact coupling replicas;
2. exact compact SHA + `array_equal` comparator;
3. only on compact PASS, two fresh finalizer jobs;
4. exact selected-window SHA + `array_equal` comparator;
5. final PASS token `PASS_EXP073BA_WM_S1_LOW_MEMORY_GENERAL_COUPLING_EXACT_V0_1`;
6. authority class `low_memory_general_coupling_deterministic_v1`.

Even BA PASS gives +0 readiness. Wm_S2 remains forbidden until full BA Wm_S1 PASS.

## Frozen Article-3 boundaries — unchanged

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid row fraction `<=0.05` inclusive;
- final retained observation dimension `>=15`;
- DES `NSIDE=4096`;
- true ell `0..12287`, 39 frozen bands;
- Wm `TE <- TE`, WW `EE <- EE`;
- canonical selected window `<f8 [39,12288]`;
- positive absolute operator/window envelope only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k or fiducial-P shortcut;
- no covariance/whitening/nuisance/quotient/relation/null/G8 leakage before its authorized stage;
- exact threshold ambiguity remains `numerically_unresolved`.

## Current authorized order

1. resolve Exp073AZ Wm_S1 exact mask-PCL gate;
2. if AZ PASS: freeze binding receipt and trigger already-frozen Exp073BA;
3. if BA exact PASS: Wm_S1 is admitted under the new low-memory authority class, then prospectively freeze/run Wm_S2;
4. continue `Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`, each with its own exact classifying authority;
5. assemble real Exp073AR 14-window aggregate;
6. build real Exp073AS complete immutable 1410-row pre-support candidate manifest;
7. only then may the 52% readiness barrier be reconsidered under the frozen accounting contract;
8. downstream remains real Layer A -> Layer B -> covariance/whitening -> nuisance quotient -> G7 -> immutable relation freeze -> fresh G8.
