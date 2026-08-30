# DSIR RECOVERY LATEST — live pointer

**Updated:** 2026-08-30.  
**Strict Article-3 scientific repository readiness:** **52%**.  
**Article-2 repository-for-writing readiness:** **100%** for declared scope; not G7/G8/G9 closure.

## Read first

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
3. `docs/RECOVERY_MANUAL_ADDENDUM_EXP073AT_2026-08-30.md`
4. `docs/DSIR_CROSS_CHAT_AUTHORITY_CONSOLIDATION_2026-08-30.md`
5. `recovery/2026-08-30_exp073at_layera_admission_hosted_pass_aq_still_running.md`

Repository/hosted authority outranks chat wording. RTK/RQIR remain excluded from DSIR authority/readiness.

## Current authority state

- Historical primary P exact Wm_S0 SHA `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f` remains historical-route authority only.
- Historical Q remains immutable `SCIENTIFIC_REPEATABILITY_FAIL`; computational repeatability, not dark-sector physics.
- Exp073AM controlled single-thread exact repeatability PASS: run `33321661835`, artifact `9735051043`, canonical Wm_S0 SHA `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`, exact A/B equality, +0 readiness.
- Exp073AN classified `DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P`; +0 readiness.
- Exp073AO defines the prospective successor authority class `controlled_single_thread_exact_v1`; no tolerance/ULP/rounding contract is authorized.
- Exp073AP real hosted decision `AUTHORIZE_EXECUTION_QUALIFIED_EXACT_SUCCESSOR_ROUTE`; +0 readiness.
- Exp073AR supersedes historical Exp073AG only for the future execution-qualified 14-window aggregate schema.
- Exp073AS supersedes historical Exp073AE only for the future execution-qualified pre-support join schema.
- Exp073AT freezes the future execution-qualified candidate-manifest -> Layer-A admission boundary while retaining the old Layer-A numerical semantics unchanged.

## Successor exact angular contract

Controlled Wm_S0 anchor:

`8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`.

Every remaining angular task requires two independent hosted replicas under exactly:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

Admission requires exact canonical SHA equality and `numpy.array_equal == True`. No tolerance, rounding, majority vote, preferred-replica selection or closeness-to-P rescue.

Remaining order:

`Wm_S1, Wm_S2, Wm_S3, WW_S0_S0, WW_S0_S1, WW_S0_S2, WW_S0_S3, WW_S1_S1, WW_S1_S2, WW_S1_S3, WW_S2_S2, WW_S2_S3, WW_S3_S3`.

## Exp073AQ — active first real controlled production gate

Frozen chain:

- prereg `2794ed0a48e8e7f8019584461296661d1a83ae08`;
- unchanged physical/angular runner `45ed8d8d1e90cdaf314e0384b6f3cdfef369925b`;
- comparator `8772ff5550351d53dfa47aeb05cd83bd6f673750`;
- workflow `42b6241dc90a253cc4d4e8f8dbf72a6a71b46c18`;
- workflow freeze `a60c7a2020843e2ea800e361e54cb13ac6c39ac4`;
- trigger/head `fe89b6c64ee0cee5dbc40080973ec2af2ae683e0`;
- run `33327372191`.

Latest inspection after Exp073AT hosted completion:

- replica A job `99299799192`: **IN PROGRESS**, exact controlled Wm_S1 computation;
- replica B job `99299799338`: **IN PROGRESS**, exact controlled Wm_S1 computation;
- no AQ artifact exists yet.

Allowed completed classifications are only:

