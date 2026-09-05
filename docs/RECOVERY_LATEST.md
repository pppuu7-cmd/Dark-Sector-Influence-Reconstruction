# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-05
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Frozen science boundaries remain unchanged.

## Scientific frontier — Wm_S3 exact PASS admitted
Wm_S1 Track-A exact PASS and admitted Wm_S2 authority remain preserved. **Wm_S3 scientific angular authority is now admitted as exact PASS** from the prospectively frozen Exp073BU A/B gate executed through Exp073DJ checkpoint-preserving resume.

Authoritative science process:
- workflow `.github/workflows/exp073dj-exp073bu-checkpoint-resume-v0-1.yml`;
- run `33910213781`;
- hosted job `101144603730`: SUCCESS;
- self-hosted job `101144660519`: SUCCESS;
- activation head `c0f5959b3edb0957cfb14a1d06f7715242d57f48`;
- frozen science head `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`;
- contract fingerprint `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`;
- historical checkpoint root `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`;
- namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`.

Actions artifact `9959064322`, name `exp073dj-exp073bu-checkpoint-resume-33910213781-c0f5959b3edb0957cfb14a1d06f7715242d57f48`, GitHub digest `sha256:4c9cbebdf4be2e901943a738ebb7df9c1040a6d9524bdd359feb3d3331a647c9`. Independent download produced the identical ZIP SHA256.

The raw `terminal_science_receipt_resume_v0_1.json` was inspected. It records:
- `classification=PASS`;
- raw token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`;
- `science_gate_scored=true` and `wm_s3_authority_created=true`;
- canonical dtype `<f8`, shape `[39,12288]`;
- `whole_canonical_sha256_equal=true` and `numpy_array_equal=true`;
- `no_tolerance_rescue=true`;
- A/B selected-TE SHA256 both `d282ebdf98dc04e41a8c85f487e209634a8324ce7677107112b8abfd1660f749`;
- A/B fresh-PCL SHA256 both `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`;
- A/B workspace-FITS SHA256 both `7f563fb42487261165dc574beb395e552565a634a86f6a46798f0ef33300f0e6`;
- `historical_wm_s3_numerical_import=false`, execution workers=8, PyMaster 2.7.

A/B replica receipts and selected-TE manifests were also inspected and preserve the frozen source/fingerprint/namespaces, `TE<-TE`, `<f8 [39,12288]`, no other-replica output read, no historical Wm_S3 numerical import and no tolerance rescue. Therefore workflow success is not being used as the scientific criterion; the raw frozen comparator and evidence establish the PASS.

Immutable detailed authority: `recovery/2026-09-05_exp073dj_wm_s3_exact_pass_exp073dk_dl_evidence_recovery.md`.

## Historical outcomes preserved
- Exp073CM remains RESOURCE/PERFORMANCE FAIL `+0/+0`, not a Wm_S3 arithmetic FAIL.
- Original Exp073BU v0.4 run/job `33901458494 / 101116305364` remains `INFRASTRUCTURE_INCOMPLETE / runner-loss-like +0/+0`; it produced no terminal comparator.
- Validated checkpoint-resume support chain Exp073DE/DF/DG/DH/DI remains support `+0/+0` and is not rewritten by the later science PASS.

## Terminal evidence support recovery — Exp073DK → Exp073DL
Exp073DK run `33932618320` failed only in hosted static-audit job `101214169930`; self-hosted export `101214196702` was skipped. The first causal log failure was `ValueError: substring not found` inside the static regression harness before any checkpoint-root access. Classification: support/infrastructure failure `+0/+0`; it does not invalidate or rescue Wm_S3 PASS.

Exp073DL was prospectively preregistered as evidence-only support `+0/+0`:
- prereg `experiments/073dl_exp073bu_terminal_payload_evidence_recovery_v0_1_prereg.md`;
- prereg commit/blob `d22a4cddd4675ca3174eb0ba38d8b5cd16ba7296 / 1422fc524ed1a391fa6a0b3a464a2c754fcca01a`.

Two hosted-only Exp073DL attempts (`33934660163`, `33934706167`) failed fail-closed in self-referential static-audit harnesses before self-hosted checkpoint access; export jobs were skipped. The regression was externalized to `ci/exp073dl_evidence_guard_static_test_v0_1.py`, commit `a1dd414f5f4f27f1eed3a4e3020be8e901448e7d`. Current activation commit `c604862f7fe859ae2271b38a0c8148f395317f95` launched run `33934784345`.

Current live process:
- run `33934784345`;
- hosted static-audit job `101220470223`: SUCCESS;
- self-hosted evidence-only job `101220495111`: IN_PROGRESS at latest reconciliation;
- DSIR-HOME-PC is RESERVED BY this single evidence-only process while active;
- no NaMaster/mask/workspace/MCM/PCL recomputation is permitted;
- after the home lock and live noncompetition check it only reads/copies already-terminal A/B `selected_te.bin`, exact-validates provenance/hashes and independently recomputes SHA equality plus `numpy.array_equal`;
- support token is `PASS_EXP073DL_TERMINAL_PAYLOAD_EVIDENCE_RECOVERY_V0_1`;
- Exp073DL cannot create, alter or rescue Wm_S3 scientific authority.

Detailed live ledger: `docs/CURRENT_PROCESS.md`.

## Frozen execution/science contract
Exact band authority remains `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`, 39 bands, ell `0..12287`, full window `[2,39,2,12288]`, selected `wins[0,:,0,:] = TE<-TE`. Exactly 8 affinity CPUs for the frozen heavy architecture; `OMP_NUM_THREADS=8`, nested BLAS/MKL/OpenBLAS/NumExpr/BLIS/Veclib threads=1; runtime must prove the frozen 8-thread downstream. Six durable stages remain `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`.

Frozen science boundaries: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gate
Consume run/job `33934784345 / 101220495111` without duplication. If terminal PASS, independently verify its Actions artifact digest and exported A/B canonical payloads and record Exp073DL as evidence support PASS `+0/+0`. If it fails/BLOCKS, diagnose the first support/infrastructure cause and preserve the already-admitted Wm_S3 PASS and checkpoints. After terminal evidence support is consumed, advance to the next prospectively permitted DSIR scientific gate from the Wm_S3-closed frontier; do not create a competing home job while Exp073DL is active.
