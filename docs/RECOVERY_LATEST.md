# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-02  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance/static QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-02_exp073cf_continuation_successor_workflow_binding_prepared.md`
2. `.github/workflows/exp073cf-continuation-successor-v0-1.yml`
3. `experiments/073cf_continuation_successor_v0_1_binding.json`
4. `recovery/2026-09-02_exp073cf_second_static_continuation_binding_audit_pass.md`
5. `ci/exp073cf_continuation_successor_v0_1.disabled.yml`
6. `recovery/2026-09-02_exp073cf_versioned_continuation_hosted_qa_pass.md`
7. `preregistration/2026-09-02_exp073cf_versioned_continuation_driver_v0_1.md`
8. `recovery/2026-09-02_exp073cf_checkpoint_sync_v0_2_hosted_qa_pass.md`
9. `recovery/2026-09-02_exp073cf_attempt2_terminal_infrastructure_incomplete.md`
10. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current frontier

Exp073CF attempt2 run `33548649445` is terminal `completed/failure` at head `f9cb1eec582276776ddac3b1207686b1e01d3b6a` and remains frozen as:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, `+0/+0`.

This is not scientific repeatability FAIL. Complete valid A/B 39-band compact comparator inputs were never both produced; comparator/finalizer were skipped.

Durable checkpoint authority remains exactly:

- A: 32/39, bands `0..31`, branch `checkpoints/exp073cf-wm-s2-a-v0-1`, head `5c7ccddb54afe1ad286d08abc6f7372aa5a11103`;
- B: 28/39, bands `0..27`, branch `checkpoints/exp073cf-wm-s2-b-v0-1`, head `ce9189a1ccaabc62708f753897b9cab5f51cb9f4`.

Local-only attempt2 bands beyond those heads are non-authoritative and must be recomputed.

Both replicas completed full-scale memory-stable Wm_S2 PCL under the observed home environment. A peak RSS `5652720 KiB`, B peak RSS `5606320 KiB`; both PCL exits were 0. Infrastructure evidence only.

## Checkpoint transport repair

Checkpoint sync v0.2 helper commit: `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`.

Immutable hosted QA: run `33577308398`, job `100083999324`, artifact `9827093387`, digest `sha256:b39a57c5e6caea56a803f5e0756b873910566d2215c7c675a8f12200b4fb1992`, terminal PASS, `+0/+0`.

The v0.2 transport distinguishes verified ABSENT from unknown transport failure, avoids persistent local checkpoint refs, uses compare-and-push lease, independently verifies post-push exact remote head, and exact-pins restore.

## Versioned continuation driver — hosted QA PASS

Prospective preregistration commit: `36853b723b172a6038c6d3023805f08f37ffac72`.

Continuation wrapper commit: `ce818db7ae53376ba6e5f7934c24f4c5acb3c75c` (`ci/exp073cf_continuation_wm_s2_v0_1.py`).

Synthetic compatibility test commit: `748cf7778aa9ddd441a9cb7c051a2a9491fa4262`.

Hosted workflow/head commit: `69ffe9962c17e63c79d0fbcf80439ed73ccb4815`.

Immutable hosted run `33585095288`, job `100107489860`, `ubuntu-latest`, completed/success. Artifact `9829783026`, digest `sha256:b8324bc9305b02ad08326117d8f2f7cb6e2c78ec5fb473b03c3f23ff3d8f2f36`.

Terminal status: `EXP073CF_CONTINUATION_V0_1_SYNTHETIC_COMPATIBILITY_PASS`, classification `SYNTHETIC_NONCLASSIFYING_INFRASTRUCTURE_QA`, readiness `+0/+0`.

The wrapper preserves historical payload `source_commit=f9cb1eec...` and historical `checkpoint_sync_commit=96886916...`, records continuation provenance separately, and routes subsequent checkpoint pushes through v0.2 only. Hosted synthetic QA demonstrated historical-form A/B contract restore/validation and fail-closed negative cases. It does not classify real-survey Wm_S2 repeatability.

## Second static continuation binding/integration audit — PASS

