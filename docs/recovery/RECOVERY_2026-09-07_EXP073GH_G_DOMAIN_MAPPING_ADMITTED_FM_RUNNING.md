# DSIR recovery — Exp073GH G_DOMAIN_MAPPING admitted while Exp073FM remains running

Date: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

## Authoritative WW process remains unchanged

Exp073FM `WW_S1_S1` remains the sole live heavy process:
- workflow/run `34050657030`;
- home job `101533574294`;
- head `f0caca0c3e812710e5958ee13348a150d045a7d8`;
- live state: `IN_PROGRESS` in the frozen A/B durable-checkpoint science step;
- runner owner: `DSIR-HOME-PC` exclusively by job `101533574294`;
- checkpoint namespaces `checkpoints/exp073fm-ww-s1-s1-a-v0-1` and `checkpoints/exp073fm-ww-s1-s1-b-v0-1`;
- partial numerical output and checkpoint progress were not inspected.

No competing home/self-hosted science was launched.

## Newly admitted DSIR-4 gate authority

The independent DSIR-4 C0/C1 analytic residual-mapping branch advanced from mapping readiness to a narrowly scoped scientific gate authority.

Frozen source identities used by the repaired admission:
- `experiments/073gh_dsir4_c0_c1_domain_mapping_admission_v0_1_prereg.md` blob `aff3ba121909642b0671287761155f0b3eacc4b6`;
- `docs/dsir4/DSIR4_COMMON_RESIDUAL_CONVENTION_V0_1.md` blob `9ab68fe254891a076e24757de724e32e2190bfb6`;
- `docs/dsir4/mappings/C0_C1_ANALYTIC_RESIDUAL_MAPPINGS_V0_1.md` blob `f080b8cec3197d8852a68e7de7e2183d2c7c6b50`;
- C0 mapping blob `46e9a402a57aee7baa4649784e868013ea6a07bb`;
- C1 mapping blob `cec09e097aa8650f488276ed21e949f34e4f4ac1`;
- validator blob `de0bce5e3e96d20e7a56e546cecfb846289b2f5c`.

### Historical Exp073GH v0.1 infrastructure/static failure — immutable +0/+0

Run/job `34060870654 / 101561036784`, head `f4d9d2e34d72415dda4b70522e63703c549840c4`, failed before any new scientific result was created. The first causal failure was the exact-line transport check `grep -aFx` against timestamp-prefixed GitHub job logs. The scientific mapping artifacts, domain, residual convention and validator were not changed.

Minimal repair: workflow-only log-token matching changed to timestamp-tolerant fixed-substring matching (`grep -aF`) while preserving every frozen scientific identity and criterion. Repair/install commits: `5ca0d66050d86d4f62d801310160fccf1f627008` then activation head `000641a05b962e53ce5b9e8f2feafe20ff312d1b`.

Classification of v0.1: `INFRASTRUCTURE_LOG_TRANSPORT_FAIL_PLUS_0_PLUS_0`. It created no authority and is never reinterpreted as science.

### Repaired Exp073GH v0.2 — raw-log verified admission

Run/job `34060904951 / 101561132087`, head `000641a05b962e53ce5b9e8f2feafe20ff312d1b`, completed SUCCESS and its raw job log was independently inspected.

Exact emitted tokens:
- `PASS_EXP073GH_C0_LCDM_G_DOMAIN_MAPPING_ADMISSION_V0_1`;
- `PASS_EXP073GH_C1_SMOOTH_W_G_DOMAIN_MAPPING_ADMISSION_V0_1`;
- `classification=SCIENTIFIC_GATE_AUTHORITY_ADMITTED`;
- `admitted_gate=G_DOMAIN_MAPPING`;
- `scientific_model_authority_created=false`;
- `full_dsir_model_pass=false`;
- `downstream_model_gates=NOT_YET_TESTABLE`.

The admission revalidated the exact DSIR domain `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`, linear regime, no quasi-static assumption and no sub-horizon assumption. Both mapping artifacts remain `mapping_ready=true`, `prediction_ready=false` and retain six nonempty residual-component expressions. C1 retains `epsilon_w=0.0001`, `w=-0.9999`, `smooth_de_control=true`.

Therefore the only newly created authority is the **G_DOMAIN_MAPPING gate** for C0 and C1. This is not full model authority, not a prediction PASS, and not a DSIR model PASS.

## Exact next actions

1. If Exp073FM becomes terminal, consume it immediately and independently verify the frozen artifact/checkpoint/source/same-object/file-backed/exact-equality contract before any classification. Only a valid candidate PASS permits canonical hosted Exp073FR admission.
2. While Exp073FM remains running, no partial FM numerical output may be inspected and no competing home computation may start.
3. DSIR-4 work may proceed only to the next prospectively frozen prediction-interface/gate that does not infer full-model authority from G_DOMAIN_MAPPING alone.
