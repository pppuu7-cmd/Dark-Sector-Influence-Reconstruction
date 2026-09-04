# Exp073BU 8-core v0.4 runner-loss classification and checkpoint-resume support chain

Date: 2026-09-04
Scope: DSIR only. Historical science is not rewritten.

## Terminal classification of Exp073BU v0.4
Authoritative science run/job `33901458494 / 101116305364`, frozen head `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`, ended with Actions run conclusion `failure` at `2026-09-04T18:30:00Z`.

All setup stages through the exact 8-thread runtime certification completed successfully. The science step `Fresh live exclusivity and Exp073BU 8-core A-then-B science` remained reported `in_progress` with no completion timestamp even though the job itself became terminal. All following `if: always()` evidence/upload/classification steps remained pending and the run has **no artifact**. The GitHub job-log blob endpoint returned `BlobNotFound`, so no terminal launcher stderr/receipt is available from Actions.

Therefore this run is classified **INFRASTRUCTURE_INCOMPLETE / runner-loss-like termination `+0/+0`**, not `SCIENTIFIC_REPEATABILITY_FAIL`. No A/B terminal comparator was produced and Wm_S3 authority remains absent. The local checkpoint root created by that frozen run remains:
`~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`.

Frozen historical checkpoint identity:
- science head `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`;
- original workflow blob `f8c70a4206321b0dc10b57f63a2a06163da2249a`;
- original contract fingerprint `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`;
- namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`.

No historical checkpoint manifest may be rewritten or rebound to a newer implementation identity.

## Validated prospective resume-support chain
All gates below are hosted support/readiness `+0/+0`; none creates Wm_S3 authority.

### Exp073DE — split historical science / repair implementation identity
Run `33908858642`, head `d4e29841cf046e1a17fedb6372f12ce4eac03372`, artifact `9950549286`, independently verified ZIP SHA256 `4b0f21f407f66659dae89e488c34ab65c56fcf4ce77fb24415272ee44b91b91e`.
Raw token: `PASS_EXP073DE_SPLIT_IDENTITY_RESUME_BINDING_V0_1`.
It prospectively requires old science head/fingerprint to validate old checkpoints while separately binding the audited newer resume implementation.

### Exp073DF — immutable legacy-complete replica passthrough
Run `33909072007`, head `00e071d94d502b4293f2eba9e5a7a49883e2d08e`, artifact `9950629085`, independently verified ZIP SHA256 `494b5f98242fef972fb632995f3553293ed452a0bc21d9da4168eeb94ca5e8c1`.
Raw token: `PASS_EXP073DF_LEGACY_COMPLETE_RESUME_PASSTHROUGH_V0_1`.
A complete legacy replica receipt can be accepted read-only only when both receipt and workspace independently prove exact cumulative mask lineage `{lens:1,source:1}`. Legacy `{0,0}` cumulative lineage is rejected.

### Exp073DG — boundary-safe full-window resume
Run `33909299159`, head `4021543896319f8bc0ec13eec48d9b789c6cb6d0`, artifact `9950710099`, independently verified ZIP SHA256 `75b8837c71f2592c5fbadd5e37ec32159e4f7e47aa7d9807da900f72523cc19f`.
Raw token: `PASS_EXP073DG_BOUNDARY_SAFE_RESUME_V0_1`.
A valid `full_window_complete` stage is never recomputed. If only `selected_te_complete` is missing, the resume code verifies the full-window SHA/shape and derives exactly `wins[0,:,0,:] = TE<-TE` into canonical `<f8 [39,12288]` with `numpy.array_equal`, then writes only the missing selected-TE stage.

### Exp073DH — masks-to-workspace cumulative lineage
Run `33909572046`, head `aa83811575464331a0e9bdc7852606125ba16320`, artifact `9950808508`, independently verified ZIP SHA256 `e0803731b8c6b76aaf6d1295e9cb9f625355f5ca6258bbb5f0c95652c33182a1`.
Raw token: `PASS_EXP073DH_MASK_WORKSPACE_LINEAGE_RESUME_V0_1`.
When resuming from a valid `fresh_masks_complete` boundary, the newly created workspace manifest records immutable cumulative `{lens:1,source:1}` only after verifying the stored mask checkpoint identity and both canonical mask SHA values. Invocation-local `{0,0}` is not substituted for cumulative lineage.

### Exp073DI — persisted adapter runtime provenance on late resume
Run `33909833283`, head `3f8dbdf0985b74e5d4901452062ee49364e8048f`, artifact `9950924076`, independently verified ZIP SHA256 `518594fcc23bf7ad793d726e23e7c4b65e02a4cbd0ec6080d877caaff98432c5`.
Raw token: `PASS_EXP073DI_RESTORED_ADAPTER_RUNTIME_PROVENANCE_V0_1`.
If a resumed replica receipt lacks embedded downstream parallelism because selected TE was already a verified checkpoint, the resume-only launcher may use `exact_route/receipt.json` solely as a fallback after exact validation of frozen source head, contract fingerprint, namespace, workspace/full/selected SHA identities, shapes, no-tolerance/no-historical-import flags and exact OpenMP-8 runtime proof. Missing or mismatched persisted adapter provenance is fail-closed and cannot be inferred or recreated.

Current validated resume implementation bindings:
- lineage implementation `ci/exp073bu_wm_s3_fresh_ab_production_v0_5.py`, blob `a0b3f399cb26457c03b57dd16e79245aec4fbca0`;
- thin 8-core resume wrapper `ci/exp073bu_wm_s3_fresh_ab_production_8core_resume_v0_7.py`, blob `d0fd545ef7b1245f21a5d7cba2f3b2eed459d87b`;
- resume-only provenance launcher `ci/exp073bu_wm_s3_science_launcher_8core_resume_v0_4.py`, blob `0026c9607c935b4b2ad90a396cecee735b893738`;
- frozen original science launcher blob `8a725ba135e3e120ce6e8d0db3dd14d95d4ffd6e`;
- exact certified OMP8 adapter blob `63ee393791bba43d3eabbea654efdb9d439d477e`.

## Scientific boundaries unchanged
39 frozen bands, DES NSIDE=4096, ell 0..12287, Wm `TE<-TE`, canonical `<f8 [39,12288]`, exact whole-array SHA256 plus `numpy.array_equal`, eight-worker/OpenMP execution with nested BLAS/MKL/NumExpr threads=1, six checkpoint stages and no tolerance/rounding/smoothing/averaging rescue remain unchanged.

## Next permitted gate
Prospectively bind a **single** self-hosted checkpoint-resume orchestration to the historical science identity and the complete Exp073DE→DI validated repair chain. It must require the old checkpoint root to exist, inventory/validate complete-stage manifests fail-closed, preserve every valid complete stage, and run only the missing work. Before activation, live Actions must show no competing queued/in-progress DSIR self-hosted process. The terminal raw launcher receipt must then be consumed independently; only `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3` may create Wm_S3 authority.
