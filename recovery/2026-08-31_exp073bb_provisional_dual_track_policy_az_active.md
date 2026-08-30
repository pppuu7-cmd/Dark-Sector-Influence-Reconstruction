# DSIR recovery checkpoint — Exp073BB provisional dual-track policy, Exp073AZ active

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Scientific readiness:** 52%, unchanged.

## New governance state

User-directed research policy has been formalized prospectively as Exp073BB: continue scientific exploration and working-manuscript construction from complete numerically non-identical replicas without weakening Track-A scientific authority.

Frozen preregistration commit:

`d4824c1f0e111b25abe0da7e1747a8687a77a175`.

Validator commit:

`813acd62f3ea9d9009fcbfcc2c10582c15fc40d1`.

Workflow commit:

`b0cf034a2a8a1db39f465f4ff1969ceb9417bb0b`.

Workflow freeze commit:

`635da58570618273e2950d007bbfb20116811128`.

Trigger/head:

`9145269299d2de31cc2429b01fbacc9db30ce81c`.

Hosted QA:

- run `33340993757`;
- job `99336479836`;
- artifact `9740524091`;
- digest `sha256:e5224a91110f9a0cf73e4254837a9cfca6f4f7fc3115d065207d6239fd219c2a`;
- `16/16` frozen checks PASS;
- token `PASS_EXP073BB_PROVISIONAL_DUAL_TRACK_POLICY_SYNTHETIC_V0_1`;
- classification `HOSTED_SYNTHETIC_GOVERNANCE_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

## Track separation

### Track A — scientific authority

Unchanged. Exp073AQ remains permanent `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`. Only Track A can satisfy authority prerequisites or change readiness.

Current Track-A recovery path is Exp073AZ -> Exp073BA low-memory deterministic succession.

### Track P — provisional research/manuscript

Complete non-identical branches may continue downstream for exploratory science and manuscript orientation. All complete branches must be propagated; selecting a preferred replica is forbidden.

P1 `PROVISIONAL_BRANCH_ROBUST_MANUSCRIPT_ELIGIBLE`: all branches preserve the same frozen qualitative conclusion.

P2 `PROVISIONAL_NUMERICALLY_SENSITIVE_RECOMPUTE_PRIORITY`: branch spread changes sign/order/gate/discrete class or reaches an unresolved threshold.

P3 `PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`: incomplete/missing/malformed branch.

Track-P outputs always have `authority=false`, `scientific_pass_claimed=false`, `readiness_increment=0`, `recompute_before_final_submission=true` until superseded by Track A.

## Wm_S1 initial provisional item

Immutable AQ A/B arrays were inspected without selecting a preferred branch.

Input diagnostics:

- `max|delta| = 2.0816681711721685e-17`;
- `max|W| = 0.04906169081530385`;
- `max|delta|/max|W| = 4.2429605188470844e-16`;
- `RMS(delta)/RMS(A) = 2.193471255136272e-16`;
- sign-bit mismatch count `0`;
- zero/nonzero mismatch count `0`;
- max relative per-band absolute-response-norm difference `4.130423023448714e-16`.

This admits the pair only to provisional downstream sensitivity propagation; no Layer-A/support classification is inferred yet.

Durable ledger:

`docs/ARTICLE3_PROVISIONAL_RECOMPUTE_LEDGER_2026-08-31.md`.

## Exp073AZ status

Run `33339663991` remains active at this checkpoint.

- hosted selftest completed success;
- PCL replica A job `99332874913` computing Wm_S1 mask-PCL;
- PCL replica B job `99332875116` computing Wm_S1 mask-PCL;
- exact PCL comparator has not yet classified.

Do not trigger Exp073BA until AZ produces valid exact PCL PASS and the frozen BA binding receipt is created.

## Local low-memory benchmark

Full `L=12288` scalar general-coupling benchmark is running inside the 4-GiB local cgroup without OOM. Observed process RSS ~1.29 GiB after >20 minutes. This confirms memory feasibility of sequential scalar blocks but is benchmark-only and not authority.

## Manuscript rule

Working Article-3 drafting may orient around P1 provisional evidence with explicit provisional labeling and branch-envelope reporting. P2/P3 are not positive article claims. Central provisional dependencies remain in the exact-recompute ledger for later replacement/verification.

No scientific PASS/readiness increment is created by this policy.