Concrete non-executable audit object: `ci/exp073cf_continuation_successor_v0_1.disabled.yml`.

- initial spec commit: `c8659fdf49999f8db623b0088b25b56d53efa994`;
- strengthened binding assertions commit: `05cbcecc57975187cb1dffcf5295876aee6bec61`;
- audit recovery commit: `5798b0d76524a3b860071e5bef22273a914cf978`.

Verdict: `PASS_EXP073CF_SECOND_STATIC_CONTINUATION_BINDING_INTEGRATION_AUDIT_V0_1`, classification static/infrastructure, `+0/+0`.

## Real continuation successor workflow/binding — PREPARED, NOT AUTHORIZED

Real workflow path: `.github/workflows/exp073cf-continuation-successor-v0-1.yml`.

Workflow commit: `93ac80426c877c4769ded24fb16196fcfa2501f5`.

Prospective binding path: `experiments/073cf_continuation_successor_v0_1_binding.json`.

Binding commit: `1a9f34f87d4e485b00b073e1a75eafd90b0cbe5c`.

Binding state is `PREPARED_NOT_AUTHORIZED`; `scientific_contract_changed=false`.

The workflow exact-pins A/B restore through checkpoint sync v0.2, invokes only the versioned continuation wrapper for resumed heavy computation, preserves threads=8, max-parallel=1, fresh memory-stable PCL, network-hardened exact DES size/SHA checks, frozen compile/preflight, <=60 s heartbeat, exact comparator/finalizer bodies and no-rescue semantics.

The required activation file `ci/exp073cf_continuation_successor_v0_1.activation.json` is intentionally absent. Therefore the existence of the workflow/binding does **not** authorize self-hosted execution. No run was triggered by preparation.

## Preserved scientific authority

- **Exp073BJ** run `33379013167`: terminal Track-A exact Wm_S1 authority PASS; artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ**: permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD**: `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV**: source-lineage PASS.
- **Exp073BW**: exact streaming-equivalence PASS.
- **Exp073BZ**: remote checkpoint/failover exact-byte PASS.
- **Exp073CC/CD/CE**: synthetic/nonclassifying evidence only, all `+0/+0`.
- **Exp073CF attempt1/attempt2**: infrastructure incomplete, `+0/+0`.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Coordination state

Repository-wide checks before and after workflow/binding preparation showed queued runs `0` and in-progress runs `0`. No self-hosted scientific successor has been activated.

## Exact next gate

Perform a final read-only/static audit of the actual workflow commit `93ac80426c877c4769ded24fb16196fcfa2501f5` and binding commit `1a9f34f87d4e485b00b073e1a75eafd90b0cbe5c` against the passed disabled specification. Audit activation fail-closed semantics, exact A/B restore roots, historical-vs-continuation provenance separation, frozen helper lineage, DES exact binding, PCL/compile/preflight, heartbeat, comparator/finalizer bodies, artifact naming and absence of any active collision.

Only after a PASS may a **separate prospective activation/trigger authorization** be prepared. Before that activation, repeat repository-wide `queued=0` / `in_progress=0` checks. Do not launch DSIR-HOME-PC merely because the workflow and binding exist.

- ✅ Exp073CF attempt2 remains infrastructure incomplete, not scientific FAIL.
- ✅ Durable checkpoint authority preserved exactly: A `32/39`, B `28/39`.
- ✅ Checkpoint sync v0.2 hosted QA PASS, `+0/+0`.
- ✅ Versioned continuation wrapper hosted synthetic compatibility QA PASS, `+0/+0`.
- ✅ Second static continuation binding/integration audit PASS, `+0/+0`.
- ✅ Real successor workflow and prospective binding prepared, not activated, `+0/+0`.
- 🟡 Final actual-workflow/binding static audit remains open.
- ❌ No complete A/B Wm_S2 comparator inputs; no repeatability classification.
- ❌ Exp073AQ permanent scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Home runner = NOT ACTIVE / no new self-hosted frontier authorized. Verified: 52.0% | Draft/data: 53.7%**
