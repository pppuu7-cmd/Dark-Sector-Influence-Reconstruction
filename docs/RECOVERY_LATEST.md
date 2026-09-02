# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-02  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance/static QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-02_exp073cf_hosted_authorization_gate_static_audit_pass.md`
2. `.github/workflows/exp073cf-continuation-successor-v0-1.yml`
3. `experiments/073cf_continuation_successor_v0_1_binding.json`
4. `recovery/2026-09-02_exp073cf_actual_successor_static_audit_blocked_activation_gate.md`
5. `recovery/2026-09-02_exp073cf_second_static_continuation_binding_audit_pass.md`
6. `recovery/2026-09-02_exp073cf_versioned_continuation_hosted_qa_pass.md`
7. `recovery/2026-09-02_exp073cf_checkpoint_sync_v0_2_hosted_qa_pass.md`
8. `recovery/2026-09-02_exp073cf_attempt2_terminal_infrastructure_incomplete.md`
9. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current scientific frontier state

Exp073CF attempt2 run `33548649445` is terminal `completed/failure` at head `f9cb1eec582276776ddac3b1207686b1e01d3b6a` and remains frozen as:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, `+0/+0`.

It is **not** a scientific repeatability FAIL. Complete valid A/B comparator inputs were never both produced.

Durable checkpoint authority remains exactly:

- A: 32/39, bands `0..31`, branch `checkpoints/exp073cf-wm-s2-a-v0-1`, head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`;
- B: 28/39, bands `0..27`, branch `checkpoints/exp073cf-wm-s2-b-v0-1`, head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`.

Local-only bands beyond those heads remain non-authoritative. Both attempt2 replicas completed the full-scale memory-stable Wm_S2 PCL with exit 0; this remains infrastructure evidence only.

## Frozen continuation infrastructure already validated

Checkpoint transport v0.2 helper commit: `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`.

Hosted QA: run `33577308398`, job `100083999324`, artifact `9827093387`, digest `sha256:b39a57c5e6caea56a803f5e0756b873910566d2215c7c675a8f12200b4fb1992`, PASS, `+0/+0`.

Versioned continuation preregistration: `36853b723b172a6038c6d3023805f08f37ffac72`.

Continuation wrapper: `ce818db7ae53376ba6e5f7934c24f4c5acb3c75c`.

Hosted wrapper compatibility QA: run `33585095288`, job `100107489860`, artifact `9829783026`, digest `sha256:b8324bc9305b02ad08326117d8f2f7cb6e2c78ec5fb473b03c3f23ff3d8f2f36`, PASS, `+0/+0`.

The wrapper preserves historical payload `source_commit=f9cb1eec...` and historical checkpoint-sync fingerprint `96886916...`, while routing new checkpoint transport through v0.2 only.

## Repaired real successor workflow/binding — static PASS, still NOT AUTHORIZED

Workflow:

`.github/workflows/exp073cf-continuation-successor-v0-1.yml`

repaired workflow commit `d9ec433ae002c93f7ae49c1b2b5973b585f98a99`.

Binding:

`experiments/073cf_continuation_successor_v0_1_binding.json`

new binding commit `925a345a0c1a05ab18fa0d7f0e7332b8b85f48d9`.

Binding state remains `PREPARED_NOT_AUTHORIZED`; `scientific_contract_changed=false`.

The prior control-plane blocker is repaired prospectively: `workflow_dispatch` first schedules hosted job `authorize` on `ubuntu-24.04`; self-hosted `compact-replica` has `needs: authorize`. Therefore an absent/invalid activation cannot schedule `[self-hosted, Linux, X64]`.

The hosted gate exact-validates workflow commit, binding commit, activation object, frozen helper provenance, exact A/B restore heads, threads/chunk/heartbeat contract, and repository-wide collision state. Its collision check excludes only the current hosted authorization run itself and requires all other queued/in-progress DSIR runs to be zero.

The activation file `ci/exp073cf_continuation_successor_v0_1.activation.json` is still absent. No workflow run was triggered during this repair/audit.

Static verdict:

`STATIC_CONTROL_PLANE_QA_PASS_NONCLASSIFYING`, `+0/+0`.

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

Repository-wide checks before and after repair showed `queued=0`, `in_progress=0`. No self-hosted successor is authorized.

**Exact next permitted gate:** prepare a separate prospective activation/trigger authorization object bound to workflow commit `d9ec433ae002c93f7ae49c1b2b5973b585f98a99` and binding commit `925a345a0c1a05ab18fa0d7f0e7332b8b85f48d9`, then perform a final read-only collision/binding audit. Do not dispatch the workflow in the same step as activation creation. Only after that final audit is PASS may a separately authorized self-hosted continuation run be triggered.

- ✅ Exp073CF attempt2 remains infrastructure incomplete, not scientific FAIL.
- ✅ Durable authority A `32/39`, B `28/39` preserved.
- ✅ Checkpoint sync v0.2 and continuation-wrapper hosted QA PASS, `+0/+0`.
- ✅ Hosted pre-self-hosted authorization-gate repair static PASS, `+0/+0`.
- 🟡 Real successor is prepared but not activated or execution-authorized.
- ❌ No complete A/B Wm_S2 comparator inputs; no repeatability classification.
- ❌ Exp073AQ FAIL and Exp073BD no-downstream preserved.
- ❌ Layer A/B through G7/G8 remain unauthorized.

**Home runner = NOT ACTIVE / no new self-hosted frontier authorized. Verified: 52.0% | Draft/data: 53.7%**
