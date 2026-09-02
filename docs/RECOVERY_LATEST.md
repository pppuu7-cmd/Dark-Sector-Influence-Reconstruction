# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-02  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance/static QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-02_exp073cf_actual_successor_static_audit_blocked_activation_gate.md`
2. `recovery/2026-09-02_exp073cf_continuation_successor_workflow_binding_prepared.md`
3. `.github/workflows/exp073cf-continuation-successor-v0-1.yml`
4. `experiments/073cf_continuation_successor_v0_1_binding.json`
5. `recovery/2026-09-02_exp073cf_second_static_continuation_binding_audit_pass.md`
6. `ci/exp073cf_continuation_successor_v0_1.disabled.yml`
7. `recovery/2026-09-02_exp073cf_versioned_continuation_hosted_qa_pass.md`
8. `recovery/2026-09-02_exp073cf_checkpoint_sync_v0_2_hosted_qa_pass.md`
9. `recovery/2026-09-02_exp073cf_attempt2_terminal_infrastructure_incomplete.md`
10. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current scientific frontier state

Exp073CF attempt2 run `33548649445` is terminal `completed/failure` at head `f9cb1eec582276776ddac3b1207686b1e01d3b6a` and remains frozen as:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, `+0/+0`.

It is **not** a scientific repeatability FAIL. Complete valid A/B comparator inputs were never both produced.

Durable checkpoint authority remains exactly:

- A: 32/39, bands `0..31`, branch `checkpoints/exp073cf-wm-s2-a-v0-1`, head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`;
- B: 28/39, bands `0..27`, branch `checkpoints/exp073cf-wm-s2-b-v0-1`, head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`.

Local-only bands beyond those heads remain non-authoritative.

Both attempt2 replicas completed the full-scale memory-stable Wm_S2 PCL: A peak RSS `5652720 KiB`, B peak RSS `5606320 KiB`; both PCL exits 0. Infrastructure evidence only.

## Frozen continuation infrastructure already validated

Checkpoint transport v0.2 helper commit: `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`.

Hosted QA: run `33577308398`, job `100083999324`, artifact `9827093387`, digest `sha256:b39a57c5e6caea56a803f5e0756b873910566d2215c7c675a8f12200b4fb1992`, PASS, `+0/+0`.

Versioned continuation preregistration: `36853b723b172a6038c6d3023805f08f37ffac72`.

Continuation wrapper: `ce818db7ae53376ba6e5f7934c24f4c5acb3c75c`.

Hosted wrapper compatibility QA: run `33585095288`, job `100107489860`, artifact `9829783026`, digest `sha256:b8324bc9305b02ad08326117d8f2f7cb6e2c78ec5fb473b03c3f23ff3d8f2f36`, PASS, `+0/+0`.

The wrapper preserves historical payload `source_commit=f9cb1eec...` and historical checkpoint-sync fingerprint `96886916...`, while routing new checkpoint transport through v0.2 only.

Second static continuation binding/integration audit passed on the non-executable design object; audit recovery commit `5798b0d76524a3b860071e5bef22273a914cf978`, `+0/+0`.

## Real successor workflow/binding — prepared but BLOCKED

Prepared workflow:

`.github/workflows/exp073cf-continuation-successor-v0-1.yml`

workflow commit `93ac80426c877c4769ded24fb16196fcfa2501f5`.

Prepared binding:

`experiments/073cf_continuation_successor_v0_1_binding.json`

binding commit `1a9f34f87d4e485b00b073e1a75eafd90b0cbe5c`.

Binding state is `PREPARED_NOT_AUTHORIZED`; `scientific_contract_changed=false`.

The actual-workflow audit found one control-plane blocker:

`workflow_dispatch` can schedule the first matrix job directly on `[self-hosted, Linux, X64]`, while the activation guard currently executes only as a step **inside** that self-hosted job. Therefore unauthorized/manual dispatch could touch DSIR-HOME-PC before failing the missing-activation check.

Verdict:

`BLOCKED_EXP073CF_ACTUAL_SUCCESSOR_ACTIVATION_GATE_PLACEMENT_V0_1`, `+0/+0`.

No workflow run was triggered during preparation or audit. The required activation file `ci/exp073cf_continuation_successor_v0_1.activation.json` remains absent.

The prepared workflow/binding commits above are **not execution authority** and must not be activated as-is.

## Required minimal repair

Prospectively revise the workflow so authorization is checked before any self-hosted scheduling. Preferred pattern:

1. `workflow_dispatch` first runs an `ubuntu-24.04` authorization job;
2. that hosted job exact-validates workflow commit, new binding commit, activation file, historical/continuation provenance and coordination conditions;
3. the self-hosted A/B matrix has `needs:` on the hosted authorization job and therefore cannot schedule when activation is absent/invalid;
4. preserve A/B `max-parallel=1`, threads=8, chunk=4, exact restore roots, v0.2 transport, wrapper-only heavy path, DES exact binding, memory-stable PCL, compile/preflight, <=60 s heartbeat, exact comparator/finalizer and no-rescue semantics;
5. because the workflow changes, create a **new** prospective binding to the repaired exact workflow commit; do not reuse binding commit `1a9f34f...` as authority;
6. only after another static PASS and fresh repository-wide `queued=0` / `in_progress=0` collision check may a separate activation/trigger authorization be prepared.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV** source-lineage PASS; **Exp073BW** exact streaming-equivalence PASS; **Exp073BZ** checkpoint/failover PASS.
- **Exp073CC/CD/CE**: synthetic/nonclassifying, `+0/+0`.
- **Exp073CF attempt1/attempt2**: infrastructure incomplete, `+0/+0`.

## Frozen Article-3 order/boundaries

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Coordination state and exact next gate

Latest repository-wide checks after preparation showed `queued=0`, `in_progress=0`. No self-hosted successor is authorized.

**Exact next permitted gate:** repair the actual successor workflow with a hosted pre-self-hosted authorization gate, then issue a new prospective binding to that repaired exact workflow commit and perform a static audit. Do not create the activation file or launch DSIR-HOME-PC until that repaired workflow/binding audit passes.

- ✅ Exp073CF attempt2 remains infrastructure incomplete, not scientific FAIL.
- ✅ Durable authority A `32/39`, B `28/39` preserved.
- ✅ Checkpoint sync v0.2 and continuation-wrapper hosted QA PASS, `+0/+0`.
- ✅ Non-executable second static integration audit PASS, `+0/+0`.
- 🟡 Real successor workflow/binding prepared but activation-gate audit BLOCKED, `+0/+0`.
- ❌ No complete A/B Wm_S2 comparator inputs; no repeatability classification.
- ❌ Exp073AQ FAIL and Exp073BD no-downstream preserved.
- ❌ Layer A/B through G7/G8 remain unauthorized.

**Home runner = NOT ACTIVE / no new self-hosted frontier authorized. Verified: 52.0% | Draft/data: 53.7%**
