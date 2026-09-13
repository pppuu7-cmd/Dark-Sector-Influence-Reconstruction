# DSIR current-process ledger

Updated: 2026-09-13. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Active frontier — V0.13 replay sequencing / reproducibility audit

Authoritative active run: `34773514342`, launch commit `7c0a10a24f38966f830b7fc2438d8c134e6b5853`.

Parent authority: `docs/dsir4/authority/LAYERB_BETA_PRODUCTION_H_COMMON_GRID_INTERPOLATION_V0_12.json`, creation commit `b6f0f7e8f3042c55ba47f860cc03210d393a808b`. Parent classification: `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`; authorized next stage is strictly `NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_12_INVARIANT_FAILURE`.

Prospectively frozen V0.13 contract: `docs/dsir4/contracts/LAYERB_BETA_REPLAY_SEQUENCING_V0_13.json`, creation commit `9105ff24f4561ec61cf286425bc143d6a98aabdf`.

Executor: `ci/layerb_beta_replay_sequencing_v0_13.py`, creation commit `d1825ec35c69c3dc62a3fdd77194a52c6829f87e`, blob `83ae5ff8ebd9cf2123099b354be8b6e724186705`.

Workflow: `.github/workflows/layerb-beta-replay-sequencing-v0-13.yml`, creation commit `7e2d8803bc41ddd3645eb518775961b9f81f5c8a`.

V0.13 contains 12 independent hosted science/technical lanes: `GRID768` and `GRID1024` × `PURE_PAIR` and `INTERLEAVED` × replicas `R1/R2/R3`. The diagnostic is deliberately limited to the three V0.12 replay-failure cells plus two frozen anchor cells. It distinguishes execution-order/interleaving state dependence, cross-run parent non-reproducibility, same-profile hosted numerical nondeterminism, non-reproduced V0.12 replay failures, or a mixed/unresolved replay pattern.

At latest write 10/12 profile lanes are `in_progress`, two are queued for hosted-runner capacity, and the invariant job is queued. Do not inspect partial profile numeric results and do not alter the frozen `1e-5` replay threshold.

Frozen boundaries remain: production `h=1e-4`; scientific response threshold `<1e-3`; technical replay threshold `<1e-5`; production sampling `0.00035`; stabilized `tol_perturb_integration=1e-12`; exact requested-node binding `<=1e-12`. No full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 or science gate is authorized.

## Closed parent — V0.12 production-h interpolation audit

Run `34749034836`, head `0daf43908e276482eb3b02e45d9d93af02bc43f2`; decision job `103703327770`; decision artifact `10314853600`, ZIP SHA256 `cee9d8d9c951fab434b7b32db4a97aa62d0e684e9df625da8dceb43272f30f16`.

Classification: `PRODUCTION_H_COMMON_GRID_INTERPOLATION_AUDIT_INCONCLUSIVE`, effect `+0/+0`.

All three frozen V0.11 violation cells reproduced. At each one, pure-grid and mixed-grid cubic interpolation were identical, the mixed exact-target response matched independent direct-k TOL300, and cubic interpolation retained the parent discrepancy. Diagnostic interpolation support therefore occurred in all 3/3 offending cells; node-set-dependence support occurred in 0/3.

Formal promotion was blocked because 3 of 30 preregistered replay cells exceeded the stricter `1e-5` replay threshold, although all remained below the scientific `1e-3` threshold. The localized replay failures are: `GRID1024,h=2e-4,z=0.4175,k≈0.0122345` at `1.550639279e-4`; `GRID768,h=1e-4,z=0.62,k≈0.01551635` at `2.493437109e-5`; and `GRID1024,h=1e-4,z=0.62,k≈0.01551635` at `1.047897806e-5`.

Interpretation is intentionally limited: V0.12 provides strong diagnostic evidence for cubic interpolation at the three actual offending cells, but the frozen replay invariant prevents scientific promotion until V0.13 diagnoses those three technical replay failures.

## Anti-duplication / exact next gate

Do not launch duplicate V0.13 lanes. Wait for all 12 profile lanes plus invariant and the single decision barrier. Promote a durable V0.13 authority only after the terminal classifier is available, then follow only its encoded `next_stage`.

## Recovery/readiness

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and funnel-freeze/scientific frontier `67%`; numerical diagnostic progress alone does not raise either value. Article-II real G5 ACT×unWISE remains a separate unresolved publication gate.
