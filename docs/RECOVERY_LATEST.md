# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-31.  
**Article-3 scientific authority readiness:** **52.0%**.  
**Article-3 draft/data readiness:** **53.7%** (`53.714285714285715%` exact ledger value).  
**Article-2 repository-for-writing readiness:** **100%** for declared scope only; not G7/G8/G9 closure.

Dashboard shorthand:

`Verified: 52.0% | Draft/data: 53.7%`

Repository/hosted authority outranks chat wording. RTK/RQIR are excluded from DSIR authority/readiness.

The two Article-3 percentages are deliberately different metrics. `Scientific authority` is Track A only. `Draft/data` is an operational manuscript/data completion metric under the prospectively frozen rules in `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`; it is not evidence strength or a probability of correctness.

## Read first

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`
4. `docs/RECOVERY_MANUAL_ADDENDUM_DUAL_READINESS_2026-08-31.md`
5. `recovery/2026-08-31_dual_readiness_accounting_frozen.md`
6. `recovery/2026-08-31_exp073bb_provisional_dual_track_policy_az_active.md`
7. `docs/RECOVERY_MANUAL_ADDENDUM_EXP073BB_2026-08-31.md`
8. `experiments/073bb_article3_provisional_dual_track_evidence_policy_v0_1_prereg.md`
9. `docs/ARTICLE3_PROVISIONAL_RECOMPUTE_LEDGER_2026-08-31.md`
10. `recovery/2026-08-31_exp073bc_az_to_ba_binding_schema_preregistered.md`
11. `recovery/2026-08-31_exp073az_low_memory_qualification_active_ba_frozen.md` (historical active checkpoint; see terminal update below)
12. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
13. `experiments/073az_article3_low_memory_general_coupling_authority_v0_1_prereg.md`
14. `experiments/073ba_article3_low_memory_wm_s1_production_v0_1_prereg.md`
15. `docs/LOCAL_COMPUTE_BENCHMARK_2026-08-31.md`
16. `docs/DSIR_ALL_CHAT_REPOSITORY_RECONCILIATION_2026-08-30.md`
17. `docs/RECOVERY_MANUAL_ADDENDUM_EXP065B_EXP067E_2026-08-30.md`
18. Exp073AT/AU/AV/AW/AX addenda as needed.

## Current scientific state

- strict Article-3 scientific authority readiness = `52.0%`;
- Article-3 draft/data readiness = `53.714285714285715%` (display `53.7%`);
- Layer A = OPEN;
- Layer B = OPEN;
- covariance/whitening = BLOCKED;
- G7 = OPEN;
- G8 = OPEN;
- G9 = OPEN.

Synthetic, infrastructure, provenance, numerical-QA, route-qualification, provisional/manuscript and individual angular-authority work add `+0` scientific readiness.

### Current dual-readiness calculation

The fixed draft/data metric starts from the frozen 52-point baseline and allocates the remaining 48 points across the concrete downstream Article-3 production path.

The 14-window angular stage is worth 12 points. At present two complete angular data objects are usable for draft-data continuation:

1. Wm_S0 — complete controlled exact object from Exp073AM;
2. Wm_S1 — complete AQ A/B pair eligible for Track-P downstream sensitivity propagation while AQ remains an immutable exact repeatability FAIL.

Therefore current angular draft credit is `12 * 2/14 = 1.7142857142857142`, giving `52 + 1.7142857142857142 = 53.714285714285715%`.

No Layer-A/B/covariance/nuisance/G7/G8/G9 draft-stage credit is currently awarded. Synthetic QA and merely written workflow/governance code receive no draft-data points.

## Exp073BB — two-track operating policy

DSIR proceeds in two explicitly separated tracks.

### Track A — scientific authority

Unchanged frozen scientific authority. Only Track A can satisfy real prerequisites, create scientific PASS, or change scientific authority readiness. Historical scientific/computational FAILs remain immutable.

### Track P — provisional research/manuscript

Complete numerically non-identical replicas may be propagated downstream for exploration, sensitivity analysis, prioritization and working Article-3 drafting.

Every provisional object must have:

- `authority=false`;
- `provisional=true`;
- `scientific_pass_claimed=false`;
- `readiness_increment=0` for scientific readiness;
- `recompute_before_final_submission=true` until later Track-A supersession;
- all complete replicas propagated;
- no preferred-replica selection.

Classes:

- `P1 PROVISIONAL_BRANCH_ROBUST_MANUSCRIPT_ELIGIBLE`: every complete branch preserves the same frozen qualitative conclusion; may orient the working manuscript with explicit provisional wording;
- `P2 PROVISIONAL_NUMERICALLY_SENSITIVE_RECOMPUTE_PRIORITY`: branch spread changes sign/order/gate/discrete class or reaches an unresolved threshold; not a positive article claim;
- `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`: incomplete/missing/malformed branch; cannot propagate.

Numerical article values use explicit branch values or branch `[min,max]` envelope. Never silently choose A/B because it is smoother or more favorable.

Hosted Exp073BB governance QA:

- run `33340993757`;
- job `99336479836`;
- artifact `9740524091`;
- digest `sha256:e5224a91110f9a0cf73e4254837a9cfca6f4f7fc3115d065207d6239fd219c2a`;
- token `PASS_EXP073BB_PROVISIONAL_DUAL_TRACK_POLICY_SYNTHETIC_V0_1`;
- `16/16` frozen tests PASS;
- +0 scientific readiness.

Durable provisional/exact-recompute ledger:

`docs/ARTICLE3_PROVISIONAL_RECOMPUTE_LEDGER_2026-08-31.md`.

## Exp073AQ — permanent hosted repeatability FAIL, provisional branches preserved

Frozen run `33327372191` authority remains:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Comparator authority artifact `9739725913`, digest `sha256:5184bb3034bd2c1bd497ad30db3dbd4e1550d09a0c25af328cdee553385fef03`.

Frozen exact facts:

- `array_equal=false`;
- SHA equality=false;
- A selected-window SHA `979c61faea99cf60146078ccdd5a9c75547dcc5a689ee48c4c5f309cf6a10b69`;
- B selected-window SHA `5b02a691607dd21ede7601f081767ac3713e300abd5a9e358e4593a6ec486225`;
- differing entries `472997/479232`;
- differing bands `39/39`;
- max absolute difference `2.0816681711721685e-17`.

No tolerance/ULP/rounding/preferred-replica/majority-vote rescue exists. AQ is never erased or reclassified.

For Track P only, both complete A/B arrays may be propagated together. Input-level diagnostics:

- `max|W| = 0.04906169081530385`;
- `max|delta|/max|W| = 4.2429605188470844e-16`;
- `RMS(delta)/RMS(A) = 2.193471255136272e-16`;
- sign-bit mismatches = `0`;
- zero/nonzero mismatches = `0`;
- max relative difference in per-band `sum(abs(W)) = 4.130423023448714e-16`.

Current Track-P label is only:

`PROVISIONAL_WM_S1_BRANCH_PAIR_ELIGIBLE_FOR_DOWNSTREAM_SENSITIVITY_PROPAGATION`.

It does not pre-award Layer-A/support PASS; both branches must independently cross every frozen downstream rule.

## Exp073AZ — terminal exact mask-PCL PASS, +0 readiness

Hosted run `33339663991` is now completed/success.

- PCL replica A job `99332874913`: completed/success;
- PCL replica B job `99332875116`: completed/success;
- comparator job `99338088877`: completed/success;
- authority artifact `9740703849`;
- artifact digest `sha256:3cecacff76169dd968e458db0ae70563cf8c3cb0b30d0dff4038a2c792dd3d75`;
- terminal token `PASS_EXP073AZ_WM_S1_MASK_PCL_EXACT_V0_1`;
- `array_equal=true`;
- A/B PCL SHA `2a990b06defbe9922f82b4b85ae26df09bc7881508a85b003648cb23907a5888`;
- canonical shape `[12288]`, dtype `<f8` under the frozen contract;
- scientific readiness remains `52.0%`, increment `+0`.

Exp073AQ remains permanent FAIL. AZ validates only the exact mask-PCL predecessor needed by the prospective low-memory successor route; it does not retroactively repair AQ.

The successful AZ PCL does not increase current draft/data readiness because Wm_S1 was already counted once as a complete usable draft-data object; double-counting is forbidden.

## Exp073BC / Exp073BA next Track-A step

Exp073BC binding schema was prospectively preregistered in commit `feb0e070ee4b2e766ec7d98d964ca71c7929b7dd` before the terminal AZ metadata were filled.

A future immutable BC receipt may now bind the hosted AZ PASS metadata to the already-frozen Exp073BA production route. It is a nonclassifying prerequisite and gives +0 readiness.

Exp073BA remains the frozen Wm_S1 low-memory production route:

- prereg commit `b445066a36c838b18e4cea2ca56f2f6abee56406`;
- exact comparator commit `a0b5bd8065c590e20c648215b8d993452fb7339c`;
- workflow commit `fc0ca8b4c0e31673c1470418060a95ac507b3759`;
- workflow-freeze commit `f9f19f80ed62090b22d69e6a667ea96fc7cf1f82`.

BA may be triggered only after a valid immutable BC binding receipt. BA PASS would still add +0 readiness and would admit Wm_S1 under `low_memory_general_coupling_deterministic_v1`; only then may Track A proceed prospectively to Wm_S2.

## Frozen Article-3 boundaries — unchanged in both tracks

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
- no covariance/whitening/nuisance/quotient/relation/null/G8 leakage before its authorized/provisional stage;
- exact threshold ambiguity remains `numerically_unresolved`.

## Current operating order

### Track A

1. create/freeze the valid Exp073BC hosted AZ-to-BA binding receipt using terminal AZ PASS metadata;
2. trigger the already-frozen Exp073BA Wm_S1 low-memory production;
3. if BA exact PASS: admit Wm_S1 under the new low-memory authority class, then prospectively freeze/run Wm_S2;
4. continue `Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`, each with its own exact classifying authority;
5. assemble real Exp073AR 14-window aggregate;
6. build real Exp073AS complete immutable 1410-row pre-support candidate manifest;
7. only then may the 52% scientific readiness barrier be reconsidered under the frozen accounting contract;
8. downstream remains real Layer A -> Layer B -> covariance/whitening -> nuisance quotient -> G7 -> immutable relation freeze -> fresh G8.

### Track P

1. propagate every complete non-identical replica branch rather than selecting a favorite;
2. continue provisional Wm/WW/support/geometry calculations as soon as complete branch inputs exist;
3. classify each manuscript-relevant claim P1/P2/P3 using the frozen downstream rule on every branch;
4. use only P1 for working manuscript orientation and mark it explicitly provisional;
5. place every Track-P dependency in the exact-recompute ledger;
6. when Track A later becomes available, replace/verify provisional values without deleting the historical provisional record.

## Mandatory progress reporting

After every substantive Article-3 computation/data step report both:

`Verified: XX.X% | Draft/data: YY.Y%`

Update `Verified` only under the frozen scientific authority accounting. Update `Draft/data` only under `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`.

Track P is designed to keep scientific exploration and manuscript preparation moving while Track A establishes exact reproducibility. It never raises scientific authority readiness by itself.