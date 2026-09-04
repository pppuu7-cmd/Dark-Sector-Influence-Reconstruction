# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

## Current live process
- **DSIR-HOME-PC: currently UNOWNED; the historical Exp073BU checkpoint root is RESERVED FOR CHECKPOINT-PRESERVING RESUME ONLY.** Do not delete, migrate, or reuse it for another experiment.
- Current hosted support gate: `Exp073DI restored adapter runtime provenance v0.1`.
- Workflow: `.github/workflows/exp073di-restored-adapter-runtime-provenance-v0-1.yml`.
- Run/job: `33909833283 / 101143394596`.
- Activation/head: `3f8dbdf0985b74e5d4901452062ee49364e8048f`.
- State at latest reconciliation: `QUEUED`.
- Expected support token: `PASS_EXP073DI_RESTORED_ADAPTER_RUNTIME_PROVENANCE_V0_1`.
- Scientific score: `+0/+0`; this gate cannot create Wm_S3 authority.
- On PASS: consume the raw artifact and independently verify its ZIP digest and bound blobs, then prospectively construct/activate one self-hosted checkpoint-resume orchestration if live Actions show no competing DSIR self-hosted process.
- On FAIL: preserve the support FAIL and diagnose/fix only the first provenance/control-flow defect; no home science resume is permitted.

## Historical science process to resume
- Frozen science workflow: `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-8core-v0-4.yml`.
- Historical run/job: `33901458494 / 101116305364`.
- Run start: `2026-09-04T17:36:14Z`; terminal update `2026-09-04T18:30:00Z`.
- Terminal class: **INFRASTRUCTURE_INCOMPLETE / runner-loss-like termination `+0/+0`**, not scientific FAIL.
- Evidence: science step remained reported `in_progress` while the job/run became terminal `failure`; all following always-evidence/classification steps remained pending; no run artifact exists; job-log blob retrieval returned BlobNotFound. Therefore no terminal A/B comparator exists.
- Frozen science/source head: `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`.
- Original workflow blob: `f8c70a4206321b0dc10b57f63a2a06163da2249a`.
- Original contract fingerprint: `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`.
- Checkpoint root: `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`.
- A/B checkpoint namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`.
- Required science PASS token remains `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`.
- Checkpoint contents have not been numerically inspected for result-dependent tuning. A future self-hosted resume must inventory complete-stage identities and exact payload hashes only, preserve all valid complete stages, and execute only missing work.

## Validated resume-support authority
All are hosted support/readiness `+0/+0` and do not create Wm_S3 authority.
- Exp073DE run `33908858642`, artifact `9950549286`, ZIP SHA256 `4b0f21f407f66659dae89e488c34ab65c56fcf4ce77fb24415272ee44b91b91e`: `PASS_EXP073DE_SPLIT_IDENTITY_RESUME_BINDING_V0_1`.
- Exp073DF run `33909072007`, artifact `9950629085`, ZIP SHA256 `494b5f98242fef972fb632995f3553293ed452a0bc21d9da4168eeb94ca5e8c1`: `PASS_EXP073DF_LEGACY_COMPLETE_RESUME_PASSTHROUGH_V0_1`.
- Exp073DG run `33909299159`, artifact `9950710099`, ZIP SHA256 `75b8837c71f2592c5fbadd5e37ec32159e4f7e47aa7d9807da900f72523cc19f`: `PASS_EXP073DG_BOUNDARY_SAFE_RESUME_V0_1`.
- Exp073DH run `33909572046`, artifact `9950808508`, ZIP SHA256 `e0803731b8c6b76aaf6d1295e9cb9f625355f5ca6258bbb5f0c95652c33182a1`: `PASS_EXP073DH_MASK_WORKSPACE_LINEAGE_RESUME_V0_1`.

Prospective implementation bindings:
- boundary/cumulative-lineage resume driver `ci/exp073bu_wm_s3_fresh_ab_production_v0_5.py`, blob `a0b3f399cb26457c03b57dd16e79245aec4fbca0`;
- 8-core resume wrapper `ci/exp073bu_wm_s3_fresh_ab_production_8core_resume_v0_7.py`, blob `d0fd545ef7b1245f21a5d7cba2f3b2eed459d87b`;
- candidate resume launcher `ci/exp073bu_wm_s3_science_launcher_8core_resume_v0_4.py`, blob `0026c9607c935b4b2ad90a396cecee735b893738` (not authoritative until Exp073DI raw PASS);
- frozen original launcher blob `8a725ba135e3e120ce6e8d0db3dd14d95d4ffd6e`;
- exact certified OMP8 adapter blob `63ee393791bba43d3eabbea654efdb9d439d477e`.

## Execution/science contract preserved
- Exactly 8 outer/OpenMP workers; OpenBLAS/MKL/NumExpr nested threads=1.
- 39 frozen bands; DES NSIDE=4096; ell=0..12287; Wm `TE<-TE`.
- Canonical selected payload `<f8 [39,12288]`.
- Six durable checkpoint stages: `fresh_masks_complete`, `fresh_workspace_mcm_complete`, `mcm_fits_verified`, `full_window_complete`, `selected_te_complete`, `replica_receipt_complete`.
- Terminal equality: whole canonical SHA256 equality AND `numpy.array_equal`.
- No effective ell/z/k, fiducial-P, tolerance, rounding, smoothing, averaging, or preferred-replica rescue.

## Exact next action
Consume Exp073DI terminal raw artifact. Only validated support PASS permits a single prospective self-hosted resume workflow bound simultaneously to the historical science head/fingerprint/checkpoint root and the separately audited repair implementation. Immediately before that activation, verify no competing queued/in-progress DSIR self-hosted run. Only a subsequently validated raw science PASS token may admit Wm_S3 authority.
