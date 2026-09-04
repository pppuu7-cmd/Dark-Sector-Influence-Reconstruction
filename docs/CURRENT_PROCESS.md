# DSIR current-process ledger

Updated: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.

## Current authoritative process
- **DSIR-HOME-PC: RESERVED BY THE SINGLE IN-PROGRESS EXP073DJ / EXP073BU CHECKPOINT-RESUME PROCESS.** Do not start another DSIR self-hosted job.
- Workflow: `.github/workflows/exp073dj-exp073bu-checkpoint-resume-v0-1.yml`.
- Run: `33910213781`.
- Hosted preflight job `101144603730`: **completed SUCCESS**; exact frozen-science/repair binding and self-hosted noncompetition checks passed.
- Self-hosted science-resume job `101144660519`: **IN_PROGRESS** at latest reconciliation.
- Activation/head: `c0f5959b3edb0957cfb14a1d06f7715242d57f48`.
- Historical frozen science/source head: `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`.
- Original contract fingerprint: `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`.
- Historical checkpoint root: `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`.
- A/B namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`.
- Resume implementation head is the activation head above, but historical checkpoint validation remains bound to the old science head/fingerprint; the two identities must never be conflated.
- Expected science PASS token remains exactly `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`.
- Current state: self-hosted runner claimed the job. Steps through exact checkpoint inventory, frozen S3/lens staging, OpenMP-8 downstream compilation and actual 8-thread runtime certification are completed SUCCESS. Active step is `Live exclusivity and checkpoint-preserving Exp073BU A-then-B resume`; evidence/upload/classification steps are still pending.
- Last durable checkpoint: the live job has successfully completed the fail-closed durable checkpoint inventory step. Exact manifest/hash details are not asserted here because decoded active-job logs returned `BlobNotFound`; no partial numerical values were inspected.
- Immutable live reconciliation note: `recovery/2026-09-04_exp073dj_resume_started_checkpoint_inventory_pass.md`, commit `6f76e3ecf40dd0746880a5f8ac1387c8c21b8055`.

## Historical Exp073BU v0.4 terminal state
- Run/job `33901458494 / 101116305364` ended `failure` with the science step still reported `in_progress`, no following always-evidence/classification steps executed and no Actions artifact.
- Classification: **INFRASTRUCTURE_INCOMPLETE / runner-loss-like termination `+0/+0`**, not scientific repeatability FAIL.
- Original workflow blob: `f8c70a4206321b0dc10b57f63a2a06163da2249a`.
- GitHub job-log blob retrieval returned BlobNotFound; no terminal A/B comparator was available from Actions.
- Wm_S3 scientific authority therefore remains absent.

## Validated resume-support authority
All are hosted support/readiness `+0/+0` and do not create Wm_S3 authority.
- Exp073DE run `33908858642`, artifact `9950549286`, independently verified ZIP SHA256 `4b0f21f407f66659dae89e488c34ab65c56fcf4ce77fb24415272ee44b91b91e`: `PASS_EXP073DE_SPLIT_IDENTITY_RESUME_BINDING_V0_1`.
- Exp073DF run `33909072007`, artifact `9950629085`, independently verified ZIP SHA256 `494b5f98242fef972fb632995f3553293ed452a0bc21d9da4168eeb94ca5e8c1`: `PASS_EXP073DF_LEGACY_COMPLETE_RESUME_PASSTHROUGH_V0_1`.
- Exp073DG run `33909299159`, artifact `9950710099`, independently verified ZIP SHA256 `75b8837c71f2592c5fbadd5e37ec32159e4f7e47aa7d9807da900f72523cc19f`: `PASS_EXP073DG_BOUNDARY_SAFE_RESUME_V0_1`.
- Exp073DH run `33909572046`, artifact `9950808508`, independently verified ZIP SHA256 `e0803731b8c6b76aaf6d1295e9cb9f625355f5ca6258bbb5f0c95652c33182a1`: `PASS_EXP073DH_MASK_WORKSPACE_LINEAGE_RESUME_V0_1`.
- Exp073DI run `33909833283`, artifact `9950924076`, independently verified ZIP SHA256 `518594fcc23bf7ad793d726e23e7c4b65e02a4cbd0ec6080d877caaff98432c5`: `PASS_EXP073DI_RESTORED_ADAPTER_RUNTIME_PROVENANCE_V0_1`.

Validated repair blobs:
- `ci/exp073bu_wm_s3_fresh_ab_production_v0_5.py`: `a0b3f399cb26457c03b57dd16e79245aec4fbca0`;
- `ci/exp073bu_wm_s3_fresh_ab_production_8core_resume_v0_7.py`: `d0fd545ef7b1245f21a5d7cba2f3b2eed459d87b`;
- `ci/exp073bu_wm_s3_science_launcher_8core_resume_v0_4.py`: `0026c9607c935b4b2ad90a396cecee735b893738`;
- frozen original launcher: `8a725ba135e3e120ce6e8d0db3dd14d95d4ffd6e`;
- exact certified OMP8 adapter: `63ee393791bba43d3eabbea654efdb9d439d477e`.

## Resume execution contract
- The **existing** historical checkpoint root is mandatory; missing root is BLOCKED, never silently replaced.
- Six stage manifests for each replica must form an ordered prefix and exact-match replica/namespace/frozen science head/original contract fingerprint.
- Every accepted complete payload is hash-verified before resume; verified complete stages are read-only and never recomputed.
- Exactly 8 affinity CPUs are required; `OMP_NUM_THREADS=8`; OpenBLAS/MKL/NumExpr/BLIS/Veclib nested threads=1; runtime downstream must prove `DSIR_OMP_TEAM=8`.
- Resume A to completion, then B, then the unchanged frozen exact comparator.
- Terminal output is written to `terminal_science_receipt_resume_v0_1.json`, leaving any historical terminal receipt untouched.

## Frozen science contract
39 frozen bands; DES NSIDE=4096; ell=0..12287; Wm `TE<-TE`; selected canonical `<f8 [39,12288]`; whole-array SHA256 equality **and** `numpy.array_equal`; no tolerance, rounding, smoothing, averaging, effective ell/z/k, fiducial-P or preferred-replica rescue.

## Exact next action
Track run/job `33910213781 / 101144660519` without duplication. While it remains active, do not inspect partial numerical values or change the frozen gate. When terminal, immediately inspect the raw evidence artifact and classify it under the frozen contract. Only independently validated raw `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3` may admit Wm_S3 authority; exact inequality is scientific FAIL; checkpoint/runner/provenance failures remain infrastructure/BLOCKED `+0/+0` and must preserve valid checkpoints.