- `PASS_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`, or
- `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

Failure before a valid comparator classification remains infrastructure-INCOMPLETE. An exact PASS admits only Wm_S1 and adds 0 readiness.

## Exp073AR — successor 14-window aggregate schema

Hosted synthetic PASS run `33327870470`, job `99301112192`, artifact `9736757853`, digest `sha256:b3d2a1195299d9daedd469dee1fb394bcfba4499abfdbd04159330566d8c76e9`, token `PASS_EXP073AR_EXECUTION_QUALIFIED_14WINDOW_AGGREGATE_SUCCESSION_SYNTHETIC_V0_1`, 24/24 cases, +0 readiness.

Future aggregate must use Exp073AM Wm_S0 plus 13 admitted exact controlled-twin hosted authorities, all under `controlled_single_thread_exact_v1`. Historical `canonical_exp073x2` / `exp073aa` future authority classes are rejected.

## Exp073AS — successor pre-support join schema

Hosted synthetic PASS run `33330144734`, job `99307146685`, artifact `9737392901`, digest `sha256:1542be1b0982916b921d4c908a2ce9d58e4a9e17c34784dc9d9b5ba4273919ff`, token `PASS_EXP073AS_EXECUTION_QUALIFIED_PRESUPPORT_JOIN_SUCCESSION_SYNTHETIC_V0_1`, 24/24 cases, +0 readiness.

Future real join must bind unchanged Exp073U/Z2/AB/W authorities to one real Exp073AR-validated `controlled_single_thread_exact_v1` 14-window aggregate and produce a complete immutable 1410-row pre-support candidate manifest. It may not use support/covariance/nuisance/G8 to choose the candidate set.

## Exp073AT — successor Layer-A admission firewall

A downstream audit found that the existing Layer-A numerical evaluator is route-agnostic but predates the execution-qualified successor route and therefore lacked a frozen provenance/completeness admission rule for a real Exp073AS manifest. Exp073AT was prospectively frozen while AQ was still running, before any AQ authority, real aggregate, real candidate manifest or real Layer-A result existed.

Frozen chain:

- prereg `507c210419223e20f77dd0c5a9ffc6f8d150b41b`;
- validator `931bb2334e901044fbbaaa6a7ddf8a6b326daf62`;
- workflow `1bf8f72a4690c0b45686a52b6e54630f2fbf7849`;
- workflow freeze `acff4891f05bb5a56acd1d8f7ef1a80cc093e77d`;
- trigger/head `d67a6ebe8cf48c416081747e2966811b46282062`;
- hosted run `33331600899`, job `99310991453`;
- artifact `9737797541`;
- digest `sha256:4eb8bb758bdf01aae6808a358220762f5b2e6d5da15b617c5d95b727b597c1f3`;
- token `PASS_EXP073AT_EXECUTION_QUALIFIED_LAYERA_ADMISSION_SYNTHETIC_V0_1`;
- 24/24 frozen synthetic cases passed.

Classification: **HOSTED SYNTHETIC PASS / provenance-release QA / non-scientific / +0 readiness**.

A future real Layer-A evaluator may receive only a complete immutable hosted candidate receipt with:

- `authority_route = controlled_single_thread_exact_v1`;
- `join_schema = exp073as_execution_qualified_presupport_join_v0_1`;
- `candidate_manifest_complete=true`;
- `support_selection_applied=false`;
- exactly 1410 rows, block counts `Wm=780`, `WW=390`, `BOSS=240`;
- Exp073U ordered-ID SHA `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
- controlled Wm_S0 anchor `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`;
- immutable hosted Exp073AS provenance and candidate metadata SHA.

Historical primary-P, old X2/Exp073AA route classes, historical Exp073AE join schema, incomplete/already-selected manifests, malformed provenance and downstream leakage are blocked.

Exp073AT does not alter or evaluate Layer-A mathematics.

## Frozen Layer-A science boundaries — unchanged

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid = 1-valid_mass/total_mass`;
- inclusive Layer-A threshold `f_invalid <= 0.05`;
- exact boundary splitting and exact-threshold ambiguity firewall;
- integer-ell sum of `abs(W_ell)` with no extra `(2ell+1)` measure;
- piecewise-linear radial integration/inverse-chi;
- positive absolute operator/window envelope only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k or fiducial-P shortcut;
- no covariance/whitening/nuisance/quotient/relation/null/G8 leakage before support selection is frozen.

## Current authorized order

`resolve Exp073AQ Wm_S1`

`-> if exact PASS, prospectively freeze/run Wm_S2 as its own controlled twin gate`

`-> continue remaining tasks only via independent exact twin admission`

`-> Exp073AM Wm_S0 + 13 admitted controlled-twin authorities`

`-> real ordered 14-window authority under Exp073AR`

`-> real complete 1410-row pre-support candidate manifest under Exp073AS`

`-> Exp073AT Layer-A admission`

`-> unchanged real Layer-A evaluator`

`-> Layer B -> covariance/whitening -> nuisance/quotient/relation/null -> fresh G8 under the frozen order`.

Strict Article-3 readiness remains **52%** until the real complete pre-support finite-operator candidate manifest exists and the prospectively frozen scientific-accounting rule authorizes the corresponding credit.
